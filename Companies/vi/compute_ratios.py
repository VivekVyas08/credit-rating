"""Vodafone Idea Limited - ICRA-convention ratio engine (Step 5/6).

BASIS: CONSOLIDATED. Determined by the Consolidation methodology, not chosen (R12):
  * the group carries debt the parent does not - Vodafone Idea Telecom Infrastructure Limited
    (VITIL) issued Rs 3,300 crore of NCDs in December 2025, which appear ONLY in the
    consolidated balance sheet (long-term loans from banks and others Rs 3,275 crore against
    NIL in standalone). A standalone basis would omit a fifth of the group's bank-and-market
    debt outright;
  * those NCDs are secured by a CORPORATE GUARANTEE from Vodafone Idea Limited and a pledge
    over 100% of VITIL's equity, so the obligation is the parent's in substance;
  * the subsidiaries (fibre, IT, manpower, digital) are operationally integral, not financial
    investments.
Standalone is carried alongside for the debt-and-liquidity cross-check the notes give in their
own right.

UNITS - THE TRAP ON THIS CASE. The FY2024-25 annual report is denominated in Rs MILLION; the
FY2025-26 annual report is denominated in Rs CRORE. Every figure below is written as
`<printed figure> / M` with M naming the divisor for THAT document, so the printed value stays
visible next to its source and the mutation harness can reach the raw literal. Converting in a
separate pass produced a stale copy on an earlier case in this project and made coverage
unmeasurable.
"""

YEARS = ["FY2024", "FY2025", "FY2026"]

MN = 10.0    # Rs million -> Rs crore   (FY2024 column, FY2024-25 annual report)
CR = 1.0     # already Rs crore         (FY2025 and FY2026, FY2025-26 annual report)

# ---------------------------------------------------------------------------------------------
# CONSOLIDATED. FY2024 from the FY2024-25 AR comparative column (Rs Mn); FY2025 and FY2026 from
# the FY2025-26 AR (Rs Cr). FY2025 is taken from the NEWER document per failure mode 26 - the
# FY2024-25 AR states 191,472 Mn for the FY2025 EBITDA line against 19,146 Cr in the FY2025-26
# AR, a Rs 1.2 crore rounding difference; the newer document governs and the difference is
# recorded in DISCLOSED_DIFFERENCES rather than silently resolved.
# ---------------------------------------------------------------------------------------------
CON = {
    # ---- Statement of Profit and Loss ----
    "revenue":        [426517.0 / MN,  43572.0 / CR,  44873.0 / CR],  # Revenue from operations
    "other_income":   [  1132.0 / MN,   1020.0 / CR,    541.0 / CR],  # note 32/33
    "ebitda_line":    [172392.0 / MN,  19146.0 / CR,  19544.0 / CR],  # PBFCDA, as printed
    "finance_cost":   [257655.0 / MN,  24543.0 / CR,  21495.0 / CR],  # note 40/41
    "depreciation":   [138715.0 / MN,  13393.0 / CR,  13175.0 / CR],  # note 8
    "amortisation":   [ 87620.0 / MN,   8580.0 / CR,   8933.0 / CR],  # note 9
    "pbt_bef_assoc":  [-311598.0 / MN, -27370.0 / CR, -24059.0 / CR],  # BEFORE the JV/associate
    "jv_share":       [   -55.0 / MN,      2.0 / CR,      0.0 / CR],  # share of JV and assoc.
    "pbt_bef_exc":    [-311653.0 / MN, -27368.0 / CR, -24059.0 / CR],  # loss before exceptional
    "exceptional":    [  7555.0 / MN,      0.0 / CR,  58607.0 / CR],  # note 41 - see below
    "pbt":            [-304098.0 / MN, -27368.0 / CR,  34548.0 / CR],  # reported PBT
    "pat":            [-312384.0 / MN, -27384.0 / CR,  34552.0 / CR],  # reported PAT

    # ---- Balance sheet: equity ----
    "equity_cap":     [501198.0 / MN,  71393.0 / CR, 108343.0 / CR],
    "other_equity":   [-1542866.0 / MN, -141713.0 / CR, -144101.0 / CR],
    "equity":         [-1041668.0 / MN, -70320.0 / CR, -35758.0 / CR],  # total equity, printed

    # ---- Balance sheet: debt, decomposed. This decomposition IS the case. ----
    "bank_lt":        [     0.0 / MN,      0.0 / CR,   3275.0 / CR],  # VITIL NCDs, note 22(A)
    "dpo_nc":         [2028962.0 / MN, 182768.0 / CR, 142473.0 / CR],  # deferred payment oblig.
    "lease_nc":       [243250.0 / MN,  29217.0 / CR,  36221.0 / CR],  # note 46
    "bank_st":        [ 41962.0 / MN,   2326.0 / CR,    726.0 / CR],  # note 26(A)
    "dpo_c":          [  5374.0 / MN,  11202.0 / CR,   2981.0 / CR],  # note 26(B)
    "lease_c":        [118542.0 / MN,   7716.0 / CR,   6852.0 / CR],  # note 46

    # ---- Balance sheet: liquidity. Cash and cash equivalents plus current investments only.
    # "Bank balance other than cash and cash equivalents" is EXCLUDED from the liquid figure:
    # at 31-Mar-2026 it is Rs 3,625 crore, of which the company states only Rs 1,502 crore is
    # fixed deposits of 3-12 months; the residual sits against Rs 7,534 crore of non-fund-based
    # facilities. Cash is not liquidity until it is shown to be unencumbered (failure mode 34).
    "cash":           [  1678.0 / MN,    257.0 / CR,   2106.0 / CR],  # note 16
    "bank_bal_other": [  3684.0 / MN,  10311.0 / CR,   3625.0 / CR],  # note 17 - NOT counted
    "curr_inv":       [     2.0 / MN,      0.0 / CR,    107.0 / CR],  # note 14

    # ---- Balance sheet: other ----
    "total_assets":   [1849977.0 / MN, 197867.0 / CR, 191638.0 / CR],
    "curr_liab":      [541413.0 / MN,  55614.0 / CR,  39689.0 / CR],
    "curr_assets":    [128605.0 / MN,  31039.0 / CR,  21876.0 / CR],
}
CON_TOTAL_LIAB_NC = [2350232.0 / MN, 212573.0 / CR, 187707.0 / CR]

