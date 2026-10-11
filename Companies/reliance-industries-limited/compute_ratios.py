"""Reliance Industries Limited (RIL) - ratio engine, CRISIL corporate (diversified conglomerate).

Engine contract (tools/engine_contract.py): YEARS, compute(), tieouts(R), DISCLOSED_DIFFERENCES.
Every figure is typed ONCE from the company's own audited annual reports (FY2023-24, FY2024-25,
FY2025-26) and the quarterly media releases in documents/, with the source on each table. All
amounts Rs crore. Periods are financial years ending 31 March.

ANALYTICAL BASIS (R12 - methodology-determined)
-----------------------------------------------
CRISIL 'Criteria for consolidation' (Section I): the business and financial risk profiles of
subsidiaries are generally combined with the parent's by full consolidation; the exceptions are
subsidiaries in a different sector (finance/insurance) or ring-fenced entities. RIL's material
subsidiaries (Jio Platforms, Reliance Jio Infocomm, Reliance Retail Ventures, Reliance Retail,
Reliance International - FY2025-26 AR Board's report) are all operating businesses under RIL's
management control sharing the Reliance name; the financial-services arm (Jio Financial
Services) was demerged in FY2023 (FY2023-24 AR, discontinued operations). BASIS = CONSOLIDATED
(full), as the case file declares. Non-controlling interest is kept inside adjusted networth.

CRISIL DEFINITIONS USED (CRISIL/CRISIL_CONVENTIONS.md s1-s5)
------------------------------------------------------------
  PBDIT     = PBT (before associates) + finance costs + D&A, i.e. INCLUDING recurring
              non-operating income (interest, dividend, treasury gains) and EXCLUDING one-time
              items: FY2026 other income carries Rs 8,924 crore 'proceeds of profit from sale of
              listed investments' (Q4 FY2026 release note 5) - removed.
  Interest  = finance costs as reported (incl. lease interest and the forex loss the company
              classifies as borrowing cost) + interest CAPITALISED (finance-cost note footnote).
  Adj. debt = borrowings (NC + current) + lease liabilities + deferred payment liabilities to DoT
              for spectrum (NC note 17 + current maturities in note 22) ['deferred payment
              credit' in CRISIL's list]. Supplier-finance arrangements (note 44, payable 45-1,083
              days after invoice) are added in the WIDE measure (FY2025-FY2026, the only years
              disclosed). Guarantees (note 34) assessed, not added - see DISCLOSED_DIFFERENCES.
  Adj. NW   = total equity incl. non-controlling interest; DTL not added; no revaluation reserve.
  RoCE      = PBIT / average (adj. debt + adj. networth + DTL).
"""

YEARS = ["FY2023", "FY2024", "FY2025", "FY2026"]
IX = {y: i for i, y in enumerate(YEARS)}
N = None

# =========================================================================================
# 1. CONSOLIDATED STATEMENT OF PROFIT AND LOSS
#    FY2023: FY2023-24 AR (comparative); FY2024: FY2024-25 AR (comparative, = FY2023-24 AR);
#    FY2025-FY2026: FY2025-26 AR p198.
# =========================================================================================
PL = {
    "Value of sales and services":    [974864, 1000122, 1071174, 1175919],
    "GST recovered":                  [83553, 85650, 91038, 100244],
    "Revenue from operations":        [891311, 914472, 980136, 1075675],
    "Other income":                   [11734, 16057, 17978, 28962],
    "Cost of materials consumed":     [450241, 400345, 422127, 443101],
    "Purchases of stock-in-trade":    [168505, 189881, 222686, 255829],
    "Change in inventories":          [-30263, -4883, -15124, -10267],
    "Excise duty":                    [13476, 13408, 15443, 18456],
    "Employee benefits expense":      [24872, 25679, 28559, 30318],
    "Finance costs":                  [19571, 23118, 24269, 27061],
    "Depreciation and amortisation":  [40303, 50832, 53136, 57688],
    "Other expenses":                 [122318, 127809, 141001, 159289],
    "Current tax":                    [8398, 13590, 12758, 9736],
    "Deferred tax":                   [11978, 12117, 12472, 17816],
    "Share of associates and JVs":    [24, 387, 522, 144],
    "Profit from discontinued operations": [418, 0, 0, 0],
}
PL_PRINTED = {
    "Total income":                   [903045, 930529, 998114, 1104637],
    "Total expenses":                 [809023, 826189, 892097, 981475],
    "PBT before associates":          [94022, 104340, 106017, 123162],
    "Profit for the year":            [74088, 79020, 81309, 95754],
    "Attributable to owners":         [66702, 69621, 69648, 80775],
    "Attributable to NCI":            [7386, 9399, 11661, 14979],
}

# Other income note 26 (FY2023-24 AR for FY2023/FY2024; FY2025-26 AR for FY2025/FY2026).
OTHER_INCOME = {
    "Interest income":                [11240, 10745, 12410, 13302],
    "Dividend income":                [38, 89, 504, 9100],
    "Other non-operating income":     [1758, 3302, 3507, 3614],
    "Gain/(loss) on financial assets": [-1302, 1921, 1557, 2946],
}
# One-time item inside other income: 'Other Income for the year ended March 31, 2026 includes
# Rs 8,924 crore, being proceeds of profit from sale of listed investments' (Q4 FY2026 release
# notes; same note in Q1/Q2/Q3 FY2026 and Q1 FY2027 releases). No other year carries one.
ONE_TIME_INCOME = {"Profit on sale of listed investments": [0, 0, 0, 8924]}

# Finance costs note 29 + 'Net of Interest Capitalised' footnote.
FIN_COST = {
    "Interest expenses (net of capitalised)": [17309, 20121, 20414, 22050],
    "Interest on lease liabilities":  [1649, 1651, 1707, 2006],
    "Other borrowing costs":          [124, 163, 290, 217],
    "Forex loss treated as borrowing cost": [489, 1183, 1858, 2788],
}
CAPITALISED_INTEREST = {"Interest capitalised": [8830, 15222, 18283, 16091]}
# Second source: each AR's footnote repeats the prior year ('Previous Year').
CAP_INT_NEXT_AR = {"Interest capitalised, next AR comparative": [N, 15222, 18283, N]}

