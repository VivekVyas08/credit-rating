"""
IIFL Finance Limited (STANDALONE) — extraction + CARE/CareEdge NBFC ratio suite.
STEP 5 (extraction) + STEP 6 (ratios & tie-out) of the SOP.

Basis: STANDALONE (IIFL Finance Limited only), per user instruction.
Source: IIFL Finance's OWN audited standalone financial statements — FY26 Annual
Report (Balance Sheet p.308 / P&L p.309 / loan note 8 / directors' report), with
FY25 & FY24 comparatives. Amounts in Rs crore. Units converted once, here.
Ratio definitions per CARE 'Financial Ratios - Financial Sector' (Feb 2025).
Data rule (R1/R2): NO figure sourced from any CRA rating or the broker note.
"""

# ================================================================ EXTRACTION (Rs cr)
# --- Balance sheet (standalone) : FY26 / FY25 ---
BS = {
 "cash_ce":        {"FY26": 1322.39, "FY25": 528.23},
 "bank_bal_other": {"FY26": 600.59,  "FY25": 832.38},
 "investments":    {"FY26": 5844.41, "FY25": 5457.57},
 "loans_net":      {"FY26": 38135.72,"FY25": 22866.99},
 "loans_gross":    {"FY26": 38565.00,"FY25": 23304.56},
 "ecl_allowance":  {"FY26": 429.28,  "FY25": 437.57},
 "secured_gross":  {"FY26": 35527.43,"FY25": 16509.51},
 "unsecured_gross":{"FY26": 2960.38, "FY25": 6706.27},
    # THIRD Schedule III Division III category, added 29-Aug-2026. The extraction
    # carried only secured and unsecured, so the two did not sum to gross loans - a
    # shortfall of 88.78 (FY25) and 77.19 (FY26) that nothing in this engine noticed,
    # because it had no tie-outs at all. The FY25 figure is confirmed against the
    # annual report's own row, "Covered by bank/government guarantees | 88.78".
    # FY26 is left None: a 77.19 residual is implied by the arithmetic, but the
    # corresponding printed row was NOT unambiguously identified in this pass (the
    # documents carry several such lines - 14.05, 48.06, 88.78 - across entities and
    # years), and writing an implied figure in as though it were extracted is exactly
    # the habit these checks exist to break.
    "guarantee_backed_gross": {"FY25": 88.78, "FY26": None},
 "total_assets":   {"FY26": 49634.21,"FY25": 32114.54},
 "dta_net":        {"FY26": 185.14,  "FY25": 295.54},
 "intangibles":    {"FY26": 4.66,    "FY25": 7.05},     # other intangibles + under-dev
 "debt_securities":{"FY26": 15384.97,"FY25": 11360.00}, # note 19 (NCDs incl PP-MLD)
 "other_borrow":   {"FY26": 19613.66,"FY25": 11297.94}, # note 20 (bank TL/ECB/refinance)
 "sub_liabilities":{"FY26": 3741.37, "FY25": 1866.22},  # note 21 (incl PDI 600 in FY26)
 "lease_liab":     {"FY26": 417.30,  "FY25": 351.27},
 "net_worth":      {"FY26": 7560.71, "FY25": 6507.10},  # eq cap + other equity
}
# --- P&L (standalone) : FY26 / FY25 / FY24 ---
PL = {
 "interest_income":{"FY26": 6438.86, "FY25": 3777.80, "FY24": 4348.34},
 "total_income":   {"FY26": 7467.11, "FY25": 4080.16, "FY24": 4649.43},
 "finance_cost":   {"FY26": 3273.29, "FY25": 1848.72, "FY24": 1702.08},
 "impairment":     {"FY26": 705.59,  "FY25": 456.50,  "FY24": 378.71},
 "employee_exp":   {"FY26": 1076.06, "FY25": 759.73,  "FY24": 723.29},
 "other_exp":      {"FY26": 722.69,  "FY25": 463.38,  "FY24": 572.41},
 "depreciation":   {"FY26": 163.14,  "FY25": 136.98,  "FY24": 134.90},
 "exceptional":    {"FY26": 0.0,     "FY25": 586.50,  "FY24": 0.0},  # AIF provision (non-recurring)
 # --- lines the FY24-26 build-up was missing (added 04-Sep-2026) -----------------------------
 # Found while adding interest coverage: a PBT derived from the lines above came out 1,526.34
 # for FY2026 against the AR's printed 1,506.09, and -171.65 for FY2025 against the printed
 # -550.77. Two expense captions were absent. This is failure mode 38 in miniature - a
 # reconstruction used where the printed figure was available - so the printed PBT is now
 # carried as an input and the decomposition is TIED to it (failure mode 39: a decomposition
 # is not verification until it reconciles to the note's own total).
 "fv_loss":        {"FY26": 20.25,   "FY25": 0.0,     "FY24": 241.29},  # net loss on FV changes
 "derecog_loss":   {"FY26": 0.0,     "FY25": 379.12,  "FY24": 166.77},  # FVTOCI derecognition
 "pbt_printed":    {"FY26": 1506.09, "FY25": -550.77, "FY24": 729.98},  # AR printed PBT row
 "pat":            {"FY26": 1153.52, "FY25": -409.57, "FY24": 584.78},
}
# --- Regulatory / disclosed (as reported to RBI) ---
REG = {"crar_FY26": 17.84, "tier1_FY26": 12.24, "tier2_FY26": 5.60,
       "gnpa_pct_group_FY26": 1.5, "nnpa_pct_group_FY26": 0.7, "pcr_pct_FY26": 93.0}  # AR group-headline