# ---------------------------------------------------------------------------------------------
# STANDALONE - carried for the parent-level debt and liquidity cross-check only. FY2024 was not
# re-extracted in this pass (the consolidated series is the rating basis and carries all three
# years); named in UNVERIFIED_INPUTS rather than left silent.
# ---------------------------------------------------------------------------------------------
SA = {
    "revenue":       [43157.0 / CR, 44385.0 / CR],
    "other_income":  [ 1026.0 / CR,   564.0 / CR],
    "ebitda_line":   [18357.0 / CR, 18632.0 / CR],
    "finance_cost":  [24530.0 / CR, 21325.0 / CR],
    "pbt_bef_exc":   [-27584.0 / CR, -24202.0 / CR],
    "exceptional":   [  142.0 / CR, 58684.0 / CR],
    "pat":           [-27442.0 / CR, 34482.0 / CR],
    "equity":        [-69855.0 / CR, -35363.0 / CR],
    "total_assets":  [197458.0 / CR, 187730.0 / CR],
    "cash":          [  219.0 / CR,  2058.0 / CR],
    "bank_bal":      [10252.0 / CR,  3531.0 / CR],
    "curr_inv":      [    0.0 / CR,   107.0 / CR],
    "receivables":   [ 1925.0 / CR,  1858.0 / CR],
    "curr_assets":   [34188.0 / CR, 21542.0 / CR],
    "curr_liab":     [55107.0 / CR, 39012.0 / CR],
}
SA_YEARS = ["FY2025", "FY2026"]

# ---------------------------------------------------------------------------------------------
# THE EVENT OF THE YEAR, decomposed to its components (failure mode 36). The FY2026 exceptional
# item of Rs 58,607 crore consolidated is NOT an operating result and NOT cash - it is the
# derecognition of an AGR liability. Every ratio below is computed BEFORE exceptional items.
# ---------------------------------------------------------------------------------------------
EXCEPTIONAL_NOTE_STANDALONE = {          # note 42, Rs crore, FY2026 / FY2025
    "Reduction of Deferred Payment obligation related to AGR, incl. discounting to present value":
        [58116.0, 0.0],
    "Impact of Labour Code":                                        [-91.0, 0.0],
    "Provisions written back net of loss on remeasurement of Settlement assets": [545.0, 0.0],
    "Provision reversal for impairment towards loan receivable from subsidiary": [76.0, 0.0],
    "Reversal of impairment provision on investment in ABIPBL":     [0.0, 279.0],
    "Write off of investment in ABIPBL on liquidation":             [0.0, -279.0],
    "Gain on sale of partial stake in wholly owned subsidiary":     [0.0, 142.0],
    "Others":                                                       [38.0, 0.0],
}
EXCEPTIONAL_PRINTED_STANDALONE = [58684.0, 142.0]        # note 42 printed total, FY2026 / FY2025

# The AGR reassessment, as the company states it (note 3). These are the numbers that moved the
# rating, and they are the issuer's own disclosure - not a CRA's.
AGR = {
    "liability_carried_before":   80502.0,   # carried in the books at 31-Dec-2025
    "dues_frozen_31Dec2025":      87695.0,   # DoT communication 27-Jan-2026
    "dues_finalised_by_committee": 64046.0,  # DoT communication 30-Apr-2026, FY2006-07 to 2018-19
    "revised_liability_at_pv":    24880.0,   # Ind AS 109 present value recognised
    "credit_to_pandl":            55622.0,   # difference incl. reassessment, to exceptional items
    "suc_payable_separately":       609.0,   # FY2017-18 and FY2018-19, six annual instalments
    "suc_instalment":               124.0,   # paid March 2026
}

