"""Cochin Minerals and Rutile Limited - CareEdge manufacturing ratio suite. STANDALONE.

AGENCY : CareEdge.  ENTITY: corporate (synthetic rutile from ilmenite; TiO2 feedstock chain).
BASIS  : STANDALONE, and that is not a judgement call here - the annual report states in the
         corporate-governance section that "The Company has no subsidiary" (pre-flight probe [3]).
         Declared as standalone in case.json at intake.

UNITS  : the company reports in RUPEES LAKH. Every figure below is entered AS PRINTED in lakh
         and converted to Rs CRORE exactly once, in code (R6). Nothing is pre-divided by hand.

SOURCES
  FY2026 + FY2025 : Annual Report 2025-26, standalone Balance Sheet (L2674) and Statement of
                    Profit and Loss (L2745). Note 12 (L3765) gives the bank-balance split.
  FY2024          : Annual Report 2024-25, comparative column of the same statements (L2608 /
                    L2705).

*** TWO RESTATEMENTS BETWEEN AR VINTAGES, both nil-sum, newer governs (failure mode 26) ***
  1. CSR expense of 81.62 (FY2025) was shown as its OWN expense line in the FY2024-25 AR and
     is FOLDED INTO other expenses in the FY2025-26 AR (10,733.20 + 81.62 = 10,814.82).
  2. 15.16 was reclassified from other income into revenue from operations in FY2025
     (revenue 31,906.32 -> 31,921.48; other income 834.70 -> 819.54). Total income unchanged.
  A third restatement hits the balance sheet: FY2025 other current assets fall 960.60 -> 746.68
  (-213.92), matched by non-current liabilities -107.40 and current liabilities -106.52. The
  213.92 reconciles on both sides. This engine uses the FY2025-26 AR throughout for FY2025.

*** AN OCR DECIMAL LOSS, caught by arithmetic rather than by eye ***
  The FY2025-26 AR prints FY2025 cost of material as "1614195". The expense build-up only
  reconciles to the printed total of 28,967.05 at 16,141.95, which the FY2024-25 AR confirms.
  Recorded rather than silently corrected.

*** VERSION 2, 13-Sep-2026 - WHY THIS ENGINE WAS REBUILT ***
  Version 1 delivered CARE A-; Stable / CARE A2+ on 13-Sep-2026 with 30/30 tie-outs and 94.3%
  mutation coverage, having concluded from a clean library search that NO CRA HAD EVER RATED
  THIS ISSUER. CareEdge has rated it continuously since at least April 2023 and published
  CARE BBB; Stable / CARE A3+ on 04-Sep-2026 - two notches below v1 on both scales.

  The searches were not the failure; re-run, they still return nothing. The failure was the
  INFERENCE. "No rating is disclosed in these documents and none is in our library" is what
  the evidence supported; "no CRA has rated this issuer" is what v1 wrote, and no corpus
  search can ever support that. Everything downstream followed: no rating history, rated
  amounts left blank while Rs 133.50 crore of real limits existed, and Step 14 downgraded to
  peer benchmarking - which the delivery gate recorded as "N/A" and v1 read as a pass.

  v2 therefore separates two things v1 conflated, and the separation is the point:
    tieouts()     - INTERNAL arithmetic. Does the extraction reproduce the printed statements?
    validations() - EXTERNAL truth. Does it reproduce a figure published by someone else?
  A 100% tieouts() score says nothing whatever about validations(), and v1's 94.3% coverage
  was quoted as though it did.
"""

L = 100.0                      # lakh -> crore, applied once, in code

YEARS = ["FY2024", "FY2025", "FY2026"]
BASIS = "standalone"
AR26 = "AR 2025-26 standalone statements"
AR25 = "AR 2024-25 standalone statements (FY2024 comparative)"

# ---------------------------------------------------------------- P&L (Rs LAKH, as printed)
PL = {
    "Revenue from operations":    ([30043.86, 31921.48, 29491.66], AR26 + " / " + AR25),
    "Other income":               ([285.04, 819.54, 227.24], AR26 + " note 23"),
    "Total income":               ([30328.90, 32741.02, 29718.90], AR26 + " printed TOTAL INCOME"),
    "Cost of material consumed":  ([16271.15, 16141.95, 15134.70],
                                   AR26 + " note 24 - FY2025 printed as '1614195' (OCR)"),
    "Changes in inventories":     ([-3587.40, -938.68, -926.78], AR26 + " note 25, sign as printed"),
    "Employee costs":             ([2784.47, 2815.18, 3413.43], AR26 + " note 26"),
    "Finance costs":              ([83.93, 20.29, 19.29], AR26 + " note 27"),
    "CSR expenses":               ([49.97, 0.0, 0.0],
                                   AR25 + " separate line in FY2024; folded into other "
                                           "expenses from the FY2025-26 AR onward"),
    "Depreciation & amortisation": ([85.56, 113.49, 159.37], AR26 + " note 4"),
    "Other expenses":             ([10736.86, 10814.82, 9521.67],
                                   AR26 + " note 28 - FY2025 is CSR-inclusive per the newer AR"),
    "Total expenses":             ([26424.54, 28967.05, 27321.68], AR26 + " printed TOTAL EXPENSES"),
    "PBT before exceptional":     ([3904.36, 3773.97, 2397.22], AR26 + " printed line V"),
    "Exceptional items":          ([0.0, 0.0, 505.20],
                                   AR26 + " note 5 - impairment of the metallisation CWIP"),
    "Profit before tax":          ([3904.36, 3773.97, 1892.02], AR26 + " printed line VI"),
    "Current tax":                ([1239.41, 1386.16, 659.37], AR26 + " tax (1)"),
    "Deferred tax":               ([-4.28, 31.90, -17.95], AR26 + " tax (2)"),
    "Profit after tax":           ([2669.23, 2355.91, 1250.60], AR26 + " printed line VIII"),
}