# Other expenses note 30, FY2025-FY2026 decomposed (FY2025-26 AR). FY2023/FY2024 not
# decomposed beyond the two non-operating lines (FY2023-24 AR note 30).
OTHER_EXP_SUB = {
    "Manufacturing expenses":         [N, N, 39862, 40473],
    "Land development and construction": [N, N, 378, 310],
    "Selling and distribution":       [N, N, 23474, 21947],
    "Establishment expenses":         [N, N, 80143, 99806],
    "Less: transferred to project development": [N, N, -2856, -3247],
}
OTHER_EXP_MFG = {
    "Stores, chemicals and packing":  [N, N, 8057, 8453],
    "Electric power, fuel and water": [N, N, 23823, 22069],
    "Labour processing, royalty, machinery hire": [N, N, 5382, 6204],
    "Repairs to building":            [N, N, 340, 821],
    "Repairs to machinery":           [N, N, 2242, 2406],
    "Exchange difference (net)":      [463, 109, -189, -35],
    "Excise duty (in other exp.)":    [N, N, 51, 184],
    "Lease rent":                     [N, N, 156, 371],
}
OTHER_EXP_SELL = {
    "Warehousing and distribution":   [N, N, 12922, 12180],
    "Sales tax / VAT":                [N, N, 1873, 1439],
    "Other selling and distribution": [N, N, 8679, 8328],
}
OTHER_EXP_EST = {
    "Professional fees":              [N, N, 3459, 3874],
    "Network operating expenses":     [N, N, 31323, 32163],
    "Access charges (net)":           [N, N, 1281, 1637],
    "Regulatory charges":             [N, N, 10495, 11710],
    "General expenses":               [N, N, 11415, 12315],
    "Programming and telecast":       [N, N, 11489, 22546],
    "Rent":                           [N, N, 2623, 5803],
    "Insurance":                      [N, N, 1451, 1479],
    "Rates and taxes":                [N, N, 1273, 1877],
    "Other repairs":                  [N, N, 1941, 2448],
    "Travelling":                     [N, N, 872, 960],
    "Payment to auditors":            [N, N, 100, 122],
    "Loss on sale/discard of PPE":    [156, 265, 154, 116],
    "Charity and donations":          [N, N, 2267, 2756],
}

# =========================================================================================
# 2. CONSOLIDATED BALANCE SHEET (FY2023-24 AR for 31-Mar-2023; FY2024-25 AR for 31-Mar-2024;
#    FY2025-26 AR p196 for 31-Mar-2025/2026)
# =========================================================================================
NCA = {
    "Property, plant and equipment":  [570503, 606084, 683102, 751087],
    "Spectrum":                       [75351, 69852, 147122, 188120],
    "Other intangible assets":        [63681, 89060, 144639, 157126],
    "Goodwill":                       [15270, 14989, 24530, 28462],
    "Capital work-in-progress":       [117259, 152382, 169710, 192287],
    "Spectrum under development":     [122357, 129602, 54176, 8611],
    "Intangibles under development":  [54136, 56871, 38472, 36788],
    "Non-current investments":        [117087, 119502, 123672, 150901],
    "Non-current loans":              [1525, 899, 742, 826],
    "Other non-current financial assets": [2523, 2622, 6088, 4899],
    "Deferred tax assets":            [1549, 938, 408, 594],
    "Other non-current assets":       [40894, 43085, 58190, 64190],
}
CA = {
    "Inventories":                    [140008, 152770, 146062, 166941],
    "Current investments":            [118473, 106170, 118709, 97431],
    "Trade receivables":              [28448, 31628, 42121, 58491],
    "Cash and cash equivalents":      [68664, 97225, 106502, 145977],
    "Current loans":                  [176, 2517, 5182, 4870],
    "Other current financial assets": [19696, 23965, 23546, 57926],
    "Other current assets":           [49831, 55825, 57148, 62613],
}
EQUITY = {
    "Equity share capital":           [6766, 6766, 13532, 13532],
    "Other equity":                   [709106, 786715, 829668, 890498],
    "Non-controlling interest":       [113009, 132307, 166426, 181836],
}
NCL = {
    "Non-current borrowings":         [183176, 222712, 236899, 270751],
    "Non-current lease liabilities":  [16230, 17415, 17142, 16198],
    "Deferred payment liabilities (NC)": [112847, 108272, 104410, 99552],
    "Other non-current financial liabilities": [7704, 5667, 10909, 37833],
    "Non-current provisions":         [1607, 2044, 28304, 21793],
    "Deferred tax liabilities":       [60324, 72241, 83453, 97961],
    "Other non-current liabilities":  [919, 4480, 5641, 6932],
}
CL = {
    "Current borrowings":             [130790, 101910, 110631, 103670],
    "Current lease liabilities":      [4196, 4105, 4903, 7381],
    "Trade payables":                 [147172, 178377, 186789, 158842],
    "Other current financial liabilities": [68501, 55602, 57143, 64660],
    "Other current liabilities":      [42906, 55198, 90124, 201503],
    "Current provisions":             [2178, 2175, 4147, 5198],
}
BS_PRINTED = {
    "Total non-current assets":       [1182135, 1285886, 1450851, 1583891],
    "Total current assets":           [425296, 470100, 499270, 594249],
    "Total assets":                   [1607431, 1755986, 1950121, 2178140],
    "Total equity":                   [828881, 925788, 1009626, 1085866],
    "Total non-current liabilities":  [382807, 432831, 486758, 551020],
    "Total current liabilities":      [395743, 397367, 453737, 541254],
}

# Note 20 (current borrowings) and note 22 (other current financial liabilities) lines used.
DEBT_NOTES = {
    "Current maturities of NC borrowings": [48532, 45268, 29323, 25965],
    "Commercial paper":               [20506, 19595, 29162, 13186],
    "Current maturities of deferred payment liabilities": [4425, 4577, 4738, 4962],
    "Interest accrued on borrowings": [2817, 2180, 2046, 2497],
}
# Note 16 (FY2025-26 AR) - non-current borrowings by instrument, FY2025/FY2026.
NC_BORROW_LINES = {
    "Secured NCDs":                   [N, N, 20415, 20545],
    "Secured term loans from banks":  [N, N, 1089, 640],
    "Unsecured NCDs":                 [N, N, 7367, 7369],
    "Bonds (foreign currency)":       [N, N, 52048, 57274],
    "Unsecured term loans from banks": [N, N, 154683, 183436],
    "Unsecured term loans from others": [N, N, 1297, 1487],
}
# Note 20 (FY2025-26 AR) - current borrowings by instrument, FY2025/FY2026.
CB_LINES = {
    "Secured WC loans from banks":    [N, N, 15594, 17146],
    "Secured WC loans from others":   [N, N, 0, 7],
    "Unsecured WC loans from others": [N, N, 0, 32],
    "Unsecured loans from banks":     [N, N, 33124, 47334],
    "Unsecured loans from others":    [N, N, 3366, 0],
    "Commercial paper (note 20)":     [N, N, 29162, 13186],
    "Loans from related parties":     [N, N, 62, 0],
    "Current maturities (note 20)":   [N, N, 29323, 25965],
}
# Note 17 - DoT deferred payment liabilities by auction (FY2025-26 AR footnote ^).
DPL_AUCTIONS = {
    "March 2021 auction, 7.30%, 13 instalments": [N, N, N, 30213],
    "August 2022 auction, 7.20%, 16 instalments": [N, N, N, 73425],
    "July 2024 auction, 8.65%, 18 instalments": [N, N, N, 876],
}
# Note 44 - supplier financing arrangements (first disclosed FY2025-26 AR with FY2025 opening).
SUPPLIER_FINANCE = {
    "Supplier finance in trade payables": [N, N, 92223, 47121],
    "Supplier finance in other financial liabilities": [N, N, 11493, 29256],
}
# Note 23 - other current liabilities: contract liabilities (FY2025-26 AR).
CONTRACT_LIAB = {"Current contract liabilities": [N, N, 63005, 172201]}