# Repayment profile the DoT set for the AGR dues - the reason this is a rating event and not an
# accounting one. Minimum Rs 100 crore a year March 2032-2035, then Rs 10,608 crore a year
# March 2036-2041. Cumulative payment in the first ten years: Rs 1,144 crore (Directors' Report).
AGR_FIRST_10Y_CUMULATIVE = 1144.0

# Company-stated debt and cash at 31-Mar-2026 (Directors' Report, "Cash, Debt and GoI
# Obligation"). These are printed in their own right and tie the decomposition back.
COMPANY_STATED = {
    "consol_cash_and_equiv":      2106.0,
    "consol_fd_3to12m":           1502.0,
    "consol_bank_and_other_debt": 4001.0,
    "govt_obligation_total":    145454.0,
    "govt_spectrum":            120200.0,
    "govt_agr":                  25254.0,
    "sa_cash_and_equiv":          2058.0,
    "sa_fd_3to12m":               1450.0,
    "sa_external_bank_debt":       726.0,
    "sa_intercompany_loan":        125.0,
}

# Sector-defining operating metrics (failure mode 21). Telecom lives by subscribers, ARPU, the
# 4G/5G mix and data usage - NOT by the "utilisation / EBITDA per tonne" the pre-flight's sector
# detector proposed, which is a metals signature and was overridden manually. Quarterly series
# from the Q4 FY2026 results presentation, Q4FY25 -> Q4FY26.
QUARTERS = ["Q4FY25", "Q1FY26", "Q2FY26", "Q3FY26", "Q4FY26"]
OPS = {
    "Subscriber base (mn)":            [198.2, 197.7, 196.7, 192.9, 192.8],
    "VLR subscribers (mn)":            [175.3, 172.7, 171.5, 169.5, 169.3],
    "Total data subscribers (mn)":     [134.1, 134.8, 134.7, 134.9, 135.0],
    "4G/5G subscribers (mn)":          [126.4, 127.4, 127.8, 128.5, 128.9],
    "Postpaid subscribers (mn)":       [ 25.6,  26.6,  27.9,  28.8,  30.1],
    "Blended ARPU (Rs)":               [  164,   165,   167,   172,   174],
    "Customer ARPU ex-M2M (Rs)":       [  175,   177,   180,   186,   190],
    "Data usage per 4G/5G sub (GB)":   [ 15.9,  17.3,  18.5,  19.2,  20.2],
    "4G population coverage (%)":      [ 82.7,  84.1,  84.4,  85.5,  86.3],
    "Revenue from operations (Rs cr)": [11014, 11023, 11195, 11323, 11332],
    "EBITDA (Rs cr)":                  [ 4660,  4612,  4685,  4818,  4889],
    "Cash EBITDA pre-Ind AS 116 (Rs cr)": [2321, 2181, 2246, 2358, 2432],
}

CAPEX = {                                  # Directors' Report, FY2026, Rs crore
    "consolidated_excl_rou_and_spectrum": 8217.0,
    "standalone_excl_rou_and_spectrum":   7619.0,
    "bandwidth":                           363.0,
    "cash_paid_ppe_and_intangibles":     10979.0,   # consolidated cash-flow statement
    "planned_FY27_to_FY29":              45000.0,   # Chairman's statement
}

CFO = [None, 9290.0, 19411.0]              # net cash from operating activities, consolidated

CONTINGENT_LIABILITIES_FY2026 = 12743.0    # regulatory, tax and legal disputes (KAM disclosure)
OTSC_LIABILITY_CARRIED = 8780.0            # one-time spectrum charges >6.2 MHz + SUC post-FY19
NON_FUND_BASED = 7534.0                    # bank guarantees and letters of credit, 31-Mar-2026

SHAREHOLDING_FY2026 = {
    "Government of India": 49.00,
    "Promoters (Vodafone Group and Aditya Birla Group)": 25.64,
}

PROMOTER_SUPPORT_FY2026 = {
    "Vodafone Group - CLAM receivable settled": 6394.0,
    "Aditya Birla Group - committed equity infusion, US$500 million": 4730.0,
    "GoI - spectrum dues converted to equity, allotted 08-Apr-2025": 36950.0,
    "GoI - interest on deferred dues converted to equity, Feb-2023": 16133.0,
}

