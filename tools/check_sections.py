#!/usr/bin/env python3
"""Section-completeness auditor for rating rationales (CLAUDE.md Step 17 / failure mode 19).

WHY THIS EXISTS: on 11-13 Aug 2026 the mandatory ESG / Environmental-and-social section was
omitted from four consecutive CRISIL rationales even though SKELETON.md required it AND a peer
report read in the same session contained one. Written guidance had already failed to prevent
the miss, so this is a MECHANICAL check rather than another rule to remember.

DESIGN NOTES (learned by getting v1 wrong on 13-Aug-2026 - both directions):
  * Match SECTION HEADERS ONLY (^#+ ...). v1 searched whole body text and gave a FALSE PASS on
    a report that merely mentioned "environmental and social" in a criteria list while having
    no such section. A false pass is worse than a false alarm.
  * Accept ALL THREE agencies' wordings for the same section - ICRA "Liquidity position: X" /
    "Rating sensitivities", CareEdge "Key strengths" / "Key weaknesses", CRISIL "Key Rating
    Drivers - Strengths" / "ESG Profile". v1 flagged correct ICRA and CareEdge reports.
  * Outlook is CONDITIONAL, not mandatory: short-term-only mandates (e.g. a CP-only rating)
    correctly carry no outlook per the outlook policy. Suppress when the report says so.

USAGE
    python check_sections.py                 # audit every rationale in the project root
    python check_sections.py <file.md> ...   # audit specific files
Exit 1 if any MANDATORY section is missing, or if any BLOCKING probe fires (see
BLOCKING_PROBES) - so it can gate a delivery. Every other probe is a WARN: it prints
and the case still passes.
"""
import json

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.
HEADER_RE = re.compile(r"^\s{0,3}#{1,6}\s*(.+?)\s*$", re.M)


def headers(text: str):
    """All markdown header lines, stripped of bold/underline/emphasis markup.

    NB: strip whole HTML tags FIRST. Stripping the raw characters < > / first turns
    '<u>Liquidity:</u>' into 'u liquidity: u' and the leading 'u' breaks '^liquidity'
    anchors - that bug produced two false positives on 13-Aug-2026.
    """
    out = []
    for h in HEADER_RE.findall(text):
        h = re.sub(r"</?[a-zA-Z][^>]{0,20}>", "", h)   # whole tags: <u>, </u>, <sup> ...
        h = re.sub(r"[*_`\\]", "", h)                  # emphasis markers
        out.append(h.strip().lower())

    # CRISIL opens with the rating action as a BOLDED TABLE-HEADER CELL - "|**Rating Action**||" -
    # not a markdown header. Header-only matching therefore failed CRISIL's own published
    # rationale for State Bank of India (05-Mar-2026) on a section that is plainly present.
    # Verified 14-Aug-2026 by running this checker against that reference file.
    for cell in re.findall(r"^\s*\|\s*\*\*(.+?)\*\*\s*\|", text, re.M):
        cell = re.sub(r"</?[a-zA-Z][^>]{0,20}>", "", cell)
        out.append(re.sub(r"[*_`\\]", "", cell).strip().lower())
    return out


def detect_agency(path: Path, text: str) -> str:
    """CRISIL / CareEdge / ICRA - section names differ materially between them.

    Reads the HEADLINE only (the report's own bracket/house-style notation - "[ICRA]AA",
    "Crisil AA+/Stable", "CARE AA+; Stable"), not any mention of an agency name anywhere in
    the opening text. A bare substring scan of the first 3000 characters previously
    misdetected an ICRA report as CRISIL because its Summary-of-rating-action footnote (a
    CLAUDE.md Step 14 divergence disclosure) discussed a peer-agency CRISIL rationale at
    length - the false positive then demanded a CRISIL-only "Outlook" header an ICRA-format
    report correctly omits. The headline is the report's OWN declared agency and is a much
    narrower, more reliable signal than "does this word appear anywhere nearby".
    """
    head = text[:800]
    if re.search(r"\[ICRA\]", head):
        return "ICRA"
    if re.search(r"\bCrisil\s+[A-Z]", head) or re.search(r"'Crisil\b", head, re.I):
        return "CRISIL"
    if re.search(r"\bCARE\s+[A-Z]{2,3}[+-]?\b", head) or re.search(r"CareEdge", head, re.I):
        return "CareEdge"
    # fall back to the old broad scan only if the headline itself is inconclusive
    blob = (path.name + " " + head).lower()
    if "crisil" in blob:
        return "CRISIL"
    if "careedge" in blob or "care ratings" in blob or "care rating" in blob:
        return "CareEdge"
    return "ICRA"


# label -> (regexes matched against HEADERS, mandatory)
# mandatory flag: True | False | None (=conditional) | "CRISIL" (=mandatory for that agency only)
SECTIONS = [
    ("Rating action",              [r"^rating action", r"summary of rating action",
                                    r"rationale and key rating drivers"], True),
    ("Detailed rationale",         [r"detailed rationale", r"^rationale\b", r"rationale and key rating drivers"], True),
    ("Key drivers - strengths",    [r"strengths?$", r"drivers?\s*[-—:].*strength", r"^key strengths",
                                    r"credit strengths", r"description of key rating drivers"], True),
    ("Key drivers - weaknesses",   [r"weakness", r"^key weaknesses", r"credit challenges",
                                    r"description of key rating drivers"], True),
    ("ESG / Environmental+social", [r"^esg\b", r"esg profile", r"esg highlights",
                                    r"environmental and social", r"environment.*social"], True),
    ("Liquidity + descriptor",     [r"^liquidity", r"liquidity position", r"liquidity:"], True),
    ("Rating sensitivities",       [r"sensitivit"], True),
    ("About the company",          [r"^about the", r"^about\b"], True),
    # "Brief Financials" is CareEdge's own name for this table - it appears that way in 480 of the
    # published CareEdge rationales in the reference library and never as "key financial
    # indicators". Omitting it failed a correct report on 19-Aug-2026.
    ("Key financial indicators",   [r"key financial", r"financial indicators", r"financial performance",
                                    r"financial risk profile", r"annexure.*financial",
                                    r"brief financials"], True),
    ("Annexure - instruments",     [r"annexure.*instrument", r"instrument details", r"details of instrument",
                                    r"annexure-?1", r"annexure - 1"], True),
    # ICRA embeds the outlook in the headline + closing rationale paragraph and has NO separate
    # Outlook header (see CLAUDE.md S7 mandatory section order). CRISIL uses a dedicated header.
    ("Outlook (CRISIL format)",    [r"^outlook"], "CRISIL"),
    ("Complexity level",           [r"complexity"], False),
    ("Analytical approach",        [r"analytical approach"], False),
    ("Entities consolidated",      [r"entities consolidated", r"list of entities"], False),
    ("Rating history",             [r"rating history"], False),
]

NO_OUTLOOK_RE = re.compile(
    r"no outlook is assigned|outlooks? (are|is) not assigned|short[- ]term rating[s]? only"
    r"|not applicable.{0,20}outlook", re.I)


def _strip_masthead(t: str) -> str:
    """Drop a standalone 'Press Release' masthead line before the FM14 date check.

    CareEdge's house format opens EVERY rationale with a bare "Press Release" line, so the
    FM14 trigger (which looks for "press release" as an attribution to another CRA's
    publication) fired on the masthead of a correctly dated report and could never be
    satisfied - the masthead sits alone on its line, so no date can follow it on that line.
    Every CareEdge-format report would have failed this probe forever. Only a STANDALONE
    line is stripped; "...per CareEdge's press release of 09-Oct-2025" is untouched, which
    is the case the probe actually exists to police.
    """
    return re.sub(r"^\s*#*\s*press release\s*$", "", t, flags=re.I | re.M)


_CRA_TRIGGER_RE = re.compile(r"CRA[- ]published|press release", re.I)
_MONTHS = r"jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec"
_DATE_RE = re.compile(
    r"\d{1,2}[- ](?:" + _MONTHS + r")[a-z]*[- ,]{1,2}\d{2,4}"      # 09-Oct-2025
    r"|(?:" + _MONTHS + r")[a-z]*[- ]\d{1,2},?\s*\d{4}"            # October 09, 2025
    r"|\d{4}-\d{2}-\d{2}", re.I)                                   # 2025-10-09


def _cra_amounts_dated(t: str) -> bool:
    """FM14 condition (2): a CRA-published amount must carry that publication's DATE.

    Looks BOTH WAYS around each attribution, within 200 characters. The first version looked
    only FORWARD and only within a single line, which failed a correctly dated report on
    26-Aug-2026 whose sentence reads "...published rating action dated October 09, 2025 ...
    the amounts are CRA-published and not issuer-confirmed". The date was stamped beside the
    attribution exactly as the rule requires - just before it rather than after. "Beside"
    includes before.

    EVERY attribution must be dated, not merely one of them: a report that dates its first
    reference and then attributes a second, older table undated is precisely the staleness
    this guards against.
    """
    s = _strip_masthead(t)
    hits = list(_CRA_TRIGGER_RE.finditer(s))
    if not hits:
        return True
    return all(_DATE_RE.search(s[max(0, m.start() - 200): m.end() + 200]) for m in hits)


_PLACEHOLDER_RE = re.compile(r"\[ANALYST:\s*([^\]]{0,90})", re.I)


def _unfilled_placeholders(t: str):
    """build_rationale.py emits [ANALYST: ...] for every judgement it cannot make.

    Those placeholders are the whole safety mechanism of the generator: it fills every FIGURE
    from the verified engine and marks every JUDGEMENT. If a draft could pass the delivery
    gate with them still in it, the generator would be a way to ship a skeleton that merely
    LOOKS complete - numbers everywhere, analysis nowhere - which is worse than having no
    generator at all. So an unfilled placeholder is a hard delivery failure.
    """
    return [m.group(1).strip() for m in _PLACEHOLDER_RE.finditer(t)]


def _section_body(text: str, pattern: str, span: int = 4000) -> str:
    m = re.search(r"^\s{0,3}#{1,6}\s*[^\n]*" + pattern + r"[^\n]*$", text, re.I | re.M)
    return text[m.end(): m.end() + span] if m else ""


ABSENCE_RE = re.compile(
    r"\b(not (available|extractable|disclosed|obtainable|determinable|found|present)"
    r"|could not be (established|constructed|determined|found|extracted)"
    r"|no .{0,40}(was|were) (available|disclosed|found)"
    r"|absent from the (document|documents|supplied))\b", re.I)

# an absence-claim is only legitimate if the report SHOWS the search that proves it
EVIDENCED_RE = re.compile(
    r"(grep|searched|search of|zero hits|no hits|0 hits|pattern[s]? .{0,30}return|"
    r"searched-and-absent|not extracted in this pass)", re.I)