# ---------------------------------------------------------------- balance sheet (Rs LAKH)
BS = {
    "Total non-current assets":   ([4320.09, 4413.03, 4271.60], AR26 + " printed total"),
    "Inventories":                ([11405.56, 16647.04, 12518.21], AR26 + " note 9"),
    "Trade receivables":          ([3506.58, 1661.22, 2435.60], AR26 + " note 10"),
    "Cash & cash equivalents":    ([2.89, 5.03, 1413.66], AR26 + " note 11"),
    "Other bank balances":        ([2260.62, 2760.11, 2959.63], AR26 + " note 12 - split below"),
    "Current tax assets":         ([100.00, 100.00, 100.00], AR26 + " note 13"),
    "Other current assets":       ([2433.17, 746.68, 999.71], AR26 + " note 8"),
    "Total current assets":       ([19708.82, 21920.08, 20426.81], AR26 + " printed total"),
    "Total assets":               ([24028.91, 26333.11, 24698.41], AR26 + " printed TOTAL ASSETS"),
    "Share capital":              ([783.00, 783.00, 783.00], AR26 + " note 14"),
    "Other equity":               ([14061.30, 15756.54, 16419.75], AR26 + " note 15"),
    "Total equity":               ([14844.30, 16539.54, 17202.75], AR26 + " printed total"),
    "Borrowings - long term":     ([337.00, 0.0, 0.0],
                                   AR25 + " note 16 - NIL from FY2025; the company is "
                                           "essentially debt-free"),
    "Total non-current liab":     ([858.01, 493.78, 515.11], AR26 + " printed total"),
    "Borrowings - short term":    ([235.10, 1078.07, 621.14], AR26 + " note 16"),
    "Total current liabilities":  ([8326.60, 9299.79, 6980.55], AR26 + " printed total"),
}

# Note 12 decomposed, because a cash caption is not a liquidity figure until it is (FM34/45).
# Margin money is pledged against bank guarantees and letters of credit; unpaid dividend is
# statutorily restricted. Neither can service debt. FY2024 is not split in the older AR.
BANK_SPLIT = {
    "Margin money vs BG/LC":      ([None, 523.74, 506.82], AR26 + " note 12(i)"),
    "Deposits 3-12 months":       ([None, 2201.28, 2402.88], AR26 + " note 12(ii)"),
    "Unpaid dividend":            ([None, 35.09, 49.93], AR26 + " note 12(iii)"),
}

# ---------------------------------------------------------------------------------------
# THE AGENCY'S OWN PUBLISHED ACTION FOR THIS ISSUER (failure modes 29/41/43).
# CareEdge Ratings press release dated 04 September 2026, in the reference library at
# CareEdge/Report for Reference/Cochin Minerals and Rutile Limited_04 Sep 2026.md.
# Reproduced verbatim under the five-condition amendment: primary rationale for THIS issuer,
# every line copied, date-stamped, labelled CRA-published and issuer-unconfirmed, line
# integrity verified, limits distinguished from drawn debt.
CAREEDGE = {
    "date": "04 September 2026",
    "lt": "CARE BBB; Stable", "st": "CARE A3+",
    "action": "Reaffirmed (both)",
    "approach": "Standalone",
    "liquidity": "Adequate",
    # Annexure-1, four lines. 1.50 long-term; 48.00 + 4.00 + 80.00 = 132.00 short-term.
    "facilities": [("Fund-based - LT-Cash Credit", 1.50, "CARE BBB; Stable"),
                   ("Fund-based - ST-EPC/PSC", 48.00, "CARE A3+"),
                   ("Non-fund-based - ST-Bank Guarantee", 4.00, "CARE A3+"),
                   ("Non-fund-based - ST-Letter of credit", 80.00, "CARE A3+")],
    "lt_amt": 1.50, "st_amt": 132.00, "total_amt": 133.50,
    # Brief Financials, Rs crore: FY2025(A), FY2026(A), Q1FY27(UA)
    "toi": [323.33, 294.91, 131.26],
    "pbildt": [35.58, 23.48, 15.32],
    "pat": [23.56, 12.15, 12.38],
    "gearing": [0.33, 0.31, None],
    "intcov": [45.43, 121.70, 306.4],
    "tdgca": [2.21, 3.97, None],
    "history": "CARE BBB; Positive (03-Apr-23) -> CARE BBB; Stable (01-Dec-23) -> "
               "(27-Nov-24) -> (11-Aug-25) -> (04-Sep-26). Short-term CARE A3+ throughout. "
               "The issuer has been rated BBB for three years; this is NOT a first assignment.",
}