# Company capital-management note 35 (net gearing) - the AR's own net-debt definition.
AR_NET_DEBT = {
    "Gross debt":                     [313966, 324622, 347530, 374421],
    "Cash and marketable securities": [188200, 208341, 230447, 249704],
    "Other marketable securities":    [1022, 4980, 5236, 6296],
    "Share call money receivable":    [41, 34, 0, 0],
    "Net debt":                       [125766, 116281, 117083, 124717],
    "Equity attributable to owners":  [715872, 793481, 843200, 904030],
}
# Company-published headline figures (Q4 media releases FY2025 and FY2026; MD&A).
AR_PUBLISHED = {
    "EBITDA":                         [N, 178290, 183422, 207911],
    "Capex (excl. spectrum)":         [N, 131769, 131107, 144271],
    "Net debt to EBITDA (x)":         [N, 0.65, 0.64, 0.60],
}

# =========================================================================================
# 3. CONSOLIDATED CASH FLOW (FY2023-24 AR for FY2023; FY2024-25 AR for FY2024 (as regrouped);
#    FY2025-26 AR p202 for FY2025/FY2026)
# =========================================================================================
CF = {
    "Cash generated from operations": [121329, 170749, 190628, 201721],
    "Taxes paid":                     [6297, 11961, 11925, 9608],
    "Net cash from operating activities": [115032, 158788, 178703, 192113],
    "Capex (PPE, spectrum, intangibles)": [140988, 152883, 139967, 122916],
    "Payment of deferred payment liabilities": [0, 4423, 4574, 4736],
    "Proceeds from NC borrowings":    [35936, 69610, 26378, 38871],
    "Repayment of NC borrowings":     [29059, 35055, 31755, 30881],
    "Current borrowings (net)":       [31198, -25293, 24624, -5171],
    "Dividend paid to owners":        [5083, 6089, 6766, 7443],
    "Dividend paid to NCI":           [0, 0, 414, 436],
    "Interest paid":                  [21650, 37173, 41024, 39981],
    "Payment of lease liabilities":   [1406, 2483, 2956, 6508],
    "Working capital change":         [-19634, 6366, 23724, 12497],
}
# 'Change in liability arising from financing activities' (each AR, below the cash flow).
DEBT_BRIDGE = {
    "Opening total borrowings":       [266305, 313966, 324622, 347530],
    "NC borrowings cash flow":        [6877, 34555, -5377, 7990],
    "Current borrowings cash flow":   [31198, -25293, 24624, -5171],
    "FX movement / others":           [9586, 1394, 3661, 24072],
    "Closing total borrowings":       [313966, 324622, 347530, 374421],
    "Closing NC incl. current maturities": [231708, 267980, 266222, 296716],
}

# Printed cash-flow totals and the remaining lines needed to rebuild them (same pages).
CF_PRINTED = {
    "PBT basis used in cash flow":    [94801, 104340, 106017, 123162],
    "Adjustments sub-total":          [46162, 60043, 60887, 66062],
    "Operating profit before WC changes": [140963, 164383, 166904, 189224],
    "Net cash used in investing":     [-91235, -113581, -137535, -101089],
    "Net cash from financing":        [10455, -16646, -31891, -51549],
    "Net increase in cash":           [34252, 28561, 9277, 39475],
    "Opening cash":                   [36178, 68664, 97225, 106502],
    "Cash added on acquisitions less demerger": [-1766, 0, 0, 0],
}
CF_OTHER = {   # investing lines other than capex / DPL; financing lines other than debt/div/int/lease
    "Other investing (disposals, investments, interest, dividends received)": [49753, 43725, 7006, 26563],
    "Other financing (equity, NCI, rights issue)": [519, 19837, 22, 0],
}
# Same balance-sheet note lines as printed in the FOLLOWING year's AR (independent document).
DEBT_NOTES_NEXT_AR = {
    "Current maturities of NC borrowings": [N, 45268, 29323, N],
    "Commercial paper":               [N, 19595, 29162, N],
    "Current maturities of deferred payment liabilities": [N, 4577, 4738, N],
    "Interest accrued on borrowings": [N, 2180, 2046, N],
}
# Supplier-finance roll-forward printed under the FY2026 cash flow (note 44).
SF_BRIDGE = {
    "Trade payables: opening / cash flow / FX": [92223, -53969, 8867],
    "Other financial liabilities: opening / cash flow / FX": [11493, 17198, 565],
    "Total opening (printed)":        [103716],
}
OTHER_CL_PAYABLES = {"Other payables in other current liabilities": [N, N, 27119, 29302]}
SOCE_DIVIDEND = {"Dividend in statement of changes in equity": [N, 6089, N, 7443]}
PROMOTER_SHARES = {"Promoter shares (FY2026)": 6645496096, "Total shares (FY2026)": 13532472634}
COMMIT_LINES = {
    "Capital commitments - joint arrangements": [N, N, 1624, 4875],
    "Capital commitments - others":   [N, N, 30005, 61642],
}
ONE_TIME_NEXT = {"One-time gain as stated in Q1 FY2027 release": [N, N, N, 8924]}
OPS_OTHER_RELEASE = {   # repeated in a different release
    "Jio ARPU Q4 (Rs/month)":         [N, N, 206.2, 214.0],
    "Jio data traffic (bn GB)":       [N, N, 184.5, N],
}

# =========================================================================================
# 4. SEGMENTS (audited consolidated segment information in the Q4 FY2025 and Q4 FY2026 media
#    releases; FY2023 not extracted)
# =========================================================================================
SEG_REV = {
    "O2C":                            [N, 564749, 626921, 662401],
    "Oil and Gas":                    [N, 24439, 25211, 23861],
    "Retail":                         [N, 306848, 330943, 371085],
    "Digital Services":               [N, 132938, 154119, 176164],
    "Others":                         [N, 80516, 55859, 80522],
}
SEG_REV_ELIM = {"Inter-segment transfers": [N, 109368, 121879, 138114]}
SEG_EBITDA = {
    "O2C":                            [N, 62389, 54988, 60546],
    "Oil and Gas":                    [N, 20191, 21188, 19050],
    "Retail":                         [N, 23108, 25094, 27034],
    "Digital Services":               [N, 56675, 65001, 76560],
    "Others":                         [N, 8466, 8526, 10857],
}
SEG_PRINTED = {
    "Total segment EBITDA":           [N, 170829, 174797, 194047],
    "Total segment EBIT":             [N, 120276, 122414, 136698],
    "Unallocated interest income":    [N, 9575, 10896, 10395],
    "Other unallocable income (net)": [N, -2393, -3024, 3130],
}
# The Q4 FY2026 release repeats FY2025 segment EBITDA; the Q4 FY2025 release states FY2024.
SEG_EBITDA_NEXT = {"Total segment EBITDA, next release": [N, N, 174797, N]}