# Triggers must identify the ENTITY's sector, not incidental words ("bank facilities" is not
# a bank). KPI must appear WITH A NUMBER - a passing mention ("tenancy base") is not the metric.
SECTOR_KPI = {
    r"telecom tower|tower (company|operator|business)|co-location":
        (r"tenancy ratio|sharing ratio|sharing factor", "tenancy / sharing ratio"),
    r"forging|forged and machined":
        (r"capacity utilisation|capacity utilization", "capacity utilisation"),
    r"zinc|integrated (zinc|metal)|smelter|mined metal":
        (r"cost of production|per tonne|/tonne", "cost of production per tonne"),
    r"cement (manufactur|producer|plant)":
        (r"capacity utilisation|ebitda ?/ ?tonne", "capacity utilisation or EBITDA/tonne"),
    r"\bdistributor\b|distribution business|trading compan":
        (r"receivable days|gca days", "receivable / GCA days"),
    r"hotel[s]? (compan|chain|propert|and resort)"
    r"|hospitality (compan|business|player|major)|owns and operates .{0,40}hotel":
        (r"revpar|occupancy", "RevPAR or occupancy"),
    # Sugar added 13-Sep-2026. Dhampur Bio Organics shipped with CAPACITY (TCD) and no
    # THROUGHPUT. Capacity is a static licence figure; cane crushed is what actually moved -
    # 41.44 -> 34.98 -> 32.92 lakh tonne, a 20.6% two-year decline, sitting in a clean table in
    # the issuer's own annual report. Sugar output still ROSE, 3.10 -> 3.54 lakh tonne, on
    # better recovery - the operating story the report never told (failure mode 21).
    # THROUGHPUT ONLY in the alternation. The first draft of this entry also accepted
    # "recovery" and "realisation", and the Dhampur report passed it - because it DID quote
    # recovery. Accepting a softer metric lets the missing one through, which is the whole
    # defect. Recovery and realisation belong in the report; the gate binds on the one that
    # was actually absent.
    # The UNIT is the discriminator, and getting it wrong is how the first two drafts of this
    # entry passed the very report that motivated it. Throughput is quoted in LAKH TONNE;
    # capacity is quoted in TCD. An earlier pattern included "cane crush", which matched
    # "cane crushing" - i.e. the capacity sentence - and waved the report through.
    r"\bsugar\b|sugarcane|\bcane\b|distillery|molasses":
        (r"cane crushed|lakh (tonne|ton)|lac (tonne|ton)",
         "cane crushed / crushing THROUGHPUT in lakh tonne. TCD is a licence figure, not an "
         "operating metric - Dhampur's throughput fell 41.44 -> 34.98 -> 32.92 lakh tonne "
         "while its TCD number sat still"),
    # Broking added 20-Aug-2026: a broking company is defined by TURNOVER and CLIENT COUNT,
    # not by lending or manufacturing metrics. Without this trigger an HDFC Securities
    # rationale would pass the gate with no sector metric at all (failure mode 28).
    r"broking (compan|house|firm|business|arm|major)"
    r"|brokerage (firm|house|business)|stock ?brok|securities broking":
        (r"average daily turnover|\badto\b|active client|market share",
         "average daily turnover / active clients"),
    # Entity-descriptive bank phrases only. "bank facilities"/"bank limits" is a corporate
    # borrowing a bank's money, not a bank - those must never trigger. Widened 14-Aug-2026:
    # the original set missed "is a scheduled commercial bank" / "India's largest bank",
    # so a bank rationale silently skipped the KPI rule.
    # NBFC / HFC listed FIRST and separately. Ind AS NBFC statements say "Stage III" in ECL
    # tables, never "GNPA" - and NBFCs report AUM and CAR where banks report NIM and CASA.
    # Requiring bank vocabulary of an NBFC report warned on a correct v2 rationale that
    # quantified stage III at 0.85% and CAR at 22.26% (NABKISAN, 19-Aug-2026).
    r"\bnbfc\b|non-banking financial compan|housing finance compan":
        (r"stage 3|stage iii|\bgnpa\b|\bcrar\b|capital adequacy|\baum\b|"
         r"assets under management",
         "Stage III / AUM / CRAR (an NBFC says 'Stage III', never 'GNPA')"),
    r"is a bank|banking compan|deposit franchise"
    r"|scheduled commercial bank|public sector bank|private sector bank|commercial bank"
    r"|largest bank|bank in india|small finance bank|payments bank":
        (r"\bnim\b|gnpa|crar|cet-?1", "NIM / GNPA / CRAR"),
    # ---- Infrastructure sub-sectors, added 06-Sep-2026 from criteria-for-infrastructure-
    # sectors.md. Each metric is the one CRISIL says the asset class actually turns on, and
    # each is one a report cannot omit without reading as written from outside the sector
    # (failure mode 21). Verified by tools/test_infra_kpi.py, which caught two real bugs in
    # the first version of this block: every word boundary had been silently stripped, and
    # the renewable trigger fired on a CHEMICALS manufacturer whose ESG paragraph mentioned
    # a captive solar plant - because _section_body reads 1800 characters from "About the",
    # which on a short report runs past the section. The triggers below therefore require
    # entity-shaped language (SPV / special purpose vehicle / IPP) near the technology word,
    # not the technology word alone.
    #
    # Renewables: CRISIL computes DSCR on the P90 PLF, never P50 - "the PLF level that a
    # wind turbine is 90% likely to exceed in a given year". Estimation SD is 2-3% for solar
    # against 4-6% for wind, which is why the seasonality liquidity floor is ~2 months of
    # debt obligation for solar and at least 4 months for wind.
    r"(?:solar|wind)[^.]{0,60}(?:spv|special purpose vehicle)"
    r"|(?:spv|special purpose vehicle)[^.]{0,60}(?:solar|wind)"
    r"|independent power producer|\bipp\b":
        (r"\bp90\b|\bplf\b|plant load factor|capacity utilisation factor|\bcuf\b",
         "P90 PLF (CRISIL computes renewable DSCR on the P90, never the P50 - a DSCR quoted "
         "without its PLF basis is not a CRISIL DSCR)"),
    # Transmission: line availability is the operating metric, banded - charges cut below an
    # upper threshold (~98%), penalty below a lower one (~95%), incentive above. Most
    # operational assets run 99%+.
    r"transmission (?:project|licensee|spv|system)|inter-?state transmission"
    r"|\bists\b|transmission service agreement":
        (r"line availability|availability factor|transmission availability",
         "line availability (CRISIL bands it: charges cut below ~98%, penalty below ~95%, "
         "incentive above; operational assets typically run 99%+)"),
    # Toll roads: revenue is traffic x toll rate. CRISIL notes traffic "was highly
    # overestimated" in many past cases and always runs a traffic sensitivity.
    r"toll road|toll (?:collection|plaza|revenue)|build-?operate-?transfer"
    r"|toll-?operate-?transfer":
        (r"traffic|\bpcu\b|toll rate",
         "traffic volume and toll rate - the two terms of toll revenue"),
    # Annuity / HAM: no demand or price risk, so the rating turns on DSCR and the annuity
    # receipt record. CRISIL states three times that this DSCR EXCLUDES parent support and
    # DSRA - see CRISIL_INFRASTRUCTURE_CONVENTIONS.md S2.
    r"annuity road|hybrid annuity|\bham\b (?:project|road|model)"
    r"|annuity (?:project|spv)":
        (r"\bdscr\b|annuity receipt|annuity payment",
         "DSCR and the annuity receipt track record (CRISIL's DSCR here excludes parent "
         "support and DSRA)"),
    # ---- CRISIL corporate sectors, added 13-Sep-2026 from criteria-for-manufacturing-
    # trading-and-corporate-services-sector.md, read in full. That one file publishes the
    # defining operating metrics for 22 industries; SECTOR_KPI held entries for six of them,
    # so failure mode 21 was UNENFORCED for most of the delivered corpus - steel, pharma,
    # tyres, FMCG, E&P, textiles, IT services and speciality chemicals all shipped with no
    # sector-metric gate at all. Each metric below is the one CRISIL names as defining for
    # that industry, narrowed to metrics a rationale cannot omit without reading as written
    # from outside the sector. Controls: tools/test_sector_kpi_crisil.py.
    #
    # Triggers are entity-shaped on purpose. The renewable bug of 06-Sep-2026 - a chemicals
    # manufacturer matched on "solar" because _section_body reads 1800 chars from "About the"
    # and ran past the section on a short report - is the standing hazard for every entry here.
    r"pharmaceutical[s]? (compan|business|player|major|manufactur|firm|segment)"
    r"|manufactur\w* .{0,40}active pharmaceutical ingredient"
    r"|\bapi\b (manufactur|business|player)":
        (r"usfda|us fda|\bdpco\b|\bnlem\b|r&d (spend|expense|cost)|regulated market",
         "USFDA facility status / DPCO-NLEM price-controlled share / R&D spend - the three "
         "named pharma drivers (over a fifth of the Indian market by value is price-"
         "controlled, so the uncovered share is a margin fact, not a footnote)"),
    r"\btyre[s]? (manufactur|business|compan|maker)"
    r"|auto ?component|automotive component|auto ancillar":
        (r"replacement (market|segment|demand)|aftermarket|capacity utilisation"
         r"|capacity utilization|content per vehicle",
         "OEM vs replacement/aftermarket mix and capacity utilisation - CRISIL rates the "
         "aftermarket as more profitable and less price-pressured, so the mix IS the margin "
         "story; content per vehicle is the other named metric"),
    r"steel (manufactur|producer|plant|maker|compan)|integrated steel"
    r"|stainless steel|crude steel|\bsteelmak":
        (r"capacity utilisation|capacity utilization|crude steel production"
         r"|saleable steel|value[- ]added",
         "capacity utilisation / crude steel volume / value-added share - the named steel "
         "efficiency metrics are coke rate, blast-furnace productivity, continuous-cast "
         "share and production yield; at minimum the throughput and the value-added mix"),
    r"speciality chemical[s]? (compan|business|player|manufactur|major)"
    r"|specialty chemical[s]? (compan|business|player|manufactur|major)"
    r"|chemical[s]? (manufactur|business|player|compan)"
    r"|chemical intermediate|agrochemical (manufactur|compan|business|player)":
        (r"capacity utilisation|capacity utilization",
         "capacity utilisation - CRISIL assesses chemicals on speciality-vs-bulk mix, cost "
         "against the GLOBAL weighted average and bottom-of-cycle global prices, integration "
         "and export share; utilisation is the one that is always quotable"),
    r"\bfmcg\b (compan|business|major|player|firm)"
    r"|fast[- ]moving consumer goods (compan|business|major|player)"
    r"|consumer goods (compan|business|major)"
    r"|consumer durable[s]? (manufactur|compan|maker|business)":
        (r"market share|distribution reach|\boutlets\b|advertis|new (product|brand)",
         "market share (CRISIL requires it by VALUE and by VOLUME), distribution reach and "
         "the revenue share of brands launched in the past 3-5 years - the named innovation "
         "metric for FMCG and consumer durables alike"),
    r"oil and gas exploration|upstream oil"
    r"|exploration and production (compan|business|player|major)"
    r"|\be&p\b (compan|business|player|major)":
        (r"reserve replacement|proven reserve|\b[12]p\b reserve|production cost"
         r"|per barrel|\bboe\b|reserve[- ]to[- ]production",
         "reserve replacement (measured as FD&A cost averaged over 3-5 years), the developed "
         "share of proven reserves, and all-inclusive production cost per barrel"),
    r"textile[s]?|spinning mill|cotton yarn|terry towel|home textile|\bdenim\b":
        (r"capacity utilisation|capacity utilization|\bcount[s]?\b|spindle",
         "capacity utilisation and the COUNT RANGE - finer counts are less price-elastic, "
         "cotton is the single largest cost, and power is 8-10% of operating income for "
         "spinning"),
    r"software (services|development|product) (compan|business|firm|player)"
    r"|\bit services (compan|business|player|provider|firm)"
    r"|information technology (services|enabled)|\bbpo\b"
    r"|technology services (compan|provider|business)":
        (r"attrition|utilisation rate|utilization rate|revenue per employee|offshore"
         r"|client concentration",
         "employee utilisation, attrition and revenue per employee - the named IT metrics, "
         "with offshore-onshore mix and top 5-10 client concentration"),
    r"mobile (telephony|services|operator|network)|telecom (operator|service provider)"
    r"|wireless subscriber|cellular services":
        (r"\barpu\b|average revenue per user|subscriber (base|market share|addition)|churn",
         "ARPU, subscriber and revenue market share, share of NET subscriber additions, and "
         "churn - the postpaid mix is treated as a positive (higher ARPU, stickier)"),
    r"engineering (compan|business|services|goods)|capital goods"
    r"|\bepc\b (contract|player|compan|business)|defence (manufactur|psu|equipment)"
    r"|aerospace|construction (compan|business)|civil construction":
        (r"order book|order backlog|book[- ]to[- ]bill|order inflow",
         "order book and book-to-bill - for construction CRISIL states outright that "
         "conventional ratio analysis is often NOT sufficient and moves to a CASH-based "
         "analysis, weighting order-book quality by project stage"),
    r"aluminium|alumina refinery|\bsmelter\b (business|compan)":
        (r"cost of production|per tonne|/tonne|specific (power |energy )?consumption"
         r"|capacity utilisation",
         "cost of production per tonne and specific consumption - power is ~35% of aluminium "
         "production cost, so the integration and power position IS the credit"),
    r"paper (mill|manufactur|business)|writing and printing paper"
    r"|paperboard[s]? (mill|manufactur)|\bpulp (mill|manufactur)":
        (r"capacity utilisation|capacity utilization|per tonne|realisation",
         "capacity utilisation and realisation per tonne - note the counter-intuitive rule "
         "that LESS integration is better in a downturn (lower fixed-cost intensity)"),
    r"fertiliser|fertilizer|\burea\b (manufactur|plant|business)":
        (r"capacity utilisation|energy consumption|subsidy",
         "energy consumption against the NPS group norms (urea), capacity utilisation, and "
         "the subsidy receivable, which drives the working-capital cycle"),
    r"organised retail|retail chain|retail (stores|outlets|format)|multi[- ]?brand outlet":
        (r"same[- ]store|like[- ]to[- ]like|revenue per square|footfall|private label",
         "same-store/like-to-like sales growth, revenue per square foot, and the share of "
         "stores at breakeven with time-to-breakeven for new stores"),
    r"petrochemical[s]? (compan|business|player|major|complex)"
    r"|naphtha cracker|polymer (manufactur|business)":
        (r"operating rate|capacity utilisation|capacity utilization",
         "operating rate (capacity utilisation) and feedstock security - government-"
         "controlled gas pricing is a named competitive advantage against naphtha"),
    r"two[- ]?wheeler (manufactur|oem|maker)|commercial vehicle (manufactur|oem|maker)"
    r"|tractor (manufactur|maker)|passenger vehicle manufactur":
        (r"market share|channel inventory|capacity utilisation|capacity utilization",
         "market share and CHANNEL INVENTORY - CRISIL singles out channel inventory as the "
         "measure that reveals true retail demand behind wholesale despatches"),
    r"educational institut|\buniversity\b|engineering college|school (chain|network)"
    r"|education (trust|society|business)":
        (r"occupancy|seat utilisation|enrol",
         "occupancy / seat utilisation, plus the education-specific Adjusted DSCR = "
         "((NCA - NCA used for capex) + Interest) / (Interest + Repayment)"),
    r"iron ore mining|coal mining|mining (compan|business|operation)":
        (r"stripping ratio|overburden|reserve|production cost|per tonne",
         "stripping/overburden ratio, proven and probable reserves, reserve replacement and "
         "mine life, and cost per tonne against domestic AND international peers"),
    r"real[- ]estate develop|residential (project|development|real estate)"
    r"|property development|realty (compan|business)":
        (r"bookings|collections|sales value|area sold|committed receivable",
         "bookings, collections and committed receivables - CRISIL does NOT rate a developer "
         "on accrual coverage or ordinary gearing; see CRISIL_REAL_ESTATE_CONVENTIONS.md for "
         "the CFO-based ratio set it actually publishes (failure mode 60)"),
}


def _absence_claims_unevidenced(t: str):
    """Absence-claims not backed by a shown search.

    A Correction Note QUOTES the false claims it is retracting; those quotations are not
    new assertions, so text from a correction/retraction section onward is excluded, as is
    any match sitting inside quotation marks.
    """
    body = t
    cut = re.search(r"^\s{0,3}#{1,6}\s*.*correction note", t, re.I | re.M)
    if cut:
        body = t[: cut.start()]
    out = []
    for m in ABSENCE_RE.finditer(body):
        seg = body[max(0, m.start() - 120): m.end() + 120]
        if re.search(r'["“”]', seg[:130]) and re.search(r'["“”]', seg[130:]):
            continue                                   # inside a quotation
        window = body[max(0, m.start() - 400): m.end() + 400]
        if not EVIDENCED_RE.search(window):
            out.append(body[max(0, m.start() - 60): m.end() + 60].replace("\n", " ").strip())
    return out[:4]


# ---- failure mode 60: CRISIL publishes a CFO-BASED ratio set for real-estate developers, and
# this project was assessing them on accrual coverage and ordinary gearing instead. That is the
# root cause behind FM40/Godrej Properties, where an accrual interest-coverage hard cap
# manufactured nine of twelve notches of apparent divergence. FM40's recorded remedy - allow the
# cap to be disapplied in writing - treated the symptom. The cause was using the wrong ratios.
_RE_DEVELOPER_RE = re.compile(
    r"real[- ]estate develop|residential (?:project|development|real estate)"
    r"|property development|realty (?:compan|business)", re.I)
_ACCRUAL_RATIO_RE = re.compile(r"interest coverage|gearing|debt[ /]?to[ /]?equity", re.I)
# Any ONE of these shows the CRISIL developer framework was actually used.
_CFO_RATIO_RE = re.compile(
    r"\bcfo\b|cash flow from operation|cash buffer|committed receivable"
    r"|debt[ /]*to[ /]*cfo|debt[ /]cfo|collections?\b", re.I)


def _real_estate_wrong_ratio_set(t: str):
    """A residential/commercial-for-sale developer assessed on accrual coverage alone.

    CRISIL rates a developer on CFO (adjusted) = collections - construction cost - other
    operating expenses - JV/JDA outflows, and on Debt/CFO, CFO/interest, the cash buffer ratio
    and the adequacy of committed receivables. Leverage enters only as a structural anchor
    inside financial flexibility. Commercial-for-LEASE is assessed on DSCR instead, so a report
    that quotes DSCR is on a legitimate alternative track and is not flagged.
    """
    low = t.lower()
    about = _section_body(low, r"about the", span=1800) or low[:1500]
    if not _RE_DEVELOPER_RE.search(about):
        return None
    if re.search(r"\bdscr\b|lease rental discount|\blrd\b", low):
        return None                      # the lease/LRD track, correctly on DSCR
    if _CFO_RATIO_RE.search(low):
        return None                      # the developer framework was used
    m = _ACCRUAL_RATIO_RE.search(low)
    if not m:
        return None
    return low[max(0, m.start() - 60): m.end() + 60].replace("\n", " ").strip()


# ---- failure mode 61: a global-scale rating is NOT a national-scale rating, and the gap is
# large. CRISIL states a foreign parent's global-scale rating "tends to map to a rating on the
# Crisil Ratings scale which is typically 6 to 7 NOTCHES HIGHER" (S&P BBB+ -> Crisil AAA/AA+;
# S&P BB+ -> Crisil AA-/A+; S&P B -> Crisil BB+/BB), narrowing at the lower end. Using the
# parent's S&P grade directly in a support assessment understates the parent by 6-7 notches.
_GLOBAL_CRA_RE = re.compile(r"s&p|standard (?:and|&) poor|moody|fitch", re.I)
_PARENT_CTX_RE = re.compile(
    r"parent|promoter group|sponsor|holding compan|group support|ultimate parent"
    r"|support from|guarantor", re.I)