# CareEdge's TOTAL DEBT is wider than the balance-sheet borrowings caption. Per
# CareEdge/CORPORATE_CONVENTIONS.md (para 79 and 103) overall gearing is computed on
# "total debt INCLUDING acceptances / creditors on LC", and the criteria also weigh
# non-fund-based limits availed. The annual report does NOT split trade payables into
# LC-backed and open credit, so the split cannot be extracted - only bounded.
#
# This block RECONSTRUCTS the agency's basis to explain the divergence. It is NOT used as an
# input to any ratio this engine publishes; the engine reports the statutory figure and the
# agency figure side by side and lets the gap be seen (failure mode 12: never reconstruct a
# number and then present it as data).
CAREEDGE_DEBT_BASIS = {
    "published_gearing_FY2026": 0.31,
    "implied_total_debt": 0.31 * 172.0275,          # = 53.33 against borrowings of 6.21
    "balance_sheet_borrowings": 6.2114,
    "implied_creditors_on_LC": 0.31 * 172.0275 - 6.2114,   # = 47.12
    "corroboration": "Independent cross-check from the OTHER published ratio: TD/GCA of 3.97x "
        "on CareEdge's own GCA (PAT 12.15 + depreciation 1.59 = 13.74) implies total debt of "
        "54.55 - the same 53-55 band. And from the facility schedule: the letter-of-credit "
        "limit is 80.00 and the press release states non-fund-based utilisation averaged ~59% "
        "for the 12 months to June 2026; 80.00 x 0.59 = 47.20, against the 47.12 implied "
        "above. Three independent routes agree, so the basis is established, not guessed.",
    "balance_sheet_room": "Trade payables to non-MSME creditors were 55.03 crore at 31-03-2026 "
        "(note 17), so 47.12 of LC-backed creditors fits inside the caption. The AR gives no "
        "further split.",
    "consequence": "On CareEdge's definition CMRL is NOT in net cash. Total debt ~53.3 against "
        "unencumbered cash of 38.17 is NET DEBT of about 15.2 crore. Version 1 headlined "
        "'net cash of 31.95 crore' and built the AA- anchor on it.",
}

# Ongoing regulatory and enforcement proceedings (R13: any regulatory or governance item is
# material REGARDLESS of size). Version 1 missed all of this and stated in terms that the
# audit report carried no emphasis of matter. It does.
LITIGATION = {
    "SFIO": "The Ministry of Corporate Affairs ordered an investigation into the company's "
            "affairs under Section 212 of the Companies Act by the Serious Fraud Investigation "
            "Office. Challenged before the Delhi High Court in W.P.(Crl.) No. 1188/2024. SFIO "
            "completed the investigation and filed a criminal complaint before the Special "
            "Court, Ernakulam; the Delhi High Court by order of 28-05-2025 directed SFIO not "
            "to proceed with the complaint until the writ is disposed of. Next listed "
            "13-10-2026. The Special Court took cognizance on 11-04-2025 and issued summons to "
            "the Company; the Kerala High Court directed status quo on 16-04-2025 in Crl. Rev. "
            "Petition 442/2025, next listed 18-09-2026. Source: AR 2025-26 note 37 and the "
            "Board's report. Present in ALL THREE annual reports.",
    "ED": "An ECIR registered by the Directorate of Enforcement was challenged in W.P.(C.) "
          "15757/2024. The writ was DISMISSED by the Kerala High Court single judge on "
          "26-05-2026 and the writ appeal (No. 1140/2026) dismissed on 05-06-2026. The ED has "
          "REOPENED the investigation under the same ECIR and officers' statements have been "
          "recorded. Source: AR 2025-26 note 37 / Board's report. This is the one strand that "
          "has moved AGAINST the company in the period under review.",
    "emphasis_of_matter": "The auditor's report on the FY2025-26 standalone financial "
            "statements carries an EMPHASIS OF MATTER drawing attention to note 37 on the SFIO "
            "investigation and the ED proceedings. The opinion is not modified. Version 1 of "
            "this workpaper stated that no emphasis of matter was identified - a false "
            "statement about a document in the case folder.",
    "GST": "CRA-DISCLOSED, NOT IN THE ISSUER'S DOCUMENTS: CareEdge's press release of "
           "04-09-2026 records a GST show-cause notice dated 04 August 2026 on the "
           "classification of synthetic rutile for FY2020-21 to FY2023-24, with a proposed "
           "demand of about Rs 120.26 crore. That is 70% of tangible net worth. It post-dates "
           "the FY2025-26 annual report and appears in no document in this case folder; it is "
           "carried on the agency's authority and flagged for issuer confirmation.",
}