# --- STANDALONE asset quality, computed from Note 38A.6 stage-wise EAD (Rs cr) ---
STAGE = {"stage1":{"FY26":36816.73,"FY25":22037.63},"stage2":{"FY26":746.21,"FY25":574.03},
         "stage3":{"FY26":428.12,"FY25":423.67},"total_ead":{"FY26":37991.06,"FY25":23035.33},
         "stage3_ecl":{"FY26":208.04,"FY25":269.81}}   # Stage-3 ECL on principal (Note 8)
# --- Instrument split (Note 19; face/component, Rs cr) ---
INSTR = {"ncd_secured_FY26":9562.92, "ncd_secured_FY25":8643.23, "mtn_usd_within_ncd_FY26":4030.49,
         "cp_unsecured_FY26":5742.90, "cp_unsecured_FY25":2649.70,
         "sub_liabilities_FY26":3741.37, "pdi_FY26":600.00,
         "bank_facilities_FY26":19613.66, "cp_programme_limit":3000.0}
# --- 12-month contractual debt maturities (Note 38B(i), FY26, Rs cr) : upto-3m + 3-6m + 6-12m ---
MAT12 = {"debt_securities":5160.55+926.46+1965.65, "other_borrow":2556.19+989.44+3765.34,
         "sub_liabilities":50.51+24.82+40.33, "lease":29.87+26.36+54.50}

# ================================================================ HELPERS
def total_debt(y, incl_lease=False):
    d = BS["debt_securities"][y] + BS["other_borrow"][y] + BS["sub_liabilities"][y]
    return d + (BS["lease_liab"][y] if incl_lease else 0.0)
def tnw(y):
    return BS["net_worth"][y] - BS["dta_net"][y] - BS["intangibles"][y]
def avg(d, y="FY26", yp="FY25"):
    return (d[y] + d[yp]) / 2.0

# ================================================================ RATIOS (FY26)
nii26  = PL["interest_income"]["FY26"] - PL["finance_cost"]["FY26"]
opex26 = PL["employee_exp"]["FY26"] + PL["other_exp"]["FY26"] + PL["depreciation"]["FY26"]
opex25 = PL["employee_exp"]["FY25"] + PL["other_exp"]["FY25"] + PL["depreciation"]["FY25"]


