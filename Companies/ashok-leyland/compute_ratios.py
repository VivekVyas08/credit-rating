"""Ashok Leyland Limited (AL) - ratio engine, ICRA corporate (Commercial Vehicles OEM).

Engine contract (tools/engine_contract.py): YEARS, compute(), tieouts(R), DISCLOSED_DIFFERENCES.
Every figure is typed ONCE from the company's own audited annual reports (FY2024, FY2025,
FY2026) and the four quarterly filings in documents/, with the source on each table. All
amounts Rs crore. Periods are financial years ending 31 March.

ANALYTICAL BASIS (R12 - methodology-determined, not an operator choice)
------------------------------------------------------------------------
ICRA 934 (Consolidation, Nov 2024), "Approach for consolidated analysis when a parent and its
subsidiary are in dissimilar businesses": where "the parent is a non-financial sector entity
with a subsidiary in the financial sector (such as the captive finance arm of an automobile
manufacturer) ... the parent and its subsidiary are assessed separately on a standalone basis
by applying the rating methodology of their respective sectors. The standalone analysis,
however, does consider the ongoing and future funding interchange (including the likely
extraordinary support) among them."  AL owns 61.12% of Hinduja Leyland Finance (HLF, an NBFC
with gross loans of Rs 49,157 crore at Mar-26), so the reported consolidated numbers - where
HLF's borrowings are 93% of group debt - do not describe the CV business's credit risk.

  BASIS        consolidated EXCLUDING the financial-services subsidiaries (HLF group) - the
               automotive business: AL + its CV-related subsidiaries (Optare/Switch, OHM,
               Hinduja Tech, Albonair, ...) consolidated; HLF assessed separately with its
               expected funding needs factored in (934 dissimilar-business rule + "Limited
               Consolidation"; same construction as ICRA's M&M rationale, 29-Sep-2025).
               Measured two ways because the segment note gives CV PBIT but not CV D&A:
                 AUTO_*  segment-based (note 3.8; non-financial debt exact from notes 1.20/1.26)
                 ADJ_*   standalone OPBDITA against standalone + non-FS subsidiary debt
                                                                                  -> SEG_*, CONS_*
  RATED ENTITY AL standalone (carries the rated instruments; full ratio suite)    -> SA_* tables
  SUPPLEMENT   reported consolidated (includes HLF) - shown, never relied on      -> CONS_*

Operating profit follows ICRA 960 footnote 5 / ICRA/ICRA_CONVENTIONS.md s1: revenue from
operations less operating costs; interest, dividend, investment gains and every other line of
"Other income" are EXCLUDED (all components read in note 2.2 - none is job-work/scrap; scrap
and export incentives already sit inside revenue from operations).
"""

YEARS = ["FY2023", "FY2024", "FY2025", "FY2026"]
IX = {y: i for i, y in enumerate(YEARS)}
N = None

# =========================================================================================
# 1. STANDALONE - statement of profit and loss
#    FY2023 & FY2024: FY2023-24 AR p116-117; FY2025: FY2024-25 AR p113; FY2026: FY2025-26 AR p123
# =========================================================================================
SA_PL = {
    "Revenue from operations":        [36144.14, 38367.03, 38752.74, 44007.03],
    "Other income":                   [116.14, 246.57, 250.25, 315.17],
    "Cost of materials consumed":     [27246.95, 26916.54, 25711.74, 29722.68],
    "Purchases of stock-in-trade":    [1160.69, 1506.41, 1680.46, 1805.39],
    "Change in inventories":          [-558.49, -510.94, 230.58, -110.93],
    "Employee benefits expense":      [2113.86, 2233.38, 2406.27, 2606.69],
    "Finance costs":                  [289.09, 249.44, 216.91, 169.73],
    "Depreciation and amortisation":  [731.96, 717.81, 719.34, 715.19],
    "Other expenses":                 [3250.43, 3615.06, 3793.13, 4250.95],
    "Exceptional items":              [84.61, -93.72, 103.73, -348.48],
    "Tax expense":                    [730.29, 1174.31, 1045.00, 1248.49],
}

# The AR's own printed subtotals - independent check figures for the line items above.
SA_PL_PRINTED = {
    "Total income":                   [36260.28, 38613.60, 39002.99, 44322.20],
    "Cost of goods sold subtotal":    [27849.15, 27912.01, 27622.78, 31417.14],
    "Total expenses":                 [34234.49, 34727.70, 34758.43, 39159.70],
    "Profit before exceptional & tax": [2025.79, 3885.90, 4244.56, 5162.50],
    "Profit before tax":              [2110.40, 3792.18, 4348.29, 4814.02],
    "Profit for the year":            [1380.11, 2617.87, 3303.29, 3565.53],
}

# Finance cost note 2.5 decomposition (FY2025-26 AR p169; FY2024-25 AR comparatives in it).
# FY2023/FY2024 not decomposed in the extraction - None (named in DISCLOSED_DIFFERENCES).
SA_FIN_COST = {
    "Interest expense net of capitalised": [N, N, 124.89, 70.05],
    "Unwinding of discount on provisions": [N, N, 88.55, 95.69],
    "Interest on lease liability":         [N, N, 3.47, 3.99],
}

# Other income note 2.2 components (FY2025-26 AR p168) - read to decide OPBDITA treatment.
SA_OTHER_INCOME = {
    "Interest income":                     [N, N, 40.27, 66.92],
    "Dividend from subsidiaries/associates": [N, N, 48.54, 6.01],
    "Profit on sale of current investments": [N, N, 43.12, 92.83],
    "Profit on sale of PPE":               [N, N, 20.44, 43.15],
    "FVTPL gain":                          [N, N, 29.96, 26.61],
    "Others (note 3.8)":                   [N, N, 67.92, 79.65],
}

# Revenue mix - note 2.1 / 3.7.1 'Disaggregated revenue information' (FY2023-24 AR for
# FY2023-24, FY2024-25 AR for FY2025, FY2025-26 AR for FY2026). Feeds the Step 12 Revenue Model.
REV_MIX = {
    "Commercial vehicles":             [31646.05, 32714.70, 32383.69, 36842.91],
    "Engines and gensets":             [633.84, 1006.55, 1190.17, 1414.29],
    "Ferrous castings and patterns":   [609.33, 508.77, 572.24, 602.41],
    "Spare parts and others":          [2577.88, 3469.41, 3977.90, 4450.37],
    "Sale of services":                [1106.88, 1209.86, 1264.42, 1257.11],
    "Scrap sales":                     [108.56, 114.04, 96.80, 110.63],
    "Other operating revenue - others": [11.11, 15.68, 23.00, 53.54],
    "Rebates and discounts":           [597.05, 715.52, 805.57, 794.91],
    # Outside 'revenue from contracts with customers': export incentives (47.10 / 43.54 /
    # 50.09 / 70.68) plus FY2023 grant income 0.44.
    "Export incentives and grant income": [47.54, 43.54, 50.09, 70.68],
}
REV_PRINTED = {
    "Sale of products subtotal":       [35467.10, 37699.43, 38124.00, 43309.98],
    "Revenue from contracts with customers": [36096.60, 38323.49, 38702.65, 43936.35],
}
REV_GEO = {
    "India":                           [34230.04, 36608.91, 36571.31, 40846.22],
    "Outside India":                   [1866.56, 1714.58, 2131.34, 3090.13],
}

