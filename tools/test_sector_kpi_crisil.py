"""Controls for the CRISIL corporate SECTOR_KPI entries added 13-Sep-2026 (failure mode 21).

A check that cannot fail its own control is not a check. Every NEGATIVE control below is a
VERBATIM fragment of a real rationale in Companies/ that the first version of these triggers
matched wrongly - not an invented counter-example. That first version produced eight false
positives on a 35-rationale corpus, including asking a telecom-TOWER company for ARPU (its
customers' metric) and asking ALEMBIC LIMITED for pharma metrics when Alembic Limited is the
real-estate entity left behind after the formulations business was demerged into a different
company whose NAME contains "Pharmaceuticals".

The recurring shape: a sector word appears in the report because of the industry-classification
table, a list of customer industries, a segment name, a subsidiary's activity, or an end-use of
the product - none of which is the rated entity's own sector.

    python tools/test_sector_kpi_crisil.py
"""
import importlib.util
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "cs", str(Path(__file__).resolve().parent / "check_sections.py"))
cs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cs)


def _doc(about, body=""):
    """Minimal document with an About-the section, which is where triggers are read."""
    return ("## about the company\n" + about + "\n\n## rating rationale\n" + body).lower()


# (name, about-text, body-text, expect_finding)
CASES = [

    # ---------------------------------------------------------------- POSITIVE controls
    # Each must FIRE: the entity is squarely in the sector and the metric is absent.
    ("pharma, metric absent",
     "abc pharmaceuticals company manufactures generic formulations",
     "revenue grew 12% to rs 900 crore on strong domestic sales", True),
    ("tyre, metric absent",
     "the company is a tyre manufacturer supplying passenger and truck radials",
     "operating margin improved to 14.2% on softer natural rubber prices", True),
    ("steel, metric absent",
     "the company is an integrated steel producer with 18 mtpa of capacity",
     "ebitda per tonne stood at rs 9,100 in fy26", True),
    ("speciality chemicals, metric absent",
     "the company is a speciality chemicals manufacturer of aroma ingredients",
     "exports contributed 58% of revenue in fy26", True),
    # KNOWN LIMITATION, controlled deliberately rather than left implicit: quantification is
    # tested FORWARD from the metric phrase only, so a number-first construction
    # ("usd 74 per barrel") reads as unquantified and the gate fires anyway. A backward window
    # was tried on 13-Sep-2026 and reverted the same day - it made "capacity of 2.5 lakh tonne"
    # read as a quantified crushing THROUGHPUT and silently killed the Dhampur sugar finding
    # the sugar entry exists for. A gate that over-fires is recoverable; one that under-fires
    # is the defect being guarded against.
    ("number-first phrasing still fires (documented limitation)",
     "the company is engaged in oil and gas exploration across 21 blocks",
     "realisation averaged usd 74 per barrel", True),
    ("e&p, truly absent",
     "the company is engaged in oil and gas exploration across 21 blocks",
     "revenue rose 9% on higher volumes", True),
    ("textiles, metric absent",
     "the company operates a spinning mill and terry towel unit in panipat",
     "gross margin was stable at 22%", True),
    ("mobile telephony, metric absent",
     "the company is a telecom operator with pan-india wireless subscribers",
     "revenue declined 4% in fy26", True),
    ("retail, metric absent",
     "the company runs a retail chain of 340 supermarkets",
     "revenue per store data is not disclosed", True),
    ("engineering, metric absent",
     "the company is an engineering company executing turnkey process plants",
     "revenue rose 18% in fy26", True),
    ("real estate, metric absent",
     "the company is a real-estate developer with projects in mmr and ncr",
     "debt to equity stood at 0.6 times", True),

    # Metric PRESENT and quantified -> no finding (guards against a check that always fires).
    ("pharma, metric present",
     "abc pharmaceuticals company manufactures generic formulations",
     "r&d spend was 6.4% of sales; two usfda observations were closed in fy26", False),
    ("tyre, metric present",
     "the company is a tyre manufacturer supplying passenger and truck radials",
     "capacity utilisation was 82% and the replacement market contributed 68% of sales",
     False),
    ("textiles, metric present",
     "the company operates a spinning mill and terry towel unit in panipat",
     "capacity utilisation stood at 91% across 45,000 spindles", False),

    # ---------------------------------------------------------------- NEGATIVE controls
    # Verbatim from real rationales. Each matched the WRONG sector before the fix.

    # Alembic Limited: "pharmaceutical" appears only in the NAME of the demerged entity.
    # The rated entity is a real-estate company. Before the fix this asked a property
    # developer for USFDA observations.
    ("alembic: pharma name, real-estate entity",
     "alembic limited was incorporated on july 30, 1907. following the demerger of its "
     "formulations business into alembic pharmaceuticals limited with effect from april 1, "
     "2010, al operates in real-estate development and leasing",
     "bookings of rs 410 crore and collections of rs 380 crore were recorded in fy26", False),

    # HLE Glascoat: a list of CUSTOMER industries.
    ("hle: customer industries are not a sector",
     "plants in western india and two in germany, serving pharmaceutical, "
     "specialty-chemical, agrochemical, dyes and pigments, oil and gas and infrastructure "
     "customers",
     "the order book stood at rs 720 crore, 1.4 times fy26 revenue", False),

    # Dhampur: the standard INDUSTRY CLASSIFICATION table names FMCG at the macro level while
    # the basic industry is sugar. Before the fix a sugar mill was asked for market share.
    ("dhampur: classification table is not a sector claim",
     "industry classification | macro-economic indicator | sector | industry | basic industry "
     "| fast moving consumer goods | fast moving consumer goods | agricultural food and other "
     "products | sugar |",
     "cane crushed was 32.92 lakh tonne in fy26", False),

    # Jindal Stainless: consumer durables is an END-USE of stainless steel.
    ("jindal: end-use industries are not a sector",
     "the stainless steel industry is driven by construction and infrastructure, automotive "
     "and railways, process industry and consumer durables demand",
     "capacity utilisation was 87% and value-added products were 41% of volumes", False),

    # ITC: hotels were DEMERGED; IT services sit in a subsidiary; fmcg appears as a segment
    # label. A diversified conglomerate legitimately yields no single sector metric.
    ("itc: demerged segment, subsidiary activity, segment labels",
     "itc limited, established in 1910, is the largest cigarette manufacturer in india. "
     "following the demerger of its hotels business into itc hotels limited, itc reports five "
     "operating segments - fmcg-cigarettes; fmcg-others; hotels; paperboards, paper and "
     "packaging; agri business. it services are provided through subsidiary itc infotech "
     "india ltd",
     "gross revenue rose 8% in fy26", False),

    # SBI: "broking" is what a SUBSIDIARY does. Before the fix India's largest bank was asked
    # for average daily turnover and active client counts.
    ("sbi: subsidiary activity list is not a sector",
     "the group offers investment banking, credit cards, life insurance, general insurance, "
     "fund management, primary dealership, broking and factoring. sbi is the largest bank in "
     "india",
     "gnpa was 1.82%, nim 3.05% and crar 14.1% as on march 31, 2026", False),

    # Gujarat Energy: E&P is one of four segments folded in by a scheme of arrangement.
    ("gujarat energy: one segment of an integrated utility",
     "a scheme of arrangement took effect under which it became an integrated energy company: "
     "gas trading, exploration and production assets, wind power generation and investments "
     "were brought in, while the gas transmission business was moved out",
     "ebitda rose 11% in fy26", False),

    # Cochin Minerals: "chemicals and petrochemicals" is the classification taxonomy.
    ("cochin: petrochemicals in the classification taxonomy",
     "industry classification | commodities | chemicals | chemicals and petrochemicals | "
     "specialty chemicals |",
     "revenue was rs 240 crore in fy26", False),

    # ---------------------------------------------------------------- ORDERING control
    # Indus Towers quantifies its tenancy ratio, satisfying the tower trigger, and then also
    # matches "mobile network". Before the first-satisfied-wins change it was asked for ARPU -
    # which belongs to its CUSTOMERS, not to a tower company.
    ("tower co satisfying its own metric is not then asked for ARPU",
     "the company is a telecom tower operator providing co-location to mobile network "
     "operators across india",
     "the sharing ratio stood at 1.72 times as on march 31, 2026", False),
    # ...but a tower company that omits its OWN metric must still fire.
    ("tower co omitting its own metric still fires",
     "the company is a telecom tower operator providing co-location to mobile network "
     "operators across india",
     "revenue rose 6% in fy26", True),
]


def main():
    fails = []
    for name, about, body, expect in CASES:
        got = cs._missing_sector_kpi(_doc(about, body))
        ok = bool(got) == expect
        print(("  ok   " if ok else "  FAIL ") + name
              + ("" if ok else f"\n         expected finding={expect}, got={got!r}"))
        if not ok:
            fails.append(name)

    print()
    if fails:
        print(f"{len(fails)} FAILED of {len(CASES)}")
        return 1
    print(f"ALL PASS - {len(CASES)}/{len(CASES)} controls")
    return 0


if __name__ == "__main__":
    sys.exit(main())
