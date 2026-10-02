"""Generates Yasho Industries Limited_Financial_Spreads.xlsx (standing Step 5 deliverable).
All inputs traced; all ratios written as live Excel formulas off the Inputs sheet.
Figures Rs CRORE (source unit Rs lakh, converted once at extraction)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads          # noqa: E402

Y = ["FY2024", "FY2025", "FY2026"]
AR26 = "FY26 AR, consolidated/standalone as noted"
MDA = "FY26 AR MD&A 'Key Financials' L1226-1276"

INPUTS = [
    ("Revenue from operations",            [595.70, 675.64, 830.03],  f"{AR26} P&L L8550 (consol); FY24 standalone"),
    ("EBITDA (as disclosed)",              [106.67, 119.40, 144.46],  f"{MDA}; FY24 derived PBT+D+I"),
    ("Profit before tax",                  [76.34, 8.34, 33.97],      f"{AR26} consolidated P&L"),
    ("PAT (consolidated)",                 [57.12, 6.02, 25.26],      f"{AR26} consolidated P&L L8589"),
    ("Depreciation & amortisation",        [15.62, 50.06, 54.77],     f"{AR26} P&L L5261"),
    ("Finance costs",                      [14.71, 58.81, 55.56],     f"{AR26} P&L"),
    ("Borrowings - non current",           [333.65, 324.45, 289.13],  f"{AR26} BS Note 15"),
    ("Borrowings - current",               [214.79, 234.07, 251.81],  f"{AR26} BS Note 20"),
    ("Lease liabilities - non current",    [21.11, 12.48, 6.74],      f"{AR26} BS"),
    ("Lease liabilities - current",        [9.49, 11.56, 10.25],      f"{AR26} BS"),
    ("Total equity (networth)",            [293.36, 420.60, 441.31],  f"{AR26} BS; FY25 incl Rs 125cr pref allotment"),
    ("Total assets",                       [991.68, 1093.34, 1160.12], f"{AR26} BS"),
    ("Trade receivables",                  [124.71, 147.44, 201.93],  f"{AR26} BS"),
    ("Inventories",                        [124.96, 245.13, 235.05],  f"{AR26} BS"),
    ("Trade payables",                     [47.87, 62.78, 97.21],     f"{AR26} BS"),
    ("Cash flow from operations",          [89.99, 45.03, 151.08],    f"{AR26} Cash Flow Statement"),
    ("Capital expenditure (cash)",         [336.99, 11.15, 73.84],    f"{AR26} CFS investing; FY24 = Pakhajan greenfield"),
    ("Director/KMP unsecured loans",       [None, 48.51, 47.00],      f"{AR26} RPT note - CRISIL Box 1 treatment applies"),
    ("Capacity utilisation (Pakhajan)",    [None, None, 0.60],        "Q4FY26 deck narrative ~60%; >65% in Q1FY27"),
]
R = {lab: 6 + i for i, (lab, _, _) in enumerate(INPUTS)}


def I(label):
    return "Inputs!{c}%d" % R[label]


def _f(expr):
    return "=" + expr


DEBT = f"({I('Borrowings - non current')}+{I('Borrowings - current')})"
LEASE = f"({I('Lease liabilities - non current')}+{I('Lease liabilities - current')})"
ADJ_DEBT = f"({DEBT}+{LEASE})"

RATIOS = [
    ("EBITDA margin %", _f(f"{I('EBITDA (as disclosed)')}/{I('Revenue from operations')}"),
     "EBITDA / operating revenue", "0.0%"),
    ("PAT margin %", _f(f"{I('PAT (consolidated)')}/{I('Revenue from operations')}"),
     "PAT / operating revenue - CRISIL's KI-table convention", "0.00%"),
    ("Borrowings (excl leases)", _f(DEBT), "Non-current + current borrowings", "#,##0.00"),
    ("Lease liabilities", _f(LEASE), "Ind AS 116 lease liabilities", "#,##0.00"),
    ("CRISIL adjusted debt", _f(ADJ_DEBT),
     "CRISIL adjusted-debt convention includes lease liabilities", "#,##0.00"),
    ("Gearing (adj debt / adj NW) x", _f(f"{ADJ_DEBT}/{I('Total equity (networth)')}"),
     "CRISIL core ratio 1: adjusted total debt / adjusted networth", '0.00"x"'),
    ("TOL / TNW x",
     _f(f"({I('Total assets')}-{I('Total equity (networth)')})/{I('Total equity (networth)')}"),
     "CRISIL core ratio 2: total outside liabilities / adjusted networth", '0.00"x"'),
    ("Adjusted debt / EBITDA x", _f(f"{ADJ_DEBT}/{I('EBITDA (as disclosed)')}"),
     "CRISIL case-to-case alternative to NCATD", '0.00"x"'),
    ("Interest coverage (PBDIT/int) x",
     _f(f"{I('EBITDA (as disclosed)')}/{I('Finance costs')}"),
     "CRISIL core ratio 3: PBDIT / interest and finance charges", '0.00"x"'),
    ("EBIT / interest x  [MD&A basis]",
     _f(f"({I('EBITDA (as disclosed)')}-{I('Depreciation & amortisation')})/{I('Finance costs')}"),
     "Company's own MD&A convention - reconciles to disclosed 1.61x FY26", '0.00"x"'),
    ("NCATD %",
     _f(f"({I('PAT (consolidated)')}+{I('Depreciation & amortisation')})/{ADJ_DEBT}"),
     "CRISIL core ratio: net cash accrual / adjusted total debt", "0.0%"),
    ("RoCE %",
     _f(f"({I('EBITDA (as disclosed)')}-{I('Depreciation & amortisation')})"
        f"/({ADJ_DEBT}+{I('Total equity (networth)')})"),
     "PBIT / (total debt + adjusted networth)", "0.0%"),
    ("Receivable days", _f(f"365*{I('Trade receivables')}/{I('Revenue from operations')}"),
     "365 x trade receivables / revenue", "0"),
    ("Inventory days", _f(f"365*{I('Inventories')}/{I('Revenue from operations')}"),
     "365 x inventories / revenue", "0"),
    ("Payable days", _f(f"365*{I('Trade payables')}/{I('Revenue from operations')}"),
     "365 x trade payables / revenue", "0"),
    ("Net working capital days",
     _f(f"365*({I('Trade receivables')}+{I('Inventories')}-{I('Trade payables')})"
        f"/{I('Revenue from operations')}"),
     "THE sector-critical metric - working capital intensity (company: 190->143 days Q1FY27)", "0"),
    ("Free cash flow",
     _f(f"{I('Cash flow from operations')}-{I('Capital expenditure (cash)')}"),
     "CFO less cash capex", "#,##0.00"),
    ("Capex / revenue %",
     _f(f"{I('Capital expenditure (cash)')}/{I('Revenue from operations')}"),
     "Capital intensity - FY24 spike is the Pakhajan greenfield", "0.0%"),
]

TIEOUTS = [
    ("FY26 gearing vs MD&A 'Debt/Equity 1.26'",
     "=(Inputs!E%d+Inputs!E%d+Inputs!E%d+Inputs!E%d)/Inputs!E%d" % (
         R["Borrowings - non current"], R["Borrowings - current"],
         R["Lease liabilities - non current"], R["Lease liabilities - current"],
         R["Total equity (networth)"]), 1.26,
     "Company's own MD&A ratio table - exact match"),
    ("FY26 EBIT/interest vs MD&A 'Interest Coverage 1.61'",
     "=(Inputs!E%d-Inputs!E%d)/Inputs!E%d" % (
         R["EBITDA (as disclosed)"], R["Depreciation & amortisation"], R["Finance costs"]), 1.61,
     "Company's own MD&A ratio table - exact match, confirms EBITDA and depreciation"),
    ("FY26 borrowings vs Q4FY26 deck bar chart",
     "=Inputs!E%d+Inputs!E%d" % (R["Borrowings - non current"], R["Borrowings - current"]), 540.94,
     "Deck shows LT 305.2 + ST 235.7 = Rs 540.9 cr - balance sheet ties to the deck"),
    ("FY26 revenue vs Q4FY26 deck",
     "=Inputs!E%d" % R["Revenue from operations"], 830.03,
     "Company-disclosed FY26 consolidated revenue"),
    ("FY26 EBITDA vs Q4FY26 deck",
     "=Inputs!E%d" % R["EBITDA (as disclosed)"], 144.46,
     "Deck EBITDA Rs 144.46 cr; independently derived PBT+D+I gives 144.29 - 0.1% variance"),
]

SCORE = {
    "factors": [
        ("Industry / operating environment", 3, 0.20,
         "Speciality chemicals: CRISIL's chemical-industry criteria favours speciality over bulk "
         "(proprietary technology, sticky post-qualification customer relationships, low share of "
         "customer's cost base, less pronounced cycles). Offset by exposure to crude-linked raw "
         "material volatility, Chinese competition on price, and export-market tariff risk which "
         "demonstrably suppressed utilisation through Q2-Q3 FY26."),
        ("Market position", 3, 0.20,
         "Rs 830 crore revenue (FY26) across 140+ products in five verticals; ~62-65% exports to "
         "USA, Europe, Asia, Middle East. Two plants (Vapi, Pakhajan) with combined peak revenue "
         "capacity of Rs 1,450-1,550 crore. Positive: a 15-year lubricant-additives supply "
         "agreement with a global MNC, fully customer-funded (Rs 85-90 crore project cost, Rs 98 "
         "crore of advances received). Negative: customer-concentration percentages are NOT "
         "disclosed in any supplied document, and the Consumer division has compressed from 17% "
         "to 11% of revenue in two years without management explanation."),
        ("Financial risk profile", 4, 0.45,
         "The binding constraint. Gearing 1.26x and TOL/TNW 1.63x remain elevated; adjusted "
         "debt/EBITDA 3.86x (FY26) and interest coverage of just 2.60x (PBDIT basis) / 1.61x "
         "(EBIT basis) are weak for the mid-BBB/A- boundary. Working capital is heavy - 152 net "
         "days FY26, receivable days deteriorating 76->80->90. Mitigants are real and improving: "
         "FY26 CFO of Rs 151 crore, positive FCF of Rs 77 crore, adjusted debt down Rs 25 crore, "
         "and a Rs 125 crore FY25 equity infusion. Q1FY27 marks a step-change - Rs 307.74 crore "
         "revenue (48% annualised run-rate uplift), 24.2% EBITDA margin, company-reported "
         "debt/EBITDA of 1.86x, working capital cut to 143 days."),
        ("Management & governance", 3, 0.15,
         "Promoter-led (Jhaveri family, 67.91%), three decades of sector operating history, "
         "unmodified audit opinions in all three years with no Emphasis of Matter. Watch items: "
         "recurring director/KMP unsecured loans of Rs 47 crore (CRISIL Box 1 - treated as debt "
         "here, not equity, absent evidence of formal subordination); CSR consistently underspent "
         "and deferred to the statutory unspent account in both FY25 and FY26; FY26 Scope 1/2 GHG "
         "emissions marked 'Under Process' in the company's own BRSR, a latest-year disclosure gap."),
    ],
    "anchor": "BBB+ / A- boundary (weighted composite 3.45 - upper-BBB, transitioning)",
    "view": "Crisil A-/Stable  ·  Crisil A2+",
    "divergence": "None against the CURRENT agency action. CRITICAL STEP-14 NOTE: the reference "
                  "library's CRISIL file (11-Feb-2026 Credit Bulletin) shows Crisil BBB+/Positive "
                  "and Crisil A2 - this is SUPERSEDED. The issuer's own Q1FY27 investor "
                  "presentation states verbatim: 'Bank Loan Ratings of the Company has been "
                  "upgraded/assigned by CRISIL and ICRA from BBB+ to A-.' The current CRISIL "
                  "rating is therefore A-, and this assessment converges on it independently: the "
                  "FY26 deleveraging (gearing 1.97->1.26x, adj debt/EBITDA 5.43->3.86x), the swing "
                  "to positive FCF, and the Q1FY27 step-change in scale and margin together "
                  "support a one-notch upgrade from BBB+. Had the superseded library file been "
                  "taken as the anchor, this report would have published BBB+ - repeating the "
                  "Indus Towers failure exactly (CLAUDE.md failure mode 24).",
}

if __name__ == "__main__":
    out = build_spreads(
        company="Yasho Industries Limited", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE,
        out="Yasho Industries Limited_Financial_Spreads.xlsx")
    print("Saved:", out)
