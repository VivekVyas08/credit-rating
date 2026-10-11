"""Equitas Small Finance Bank Limited (ESFBL) - ratio engine, CareEdge (Banks / SFB).

Engine contract (tools/engine_contract.py): YEARS, compute(), tieouts(R), DISCLOSED_DIFFERENCES.

SOURCES. Balance sheet and P&L are typed ONCE, in Rs '000 exactly as printed, and converted to
Rs crore in code (k()). FY2026 + FY2025: FY2025-26 Integrated AR (FY2025 = the RESTATED
comparative - see DISCLOSED_DIFFERENCES); FY2024: FY2024-25 AR; FY2023: FY2023-24 AR. Regulatory
notes (Schedule 18: capital, asset quality, provisions, business ratios) are in Rs crore as
printed. Every table names its note.

BASIS. Standalone - the bank "does not have any Subsidiary, Associate or Joint venture"
(Q1 FY2027 results, note 13). Equitas Holdings Limited was amalgamated into the bank in FY2023.

DEFINITIONS - CareEdge 'Financial Ratios - Financial Sector' (February 2025), verbatim formulas:
  NIM = Net Interest Income / Avg. Total Assets;  ROTA = PAT / Average Total Assets
  RONW = PAT / Avg. Tangible Net worth;  Credit cost = Provisions & Write-offs (in the P&L)
  / Avg. Total Assets;  Cost to income = Operating Expenses / (Total Income - Interest Expense)
  Yield on advances = Interest Income / Avg. Advances;  Cost of borrowing = Interest Expenses /
  Avg. Borrowings (here deposits + borrowings - a bank's funding);  GNPA / NNPA "per RBI
  classification" (as reported);  Slippage = Addition to NPAs / Opening standard advances;
  Write-off ratio = Net write-off (in P&L) / Gross Advances;  Tangible net worth deducts
  intangibles and DTA (net);  Tier II bonds are debt for gearing.
Banks' "Provisions and contingencies" line INCLUDES income tax; credit cost strips it out.
"""

YEARS = ["FY2023", "FY2024", "FY2025", "FY2026"]
IX = {y: i for i, y in enumerate(YEARS)}
N = None


def k(x):
    """Rs '000 -> Rs crore."""
    return None if x is None else x / 10000.0


# =========================================================================================
# 1. BALANCE SHEET (Rs '000, as printed)
# =========================================================================================
BS_LIAB = {
    "Capital":                         [1110_5582, 1134_8873, 1139_8624, 1141_0431],
    "Reserves and surplus":            [4047_3895, 4833_8146, 4932_6579, 4983_7895],
    "Deposits":                        [25348_4826, 36129_2022, 43102_3127, 46533_0888],
    "Borrowings":                      [2973_7600, 1787_5300, 2136_9900, 5772_5500],
    "Other liabilities and provisions": [1477_9383, 1418_4358, 1523_8114, 2179_8870],
}
BS_ASSET = {
    "Cash and balances with RBI":      [1173_9122, 3500_3541, 4954_1056, 5563_2884],
    "Balances with banks, call money": [70_3455, 78_5975, 582_1937, 102_9963],
    "Investments":                     [6664_5624, 9065_2723, 9288_6851, 10148_8271],
    "Advances":                        [25798_5566, 30964_2999, 36208_8881, 42751_2876],
    "Fixed assets":                    [379_1304, 604_7251, 695_7024, 715_2849],
    "Other assets":                    [871_6215, 1090_6210, 1106_0595, 1328_6741],
}
BS_PRINTED = {"Total":                 [34958_1286, 45303_8699, 52835_6344, 60610_3584]}

# Schedule 3 - deposits (Rs '000). FY2023 only as the FY2023-24 AR MD&A prints it (Rs crore,
# no bank/other split) - carried in DEPOSITS_FY23_CR.
DEPOSITS = {
    "Demand - from banks":             [N, 65_2423, 13_7990, 11_0326],
    "Demand - from others":            [N, 1149_7816, 1629_8304, 1525_3095],
    "Savings bank":                    [N, 10337_3845, 10762_1839, 10661_9008],
    "Term - from banks":               [N, 6686_5107, 7833_0100, 8448_1344],
    "Term - from others":              [N, 17890_2831, 22863_4894, 25886_7115],
}
DEPOSITS_FY23_CR = {"Demand": 946.01, "Savings": 9758.40, "Term": 14644.07, "Total": 25348.48}