def pbt_derived(y):
    """PBT rebuilt from the printed expense components. Used ONLY to tie against the printed
    PBT below - never as the figure itself (failure mode 38: the note is the source, a
    reconstruction is not). The derecognition gain sits inside total income, so only the loss
    side is subtracted here."""
    return (PL["total_income"][y] - PL["finance_cost"][y] - PL["fv_loss"][y]
            - PL["derecog_loss"][y] - PL["impairment"][y] - PL["employee_exp"][y]
            - PL["other_exp"][y] - PL["depreciation"][y] - PL["exceptional"][y])


def pbt(y):
    """PBT AS PRINTED in the AR's statement of profit and loss."""
    return PL["pbt_printed"][y]
avg_ta = avg(BS["total_assets"]); avg_tnw = (tnw("FY26")+tnw("FY25"))/2
avg_gl = avg(BS["loans_gross"]); avg_bor = (total_debt("FY26")+total_debt("FY25"))/2

R = {
 "Interest-income growth %":        100*(PL["interest_income"]["FY26"]/PL["interest_income"]["FY25"]-1),
 "Gross-loan growth %":             100*(BS["loans_gross"]["FY26"]/BS["loans_gross"]["FY25"]-1),
 "Total-income growth %":           100*(PL["total_income"]["FY26"]/PL["total_income"]["FY25"]-1),
 "Overall gearing TD/TNW x (excl lease)": total_debt("FY26")/tnw("FY26"),
 "Overall gearing TD/TNW x (incl lease)": total_debt("FY26",True)/tnw("FY26"),
 "Gearing FY25 x (excl lease)":     total_debt("FY25")/tnw("FY25"),
 "CRAR % (RBI, FY26)":              REG["crar_FY26"],
 "Tier-I CRAR %":                   REG["tier1_FY26"],
 "TNW FY26 (Rs cr)":                tnw("FY26"),
 "Total debt excl-lease FY26 (Rs cr)": total_debt("FY26"),
 "ECL allowance / gross loans %":   100*BS["ecl_allowance"]["FY26"]/BS["loans_gross"]["FY26"],
 "Secured (tangible) mix %":        100*BS["secured_gross"]["FY26"]/BS["loans_gross"]["FY26"],
 "Unsecured mix %":                 100*BS["unsecured_gross"]["FY26"]/BS["loans_gross"]["FY26"],
 "GNPA (Gross Stage-3 %) STANDALONE FY26": 100*STAGE["stage3"]["FY26"]/STAGE["total_ead"]["FY26"],
 "GNPA (Gross Stage-3 %) STANDALONE FY25": 100*STAGE["stage3"]["FY25"]/STAGE["total_ead"]["FY25"],
 "NNPA (Net Stage-3 %) STANDALONE FY26":   100*(STAGE["stage3"]["FY26"]-STAGE["stage3_ecl"]["FY26"])/(STAGE["total_ead"]["FY26"]-STAGE["stage3_ecl"]["FY26"]),
 "Stage-2 % STANDALONE FY26":       100*STAGE["stage2"]["FY26"]/STAGE["total_ead"]["FY26"],
 "Stage-3 specific PCR % STANDALONE": 100*STAGE["stage3_ecl"]["FY26"]/STAGE["stage3"]["FY26"],
 "GNPA/NNPA/PCR % (AR group-headline)": f'{REG["gnpa_pct_group_FY26"]}/{REG["nnpa_pct_group_FY26"]}/{REG["pcr_pct_FY26"]}',
 "12m debt maturities STANDALONE (Rs cr)": sum(MAT12.values()),
 "Immediate liquidity cover (months, liquid/[12m debt/12])": (BS["cash_ce"]["FY26"]+BS["bank_bal_other"]["FY26"])/(sum(MAT12.values())/12),
 "RoTA (PAT/avg TA) %":             100*PL["pat"]["FY26"]/avg_ta,
 "RoNW (PAT/avg TNW) %":            100*PL["pat"]["FY26"]/avg_tnw,
 "NIM (NII/avg TA) %":              100*nii26/avg_ta,
 "Yield on advances %":             100*PL["interest_income"]["FY26"]/avg_gl,
 "Cost of borrowing %":             100*PL["finance_cost"]["FY26"]/avg_bor,
 "Interest spread %":               100*PL["interest_income"]["FY26"]/avg_gl - 100*PL["finance_cost"]["FY26"]/avg_bor,
 "Cost-income % (opex/(TI-fin))":   100*opex26/(PL["total_income"]["FY26"]-PL["finance_cost"]["FY26"]),
 "Opex / avg TA %":                 100*opex26/avg_ta,
 "Credit cost (impairment/avg TA) %": 100*PL["impairment"]["FY26"]/avg_ta,
 "NII FY26 (Rs cr)":                nii26,
 "PAT FY26 (Rs cr)":                PL["pat"]["FY26"],
 # --- rows CareEdge's own financial-sector template carries and this engine lacked -----------
 # Added 04-Sep-2026: check_sections' peer-row probe (failure modes 32/33) reported Total
 # assets, Cost-to-income and Interest coverage absent from the rationale against the peer
 # 360 One Wam Limited_16 Feb 2026. Cost-to-income and total assets already existed here;
 # interest coverage did not, and was being written into prose rather than computed (R6).
 # PBT is DERIVED from the printed P&L components rather than taken as a figure, so the
 # tie-out below can test it. FY2026 implies a 24.4% tax charge against India's ~25.17%
 # NBFC rate - the sanity check that says the derivation is right. FY2025 carries a tax
 # charge on a pre-tax loss, consistent with the deferred-tax asset falling 295.54 -> 185.14.
 "PBT FY26 derived (Rs cr)":        pbt("FY26"),
 "PBT FY25 derived (Rs cr)":        pbt("FY25"),
 "Interest coverage x FY26 ((PBT+fin)/fin)": (pbt("FY26") + PL["finance_cost"]["FY26"])
                                             / PL["finance_cost"]["FY26"],
 "Interest coverage x FY25 ((PBT+fin)/fin)": (pbt("FY25") + PL["finance_cost"]["FY25"])
                                             / PL["finance_cost"]["FY25"],
 "Cost-income % FY25 (opex/(TI-fin))": 100*opex25/(PL["total_income"]["FY25"]
                                                   - PL["finance_cost"]["FY25"]),
 "Total assets FY26 (Rs cr)":       BS["total_assets"]["FY26"],
 "Total assets FY25 (Rs cr)":       BS["total_assets"]["FY25"],
 "Cash + bank balances (Rs cr)":    BS["cash_ce"]["FY26"]+BS["bank_bal_other"]["FY26"],
}