# FY2026 standalone borrowings by instrument - repayment schedule in the borrowings note
# (FY2025-26 AR: term loans TL-1..TL-18 total row; NCD Series 3; sales-tax 'Programme II') and
# note 1.21 (short-term bank loans). Earlier years not decomposed. Feeds the Debt Breakup tab.
SA_DEBT_FY26 = {
    "Term loans - non-current":            [N, N, N, 456.38],
    "Term loans - current maturities":     [N, N, N, 279.25],
    "NCD Series 3 7.30% AL 2027 - current": [N, N, N, 200.00],
    "Sales-tax loans (interest-free) - non-current": [N, N, N, 61.50],
    "Sales-tax loans (interest-free) - current": [N, N, N, 4.91],
    "Short-term loans from banks (unsecured)": [N, N, N, 150.00],
    # printed check figures
    "Long-term borrowings incl. current maturities (Board's report)": [N, N, N, 1002.04],
    "Current maturities of long-term debts (note 1.21)": [N, N, N, 483.82],
}

# =========================================================================================
# 2. STANDALONE - balance sheet (FY2023-24 AR p115; FY2024-25 AR p111; FY2025-26 AR p121)
# =========================================================================================
SA_NCA = {
    "Property, plant and equipment":   [4747.85, 4502.22, 4406.64, 5072.10],
    "Capital work-in-progress":        [48.95, 95.53, 276.87, 209.98],
    "Right-of-use asset":              [236.98, 235.30, 275.33, 263.04],
    "Goodwill":                        [449.90, 449.90, 449.90, 449.90],
    "Other intangible assets":         [869.42, 764.38, 713.62, 603.83],
    "Intangibles under development":   [83.57, 106.00, 147.89, 269.31],
    "Non-current investments":         [3892.18, 5310.71, 5654.26, 6559.29],
    "Non-current trade receivables":   [0.63, 0.25, 0.00, 0.00],
    "Other non-current financial assets": [97.30, 64.94, 575.01, 128.40],
    "Income tax assets":               [133.91, 50.34, 34.32, 14.53],
    "Other non-current assets":        [327.32, 369.09, 659.69, 361.29],
}
SA_CA = {
    "Inventories":                     [2774.48, 3190.69, 2957.32, 3486.02],
    "Current investments":             [2771.42, 249.06, 3018.70, 4119.71],
    "Trade receivables":               [4062.08, 3569.65, 2887.32, 2950.41],
    "Cash and cash equivalents":       [454.11, 1941.87, 2659.82, 2031.09],
    "Other bank balances":             [47.18, 1496.31, 46.13, 945.96],
    "Current loans":                   [0.00, 95.00, 0.00, 0.00],
    "Other current financial assets":  [581.44, 241.80, 118.21, 242.94],
    "Other current assets":            [940.99, 812.69, 621.12, 885.86],
}
SA_HFS_ASSETS = {"Assets held for sale": [71.92, 66.02, 23.68, 0.00]}

SA_EQUITY = {
    "Equity share capital":            [293.61, 293.63, 293.65, 587.39],
    "Other equity":                    [8132.19, 8516.74, 11225.14, 12526.03],
}
SA_NCL = {
    "Non-current borrowings":          [1766.23, 1131.64, 902.23, 517.88],
    "Non-current lease liabilities":   [31.02, 29.40, 31.74, 29.60],
    "Other non-current financial liabilities": [23.01, 21.31, 12.57, 10.99],
    "Non-current contract liabilities": [250.04, 283.45, 372.86, 423.97],
    "Non-current provisions":          [519.22, 724.07, 708.97, 635.45],
    "Deferred tax liability (net)":    [503.51, 556.31, 547.89, 535.71],
}
SA_CL = {
    "Current borrowings":              [1413.87, 1122.89, 533.21, 633.82],
    "Current lease liabilities":       [13.71, 15.47, 14.54, 13.74],
    "Trade payables - MSE":            [73.75, 79.54, 56.58, 231.08],
    "Trade payables - others":         [7101.37, 6225.65, 7248.11, 8098.18],
    "Other current financial liabilities": [939.48, 2463.77, 1211.22, 1365.79],
    "Current contract liabilities":    [362.83, 476.02, 422.85, 674.11],
    "Current provisions":              [519.32, 650.68, 825.15, 1350.34],
    "Other current liabilities":       [514.13, 478.11, 492.78, 219.02],
    "Current tax liabilities":         [123.47, 526.24, 621.69, 740.56],
}
SA_HFS_LIAB = {"Liabilities held for sale": [10.87, 16.83, 4.65, 0.00]}

SA_BS_PRINTED = {
    "Total non-current assets":        [10888.01, 11948.66, 13193.53, 13931.67],
    "Total current assets":            [11631.70, 11597.07, 12308.62, 14661.99],
    "Total assets":                    [22591.63, 23611.75, 25525.83, 28593.66],
    "Total equity":                    [8425.80, 8810.37, 11518.79, 13113.42],
    "Total non-current liabilities":   [3093.03, 2746.18, 2576.26, 2153.60],
    "Total current liabilities":       [11061.93, 12038.37, 11426.13, 13326.64],
}

# Earmarked / non-liquid items inside liquidity captions (pre-flight probe [0e]).
# Note 1.11B each year: unclaimed-dividend + escrow accounts are earmarked; FY2024 also held
# Rs 1,453.48 crore in a designated account for an interim dividend already declared (the
# matching payable sits in other current financial liabilities). FY2026's Rs 900 crore of
# 3-12 month deposits "includes fixed deposit of Rs. 100 crores (2024-25: Nil) ... towards
# meeting Debenture Redemption Fund requirements" (note 1.11B footnote #) - that Rs 100 crore is
# usable only for the NCD maturing 17-Mar-2027 (ICRA_CONVENTIONS s3 fn 2 / s8), so it is NOT
# free liquidity; the other Rs 800 crore is. FY2024 current investments include Rs 23.90 crore
# of subsidiary preference shares (redeemed FY2025, standalone cash flow) - not liquid.
SA_EARMARKED = {
    "Unclaimed dividend accounts":     [10.30, 10.22, 13.52, 13.35],
    "Escrow account":                  [36.88, 32.61, 32.61, 32.61],
    "Interim dividend account":        [0.00, 1453.48, 0.00, 0.00],
    "Debenture redemption fund deposit": [0.00, 0.00, 0.00, 100.00],
    "Non-liquid current investments":  [0.00, 23.90, 0.00, 0.00],
}
FREE_BANK_DEPOSITS = {"3-12 month deposits (free)": [0.00, 0.00, 0.00, 800.00]}

# The AR's own net-debt reconciliation (standalone note 1.21 / 1.16 'Net debt
# reconciliation'; FY2023-24 AR for FY2023-24, FY2025-26 AR for FY2025-26). Positive = surplus.
AR_NET_DEBT_BRIDGE = {
    "Cash":                            [454.11, 1941.87, 2659.82, 2031.09],
    "Liquid investments":              [2771.42, 225.16, 3018.70, 4119.71],
    "Current borrowings (bridge)":     [269.65, 484.87, 150.87, 150.78],
    "Non-current borrowings (bridge)": [2961.17, 1777.16, 1289.57, 1003.93],
    "Derivative asset/(liability)":    [97.41, 51.99, 12.19, -16.10],
    "Lease liabilities (bridge)":      [44.73, 44.87, 46.28, 43.34],
    "Net surplus (printed)":           [47.39, -87.88, 4203.99, 4936.65],
    # Movements printed in the bridge for the year (FY2023-24 AR bridge for FY2023-24).
    "Interest paid - non-current":     [226.40, 200.20, 115.66, 83.29],
    "Interest paid - current":         [33.39, 45.91, 33.40, 10.35],
    "Non-current borrowings net cash flow": [375.94, 1104.98, 441.73, 276.60],
}