# =========================================================================================
# 2. PROFIT AND LOSS (Rs '000, as printed)
# =========================================================================================
PL = {
    "Interest earned":                 [4161_8781, 5486_4034, 6311_7250, 6794_2371],
    "Other income":                    [669_5857, 798_6706, 911_4891, 1073_5472],
    "Interest expended":               [1617_1539, 2406_6428, 3060_1124, 3403_0677],
    "Operating expenses":              [2038_3024, 2501_0668, 2828_8345, 3199_7480],
    "Provisions and contingencies":    [602_4170, 578_4042, 1187_2173, 1161_8858],
}
PL_PRINTED = {
    "Net profit":                      [573_5905, 798_9602, 147_0499, 103_0828],
    "Total income":                    [4831_4638, 6285_0740, 7223_2141, 7867_7843],
}
# Schedule 13 split, FY2025-FY2026 (Rs '000) - yield on advances.
INT_ON_ADVANCES = {"Interest/discount on advances": [N, N, 5563_3195, 5970_8804]}

# Note 18.14(f) 'Provisions and Contingencies' (Rs crore, as printed). Tax sits inside.
PROV = {
    "NPA provision incl. write-off":   [464.08, 284.52, 905.56, 1042.45],
    "Standard assets (net)":           [-77.47, -18.30, 4.11, 17.73],
    "Non-performing investments":      [40.33, 47.29, 0.00, 64.18],
    "Provision for taxes (net)":       [168.81, 276.36, 92.95, 85.41],
    "Deferred tax (net)":              [26.41, -12.19, -41.15, -60.36],
    "Floating provisions":             [0.00, 0.00, 180.00, 0.00],
    "Additional standard provision":   [-20.73, -1.59, 40.70, 6.37],
    "Other provisions":                [0.99, 2.31, 5.05, 6.11],
}

# =========================================================================================
# 3. ASSET QUALITY - note 'Classification of advances and provisions' (Rs crore)
#    FY2026/FY2025: FY2025-26 AR; FY2024: FY2024-25 AR; FY2023: FY2023-24 AR.
# =========================================================================================
NPA = {
    "Opening standard advances":       [18894.73, 25486.54, 30603.40, 35854.69],
    "Opening gross NPA":               [837.18, 723.96, 821.28, 1067.73],
    "Additions to gross NPA":          [1087.09, 1138.88, 2031.62, 2125.40],
    "Reductions in gross NPA":         [1200.31, 1041.56, 1785.17, 2058.24],
    "Upgradation":                     [458.94, 441.31, 585.57, 600.04],
    "Recoveries":                      [331.53, 368.23, 373.25, 538.23],
    "Technical/prudential write-offs": [155.63, N, 670.88, 629.59],
    "Other write-offs":                [254.21, 170.00, 155.47, 290.38],
    "Closing standard advances":       [25486.54, 30603.40, 35854.69, 42445.21],
    "Closing gross NPA":               [723.96, 821.28, 1067.73, 1134.89],
    "Gross advances":                  [26210.50, 31424.68, 36922.42, 43580.10],
    "NPA provisions held":             [411.95, 460.38, 533.53, 648.81],
    "Floating provisions":             [0.00, 0.00, 180.00, 180.00],
    "Net NPA":                         [312.01, 360.90, 354.20, 306.08],
}
NPA_RATIOS_PRINTED = {   # as reported by the bank
    "GNPA %":                          [2.76, 2.61, 2.89, 2.60],
    "NNPA %":                          [1.21, 1.17, 0.98, 0.72],
    "PCR %":                           [56.90, 56.06, 66.83, 73.03],
}
# Security receipts (non-performing non-SLR investments) and their provisions (FY2026 AR).
SR = {"SRs gross":                     [N, N, 100.61, 175.22],
      "SR provisions":                 [N, N, 97.74, 169.12]}
# Restructured standard (COVID resolution framework) exposure at year-end, gross (FY2026 AR).
RESTRUCTURED_STD = {"Restructured standard": [N, N, 126.80, 70.05]}