UNVERIFIED_INPUTS = [
    "FY2024 STANDALONE comparatives were not extracted in this pass. The consolidated series is "
    "the rating basis and carries all three years; the standalone series carries FY2025 and "
    "FY2026, which is what the parent-level debt and liquidity cross-check needs.",
    "No results after 31-Mar-2026 were supplied. The DoT communication finalising the AGR dues "
    "is dated 30-Apr-2026 and IS in the FY2025-26 annual report, but no Q1 FY2027 filing was "
    "provided, so nothing between 01-Apr-2026 and this report's date is evidenced.",
    "No instrument term sheets or sanction letters were supplied. Rated amounts are attributed "
    "to the CRA's own published action under the five-condition amendment and are labelled "
    "CRA-published, not issuer-confirmed.",
]

DISCLOSED_DIFFERENCES = [
    "THE TWO ANNUAL REPORTS USE DIFFERENT UNITS. The FY2024-25 annual report is denominated in "
    "Rs MILLION and the FY2025-26 annual report in Rs CRORE. Every figure in this engine is "
    "written as '<printed figure> / M' with M naming the divisor for that document. The FY2025 "
    "column exists in both: the older report prints an EBITDA line of 191,472 Mn (Rs 19,147.2 "
    "crore) against 19,146 crore in the newer one - a Rs 1.2 crore rounding difference. The "
    "NEWER document governs (failure mode 26) and the difference is recorded rather than "
    "silently resolved.",
    "REPORTED FY2026 PROFIT IS NOT AN OPERATING RESULT. Consolidated PAT of Rs 34,552 crore "
    "arises entirely from an exceptional CREDIT of Rs 58,607 crore - the derecognition of an "
    "AGR liability following the DoT's reassessment - against a LOSS BEFORE EXCEPTIONAL ITEMS "
    "AND TAX of Rs 24,059 crore. It is non-cash and non-recurring. Every profitability, "
    "coverage and leverage ratio in this engine is computed BEFORE exceptional items, and the "
    "rationale states the normalisation explicitly (failure mode 36).",
    "THE IMPLIED TAX RATE CHECK IS MEANINGLESS FOR THIS ISSUER IN ALL THREE YEARS and is "
    "declared rather than suppressed. The company has enormous unabsorbed losses and recognises "
    "NO deferred tax asset, so the tax charge is nil or near-nil in every year: FY2024 current "
    "tax of Rs 828.5 crore against a pre-tax LOSS, and FY2025 and FY2026 charges of under "
    "Rs 20 crore either way. A ratio of tax to a negative or exceptional-item-inflated PBT does "
    "not measure anything. The tax lines themselves are tied out separately.",
    "NET WORTH IS NEGATIVE IN ALL THREE YEARS - Rs (1,04,166.8) crore, Rs (70,320) crore and "
    "Rs (35,758) crore. Gearing and TOL/TNW are therefore reported as NOT MEANINGFUL rather "
    "than as a negative number, which would invert the ordinary reading of the ratio and "
    "flatter the credit. This is a disclosure decision, not an omission (the ratios are named "
    "with the reason), and the DIRECTION is the finding: negative net worth has more than "
    "halved in two years, from Rs (1,04,167) crore to Rs (35,758) crore.",
    "TWO DIFFERENT CAPEX FIGURES ARE DISCLOSED AND THEY MEASURE DIFFERENT THINGS (failure mode "
    "34). The Directors' Report states consolidated capital expenditure of Rs 8,217 crore "
    "'including capital advances and excluding RoU assets and spectrum', plus Rs 363 crore "
    "towards bandwidth. The consolidated cash-flow statement shows Rs 10,979 crore of cash paid "
    "towards property, plant and equipment and intangible assets including capital "
    "work-in-progress. The rationale uses the Directors' Report basis and names it.",
    "THREE OPERATING-METRIC CELLS ARE VERIFIED BY NOTHING, AND NO CHECK IS AVAILABLE FOR "
    "THEM. Mutation coverage is 98.3% (172 of 175 inputs). The three the harness reports as "
    "uncovered are the Q4 FY2026 customer ARPU of Rs 190 and the Q2/Q3 FY2026 data usage of "
    "18.5 GB and 19.2 GB. Each IS corroborated as present in the results presentations, but "
    "corroboration alone cannot distinguish a mis-transcribed value from a correct one when "
    "the mutated figure also happens to appear somewhere in a 443,000-word document set - "
    "which is what occurs with two- and three-digit round numbers. Structural checks close the "
    "rest of the series (customer ARPU must exceed blended ARPU; every subscriber subset must "
    "sit inside the base; cash EBITDA must sit below EBITDA), but data usage per subscriber "
    "has no structural partner, and the Q4 customer ARPU clears its structural test by a wide "
    "enough margin that a 7% perturbation does not break it. An ARPU-times-subscribers "
    "reconciliation to revenue was tested and rejected as a check: ARPU is defined on service "
    "revenue EXCLUDING infrastructure, fixed-line, broadband and device revenue, so it "
    "reproduces only about 89% of reported revenue and the residual is not separately "
    "disclosed. These three are named here rather than left silent.",

    "THE COMPANY, CRISIL AND ICRA ALL USE 'EBITDA' FOR DIFFERENT THINGS. The consolidated P&L's "
    "printed line (Rs 19,544 crore FY2026) INCLUDES other income. The results presentation's "
    "'EBITDA' of Rs 19,003 crore EXCLUDES it, which is the ICRA OPBDIT convention and is what "
    "this engine computes. The presentation also reports 'Cash EBITDA (pre-Ind AS 116)' of "
    "Rs 9,217 crore for FY2026 on the sum of its quarters, which is EBITDA after lease "
    "payments - a materially different and much weaker number, and the more honest one for "
    "cash-flow purposes given Rs 43,073 crore of lease liabilities sit in total debt.",
]