# Company-published headline figures (chairman's letters / press releases) - cross-checks.
AR_PUBLISHED = {
    # EBITDA: FY2024 AR chairman "EBITDA ... Rs 4,607 Cr"; FY2025 AR "Rs 4,931 crores";
    # FY2026 AR "Rs 5,732 crores at a margin of 13.0%". Rounded to the crore.
    "EBITDA":                          [N, 4607.0, 4931.0, 5732.0],
    # Net cash: FY2025 AR "net cash position of Rs 4,242 crores ... from a net debt of Rs 89
    # crores the previous year"; FY2026 AR "Net cash ... Rs 5,899 crores".
    "Net cash":                        [N, -89.0, 4242.0, 5899.0],
}

# =========================================================================================
# 3. STANDALONE - cash flow (same pages + 1)
# =========================================================================================
SA_CF = {
    "Cash from operations (pre-tax)":  [2536.22, 3127.65, 8760.15, 5880.36],
    "Income tax paid":                 [400.21, 624.53, 940.73, 1088.26],
    "Net cash from operating activities": [2136.01, 2503.12, 7819.42, 4792.10],
    "Capex (purchase of PPE & intangibles)": [502.05, 495.50, 954.29, 1049.53],
    "Repayment of non-current borrowings": [375.94, 1104.98, 688.73, 379.60],
    "Proceeds from non-current borrowings": [0.00, 0.00, 247.00, 103.00],
    "Interest paid":                   [259.79, 246.11, 149.06, 93.64],
    "Dividend paid":                   [293.55, 763.39, 2040.77, 1835.42],
    # Equity put into subsidiaries/JVs: FY2024 board report (Optare 1,200; OHM 299.99; TVS
    # Trucks JV 24.95; others) and cash flow 'purchase of non-current investments' 1,567.02;
    # FY2025 cash flow 218.30 + 'investment in subsidiary pending allotment' 498.76 (Optare);
    # FY2026 cash flow 386.28.
    "Investment in subsidiaries/JVs":  [19.81, 1567.02, 717.06, 386.28],
}

# =========================================================================================
# 4. CONSOLIDATED (reported, includes the financial-services subsidiaries)
#    FY2023: FY2023-24 AR p210-211 (as originally presented); FY2024: FY2024-25 AR p208-209
#    comparatives (as RESTATED - see DISCLOSED_DIFFERENCES); FY2025/26: FY2025-26 AR p220-221
# =========================================================================================
CONS_PL = {
    "Revenue incl. financing income":  [41672.60, 45703.34, 48535.14, 56362.08],
    "Other income":                    [107.11, 227.88, 358.46, 584.82],
    "Finance costs":                   [2093.50, 2982.25, 3930.21, 4704.65],
    "Depreciation and amortisation":   [900.22, 927.29, 1086.65, 1137.56],
    "PBT before JV share & exceptional": [2206.29, 4173.91, 4549.35, 5487.61],
    "Share of JV/associates":          [10.75, 16.38, 31.58, 51.62],
    "Exceptional items":               [47.89, -84.22, 15.40, -384.44],
    "PBT":                             [2264.93, 4106.07, 4596.33, 5154.79],
    "Tax expense":                     [906.11, 1409.73, 1213.54, 1433.81],
    "PAT":                             [1358.82, 2696.34, 3382.79, 3720.98],
}
# Consolidated cash flow: D&A split (FY2023-24 AR p212 for FY2023-24; FY2025-26 AR p222).
CONS_DA_CF = {
    "D&A excl. right-of-use":          [839.20, 865.42, 1006.68, 1060.58],
    "Right-of-use depreciation":       [61.02, 61.87, 79.97, 76.98],
}
CONS_BS = {
    "Total assets":                    [54746.01, 67660.46, 81714.64, 101040.74],
    "Total equity (incl. NCI)":        [10795.81, 11814.59, 15844.86, 18546.24],
    "Non-current borrowings":          [19502.86, 26695.71, 36382.92, 46016.36],
    "Current borrowings":              [11417.58, 13868.63, 13318.18, 17633.44],
    "Lease liabilities (NC + current)": [240.49, 237.84, 261.01, 285.90],
}
CONS_LEASE = {
    "Non-current lease liabilities":   [188.97, 151.21, 185.40, 202.37],
    "Current lease liabilities":       [51.52, 86.63, 75.61, 83.53],
}
# Consolidated note 1.20 (non-current borrowings) line items - each AR's own table.
CONS_NC_COMPONENTS = {
    "Secured NCDs":                    [278.80, 627.43, 1457.24, 1372.11],
    "Term loans from banks":           [17822.25, 24800.19, 31646.70, 40116.05],
    "SIPCOT soft loan":                [31.18, 31.18, 0.00, 0.00],
    "Subordinated NCDs incl. perpetual": [843.43, 1113.10, 3212.57, 4417.12],
    "Unsecured unsubordinated NCDs":   [0.00, 0.00, 0.00, 49.58],
    "External commercial borrowings":  [385.86, 55.97, 0.00, 0.00],
    "Interest-free sales tax loans":   [66.41, 66.41, 66.41, 61.50],
    "Others incl. subordinated loans": [74.93, 1.43, 0.00, 0.00],
}
# Consolidated note 1.26 (current borrowings). FY2023 not decomposed (one line not captured).
CONS_CB_COMPONENTS = {
    "Secured loans from banks":        [N, 2106.74, 1306.19, 857.90],
    "Bills discounted":                [N, 84.31, 0.00, 0.00],
    "Unsecured loans from banks":      [N, 233.41, 278.19, 244.83],
    "Commercial papers":               [N, 1479.08, 98.73, 96.94],
    "Loans from others":               [N, 1.84, 1.55, 0.00],
    "Subordinated NCDs (current)":     [N, 549.59, 0.00, 0.00],
    "Supplier finance liabilities":    [N, 0.00, 0.00, 87.25],
    "Current maturities of LT debt":   [N, 9413.66, 11633.52, 16346.52],
}

# Borrowings relating to financing activities (consolidated notes 1.20 note 8 and 1.26 note 2)
# FY2023: FY2023-24 AR; FY2024: FY2023-24 AR & FY2024-25 AR (agree); FY2025-26: FY2025-26 AR.
FS_DEBT = {
    "FS non-current borrowings":       [16960.42, 25204.93, 34006.51, 43119.02],
    "FS current borrowings":           [8900.03, 11497.38, 11840.16, 15840.45],
}
FS_NC_COMPONENTS = {
    "FS secured NCDs":                 [79.77, 428.10, 1257.90, 1372.11],
    "FS term loans from banks":        [16037.22, 23663.73, 29536.04, 37280.21],
    "FS subordinated NCDs":            [843.43, 1113.10, 3212.57, 3686.16],
    "FS perpetual debt instrument":    [0.00, 0.00, 0.00, 730.96],
    "FS unsecured unsubordinated NCDs": [0.00, 0.00, 0.00, 49.58],
}
FS_CB_COMPONENTS = {
    "FS secured loans from banks":     [848.10, 701.51, 671.40, 73.32],
    "FS current maturities (incl. current sub NCDs)": [7855.51, 9316.79, 11070.03, 15670.19],
    "FS commercial papers":            [196.42, 1479.08, 98.73, 96.94],
}