_MAPPED_RE = re.compile(
    r"national scale|global scale|mapp(?:ed|ing)|notch(?:es)? higher|6 to 7|six to seven"
    r"|not comparable|different scale", re.I)


def _global_scale_unmapped(t: str):
    """A foreign CRA's rating cited near parent/support language with no mapping statement."""
    low = t.lower()
    if _MAPPED_RE.search(low):
        return None                      # the scale difference is addressed somewhere
    for m in _GLOBAL_CRA_RE.finditer(low):
        window = low[max(0, m.start() - 220): m.end() + 220]
        if _PARENT_CTX_RE.search(window):
            return low[max(0, m.start() - 70): m.end() + 70].replace("\n", " ").strip()
    return None


def _missing_sector_kpi(t: str):
    """Sector trigger is read from the ABOUT-THE-COMPANY section only - that is where the
    entity's own business is defined. Reading triggers from the whole document produced a
    false positive on a diversified issuer whose report merely mentioned the demerger of a
    hotels business. The KPI itself may appear anywhere, but must carry A NUMBER within
    ~120 chars - a passing mention ("tenancy base") is not the metric.
    """
    low = t.lower()
    about = _section_body(low, r"about the", span=1800) or low[:1500]
    for trigger, (kpi_re, label) in SECTOR_KPI.items():
        if not re.search(trigger, about):
            continue
        quantified = any(re.search(r"\d", low[m.start(): m.end() + 120])
                         for m in re.finditer(kpi_re, low))
        if quantified:
            return None          # sector identified AND its metric is present - stop looking
        return label + (" (mentioned but not quantified)"
                        if re.search(kpi_re, low) else " (absent)")
    return None


_AMT_RE = re.compile(r"(?:rs\.?|₹)?\s*\*{0,2}\s*([\d,]+\.\d{2})\s*\*{0,2}", re.I)


def _line_integrity_breaks(t: str):
    """FM12/23. Annexure I lines must SUM to the total they sit under.

    An invented or mis-split facility line is invisible to every other check - the report reads
    correctly and the arithmetic is simply wrong. This was verified BY HAND on HDFC Securities
    (13,860.00 + 6,140.00 = 20,000.00), and hand-arithmetic is precisely what should not be
    manual. Walks the instrument annexure, and for each row whose label says "total", compares
    it against the sum of the component rows since the previous total.
    """
    m = re.search(r"^\s{0,3}#{1,6}[^\n]*annexure[^\n]*(instrument|facilit)[^\n]*$",
                  t, re.I | re.M)
    if not m:
        return []
    body = t[m.end(): m.end() + 9000].split("\n## ")[0]
    out, run = [], []
    for line in body.split("\n"):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or set("".join(cells)) <= set("-: "):
            continue
        label = re.sub(r"[*_`]", "", cells[0]).strip()
        amts = [float(a.replace(",", "")) for c in cells[1:] for a in _AMT_RE.findall(c)]
        if not amts:
            continue
        value = amts[-1]                      # size column is the last numeric cell
        if re.search(r"\btotal\b", label, re.I):
            if len(run) >= 2 and abs(sum(run) - value) > 0.02:
                out.append(f'"{label[:44]}" states {value:,.2f} but its {len(run)} lines '
                           f'sum to {sum(run):,.2f} (out by {value - sum(run):,.2f})')
            run = []
        else:
            run.append(value)
    return out


def _rating_table_uses_outstandings(t: str):
    """FM31. The Rating Action table carries SANCTIONED/RATED LIMITS, never drawn balances.

    A rated limit is almost never in an annual report - it lives in the CRA press release - so
    failing to find one is the EXPECTED state, not licence to substitute an outstanding.
    (HDFC Securities, 20-Aug-2026: CP outstanding of Rs 12,931.33 cr was tabled against a
    published rated programme of Rs 20,000.00 cr.)  Only the head of the report is searched:
    outstandings are legitimate in Brief Financials and the liquidity section.
    """
    # Require the AMOUNT ITSELF to be the outstanding. A report that states the rated limit and
    # merely annotates it - "5,000.00 (nil outstanding as on Mar 31, 2026)" - is doing exactly
    # the right thing and must not be flagged (JSW Steel, false positive caught 20-Aug-2026).
    head = t[:6000]
    amt = r"(?:rs\.?|₹)\s*\*{0,2}[\d,]+(?:\.\d+)?\s*\*{0,2}\s*(?:crore|cr\b)\*{0,2}"
    m = re.search(amt + r"\s*\*{0,2}\s*outstanding as (?:on|at)", head, re.I)
    return t[max(0, m.start() - 55): m.end() + 30].replace("\n", " ") if m else None


def _no_outlook_contradicted(t: str):
    """FM31. 'No outlook is assigned' cannot stand beside a long-term rating carrying one."""
    if not re.search(r"no outlook is assigned|outlooks? (are|is) not assigned", t, re.I):
        return None
    m = re.search(r"\b(AAA|AA[+-]?|A[+-]?|BBB[+-]?)\s*;\s*(Stable|Positive|Negative)", t)
    return m.group(0) if m else None


def _networth_basis_unstated(t: str) -> bool:
    """FM32. A financial-sector report quoting gearing or RONW must name its net-worth basis.

    CareEdge uses TANGIBLE net worth (equity less DTA and intangibles) and includes non-fund-based
    limits in gearing; using total equity silently produced 4.20x against a published 4.64x.
    """
    if not re.search(r"gearing|return on net.?worth|\bRONW\b|RoNW", t, re.I):
        return False
    # "Financial Sector" also names a CRITERIA DOCUMENT ("Financial Ratios - Financial Sector"),
    # which every CareEdge corporate report lists - that string fired on a sugar company and an
    # FMCG company (20-Aug-2026). Read the entity's sector from the about-section only, and use
    # entity-descriptive terms, never a criteria-document name.
    #
    # Widened 20-Aug-2026 to ALL CareEdge reports, not just financial-sector ones. The newly
    # added Financial_Ratios_Non_Financial_Sector_March_2025 confirms CareEdge uses TANGIBLE
    # net worth for manufacturing, trading and service entities too - with a different build-up
    # from the financial-sector one (intangibles critical to core operations are RETAINED, and
    # deferred tax assets are not deducted). Two different TNW definitions is exactly the kind
    # of thing a report must state rather than leave the reader to assume.
    about = _section_body(t, r"about the")
    is_fin = re.search(r"\bbroking\b|stock ?brok|\bnbfc\b|non-banking financial compan"
                       r"|housing finance compan|scheduled commercial bank|banking compan",
                       about, re.I)
    is_careedge = re.search(r"careedge|care rating", t[:3000], re.I)
    if not (is_fin or is_careedge):
        return False
    return not re.search(r"tangible net.?worth|\bTNW\b|net.?worth basis", t, re.I)


def _broking_missing_careedge_metrics(t: str):
    """FM33. CareEdge's broking template reports these as standard rows.

    A metric may be excluded only after checking a published report of THAT agency in THAT
    sector. Generalising the NBFC rule (FM28) produced a written justification for omitting
    cost-to-income and ROTA from a broking report that should carry both.
    """
    if not re.search(r"\bbroking\b|stock ?brok", _section_body(t, r"about the"), re.I):
        return None
    need = {
        "cost-to-income": r"cost[- ]to[- ]income",
        "RONW": r"return on net.?worth|\bRONW\b|RoNW",
        "tangible net worth": r"tangible net.?worth|\bTNW\b",
        "gearing": r"gearing",
        "MTF / margin trading book": r"\bMTF\b|margin trading|margin funding",
    }
    miss = [k for k, p in need.items() if not re.search(p, t, re.I)]
    return ", ".join(miss) if miss else None


def _liquidity_encumbrance(t: str) -> bool:
    """FM34, GENERALISED BEYOND BROKING on 13-Sep-2026.

    The original version returned False for any report that did not mention broking, because
    the lesson was learned on HDFC Securities. That scoping was itself failure mode 33 in
    reverse - refusing to generalise a rule that IS general. Every issuer that parks money in
    margin deposits, earmarked balances, unpaid-dividend accounts or DSRA has the same problem.

    Dhampur Bio Organics, 04-Sep-2026, is the case that forced the widening: the report quoted
    cash and bank of Rs 36.16 crore, adding "other bank balances" of Rs 27.45 crore to cash and
    cash equivalents. CareEdge's published rationale of the same date states cash and bank was
    "low at Rs 4.5 crore" - an ~8x overstatement of free liquidity, on a sugar company, which
    the broking-scoped probe could not see.

    A Liquidity section that quotes a rupee cash figure must either call it unencumbered, or
    say what it excludes. Naming the treatment is the whole fix.
    """
    body = _section_body(t, r"liquidity")
    if not re.search(r"(rs\.?|₹)\s*\*{0,2}[\d,]{2,}", body, re.I):
        return False
    if not re.search(r"\bcash\b|bank balance|liquid asset", body, re.I):
        return False
    return not re.search(r"unencumber|encumber|free cash|excluding margin|net of margin"
                         r"|earmark|restricted", body, re.I)


def _report_date(t: str):
    """The report's own stated date, as (year, month, day). None if not found."""
    months = ("january february march april may june july august september october november "
              "december").split()
    m = re.search(r"\b([A-Z][a-z]{2,8})\s+(\d{1,2}),\s*(20\d\d)\b", t)
    if m and m.group(1).lower() in months:
        return int(m.group(3)), months.index(m.group(1).lower()) + 1, int(m.group(2))
    m = re.search(r"\b(\d{1,2})[ -]([A-Z][a-z]{2})[a-z]*[ -](20\d\d)\b", t)
    if m:
        abbr = [x[:3] for x in months]
        if m.group(2).lower() in abbr:
            return int(m.group(3)), abbr.index(m.group(2).lower()) + 1, int(m.group(1))
    return None


def _cra_amount_stale(t: str):
    """FM14 with TEETH. The old probe checked a date was PRESENT; this checks it is CURRENT.

    Dhampur Bio Organics, 04-Sep-2026: the report carried CareEdge's rated amounts stamped
    13-Jan-2026 - correctly date-stamped, so the presence probe passed - and presented them in
    the header as the September position. The real limits had been cut to Rs 987.05 crore and
    Rs 75.00 crore from Rs 1,019.45 crore and Rs 115.00 crore, because a unit had been sold and
    term debt prepaid IN BETWEEN. The report overstated the rated programme by Rs 72.40 crore
    while describing that very divestment in its own text.

    A stamped date is not freshness. Fires when the gap exceeds 180 days AND the report itself
    describes a capital event that would move facility limits.
    """
    rep = _report_date(t)
    if not rep:
        return None
    events = re.search(r"divest|slump sale|business transfer|prepay|pre-pay|pre-payment"
                       r"|repaid|acquisit|capacity (reduc|fell|reduced)|sold (off )?its",
                       t, re.I)
    if not events:
        return None
    # A RATING-HISTORY annexure legitimately contains old dates - that is what it is for.
    # Without this exclusion the probe fires on every well-formed report, which is the
    # cry-wolf failure it is supposed to prevent. Only dates in the body count.
    body = re.split(r"^[^\n]*rating history[^\n]*$", t, maxsplit=1, flags=re.I | re.M)[0]
    worst = None
    for m in re.finditer(r"(?:dated|stamped|as at|of)\s+((?:\d{1,2}[ -])?[A-Z][a-z]{2,8}[ -]"
                          r"\d{0,2},?\s*20\d\d)", body):
        d = _report_date(m.group(1))
        if not d:
            continue
        gap = (rep[0] - d[0]) * 365 + (rep[1] - d[1]) * 30 + (rep[2] - d[2])
        # Only a date attached to a RATED-AMOUNT attribution matters. Requiring a CRA name
        # alone fired on "this basis matches the one CareEdge applied in its action of
        # 13 January 2026" - a legitimate reference to a past action for BASIS comparison,
        # which is exactly the Step 14 behaviour the project wants to encourage. The context
        # must name both the publisher AND an amount.
        ctx = t[max(0, m.start() - 400): m.start()].lower()
        if not re.search(r"care|crisil|icra|cra-published|published", ctx):
            continue
        # "crore" alone is far too common - it matched "moves tangible net worth by Rs 3.04
        # crore" in a sentence about the analytical BASIS. The context must be about the rated
        # programme itself.
        if not re.search(r"rated amount|rated limit|sanctioned|facilit|programme|"
                         r"rating action table", ctx):
            continue
        if gap > 180 and (worst is None or gap > worst[1]):
            worst = (m.group(1), gap)
    return worst


def _post_bs_event_untreated(t: str) -> bool:
    """The Meerganj error, made mechanical.

    Dhampur Bio Organics, 04-Sep-2026: the report said FY2026 deleveraging was "assisted by the
    receipt of Rs 305.00 crore from the Meerganj divestment applied towards term-loan
    prepayment". The unit transferred in JUNE 2026 - FY2027. It cannot have moved the
    31-Mar-2026 balance sheet. Putting a forward catalyst in the past tense is also what turned
    a Positive outlook into a Stable one: a catalyst placed in the wrong period stops being a
    catalyst.

    Any report describing a divestment, slump sale, acquisition or major prepayment must state
    WHETHER the rated-period figures reflect it. This is a state-the-treatment probe, the same
    shape as the operating-profit normalisation one, because that shape works.
    """
    if not re.search(r"divest|slump sale|business transfer agreement|acquisition of|prepay"
                     r"|pre-payment", t, re.I):
        return False
    return not re.search(
        r"after the balance[- ]sheet date|post[- ]balance[- ]sheet|subsequent to the"
        r"|not reflected in|is not reflected|does not affect the (FY|rated)"
        r"|falls in FY|completed in FY\d{4}|reflected in the (FY\d{4}|rated[- ]period)"
        r"|balance sheet date of|after the (data cutoff|reporting date)", t, re.I)


def _opm_normalisation_unstated(t: str) -> bool:
    """FM36. An operating-profit measure must name its NORMALISATION treatment.

    Balkrishna Industries, 25-Aug-2026: "Other Expenses" went into OPBDITA as a subtotal,
    carrying a Rs 290.01 crore forex loss inside it. Published margin 21.25% against ICRA's
    actual 24.3%; the rating shipped a notch low on a "margin compression" that had not
    happened.

    The structural trap, and why naming the treatment is the fix: the SAME economic item
    migrates between notes with its sign. BKT's FY2025 forex GAIN (Rs 267.36 cr) sat in Other
    Income; its FY2026 forex LOSS (Rs 290.01 cr) sat in Other Expenses. A convention of
    "PBT + finance + depreciation - other income" therefore strips the gain automatically and
    keeps the loss - asymmetric, and it manufactures a margin decline out of nothing.

    Note this probe deliberately does NOT accept a bare "no exceptional item was disclosed":
    a forex loss is not captioned "exceptional", so that sentence is not a treatment - it is an
    unevidenced absence claim (failure mode 20), which is exactly the sentence the failing
    report contained.
    """
    if not re.search(r"OPBDIT|OPBDITA|PBILDT|EBITDA|operating (?:profit )?margin", t, re.I):
        return False
    return not re.search(
        r"forex|foreign (?:currency|exchange)|normalis|normaliz|"
        r"exceptional[^.]{0,60}(?:excluded|added back|adjusted)|"
        r"(?:excluded|added back|adjusted)[^.]{0,60}exceptional", t, re.I)