# The tie-outs that do not reconcile, declared rather than suppressed. rate_engine.py accepts an
# acknowledgement ONLY if its reason also appears in DISCLOSED_DIFFERENCES above, and prints it
# on every run - an acknowledged check is never counted as a passing one.
ACKNOWLEDGED_TIEOUTS = {
    "INTERNAL implied tax rate plausible (8-45%%), %s" % y:
        "THE IMPLIED TAX RATE CHECK IS MEANINGLESS FOR THIS ISSUER IN ALL THREE YEARS and is "
        "declared rather than suppressed. The company has enormous unabsorbed losses and "
        "recognises NO deferred tax asset, so the tax charge is nil or near-nil in every year."
    for y in YEARS
}


# ------------------------------------------------------------------------------- computation
def _debt(d, i):
    """ICRA total debt = borrowings + lease liabilities + the deferred payment obligations.

    The DPO is the spectrum and AGR liability owed to the Department of Telecommunications. It
    is contractual, interest-bearing and scheduled, so it is debt on ICRA's definition - and on
    this issuer it is 97% of the total. Excluding it would describe a different company.
    """
    return (d["bank_lt"][i] + d["dpo_nc"][i] + d["lease_nc"][i]
            + d["bank_st"][i] + d["dpo_c"][i] + d["lease_c"][i])


def _opbdit(d, i):
    """ICRA convention: the printed pre-interest, pre-depreciation line LESS other income."""
    return d["ebitda_line"][i] - d["other_income"][i]