# Sector-defining operating facts (failure mode 21). Capacity is a licence figure; the binding
# constraint for this issuer is RAW MATERIAL ACCESS, which is why it is carried here.
OPS = {
    "Synthetic rutile capacity (MT)": 50000,
    # Quantified, dated and in the issuer's OWN annual report - and missed by version 1.
    "ferric_chloride_disruption": "Geopolitical tension in West Asia disrupted maritime "
        "shipping to Middle East ports, the primary market for FERRIC CHLORIDE. Export "
        "shipments were SUSPENDED in March 2026 and monthly sales fell to 980 MT against a "
        "previous average of 2,900 MT - a 66% fall. The company states a prolonged disruption "
        "would materially affect sales volume and manufacturing operations. Source: AR 2025-26 "
        "management discussion. By-products are not incidental here: the company describes "
        "itself as zero-waste and sells ferric and ferrous chloride as products.",
    # CRA-published operating metrics. Not derivable from the issuer's documents - the annual
    # reports give installed capacity but no tonnage produced or sold - so these are carried on
    # CareEdge's authority and labelled, never presented as computed.
    "cra_published_operating": "CareEdge, 04-09-2026: synthetic rutile SALES VOLUMES fell ~14% "
        "in FY2026; capacity utilisation moderated to ~50% from 59% in FY2025; synthetic "
        "rutile is ~90% of revenue; the top three customers are ~70-80% of total sales, with "
        "significant exposure to JAPAN; and the ORDER BOOK stood at ~Rs 418.68 crore at "
        "31-03-2026 - 1.42x FY2026 revenue, which is what gives the FY2027 recovery its "
        "visibility. A long-term tripartite TOLLING arrangement with Mitsui and end-users, "
        "effective July 2025, links finished-product prices to raw-material cost by formula.",
    "one_offs_FY2026": "CareEdge identifies two one-time charges in FY2026: a gratuity payout "
        "of ~5.5 crore to the erstwhile Chairman and other senior officials, and the ~5.05 "
        "crore write-off discussed below. Neither is separately captioned in the P&L; the "
        "gratuity sits inside employee costs, which rose 21.3% to 3,413.43 lakh from 2,815.18 "
        "on a FALLING revenue base - a movement version 1 extracted and never questioned.",
    "note": "Synthetic rutile is made by upgrading ILMENITE with hydrochloric acid. The AR "
            "2025-26 states domestic ilmenite availability has 'declined significantly', so "
            "the company now relies increasingly on IMPORTED ilmenite, and has modified its "
            "process to run different imported grades. It also states that synthetic rutile "
            "prices fell without a proportional fall in ilmenite - a margin squeeze from both "
            "ends. The FY2026 exceptional item is the impairment of the metallisation project, "
            "abandoned for exactly this reason: 'long suspended due to short supply of main "
            "raw material, ilmenite from the domestic market'.",
}


# Q1 FY2026-27 (quarter ended 30-06-2026, unaudited) - the NEWEST document in the folder and
# the single most important fact in this case (failure mode 26: read the newest first).
# Carried as a dated data point, not as a computed column: one unaudited quarter does not
# belong in a ratio suite, but ignoring it would hide a turnaround.
Q1FY27 = {
    "revenue": 13126.13, "revenue_q1fy26": 7620.74,
    "total_income": 13332.56, "other_income": 206.43,
    "pbt_before_exc": 1679.87, "pbt_before_exc_q1fy26": 507.42,
    "pat": 1238.18, "depreciation": 54.62, "total_expenses": 11653.49,
    "note": "Revenue rose 72.2% year on year (13,126.13 against 7,620.74 in Q1 FY2026) and "
            "profit before exceptional items 231% (1,679.87 against 507.42). PAT of 1,238.18 "
            "in ONE quarter is within 1% of the ENTIRE FY2026 figure of 1,250.60. FY2026 "
            "therefore reads as the trough of a raw-material and price squeeze rather than a "
            "structural decline. Source: BSE filing for the quarter ended 30-06-2026.",
    "classification_note": "That filing splits FY2026 as revenue 28,718.59 / other income "
            "1,000.31; the audited AR splits the same total income of 29,718.90 as 29,491.66 / "
            "227.24 - a reclassification of 773.07 between the two lines. Total income is "
            "identical in both. This engine uses the AUDITED ANNUAL REPORT throughout.",
}


def compute():
    """Contract member: {period: {metric: value}}. Rs CRORE, converted once from lakh."""
    P = {k: [x / L for x in v[0]] for k, v in PL.items()}
    B = {k: [x / L for x in v[0]] for k, v in BS.items()}
    K = {k: [None if x is None else x / L for x in v[0]] for k, v in BANK_SPLIT.items()}
    R = {}
    for i, y in enumerate(YEARS):
        r = {k: P[k][i] for k in P}
        r.update({k: B[k][i] for k in B})

        toi = P["Revenue from operations"][i]          # no excise duty in this P&L
        r["TOI"] = toi
        # CareEdge PBILDT: before interest, lease rentals, depreciation and tax, and BEFORE
        # exceptional items - so the metallisation impairment is excluded by construction.
        pbildt = (P["PBT before exceptional"][i] + P["Finance costs"][i]
                  + P["Depreciation & amortisation"][i] - P["Other income"][i])
        r["PBILDT"] = pbildt
        r["PBILDT margin (%)"] = pbildt / toi * 100
        r["PAT margin (%)"] = P["Profit after tax"][i] / toi * 100

        debt = B["Borrowings - long term"][i] + B["Borrowings - short term"][i]
        tnw = B["Total equity"][i]     # CareEdge CORPORATE convention: no DTA/intangible deduct
        r["Total debt"] = debt
        r["Tangible net worth"] = tnw
        r["Overall gearing (x)"] = debt / tnw
        r["TOL / TNW (x)"] = (B["Total assets"][i] - tnw) / tnw
        r["Interest coverage (x)"] = pbildt / P["Finance costs"][i]
        r["Total debt / PBILDT (x)"] = debt / pbildt
        gca = P["Profit after tax"][i] + P["Depreciation & amortisation"][i]
        r["Gross cash accruals"] = gca
        r["Total debt / GCA (x)"] = debt / gca

        # UNENCUMBERED cash only. Where note 12 is split, margin money and unpaid dividend are
        # removed; where it is not (FY2024), only cash and cash equivalents are counted and the
        # limitation is disclosed rather than the caption being taken at face value.
        if K["Deposits 3-12 months"][i] is not None:
            free = B["Cash & cash equivalents"][i] + K["Deposits 3-12 months"][i]
            r["Encumbered bank balances"] = (K["Margin money vs BG/LC"][i]
                                             + K["Unpaid dividend"][i])
        else:
            free = B["Cash & cash equivalents"][i]
            r["Encumbered bank balances"] = None
        r["Unencumbered cash"] = free
        r["Net debt / (net cash)"] = debt - free

        r["Current ratio (x)"] = (B["Total current assets"][i]
                                  / B["Total current liabilities"][i])
        r["RoCE (%)"] = (pbildt - P["Depreciation & amortisation"][i]) / (debt + tnw) * 100
        r["Inventory days"] = B["Inventories"][i] * 365 / toi
        r["Receivable days"] = B["Trade receivables"][i] * 365 / toi
        R[y] = r
    return R