# --------------------------------------------------------------------------------------
# Failure modes 47, 51, 52 - definitions and notch counts that differ BY AGENCY, added
# 13-Sep-2026 after Cochin Minerals (CareEdge gearing 0.04x vs published 0.31x, the gap
# being ~47 crore of LC-backed creditors CareEdge's own methodology puts in Total Debt and
# ICRA's own methodology does not) and the completed ICRA/CRISIL Banks & NBFC methodology
# read that surfaced two DIFFERENT hybrid-instrument caps and two DIFFERENT support-notch
# conventions with numerically similar-looking numbers attached to them.
# --------------------------------------------------------------------------------------

def _agency_from_headline(t: str) -> str:
    """Same signal detect_agency() uses (the report's OWN declared house style), exposed as
    a plain function so a probe can call it without needing the Path this file's audit()
    already has. Kept identical to detect_agency()'s headline patterns on purpose - two
    slightly different agency-sniffers in one file is how a probe silently stops firing."""
    head = t[:3000]
    if re.search(r"\[ICRA\]", head):
        return "ICRA"
    if re.search(r"\bCrisil\s+[A-Z]", head) or re.search(r"'Crisil\b", head, re.I):
        return "CRISIL"
    if re.search(r"\bCARE\s+[A-Z]{2,3}[+-]?\b", head) or re.search(r"CareEdge", head, re.I):
        return "CareEdge"
    return "ICRA"


def _total_debt_basis_unstated(t: str) -> bool:
    """FM47. CareEdge and CRISIL both fold LC-backed acceptances/creditors into Total Debt for
    gearing (CareEdge/CORPORATE_CONVENTIONS.md S10, CRISIL_CONVENTIONS.md S3); ICRA's own
    Corporate Credit Rating Methodology does NOT name them as a Total Debt component - they sit
    in Total Outside Liabilities instead. A report that quotes gearing for a CareEdge or CRISIL
    issuer with disclosed non-fund-based facilities, without ever connecting the two, is
    reproducing exactly the Cochin Minerals gap: statutory gearing 0.04x against CareEdge's own
    published 0.31x, the difference being ~47 crore of LC-backed creditors.

    Scoped to fire ONLY when non-fund-based facilities are actually disclosed somewhere in the
    document - an issuer with no LC/BG/acceptance exposure has nothing to decompose, and
    requiring the phrase anyway would be a false-positive factory, exactly what trains a reader
    to ignore a checker.
    """
    if not re.search(r"\bgearing\b", t, re.I):
        return False
    agency = _agency_from_headline(t)
    if agency not in ("CareEdge", "CRISIL"):
        return False   # ICRA's own convention does not require this cross-reference
    # "no non-fund-based facilities" must NOT count as a disclosure to cross-reference against -
    # exclude a hit preceded within ~15 characters by a negation (found via a positive control).
    nfb_hits = list(re.finditer(r"letter of credit|non-fund.?based|bank guarantee|\bacceptance",
                                t, re.I))
    has_nfb = any(not re.search(r"\bno\b|\bnone\b|\bnil\b|\bwithout\b", t[max(0, m.start() - 15):m.start()], re.I)
                 for m in nfb_hits)
    if not has_nfb:
        return False
    linked = re.search(
        r"total debt[^.]{0,120}(acceptance|letter of credit|non-fund)"
        r"|(acceptance|letter of credit|non-fund)[^.]{0,120}total debt"
        r"|gearing[^.]{0,150}(acceptance|letter of credit|non-fund)"
        r"|(acceptance|letter of credit|non-fund)[^.]{0,150}gearing", t, re.I | re.S)
    return not linked


# CRISIL's own LT-ST mapping (basics-of-ratings.md Table 1), keyed by entity class. Table 1's
# own caption: "ratings within brackets only in exceptional cases" - so the UNBRACKETED value
# in each cell is CRISIL's stated primary/default mapping, and is what is encoded below. A cell
# with two co-equal UNBRACKETED values (e.g. "A2+, A2") is genuinely ambiguous in the source and
# is deliberately omitted, the same honest-limitation choice as ICRA's own liquidity-dependent
# middle band (see _ICRA_LT_ANCHORS).
_CRISIL_LT_ST = {
    "Corporates": {"AAA": "A1+", "AA+": "A1+", "AA": "A1+", "AA-": "A1+", "A+": "A1", "A": "A1",
                  "A-": "A2+", "BBB+": "A2", "BBB": "A3+", "BBB-": "A3",
                  "BB+": "A4+", "BB": "A4+", "BB-": "A4+", "B": "A4", "C": "A4"},
    "Banks": {"AAA": "A1+", "AA+": "A1+", "AA": "A1+", "AA-": "A1+", "A+": "A1+", "A": "A1+",
             "A-": "A1+", "BBB+": "A1",   # BBB and BBB- are genuinely ambiguous for Banks - omitted
             "BB+": "A4+", "BB": "A4+", "BB-": "A4+", "B": "A4", "C": "A4"},
    "PDs": {"AAA": "A1+", "AA+": "A1+", "AA": "A1+", "AA-": "A1+", "A+": "A1+", "A": "A1+",
           "A-": "A1", "BBB+": "A2+", "BBB": "A2",   # BBB- ambiguous for PDs - omitted
           "BB+": "A4+", "BB": "A4+", "BB-": "A4+", "B": "A4", "C": "A4"},
    "Other Fin sector entities": {"AAA": "A1+", "AA+": "A1+", "AA": "A1+", "AA-": "A1+",
                  "A+": "A1+", "A": "A1", "A-": "A1",   # BBB+ ambiguous - omitted
                  "BBB": "A3+", "BBB-": "A3",
                  "BB+": "A4+", "BB": "A4+", "BB-": "A4+", "B": "A4", "C": "A4"},
}
_ICRA_LT_ANCHORS = {  # only the two FIXED anchors - the rest is a liquidity-dependent choice
    "AAA": "A1+", "AA+": "A1+", "AA": "A1+", "AA-": "A1+",
    "B+": "A4", "B": "A4", "B-": "A4", "C+": "A4", "C": "A4", "C-": "A4",
}
_LT_GRADE_RE = re.compile(r"\b(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|C[+-]?|D)\b")
_ST_GRADE_RE = re.compile(r"\b(A1\+|A1|A2\+|A2|A3\+|A3|A4\+|A4)\b")


def _lt_st_mapping_mismatch(t: str):
    """LT-ST mapping is agency-specific, and for CRISIL, entity-class-specific too (CLAUDE.md
    Step 13, corrected 13-Sep-2026 - the previous single hardcoded table was ICRA's own,
    applied to all three agencies without checking). Checks the report's OWN stated (LT, ST)
    pair against the correct table, only where that table has a fixed answer.

    CareEdge is DELIBERATELY not checked here: its own LT-ST mapping table
    (Rating_of_Short_Term_Instruments_Feb_2025.md) survived PDF conversion with every data cell
    blank (failure mode 49) - there is no verified CareEdge table to check against, and
    asserting one would be worse than asserting none.
    """
    # NB: "\b" after a "+" is not a word boundary between two non-word characters (e.g. "A2+;")
    # and silently matches the SHORTER grade instead - the same bug corpus_mine.py's ST_RE had
    # to fix. A negative lookahead, not \b, is what actually stops "AA" swallowing "AAA" or
    # "A2" swallowing "A2+".
    head = t[:3000]
    lt_m = re.search(
        r"(?:\[ICRA\]|CARE\s+|Crisil\s+)(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|C[+-]?|D)(?![A-Za-z0-9+])",
        head)
    st_m = re.search(
        r"(?:\[ICRA\]|CARE\s+|Crisil\s+)(A1\+|A1|A2\+|A2|A3\+|A3|A4\+|A4)(?![A-Za-z0-9+])",
        head)
    if not (lt_m and st_m):
        return None
    lt, st = lt_m.group(1), st_m.group(1)
    agency = _agency_from_headline(t)
    if agency == "ICRA":
        want = _ICRA_LT_ANCHORS.get(lt)
        if want and st != want:
            return (f"[ICRA]{lt} is one of ICRA's two FIXED anchors and must map to [ICRA]{want} "
                    f"always (mapping.md) - this report states {st}")
        return None
    if agency == "CRISIL":
        about = _section_body(t, r"about the")
        if re.search(r"\bprimary dealer\b|\bPD\b", about):
            table, cls = _CRISIL_LT_ST["PDs"], "PDs"
        elif re.search(r"is a bank|banking compan|scheduled commercial bank"
                       r"|public sector bank|private sector bank|commercial bank"
                       r"|small finance bank|payments bank|deposit franchise"
                       r"|largest bank|bank in india", about, re.I):
            table, cls = _CRISIL_LT_ST["Banks"], "Banks"
        elif re.search(r"\bnbfc\b|housing finance|financial institution", about, re.I):
            table, cls = _CRISIL_LT_ST["Other Fin sector entities"], "Other Fin sector entities"
        else:
            table, cls = _CRISIL_LT_ST["Corporates"], "Corporates"
        want = table.get(lt)
        if want and st != want:
            return (f"Crisil {lt} for a {cls} entity maps to Crisil {want} per CRISIL's own "
                    f"Table 1 (basics-of-ratings.md) - this report states {st}")
        return None
    return None


def _hybrid_cap_conflated(t: str):
    """FM51. Two numerically similar-looking hybrid-instrument caps from different agencies
    measure different things: ICRA's CORPORATE hybrid equity-credit cap is 30% of adjusted
    equity (an analytical convention, ICRA_CONVENTIONS.md S9); CRISIL's NBFC/HFC perpetual-
    debt Tier I inclusion cap is 15% of Tier I capital (a regulatory limit CRISIL applies
    analytically, CRISIL_BANKS_NBFC_CONVENTIONS.md S2). Citing one agency's percentage inside
    the other agency's (and entity class's) workpaper is the exact trap FM51 exists to catch.
    """
    hybrid_ctx = _section_body(t, r"hybrid|perpetual|tier[- ]?i\b|additional tier")
    if not hybrid_ctx:
        return None
    agency = _agency_from_headline(t)
    about = _section_body(t, r"about the")
    is_nbfc = re.search(r"\bnbfc\b|housing finance|non-banking financial", about, re.I)
    if agency == "ICRA" and not is_nbfc and re.search(r"\b15\s*%", hybrid_ctx):
        return ("ICRA corporate hybrid-instrument cap cited as 15% - ICRA's own cap is 30% of "
                "adjusted equity (ICRA_CONVENTIONS.md S9). 15% of Tier I capital is CRISIL's "
                "NBFC/HFC regulatory-inclusion rule and does not apply to an ICRA corporate case.")
    if agency == "CRISIL" and is_nbfc and re.search(r"\b30\s*%", hybrid_ctx):
        return ("CRISIL NBFC/HFC hybrid-instrument cap cited as 30% - CRISIL's own cap is 15% "
                "of Tier I capital (CRISIL_BANKS_NBFC_CONVENTIONS.md S2). 30% of adjusted equity "
                "is ICRA's corporate analytical rule and does not apply to a CRISIL NBFC case.")
    # THE THIRD CAP, added 06-Sep-2026 after reading basics-of-ratings.md Section XII in full.
    # This function shipped knowing only TWO caps, and was therefore blind to a CRISIL
    # CORPORATE case citing either of the other figures - the likeliest conflation of all,
    # since CRISIL corporates are the commonest case type in this project. CRISIL states it
    # plainly: "Crisil Ratings limits the total equity content for hybrids for an issuer to
    # 20% of its adjusted net worth" (basics-of-ratings.md, III.2). Three caps, three bases,
    # all within ten percentage points of each other:
    #     ICRA corporate     30% of adjusted equity      analytical
    #     CRISIL corporate   20% of adjusted net worth   analytical
    #     CRISIL NBFC/HFC    15% of Tier I capital       regulatory
    if agency == "CRISIL" and not is_nbfc:
        m = re.search(r"\b(30|15)\s*%", hybrid_ctx)
        if m:
            wrong = m.group(1)
            owner = ("ICRA's corporate rule (30% of adjusted equity)" if wrong == "30"
                     else "CRISIL's own NBFC/HFC regulatory rule (15% of Tier I capital), "
                          "which does not apply to a corporate")
            return (f"CRISIL corporate hybrid-instrument cap cited as {wrong}% - CRISIL's own "
                    f"corporate cap is 20% of adjusted net worth (CRISIL_CONVENTIONS.md S7, "
                    f"from basics-of-ratings.md III.2). {wrong}% is {owner}.")
    return None


# CRISIL's published Expected Loss bands (crisils-criteria-for-expected-loss-ratings-for-
# infrastructure-projects.md). Aligned to SEBI's scale in July 2021; the pre-2021 symbols
# were "CRISIL INFRA EL 1-7" over identical bands. Lower bound exclusive, upper inclusive.
_EL_BANDS = {
    1: (0.0, 1.25), 2: (1.25, 3.5), 3: (3.5, 7.5), 4: (7.5, 15.0),
    5: (15.0, 25.0), 6: (25.0, 35.0), 7: (35.0, float("inf")),
}


def _asset_quality_improvement_without_writeoffs(t: str):
    """FM59. A lender's delinquency numbers improve automatically when it writes loans off.

    CRISIL states the mechanism plainly in its securitisation criteria, where it is analysing
    an ORIGINATOR rather than a securitisation: "Writing off loans leads to recognition of
    losses and the exposure is usually removed from the portfolio of the originator in the
    delinquency analysis. Thus, the exposure does not show up in any of the delinquency
    buckets, which leads to an apparent improvement in the dpd profile of the portfolio. All
    else being equal, originators adopting aggressive write-off policies will show better
    delinquency levels than others." Its remedy is to obtain historic write-off data NET OF
    RECOVERIES and express the cumulative figure against portfolio principal ~12 months
    earlier - a proxy for net losses on a static-pool basis.

    Nothing about this is securitisation-specific, and the gap is live here: on 06-Sep-2026
    four delivered lender cases quoted asset-quality metrics and NONE mentioned write-offs -
    Repco Home Finance (8 asset-quality references, 0 write-off), Aptus (6/0), IIFL (4/0),
    SBI (2/0). Repco reports GNPA improving every year from 7.0% to 2.67% with no write-off
    figure anywhere, so on the evidence in the report we cannot tell a genuine recovery from
    a write-off-driven one.

    The probe asks only that the report ADDRESS write-offs - stating they were nil is a
    complete answer. It does not require write-offs to exist.
    """
    about = _section_body(t, r"about the", span=1800) or t[:1500]
    if not re.search(r"\bnbfc\b|non-banking financial|housing finance"
                     r"|\bhfc\b|is a bank|banking compan|scheduled commercial bank"
                     r"|public sector bank|private sector bank|small finance bank"
                     r"|microfinance|asset finance", about, re.I):
        return None
    aq = re.search(r"\bgnpa\b|gross npa|\bnnpa\b|net npa"
                   r"|stage 3|stage iii|\bgs3\b|\bns3\b"
                   r"|delinquenc|days past due|\bdpd\b", t, re.I)
    if not aq:
        return None
    # Only fire where the report CLAIMS the metric got better. A report simply stating a
    # level, or reporting deterioration, is not making the claim this trap corrupts.
    improved = re.search(r"(?:improv|declin|reduc|fell|lower|moderat|eased|compress)"
                         r"[a-z]*[^.]{0,160}?(?:gnpa|gross npa|nnpa|net npa|stage 3|stage iii"
                         r"|asset quality|delinquenc|dpd)"
                         r"|(?:gnpa|gross npa|nnpa|net npa|stage 3|stage iii|asset quality"
                         r"|delinquenc|dpd)[^.]{0,160}?"
                         r"(?:improv|declin|reduc|fell|lower|moderat|eased|compress)", t, re.I)
    if not improved:
        return None
    if re.search(r"written[- ]off|write[- ]?off|writeoff|technical write", t, re.I):
        return None
    return ("the report claims an asset-quality improvement (" +
            re.sub(r"\s+", " ", improved.group(0))[:90].strip() +
            ") but never mentions write-offs. Writing loans off removes them from every "
            "delinquency bucket, so a book that writes off aggressively shows a better dpd "
            "profile for no credit reason - CRISIL: \"all else being equal, originators "
            "adopting aggressive write-off policies will show better delinquency levels "
            "than others.\" State write-offs net of recoveries, or state that they were nil.")


