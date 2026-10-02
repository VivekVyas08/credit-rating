"""Generates Riba Textiles Limited_Financial_Spreads.xlsx (CLAUDE.md Step 5 deliverable).

CareEdge convention: PBILDT as the earnings measure, overall AND net overall gearing reported
separately, TOL/TNW, interest coverage in times. Rs CRORE (source Rs lakhs, converted once).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads          # noqa: E402

Y = ["FY2023", "FY2024", "FY2025"]
A25 = "AR FY2024-25 (998.md)"
A24 = "AR FY2023-24 (973.md) comparative"

INPUTS = [
    ("Revenue from operations",   [None, 246.89, 295.86],  f"{A25} P&L L~3095"),
    ("Other income",              [None, 0.31, 0.27],      f"{A25} P&L L~3096"),
    ("Total income",              [242.83, 247.21, 296.13], f"{A24} L3164; {A25} L~3097"),
    ("Depreciation",              [4.47, 4.79, 5.47],      f"{A24} L3170; {A25} L~3109"),
    ("Finance cost",              [4.49, 4.65, 5.89],      f"{A24} L3171; {A25} L~3110"),
    ("Profit before tax",         [9.74, 10.60, 11.16],    f"{A24} L3177; {A25} L~3120"),
    ("Profit after tax",          [7.40, 7.92, 8.50],      f"{A24} L3182; {A25} L3121"),
    ("Borrowings - non-current",  [26.12, 25.38, 25.74],   f"{A24} L3120; {A25} L3060"),
    ("Borrowings - current",      [34.68, 42.30, 35.65],   f"{A24} L3124; {A25} L3064"),
    ("Cash + other bank balances", [None, 4.77, 2.54],     f"{A25} L~3046-3047"),
    ("Tangible net worth",        [81.48, 89.40, 97.90],   "Equity share capital + reserves"),
    ("Total assets",              [164.21, 179.08, 181.45], f"{A24} L3110; {A25} L3067"),
    ("Inventories",               [None, 25.68, 25.16],    f"{A25} L3042"),
    ("Trade receivables",         [None, 41.59, 36.22],    f"{A25} L3044"),
    ("Current assets",            [None, 82.63, 75.89],    f"{A25} L~3050"),
    ("Current liabilities",       [None, 61.99, 54.91],    f"{A25} L3068"),
]
R = {lab: 6 + i for i, (lab, _, _) in enumerate(INPUTS)}


def I(label):
    return "Inputs!{c}%d" % R[label]


def _f(e):
    return "=" + e


RATIOS = [
    ("PBILDT",
     _f(f"{I('Profit before tax')}+{I('Finance cost')}+{I('Depreciation')}-{I('Other income')}"),
     "CareEdge earnings measure. No lease liabilities on the balance sheet in any year, so "
     "PBILDT equals PBDIT here - absence recorded, not assumed", "#,##0.00"),
    ("PBILDT margin (%)",
     _f(f"({I('Profit before tax')}+{I('Finance cost')}+{I('Depreciation')}-{I('Other income')})"
        f"/{I('Total income')}"),
     "THE CORE WEAKNESS: thin and slipping", "0.00%"),
    ("PAT margin (%)",
     _f(f"{I('Profit after tax')}/{I('Total income')}"), "Profit after tax over income", "0.00%"),
    ("Total debt",
     _f(f"{I('Borrowings - non-current')}+{I('Borrowings - current')}"),
     "Non-current plus current borrowings", "#,##0.00"),
    ("Net debt",
     _f(f"{I('Borrowings - non-current')}+{I('Borrowings - current')}"
        f"-{I('Cash + other bank balances')}"), "Debt less cash", "#,##0.00"),
    ("Overall gearing (x)  [SECTOR-DEFINING]",
     _f(f"({I('Borrowings - non-current')}+{I('Borrowings - current')})/{I('Tangible net worth')}"),
     "Total debt to tangible net worth - CareEdge reports this AND the net measure", '0.00"x"'),
    ("Net overall gearing (x)",
     _f(f"({I('Borrowings - non-current')}+{I('Borrowings - current')}"
        f"-{I('Cash + other bank balances')})/{I('Tangible net worth')}"),
     "Net of cash", '0.00"x"'),
    ("TOL / TNW (x)",
     _f(f"({I('Total assets')}-{I('Tangible net worth')})/{I('Tangible net worth')}"),
     "Total outside liabilities to tangible net worth", '0.00"x"'),
    ("Interest coverage (x)  [SECTOR-DEFINING]",
     _f(f"({I('Profit before tax')}+{I('Finance cost')}+{I('Depreciation')}-{I('Other income')})"
        f"/{I('Finance cost')}"),
     "PBILDT to finance cost. DECLINING - the key monitorable", '0.00"x"'),
    ("Total debt / PBILDT (x)",
     _f(f"({I('Borrowings - non-current')}+{I('Borrowings - current')})"
        f"/({I('Profit before tax')}+{I('Finance cost')}+{I('Depreciation')}-{I('Other income')})"),
     "Years of earnings to clear debt", '0.00"x"'),
    ("Current ratio (x)",
     _f(f"{I('Current assets')}/{I('Current liabilities')}"), "Short-term liquidity", '0.00"x"'),
    ("RoCE (%)",
     _f(f"({I('Profit before tax')}+{I('Finance cost')}-{I('Other income')})"
        f"/({I('Borrowings - non-current')}+{I('Borrowings - current')}+{I('Tangible net worth')})"),
     "PBIT over capital employed", "0.00%"),
    ("Receivable days",
     _f(f"365*{I('Trade receivables')}/{I('Total income')}"),
     "Collection cycle - improving sharply", "0"),
    ("Inventory days",
     _f(f"365*{I('Inventories')}/{I('Total income')}"), "Stock holding - improving", "0"),
]

TIEOUTS = [
    ("FY25 total income = revenue + other income", "=Inputs!E%d+Inputs!E%d" % (
        R["Revenue from operations"], R["Other income"]), 296.13,
     "Reported total income Rs 296.13 crore - exact"),
    ("FY25 current ratio vs company-disclosed", "=Inputs!E%d/Inputs!E%d" % (
        R["Current assets"], R["Current liabilities"]), 1.38,
     "The FY2025 AR's own key-ratio table reports 1.38 - exact match"),
    ("FY24 current ratio vs company-disclosed", "=Inputs!D%d/Inputs!D%d" % (
        R["Current assets"], R["Current liabilities"]), 1.33,
     "The FY2024 AR reports 1.33 - exact match"),
    ("FY25 company 'debt-equity' = LT debt / TNW", "=Inputs!E%d/Inputs!E%d" % (
        R["Borrowings - non-current"], R["Tangible net worth"]), 0.26,
     "The company's published 'Debt Equity Ratio' uses LONG-TERM debt only. Reproducing 0.26 "
     "confirms both the extraction and the convention - CareEdge gearing on TOTAL debt is 0.63x"),
    ("FY24 company 'debt-equity' = LT debt / TNW", "=Inputs!D%d/Inputs!D%d" % (
        R["Borrowings - non-current"], R["Tangible net worth"]), 0.28,
     "Company reports 0.28 - exact"),
]

SCORE = {
    "factors": [
        ("Industry risk - cotton textiles", 4, 0.20,
         "Terry towels and home textiles: fragmented, working-capital intensive, exposed to cotton "
         "price volatility and to export demand. CareEdge's cotton-textile methodology treats raw "
         "material pass-through as the central variable. Structurally a mid-band industry."),
        ("Scale and market position", 4, 0.15,
         "Revenue of Rs 295.86 crore in FY2025 (+19.8%). Small in absolute terms; Panipat-based "
         "with a single promoter group holding. Limited pricing power against branded and export "
         "buyers."),
        ("Financial risk - leverage", 2, 0.25,
         "Genuine deleveraging: overall gearing 0.76x to 0.63x, net gearing 0.70x to 0.60x, "
         "TOL/TNW 1.00x to 0.85x. Total debt fell to Rs 61.39 crore while net worth rose to "
         "Rs 97.90 crore through accruals. The clearest strength in the credit."),
        ("Financial risk - profitability and coverage", 4, 0.25,
         "THE CONSTRAINT. PBILDT margin 7.52%, down from 7.99%; the company's own operating "
         "margin fell 16.63% to 12.56%. Interest coverage DECLINED to 3.78x from 4.24x even as "
         "debt fell, because finance cost rose 26.7% while PBILDT rose only 12.8%. Revenue grew "
         "19.8% but earnings did not keep pace - growth is being bought with margin."),
        ("Working capital and liquidity", 3, 0.15,
         "Marked improvement: receivable days 61 to 45, inventory days 38 to 31, current ratio "
         "1.33x to 1.38x. Offset by thin absolute liquidity - cash and bank balances of only "
         "Rs 2.54 crore against Rs 35.65 crore of current borrowings."),
    ],
    "anchor": "BBB band (composite 3.35)",
    "view": "CARE BBB; Stable / CARE A3+",
    "divergence": "No divergence at the issuer level. The company's own FY2024-25 annual report "
                  "discloses CRISIL reaffirming BBB/Stable on Rs 94 crore of bank facilities on "
                  "04-Jul-2025, up from BBB/Negative on Rs 76.5 crore in the two prior years. "
                  "This assessment reaches the same band and the same outlook independently, and "
                  "the Negative-to-Stable move is corroborated by the deleveraging above. NO Riba "
                  "rationale exists in any reference library - searched; the anchor is the "
                  "issuer's own Step 7b disclosure.",
}

if __name__ == "__main__":
    out = build_spreads(
        company="Riba Textiles Limited", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE,
        out="Riba Textiles Limited_Financial_Spreads.xlsx")
    print("Saved:", out)