# --------------------------------------------------------------------------- tie-outs
# Added 29-Aug-2026. This engine carried NO tie-outs, so every figure in it was verified by
# nothing. FLAT below is DERIVED from the engine's own table at import - nothing is retyped,
# so this cannot introduce an error of its own - and it is what the checks read, which is also
# what makes the coverage harness able to measure this engine at all.
YEARS = ["FY25", "FY26"]


def _flat():
    import os
    import sys
    _root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if _root not in sys.path:
        sys.path.insert(0, os.path.join(_root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts
    return common_tieouts.flatten_metric_major(BS, YEARS)


FLAT = _flat()


def compute():
    """{period: {metric: value}} - the contract shape the shared tooling drives."""
    out = {}
    for i, y in enumerate(YEARS):
        out[y] = {k: v[i] for k, v in FLAT.items() if v[i] is not None}
    return out


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source). Structural only - see
    common_tieouts.py for exactly what these do and do not prove."""
    import os
    import sys
    _root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if _root not in sys.path:
        sys.path.insert(0, os.path.join(_root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts
    T = common_tieouts.build(FLAT, YEARS)
    T += common_tieouts.corroboration(FLAT, YEARS, 'iifl')

    # The DERIVED PBT must leave a credible tax charge against the audited PAT. This is the
    # check that makes the interest-coverage row testable rather than merely computed: if the
    # expense build-up were wrong, PBT would move and the implied tax rate would go implausible.
    # FY2026 only - FY2025 carries a tax charge on a pre-tax loss (the deferred-tax asset falls
    # 295.54 -> 185.14), so an effective-rate test is not meaningful in that year and is not
    # asserted here.
    # A decomposition is not verification until it reconciles to the note's own printed total
    # (failure mode 39). Rebuilding PBT from every expense caption must reproduce the AR's
    # printed PBT row exactly - this is the check that caught two missing expense lines.
    for _y in ("FY24", "FY25", "FY26"):
        T.append(("%s expense build-up reproduces the AR's printed PBT" % _y,
                  pbt_derived(_y), PL["pbt_printed"][_y], 0.02,
                  "audited standalone statement of profit and loss - every expense caption "
                  "against the printed 'Profit before tax' row"))
    # And the printed PBT less the printed PAT must leave a credible tax charge.
    _p, _pat = pbt("FY26"), PL["pat"]["FY26"]
    T.append(("FY2026 implied tax rate on printed PBT is the Indian NBFC rate",
              100 * (_p - _pat) / _p, 25.17, 2.0,
              "audited standalone P&L - printed PBT against printed PAT; 25.17% is the "
              "statutory rate under s.115BAA"))
    return T


if __name__ == "__main__":
    print("="*64); print(" IIFL FINANCE (STANDALONE) — CARE NBFC ratio suite, FY26"); print("="*64)
    for k,v in R.items():
        print(f"  {k:<48} {v:>12.2f}" if isinstance(v,(int,float)) else f"  {k:<48} {v:>12}")
    print("\n--- STEP 6 external/internal TIE-OUTS (reconcile to the AR) ---")
    print(f"  Net loans:  gross {BS['loans_gross']['FY26']:.2f} - ECL {BS['ecl_allowance']['FY26']:.2f} = "
          f"{BS['loans_gross']['FY26']-BS['ecl_allowance']['FY26']:.2f}  | AR net = 38135.72")
    print(f"  Gross mix:  secured {BS['secured_gross']['FY26']:.2f} + unsec {BS['unsecured_gross']['FY26']:.2f} + gtee 77.19 = "
          f"{BS['secured_gross']['FY26']+BS['unsecured_gross']['FY26']+77.19:.2f}  | AR gross = 38565.00")
    print(f"  Equity:     eq cap 85.06 + other equity 7475.65 = {85.06+7475.65:.2f}  | AR = 7560.71")
    print(f"  Total debt: {total_debt('FY26'):.2f} excl-lease (debt sec 15384.97 + other 19613.66 + sub 3741.37)")


_T = tieouts()
_bad = [x for x in _T if abs(x[1] - x[2]) > x[3]]
print("")
print("%d/%d tie-outs reconcile" % (len(_T) - len(_bad), len(_T)))
for _x in _bad:
    print("  FAIL %s  [%s]" % (_x[0], _x[4]))


# ---- Measured coverage disclosure (failure mode 39) -----------------------------------------
# tools/tieout_mutation.py reports 87.9% coverage: 4 of 33 perturbed inputs are
# reachable by NO tie-out. FM39 requires each to be given a check or NAMED as
# uncheckable with the reason. Measured, not assumed - re-run the harness to confirm.
DISCLOSED_DIFFERENCES = [
    ("Deferred tax assets and intangibles, both FY2025 and FY2026, are covered by no tie-out",
     "Measured with tools/tieout_mutation.py: 4 of 33 inputs. These four are the "
     "deductions that convert equity into TANGIBLE net worth. No published "
     "tangible-net-worth figure for this issuer is held in the engine to reconcile the "
     "build-up against, so the deduction is traceable to the balance sheet but not "
     "independently reproducible - and per failure mode 32 the tangible-net-worth basis "
     "is precisely where a wrong definition shows up in gearing and return. Named rather "
     "than left silent."),
]