def _el_band_mismatch(t: str):
    """FM58. An EL rating and a stated expected-loss percentage must agree with CRISIL's
    published bands. EL = PD x LGD over the life of the instrument, and the seven bands are
    numeric and public, so this is arithmetic - the same class of check as the Annexure-I
    line-integrity probe, and it fails the same way: silently, with prose that reads fine.

    CRISIL-scoped on purpose. ICRA publishes its own expected-loss methodology (960-series
    "Expected Loss" file) which has NOT been read for this project, so its bands must not be
    assumed identical. Applying CRISIL's numbers to an ICRA EL case would be failure mode 33
    in its purest form.

    THE ANNUALISED TRAP. CRISIL's own worked example quotes BOTH figures for one instrument:
    an EL of 1.5% over a ten-year life, and an annualised EL of 0.15%. The bands apply to the
    LIFE figure only. A check that grabbed the nearest percentage would read 0.15%, place it
    in EL 1, and report a mismatch against a perfectly correct EL 2 rating - so any figure
    described as annualised, per annum or yearly is skipped rather than tested.
    """
    # _agency_from_headline is case-sensitive on "Crisil" by design (it is the house style,
    # and loosening it would change behaviour for the five other probes that share it). The
    # PRE-2021 EL symbol is all-caps - "CRISIL INFRA EL 3" - so it fails that detector even
    # though it is unambiguously CRISIL's own scale. Caught by this probe's own control.
    head = t[:3000]
    if _agency_from_headline(t) != "CRISIL" and not re.search(
            r"\bCRISIL[ ]+INFRA[ ]+EL[ ]*[1-7]", head):
        return None
    m = re.search(r"(?:Crisil|CRISIL)[ ]+(?:INFRA[ ]+)?EL[ ]*([1-7])(?![0-9])", t)
    if not m:
        return None
    grade = int(m.group(1))
    lo, hi = _EL_BANDS[grade]
    for pm in re.finditer(r"expected loss[^.%]{0,80}?([0-9]+(?:\.[0-9]+)?)[ ]*%", t, re.I):
        window = t[max(0, pm.start() - 60): pm.end() + 60].lower()
        if re.search(r"annualis|annualiz|per annum|p\.a\.|yearly", window):
            continue                      # the bands are life-of-instrument figures only
        val = float(pm.group(1))
        if not (lo < val <= hi):
            return (f"report states an expected loss of {val:g}% and a rating of "
                    f"'Crisil EL {grade}', but EL {grade} spans "
                    f"{lo:g}% to {hi:g}%. On CRISIL's published bands {val:g}% is "
                    f"EL {_el_grade_for(val)}. Either the loss estimate or the grade is wrong.")
    return None


def _el_grade_for(val: float) -> int:
    for g, (lo, hi) in _EL_BANDS.items():
        if lo < val <= hi:
            return g
    return 1 if val <= 1.25 else 7


def _outlook_on_c_or_d(t: str):
    """FM54. CRISIL does not assign an outlook to a C or D category rating.

    basics-of-ratings.md, Section I: "Outlooks are assigned to ratings of long-term
    instruments and fixed deposits, BARRING 'Crisil C' and 'Crisil D' category ratings."
    Nor are outlooks assigned to short-term ratings, nor to any rating on Watch. A headline
    reading "Crisil C/Stable" is malformed on CRISIL's own rule.

    This is checkable at both ends and the tool violates it too: Rating!C36 in
    Rating_Scorecard.xlsx concatenates Inputs!C44 unconditionally, so a case whose Stage 3
    lands at C would print an outlook the agency would never publish. Found 06-Sep-2026 while
    reading basics-of-ratings.md in full; no case in the corpus is rated below B- today, so
    this probe guards a boundary the project has not yet reached rather than a live defect.
    """
    if _agency_from_headline(t) != "CRISIL":
        return None
    head = t[:3000]
    m = re.search(r"Crisil[ ]+(C[+-]?|D)(?![A-Za-z0-9+])[^.|\n]{0,40}?"
                  r"(Stable|Positive|Negative)", head, re.I)
    if not m:
        return None
    return (f"headline pairs 'Crisil {m.group(1)}' with a '{m.group(2)}' outlook. CRISIL "
            f"assigns outlooks to long-term ratings BARRING the C and D categories "
            f"(basics-of-ratings.md Section I), so this pairing cannot occur in a CRISIL "
            f"publication. Drop the outlook, or correct the grade.")


def _infra_spv_notch_excessive(t: str):
    """FM52. CRISIL states its own default: infrastructure SPVs are typically NOT notched up
    for parent support, or only by a LIMITED 1-2 notches, because they are deliberately
    structured as ring-fenced, limited-recourse entities (criteria-for-factoring-parent-group-
    government-linkages.md). Neither ICRA's Implicit Parent Support methodology nor CareEdge's
    equivalent states a numeric ceiling for the same scenario - so this check is CRISIL-only;
    applying it to an ICRA or CareEdge SPV would be importing a rule that agency never made.
    """
    if _agency_from_headline(t) != "CRISIL":
        return None
    if not re.search(r"\bspv\b|special purpose vehicle|road project|toll|annuity"
                     r"|power project|transmission project", t, re.I):
        return None
    m = re.search(r"notch(?:ed)?[- ]?up[^.]{0,40}?(\d)\s*(?:-|to)\s*(\d)\s*notch", t, re.I)
    if not m:
        m = re.search(r"(\d)\s*notch(?:es)?\s*(?:of\s+)?(?:up.?lift|support)", t, re.I)
    if not m:
        return None
    notches = max(int(g) for g in m.groups() if g)
    if notches > 2 and not re.search(
            r"exception|except\b|exceptional.{0,30}(linkage|circumstance)", t, re.I):
        return (f"{notches}-notch parent-support uplift stated for a CRISIL infrastructure SPV "
                f"with no exception justification - CRISIL's own stated norm is 1-2 notches")
    return None


# --------------------------------------------------------------------------------------
# Failure mode 37 - verbatim reuse of an agency-published report.
# --------------------------------------------------------------------------------------
# CLAUDE.md section 2 gives the reference library exactly one role: TEACH the craft. It may
# never supply a fact, a figure, a driver or a phrasing to a new report. That rule was
# prose-only, and prose-only rules in this project have a measured failure rate - so this is
# the mechanical half.
#
# The exposure is worst in the one situation the SOP itself creates. Step 14 requires opening
# the agency's own report on the issuer AFTER forming a view. Whatever is read there is then
# the freshest text in mind while the draft is being corrected, and it migrates - not as a
# quoted block anyone would notice, but as a clause here and a framing there.
#
# Balkrishna Industries, 25/26-Aug-2026: a post-delivery correction pass against ICRA's
# published rationale carried across its Q1 FY2027 framing ("increased crude oil and adverse
# currency movement impacted margins... calibrated price hikes are expected to support
# near-term margins") and its positive-sensitivity construction ("a significant increase in
# the scale of operations and earnings, led by material ramp-up of on-highway tyre segments").
# The operator caught it, not the toolchain. Worse, the imported framing was WRONG on the
# issuer's own numbers: BKT's Q1 FY2027 filing shows revenue +25.2% and the company's own
# operating margin at 15.57% against 11.52% a year earlier - improving, not compressed. Taking
# the framing meant not doing the arithmetic.
#
# Method: shared word n-grams. Independent prose about the same company shares vocabulary and
# figures constantly, but almost never a 12-word run. Numbers are normalised out so that two
# reports legitimately quoting "Rs. 10,823.08 crore" are not scored as copying; what is being
# detected is shared SENTENCE CONSTRUCTION.
_NGRAM_N = 12

# Standard regulatory boilerplate a rationale is SUPPOSED to reproduce - the complexity-
# indicator explanation and the closing disclaimer are mandated text, not analysis. Comparing
# them would generate guaranteed false positives and train the reader to ignore this probe.
_BOILERPLATE_SECTIONS = re.compile(
    r"^#{1,4}\s*(?:complexity level|annexure|disclaimer)\b", re.I | re.M)


# Lines a rationale is MANDATED to render uniformly. Comparing them measures compliance with
# the house format, not copying, and every report in the corpus shares them by construction.
# Leaving them in produced a flood of hits on "status of non cooperation with previous cra not
# applicable any other information" - two consecutive REQUIRED section headers - which is
# precisely the false-positive pattern CLAUDE.md warns trains a reader to ignore a checker.
_MANDATED_LINE = re.compile(
    r"^\s*#{1,6}\s"                       # section headers (section 7 fixes the section list)
    r"|^\s*\|"                            # table rows
    r"|^\s*\*?source\s*:"                 # mandated source line under the KI table
    r"|methodolog|criteria for"           # methodology names, quoted verbatim per section 4
    r"|as per [a-z]+(?:'s|s)? calculations"
    r"|rating outlook and rating watch|definition of default"
    r"|liquidity analysis of non[- ]financial sector"
    # The complexity-indicator explanation is prescribed text every rationale must carry, and
    # it is not always under a heading this can cut at, so allowlist the sentence itself.
    r"|complexity indicator refers to",
    re.I)


# An ATTRIBUTED QUOTATION is a citation, not passing-off. Repco Home Finance, 29-Aug-2026:
# the report names the reference-library document by title, in quotation marks, with its date,
# precisely in order to explain that it is a SECURITISATION rationale and was therefore NOT
# used as a source for the corporate rating. The probe flagged that as verbatim reuse - which
# is backwards, since disclosing what you excluded and why is the discipline the SOP asks for.
# Quoted spans are dropped only on lines that also carry an attribution cue, so a passage
# someone merely wrapped in quotes without saying whose it is still counts against them.
_ATTRIBUTION_CUE = re.compile(
    r"\btitled\b|\bentitled\b|\bdated\b|\bper\b|\baccording to\b|\bquotes?\b"
    r"|\bcites?\b|\bstates\b", re.I)
_QUOTED_SPAN = re.compile(r"[\"\u201c\u201d][^\"\u201c\u201d]{10,400}[\"\u201c\u201d]")


def _drop_attributed_quotes(line: str) -> str:
    return _QUOTED_SPAN.sub(" ", line) if _ATTRIBUTION_CUE.search(line) else line


def _originality_words(t: str) -> list:
    kept = [_drop_attributed_quotes(ln)
            for ln in t.splitlines() if not _MANDATED_LINE.search(ln)]
    t = "\n".join(kept)
    t = re.sub(r"[\d,.]+", " ", t)                              # drop all figures
    t = re.sub(r"[^a-z\s]", " ", t.lower())
    return t.split()


def _strip_boilerplate(t: str) -> str:
    m = _BOILERPLATE_SECTIONS.search(t)
    return t[:m.start()] if m else t


def _shared_ngrams(draft: str, source: str, n: int = _NGRAM_N) -> list:
    a, b = _originality_words(_strip_boilerplate(draft)), _originality_words(source)
    if len(a) < n or len(b) < n:
        return []
    src = {tuple(b[i:i + n]) for i in range(len(b) - n + 1)}
    hits, i = [], 0
    while i <= len(a) - n:
        if tuple(a[i:i + n]) in src:
            run = list(a[i:i + n])                              # extend to the full overlap
            j = i + n
            while j < len(a) and tuple(a[j - n + 1:j + 1]) in src:
                run.append(a[j])
                j += 1
            hits.append(" ".join(run))
            i = j
        else:
            i += 1
    return hits


# A file is treated as an agency publication if it carries a publisher's own footer/boilerplate
# signature. Filename conventions vary too much across this corpus to rely on.
_AGENCY_SIGNATURE = re.compile(
    r"www\.icra\.in|icra limited was set up|sensitivity label|"
    r"crisil ratings limited|about crisil|care ratings limited|careedge ratings|"
    r"©\s*copyright,?\s*20\d\d", re.I)


# Tokens too generic to identify an issuer. "Indus" matching "Industries" is the documented
# trap here (failure mode 24), so matching requires EVERY significant token to be present.
_GENERIC_TOKENS = {
    "limited", "ltd", "company", "corporation", "corp", "india", "indian", "the", "and",
    "industries", "industry", "enterprises", "holdings", "group", "private", "pvt",
    "rating", "rationale", "aug", "jul", "jun", "sep", "oct", "nov", "dec", "jan", "feb",
    "mar", "apr", "may", "crisil", "care", "icra", "careedge",
}


_PRIOR_ABSENCE_RE = re.compile(
    r"no (?:prior )?(?:CRA|credit rating agenc\w+) has (?:published|rated|assigned|issued)"
    r"|no prior rating action"
    r"|no rating history (?:exists|is available|available)"
    r"|no (?:CRA|agency) action for this issuer was located"
    r"|no anchor exposure"
    r"|not (?:located|found) in any reference librar",
    re.I)

# A corrected report QUOTES its own former false claim while correcting it - this file's own
# Cochin Minerals rationale now does exactly that. Firing on the correction would punish the
# fix and teach the analyst to delete the audit trail instead of writing one.
_CORRECTION_RE = re.compile(
    r"corrected|previously (?:asserted|read|stated|said)|was false|superseded|incorrectly|"
    r"this paragraph previously|no longer",
    re.I)

# An absence phrase that is immediately QUALIFIED - "no prior rating action *by this analysis*;
# company carries an actual outstanding Crisil AA/Stable rating, see divergence below" - is the
# opposite of a false absence-claim: it is correct disclosure. The first version of this probe
# fired on exactly that sentence in the Happy Forgings rationale, which is failure mode 37's
# calibration lesson arriving again: a checker that cries wolf trains the reader to ignore it.
_ACKNOWLEDGED_RE = re.compile(
    r"by this (?:analysis|exercise)|in this exercise"
    r"|actual(?:ly)? outstanding"
    r"|(?:carries|holds|has) an? (?:actual|outstanding|existing|live|current)"
    r"|see .{0,12}divergence",
    # Deliberately NOT keyed on a rating grade appearing nearby. A CareEdge report carries
    # "CARE A3+" in the summary table directly above its own rated-amount note, so a bare
    # grade string in the window would have suppressed the Cochin Minerals finding this probe
    # exists for - the check would have passed the exact report that motivated it.
    re.I)


