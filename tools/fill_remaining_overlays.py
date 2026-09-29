"""One-off: fill the Stage 2 committee overlay (Inputs!B60:D64) for every scorecard that was
migrated to the three-stage layout but never had its bridge written - the 11 cases outstanding
after Godrej Properties and Vodafone Idea were done individually. Each entry's justification is
grounded in that case's OWN already-delivered rationale (facts and figures already computed and
verified there), not invented for this pass. Run once; re-running just re-writes the same rows.

    python tools/fill_remaining_overlays.py
"""

import sys
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent

# {slug: {scorecard filename fragment or None for the only match: [(row 60..64, notches, why)]}}
OVERLAYS = {
    "apollo-tyres-limited": [
        (60, 0, "No sector-metric adjustment; the accrual metrics are meaningful for a "
                "manufacturer and were not disapplied."),
        (61, 1, "+1 for global scale and brand franchise the composite cannot see: "
                "732,097 MT produced in fiscal 2026 and sold in 100+ countries under the "
                "Apollo and Vredestein brands - a diversified, multi-geography manufacturing "
                "and distribution base a ratio grid reads only as one consolidated number."),
        (62, 0, "No incremental group-support notch beyond Step 12b."),
        (63, 0, "No peer-benchmarking adjustment."),
        (64, 0, "None."),
    ],
    "balkrishna-industries-ltd": [
        (60, 0, "No sector-metric adjustment."),
        (61, 1, "+1 - transcribed from this rationale's own Analytical Approach section: "
                "'a specialised global catalogue that sustains a 23.5-24.1% margin across "
                "three years, backward integration into the principal raw material, and a "
                "demonstrated capacity to fund a Rs 3,000 crore capital-expenditure year "
                "three-quarters from operating cash flow without moving gearing.' The "
                "governing calibration documents that the scorecard under-reads issuers at "
                "the AA+/AAA boundary absent this kind of qualitative overlay."),
        (62, 0, "No incremental group-support notch beyond Step 12b."),
        (63, 0, "Peer-agency consistency check (not a notch): CRISIL (27-Feb-2026) and "
                "CareEdge (05-Mar-2026) both independently rate BKT AA+ Stable, performed "
                "after this view was formed."),
        (64, 0, "None."),
    ],
    "creative-newtech-limited": [
        (60, 0, "No sector-metric adjustment."),
        (61, 2, "+2 for franchise factors the financial composite - which reads a sharp "
                "single-year leverage deterioration (gearing 0.23x to 0.84x, debt up 4.5x) - "
                "cannot offset on its own: an established two-decade distribution operating "
                "record, genuine exclusive principal relationships (national distribution for "
                "OM SYSTEM/Olympus, licensed Honeywell products), a footprint spanning South "
                "Asia, South-East Asia, the Middle East and Africa, and continued revenue "
                "momentum (52.1% FY2026 growth to Rs 2,700 crore, +21.2% in Q1 FY2027). Held "
                "to +2, not more, because the leverage deterioration is real and recent, not "
                "an accounting artefact - the assigned BBB+ remains a notch below what the "
                "franchise alone might suggest."),
        (62, 0, "No group-support notch identified."),
        (63, 0, "No peer-benchmarking adjustment; no prior rating action was available in the "
                "reference library for this issuer (declared in the rationale)."),
        (64, 0, "None."),
    ],
    "dhampur": [
        (60, 0, "No sector-metric adjustment."),
        (61, 1, "+1 for structural diversification and an improving operating trend the "
                "composite understates: forward integration across sugar, co-generation, "
                "distillery/ethanol and country liquor cushions the sugar cycle; net sugar "
                "recovery improved to 10.74% (FY2025: 9.80%) and cost of production fell to "
                "Rs 3,778/quintal, driving 13.3% revenue growth and a PAT recovery to Rs "
                "25.18 crore (FY2025: Rs 14.69 crore). The Meerganj divestment (Rs 305 crore, "
                "effective 18-Jun-2026) reduced long-term debt to ~Rs 124 crore, improving "
                "the long-term debt-equity ratio to 0.18x by Q1 FY2027 (unaudited)."),
        (62, 0, "No group-support notch identified; experienced promoters are reflected in "
                "the business-risk score, not as a separate support notch."),
        (63, 0, "No peer-benchmarking adjustment."),
        (64, 0, "None."),
    ],
    "doms-industries": [
        (60, 0, "No sector-metric adjustment."),
        (61, 0, "No separate business-risk uplift beyond what is already reflected in the "
                "consistency adjustment below."),
        (62, 0, "No incremental group-support notch beyond Step 12b."),
        (63, -2, "-2, a DOWNWARD consistency adjustment. This rationale's own disclaimer "
                 "states: 'the company's own annual report discloses the outstanding CRISIL "
                 "AA-/Stable rating, so that action was known before this view was formed' "
                 "(workpaper Sec 0/9). The financial-only anchor (AA+) does not reflect this "
                 "same-issuer, already-disclosed outstanding action; the assigned rating is "
                 "held to it rather than to the higher anchor, since the anchor's own screening "
                 "band is documented to be unreliable outside the A+...BBB- range and a "
                 "same-issuer disclosed rating is stronger evidence than the screen."),
        (64, 0, "None."),
    ],
    "happy-forgings-limited": [
        (60, 0, "No sector-metric adjustment; the company's zero-term-debt, high-coverage "
                "profile (gearing 0.15x, interest coverage 45x FY2026) is genuinely strong on "
                "an accrual basis and needs no disapplication."),
        (61, -1, "-1 for concentration and cyclicality risk the financial ratios do not "
                 "capture: the ENTIRE business is a single segment (Forging), exposed to "
                 "automotive/industrial capital-goods cyclicality, with a large "
                 "export-linked order book (Rs 950 crore incremental revenue visibility, "
                 "~60% export-linked) carrying execution and forex-translation risk, and "
                 "rising working-capital intensity as the capex cycle builds out. These are "
                 "real qualitative constraints a ratio grid showing near-zero leverage cannot "
                 "see."),
        (62, 0, "No group-support notch identified."),
        (63, 0, "No peer-benchmarking adjustment."),
        (64, 0, "None."),
    ],
    "hle-glascoat": [
        (60, 0, "No sector-metric adjustment."),
        (61, -1, "-1 for a genuine, recent margin compression the composite (built on "
                 "3-year averages) does not fully weight: consolidated OPBDITA margin fell "
                 "to 10.3% in FY2026 from 13.0% in FY2025, driven by initial losses in the "
                 "newly acquired Omeras business, domestic GLE pricing pressure and a 31% "
                 "rise in employee costs; quarterly PAT was volatile (Rs 4.6 crore Q3 FY2026 "
                 "vs Rs 20.1 crore Q4 FY2026). A sustained margin recovery - the key driver of "
                 "improving coverage - had not yet been demonstrated as at the data cutoff."),
        (62, 0, "No group-support notch identified."),
        (63, 0, "No peer-benchmarking adjustment."),
        (64, 0, "None."),
    ],
    "indus-towers": [
        (60, 0, "No sector-metric adjustment."),
        (61, 1, "+1 for a genuinely RESOLVED counterparty-concentration risk, per failure "
                "mode 22's resolving-vs-live test: receivable days compressed 82 to 58 to 55 "
                "over three periods (sustained improvement, not a single-period blip), with "
                "the company's own disclosures supporting clearance of previously overdue "
                "amounts. The original draft capped the view on counterparty risk without "
                "applying this test - see the Correction Note; a subsidiary/counterparty "
                "outgrowing its risk overhang on strong standalone performance is an upgrade "
                "signal, not a neutral fact, and is recorded here as the reasoned basis for "
                "the uplift rather than left implicit."),
        (62, 0, "No incremental group-support notch beyond Step 12b."),
        (63, 0, "No peer-benchmarking adjustment."),
        (64, 0, "None."),
    ],
    "jsw-steel": [
        (60, 0, "No sector-metric adjustment."),
        (61, 1, "+1 for the deleveraging transformation the trailing-year financial "
                "composite has not yet fully absorbed: the BPSL move into the 50:50 JSW-JFE "
                "joint venture (27-Mar-2026) is expected to deliver ~Rs 37,250 crore of total "
                "deleveraging; phase one alone took consolidated net debt from Rs 76,563 "
                "crore to Rs 53,870 crore, ND/EBITDA to 1.81x from 3.34x (AR basis, the best "
                "print since fiscal 2022), with net gearing of 0.51x against the company's "
                "own stated caps of 3.75x ND/EBITDA and 1.75x ND/equity."),
        (62, 1, "+1 for a demonstrated, board-level 3.0x internal leverage ceiling with a "
                "track record of deleveraging through capex cycles, and JFE's equity "
                "participation (second tranche of Rs 7,875 crore due June 2026) - a "
                "structural financial-policy commitment the composite cannot see, distinct "
                "from the transaction effect captured in the notch above."),
        (63, 0, "No peer-benchmarking adjustment."),
        (64, 0, "None."),
    ],
    "oil-india": [
        (60, 0, "No sector-metric adjustment."),
        (61, 0, "No separate business-risk notch beyond the government-linkage factor below, "
                "which already captures the qualitative uplift for this issuer."),
        (62, 1, "+1 - transcribed from this rationale's own structural-anchor language: "
                "'a government linkage that is both a policy-role and moral-obligation "
                "factor' - 56.66% Government of India ownership, Maharatna status, and "
                "international ratings (Moody's Baa3 / Fitch BBB-, Stable) that the "
                "company's own annual report states are 'at par with India's sovereign "
                "rating.' The rationale itself records the anchor as one notch lower, driven "
                "by consolidated leverage metrics the scorecard cannot decompose by entity or "
                "financing structure, and the calibration's own documentation states it "
                "under-reads issuers at the AA+/AAA boundary absent this support notch."),
        (63, 0, "No further peer-benchmarking adjustment."),
        (64, 0, "None."),
    ],
    "vedanta": [
        (60, 0, "No sector-metric adjustment."),
        (61, 1, "+1 for Hindustan Zinc Limited's own standalone franchise strength beyond "
                "the financial composite: an integrated zinc-lead-silver producer with a "
                "long domestic reserve life and cost-quartile position, credit factors a "
                "ratio grid built on trailing margins and leverage does not directly weight."),
        (62, 1, "+1 for the parent/group-linkage factor named explicitly in this rationale's "
                "Entity note: Vedanta Limited holds 60.71% of HZL and is assessed as a "
                "support/linkage factor distinct from HZL's own standalone metrics, which the "
                "financial-only composite (fed from HZL's own statements) cannot see."),
        (63, 0, "No further peer-benchmarking adjustment; no prior rating action was "
                "available in the reference library for this issuer (declared in the "
                "rationale)."),
        (64, 0, "None."),
    ],
}


def apply_overlay(slug: str, rows: list) -> str:
    files = sorted((ROOT / "Companies" / slug).glob("Rating_Scorecard*.xlsx"))
    if not files:
        return "no scorecard found"
    msgs = []
    for f in files:
        wb = load_workbook(f)
        ws = wb["Inputs"]
        for row, notches, why in rows:
            ws.cell(row=row, column=3, value=notches)
            ws.cell(row=row, column=4, value=why)
        wb.save(f)
        msgs.append(f.name)
    return "wrote Stage 2 to: " + ", ".join(msgs)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    # argv was never read, so `--help` fell straight through and WROTE Stage 2 into every
    # scorecard named in OVERLAYS. Found 04-Sep-2026 by running --help across every tool:
    # the run was idempotent and did no harm that time, which is luck, not a safeguard.
    if len(sys.argv) > 1:
        print("Usage: python tools/fill_remaining_overlays.py       (takes no arguments)")
        print("One-off backfill: writes the hard-coded Stage 2 committee overlay into the")
        print("scorecards of %d case(s): %s" % (len(OVERLAYS), ", ".join(sorted(OVERLAYS))))
        return 0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2
    for slug, rows in OVERLAYS.items():
        print("%-28s %s" % (slug, apply_overlay(slug, rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