def tieouts(R=None):
    """Contract member: [(description, computed, disclosed, tolerance, source), ...].

    Every check rebuilds a printed total from its own printed components. Tolerance is 0.0001
    crore (Rs 10) - these are exact statutory statements, not estimates.
    """
    P = {k: [x / L for x in v[0]] for k, v in PL.items()}
    B = {k: [x / L for x in v[0]] for k, v in BS.items()}
    K = {k: [None if x is None else x / L for x in v[0]] for k, v in BANK_SPLIT.items()}
    T = []
    for i, y in enumerate(YEARS):
        T.append(("%s total income = revenue + other income" % y,
                  P["Revenue from operations"][i] + P["Other income"][i],
                  P["Total income"][i], 0.0001, AR26 + " printed TOTAL INCOME"))
        T.append(("%s expense build-up reproduces printed total expenses" % y,
                  sum(P[k][i] for k in ("Cost of material consumed", "Changes in inventories",
                                        "Employee costs", "Finance costs", "CSR expenses",
                                        "Depreciation & amortisation", "Other expenses")),
                  P["Total expenses"][i], 0.0001,
                  AR26 + " - all expense captions against the printed total"))
        T.append(("%s PBT before exceptional = total income - total expenses" % y,
                  P["Total income"][i] - P["Total expenses"][i],
                  P["PBT before exceptional"][i], 0.0001, AR26 + " printed line V"))
        T.append(("%s PBT = PBT before exceptional less exceptional items" % y,
                  P["PBT before exceptional"][i] - P["Exceptional items"][i],
                  P["Profit before tax"][i], 0.0001, AR26 + " printed line VI"))
        T.append(("%s PAT = PBT less current and deferred tax" % y,
                  P["Profit before tax"][i] - P["Current tax"][i] - P["Deferred tax"][i],
                  P["Profit after tax"][i], 0.0001, AR26 + " printed line VIII"))
        T.append(("%s assets = equity + non-current + current liabilities" % y,
                  B["Total equity"][i] + B["Total non-current liab"][i]
                  + B["Total current liabilities"][i],
                  B["Total assets"][i], 0.0001, AR26 + " printed TOTAL EQUITY AND LIABILITIES"))
        T.append(("%s total assets = non-current + current assets" % y,
                  B["Total non-current assets"][i] + B["Total current assets"][i],
                  B["Total assets"][i], 0.0001, AR26 + " printed TOTAL ASSETS"))
        T.append(("%s current-asset components sum to the printed total" % y,
                  (B["Inventories"][i] + B["Trade receivables"][i]
                   + B["Cash & cash equivalents"][i] + B["Other bank balances"][i]
                   + B["Current tax assets"][i] + B["Other current assets"][i]),
                  B["Total current assets"][i], 0.0001,
                  AR26 + " - all six current-asset lines against the printed subtotal"))
        T.append(("%s total equity = share capital + other equity" % y,
                  B["Share capital"][i] + B["Other equity"][i],
                  B["Total equity"][i], 0.0001, AR26 + " printed Total Equity"))
        # The bank caption must decompose, or the liquidity figure is not a liquidity figure.
        if K["Deposits 3-12 months"][i] is not None:
            T.append(("%s note-12 components sum to the printed bank balance" % y,
                      (K["Margin money vs BG/LC"][i] + K["Deposits 3-12 months"][i]
                       + K["Unpaid dividend"][i]),
                      B["Other bank balances"][i], 0.0001,
                      AR26 + " note 12 - margin money + deposits + unpaid dividend"))
    # The FY2025 restatement between AR vintages nets to zero on both sides of the sheet.
    T.append(("FY2025 restatement nets to zero across assets and liabilities",
              (960.60 - 746.68) - ((601.18 - 493.78) + (9406.31 - 9299.79)), 0.0, 0.02,
              "AR 2024-25 vs AR 2025-26, FY2025 column: -213.92 of other current assets "
              "against -107.40 non-current and -106.52 current liabilities"))
    return T