def _prior_rating_absence_contradicted(t: str, rationale_name: str):
    """Failure modes 20/24/29: the report claims no prior rating exists while the agency's own
    action for this issuer sits in the reference library.

    Cochin Minerals, 13-Sep-2026, is why this exists and why it is BLOCKING. The report
    asserted three times, in bold, that no CRA had rated the issuer. CareEdge's action of nine
    days earlier was in the library, and `preflight.py` probe [1] had already reported it
    PRESENT, printed its rated-amount lines, and said in terms "You may NOT write 'no prior
    rating action'." The entry gate did its job perfectly and nothing downstream compared the
    delivered report against it, so a false absence-claim walked through every other check and
    took Step 14 - the step designed to catch exactly this - out of the flow with it. The
    result was a two-notch miss.

    Matching is deliberately strict: EVERY significant token of the issuer's name must appear
    in the library filename, so "Cochin Shipyard" and "Sarda Energy & Minerals" do not match
    "Cochin Minerals and Rutile" on a shared word. That is failure mode 24 read from the other
    direction - a loose match here would import a peer's rating, which is worse than the
    absence-claim it is trying to prevent.
    """
    m = _PRIOR_ABSENCE_RE.search(t)
    if not m:
        return None
    window = t[max(0, m.start() - 400):m.end() + 400]
    if _CORRECTION_RE.search(window) or _ACKNOWLEDGED_RE.search(window):
        return None
    tokens = _issuer_tokens(rationale_name)
    if not tokens:
        return None
    hits = []
    for lib in (ROOT / "Report for Reference", ROOT / "CRISIL" / "Report for Reference",
                ROOT / "CareEdge" / "Report for Reference"):
        if not lib.is_dir():
            continue
        for f in sorted(lib.iterdir()):
            if not f.is_file() or f.suffix.lower() not in (".md", ".txt"):
                continue
            low = f.name.lower()
            if all(re.search(r"\b" + re.escape(tok), low) for tok in tokens):
                hits.append(f"{lib.parent.name if lib.parent != ROOT else 'ICRA'}/{f.name}")
    if not hits:
        return None
    return (f"the report states {t[m.start():m.end()+60].strip()!r}, but "
            f"{len(hits)} same-issuer publication(s) sit in the reference library: "
            f"{'; '.join(hits[:3])}. preflight.py probe [1] reports these PRESENT before any "
            f"drafting begins, and CLAUDE.md Step 1a makes that binding: anything the "
            f"pre-flight reports PRESENT may never later be written as absent. A false "
            f"absence-claim is not a weak section - it removes Step 14 and with it the only "
            f"check that compares this view against the agency's own.")


def _issuer_tokens(rationale_name: str) -> set:
    """Significant tokens, or an EMPTY set when the name cannot identify an issuer safely.

    The 4-character minimum used at first threw away "JSW", leaving {steel} as the whole
    identity of "JSW Steel Limited" - which then matched Jindal Steel, Kalyani Steels, NMDC
    Steel and Manaksia Steels. That is failure mode 24's trap arriving from the other
    direction, so the floor is 3 characters and a lone token must be long enough to be a real
    name ("balkrishna" identifies; "steel" does not). Returning an empty set disables library
    matching rather than guessing.
    """
    head = rationale_name.split("_")[0]
    toks = {w for w in re.findall(r"[a-z]{3,}", head.lower())} - _GENERIC_TOKENS
    if len(toks) >= 2 or (len(toks) == 1 and len(next(iter(toks))) >= 6):
        return toks
    return set()


def resolve_case_dir(path):
    """The Companies/<slug>/ folder this rationale belongs to, or None.

    WHY THIS IS NOT JUST path.parent. The SOP files deliverables in the PROJECT ROOT
    ("<Company>_<date>_Rating Rationale.md"), while case.json lives in Companies/<slug>/.
    Resolving the case folder as path.parent therefore returned the project root for almost
    every delivered report, so every case-level probe below it - including the failure-mode-35
    Step 12 check - was SILENTLY INERT on exactly the files it was written to police. Found
    01-Sep-2026 while adding the scorecard-cached-values probe.

    A rationale inside a case folder still resolves to that folder. One in the root is matched
    against each case's registered name and aliases, whole-word, so "Vodafone Idea Limited_01
    Sep 2026_Rating Rationale.md" finds Companies/vi even though the case is named "Vi".
    """
    import json as _json
    if (path.parent / "case.json").exists():
        return path.parent
    companies = path.parent / "Companies"
    if not companies.is_dir():
        return None
    stem = re.sub(r"[_\-]+", " ", path.stem.lower())
    best, best_len = None, 0
    for d in sorted(companies.iterdir()):
        cj = d / "case.json"
        if not cj.is_file():
            continue
        try:
            meta = _json.loads(cj.read_text(encoding="utf-8"))
        except Exception:                                                 # noqa: BLE001
            continue
        cands = [str(meta.get("name", ""))] + [str(a) for a in meta.get("aliases", []) or []]
        for c in cands:
            c = c.strip().lower()
            # 3-char floor: a 2-letter alias is too generic to bind a file to a case.
            if len(c) < 3:
                continue
            if re.search(r"(?<![a-z0-9])" + re.escape(c) + r"(?![a-z0-9])", stem):
                # Longest match wins, so "state bank of india" beats a stray "sbi".
                if len(c) > best_len:
                    best, best_len = d, len(c)
    if best is not None:
        return best
    # FALLBACK. A case registered under a short form ("SBI") whose deliverables use the legal
    # name ("State Bank of India") matches no registered name, so every case-level probe would
    # be skipped for its root-filed rationale - the same silent-inertness this function was
    # written to fix, arriving by another route. Files inside a case folder belong to that case
    # by construction, so a folder holding a file with the same leading words as the rationale
    # is the right owner. Two words minimum: one is too generic to bind a file to a case.
    lead = " ".join(stem.split()[:2])
    if len(lead.split()) == 2:
        for d in sorted(companies.iterdir()):
            if not (d / "case.json").is_file():
                continue
            for f in d.iterdir():
                if not f.is_file():
                    continue
                if re.sub(r"[_\-]+", " ", f.stem.lower()).startswith(lead):
                    return d
    return best


def find_agency_publications(case_dir, rationale_name=""):
    """Agency-published texts this draft could have copied from.

    Two surfaces, because the risk lives in both:
      (a) the case folder - where an operator-supplied published rationale lands (this is how
          the Balkrishna episode happened: the PDF was shared for comparison, and its framing
          then migrated into the correction pass);
      (b) the SAME-ISSUER file in the reference library - which failure mode 29 requires be
          opened at Step 7b, well before drafting.
    The library holds ~2,100 files, so (b) is matched on FILENAME first and only matching
    files are read. A candidate must contain EVERY significant issuer token, which is what
    keeps "Indus" from matching "Industries" (failure mode 24).
    """
    if case_dir is None:
        # A rationale outside any case folder and unmatched by resolve_case_dir - e.g. a
        # scratch copy used to test a single probe. Every other case_dir use in audit() is
        # already guarded with `if case_dir is not None`; this one was not, and crashed with
        # AttributeError: 'NoneType' object has no attribute 'iterdir' instead of just skipping
        # the probe (there is no case folder to scan for agency publications).
        return []
    out = []
    for f in sorted(case_dir.iterdir()):
        if not f.is_file() or f.suffix.lower() not in (".md", ".txt"):
            continue
        if "rating rationale" in f.name.lower() or f.name in (
                "GATES.md", "COMPANY_CONTEXT.md", "RATING_REQUEST.md"):
            continue
        try:
            txt = f.read_text(encoding="utf-8", errors="replace")
        except Exception:                                        # noqa: BLE001
            continue
        if _AGENCY_SIGNATURE.search(txt):
            out.append((f.name, txt))

    tokens = _issuer_tokens(rationale_name)
    if tokens:
        for lib in (ROOT / "Report for Reference", ROOT / "CRISIL" / "Report for Reference",
                    ROOT / "CareEdge" / "Report for Reference"):
            if not lib.is_dir():
                continue
            for f in sorted(lib.iterdir()):
                if not f.is_file() or f.suffix.lower() not in (".md", ".txt"):
                    continue
                low = f.name.lower()
                if not all(re.search(r"\b" + re.escape(tok), low) for tok in tokens):
                    continue
                try:
                    out.append((f"{lib.name}/{f.name}",
                                f.read_text(encoding="utf-8", errors="replace")))
                except Exception:                                # noqa: BLE001
                    continue
    return out


# ---------------------------------------------------------------------------------------
# BLOCKING PROBES - a quality probe that STOPS delivery rather than merely warning.
#
# Every probe was a WARN until 13-Sep-2026: it printed, the case still passed, and a person
# was trusted to act on it. Failure mode 35 is the record of what that costs - an omission
# that is *disclosed* reads as a considered decision rather than an unexamined default, so
# nobody challenges it and it repeats next time. The corpus run that promoted the first entry
# below is the same story in miniature: three cases tripped the business-risk gate, printed
# the warning, and still read READY TO SHARE.
#
# Promotion is deliberate and narrow. Add a label here only when BOTH hold:
#   (a) the failure mode it guards has produced a real notch error, not a tidiness complaint;
#   (b) the remedy is a bounded, writable act - set a value, or state in writing why none
#       applies - never an open-ended analytical judgement a script cannot tell is finished.
# Condition (b) is what keeps this list honest: a blocking probe an analyst cannot clear by
# doing something specific is not a gate, it is an obstruction, and it will be worked around.
BLOCKING_PROBES = (
    # FM53 - Cochin Minerals. Averaging business risk into the numeric financial composite
    # carried the Stage 1 anchor to AA- on gearing 0.04x and interest coverage 122x, against
    # CareEdge's published BBB. Clearable by setting Inputs!C69 (ceiling grade) or writing in
    # Inputs!D69 why no ceiling applies - both bounded acts, so condition (b) holds.
    "Business-risk gate applied or waived in writing",
    # FM20/24/29 - Cochin Minerals. The entry gate reported the agency's own action
    # PRESENT and printed its rated amounts; the report asserted the opposite three
    # times and thereby skipped Step 14, producing a two-notch miss. Clearable by
    # deleting the false claim or by writing the correction note that supersedes it,
    # so condition (b) holds.
    "Prior-rating absence-claim contradicted by the reference library",
)


def _is_blocking(label: str) -> bool:
    """True when this probe's label stops delivery rather than warning."""
    return any(label.startswith(b) for b in BLOCKING_PROBES)