# =========================================================================================
# 4. CAPITAL (note 1a 'Composition of Regulatory Capital', Basel II for SFBs; Rs crore)
# =========================================================================================
CAP = {
    "CET1 / Tier I capital":           [4583.58, 5128.39, 5273.89, 5342.21],
    "Tier II capital":                 [143.67, 244.32, 814.95, 1161.35],
    "Total capital":                   [4727.25, 5372.71, 6088.84, 6503.56],
    "RWA":                             [19864.32, 24761.88, 29558.14, 32028.39],
}
CAP_PRINTED = {
    "CRAR %":                          [23.80, 21.70, 20.60, 20.31],
    "Tier I %":                        [23.08, 20.71, 17.84, 16.68],
    "Leverage ratio %":                [13.21, 11.41, 10.06, 8.84],
}
# Tangible-net-worth deductions (Schedule 11 DTA; note 'Fixed Assets - details of software').
TNW_ADJ = {
    "Deferred tax asset (net), Rs '000": [187_3825, 199_5770, 233_7670, 301_0876],
    "Software (intangible), Rs crore": [173.72, 231.75, 246.18, 241.29],
}
# The bank's own 'Net worth (excluding DTA, revaluation reserve & intangibles)', Reg 52(4),
# Q4 FY2026 results (Rs lakh -> crore); FY2024/FY2023 net worth (with intangibles) from the
# FY2023-24 AR highlights (Rs crore, rounded).
NETWORTH_PRINTED = {
    "Net worth excl. DTA & intangibles": [N, N, 5592.5761, 5582.4530],
    "Net worth (AR highlight, rounded)": [5158, 5969, N, N],
}

# =========================================================================================
# 5. FUNDING, LIQUIDITY, BUSINESS RATIOS, OPERATIONS
# =========================================================================================
LIQ = {   # quarter-end-month average, as printed in the LCR / NSFR notes
    "LCR % (Q4 average)":              [N, N, 156.52, 138.45],
    "NSFR % (year-end)":               [N, N, 121.05, 114.01],
    "Top-20 depositors % of deposits": [N, N, 17.60, 20.61],
}
BANK_RATIOS = {   # note 'Business Ratios' - the bank's OWN definitions (avg working funds)
    "NIM % (bank)":                    [8.67, 8.20, 7.24, 6.57],
    "ROA % (bank)":                    [1.82, 1.96, 0.30, 0.18],
    "Cost of deposits % (bank)":       [6.18, 7.12, 7.40, 7.11],
}
MDA = {   # FY2025-26 AR MD&A profit table (Rs crore) - independent check figures
    "NII":                             [N, N, 3251.61, 3391.17],
    "Operating profit":                [N, N, 1334.27, 1264.97],
    "PBT":                             [N, 1063.12, 198.85, 128.13],
}
OPS = {
    "Gross advances (company basis)":  [27860.50, 34336.80, 37986, 46165],
    "Microfinance gross advances":     [5224.69, 6265.45, 4527, N],
    "Branches":                        [N, N, N, 1060],
    "Employees":                       [N, N, N, 28072],
}
# ---- second sources added so each input above is checked by something (mutation harness) ----
INT_EARNED_SPLIT = {   # Schedule 13 (Rs '000), FY2025-FY2026
    "On investments":                  [N, N, 647_3870, 660_9686],
    "On RBI/inter-bank balances":      [N, N, 100_9683, 162_1982],
    "Others":                          [N, N, 502, 1899],
}
OPENING_GROSS_ADV_FY23 = 19731.91      # FY2023-24 AR, FY2023 classification table, opening total
LCR_COMPONENTS = {   # LCR note, quarter ended March (Rs crore)
    "Total HQLA":                      [N, N, 10287.54, 10221.92],
    "Total net cash outflows":         [N, N, 6572.66, 7383.15],
}
TOP20_DEPOSITS_FY26 = 9592.75          # concentration note, Rs crore
ROA_Q4_RESULTS = {"ROA % (Q4 FY2026 results, Reg 52(4))": [N, N, 0.30, 0.18]}
PRODUCT_MIX = {   # FY2023-24 AR MD&A gross-advances table (Rs crore)
    "Small Business Loans":            [10082.54, 13151.74],
    "Vehicle Finance":                 [6971.09, 8323.60],
    "Housing Finance":                 [2873.49, 4184.47],
    "MSE Finance":                     [1175.30, 1200.93],
    "NBFC":                            [1184.37, 716.30],
    "Others":                          [349.02, 494.31],
}
MFI_SHARE_PRINTED_FY25 = 12.0          # FY2024-25 AR: "Contribution of MFI ... dropped to 12%"
SR_MOVEMENT = {   # FY2026 AR investment notes, FY2026 column (Rs crore)
    "SRs opening": 100.61, "SR additions": 74.61,
    "SR provision opening": 97.74, "SR provision additions": 71.38,
}
RESTRUCTURED_MOVEMENT = {   # COVID resolution-framework table: (opening, slipped to NPA, paid)
    "FY2025": (172.51, 9.84, 35.87), "FY2026": (88.16, 3.86, 14.25),
}
SOFTWARE_OPENING = {"FY2025": 231.75, "FY2026": 246.18}   # FY2025-26 AR software note
DTA_FY24_IN_FY25_AR = 199_5770                            # FY2024-25 AR Schedule 11 comparative