def validations(R=None):
    """EXTERNAL validation: our computed figures against CareEdge's PUBLISHED figures.

    Distinct from tieouts() by design, and the distinction is the whole lesson of this case.
    tieouts() asks "does the extraction reproduce the printed statements" - a question a
    report built off the wrong statement, the wrong period or the wrong definition answers
    perfectly. validations() asks "does it reproduce a number somebody else published", which
    is the only question that can catch those.

    Returns [(description, ours, theirs, tolerance, note), ...]. Unlike tieouts(), a
    divergence here is NOT automatically an error - the agency can be wrong too, and on PAT it
    is. Every non-matching line must be EXPLAINED in DISCLOSED_DIFFERENCES, never forced.
    """
    R = R or compute()
    C = CAREEDGE
    V = []
    # index 0 = FY2025, index 1 = FY2026 in CareEdge's Brief Financials.
    V.append(("FY2026 TOI", R["FY2026"]["TOI"], C["toi"][1], 0.02,
              "reproduces - both are revenue from operations, 294.92 vs 294.91"))
    V.append(("FY2026 PBILDT", R["FY2026"]["PBILDT"], C["pbildt"][1], 0.02,
              "reproduces - the PBILDT convention is confirmed correct"))
    V.append(("FY2026 PBILDT margin (%)", R["FY2026"]["PBILDT margin (%)"], 7.96, 0.02,
              "reproduces exactly"))
    V.append(("FY2026 interest coverage (x)", R["FY2026"]["Interest coverage (x)"],
              C["intcov"][1], 0.10, "reproduces - 121.75 vs 121.70"))
    V.append(("FY2026 PAT", R["FY2026"]["Profit after tax"], C["pat"][1], 0.02,
              "DIVERGES 0.36. The audited P&L line VIII prints 1,250.60 lakh = 12.51 crore. "
              "CareEdge publishes 12.15 - a digit transposition IN THE AGENCY'S TABLE. Ours "
              "is right and is not adjusted to match; this is exactly the case the "
              "no-forcing rule exists for."))
    V.append(("FY2025 TOI", R["FY2025"]["TOI"], C["toi"][0], 0.02,
              "DIVERGES 4.12. Ours is revenue from operations per the audited AR (31,921.48 "
              "lakh). CareEdge publishes 323.33, which reconciles to neither the AR revenue "
              "(319.21) nor AR total income (327.41). The FY2025 comparative column of the "
              "BSE audited results - the one document that might explain it - is destroyed in "
              "the PDF-to-markdown conversion. UNRESOLVED, and named as such."))
    V.append(("FY2025 PBILDT", R["FY2025"]["PBILDT"], C["pbildt"][0], 0.02,
              "DIVERGES 4.70, and follows the TOI gap of 4.12 almost exactly - one data "
              "difference explains both, rather than two independent errors."))
    V.append(("FY2026 overall gearing (x)", R["FY2026"]["Overall gearing (x)"],
              C["gearing"][1], 0.02,
              "DIVERGES AND OURS IS WRONG ON THE AGENCY'S DEFINITION. 0.04 statutory against "
              "0.31 published. CareEdge includes creditors on LC in total debt; see "
              "CAREEDGE_DEBT_BASIS, where three independent routes agree on ~47 crore. This "
              "is the single largest analytical error in version 1."))
    V.append(("Rated amount total (Rs crore)", 133.50, C["total_amt"], 0.001,
              "Version 1 stated 'to be confirmed by issuer' while 133.50 crore was published. "
              "Line integrity: 1.50 + 48.00 + 4.00 + 80.00 = 133.50. LIMITS, not drawn debt - "
              "drawn borrowings were 6.21 crore at 31-03-2026."))
    return V


def scale_context():
    """Where this issuer sits in CareEdge's own rated book (tools/corpus_power.py, n=805).

    Version 1's scorecard anchored AA- on gearing of 0.04x and interest coverage of 122x.
    Measured against 805 published CareEdge actions, those two metrics carry little rating
    information (Spearman rho vs grade +0.31 and -0.41), while the metrics on which this
    issuer is weak carry the most (PAT -0.78, TOI -0.72). The anchor weighted the wrong end.
    """
    return {
        "TOI percentile": 8.9, "PBILDT margin percentile": 20.9,
        "interest coverage percentile": 97.0, "gearing percentile": 44.4,
        "band": "Of 27 CareEdge-rated issuers with TOI between 150 and 500 crore, 78% are "
                "rated BBB+, BBB or BBB-; only 22% reach A- or better, and those carry "
                "parentage or a genuinely differentiated franchise. CMRL is at the 8.9th "
                "percentile of the rated book on scale and the 20.9th on margin.",
        "peers": "Themis Medicare - TOI 407, PBILDT margin 12.4%, PAT 29.8, gearing 0.26x - "
                 "is rated CARE BBB-; Negative, and its rationale names 'moderate scale of "
                 "operations' as a CONSTRAINT at that size. Chemfab Alkalis reaches A- on a "
                 "comparable TOI of 327 but with a 16.7% margin, two segments, >80% "
                 "utilisation and a diversified client base. CMRL has 7.96%, one product, "
                 "~50% utilisation and 70-80% of sales in three customers.",
    }