PROBES = [
    ("No unfilled analyst placeholders (build_rationale.py drafts)",
     lambda t: not _unfilled_placeholders(t),
     "This is a GENERATED DRAFT with judgement calls still unfilled. build_rationale.py fills "
     "every figure from the verified engine and marks every judgement as [ANALYST: ...]; each "
     "one must be replaced with actual analysis before the report can be delivered. "
     "Outstanding: "),
    ("Absence-claims are evidenced (failure mode 20)",
     lambda t: not _absence_claims_unevidenced(t),
     "The report asserts data is 'not available/not disclosed/not extractable' WITHOUT showing "
     "the search that proves it. Run the grep and record pattern+file+zero-hits, or write "
     "'not extracted in this pass'. Offending phrase(s): "),
    ("Sector-defining metric present (failure mode 21)",
     lambda t: _missing_sector_kpi(t) is None,
     "The report covers a sector whose defining operating metric is missing: "),
    ("ESG section carries a quantified figure",
     lambda t: (not _section_body(t, r"(esg|environmental and social)")
                or re.search(r"\d", _section_body(t, r"(esg|environmental and social)")) is not None),
     "ESG section present but contains no number - the format expects company-disclosed metrics "
     "(emissions, renewable MW, LTIFR, diversity %, board composition)."),
    ("Liquidity descriptor named",
     lambda t: re.search(r"liquidity[^\n]{0,40}(superior|strong|adequate|stretched|poor)", t, re.I) is not None,
     "Liquidity section present but no Superior/Strong/Adequate/Stretched/Poor descriptor - the "
     "descriptor is the conclusion of the arithmetic and must be stated."),
    # Accept the rupee SYMBOL as well as "Rs" - CareEdge writes amounts as "₹94.00 crore" and
    # heads its own tables "Amount (₹ crore)". An Rs-only pattern failed a report that stated the
    # amounts correctly in CareEdge house style (19-Aug-2026).
    ("Rated amount stated or explicitly TBC",
     lambda t: re.search(r"to be confirmed by issuer|(rs\.?|₹)\s*\*{0,2}[\d,]{2,}(\.\d+)?\s*\*{0,2}\s*(crore|cr\b)",
                         t, re.I) is not None,
     "Annexure I neither states an amount nor marks it 'to be confirmed by issuer'."),
    ("Data cutoff / as-on date stated",
     lambda t: re.search(r"data cutoff|cut[- ]off|as on \w+ \d|as at \w+ \d|data as", t, re.I) is not None,
     "No data cutoff or as-on date stated."),
    ("Not-an-official-publication disclaimer",
     lambda t: re.search(r"not an official|not.{0,25}publication of", t, re.I) is not None,
     "Missing the 'not an official CRA publication' disclaimer."),
    # ---- failure modes 31-34, added 20-Aug-2026 after the HDFC Securities comparison ---------
    ("Rating table states limits, not outstandings (failure mode 31)",
     lambda t: _rating_table_uses_outstandings(t) is None,
     "The Rating Action table quotes an OUTSTANDING balance. A rating attaches to a SANCTIONED "
     "FACILITY, not a drawdown - state the rated limit or 'to be confirmed by issuer', and move "
     "outstandings to Brief Financials / Liquidity. Offending text: "),
    ("No-outlook claim not contradicted (failure mode 31)",
     lambda t: _no_outlook_contradicted(t) is None,
     "The report says no outlook is assigned, yet carries a long-term rating with one. Never "
     "infer the absence of a long-term rating from the absence of long-term DRAWN debt. Found: "),
    ("Financial-sector net-worth basis stated (failure mode 32)",
     lambda t: not _networth_basis_unstated(t),
     "Gearing or return on net worth is quoted without naming the net-worth basis. CareEdge uses "
     "TANGIBLE net worth (equity less deferred tax assets and intangibles) and includes non-fund"
     "-based limits utilised in gearing - see CareEdge/BROKING_CONVENTIONS.md."),
    ("Broking metric set complete (failure mode 33)",
     lambda t: _broking_missing_careedge_metrics(t) is None,
     "A broking report is missing rows CareEdge reports as standard. A metric may be excluded "
     "only after checking a published report of THAT agency in THAT sector. Missing: "),
    # FM14 guards condition (2) of the five-condition amendment, which every CareEdge rated
    # amount now relies on. An undated CRA table is indistinguishable from a stale one.
    ("CRA-published amounts carry a publication date (failure mode 14)",
     _cra_amounts_dated,
     "The report attributes amounts to a CRA publication without stamping that publication's "
     "DATE beside the attribution. An undated CRA table cannot be told apart from a stale one "
     "(condition (2) of the five-condition amendment)."),
    ("CRA-published amounts are CURRENT, not merely dated (failure mode 14)",
     lambda t: _cra_amount_stale(t) is None,
     "The report carries a CRA-published rated amount whose publication date is more than 180 "
     "days before this report's own date, while the report ITSELF describes a divestment, "
     "prepayment, acquisition or capacity change in the interval. A stamped date proves "
     "provenance, not freshness. Re-confirm the limits or mark them 'to be confirmed by "
     "issuer'. Stale attribution: "),
    ("Post-balance-sheet event treatment stated",
     lambda t: not _post_bs_event_untreated(t),
     "The report describes a divestment, slump sale, acquisition or major prepayment without "
     "stating WHETHER the rated-period figures reflect it. An event completed after the "
     "balance-sheet date cannot have moved that balance sheet; describing it in the past tense "
     "as having done so misstates the period AND destroys a forward catalyst."),
    ("Annexure I lines sum to their total (failure modes 12/23)",
     lambda t: not _line_integrity_breaks(t),
     "A facility total does not equal the lines beneath it. An invented or mis-split line is "
     "invisible to every other check - the report reads correctly and the arithmetic is wrong. "
     "Break(s): "),
    ("Liquidity uses unencumbered cash (failure mode 34, all sectors)",
     lambda t: not _liquidity_encumbrance(t),
     "The Liquidity section quotes a cash figure without establishing it is "
     "UNENCUMBERED. Margin money, earmarked deposits, DSRA and client balances are not "
     "available to service company debt. Dhampur Bio Organics quoted Rs 36.16 crore of 'cash "
     "and bank' where the agency found Rs 4.5 crore of free cash - an ~8x overstatement, on a "
     "sugar company, which the old broking-only scoping could not see."),
    ("Operating-profit normalisation stated (failure mode 36)",
     lambda t: not _opm_normalisation_unstated(t),
     "An operating-profit measure (OPBDIT/OPBDITA/PBILDT/EBITDA) is quoted without naming how "
     "forex and one-off items inside the Other Income / Other Expenses notes were treated. "
     "Those notes are COMPOSITES: the same forex item sits in Other Income when it is a gain "
     "and Other Expenses when it is a loss, so 'less other income' strips gains but keeps "
     "losses and manufactures a margin decline. Run preflight probe [0c], then state the "
     "include/exclude decision. 'No exceptional item was disclosed' does not count - a forex "
     "loss is not captioned exceptional."),
    # ---- failure modes 47, 51, 52, added 13-Sep-2026 after Cochin Minerals and the completed
    # ICRA/CRISIL Banks & NBFC methodology read ---------------------------------------------
    ("Total-debt basis stated for agencies that fold in LC creditors (failure mode 47)",
     lambda t: not _total_debt_basis_unstated(t),
     "Gearing is quoted and non-fund-based facilities (LC/BG/acceptances) are disclosed "
     "somewhere in the document, but the two are never connected. This agency's own Total Debt "
     "definition includes LC-backed acceptances/creditors (CareEdge/CRISIL) - see "
     "CareEdge/CORPORATE_CONVENTIONS.md S10 or CRISIL/CRISIL_CONVENTIONS.md S3. Cochin Minerals: "
     "statutory gearing 0.04x against CareEdge's published 0.31x, the gap being ~47 crore of "
     "LC-backed creditors the extraction omitted."),
    ("LT-ST mapping matches this agency's own table",
     lambda t: _lt_st_mapping_mismatch(t) is None,
     "The report's stated long-term/short-term rating pair does not match the agency's own "
     "mapping table. ICRA's table (mapping.md) has two FIXED anchors; CRISIL's table "
     "(basics-of-ratings.md) varies BY ENTITY CLASS at the same long-term grade. Do not apply "
     "one agency's table (or one entity class's row) to another. Mismatch: "),
    ("Hybrid-instrument cap not conflated across agencies (failure mode 51)",
     lambda t: _hybrid_cap_conflated(t) is None,
     "A hybrid-instrument cap percentage is cited that belongs to a DIFFERENT agency/entity "
     "class. ICRA's corporate cap is 30% of adjusted equity; CRISIL's NBFC/HFC cap is 15% of "
     "Tier I capital - numerically similar-looking, not interchangeable. Found: "),
    ("Asset-quality improvement addresses write-offs (failure mode 59)",
     lambda t: _asset_quality_improvement_without_writeoffs(t) is None,
     "Writing loans off removes them from every delinquency bucket, so a lender that writes "
     "off aggressively shows a better dpd profile for no credit reason. State write-offs net "
     "of recoveries, or state that they were nil. Found: "),
    ("Expected-loss rating matches its stated loss estimate (failure mode 58)",
     lambda t: _el_band_mismatch(t) is None,
     "CRISIL publishes numeric EL bands (EL1 <=1.25%, EL2 <=3.5%, EL3 <=7.5%, EL4 <=15%, "
     "EL5 <=25%, EL6 <=35%, EL7 >35%), so an EL grade and a stated loss estimate are "
     "reconcilable arithmetic. Found: "),
    ("Outlook not assigned to a C or D category rating (failure mode 54)",
     lambda t: _outlook_on_c_or_d(t) is None,
     "CRISIL assigns outlooks to long-term ratings barring the C and D categories, and never "
     "to short-term ratings or to a rating on Watch (basics-of-ratings.md Section I). Found: "),
    ("Real-estate developer assessed on CRISIL's own CFO ratio set (failure mode 60)",
     lambda t: _real_estate_wrong_ratio_set(t) is None,
     "CRISIL does NOT rate a residential/commercial-for-sale developer on accrual interest "
     "coverage or ordinary gearing. It publishes CFO (adjusted) = collections - construction "
     "cost - other operating expenses - JV/JDA outflows, and assesses Debt/CFO, CFO/interest, "
     "the cash buffer ratio and the adequacy of committed receivables; leverage enters only as "
     "a structural anchor inside financial flexibility. Accrual coverage is negative BY "
     "CONSTRUCTION under project-completion accounting - on Godrej Properties an accrual "
     "coverage cap manufactured nine of twelve notches of apparent divergence. See "
     "CRISIL/CRISIL_REAL_ESTATE_CONVENTIONS.md. Found: "),
    ("Global-scale rating mapped before use on the national scale (failure mode 61)",
     lambda t: _global_scale_unmapped(t) is None,
     "A global rating agency's grade is cited in a parent/support context with no statement "
     "that the two scales differ. CRISIL: a global-scale rating 'tends to map to a rating on "
     "the Crisil Ratings scale which is typically 6 to 7 notches higher' (S&P BBB+ -> Crisil "
     "AAA/AA+; S&P B -> Crisil BB+/BB), narrowing at the lower end, and the mapping uses the "
     "global-scale LOCAL CURRENCY rating. ICRA maps from Moody's instead and publishes NO "
     "notch count, so CRISIL's 6-7 must not be carried onto an ICRA case. Found: "),
    ("Infrastructure-SPV support notching within CRISIL's stated norm (failure mode 52)",
     lambda t: _infra_spv_notch_excessive(t) is None,
     "CRISIL states its own default is NOT to notch up an infrastructure SPV for parent "
     "support, or to do so by at most 1-2 notches, because such SPVs are deliberately "
     "structured as ring-fenced and limited-recourse. A larger uplift needs an explicit written "
     "exception, not general 'strong linkage' language. Found: "),
]