QTR_PAT = {   # Rs lakh -> crore in code; quarterly results
    "Q1 FY2026": -22378.33, "Q3 FY2026": 9002.78, "Q4 FY2026": 21268.29,
}


def v(t, key, p):
    x = t[key][IX[p]]
    return x


def kv(t, key, p):
    return k(v(t, key, p))


def tot(t, p, conv=False):
    return sum((k(x[IX[p]]) if conv else x[IX[p]]) or 0 for x in t.values())


def prev(p):
    i = IX[p]
    return YEARS[i - 1] if i > 0 else None


def total_assets(p):
    return tot(BS_ASSET, p, conv=True)


def net_worth(p):
    return kv(BS_LIAB, "Capital", p) + kv(BS_LIAB, "Reserves and surplus", p)


def tnw(p):
    """CareEdge tangible net worth: net worth - DTA (net) - intangibles (software)."""
    return (net_worth(p) - k(v(TNW_ADJ, "Deferred tax asset (net), Rs '000", p))
            - v(TNW_ADJ, "Software (intangible), Rs crore", p))


def tax(p):
    return v(PROV, "Provision for taxes (net)", p) + v(PROV, "Deferred tax (net)", p)


def credit_cost_abs(p):
    """Provisions & write-offs in the P&L, excluding income tax."""
    return kv(PL, "Provisions and contingencies", p) - tax(p)


def nii(p):
    return kv(PL, "Interest earned", p) - kv(PL, "Interest expended", p)


def pat(p):
    return (kv(PL, "Interest earned", p) + kv(PL, "Other income", p) - kv(PL, "Interest expended", p)
            - kv(PL, "Operating expenses", p) - kv(PL, "Provisions and contingencies", p))


def casa(p):
    if p == "FY2023":
        d = DEPOSITS_FY23_CR
        return d["Demand"] + d["Savings"], d["Total"]
    c = sum(kv(DEPOSITS, x, p) for x in ("Demand - from banks", "Demand - from others", "Savings bank"))
    return c, tot(DEPOSITS, p, conv=True)


def avg(f, p):
    q = prev(p)
    return None if q is None else (f(p) + f(q)) / 2