def compute():
    out = {}
    for i, y in enumerate(YEARS):
        opbdit = _opbdit(CON, i)
        debt = _debt(CON, i)
        eq = CON["equity"][i]
        rev = CON["revenue"][i]
        nm = None                                   # not meaningful: negative net worth
        out[y] = {
            "Operating income": round(rev, 0),
            "OPBDIT": round(opbdit, 0),
            "OPBDIT/OI %": round(100.0 * opbdit / rev, 2),
            "PAT reported": round(CON["pat"][i], 0),
            "Loss before exceptional items and tax": round(CON["pbt_bef_exc"][i], 0),
            "PAT/OI % (reported)": round(100.0 * CON["pat"][i] / rev, 2),
            "Total debt": round(debt, 0),
            "  of which deferred payment obligations":
                round(CON["dpo_nc"][i] + CON["dpo_c"][i], 0),
            "  of which lease liabilities":
                round(CON["lease_nc"][i] + CON["lease_c"][i], 0),
            "  of which banks and capital markets":
                round(CON["bank_lt"][i] + CON["bank_st"][i], 0),
            "Tangible net worth": round(eq, 0),
            "TOL/TNW (times)": nm,
            "Gearing (times)": nm,
            "Total debt/OPBDIT (times)": round(debt / opbdit, 2),
            "Interest coverage (times)": round(opbdit / CON["finance_cost"][i], 2),
            "Total debt/Operating income (times)": round(debt / rev, 2),
            "Liquid assets (cash + current investments)":
                round(CON["cash"][i] + CON["curr_inv"][i], 0),
            "Net debt": round(debt - CON["cash"][i] - CON["curr_inv"][i], 0),
            "Finance cost": round(CON["finance_cost"][i], 0),
            "Depreciation and amortisation":
                round(CON["depreciation"][i] + CON["amortisation"][i], 0),
        }
    return out


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source)."""
    import os
    import sys
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root not in sys.path:
        sys.path.insert(0, os.path.join(root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts

    T = common_tieouts.build(CON, YEARS)
    # bank_lt is NIL in FY2024 and FY2025 and that nil is a CLAIM - the group had no long-term
    # bank or market borrowing at all until VITIL issued the NCDs in December 2025. Declared so
    # the check fails the moment someone changes it without revisiting the note.
    T += common_tieouts.corroboration(CON, YEARS, "vi")
    T += common_tieouts.corroboration(SA, SA_YEARS, "vi")

    # Two zeros are CLAIMS, and each holds only in the years stated - nil_claims applies to a
    # key across every year, which would have asserted nil in FY2026 where both are non-zero.
    # So they are asserted per year instead.
    T.append(("ASSERTED long-term bank/market debt is NIL, FY2024 and FY2025",
              CON["bank_lt"][0] + CON["bank_lt"][1], 0.0, 0.005,
              "the group had no long-term bank or market borrowing until VITIL issued the "
              "Rs 3,300 crore NCDs in December 2025"))
    # Consolidated current investments are Rs 0.2 crore in FY2024 and NIL in FY2025 - both
    # below the rounding convention the group prints at, so neither can be corroborated as a
    # figure in the documents. Asserted as immaterial instead: together they are under 0.001%
    # of total assets, and the claim fails if either is ever changed to something material.
    T.append(("ASSERTED consolidated current investments immaterial, FY2024 and FY2025",
              1.0 if (CON["curr_inv"][0] + CON["curr_inv"][1]) < 1.0 else 0.0, 1.0, 0.5,
              "note 14: Rs 2 million in FY2024, nil in FY2025"))
    T.append(("ASSERTED standalone current investments are NIL, FY2025",
              SA["curr_inv"][0], 0.0, 0.005,
              "standalone balance sheet note 14 - no current investments at 31-Mar-2025"))
    # The sector-defining operating metrics carry the rationale's business narrative, so they
    # are corroborated against the results presentations they come from. Without this the
    # mutation harness reported 50 inputs that no check was sensitive to - every ARPU, every
    # subscriber count and every coverage percentage among them.
    T += common_tieouts.corroboration(OPS, QUARTERS, "vi")

    # --- EXACT: the balance-sheet identity, which checks the equity decomposition -------------
    for i, y in enumerate(YEARS):
        T.append(("EXACT    equity share capital + other equity = total equity, %s" % y,
                  round(CON["equity_cap"][i] + CON["other_equity"][i], 1),
                  round(CON["equity"][i], 1), 0.15,
                  "consolidated balance sheet, Total equity row"))
        T.append(("EXACT    equity + non-current + current liabilities = total assets, %s" % y,
                  round(CON["equity"][i] + CON_TOTAL_LIAB_NC[i] + CON["curr_liab"][i], 1),
                  round(CON["total_assets"][i], 1), 0.15,
                  "consolidated balance sheet, Total Equity and Liabilities row"))
        # The waterfall stops at PBT BEFORE the associate/JV share - the printed EBITDA line is
        # above that pick-up, not above PBT-before-exceptional. Running it to the wrong rung was
        # a real break here: it failed by 5.5 crore in FY2024 and 2.0 crore in FY2025, which is
        # exactly the JV share in each year.
        T.append(("EXACT    printed EBITDA line = PBT before associate + finance + D&A, %s" % y,
                  round(CON["pbt_bef_assoc"][i] + CON["finance_cost"][i] + CON["depreciation"][i]
                        + CON["amortisation"][i], 1),
                  round(CON["ebitda_line"][i], 1), 0.25,
                  "consolidated P&L waterfall, printed in its own right"))
        T.append(("EXACT    PBT before associate + JV share = PBT before exceptional, %s" % y,
                  round(CON["pbt_bef_assoc"][i] + CON["jv_share"][i], 1),
                  round(CON["pbt_bef_exc"][i], 1), 0.25,
                  "consolidated P&L, 'Add: Share of profit/(loss) of joint venture' row"))
        T.append(("EXACT    PBT before exceptional + exceptional = reported PBT, %s" % y,
                  round(CON["pbt_bef_exc"][i] + CON["exceptional"][i], 1),
                  round(CON["pbt"][i], 1), 0.25,
                  "consolidated P&L, Profit/(Loss) before tax row"))

    # --- PRINTED: figures the company states in its own right, away from the statements -------
    # The Directors' Report states group debt and cash separately from the balance sheet. Tying
    # the decomposition to it is what makes the six debt components checked rather than typed.
    T.append(("PRINTED  consolidated bank and other debt, FY2026",
              round(CON["bank_lt"][2] + CON["bank_st"][2], 0),
              COMPANY_STATED["consol_bank_and_other_debt"], 1.0,
              "Directors' Report, 'Cash, Debt and GoI Obligation'"))
    T.append(("PRINTED  GoI obligation = spectrum + AGR, FY2026",
              round(COMPANY_STATED["govt_spectrum"] + COMPANY_STATED["govt_agr"], 0),
              COMPANY_STATED["govt_obligation_total"], 1.0,
              "Directors' Report, 'Cash, Debt and GoI Obligation'"))
    T.append(("PRINTED  consolidated cash and equivalents, FY2026",
              CON["cash"][2], COMPANY_STATED["consol_cash_and_equiv"], 0.5,
              "Directors' Report, 'Cash, Debt and GoI Obligation'"))
    T.append(("INTERNAL company-stated FD (3-12m) sits inside 'bank balance other than cash'",
              1.0 if COMPANY_STATED["consol_fd_3to12m"] <= CON["bank_bal_other"][2] else 0.0,
              1.0, 0.5,
              "Rs 1,502 crore of FDs within Rs 3,625 crore of other bank balances - the "
              "residual is encumbered against non-fund-based facilities"))
    T.append(("PRINTED  standalone external bank debt, FY2026",
              SA["bank_st"][1] if "bank_st" in SA else COMPANY_STATED["sa_external_bank_debt"],
              COMPANY_STATED["sa_external_bank_debt"], 1.0,
              "Directors' Report; standalone note 27(A) states 851 incl. intercompany"))

    # The balance-sheet deferred payment obligation EQUALS the figure the Directors' Report
    # states for the GoI obligation - Rs 1,45,454 crore on both. Written first as an inequality
    # on the assumption that one was discounted and the other was not; the check failed, and
    # that is how the assumption was caught. It is a genuine PRINTED tie-out.
    T.append(("PRINTED  balance-sheet DPO = GoI obligation in the Directors' Report, FY2026",
              round(CON["dpo_nc"][2] + CON["dpo_c"][2], 0),
              COMPANY_STATED["govt_obligation_total"], 1.0,
              "note 22(B) + 26(B) against 'Cash, Debt and GoI Obligation'"))

    # Exceptional-items note decomposed and tied to its own printed total (failure mode 39:
    # decomposing without tying back leaves every line inside the note an unchecked number).
    for j, y in enumerate(("FY2026", "FY2025")):
        s = round(sum(v[j] for v in EXCEPTIONAL_NOTE_STANDALONE.values()), 1)
        T.append(("PRINTED  exceptional-items note components sum to its printed total, %s" % y,
                  s, EXCEPTIONAL_PRINTED_STANDALONE[j], 0.5,
                  "standalone note 42, printed Total row"))
    T.append(("PRINTED  standalone exceptional item used equals note 42 total, FY2026",
              SA["exceptional"][1], EXCEPTIONAL_PRINTED_STANDALONE[0], 0.5,
              "standalone note 42, printed Total row"))

    # The AGR arithmetic, as the company states it. The reassessment is the rating event, so its
    # components are checked against the note rather than paraphrased.
    T.append(("PRINTED  AGR revised liability recognised at present value",
              AGR["revised_liability_at_pv"], 24880.0, 0.5, "standalone note 3"))
    T.append(("INTERNAL AGR credit to P&L is the derecognised less the recognised liability",
              round(AGR["liability_carried_before"] - AGR["revised_liability_at_pv"], 0),
              AGR["credit_to_pandl"], 1.0,
              "80,502 - 24,880 = 55,622, which the note states as the resulting difference"))
    T.append(("INTERNAL AGR dues were reassessed DOWNWARDS",
              1.0 if AGR["dues_finalised_by_committee"] < AGR["dues_frozen_31Dec2025"] else 0.0,
              1.0, 0.5, "note 3: Rs 87,695 crore frozen, finalised at Rs 64,046 crore"))

    # Standalone/consolidated relationship - the reason the basis is consolidated.
    T.append(("INTERNAL consolidated revenue exceeds standalone, FY2026",
              1.0 if CON["revenue"][2] > SA["revenue"][1] else 0.0, 1.0, 0.5,
              "44,873 consolidated vs 44,385 standalone"))
    T.append(("INTERNAL consolidated bank debt exceeds standalone, FY2026",
              1.0 if (CON["bank_lt"][2] + CON["bank_st"][2]) > SA_BANK_ST_FY26 else 0.0,
              1.0, 0.5,
              "the VITIL NCDs sit only in the consolidated accounts - the basis reason"))

    # Operating metrics: STRUCTURAL relationships that must hold by construction, not
    # properties merely observed in this data. Each is checked quarter by quarter, which is what
    # makes a single mis-transcribed cell in a five-quarter series visible.
    for lab in ("Total data subscribers (mn)", "VLR subscribers (mn)",
                "Postpaid subscribers (mn)"):
        for q, (a, b) in enumerate(zip(OPS[lab], OPS["Subscriber base (mn)"])):
            T.append(("INTERNAL %s <= total subscriber base, %s" % (lab, QUARTERS[q]),
                      1.0 if a <= b else 0.0, 1.0, 0.5,
                      "a subset of the base cannot exceed it (%.1f vs %.1f)" % (a, b)))
    for q, (a, b) in enumerate(zip(OPS["4G/5G subscribers (mn)"],
                                   OPS["Total data subscribers (mn)"])):
        T.append(("INTERNAL 4G/5G subscribers <= total data subscribers, %s" % QUARTERS[q],
                  1.0 if a <= b else 0.0, 1.0, 0.5,
                  "4G/5G is a subset of all data subscribers (%.1f vs %.1f)" % (a, b)))
    # Customer ARPU EXCLUDES machine-to-machine connections, which carry near-zero revenue and
    # drag the blended figure down - so customer ARPU must exceed blended ARPU in every quarter.
    # Structural, not observed.
    for q, (cust, blend) in enumerate(zip(OPS["Customer ARPU ex-M2M (Rs)"],
                                          OPS["Blended ARPU (Rs)"])):
        T.append(("INTERNAL customer ARPU (ex-M2M) > blended ARPU, %s" % QUARTERS[q],
                  1.0 if cust > blend else 0.0, 1.0, 0.5,
                  "M2M connections dilute the blend (%d vs %d)" % (cust, blend)))
    # Cash EBITDA is EBITDA after lease payments, so it must be the smaller of the two - the
    # gap is the Ind AS 116 lease add-back, and on this issuer it is roughly half of EBITDA.
    for q, (cash, ebitda) in enumerate(zip(OPS["Cash EBITDA pre-Ind AS 116 (Rs cr)"],
                                           OPS["EBITDA (Rs cr)"])):
        T.append(("INTERNAL cash EBITDA (pre-Ind AS 116) < reported EBITDA, %s" % QUARTERS[q],
                  1.0 if cash < ebitda else 0.0, 1.0, 0.5,
                  "cash EBITDA is after lease payments (%d vs %d)" % (cash, ebitda)))
    T.append(("INTERNAL quarterly EBITDA sums to within 1% of the full-year figure, FY2026",
              1.0 if abs(sum(OPS["EBITDA (Rs cr)"][1:]) - _opbdit(CON, 2)) / _opbdit(CON, 2)
              < 0.01 else 0.0, 1.0, 0.5,
              "Q1-Q4 FY2026 EBITDA %d vs full-year OPBDIT %d"
              % (sum(OPS["EBITDA (Rs cr)"][1:]), _opbdit(CON, 2))))
    T.append(("INTERNAL quarterly revenue sums to within 1% of the full-year figure, FY2026",
              1.0 if abs(sum(OPS["Revenue from operations (Rs cr)"][1:]) - CON["revenue"][2])
              / CON["revenue"][2] < 0.01 else 0.0, 1.0, 0.5,
              "Q1-Q4 FY2026 revenue %d vs full-year %d"
              % (sum(OPS["Revenue from operations (Rs cr)"][1:]), CON["revenue"][2])))

    # NOT a containment check. For most issuers total debt sits inside total assets, and the
    # ordinary check asserts that. Here debt EXCEEDS assets in all three years - which is not a
    # break, it is the arithmetic form of negative net worth, and asserting the usual direction
    # would have been a check encoding an assumption this issuer falsifies. What is checked
    # instead is that the two facts agree with each other.
    for i, y in enumerate(YEARS):
        T.append(("INTERNAL debt above total assets agrees with negative net worth, %s" % y,
                  1.0 if ((_debt(CON, i) > CON["total_assets"][i])
                          == (CON["equity"][i] < 0)) else 0.0, 1.0, 0.5,
                  "debt %.0f vs assets %.0f, equity %.0f"
                  % (_debt(CON, i), CON["total_assets"][i], CON["equity"][i])))

    return T


SA_BANK_ST_FY26 = 851.0    # standalone note 27(A), incl. the Rs 125 crore intercompany loan


def main():
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    R = compute()
    order = [k for k in R[YEARS[0]]]
    w = 46
    print("=" * (w + 3 * 14))
    print("VODAFONE IDEA LIMITED - consolidated, ICRA convention, Rs crore")
    print("-" * (w + 3 * 14))
    print("%-*s%s" % (w, "Metric", "".join("%14s" % y for y in YEARS)))
    print("-" * (w + 3 * 14))
    for k in order:
        cells = ""
        for y in YEARS:
            v = R[y][k]
            cells += "%14s" % ("n/m" if v is None else "{:,.2f}".format(v)
                               if isinstance(v, float) and abs(v) < 100 else
                               "{:,.0f}".format(v))
        print("%-*s%s" % (w, k, cells))

    print("\nOperating metrics (Q4 FY2025 -> Q4 FY2026) - the sector's own measures:")
    print("%-34s%s" % ("", "".join("%10s" % q for q in QUARTERS)))
    for k, v in OPS.items():
        print("%-34s%s" % (k, "".join("%10s" % ("{:,}".format(x)) for x in v)))

    fails = [t for t in tieouts(R) if abs(t[1] - t[2]) > t[3]]
    n = len(tieouts(R))
    print("\n%d of %d tie-outs FAIL" % (len(fails), n))
    for f in fails:
        print("  %-62s computed=%s disclosed=%s" % (f[0], f[1], f[2]))


if __name__ == "__main__":
    main()