def audit(path: Path):
    t = path.read_text(encoding="utf-8", errors="replace")
    hs = headers(t)
    agency = detect_agency(path, t)
    missing_req, missing_opt, probes_failed = [], [], []
    for label, pats, mandatory in SECTIONS:
        found = any(re.search(p, h, re.I) for h in hs for p in pats)
        if found:
            continue
        if isinstance(mandatory, str):            # agency-specific requirement
            if agency == mandatory and not NO_OUTLOOK_RE.search(t):
                missing_req.append(f"{label} [{agency} format]")
            continue
        if mandatory is None:                     # conditional
            if not NO_OUTLOOK_RE.search(t):
                missing_req.append(label + " (and no 'no outlook assigned' statement)")
            continue
        (missing_req if mandatory else missing_opt).append(label)
    # An unfilled generated draft trips half a dozen probes on the GUIDANCE TEXT inside its
    # own placeholders - the instruction "'No exceptional item was disclosed' is an absence
    # claim" is itself matched by the absence-claim probe, and so on. That cascade buries the
    # one thing the author needs to read. While placeholders remain, report only that.
    _draft_unfilled = bool(_unfilled_placeholders(t))
    for label, fn, msg in PROBES:
        if _draft_unfilled and "unfilled analyst placeholders" not in label:
            continue
        try:
            if not fn(t):
                detail = ""
                if "Absence-claims" in label:
                    detail = " | ".join(f'"…{c}…"' for c in _absence_claims_unevidenced(t))
                elif "Sector-defining" in label:
                    detail = _missing_sector_kpi(t) or ""
                elif "limits, not outstandings" in label:
                    detail = f'"…{_rating_table_uses_outstandings(t)}…"'
                elif "No-outlook" in label:
                    detail = f'"{_no_outlook_contradicted(t)}"'
                elif "Broking metric set" in label:
                    detail = _broking_missing_careedge_metrics(t) or ""
                elif "CRA-published amounts are CURRENT" in label:
                    _st = _cra_amount_stale(t)
                    detail = ("\"%s\", %d days before this report" % (_st[0], _st[1])) if _st else ""
                elif "sum to their total" in label:
                    detail = " | ".join(_line_integrity_breaks(t))
                elif "LT-ST mapping matches" in label:
                    detail = _lt_st_mapping_mismatch(t) or ""
                elif "Hybrid-instrument cap not conflated" in label:
                    detail = _hybrid_cap_conflated(t) or ""
                elif "Infrastructure-SPV support notching" in label:
                    detail = _infra_spv_notch_excessive(t) or ""
                elif "Outlook not assigned to a C or D" in label:
                    detail = _outlook_on_c_or_d(t) or ""
                elif "Expected-loss rating matches" in label:
                    detail = _el_band_mismatch(t) or ""
                elif "Asset-quality improvement addresses write-offs" in label:
                    detail = _asset_quality_improvement_without_writeoffs(t) or ""
                elif "unfilled analyst placeholders" in label:
                    _ph = _unfilled_placeholders(t)
                    detail = "%d outstanding - %s" % (
                        len(_ph), "; ".join(x[:56] for x in _ph[:4]))
                probes_failed.append((label, msg + detail))
        except Exception as e:
            probes_failed.append((label, f"probe error: {e}"))

    # ---- prior-rating absence contradicted by the library (failure modes 20/24/29) --------
    # BLOCKING. Needs the filename, so it sits outside the PROBES loop, which only sees text.
    _pa = _prior_rating_absence_contradicted(t, path.name)
    if _pa:
        probes_failed.append((
            "Prior-rating absence-claim contradicted by the reference library "
            "(failure modes 20/24/29)", _pa))

    # ---- Step 12 / 12b: projections either BUILT or explicitly SCOPED (failure mode 35) ----
    # Diagnosed 21-Aug-2026. The last forecast model was built 14-Aug (SBI); every case
    # delivered from 15-Aug onward had none - TVS Credit, NABKISAN, Riba, Gujarat Energy,
    # HDFC Securities, Aptus. The cause was not missing documents (all six cases that DID get
    # a model had no sector document either). It was BATCH MODE: asked to "process the pending
    # rating requests", the minimum coherent package gets shipped and Step 12 silently drops.
    # Disclosing the omission in the delivery scope made it read as a decision rather than a
    # default. The SOP already requires the scaling decision to be RECORDED - so require it.
    case_dir = resolve_case_dir(path)
    if case_dir is not None and (case_dir / "case.json").exists():
        try:
            import json
            cj = json.loads((case_dir / "case.json").read_text(encoding="utf-8"))
            names = [f.name.lower() for f in case_dir.iterdir() if f.is_file()]
            has_model = any(f.endswith(".xlsx") and ("model" in f or "forecast" in f)
                            for f in names)
            has_score = any(f.endswith(".xlsx") and "scorecard" in f for f in names)
            scoped = str(cj.get("step12_scaling_decision", "")).strip()
            if not (has_model and has_score) and len(scoped) < 40:
                missing = []
                if not has_model:
                    missing.append("no forecast model")
                if not has_score:
                    missing.append("no filled Rating_Scorecard")
                probes_failed.append((
                    "Step 12 projections built or scoped (failure mode 35)",
                    f"{' and '.join(missing)} in the case folder, and case.json carries no "
                    "'step12_scaling_decision'. Step 12 is PROPORTIONATE, not optional: corporate "
                    "-> 5-yr 3-statement model; bank/NBFC/HFC -> LENDING model (book growth -> NII "
                    "-> credit cost -> PAT); CP-only or stable IG surveillance -> a focused "
                    "sensitivity on the 2-3 rating-driving variables. Whichever applies, the SOP "
                    "requires the scaling decision to be RECORDED. Build it, or write why a lighter "
                    "treatment is right."))
        except Exception as e:
            probes_failed.append(("Step 12 projections built or scoped (failure mode 35)",
                                  f"could not read case.json: {e}"))

    # ---- the filled scorecard must be READABLE, not just filled ---------------------------
    # openpyxl cannot evaluate formulas, and on save it writes every formula cell as
    # `<f>..</f><v></v>` - formula kept, cached result EMPTY. Excel hides this by recalculating
    # on load; nothing else does. The webapp preview, LibreOffice, Google Sheets and pandas all
    # read the cached value, so a correctly filled scorecard renders blank from the Ratios sheet
    # down to the final grade. Found 01-Sep-2026 when a delivered workbook "was not filled
    # properly": the inputs were right and every computed cell was empty.
    #   Fix:  python recalc_workbook.py --all-scorecards
    if case_dir is not None:
        for book in sorted(case_dir.glob("Rating_Scorecard*.xlsx")):
            try:
                from openpyxl import load_workbook
                wf = load_workbook(book)
                wv = load_workbook(book, data_only=True)
                blank = 0
                for nm in wf.sheetnames:
                    a, b = wf[nm], wv[nm]
                    for row in a.iter_rows():
                        for c in row:
                            if (isinstance(c.value, str) and c.value.startswith("=")
                                    and b[c.coordinate].value is None):
                                blank += 1
                if blank:
                    probes_failed.append((
                        "Scorecard carries cached values, not just formulas",
                        f"{book.name} has {blank} formula cell(s) with NO cached value. The "
                        f"workbook opens correctly in Excel, which recalculates, but renders "
                        f"blank in every other viewer - including this project's own webapp "
                        f"preview - so the anchor grade is invisible to the reader. Run: "
                        f"python recalc_workbook.py --all-scorecards"))
            except Exception as e:                                        # noqa: BLE001
                probes_failed.append(("Scorecard carries cached values, not just formulas",
                                      f"could not read {book.name}: {e}"))

    # ---- the scorecard must not read as an assigned rating --------------------------------
    # The workbook prints its anchor under "Rating line (agency house style)", formatted exactly
    # like a rating. Opened beside a rationale carrying a different grade - B- against A- on
    # Vodafone Idea - it reads as a contradiction, and that is the first thing a reader asks.
    # The anchor is DELIBERATELY standalone (support notches zero) so divergence must be argued
    # rather than absorbed; but that design lived only in the workpaper, which is the wrong
    # place for it. A document that can be opened on its own has to explain itself on its own.
    #   Fix:  python annotate_scorecard.py --all
    if case_dir is not None:
        import re as _re
        _grade = _re.compile(r"(?:\[ICRA\]|Crisil\s+|CARE\s+)"
                             r"(AAA|AA[+-]|AA|A[+-]|A|BBB[+-]|BBB|BB[+-]|BB|B[+-]|B|C)"
                             r"(?![A-Za-z0-9+-])")
        _m = _grade.search(t[:1200])
        rationale_grade = _m.group(1) if _m else None
        for book in sorted(case_dir.glob("Rating_Scorecard*.xlsx")):
            try:
                from openpyxl import load_workbook
                wv = load_workbook(book, data_only=True)
                if "Rating" not in wv.sheetnames:
                    continue
                ws = wv["Rating"]
                # ---- Stage 3 of the workbook must EQUAL the rationale -------------------
                # Restructured 02-Sep-2026 on operator instruction: the sheet's headline is now
                # the ASSIGNED rating, derived on-sheet as
                #     Stage 1 financial anchor -> Stage 2 justified overlay -> Stage 3 assigned.
                # Before that change the workbook printed only the anchor, so a reader opening
                # it beside the report saw two unrelated grades (Vodafone Idea B- vs A-, Godrej
                # Properties B+ vs AA+). This probe is the mechanical half of the fix.
                assigned_grade = ws["C32"].value
                assigned_line = ws["C36"].value
                divergence = ws["C34"].value
                cap_text = str(ws["C14"].value or "")

                if assigned_grade is None:
                    probes_failed.append((
                        "Scorecard Stage 3 states an assigned rating",
                        f"{book.name} has no Stage 3 assigned rating (cell C32 is empty). The "
                        f"workbook has not been rebuilt to the three-stage layout, or its "
                        f"cached values were never written. Run: "
                        f"python tools/restructure_scorecard.py, refill, then "
                        f"python tools/annotate_scorecard.py --all"))
                elif rationale_grade:
                    # An issuer rated on the SHORT-TERM scale alone (ITC's ICRA and CareEdge
                    # mandates are each a single commercial-paper programme, "[ICRA]A1+", with
                    # no long-term grade anywhere) must be compared against the sheet's
                    # short-term grade. Comparing a CP rating to a long-term grade reports a
                    # mismatch that is an artefact of the comparison, not of the workbook.
                    _ST = {"A1+", "A1", "A2+", "A2", "A3+", "A3", "A4+", "A4"}
                    if rationale_grade in _ST:
                        got = str(ws["C33"].value or "").strip()
                    else:
                        got = str(assigned_grade).strip()
                    if got != rationale_grade:
                        probes_failed.append((
                            "Scorecard assigned rating equals the rationale",
                            f"{book.name} Stage 3 assigns '{assigned_line}' (grade {got}) but "
                            f"this report's headline grade is '{rationale_grade}'. These are "
                            f"the SAME decision and must not differ. Either the Stage 2 "
                            f"overlay on the Inputs sheet does not bridge the anchor to the "
                            f"committee's grade, or the report and the workbook are out of "
                            f"step. Resolve on the sheet - do not restate the grade in prose."))

                # A notch of divergence with no written reason is the defect the overlay exists
                # to prevent; an unexplained bridge is no better than the old silent one.
                try:
                    div = float(divergence or 0)
                except (TypeError, ValueError):
                    div = 0.0
                if abs(div) > 0:
                    wi = wv["Inputs"]
                    unjustified = []
                    for r in range(60, 65):
                        n = wi.cell(row=r, column=3).value
                        why = str(wi.cell(row=r, column=4).value or "").strip()
                        try:
                            n = float(n or 0)
                        except (TypeError, ValueError):
                            n = 0.0
                        if abs(n) > 0 and len(why) < 20:
                            unjustified.append("Inputs!C%d" % r)
                    if unjustified:
                        probes_failed.append((
                            "Every overlay notch carries a justification",
                            f"{book.name} bridges {div:g} notch(es) from anchor to assigned "
                            f"rating, but {', '.join(unjustified)} carr(y) notches with no "
                            f"written reason beside them. A notch without a reason is an "
                            f"assertion, not an argument."))

                # Disapplying a hard cap is a real analytical act and must be defended in
                # writing - see Godrej Properties, where the accrual-coverage cap was firing on
                # an artefact of project-completion accounting.
                if "DISAPPLIED" in cap_text.upper():
                    reason = str(wv["Inputs"]["D67"].value or "").strip()
                    if len(reason) < 40:
                        probes_failed.append((
                            "Hard-cap disapplication is justified in writing",
                            f"{book.name} disapplies the scorecard's hard caps "
                            f"(Inputs!C67 = 'N') but Inputs!D67 carries no adequate written "
                            f"reason. A cap may be disapplied only where the metric it tests is "
                            f"structurally meaningless for the sector, and that has to be "
                            f"stated and evidenced."))

                # ---- business-risk gate (failure mode 53) ----------------------------
                # Added 13-Sep-2026 after Cochin Minerals. Scorecard!E22 averages the
                # business-risk score into the same composite as the financial ratios, which
                # neither ICRA's nor CareEdge's methodology does - both band Financial Risk
                # numerically and assess Business Risk descriptively only. Where business
                # risk is materially weaker than financial risk, that averaging is what lets
                # a debt-free small issuer's ratios outvote the business weakness. The sheet
                # raises the flag; a ceiling (or a written reason for none) is the analyst's.
                try:
                    ssc = wv["Scorecard"]
                    gate = str(ssc["C42"].value or "")
                    if gate.strip().upper().startswith("YES"):
                        ceiling = str(wv["Inputs"]["C69"].value or "").strip()
                        why = str(wv["Inputs"]["D69"].value or "").strip()
                        if ceiling in ("", "0") and len(why) < 40:
                            probes_failed.append((
                                "Business-risk gate applied or waived in writing "
                                "(failure mode 53)",
                                f"{book.name}: business risk scores "
                                f"{ssc['C39'].value} against financial risk "
                                f"{ssc['C40'].value} - weaker by "
                                f"{ssc['C41'].value}, so the Stage 1 composite is averaging "
                                f"a descriptive business judgement against numeric financial "
                                f"bands. Set a ceiling grade in Inputs!C69, or state in "
                                f"Inputs!D69 why no ceiling applies. Leaving both blank is "
                                f"the Cochin Minerals defect: anchor AA- on gearing 0.04x "
                                f"and coverage 122x, against CareEdge's published BBB."))
                except KeyError:
                    pass    # workbook predates the gate; add_business_risk_gate.py adds it
            except Exception as e:                                        # noqa: BLE001
                probes_failed.append(("Scorecard Stage 3 states an assigned rating",
                                      f"could not read {book.name}: {e}"))

    # ---- analytical basis vs the same-issuer CRA action ----------------------------------
    # Added 13-Sep-2026. Dhampur Bio Organics was rated CONSOLIDATED against CareEdge's
    # STANDALONE, and the report asserted the basis was "methodology-determined, not elective"
    # while never opening the consolidation criteria - a prose claim of compliance that the
    # gate accepted AS compliance. The agency's own prior action for the same issuer was in the
    # reference library, was flagged PRESENT by the pre-flight, and states its basis on its
    # face. Both bases are internally self-consistent, so no tie-out and no coverage figure can
    # ever separate them; the only mechanical discriminator available is what the agency itself
    # did for this issuer. Differing is permitted - silently differing is not.
    _mine = re.search(r"analytical approach:?\**\s*:?\**\s*(standalone|consolidated|combined)",
                      t, re.I)
    # The intake selector is only as good as the check behind it. The operator declares the
    # basis when the case is created (webapp -> case.json "basis"); this is what stops the
    # declaration and the delivered report drifting apart without anyone noticing.
    if case_dir is not None and (case_dir / "case.json").is_file():
        try:
            _declared = str(json.loads((case_dir / "case.json").read_text(encoding="utf-8"))
                            .get("basis", "")).strip().lower()
        except Exception:                                                 # noqa: BLE001
            _declared = ""
        if _declared and _declared != "undecided":
            if not _mine:
                probes_failed.append((
                    "Analytical basis stated and matches the case declaration",
                    "case.json declares the basis as '%s', but the report states no "
                    "'Analytical approach'. The basis must appear on the face of the report."
                    % _declared))
            elif _mine.group(1).lower() != _declared:
                probes_failed.append((
                    "Analytical basis stated and matches the case declaration",
                    "The report is on a %s basis but this case was created declaring %s. One of "
                    "the two is wrong. Both bases are internally self-consistent, so no tie-out "
                    "and no coverage figure can tell them apart - this comparison is the only "
                    "mechanical check there is."
                    % (_mine.group(1).lower(), _declared)))
    if _mine and case_dir is not None:
        for _src_name, _src_text in find_agency_publications(case_dir, path.name):
            _theirs = re.search(
                r"analytical approach:?\**\s*:?\**\s*(standalone|consolidated|combined)",
                _src_text, re.I)
            if not _theirs:
                continue
            if _theirs.group(1).lower() == _mine.group(1).lower():
                continue
            if re.search(r"basis differs|differ(s|ent) from the (agency|prior|published)"
                         r"|depart(s|ure) from the (agency|prior)|why this basis differs"
                         r"|whereas the (agency|prior|published)", t, re.I):
                continue
            probes_failed.append((
                "Analytical basis differs from the agency's own action, unexplained",
                "This report is on a %s basis; %s - the same agency's published action for "
                "this issuer - is on a %s basis, and the report does not say why it differs. "
                "The basis is methodology-determined (R12), so a divergence is a finding that "
                "must be argued from the consolidation criteria, not left silent. Both bases "
                "are internally consistent, so no tie-out can detect this."
                % (_mine.group(1).lower(), _src_name, _theirs.group(1).lower())))

    # ---- no verbatim reuse of an agency publication (failure mode 37) --------------------
    for src_name, src_text in find_agency_publications(case_dir, path.name):
        shared = _shared_ngrams(t, src_text)
        if shared:
            shared.sort(key=len, reverse=True)
            shown = "; ".join('"%s"' % s[:150] for s in shared[:3])
            probes_failed.append((
                "No verbatim reuse of an agency publication (failure mode 37)",
                f"{len(shared)} run(s) of {_NGRAM_N}+ consecutive words shared with "
                f"{src_name}, which is an agency-published report. Under CLAUDE.md section 2 "
                f"a published rationale may teach craft but may never supply a fact, a "
                f"figure, a driver or a phrasing to a new report. Rewrite the passage from "
                f"the issuer's own documents and your own computed output. Longest: {shown}"))

    # ---- peer row set, written by preflight.py probe [1b] --------------------------------
    # Surfacing is not verifying. preflight PRINTS the row set the agency uses in this sector
    # and persists it here; this check confirms the delivered report actually carries it.
    # Without this, [1b] is advice - and advice is what failed on HDFC Securities, where two
    # peer reports carrying every required row sat unopened in the reference library.
    peer_file = path.parent / "peer_rows.json"
    if peer_file.exists():
        try:
            import json
            meta = json.loads(peer_file.read_text(encoding="utf-8"))
            # Compare with ALL whitespace removed. Peer labels come from PDF extraction, which
            # routinely drops spaces - "On-bookgearing (x)", "Profit after tax(PAT)". Matching
            # on spaced text alone reported "On-bookgearing" missing from a report that states
            # "On-book gearing" plainly (Aptus, 21-Aug-2026): a false positive that would train
            # the reader to ignore this check.
            norm = lambda s: re.sub(r"[^a-z0-9]+", "", s.lower())
            flat = norm(t)
            missing = []
            for row in meta.get("required_rows", []):
                # "Loan book (Margin Trading Facility)" -> accept the stem OR the parenthetical,
                # since reports abbreviate ("Loan book (MTF)"). Units (x)/(%) are not terms.
                alts = [a for a in re.split(r"[()]", row) if norm(a) and norm(a) not in ("x", "")]
                if not any(norm(a) in flat for a in alts):
                    missing.append(row)
            if missing:
                probes_failed.append((
                    "Peer row set present (failure modes 32/33)",
                    f"Rows that {meta.get('agency')} uses for this sector are absent. Source peer:"
                    f" {meta.get('peer')}. Missing: " + "; ".join(missing)))

            # ---- deviation from the peer norm must be JUSTIFIED, not silent (FM31) --------
            # This is the only check aimed at a REASONING error rather than a lookup. It does
            # not evaluate the reasoning - it detects that the conclusion is unusual for the
            # sector and demands the report say why.
            n, lt = meta.get("peers_sampled", 0), meta.get("peers_with_long_term_rating", 0)
            if n and lt > n / 2:
                has_lt = re.search(r"(AAA|AA[+-]?|A[+-]?|BBB[+-]?)\s*;\s*"
                                   r"(Stable|Positive|Negative)", t)
                # A justification must ACKNOWLEDGE the deviation. "No outlook is assigned" is
                # not one - on HSL that sentence WAS the error, restated. Accepting it would
                # have let the very report this check exists for pass unchallenged.
                justified = re.search(
                    r"searched[^.]{0,60}no long[- ]term|deviat|unlike (its |most )?peers"
                    r"|differs from (the )?peer|no long[- ]term facility (exists|is sanctioned)"
                    r"|issuer has no sanctioned long[- ]term", t, re.I)
                if not has_lt and not justified:
                    probes_failed.append((
                        "Peer-norm deviation justified (failure mode 31)",
                        f"{lt} of {n} peers in this sector carry a LONG-TERM rating, but this "
                        "report assigns none and does not say why. A rating attaches to a "
                        "SANCTIONED FACILITY - never conclude no long-term rating exists from "
                        "the absence of long-term DRAWN debt. Either assign one or state the "
                        "deviation explicitly."))
        except Exception as e:
            probes_failed.append(("Peer row set present (failure modes 32/33)",
                                  f"could not read peer_rows.json: {e}"))
    return missing_req, missing_opt, probes_failed


def main(argv):
    # CareEdge house style uses the rupee SYMBOL, and probe details quote report text.
    # On a cp1252 console that raised UnicodeEncodeError and killed the whole audit
    # mid-report (20-Aug-2026). Reconfigure once here rather than sanitising each print.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    # Rationales used to be filed loose at the project root; they now live in their own
    # Companies/<slug>/ folder (organised 01-Sep-2026), so both locations are globbed - a
    # rationale dropped straight at root (e.g. before a case folder exists) must still be found.
    files = [Path(a) for a in argv[1:]] or sorted(
        set(p for p in ROOT.glob("*Rating Rationale*.md") if p.is_file())
        | set(p for p in ROOT.glob("Companies/*/*Rating Rationale*.md") if p.is_file()))
    if not files:
        print("No rationale files found.")
        return 0
    bad = 0
    print(f"Section-completeness audit - {len(files)} rationale(s)\n" + "=" * 78)
    blocked = 0
    for f in files:
        req, opt, probes = audit(f)
        # A blocking probe fails the case exactly as a missing mandatory section does. It
        # is still reported under its own label so the reader can tell the two apart: one
        # says a section is absent, the other says a decision was never made.
        blocking = [(l, m) for l, m in probes if _is_blocking(l)]
        warns = [(l, m) for l, m in probes if not _is_blocking(l)]
        status = "FAIL" if (req or blocking) else ("WARN" if warns else "PASS")
        bad += 1 if (req or blocking) else 0
        blocked += 1 if (blocking and not req) else 0
        print(f"\n[{status}] {f.name}")
        for m in req:
            print(f"    MISSING (mandatory): {m}")
        for label, msg in blocking:
            print(f"    BLOCKING: {label}\n             -> {msg}")
        for label, msg in warns:
            print(f"    QUALITY: {label}\n             -> {msg}")
        if opt:
            print(f"    (optional absent: {', '.join(opt)})")
        if not req and not probes:
            print("    all mandatory sections present; quality probes clean")
    print("\n" + "=" * 78)
    print(f"{len(files)-bad} passed, {bad} failed"
          + (f" ({bad-blocked} on mandatory sections, {blocked} on a blocking probe)."
             if blocked else " on mandatory sections."))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