# =========================================================================================
# 5. OPERATING METRICS (Q4 releases; each figure repeated as the comparative in the next
#    release - second source below). Jio ARPU is the Q4 exit (Rs/subscriber/month).
# =========================================================================================
OPS = {
    "Jio subscribers (mn)":           [N, 481.8, 488.2, 524.4],
    "Jio ARPU Q4 (Rs/month)":         [N, 181.7, 206.2, 214.0],
    "Jio data traffic (bn GB)":       [N, 148.5, 184.5, 241.4],
    "Retail stores (nos.)":           [N, N, 19340, 20160],
    "Retail area (mn sq ft)":         [N, N, 77.4, 78.3],
    "Retail registered customers (mn)": [N, N, 349, 387],
    "O2C throughput (MMT)":           [N, 78.2, 80.5, 80.0],
    "KG D6 production (BCFe)":        [N, 260.3, 270.9, 248.8],
}
OPS_NEXT_RELEASE = {   # the same metric as printed in the FOLLOWING release
    "Jio subscribers (mn)":           [N, 481.8, 488.2, 524.4],
    "O2C throughput (MMT)":           [N, 78.2, 80.5, 80.0],
    "KG D6 production (BCFe)":        [N, 260.3, 270.9, 248.8],
}
# Q1 FY2027 (unaudited, Media Release 17-Jul-2026)
Q1FY27 = {"Gross revenue": 340257, "EBITDA": 54067, "PAT incl. associates": 23196,
          "Outstanding debt": 369705, "Cash and equivalents": 246791, "Net debt": 122914,
          "Capex": 38682, "Jio subscribers (mn)": 533.3, "Jio ARPU (Rs)": 215.6,
          "Retail stores": 20169, "O2C throughput (MMT)": 18.1, "KG D6 (BCFe)": 59.2}

# Contingent liabilities and commitments, note 34 (FY2025-26 AR).
CONTINGENT = {
    "Claims - joint arrangements":    [N, N, 1458, 1692],
    "Claims - others":                [N, N, 5512, 3840],
    "Guarantees - joint arrangements": [N, N, 1078, 1318],
    "Guarantees - associates/JVs/others": [N, N, 5880, 5799],
    "Capital commitments":            [N, N, 31629, 66517],
}
PROMOTER_PCT = {"Promoter and promoter group (%)": [N, 49.11, N, 49.11]}


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


def cogs(p):
    return (v(PL, "Cost of materials consumed", p) + v(PL, "Purchases of stock-in-trade", p)
            + v(PL, "Change in inventories", p))


def total_expenses(p):
    return (cogs(p) + v(PL, "Excise duty", p) + v(PL, "Employee benefits expense", p)
            + v(PL, "Finance costs", p) + v(PL, "Depreciation and amortisation", p)
            + v(PL, "Other expenses", p))


def pbt(p):
    return v(PL, "Revenue from operations", p) + v(PL, "Other income", p) - total_expenses(p)


def pat(p):
    """Profit for the year incl. associates and (FY2023) discontinued operations."""
    return (pbt(p) - v(PL, "Current tax", p) - v(PL, "Deferred tax", p)
            + v(PL, "Share of associates and JVs", p) + v(PL, "Profit from discontinued operations", p))


def ebitda_reported(p):
    return pbt(p) + v(PL, "Finance costs", p) + v(PL, "Depreciation and amortisation", p)


def pbdit(p):
    """CRISIL PBDIT: incl. recurring non-operating income, excl. one-time items."""
    return ebitda_reported(p) - v(ONE_TIME_INCOME, "Profit on sale of listed investments", p)


def opbdit(p):
    """Operating profit EXCLUDING all other income - shown for margin analysis only."""
    return ebitda_reported(p) - v(PL, "Other income", p)


def interest(p):
    return v(PL, "Finance costs", p) + v(CAPITALISED_INTEREST, "Interest capitalised", p)


def borrowings(p):
    return v(NCL, "Non-current borrowings", p) + v(CL, "Current borrowings", p)


def leases(p):
    return v(NCL, "Non-current lease liabilities", p) + v(CL, "Current lease liabilities", p)


def dpl(p):
    return (v(NCL, "Deferred payment liabilities (NC)", p)
            + v(DEBT_NOTES, "Current maturities of deferred payment liabilities", p))


def adj_debt(p):
    return borrowings(p) + leases(p) + dpl(p)


def supplier_finance(p):
    x = [v(SUPPLIER_FINANCE, k, p) for k in SUPPLIER_FINANCE]
    return None if x[0] is None else sum(x)


def adj_debt_wide(p):
    sf = supplier_finance(p)
    return None if sf is None else adj_debt(p) + sf


def adj_networth(p):
    return tot(EQUITY, p)


def cash_ms(p):
    """Cash + current investments + other marketable securities (the AR's own definition)."""
    return (v(CA, "Cash and cash equivalents", p) + v(CA, "Current investments", p)
            + v(AR_NET_DEBT, "Other marketable securities", p))


def total_liabilities(p):
    return tot(NCL, p) + tot(CL, p)


def capital_employed(p):
    return adj_debt(p) + adj_networth(p) + v(NCL, "Deferred tax liabilities", p)


def nwc(p):
    return v(CA, "Inventories", p) + v(CA, "Trade receivables", p) - v(CL, "Trade payables", p)


def debt_due_1y(p):
    """CRISIL CDSCR denominator debt: current maturities of NC borrowings + current DPL +
    current lease liabilities. CP and working-capital loans (rolled over) excluded."""
    return (v(DEBT_NOTES, "Current maturities of NC borrowings", p)
            + v(DEBT_NOTES, "Current maturities of deferred payment liabilities", p)
            + v(CL, "Current lease liabilities", p))