# Segment note 3.8 (consolidated): FY2023 from FY2023-24 AR (original); FY2024 restated in the
# FY2024-25 AR; FY2025-26 from FY2025-26 AR.
SEG = {
    "CV revenue":                      [38024.72, 40956.35, 42333.28, 48313.71],
    "FS revenue":                      [3649.54, 4749.66, 6202.98, 8049.34],
    "Inter-segment revenue":           [1.66, 2.67, 1.12, 0.97],
    "FS interest & borrowing costs":   [N, 2555.40, 3532.90, 4278.54],
    "CV segment result (PBIT)":        [1819.40, 3614.68, 3688.97, 4379.32],
    "FS segment result":               [656.52, 758.20, 899.23, 949.58],
    "Interest expense (non-FS)":       [376.74, 426.85, 397.31, 426.11],
    "CV segment assets":               [22416.28, 22505.58, 25088.57, 28862.65],
    "CV segment liabilities":          [17129.31, 17787.37, 18119.28, 20970.02],
    "FS segment assets":               [32329.73, 45154.88, 56626.07, 72178.09],
    "FS segment liabilities":          [26820.89, 38058.50, 47750.50, 61524.48],
}

# =========================================================================================
# 5. OPERATING AND SUPPORT DATA (company documents)
# =========================================================================================
OPS = {
    # Ten-year table 'A historical perspective' (FY2025-26 AR p6): total vehicles.
    "Total vehicle volume":            [192205, 194555, 195097, 220437],
    # MD&A domestic sales: FY2024 AR p? 'sold 1,16,069 M&HCVs'; FY2025 AR '114,793'; FY2026
    # AR '128,033'. LCV: 66,633 / 65,049 / 74,322. Exports: chairman letters 11,853 / 15,255 /
    # 18,082. FY2023 split not extracted.
    "Domestic M&HCV volume":           [N, 116069, 114793, 128033],
    "Domestic LCV volume":             [N, 66633, 65049, 74322],
    "Export volume":                   [N, 11853, 15255, 18082],
    # M&HCV (bus + truck) domestic market share, %: FY2024 AR MD&A '31.1% ... (31.8%)';
    # FY2025 AR '30.7%'; FY2026 AR MD&A '30.3%' (the FY2026 chairman's letter says 30.8% -
    # divergence recorded in DISCLOSED_DIFFERENCES; the MD&A series is used).
    "M&HCV market share %":            [31.8, 31.1, 30.7, 30.3],
    # Corporate guarantees to banks for subsidiaries/JV loans (standalone note 3.9.2).
    "Corporate guarantees for subsidiaries": [892.72, 762.16, 1021.58, 785.71],
}

# Second sources for the support and operating series.
BOARD_REPORT_INVESTMENTS = {
    # Board's report 'Subsidiaries, associates and joint ventures', sum of named investments:
    # FY2024: 1,200 + 299.99 + 24.95 + 4 + 15 + 20.37 + 3.40; FY2025: 200 + 10 + 5.09 + 3.20 +
    # 498.76; FY2026: 370.58 + 5.70 + 10.
    "Investments named in board report": [N, 1567.71, 717.05, 386.28],
}
SECOND_SOURCE = {
    # FY2024-25 AR ten-year table repeats FY2023-FY2025 vehicle volumes.
    "Vehicle volume, FY2024-25 AR table": [192205, 194555, 195097, N],
    # Guarantee figure repeated as the comparative in the next year's AR.
    "Guarantees, next AR comparative":  [N, 762.16, 1021.58, N],
    # M&HCV share change as each AR states it (pp): FY2024 AR 'lower by 0.7%'; FY2025 AR
    # 'slight decrease of 0.3%'; FY2026 AR 'decline of 0.4 percentage points'.
    "Stated change in M&HCV share (pp)": [N, -0.7, -0.3, -0.4],
}


# =========================================================================================
# helpers
# =========================================================================================
def v(table, key, p):
    return table[key][IX[p]]


def tot(table, p):
    return sum(x[IX[p]] for x in table.values() if x[IX[p]] is not None)


def prev(p):
    i = IX[p]
    return YEARS[i - 1] if i > 0 else None


def sa_cogs(p):
    return (v(SA_PL, "Cost of materials consumed", p) + v(SA_PL, "Purchases of stock-in-trade", p)
            + v(SA_PL, "Change in inventories", p))


def sa_total_expenses(p):
    return (sa_cogs(p) + v(SA_PL, "Employee benefits expense", p) + v(SA_PL, "Finance costs", p)
            + v(SA_PL, "Depreciation and amortisation", p) + v(SA_PL, "Other expenses", p))


def sa_pbt_pre(p):
    return v(SA_PL, "Revenue from operations", p) + v(SA_PL, "Other income", p) - sa_total_expenses(p)


def sa_pbt(p):
    return sa_pbt_pre(p) + v(SA_PL, "Exceptional items", p)


def sa_pat(p):
    return sa_pbt(p) - v(SA_PL, "Tax expense", p)


def sa_opbdita(p):
    """ICRA OPBDITA: revenue from operations less operating costs; ALL other income excluded."""
    return (v(SA_PL, "Revenue from operations", p) - sa_cogs(p)
            - v(SA_PL, "Employee benefits expense", p) - v(SA_PL, "Other expenses", p))


def sa_debt(p):
    """ICRA total debt: borrowings + lease liabilities."""
    return (v(SA_NCL, "Non-current borrowings", p) + v(SA_CL, "Current borrowings", p)
            + v(SA_NCL, "Non-current lease liabilities", p) + v(SA_CL, "Current lease liabilities", p))


def sa_borrowings(p):
    return v(SA_NCL, "Non-current borrowings", p) + v(SA_CL, "Current borrowings", p)


def sa_equity(p):
    return tot(SA_EQUITY, p)


def sa_total_assets(p):
    return tot(SA_NCA, p) + tot(SA_CA, p) + tot(SA_HFS_ASSETS, p)


def sa_total_liabilities(p):
    return tot(SA_NCL, p) + tot(SA_CL, p) + tot(SA_HFS_LIAB, p)


def sa_earmarked_bank(p):
    """Every earmarked balance inside note 1.11B 'other bank balances'."""
    return (v(SA_EARMARKED, "Unclaimed dividend accounts", p) + v(SA_EARMARKED, "Escrow account", p)
            + v(SA_EARMARKED, "Interim dividend account", p)
            + v(SA_EARMARKED, "Debenture redemption fund deposit", p))


def sa_free_liquidity(p):
    """Unencumbered cash + free bank deposits + liquid current investments."""
    return (v(SA_CA, "Cash and cash equivalents", p)
            + v(SA_CA, "Other bank balances", p) - sa_earmarked_bank(p)
            + v(SA_CA, "Current investments", p) - v(SA_EARMARKED, "Non-liquid current investments", p))


def sa_liquid_investments(p):
    return v(SA_CA, "Current investments", p) - v(SA_EARMARKED, "Non-liquid current investments", p)


def sa_capital_employed(p):
    return (sa_debt(p) + sa_equity(p) + v(SA_NCL, "Deferred tax liability (net)", p)
            - v(SA_NCA, "Capital work-in-progress", p))