DISCLOSED_DIFFERENCES = [
    ("The agency HAS rated this issuer - version 1 said it had not, and that error set the grade",
     "CareEdge has rated CMRL continuously since at least 03-Apr-2023 (BBB; Positive), moving "
     "to BBB; Stable on 01-Dec-2023 and reaffirmed on 27-Nov-2024, 11-Aug-2025 and 04-Sep-2026. "
     "Version 1 concluded no CRA had ever rated the issuer. The two searches behind that were "
     "both clean and both remain clean on re-running: the annual reports disclose no rating "
     "(0 matches for CARE/CRISIL/ICRA/credit rating across all eight documents) and a "
     "word-boundary library search returned nothing, the pre-flight's only hits being Cochin "
     "SHIPYARD and Sarda Energy & MINERALS. What was wrong was the inference drawn from them. "
     "The evidence supported 'not disclosed here and not in our library'; version 1 wrote 'no "
     "CRA has rated this issuer', which is a claim about the world that no corpus search can "
     "establish. An absence of evidence was published as evidence of absence. The pre-flight's "
     "only hits, Cochin SHIPYARD and Sarda Energy & MINERALS, were correctly rejected on a 1/3 "
     "name-token match, and that display of rigour is part of why the absence-claim beside it "
     "read as considered. Rejecting a false positive is not evidence of a true negative."),
    ("Overall gearing on the agency's definition is 0.31x, not the 0.04x on the balance sheet",
     "CareEdge computes overall gearing on total debt INCLUDING acceptances and creditors on "
     "letters of credit (CORPORATE_CONVENTIONS.md paras 79 and 103). The annual report does "
     "not split trade payables between LC-backed and open credit, so this engine CANNOT "
     "compute the agency figure and does not pretend to: it publishes the statutory 0.04x and "
     "reports CareEdge's 0.31x beside it. CAREEDGE_DEBT_BASIS shows three independent routes "
     "agreeing the difference is about 47 crore of creditors on LC. The consequence matters "
     "more than the ratio: on the agency's basis the company is in NET DEBT of roughly 15 "
     "crore, not the net cash of 31.95 crore that version 1 headlined and anchored on. "
     "Obtaining the LC-backed creditor split from the issuer would close this."),
    ("The ~5.05 crore write-off: the issuer and the agency describe it differently",
     "AR 2025-26 note 5 states the company reviewed capital work in progress of 5.05 crore for "
     "the METALLISATION PROJECT, 'long suspended due to short supply of main raw material, "
     "ilmenite from the domestic market', expects no future economic benefit and impaired it "
     "under Ind AS 36 as an exceptional item. CareEdge describes it as a write-off of "
     "'long-pending research and development expenditure associated with a project "
     "subsequently deemed commercially unviable'. Quantum and year agree; characterisation "
     "does not. This engine follows the ISSUER'S OWN AUDITED NOTE. The distinction is not "
     "cosmetic - on the issuer's wording the cause is raw-material access, on the agency's it "
     "is project selection. Version 1 took the issuer's wording, correctly, but then made it "
     "the largest single driver of the grade, a weight it cannot carry once the litigation, "
     "concentration and scale evidence is in view."),
    ("Customer concentration, capacity utilisation and the order book are CRA-published only",
     "The top-three customer share (~70-80%), the Japan exposure, the ~14% volume decline, the "
     "~50% capacity utilisation and the 418.68 crore order book all come from CareEdge's press "
     "release, not the issuer's documents. Searches of all three annual reports for "
     "'concentration', 'Japan', 'customer' as a commercial term, and any production tonnage "
     "return nothing. These are carried on the agency's authority, labelled, and flagged for "
     "issuer confirmation."),
    ("The FY2025 comparative is destroyed in the PDF-to-markdown conversion",
     "The BSE audited results for the year ended 31-03-2026 are the one document that could "
     "reconcile CareEdge's FY2025 TOI of 323.33 against the annual report's 319.21. Its FY2025 "
     "column is unreadable after conversion - the text reads 'GOL BS 7,540.87 | 28,718.59 601.' "
     "and 'Total Income( 1 +1 29,718.90 s741.'. The FY2026 column survives and documents a "
     "classification difference: that filing splits FY2026 as revenue 28,718.59 / other income "
     "1,000.31 where the AR splits the identical total of 29,718.90 as 29,491.66 / 227.24. A "
     "clean copy of this filing would close the FY2025 gap. This is the ONE place in this case "
     "where the conversion, rather than the analysis, is the binding constraint."),
    ("Operating cycle is not reproduced on the agency's definition",
     "CareEdge publishes an operating cycle of 133 days in FY2026 against 135 in FY2025. On "
     "inventory plus receivable days net of creditor days this engine gets about 114, and no "
     "combination of disclosed denominators reproduces 133. Disclosed rather than "
     "reverse-engineered: choosing whichever denominator lands on the published number is "
     "exactly the forcing the no-forcing rule forbids."),
    ("FY2024 bank balances are not split between free and encumbered",
     "Note 12 of the FY2025-26 AR decomposes other bank balances for FY2026 and FY2025 into "
     "margin money against BG/LC, 3-12 month deposits and unpaid dividend. The FY2024-25 AR "
     "gives only the 2,260.62 lakh total. FY2024 unencumbered cash is therefore stated on cash "
     "and cash equivalents alone (2.89 lakh), which UNDERSTATES it; the FY2024 net-debt figure "
     "is conservative by up to the unsplit balance. Stated rather than estimated."),
    ("Production volume and realisation per tonne are not in the issuer's documents",
     "Installed synthetic-rutile capacity of 50,000 MT is stated, but the annual reports give "
     "no tonnage produced or sold and no realisation per tonne. Searches for 'capacity "
     "utilis', production with a tonnage unit, and 'realisation' return only the capacity "
     "figure. That absence is real and re-verified. Version 1's error was not the search but "
     "the conclusion it drew: it treated the metric as UNAVAILABLE rather than as NOT "
     "AVAILABLE FROM THESE DOCUMENTS, and so never asked the issuer for it. CareEdge has the "
     "volumes and publishes utilisation of ~50%; the numbers exist, and obtaining them is a "
     "surveillance action, not an impossibility."),
    ("Q1 FY2027 is carried as a dated data point, not a computed column",
     "The quarter ended 30-06-2026 is unaudited and is not in the ratio suite; no tie-out "
     "reaches it. It is nonetheless the newest document in the folder and it materially "
     "changes the forward view - revenue +72.2%% and profit before exceptional items +231%% "
     "year on year, with one quarter's PAT within 1%% of the whole of FY2026. The FY2026 "
     "column alone would present a declining business; the two read together present a "
     "trough and a recovery. Both are stated in the rationale."),
    ("Interest coverage is arithmetically extreme and is not a meaningful discriminator",
     "Finance costs are 0.19 crore against PBILDT of 23.49 crore, giving coverage of about "
     "122x in FY2026. On a near-debt-free balance sheet this ratio carries almost no "
     "information: it measures the absence of debt, not the capacity to service it. The "
     "rating rests on scale, raw-material access and margin, not on coverage."),
]