def compute():
    R = {}
    for p in YEARS:
        oi = v(PL, "Revenue from operations", p)
        pb = pbdit(p)
        da = v(PL, "Depreciation and amortisation", p)
        it = interest(p)
        pt = pat(p)
        ad = adj_debt(p)
        aw = adj_debt_wide(p)
        nw = adj_networth(p)
        liq = cash_ms(p)
        div = v(CF, "Dividend paid to owners", p) + v(CF, "Dividend paid to NCI", p)
        cfo = v(CF, "Net cash from operating activities", p)
        capex = v(CF, "Capex (PPE, spectrum, intangibles)", p)
        r = {
            "Operating income (net of GST)": oi,
            "Gross revenue (value of sales and services)": v(PL, "Value of sales and services", p),
            "EBITDA as reported (company)": ebitda_reported(p),
            "PBDIT (CRISIL)": pb,
            "PBDIT margin (%)": 100 * pb / oi,
            "OPBDIT excl. all other income": opbdit(p),
            "OPBDIT margin excl. other income (%)": 100 * opbdit(p) / oi,
            "Other income share of PBDIT (%)": 100 * (v(PL, "Other income", p)
                                                      - v(ONE_TIME_INCOME, "Profit on sale of listed investments", p)) / pb,
            "PAT (incl. associates)": pt,
            "PAT margin (%)": 100 * pt / oi,
            "PAT excl. one-time gain (pre-tax amount deducted)": pt - v(ONE_TIME_INCOME, "Profit on sale of listed investments", p),
            "Interest (incl. capitalised)": it,
            "Interest capitalised": v(CAPITALISED_INTEREST, "Interest capitalised", p),
            "Interest coverage (x)": pb / it,
            "Interest coverage on P&L finance cost (x)": pb / v(PL, "Finance costs", p),
            "Borrowings": borrowings(p),
            "Lease liabilities": leases(p),
            "Deferred payment liabilities (spectrum)": dpl(p),
            "Adjusted total debt": ad,
            "Supplier finance": supplier_finance(p),
            "Adjusted total debt incl. supplier finance": aw,
            "Adjusted networth (incl. NCI)": nw,
            "Gearing (x)": ad / nw,
            "Gearing incl. supplier finance (x)": None if aw is None else aw / nw,
            "Company net gearing (x)": v(AR_NET_DEBT, "Net debt", p) / v(AR_NET_DEBT, "Equity attributable to owners", p),
            "TOL/ANW (x)": total_liabilities(p) / nw,
            "Adjusted debt/PBDIT (x)": ad / pb,
            "Adjusted debt incl. SF/PBDIT (x)": None if aw is None else aw / pb,
            "Cash and marketable securities": liq,
            "Net adjusted debt": ad - liq,
            "Net adjusted debt/PBDIT (x)": (ad - liq) / pb,
            "Company net debt": v(AR_NET_DEBT, "Net debt", p),
            "Company net debt/PBDIT (x)": v(AR_NET_DEBT, "Net debt", p) / pb,
            "NCATD (x)": (pt - div + da) / ad,
            "NCA (PAT - dividend + D&A)": pt - div + da,
            "Current ratio (x)": tot(CA, p) / tot(CL, p),
            "Debtor days": 365 * v(CA, "Trade receivables", p) / oi,
            "Inventory days": 365 * v(CA, "Inventories", p) / cogs(p),
            "Payable days": 365 * v(CL, "Trade payables", p) / cogs(p),
            "Net working capital (inv + debtors - creditors)": nwc(p),
            "GCA days (CRISIL: operating current assets / operating income)": 365 * (
                tot(CA, p) - v(CA, "Cash and cash equivalents", p) - v(CA, "Current investments", p)) / oi,
            "CFO": cfo,
            "Capex (cash flow)": capex,
            "FCF (CFO - capex - DPL - lease payments)": (cfo - capex
                                                         - v(CF, "Payment of deferred payment liabilities", p)
                                                         - v(CF, "Payment of lease liabilities", p)),
            "FCF after dividends": (cfo - capex - v(CF, "Payment of deferred payment liabilities", p)
                                    - v(CF, "Payment of lease liabilities", p) - div),
            "CFO/adjusted debt (x)": cfo / ad,
            "Capex/PBDIT (x)": capex / pb,
            "Debt payable within one year": debt_due_1y(p),
            "Commercial paper outstanding": v(DEBT_NOTES, "Commercial paper", p),
            "Liquidity cover: cash & MS / (debt due 1y + CP) (x)": liq / (debt_due_1y(p) + v(DEBT_NOTES, "Commercial paper", p)),
        }
        pp = prev(p)
        if pp is not None:
            r["Revenue growth (%)"] = 100 * (oi / v(PL, "Revenue from operations", pp) - 1)
            r["RoCE (%)"] = 100 * (pb - da) / ((capital_employed(p) + capital_employed(pp)) / 2)
            dnwc = nwc(p) - nwc(pp)
            r["CDSCR (x)"] = (pt + da + it - 0.25 * dnwc) / (debt_due_1y(p) + it)
        else:
            r["Revenue growth (%)"] = None
            r["RoCE (%)"] = None
            r["CDSCR (x)"] = None
        if v(SEG_EBITDA, "O2C", p) is not None:
            se = tot(SEG_EBITDA, p)
            for k in SEG_EBITDA:
                r["Segment EBITDA share - %s (%%)" % k] = 100 * v(SEG_EBITDA, k, p) / se
            r["Consumer businesses (Retail + Digital) EBITDA share (%)"] = 100 * (
                v(SEG_EBITDA, "Retail", p) + v(SEG_EBITDA, "Digital Services", p)) / se
            r["Energy (O2C + Oil and Gas) EBITDA share (%)"] = 100 * (
                v(SEG_EBITDA, "O2C", p) + v(SEG_EBITDA, "Oil and Gas", p)) / se
            r["O2C EBITDA margin on segment revenue (%)"] = 100 * v(SEG_EBITDA, "O2C", p) / v(SEG_REV, "O2C", p)
            r["Digital EBITDA margin on segment revenue (%)"] = 100 * v(SEG_EBITDA, "Digital Services", p) / v(SEG_REV, "Digital Services", p)
            r["Retail EBITDA margin on segment revenue (%)"] = 100 * v(SEG_EBITDA, "Retail", p) / v(SEG_REV, "Retail", p)
        for k in OPS:
            r[k] = v(OPS, k, p)
        R[p] = r
    return R


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source). Each 'disclosed' figure is a
    number a document PRINTS, independent of the line items the computation is built from."""
    if R is None:
        R = compute()
    T = []
    for p in YEARS:
        T += [
            ("Revenue from operations = value of sales and services - GST, %s" % p,
             v(PL, "Value of sales and services", p) - v(PL, "GST recovered", p),
             v(PL, "Revenue from operations", p), 0.5, "consolidated P&L"),
            ("Total income = revenue + other income, %s" % p,
             v(PL, "Revenue from operations", p) + v(PL, "Other income", p),
             v(PL_PRINTED, "Total income", p), 0.5, "consolidated P&L"),
            ("Total expenses (sum of lines), %s" % p, total_expenses(p),
             v(PL_PRINTED, "Total expenses", p), 0.5, "consolidated P&L"),
            ("PBT before associates, %s" % p, pbt(p), v(PL_PRINTED, "PBT before associates", p), 0.5,
             "consolidated P&L"),
            ("Profit for the year, %s" % p, pat(p), v(PL_PRINTED, "Profit for the year", p), 0.5,
             "consolidated P&L (FY2023 incl. discontinued operations 418)"),
            ("Owners + NCI = profit for the year, %s" % p,
             v(PL_PRINTED, "Attributable to owners", p) + v(PL_PRINTED, "Attributable to NCI", p),
             v(PL_PRINTED, "Profit for the year", p), 0.5, "consolidated P&L attribution"),
            ("Other income = note 26 lines, %s" % p, tot(OTHER_INCOME, p), v(PL, "Other income", p), 0.5,
             "note 26"),
            ("Finance costs = note 29 lines, %s" % p, tot(FIN_COST, p), v(PL, "Finance costs", p), 0.5,
             "note 29"),
            ("Non-current assets (sum of lines), %s" % p, tot(NCA, p),
             v(BS_PRINTED, "Total non-current assets", p), 0.5, "consolidated balance sheet"),
            ("Current assets (sum of lines), %s" % p, tot(CA, p),
             v(BS_PRINTED, "Total current assets", p), 0.5, "consolidated balance sheet"),
            ("Total assets, %s" % p, tot(NCA, p) + tot(CA, p), v(BS_PRINTED, "Total assets", p), 0.5,
             "consolidated balance sheet"),
            ("Total equity (incl. NCI), %s" % p, tot(EQUITY, p), v(BS_PRINTED, "Total equity", p), 0.5,
             "consolidated balance sheet"),
            ("Non-current liabilities (sum of lines), %s" % p, tot(NCL, p),
             v(BS_PRINTED, "Total non-current liabilities", p), 0.5, "consolidated balance sheet"),
            ("Current liabilities (sum of lines), %s" % p, tot(CL, p),
             v(BS_PRINTED, "Total current liabilities", p), 0.5, "consolidated balance sheet"),
            ("Balance sheet balances, %s" % p, tot(NCA, p) + tot(CA, p),
             tot(EQUITY, p) + total_liabilities(p), 0.5, "consolidated balance sheet"),
            ("Borrowings = AR gross debt (capital management note), %s" % p, borrowings(p),
             v(AR_NET_DEBT, "Gross debt", p), 0.5, "note 35 net gearing"),
            ("Owners' equity = share capital + other equity, %s" % p,
             v(EQUITY, "Equity share capital", p) + v(EQUITY, "Other equity", p),
             v(AR_NET_DEBT, "Equity attributable to owners", p), 0.5, "note 35 net gearing"),
            ("AR net debt = gross debt - cash & marketable securities, %s" % p,
             v(AR_NET_DEBT, "Gross debt", p) - v(AR_NET_DEBT, "Cash and marketable securities", p),
             v(AR_NET_DEBT, "Net debt", p), 0.5, "note 35 arithmetic"),
            ("Cash & MS rebuilt from balance sheet, %s" % p,
             cash_ms(p) + v(AR_NET_DEBT, "Share call money receivable", p),
             v(AR_NET_DEBT, "Cash and marketable securities", p), 70.0,
             "note 35 footnote; FY2024 footnote components exceed the printed total by 68 - "
             "named in DISCLOSED_DIFFERENCES"),
            ("Closing borrowings in financing-liability bridge = balance sheet, %s" % p,
             borrowings(p), v(DEBT_BRIDGE, "Closing total borrowings", p), 0.5,
             "change in liabilities from financing activities"),
            ("Bridge arithmetic: opening + flows + FX = closing, %s" % p,
             v(DEBT_BRIDGE, "Opening total borrowings", p) + v(DEBT_BRIDGE, "NC borrowings cash flow", p)
             + v(DEBT_BRIDGE, "Current borrowings cash flow", p) + v(DEBT_BRIDGE, "FX movement / others", p),
             v(DEBT_BRIDGE, "Closing total borrowings", p), 0.5, "financing-liability bridge"),
            ("NC borrowings + current maturities = bridge NC line, %s" % p,
             v(NCL, "Non-current borrowings", p) + v(DEBT_NOTES, "Current maturities of NC borrowings", p),
             v(DEBT_BRIDGE, "Closing NC incl. current maturities", p), 0.5, "notes 16/20 vs bridge"),
            ("Cash-flow NC proceeds - repayments = bridge NC cash flow, %s" % p,
             v(CF, "Proceeds from NC borrowings", p) - v(CF, "Repayment of NC borrowings", p),
             v(DEBT_BRIDGE, "NC borrowings cash flow", p), 0.5, "cash flow vs bridge"),
            ("Cash-flow current borrowings (net) = bridge, %s" % p,
             v(CF, "Current borrowings (net)", p), v(DEBT_BRIDGE, "Current borrowings cash flow", p), 0.5,
             "cash flow vs bridge"),
            ("CFO = cash generated - taxes paid, %s" % p,
             v(CF, "Cash generated from operations", p) - v(CF, "Taxes paid", p),
             v(CF, "Net cash from operating activities", p), 0.5, "consolidated cash flow"),
        ]
    for p in YEARS[1:]:
        T.append(("Opening borrowings = prior year closing, %s" % p,
                  v(DEBT_BRIDGE, "Opening total borrowings", p), borrowings(prev(p)), 0.5,
                  "bridge opening vs prior balance sheet"))
    for p in ("FY2024", "FY2025", "FY2026"):
        T += [
            ("PBDIT + one-time = company EBITDA, %s" % p,
             pbdit(p) + v(ONE_TIME_INCOME, "Profit on sale of listed investments", p),
             v(AR_PUBLISHED, "EBITDA", p), 0.5, "Q4 media release EBITDA"),
            ("Company ND/EBITDA rebuilt, %s" % p,
             v(AR_NET_DEBT, "Net debt", p) / ebitda_reported(p),
             v(AR_PUBLISHED, "Net debt to EBITDA (x)", p), 0.006, "Q4 media release (2 dp)"),
            ("Segment revenue - inter-segment = value of sales and services, %s" % p,
             tot(SEG_REV, p) - v(SEG_REV_ELIM, "Inter-segment transfers", p),
             v(PL, "Value of sales and services", p), 0.5, "segment information vs P&L"),
            ("Segment EBITDA lines = printed total, %s" % p, tot(SEG_EBITDA, p),
             v(SEG_PRINTED, "Total segment EBITDA", p), 0.5, "segment information"),
            ("Segment EBIT + interest income + unallocable - finance cost = PBT, %s" % p,
             v(SEG_PRINTED, "Total segment EBIT", p) + v(SEG_PRINTED, "Unallocated interest income", p)
             + v(SEG_PRINTED, "Other unallocable income (net)", p) - v(PL, "Finance costs", p),
             v(PL_PRINTED, "PBT before associates", p), 0.5, "segment information vs P&L"),
            ("Segment D&A (EBITDA - EBIT) within reported D&A, %s" % p,
             v(SEG_PRINTED, "Total segment EBITDA", p) - v(SEG_PRINTED, "Total segment EBIT", p),
             v(PL, "Depreciation and amortisation", p), 800.0,
             "segment D&A vs P&L D&A; residual = unallocated D&A (279 / 753 / 339)"),
        ]
    for p in ("FY2024", "FY2025"):
        T.append(("Interest capitalised repeated in next AR, %s" % p,
                  v(CAPITALISED_INTEREST, "Interest capitalised", p),
                  v(CAP_INT_NEXT_AR, "Interest capitalised, next AR comparative", p), 0.5,
                  "finance-cost footnote 'Previous Year'"))
    T.append(("Segment EBITDA FY2025 repeated in Q4 FY2026 release",
              tot(SEG_EBITDA, "FY2025"), v(SEG_EBITDA_NEXT, "Total segment EBITDA, next release", "FY2025"),
              0.5, "Q4 FY2026 release comparative column"))
    for p in ("FY2025", "FY2026"):
        T += [
            ("Other expenses = note 30 subtotals, %s" % p, tot(OTHER_EXP_SUB, p),
             v(PL, "Other expenses", p), 0.5, "note 30"),
            ("Manufacturing expenses = its lines, %s" % p, tot(OTHER_EXP_MFG, p),
             v(OTHER_EXP_SUB, "Manufacturing expenses", p), 0.5, "note 30"),
            ("Selling and distribution = its lines, %s" % p, tot(OTHER_EXP_SELL, p),
             v(OTHER_EXP_SUB, "Selling and distribution", p), 0.5, "note 30"),
            ("Establishment expenses = its lines, %s" % p, tot(OTHER_EXP_EST, p),
             v(OTHER_EXP_SUB, "Establishment expenses", p), 0.5, "note 30"),
            ("NC borrowings = note 16 lines, %s" % p, tot(NC_BORROW_LINES, p),
             v(NCL, "Non-current borrowings", p), 0.5, "note 16"),
            ("Current borrowings = note 20 lines, %s" % p, tot(CB_LINES, p),
             v(CL, "Current borrowings", p), 0.5, "note 20"),
            ("Note 20 CP = CP used, %s" % p, v(CB_LINES, "Commercial paper (note 20)", p),
             v(DEBT_NOTES, "Commercial paper", p), 0.5, "note 20"),
            ("Note 20 current maturities = note 16 current column, %s" % p,
             v(CB_LINES, "Current maturities (note 20)", p),
             v(DEBT_NOTES, "Current maturities of NC borrowings", p), 0.5, "notes 16/20"),
        ]
    T.append(("DoT deferred payment liabilities = sum of auctions, FY2026",
              tot(DPL_AUCTIONS, "FY2026"), dpl("FY2026"), 0.5, "note 17 footnote ^ vs notes 17 + 22"))
    for p in ("FY2024", "FY2025", "FY2026"):
        for k in OPS_NEXT_RELEASE:
            T.append(("%s repeated in the following release, %s" % (k, p), v(OPS, k, p),
                      v(OPS_NEXT_RELEASE, k, p), 0.05,
                      "Q4 FY2025 / Q4 FY2026 / Q1 FY2027 release comparative columns"))
    for p in YEARS:
        T += [
            ("Cash-flow PBT basis + adjustments = op. profit before WC, %s" % p,
             v(CF_PRINTED, "PBT basis used in cash flow", p) + v(CF_PRINTED, "Adjustments sub-total", p),
             v(CF_PRINTED, "Operating profit before WC changes", p), 0.5, "consolidated cash flow"),
            ("Op. profit before WC + WC change = cash generated, %s" % p,
             v(CF_PRINTED, "Operating profit before WC changes", p) + v(CF, "Working capital change", p),
             v(CF, "Cash generated from operations", p), 0.5, "consolidated cash flow"),
            ("Investing total rebuilt (capex, DPL, other), %s" % p,
             -v(CF, "Capex (PPE, spectrum, intangibles)", p) - v(CF, "Payment of deferred payment liabilities", p)
             + v(CF_OTHER, "Other investing (disposals, investments, interest, dividends received)", p),
             v(CF_PRINTED, "Net cash used in investing", p), 0.5, "consolidated cash flow"),
            ("Financing total rebuilt (debt, dividends, interest, leases), %s" % p,
             v(CF, "Proceeds from NC borrowings", p) - v(CF, "Repayment of NC borrowings", p)
             + v(CF, "Current borrowings (net)", p) - v(CF, "Dividend paid to owners", p)
             - v(CF, "Dividend paid to NCI", p) - v(CF, "Interest paid", p)
             - v(CF, "Payment of lease liabilities", p)
             + v(CF_OTHER, "Other financing (equity, NCI, rights issue)", p),
             v(CF_PRINTED, "Net cash from financing", p), 0.5, "consolidated cash flow"),
            ("CFO + investing + financing = net increase in cash, %s" % p,
             v(CF, "Net cash from operating activities", p) + v(CF_PRINTED, "Net cash used in investing", p)
             + v(CF_PRINTED, "Net cash from financing", p), v(CF_PRINTED, "Net increase in cash", p), 0.5,
             "consolidated cash flow"),
            ("Opening cash + increase (+ FY2023 acquisitions less demerger) = balance-sheet cash, %s" % p,
             v(CF_PRINTED, "Opening cash", p) + v(CF_PRINTED, "Net increase in cash", p)
             + v(CF_PRINTED, "Cash added on acquisitions less demerger", p),
             v(CA, "Cash and cash equivalents", p), 0.5, "cash flow vs balance sheet"),
        ]
    for p in ("FY2024", "FY2025", "FY2026"):
        T.append(("Cash-flow PBT basis = P&L PBT before associates, %s" % p,
                  v(CF_PRINTED, "PBT basis used in cash flow", p), v(PL_PRINTED, "PBT before associates", p),
                  0.5, "cash flow vs P&L"))
        T.append(("Gross interest (incl. capitalised, excl. forex) vs cash interest paid, %s" % p,
                  v(FIN_COST, "Interest expenses (net of capitalised)", p)
                  + v(CAPITALISED_INTEREST, "Interest capitalised", p)
                  + v(FIN_COST, "Interest on lease liabilities", p) + v(FIN_COST, "Other borrowing costs", p),
                  v(CF, "Interest paid", p), 500.0,
                  "note 29 + footnote vs cash flow; residual = accrual timing (16 / 330 / 383)"))
    for p in YEARS[1:]:
        T.append(("Cash: prior closing = this year's opening, %s" % p, v(CA, "Cash and cash equivalents", prev(p)),
                  v(CF_PRINTED, "Opening cash", p), 0.5, "cash flow"))
    for p in ("FY2024", "FY2025"):
        for k in DEBT_NOTES_NEXT_AR:
            T.append(("%s repeated in next AR, %s" % (k, p), v(DEBT_NOTES, k, p),
                      v(DEBT_NOTES_NEXT_AR, k, p), 0.5, "next year's AR comparative"))
    T += [
        ("Supplier finance FY2025 = roll-forward opening",
         supplier_finance("FY2025"), SF_BRIDGE["Total opening (printed)"][0], 0.5, "note 44 cash-flow table"),
        ("Supplier finance in trade payables FY2026 = roll-forward",
         sum(SF_BRIDGE["Trade payables: opening / cash flow / FX"]),
         v(SUPPLIER_FINANCE, "Supplier finance in trade payables", "FY2026"), 0.5, "note 44"),
        ("Supplier finance in other fin. liabilities FY2026 = roll-forward",
         sum(SF_BRIDGE["Other financial liabilities: opening / cash flow / FX"]),
         v(SUPPLIER_FINANCE, "Supplier finance in other financial liabilities", "FY2026"), 0.5, "note 44"),
        ("Supplier-finance opening split = FY2025 lines (trade payables)",
         SF_BRIDGE["Trade payables: opening / cash flow / FX"][0],
         v(SUPPLIER_FINANCE, "Supplier finance in trade payables", "FY2025"), 0.5, "note 44"),
        ("Supplier-finance opening split = FY2025 lines (other financial liabilities)",
         SF_BRIDGE["Other financial liabilities: opening / cash flow / FX"][0],
         v(SUPPLIER_FINANCE, "Supplier finance in other financial liabilities", "FY2025"), 0.5, "note 44"),
        ("Promoter holding FY2026 from share counts",
         100 * PROMOTER_SHARES["Promoter shares (FY2026)"] / PROMOTER_SHARES["Total shares (FY2026)"],
         v(PROMOTER_PCT, "Promoter and promoter group (%)", "FY2026"), 0.006, "shareholding distribution"),
        ("Promoter holding FY2024 = FY2026 (promoter shares doubled with the 1:1 bonus)",
         v(PROMOTER_PCT, "Promoter and promoter group (%)", "FY2024"),
         v(PROMOTER_PCT, "Promoter and promoter group (%)", "FY2026"), 0.006,
         "FY2023-24 AR 3,32,27,48,048 shares x2 = FY2025-26 AR 6,64,54,96,096"),
        ("One-time gain FY2026 restated in Q1 FY2027 release",
         v(ONE_TIME_INCOME, "Profit on sale of listed investments", "FY2026"),
         v(ONE_TIME_NEXT, "One-time gain as stated in Q1 FY2027 release", "FY2026"), 0.5, "Q1 FY2027 note 3"),
    ]
    for p in ("FY2025", "FY2026"):
        T += [
            ("Other current liabilities = contract liabilities + other payables, %s" % p,
             v(CONTRACT_LIAB, "Current contract liabilities", p)
             + v(OTHER_CL_PAYABLES, "Other payables in other current liabilities", p),
             v(CL, "Other current liabilities", p), 0.5, "note 23"),
            ("Capital commitments = note 34 lines, %s" % p, tot(COMMIT_LINES, p),
             v(CONTINGENT, "Capital commitments", p), 0.5, "note 34 (II)(A)"),
        ]
        for k in OPS_OTHER_RELEASE:
            if v(OPS_OTHER_RELEASE, k, p) is not None:
                T.append(("%s in another release, %s" % (k, p), v(OPS, k, p), v(OPS_OTHER_RELEASE, k, p), 0.05,
                          "Q4 FY2026 release (4Q FY25 column) / Q1 FY2027 release (FY26 column)"))
    for p in ("FY2024", "FY2026"):
        T.append(("Dividend paid to owners = SOCE dividend, %s" % p, v(CF, "Dividend paid to owners", p),
                  v(SOCE_DIVIDEND, "Dividend in statement of changes in equity", p), 0.5, "SOCE"))
    return T


DISCLOSED_DIFFERENCES = [
    ("Analytical basis - full consolidation",
     "Methodology-determined under CRISIL's consolidation criteria (module docstring): all "
     "material subsidiaries are operating businesses in the group's own sectors, under RIL's "
     "management control and sharing its name; there is no financial-sector subsidiary after "
     "the FY2023 demerger of Jio Financial Services. Matches the case file's 'consolidated'."),
    ("One-time income removed from PBDIT (FY2026, Rs 8,924 crore)",
     "The company's own releases describe it as 'proceeds of profit from sale of listed "
     "investments' and exclude it when comparing EBITDA. CRISIL PBDIT excludes one-time income. "
     "PBDIT FY2026 = 2,07,911 - 8,924 = 1,98,987. The PAT row is NOT tax-adjusted for it - the "
     "'PAT excl. one-time gain' row deducts the pre-tax amount (conservative)."),
    ("Interest includes capitalised interest and the forex loss classified as finance cost",
     "CRISIL interest includes non-funded capitalised interest (Rs 16,091 crore FY2026). The "
     "company classifies an 'applicable loss on foreign currency transactions' (Rs 2,788 crore "
     "FY2026) inside finance costs; it is kept in interest (and therefore added back in PBDIT) - "
     "conservative for coverage. Cash interest paid (39,981) is close to interest excluding "
     "that forex line (40,364)."),
    ("Adjusted debt - deferred spectrum liabilities included; supplier finance in a wide measure",
     "DoT deferred payment liabilities (Rs 1,04,514 crore FY2026) are debt-like 'deferred payment "
     "credit' and are included. Supplier-finance arrangements (Rs 76,377 crore FY2026; Rs "
     "1,03,716 crore FY2025) are presented by the company in trade payables / other financial "
     "liabilities with due dates up to 1,083 days after invoice; CRISIL folds such acceptances "
     "into debt, so a WIDE measure adds them. Not disclosed for FY2023-FY2024, so the trend "
     "uses the core measure."),
    ("Guarantees and claims not added to debt",
     "Note 34: guarantees Rs 7,117 crore and claims not acknowledged Rs 5,532 crore (FY2026), "
     "together 0.6% of adjusted networth - below R13 materiality individually and assessed as "
     "unlikely to devolve. The KG D6 gas-migration demand (USD 2.81 billion, RIL share USD 1.87 "
     "billion) is NOT in note 34 - the company considers it remote and does not quantify it; it "
     "is carried as a qualitative event risk."),
    ("FY2024 cash & marketable securities - AR footnote components exceed its printed total by 68",
     "FY2023-24 AR note: 97,225 + 1,06,170 + 4,980 + 34 = 2,08,409 vs printed 2,08,341; the "
     "printed figure (and net debt 1,16,281) is used for the company series; tolerance 70."),
    ("Jio ARPU is the Q4 exit rate",
     "The Q4 FY2026 release prints FY2025 ARPU as 196.1 in its full-year column while the Q4 "
     "FY2025 release prints 206.2 (Q4). The Q4 exit series (181.7 / 206.2 / 214.0) is used."),
    ("Segment data for FY2023 and FY2023-FY2024 other-expense detail not extracted",
     "Segment tables were taken from the Q4 FY2025 and Q4 FY2026 releases (FY2024-FY2026). "
     "Other expenses were decomposed for FY2025-FY2026 (tied to note 30); for FY2023-FY2024 only "
     "the exchange-difference (463/109) and asset-disposal (156/265) lines were read - both "
     "small and recurring-scale, retained in PBDIT."),
    ("Contract liabilities jump (FY2026) treated as working capital, flagged",
     "Note 23 current contract liabilities rose to 1,72,201 from 63,005 (+1,09,196); the "
     "standalone figure rose only to 89,099 from 66,226, so most of the increase sits in "
     "subsidiaries or in lower intra-group elimination. It lifted FY2026 CFO through 'trade and "
     "other payables' (+86,609). Not explained in the documents; carried as an issuer question."),
    ("Thirty-five inputs no tie-out can reach (94.8% measured coverage) - named, with why",
     "Measured by tools/tieout_mutation.py, not asserted. Verified by nothing because no second "
     "disclosure exists in the case documents: (a) company capex excl. spectrum (FY2024-FY2026) - "
     "a management figure, used only in prose; (b) FY2023 capitalised interest, CP, current DPL "
     "and accrued interest - the FY2022-23 AR is not in the folder, so each appears only as the "
     "FY2023-24 AR comparative; FY2026 accrued interest has no following AR yet; (c) contingent "
     "claims and guarantees - one note, no second source; (d) the zero one-time-income entries "
     "for FY2023-FY2025 (an absence: no release or AR names a one-off for those years); (e) Jio "
     "ARPU FY2024 and data traffic FY2024/FY2026, retail stores, area and registered customers - "
     "each printed in one release only; (f) FY2023-FY2024 forex and asset-disposal lines in "
     "other expenses; (g) share call money receivable. None of (a)-(g) feeds the leverage or "
     "coverage ratios except FY2023 capitalised interest (interest coverage FY2023 only)."),
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