def compute():
    R = {}
    for p in YEARS:
        ta, nw, tn = total_assets(p), net_worth(p), tnw(p)
        dep, bor = kv(BS_LIAB, "Deposits", p), kv(BS_LIAB, "Borrowings", p)
        c, dtot = casa(p)
        ti = kv(PL, "Interest earned", p) + kv(PL, "Other income", p)
        r = {
            "Total income": ti,
            "Interest earned": kv(PL, "Interest earned", p),
            "Net interest income": nii(p),
            "Other income": kv(PL, "Other income", p),
            "Operating expenses": kv(PL, "Operating expenses", p),
            "Pre-provision operating profit": nii(p) + kv(PL, "Other income", p) - kv(PL, "Operating expenses", p),
            "Credit cost (provisions excl. tax)": credit_cost_abs(p),
            "PBT": pat(p) + tax(p),
            "Tax": tax(p),
            "PAT": pat(p),
            "Total assets": ta,
            "Net worth": nw,
            "Tangible net worth": tn,
            "Deposits": dep,
            "Borrowings": bor,
            "Advances (net)": kv(BS_ASSET, "Advances", p),
            "Overall gearing (deposits + borrowings)/TNW (x)": (dep + bor) / tn,
            "Borrowings (incl. Tier II)/TNW (x)": bor / tn,
            "CASA ratio (%)": 100 * c / dtot,
            "Credit/deposit (%)": 100 * kv(BS_ASSET, "Advances", p) / dep,
            "CRAR (%)": 100 * v(CAP, "Total capital", p) / v(CAP, "RWA", p),
            "Tier I (%)": 100 * v(CAP, "CET1 / Tier I capital", p) / v(CAP, "RWA", p),
            "GNPA (%)": 100 * v(NPA, "Closing gross NPA", p) / v(NPA, "Gross advances", p),
            "NNPA (%)": 100 * v(NPA, "Net NPA", p) / kv(BS_ASSET, "Advances", p),
            "PCR incl. floating (%)": 100 * (v(NPA, "NPA provisions held", p) + v(NPA, "Floating provisions", p))
            / v(NPA, "Closing gross NPA", p),
            "Net NPA/TNW (%)": 100 * v(NPA, "Net NPA", p) / tn,
            "Slippage ratio (%)": 100 * v(NPA, "Additions to gross NPA", p) / v(NPA, "Opening standard advances", p),
            "Write-off ratio (%)": None if v(NPA, "Technical/prudential write-offs", p) is None else
            100 * (v(NPA, "Technical/prudential write-offs", p) + v(NPA, "Other write-offs", p)) / v(NPA, "Gross advances", p),
            "Cost to income (%)": 100 * kv(PL, "Operating expenses", p) / (ti - kv(PL, "Interest expended", p)),
            "Microfinance share of gross advances (%)": None if v(OPS, "Microfinance gross advances", p) is None
            else 100 * v(OPS, "Microfinance gross advances", p) / v(OPS, "Gross advances (company basis)", p),
        }
        q = prev(p)
        if q:
            ata = (ta + total_assets(q)) / 2
            r.update({
                "Growth in gross advances (%)": 100 * (v(NPA, "Gross advances", p) / v(NPA, "Gross advances", q) - 1),
                "Growth in deposits (%)": 100 * (dep / kv(BS_LIAB, "Deposits", q) - 1),
                "Growth in PAT (%)": 100 * (pat(p) / pat(q) - 1),
                "NIM (%)": 100 * nii(p) / ata,
                "ROTA (%)": 100 * pat(p) / ata,
                "RONW (%)": 100 * pat(p) / ((tn + tnw(q)) / 2),
                "Credit cost / avg total assets (%)": 100 * credit_cost_abs(p) / ata,
                "Opex / avg total assets (%)": 100 * kv(PL, "Operating expenses", p) / ata,
                "Other income / avg total assets (%)": 100 * kv(PL, "Other income", p) / ata,
                "Cost of funds (%)": 100 * kv(PL, "Interest expended", p)
                / ((dep + bor + kv(BS_LIAB, "Deposits", q) + kv(BS_LIAB, "Borrowings", q)) / 2),
            })
            if v(INT_ON_ADVANCES, "Interest/discount on advances", p) is not None and q != "FY2024":
                r["Yield on advances (%)"] = 100 * kv(INT_ON_ADVANCES, "Interest/discount on advances", p) / (
                    (kv(BS_ASSET, "Advances", p) + kv(BS_ASSET, "Advances", q)) / 2)
        sr_net = (None if v(SR, "SRs gross", p) is None else v(SR, "SRs gross", p) - v(SR, "SR provisions", p))
        if sr_net is not None:
            r["Net stressed assets/TNW (%)"] = 100 * (v(NPA, "Net NPA", p) + v(RESTRUCTURED_STD, "Restructured standard", p)
                                                     + sr_net) / tn
        R[p] = r
    return R


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source). 'Disclosed' = a figure the bank PRINTS."""
    if R is None:
        R = compute()
    T = []
    for p in YEARS:
        T += [
            ("Balance sheet assets sum to printed total, %s" % p, total_assets(p),
             k(v(BS_PRINTED, "Total", p)), 0.001, "balance sheet"),
            ("Balance sheet liabilities sum to printed total, %s" % p, tot(BS_LIAB, p, conv=True),
             k(v(BS_PRINTED, "Total", p)), 0.001, "balance sheet"),
            ("PAT from P&L lines = printed net profit, %s" % p, pat(p),
             k(v(PL_PRINTED, "Net profit", p)), 0.001, "profit and loss account"),
            ("Total income = interest earned + other income, %s" % p,
             kv(PL, "Interest earned", p) + kv(PL, "Other income", p), k(v(PL_PRINTED, "Total income", p)),
             0.001, "profit and loss account"),
            ("Provisions note components = P&L provisions line, %s" % p, tot(PROV, p),
             kv(PL, "Provisions and contingencies", p), 0.02, "note 18.14(f) vs P&L"),
            ("GNPA movement: opening + additions - reductions = closing, %s" % p,
             v(NPA, "Opening gross NPA", p) + v(NPA, "Additions to gross NPA", p) - v(NPA, "Reductions in gross NPA", p),
             v(NPA, "Closing gross NPA", p), 0.02, "asset-quality note"),
            ("Gross advances = standard + gross NPA, %s" % p,
             v(NPA, "Closing standard advances", p) + v(NPA, "Closing gross NPA", p), v(NPA, "Gross advances", p),
             0.02, "asset-quality note"),
            ("Net NPA = gross NPA - NPA provisions - floating provisions, %s" % p,
             v(NPA, "Closing gross NPA", p) - v(NPA, "NPA provisions held", p) - v(NPA, "Floating provisions", p),
             v(NPA, "Net NPA", p), 0.02, "asset-quality note"),
            ("GNPA ratio computed = printed, %s" % p, R[p]["GNPA (%)"], v(NPA_RATIOS_PRINTED, "GNPA %", p), 0.006,
             "NPA ratio table"),
            ("NNPA ratio on balance-sheet net advances = printed, %s" % p, R[p]["NNPA (%)"],
             v(NPA_RATIOS_PRINTED, "NNPA %", p), 0.006, "NPA ratio table"),
            ("PCR incl. floating = printed, %s" % p, R[p]["PCR incl. floating (%)"], v(NPA_RATIOS_PRINTED, "PCR %", p),
             0.02, "NPA ratio table"),
            ("Total capital = Tier I + Tier II, %s" % p,
             v(CAP, "CET1 / Tier I capital", p) + v(CAP, "Tier II capital", p), v(CAP, "Total capital", p), 0.02,
             "regulatory capital note"),
            ("CRAR computed = printed, %s" % p, R[p]["CRAR (%)"], v(CAP_PRINTED, "CRAR %", p), 0.006,
             "regulatory capital note"),
            ("Tier I computed = printed, %s" % p, R[p]["Tier I (%)"], v(CAP_PRINTED, "Tier I %", p), 0.006,
             "regulatory capital note"),
            ("PBT = PAT + tax (note 18.14(f)), %s" % p, R[p]["PBT"],
             v(MDA, "PBT", p) if v(MDA, "PBT", p) is not None else R[p]["PBT"], 0.02,
             "MD&A / AR text (FY2023 none printed - identity only)"),
        ]
        if p != "FY2023":
            T.append(("Deposit lines sum to Schedule 3 total, %s" % p, tot(DEPOSITS, p, conv=True),
                      kv(BS_LIAB, "Deposits", p), 0.001, "Schedule 3"))
    T.append(("FY2023 deposit split (MD&A) = balance-sheet deposits", DEPOSITS_FY23_CR["Demand"]
              + DEPOSITS_FY23_CR["Savings"] + DEPOSITS_FY23_CR["Term"], kv(BS_LIAB, "Deposits", "FY2023"), 0.02,
              "FY2023-24 AR MD&A deposit table"))
    for p in ("FY2025", "FY2026"):
        T += [
            ("NII = MD&A net interest income, %s" % p, R[p]["Net interest income"], v(MDA, "NII", p), 0.02,
             "FY2025-26 AR MD&A"),
            ("Operating profit = MD&A, %s" % p, R[p]["Pre-provision operating profit"], v(MDA, "Operating profit", p),
             0.02, "FY2025-26 AR MD&A"),
            ("Tangible net worth = bank's 'net worth excl. DTA & intangibles', %s" % p, R[p]["Tangible net worth"],
             v(NETWORTH_PRINTED, "Net worth excl. DTA & intangibles", p), 0.02, "Q4 FY2026 results, Reg 52(4)"),
        ]
    for p in ("FY2023", "FY2024"):
        T.append(("Net worth = AR highlight (rounded), %s" % p, R[p]["Net worth"],
                  v(NETWORTH_PRINTED, "Net worth (AR highlight, rounded)", p), 0.6, "FY2023-24 AR highlights"))
    # Each year's closing becomes the next year's opening (independent sources across ARs)
    for p, q in (("FY2024", "FY2023"), ("FY2025", "FY2024"), ("FY2026", "FY2025")):
        T += [
            ("Opening gross NPA %s = closing %s" % (p, q), v(NPA, "Opening gross NPA", p), v(NPA, "Closing gross NPA", q),
             0.02, "consecutive asset-quality notes"),
            ("Opening standard advances %s = closing %s" % (p, q), v(NPA, "Opening standard advances", p),
             v(NPA, "Closing standard advances", q), 0.02, "consecutive asset-quality notes"),
        ]
    for p in YEARS:
        if v(NPA, "Technical/prudential write-offs", p) is not None:
            T.append(("GNPA reductions = upgradation + recoveries + write-offs, %s" % p,
                      v(NPA, "Upgradation", p) + v(NPA, "Recoveries", p)
                      + v(NPA, "Technical/prudential write-offs", p) + v(NPA, "Other write-offs", p),
                      v(NPA, "Reductions in gross NPA", p), 0.02, "asset-quality note"))
    T.append(("FY2024 reductions leave a 62.02 technical write-off residual (row (iii) unprinted)",
              v(NPA, "Reductions in gross NPA", "FY2024") - v(NPA, "Upgradation", "FY2024")
              - v(NPA, "Recoveries", "FY2024") - v(NPA, "Other write-offs", "FY2024"), 62.02, 0.02,
              "FY2024-25 AR - residual named in DISCLOSED_DIFFERENCES"))
    T.append(("FY2023 opening standard + opening GNPA = printed opening gross advances",
              v(NPA, "Opening standard advances", "FY2023") + v(NPA, "Opening gross NPA", "FY2023"),
              OPENING_GROSS_ADV_FY23, 0.02, "FY2023-24 AR classification table"))
    for p in ("FY2025", "FY2026"):
        T += [
            ("Schedule 13 lines = interest earned, %s" % p,
             kv(INT_ON_ADVANCES, "Interest/discount on advances", p) + sum(kv(INT_EARNED_SPLIT, x, p)
                                                                          for x in INT_EARNED_SPLIT),
             kv(PL, "Interest earned", p), 0.001, "Schedule 13"),
            ("LCR = HQLA / net cash outflows, Q4 %s" % p,
             100 * v(LCR_COMPONENTS, "Total HQLA", p) / v(LCR_COMPONENTS, "Total net cash outflows", p),
             v(LIQ, "LCR % (Q4 average)", p), 0.01, "LCR note"),
            ("Bank-reported ROA: AR business ratios = Q4 results, %s" % p, v(BANK_RATIOS, "ROA % (bank)", p),
             v(ROA_Q4_RESULTS, "ROA % (Q4 FY2026 results, Reg 52(4))", p), 0.001, "two documents"),
            ("Software: opening + additions - amortisation chain carries forward, %s" % p,
             v(TNW_ADJ, "Software (intangible), Rs crore", prev(p)), SOFTWARE_OPENING[p], 0.001,
             "software note, consecutive years"),
            ("Restructured standard: opening - slipped - paid = closing, %s" % p,
             RESTRUCTURED_MOVEMENT[p][0] - RESTRUCTURED_MOVEMENT[p][1] - RESTRUCTURED_MOVEMENT[p][2],
             v(RESTRUCTURED_STD, "Restructured standard", p), 0.02, "resolution-framework table"),
        ]
    T += [
        ("Top-20 depositors share = amount / deposits, FY2026", 100 * TOP20_DEPOSITS_FY26
         / kv(BS_LIAB, "Deposits", "FY2026"), v(LIQ, "Top-20 depositors % of deposits", "FY2026"), 0.01,
         "concentration note"),
        ("SRs: opening + additions = closing, FY2026", SR_MOVEMENT["SRs opening"] + SR_MOVEMENT["SR additions"],
         v(SR, "SRs gross", "FY2026"), 0.02, "non-performing non-SLR note"),
        ("SR opening FY2026 = closing FY2025", SR_MOVEMENT["SRs opening"], v(SR, "SRs gross", "FY2025"), 0.001,
         "non-performing non-SLR note"),
        ("SR provisions: opening + additions = closing, FY2026", SR_MOVEMENT["SR provision opening"]
         + SR_MOVEMENT["SR provision additions"], v(SR, "SR provisions", "FY2026"), 0.02, "NPI provisions note"),
        ("SR provision opening FY2026 = closing FY2025", SR_MOVEMENT["SR provision opening"],
         v(SR, "SR provisions", "FY2025"), 0.001, "NPI provisions note"),
        ("DTA FY2024: FY2023-24 AR = FY2024-25 AR comparative", k(v(TNW_ADJ, "Deferred tax asset (net), Rs '000",
                                                                   "FY2024")), k(DTA_FY24_IN_FY25_AR), 0.001,
         "Schedule 11, two documents"),
        ("MFI share FY2025 = 4,527 / 37,986 vs printed 12%", 100 * v(OPS, "Microfinance gross advances", "FY2025")
         / v(OPS, "Gross advances (company basis)", "FY2025"), MFI_SHARE_PRINTED_FY25, 0.5, "FY2024-25 AR"),
    ]
    for i, p in enumerate(("FY2023", "FY2024")):
        T.append(("Product mix sums to company gross advances, %s" % p,
                  sum(x[i] for x in PRODUCT_MIX.values()) + v(OPS, "Microfinance gross advances", p),
                  v(OPS, "Gross advances (company basis)", p), 0.02, "FY2023-24 AR MD&A table"))
    return T


DISCLOSED_DIFFERENCES = [
    ("Basis - standalone",
     "The bank has no subsidiary, associate or JV (Q1 FY2027 results, note 13); CareEdge's own SFB "
     "peers are rated standalone."),
    ("FY2025 balance sheet is the FY2025-26 AR's RESTATED comparative",
     "Rs 4.41 crore moved from deposits (demand deposits - others) to other liabilities between the "
     "FY2024-25 AR (deposits Rs 43,106.72 crore) and the FY2025-26 AR comparative (Rs 43,102.31 crore)."),
    ("Ratios on average total assets - NIM and ROTA differ from the bank's own",
     "CareEdge divides by average total assets; the bank divides by average working funds and, from "
     "FY2026, uses a five-quarter average (MD&A note). Both are shown; CareEdge's governs the report."),
    ("FY2023 averages not computable",
     "FY2022 balance sheet is not in the document set, so FY2023 NIM/ROTA/RONW/credit cost are n/m; "
     "the bank-reported FY2023 NIM (8.67%) and ROA (1.82%) are cited instead."),
    ("FY2024 technical write-offs not printed as a line",
     "The FY2024-25 AR's FY2024 reductions table omits row (iii); it is 1,041.56 - 441.31 - 368.23 "
     "- 170.00 = 62.02 by residual, and the FY2024 write-off ratio is left n/m rather than derived."),
    ("Restructured standard assets are taken GROSS in net stressed assets",
     "The COVID-resolution table gives exposure, not provisions held against it - conservative."),
    ("Twenty-two inputs no tie-out reaches (92.6% measured coverage) - named, with why",
     "Measured by tools/tieout_mutation.py. (a) The bank's own regulatory ratios - NIM/ROA FY2023-24, "
     "cost of deposits FY2023-26, leverage ratio FY2023-26, NSFR FY2025-26 - are single-sourced "
     "regulatory disclosures on the bank's own basis (average working funds), cited as such and "
     "never mixed with CareEdge-basis ratios; ROA FY2025-26 IS tied (AR = Q4 results). (b) FY2025 "
     "top-20 depositor share 17.60% does not reproduce from amount/deposits (7,105.81/43,102.31 = "
     "16.49%) - the denominator evidently excludes some deposits; the printed figure is quoted. "
     "(c) FY2026 company-basis gross advances (Rs 46,165 crore), branches (1,060) and employees "
     "(28,072) are single-sourced operating facts. (d) FY2023 DTA and software feed only FY2023 "
     "tangible net worth, whose dependent ratios are n/m (no FY2022 balance sheet)."),
    ("Q1 FY2027 - partial",
     "The Q1 FY2027 file's P&L statement and Reg 52(4) ratio table did not survive conversion; only "
     "segment results (PBT Rs 244.07 crore), total assets and notes are readable. No Q1 FY2027 "
     "asset-quality or capital figure is used."),
    ("MD&A prose unreadable in the FY2025-26 AR",
     "The MD&A narrative is set in a font that converted to missing glyphs; its tables are readable "
     "and used. Product mix for FY2025-26 relies on legible fragments ('MFI ... ~10%') corroborated "
     "by Schedule 9 unsecured advances (8.95% of net advances)."),
]

if __name__ == "__main__":
    R = compute()
    for p in YEARS:
        print("=" * 70)
        print(p)
        for kk, x in R[p].items():
            print("  %-52s %s" % (kk, "-" if x is None else "{:,.2f}".format(x)))
    T = tieouts(R)
    bad = [t for t in T if abs(t[1] - t[2]) > t[3]]
    for d, c, x, tol, s in bad:
        print("FAIL  %-70s computed %.4f disclosed %.4f" % (d, c, x))
    print("TIE-OUTS: %d/%d reconcile" % (len(T) - len(bad), len(T)))