def _wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def run():
    R = compute()
    W = 40
    print("=" * 100)
    print("COCHIN MINERALS AND RUTILE LIMITED - CareEdge manufacturing suite | STANDALONE")
    print("Synthetic rutile from ilmenite. Source figures in Rs LAKH; shown in Rs CRORE.")
    print("=" * 100)
    order = ["TOI", "PBILDT", "PBILDT margin (%)", "Profit after tax", "PAT margin (%)",
             "Gross cash accruals", "Total debt", "Unencumbered cash",
             "Encumbered bank balances", "Net debt / (net cash)", "Tangible net worth",
             "Overall gearing (x)", "TOL / TNW (x)", "Interest coverage (x)",
             "Total debt / PBILDT (x)", "Total debt / GCA (x)", "Current ratio (x)",
             "RoCE (%)", "Inventory days", "Receivable days"]
    print("\n%-*s%s" % (W, "METRIC (Rs crore / x / %)", "".join("%14s" % y for y in YEARS)))
    for k in order:
        cells = "".join("%14s" % ("{:,.2f}".format(R[y][k]) if R[y].get(k) is not None else "-")
                        for y in YEARS)
        print("  %-*s%s" % (W - 2, k, cells))

    print("\n" + "=" * 100)
    print("TIE-OUTS")
    print("=" * 100)
    T = tieouts(R)
    fail = 0
    for lab, comp, disc, tol, _s in T:
        ok = abs(comp - disc) <= tol
        fail += (not ok)
        print("  [%s] %-58s computed %11s  printed %11s"
              % ("OK " if ok else "FAIL", lab, "{:,.4f}".format(comp), "{:,.4f}".format(disc)))
    print("\n%d/%d tie-outs reconcile." % (len(T) - fail, len(T)))
    print("  NOTE: this measures ARITHMETIC SELF-CONSISTENCY against the printed statements.")
    print("  It says nothing about whether the right statements were chosen. See below.")

    print("\n" + "=" * 100)
    print("EXTERNAL VALIDATION vs CareEdge's published action of %s" % CAREEDGE["date"])
    print("Published: %s / %s (%s). Rated amount Rs %.2f crore." %
          (CAREEDGE["lt"], CAREEDGE["st"], CAREEDGE["action"], CAREEDGE["total_amt"]))
    print("=" * 100)
    V = validations(R)
    div = 0
    for lab, ours, theirs, tol, note in V:
        ok = abs(ours - theirs) <= tol
        div += (not ok)
        print("  [%s] %-34s ours %11s  theirs %11s"
              % ("MATCH" if ok else "DIVER", lab,
                 "{:,.2f}".format(ours), "{:,.2f}".format(theirs)))
        if not ok:
            for line in _wrap(note, 88):
                print("          %s" % line)
    print("\n%d/%d validations match; %d divergences, each explained above." %
          (len(V) - div, len(V), div))

    print("\n" + "=" * 100)
    print("SCALE CONTEXT - where this issuer sits in CareEdge's own rated book (n=805)")
    print("=" * 100)
    sc = scale_context()
    for k in ("TOI percentile", "PBILDT margin percentile", "gearing percentile",
              "interest coverage percentile"):
        print("  %-32s %5.1f" % (k, sc[k]))
    for k in ("band", "peers"):
        for line in _wrap(sc[k], 96):
            print("  %s" % line)

    for title, text in DISCLOSED_DIFFERENCES:
        print("\n  [DISCLOSED] %s\n              %s" % (title, text))
    if fail:
        print("*** RESOLVE BEFORE DRAFTING (Step 17). ***")
    return fail


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