def auto_debt(p):
    """Consolidated borrowings less borrowings relating to financing activities, plus all
    consolidated lease liabilities (the FS share of leases is not disclosed - conservative)."""
    return (v(CONS_BS, "Non-current borrowings", p) + v(CONS_BS, "Current borrowings", p)
            - v(FS_DEBT, "FS non-current borrowings", p) - v(FS_DEBT, "FS current borrowings", p)
            + v(CONS_BS, "Lease liabilities (NC + current)", p))


def auto_borrowings_ex_lease(p):
    return auto_debt(p) - v(CONS_BS, "Lease liabilities (NC + current)", p)


def nonfs_subsidiary_debt(p):
    """Borrowings of the NON-financial subsidiaries = automotive borrowings - AL standalone."""
    return auto_borrowings_ex_lease(p) - sa_borrowings(p)


def cons_debt(p):
    return (v(CONS_BS, "Non-current borrowings", p) + v(CONS_BS, "Current borrowings", p)
            + v(CONS_BS, "Lease liabilities (NC + current)", p))


def cons_opbdita(p):
    return (v(CONS_PL, "PBT before JV share & exceptional", p) + v(CONS_PL, "Finance costs", p)
            + v(CONS_PL, "Depreciation and amortisation", p) - v(CONS_PL, "Other income", p))


def compute():
    R = {}
    for p in YEARS:
        oi = v(SA_PL, "Revenue from operations", p)
        op = sa_opbdita(p)
        da = v(SA_PL, "Depreciation and amortisation", p)
        fc = v(SA_PL, "Finance costs", p)
        pat = sa_pat(p)
        td = sa_debt(p)
        tnw = sa_equity(p)
        tol = sa_total_liabilities(p)
        liq = sa_free_liquidity(p)
        cogs = sa_cogs(p)
        payables = v(SA_CL, "Trade payables - MSE", p) + v(SA_CL, "Trade payables - others", p)
        repay = v(SA_CF, "Repayment of non-current borrowings", p)
        pb = prev(p)
        r = {
            # ---- standalone (primary)
            "Operating income": oi,
            "OPBDITA": op,
            "OPBDITA margin (%)": 100 * op / oi,
            "PBIT (operating)": op - da,
            "PBIT margin (%)": 100 * (op - da) / oi,
            "PAT": pat,
            "PAT margin (%)": 100 * pat / oi,
            "PAT before exceptional (tax-adjusted at book)": pat - v(SA_PL, "Exceptional items", p),
            "Total debt": td,
            "Tangible net worth": tnw,
            "Total outside liabilities": tol,
            "Gearing (x)": td / tnw,
            "TOL/TNW (x)": tol / tnw,
            "Total debt/OPBDITA (x)": td / op,
            "Interest coverage (x)": op / fc,
            "DSCR (x)": (pat + fc + da) / (fc + repay),
            "NCA (PAT + D&A - dividend)": pat + da - v(SA_CF, "Dividend paid", p),
            "Free cash and liquid investments": liq,
            "Net debt (negative = net cash)": td - liq,
            "Net debt/OPBDITA (x)": (td - liq) / op,
            "Current ratio (x)": tot(SA_CA, p) / tot(SA_CL, p),
            "Debtor days": 365 * v(SA_CA, "Trade receivables", p) / oi,
            "Inventory days": 365 * v(SA_CA, "Inventories", p) / cogs,
            "Payable days": 365 * payables / cogs,
            "CFO": v(SA_CF, "Net cash from operating activities", p),
            "RCF (CFO - dividend)": v(SA_CF, "Net cash from operating activities", p) - v(SA_CF, "Dividend paid", p),
            "FCF (RCF - capex - repayments)": (v(SA_CF, "Net cash from operating activities", p)
                                               - v(SA_CF, "Dividend paid", p)
                                               - v(SA_CF, "Capex (purchase of PPE & intangibles)", p) - repay),
            "Capex/OI (%)": 100 * v(SA_CF, "Capex (purchase of PPE & intangibles)", p) / oi,
            "Support to subsidiaries (equity)": v(SA_CF, "Investment in subsidiaries/JVs", p),
            # ---- automotive business = consolidated excl. financial services (adjustment layer)
            "AUTO CV revenue": v(SEG, "CV revenue", p),
            "AUTO CV PBIT margin (%)": 100 * v(SEG, "CV segment result (PBIT)", p) / v(SEG, "CV revenue", p),
            "AUTO total debt": auto_debt(p),
            "AUTO non-FS subsidiary borrowings": nonfs_subsidiary_debt(p),
            "AUTO OPBDITA low (CV PBIT + standalone D&A)": v(SEG, "CV segment result (PBIT)", p) + da,
            "AUTO OPBDITA high (CV PBIT + consolidated D&A)": (v(SEG, "CV segment result (PBIT)", p)
                                                               + v(CONS_PL, "Depreciation and amortisation", p)),
            "AUTO debt/OPBDITA at low bound (x)": auto_debt(p) / (v(SEG, "CV segment result (PBIT)", p) + da),
            "AUTO interest coverage at low bound (x)": ((v(SEG, "CV segment result (PBIT)", p) + da)
                                                        / v(SEG, "Interest expense (non-FS)", p)),
            "AUTO net assets (CV segment)": v(SEG, "CV segment assets", p) - v(SEG, "CV segment liabilities", p),
            "AUTO gearing on CV net assets (x)": auto_debt(p) / (v(SEG, "CV segment assets", p)
                                                                 - v(SEG, "CV segment liabilities", p)),
            "ADJ standalone debt + non-FS subsidiary debt / standalone OPBDITA (x)":
                (td + nonfs_subsidiary_debt(p)) / op,
            "ADJ net debt incl. non-FS subsidiary debt (negative = net cash)":
                td + nonfs_subsidiary_debt(p) - liq,
            # ---- reported consolidated (supplementary only)
            "CONS operating income": v(CONS_PL, "Revenue incl. financing income", p),
            "CONS PAT": v(CONS_PL, "PAT", p),
            "CONS total debt": cons_debt(p),
            "CONS TNW (incl. NCI)": v(CONS_BS, "Total equity (incl. NCI)", p),
            "CONS TOL/TNW (x)": ((v(CONS_BS, "Total assets", p) - v(CONS_BS, "Total equity (incl. NCI)", p))
                                 / v(CONS_BS, "Total equity (incl. NCI)", p)),
            "CONS total debt/OPBDITA (x)": cons_debt(p) / cons_opbdita(p),
            "CONS FS share of group borrowings (%)": 100 * (v(FS_DEBT, "FS non-current borrowings", p)
                                                           + v(FS_DEBT, "FS current borrowings", p))
                                                    / (v(CONS_BS, "Non-current borrowings", p)
                                                       + v(CONS_BS, "Current borrowings", p)),
            # ---- operations
            "Total vehicle volume": v(OPS, "Total vehicle volume", p),
            "M&HCV market share (%)": v(OPS, "M&HCV market share %", p),
            "Corporate guarantees for subsidiaries": v(OPS, "Corporate guarantees for subsidiaries", p),
        }
        if pb is not None:
            ce_avg = (sa_capital_employed(p) + sa_capital_employed(pb)) / 2
            r["RoCE (%)"] = 100 * (op - da) / ce_avg
            r["Revenue growth (%)"] = 100 * (oi / v(SA_PL, "Revenue from operations", pb) - 1)
        else:
            r["RoCE (%)"] = None
            r["Revenue growth (%)"] = None
        R[p] = r
    return R


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source). Each 'disclosed' figure is a
    number the AR PRINTS, independent of the line items the computation is built from."""
    if R is None:
        R = compute()
    T = []
    d = lambda k: v(SA_DEBT_FY26, k, "FY2026")  # noqa: E731
    T += [
        ("FY2026 non-current borrowings = term loans NC + sales-tax loans NC",
         d("Term loans - non-current") + d("Sales-tax loans (interest-free) - non-current"),
         v(SA_NCL, "Non-current borrowings", "FY2026"), 0.01, "borrowings repayment schedule vs balance sheet"),
        ("FY2026 current maturities = term loans + NCD + sales-tax loans (current)",
         d("Term loans - current maturities") + d("NCD Series 3 7.30% AL 2027 - current")
         + d("Sales-tax loans (interest-free) - current"),
         d("Current maturities of long-term debts (note 1.21)"), 0.5,
         "schedule is at face value; note 1.21 at amortised cost (EIR residual 0.34)"),
        ("FY2026 current borrowings = short-term bank loans + current maturities",
         d("Short-term loans from banks (unsecured)") + d("Current maturities of long-term debts (note 1.21)"),
         v(SA_CL, "Current borrowings", "FY2026"), 0.01, "note 1.21"),
        ("FY2026 long-term borrowings (Board's report) = term loans + NCD + sales-tax loans",
         d("Term loans - non-current") + d("Term loans - current maturities")
         + d("NCD Series 3 7.30% AL 2027 - current") + d("Sales-tax loans (interest-free) - non-current")
         + d("Sales-tax loans (interest-free) - current"),
         d("Long-term borrowings incl. current maturities (Board's report)"), 0.01,
         "Board's report: 'long term borrowings stood at Rs 1,002.04 crores'"),
    ]
    for p in YEARS:
        prods = sum(v(REV_MIX, k, p) for k in ("Commercial vehicles", "Engines and gensets",
                                                "Ferrous castings and patterns", "Spare parts and others"))
        rcc = (prods + v(REV_MIX, "Sale of services", p) + v(REV_MIX, "Scrap sales", p)
               + v(REV_MIX, "Other operating revenue - others", p) - v(REV_MIX, "Rebates and discounts", p))
        T += [
            ("Revenue mix: product lines = sale-of-products subtotal, %s" % p, prods,
             v(REV_PRINTED, "Sale of products subtotal", p), 0.01, "note 2.1 / 3.7.1"),
            ("Revenue mix: products + services + other - rebates = contract revenue, %s" % p, rcc,
             v(REV_PRINTED, "Revenue from contracts with customers", p), 0.01, "note 3.7.1"),
            ("Revenue mix: India + outside India = contract revenue, %s" % p, tot(REV_GEO, p),
             v(REV_PRINTED, "Revenue from contracts with customers", p), 0.01, "note 3.7.1 geography"),
            ("Revenue mix: contract revenue + export incentives/grant = revenue from operations, %s" % p,
             v(REV_PRINTED, "Revenue from contracts with customers", p)
             + v(REV_MIX, "Export incentives and grant income", p),
             v(SA_PL, "Revenue from operations", p), 0.01, "note 2.1 vs P&L"),
            ("SA total income = revenue + other income, %s" % p,
             v(SA_PL, "Revenue from operations", p) + v(SA_PL, "Other income", p),
             v(SA_PL_PRINTED, "Total income", p), 0.01, "standalone P&L, Total Income row"),
            ("SA cost of goods sold = materials + purchases + inventory change, %s" % p,
             sa_cogs(p), v(SA_PL_PRINTED, "Cost of goods sold subtotal", p), 0.01,
             "standalone P&L, printed subtotal"),
            ("SA total expenses (sum of lines), %s" % p, sa_total_expenses(p),
             v(SA_PL_PRINTED, "Total expenses", p), 0.01, "standalone P&L, Total Expenses row"),
            ("SA profit before exceptional & tax, %s" % p, sa_pbt_pre(p),
             v(SA_PL_PRINTED, "Profit before exceptional & tax", p), 0.01, "standalone P&L"),
            ("SA profit before tax, %s" % p, sa_pbt(p),
             v(SA_PL_PRINTED, "Profit before tax", p), 0.01, "standalone P&L"),
            ("SA profit after tax, %s" % p, sa_pat(p),
             v(SA_PL_PRINTED, "Profit for the year", p), 0.01, "standalone P&L"),
            ("SA non-current assets (sum of lines), %s" % p, tot(SA_NCA, p),
             v(SA_BS_PRINTED, "Total non-current assets", p), 0.02, "standalone balance sheet"),
            ("SA current assets (sum of lines), %s" % p, tot(SA_CA, p),
             v(SA_BS_PRINTED, "Total current assets", p), 0.02, "standalone balance sheet"),
            ("SA total assets, %s" % p, sa_total_assets(p),
             v(SA_BS_PRINTED, "Total assets", p), 0.02, "standalone balance sheet"),
            ("SA total equity = share capital + other equity, %s" % p, sa_equity(p),
             v(SA_BS_PRINTED, "Total equity", p), 0.01, "standalone balance sheet"),
            ("SA non-current liabilities (sum of lines), %s" % p, tot(SA_NCL, p),
             v(SA_BS_PRINTED, "Total non-current liabilities", p), 0.02, "standalone balance sheet"),
            ("SA current liabilities (sum of lines), %s" % p, tot(SA_CL, p),
             v(SA_BS_PRINTED, "Total current liabilities", p), 0.02, "standalone balance sheet"),
            ("SA balance sheet balances: assets = equity + liabilities, %s" % p, sa_total_assets(p),
             sa_equity(p) + sa_total_liabilities(p), 0.02, "standalone balance sheet"),
            ("SA cash in AR net-debt bridge = balance-sheet cash, %s" % p,
             v(SA_CA, "Cash and cash equivalents", p), v(AR_NET_DEBT_BRIDGE, "Cash", p), 0.01,
             "standalone net debt reconciliation"),
            ("SA liquid investments = AR bridge liquid investments, %s" % p,
             sa_liquid_investments(p), v(AR_NET_DEBT_BRIDGE, "Liquid investments", p), 0.01,
             "standalone net debt reconciliation (FY2024 differs from the balance sheet by "
             "Rs 23.90 crore of subsidiary preference shares - removed as non-liquid)"),
            ("CONS segment results bridge to reported PBT, %s" % p,
             v(SEG, "CV segment result (PBIT)", p) + v(SEG, "FS segment result", p)
             - v(SEG, "Interest expense (non-FS)", p) + v(CONS_PL, "Other income", p)
             + v(CONS_PL, "Share of JV/associates", p) + v(CONS_PL, "Exceptional items", p),
             v(CONS_PL, "PBT", p), 0.02, "consolidated segment note 3.8 vs consolidated P&L"),
            ("CONS segment assets sum to total assets, %s" % p,
             v(SEG, "CV segment assets", p) + v(SEG, "FS segment assets", p),
             v(CONS_BS, "Total assets", p), 0.02, "segment note vs consolidated balance sheet"),
            ("CONS segment net assets = total equity, %s" % p,
             (v(SEG, "CV segment assets", p) - v(SEG, "CV segment liabilities", p)
              + v(SEG, "FS segment assets", p) - v(SEG, "FS segment liabilities", p)),
             v(CONS_BS, "Total equity (incl. NCI)", p), 0.02, "segment note vs balance sheet"),
            ("CONS PBT = pre-JV PBT + JV share + exceptional, %s" % p,
             v(CONS_PL, "PBT before JV share & exceptional", p) + v(CONS_PL, "Share of JV/associates", p)
             + v(CONS_PL, "Exceptional items", p), v(CONS_PL, "PBT", p), 0.02, "consolidated P&L"),
        ]
    for p in ("FY2024", "FY2025", "FY2026"):
        T.append(("SA OPBDITA vs company-published EBITDA, %s" % p, sa_opbdita(p),
                  v(AR_PUBLISHED, "EBITDA", p), 0.6,
                  "chairman's letter, EBITDA (rounded to the crore)"))
        T.append(("Domestic M&HCV + domestic LCV + exports = total vehicles, %s" % p,
                  v(OPS, "Domestic M&HCV volume", p) + v(OPS, "Domestic LCV volume", p)
                  + v(OPS, "Export volume", p), v(OPS, "Total vehicle volume", p), 0.5,
                  "MD&A / chairman volumes vs ten-year historical table"))
    for p in ("FY2025", "FY2026"):
        # Company net cash = borrowings + leases netted against cash + ALL other bank balances
        # (it does not strip the earmarked unclaimed-dividend/escrow/DRF balances) + current
        # investments. Rebuilt from the balance sheet: earmarked added back to free liquidity.
        comp = (sa_free_liquidity(p) + v(SA_EARMARKED, "Unclaimed dividend accounts", p)
                + v(SA_EARMARKED, "Escrow account", p)
                + v(SA_EARMARKED, "Debenture redemption fund deposit", p) - sa_debt(p))
        T.append(("Company net cash rebuilt from the balance sheet, %s" % p, comp,
                  v(AR_PUBLISHED, "Net cash", p), 3.5,
                  "chairman's letter net cash (rounded; residual = effective-interest accruals)"))
    # FY2024 company 'net debt Rs 89 crore' excludes the earmarked dividend account entirely.
    comp24 = sa_free_liquidity("FY2024") + v(SA_EARMARKED, "Unclaimed dividend accounts", "FY2024") \
        + v(SA_EARMARKED, "Escrow account", "FY2024") - sa_debt("FY2024")
    T.append(("Company net debt FY2024 rebuilt from the balance sheet", comp24,
              v(AR_PUBLISHED, "Net cash", "FY2024"), 1.0, "FY2024-25 AR chairman's letter"))
    # Bridge internal arithmetic is the AR's own; tie OUR net surplus on the AR's definition
    # (cash + liquid investments - borrowings - leases; no bank deposits, no derivative):
    for p in YEARS:
        ours = v(SA_CA, "Cash and cash equivalents", p) + sa_liquid_investments(p) - sa_debt(p)
        T.append(("Net surplus on the AR bridge's definition, %s" % p, ours,
                  v(AR_NET_DEBT_BRIDGE, "Net surplus (printed)", p), 60.0,
                  "AR net-debt reconciliation; residual = derivative + EIR/accrued interest "
                  "(bridge carries borrowings gross of EIR) - named in DISCLOSED_DIFFERENCES"))
    for p in YEARS:
        T += [
            ("FS non-current borrowings = its components, %s" % p, tot(FS_NC_COMPONENTS, p),
             v(FS_DEBT, "FS non-current borrowings", p), 0.02, "consolidated note 1.20 note 8"),
            ("FS current borrowings = its components, %s" % p, tot(FS_CB_COMPONENTS, p),
             v(FS_DEBT, "FS current borrowings", p), 0.02, "consolidated note 1.26 note 2"),
            ("CONS non-current borrowings = note 1.20 lines, %s" % p, tot(CONS_NC_COMPONENTS, p),
             v(CONS_BS, "Non-current borrowings", p), 0.02, "consolidated note 1.20"),
            ("CONS lease liabilities = NC + current, %s" % p, tot(CONS_LEASE, p),
             v(CONS_BS, "Lease liabilities (NC + current)", p), 0.02, "consolidated balance sheet"),
            ("CONS revenue = CV + FS - inter-segment, %s" % p,
             v(SEG, "CV revenue", p) + v(SEG, "FS revenue", p) - v(SEG, "Inter-segment revenue", p),
             v(CONS_PL, "Revenue incl. financing income", p), 0.02, "segment note vs P&L"),
            ("CONS PAT = PBT - tax, %s" % p, v(CONS_PL, "PBT", p) - v(CONS_PL, "Tax expense", p),
             v(CONS_PL, "PAT", p), 0.02, "consolidated P&L"),
            ("CONS D&A = cash-flow D&A + ROU depreciation, %s" % p, tot(CONS_DA_CF, p),
             v(CONS_PL, "Depreciation and amortisation", p), 0.02, "consolidated cash flow vs P&L"),
            ("AR bridge arithmetic: net surplus from its own lines, %s" % p,
             (v(AR_NET_DEBT_BRIDGE, "Cash", p) + v(AR_NET_DEBT_BRIDGE, "Liquid investments", p)
              - v(AR_NET_DEBT_BRIDGE, "Current borrowings (bridge)", p)
              - v(AR_NET_DEBT_BRIDGE, "Non-current borrowings (bridge)", p)
              + v(AR_NET_DEBT_BRIDGE, "Derivative asset/(liability)", p)
              - v(AR_NET_DEBT_BRIDGE, "Lease liabilities (bridge)", p)),
             v(AR_NET_DEBT_BRIDGE, "Net surplus (printed)", p), 0.02, "standalone net debt reconciliation"),
            ("SA lease liabilities = AR bridge lease line, %s" % p,
             v(SA_NCL, "Non-current lease liabilities", p) + v(SA_CL, "Current lease liabilities", p),
             v(AR_NET_DEBT_BRIDGE, "Lease liabilities (bridge)", p), 0.02, "balance sheet vs bridge"),
            ("SA borrowings vs AR bridge borrowings (gross of EIR), %s" % p, sa_borrowings(p),
             v(AR_NET_DEBT_BRIDGE, "Current borrowings (bridge)", p)
             + v(AR_NET_DEBT_BRIDGE, "Non-current borrowings (bridge)", p), 55.0,
             "bridge carries borrowings gross of effective-interest adjustments"),
            ("SA other bank balances = earmarked + free deposits, %s" % p,
             sa_earmarked_bank(p) + tot(FREE_BANK_DEPOSITS, p),
             v(SA_CA, "Other bank balances", p), 0.02, "standalone note 1.11B"),
            ("SA CFO = cash from operations - tax paid, %s" % p,
             v(SA_CF, "Cash from operations (pre-tax)", p) - v(SA_CF, "Income tax paid", p),
             v(SA_CF, "Net cash from operating activities", p), 0.02, "standalone cash flow"),
        ]
    for p in ("FY2024", "FY2025", "FY2026"):
        T += [
            ("CONS current borrowings = note 1.26 lines, %s" % p, tot(CONS_CB_COMPONENTS, p),
             v(CONS_BS, "Current borrowings", p), 0.02, "consolidated note 1.26"),
            ("CONS finance costs = FS interest + non-FS interest, %s" % p,
             v(SEG, "FS interest & borrowing costs", p) + v(SEG, "Interest expense (non-FS)", p),
             v(CONS_PL, "Finance costs", p), 0.02, "segment note 'material items' vs P&L"),
            ("Equity into subsidiaries: cash flow vs board report, %s" % p,
             v(SA_CF, "Investment in subsidiaries/JVs", p),
             v(BOARD_REPORT_INVESTMENTS, "Investments named in board report", p), 1.0,
             "standalone cash flow vs board's report"),
        ]
    for p in YEARS:
        T += [
            ("Interest paid: cash flow vs AR bridge, %s" % p, v(SA_CF, "Interest paid", p),
             v(AR_NET_DEBT_BRIDGE, "Interest paid - non-current", p)
             + v(AR_NET_DEBT_BRIDGE, "Interest paid - current", p), 0.02, "net debt reconciliation"),
            ("NC borrowings net flow: repayments - proceeds = bridge, %s" % p,
             v(SA_CF, "Repayment of non-current borrowings", p)
             - v(SA_CF, "Proceeds from non-current borrowings", p),
             v(AR_NET_DEBT_BRIDGE, "Non-current borrowings net cash flow", p), 0.02,
             "net debt reconciliation"),
        ]
    for p in ("FY2025", "FY2026"):
        T += [
            ("SA finance costs = note 2.5 lines, %s" % p, tot(SA_FIN_COST, p),
             v(SA_PL, "Finance costs", p), 0.02, "standalone note 2.5"),
            ("SA other income = note 2.2 lines, %s" % p, tot(SA_OTHER_INCOME, p),
             v(SA_PL, "Other income", p), 0.02, "standalone note 2.2"),
        ]
    for p in ("FY2023", "FY2024", "FY2025"):
        T.append(("Vehicle volume repeated in FY2024-25 AR table, %s" % p,
                  v(OPS, "Total vehicle volume", p),
                  v(SECOND_SOURCE, "Vehicle volume, FY2024-25 AR table", p), 0.5, "FY2024-25 AR p6"))
    for p in ("FY2024", "FY2025"):
        T.append(("Guarantees repeated as next AR's comparative, %s" % p,
                  v(OPS, "Corporate guarantees for subsidiaries", p),
                  v(SECOND_SOURCE, "Guarantees, next AR comparative", p), 0.02, "next year's note 3.9.2"))
    for p in ("FY2024", "FY2025", "FY2026"):
        T.append(("M&HCV share change vs the change the AR states, %s" % p,
                  v(OPS, "M&HCV market share %", p) - v(OPS, "M&HCV market share %", prev(p)),
                  v(SECOND_SOURCE, "Stated change in M&HCV share (pp)", p), 0.15,
                  "MD&A; FY2025's stated -0.3 vs series -0.4 is the AR's own rounding gap"))
    return T


DISCLOSED_DIFFERENCES = [
    ("Analytical basis - consolidated excluding financial services; standalone rated entity alongside",
     "Methodology-determined under ICRA 934's dissimilar-business approach (quoted in the module "
     "docstring): HLF is assessed separately with its funding needs factored in; AL and its "
     "CV-related subsidiaries are analysed together. Consistent with the case file's "
     "'consolidated' declaration in substance; the reported consolidated view (incl. HLF) is a "
     "clearly-labelled supplement, never the basis."),
    ("Automotive OPBDITA is a bounded range, not a point",
     "The segment note gives the CV segment's PBIT but not its depreciation. The low bound adds "
     "standalone D&A only (ignores the non-financial subsidiaries' D&A - understates OPBDITA, "
     "conservative for leverage); the high bound adds consolidated D&A (includes the financial "
     "subsidiaries' D&A - overstates). Every conclusion is tested at the low bound."),
    ("Lease liabilities of the financial-services subsidiaries are not separately disclosed",
     "All consolidated lease liabilities are kept in automotive debt - overstates automotive debt "
     "by the FS share, conservative."),
    ("FY2024 consolidated figures are the RESTATED comparatives",
     "The FY2024-25 AR reclassified Rs 87.30 crore from financial-services revenue/result to other "
     "income for FY2024 (other income 140.58 -> 227.88; FS result 845.50 -> 758.20). CV segment "
     "figures are unchanged. FY2023 consolidated is as originally presented."),
    ("M&HCV market share - two figures in the FY2026 AR",
     "MD&A: 30.3% (down 0.4 pp); chairman's letter: 30.8%. The MD&A figure continues the series "
     "31.8% / 31.1% / 30.7% and is used; the 0.5 pp gap is a basis difference the AR does not explain."),
    ("Net-debt bridge residual",
     "The AR's bridge carries borrowings gross of effective-interest adjustments and includes a "
     "derivative asset/liability; our balance-sheet rebuild differs by up to ~Rs 51 crore (FY2023, "
     "interest accrued) - tolerance 60, named here rather than hidden."),
    ("Finance-cost and other-income decomposition only for FY2025-FY2026",
     "FY2023-FY2024 notes 2.5 and 2.2 were not decomposed; total finance costs (including the "
     "non-cash unwinding of discount on warranty provisions) are used for coverage - conservative."),
    ("Thirteen inputs no tie-out can reach (98.1% measured coverage) - named, with why",
     "Measured by tools/tieout_mutation.py, not asserted. Still verified by nothing: (a) capex "
     "and dividends paid, all four years - they appear only in the cash-flow statement in these "
     "documents, with no second disclosure to reconcile to; they feed RCF/FCF/NCA, so those "
     "rows are single-sourced; (b) FY2023 consolidated current borrowings and finance cost - "
     "FY2023's note 1.26 lines and segment interest were not decomposed (FY2024-FY2026 are "
     "tied); (c) corporate guarantees for FY2023 and FY2026 - each appears in one report only "
     "(FY2024 and FY2025 are tied to the next AR's comparative); (d) FY2023 equity into "
     "subsidiaries (Rs 19.81 crore, immaterial). None of these feeds the leverage or coverage "
     "ratios that drive the rating."),
    ("Debenture Redemption Fund deposit (Rs 100 crore, FY2026) - kept out of liquidity, debt kept gross",
     "Note 1.11B footnote: the Rs 900 crore of 3-12 month deposits 'includes fixed deposit of Rs. "
     "100 crores ... towards meeting Debenture Redemption Fund requirements'. It is usable only "
     "for the Rs 200 crore NCD due 17-Mar-2027, so it is excluded from free liquidity and counted "
     "in the liquidity arithmetic only against that redemption (ICRA_CONVENTIONS s8). ICRA's "
     "Total-debt formula would net it against debt (s3 fn 2): total debt 1,095.04 vs the gross "
     "1,195.04 shown, Total debt/OPBDITA 0.19x vs 0.21x. Debt is kept gross so it ties to the AR "
     "and screener.in; the gap is 0.76% of TNW - below the R13 1% threshold - and conservative."),
    ("Q1 FY2026 standalone PBT in ALResultsjune2025.md is an OCR misread",
     "The scan reads 191.13; the Q2 filing's comparative column prints 797.73 for the same quarter, "
     "consistent with the press release (PAT Rs 594 crore). Quarterly figures are not inputs here."),
]

if __name__ == "__main__":
    R = compute()
    for p in YEARS:
        print("=" * 72)
        print(p)
        for k, x in R[p].items():
            print("  %-62s %s" % (k, "-" if x is None else ("{:,.2f}".format(x))))
    T = tieouts(R)
    bad = [t for t in T if abs(t[1] - t[2]) > t[3]]
    print("=" * 72)
    print("TIE-OUTS: %d/%d reconcile" % (len(T) - len(bad), len(T)))
    for d, c, x, tol, src in bad:
        print("  FAIL  %-70s computed %.2f vs disclosed %.2f (tol %.2f)" % (d, c, x, tol))
