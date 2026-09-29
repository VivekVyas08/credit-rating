# CRISIL — infrastructure sectors: project-finance conventions, DSCR discipline and sector metrics

**Source, read in full 06-Sep-2026:** `CRISIL/Methodology/criteria-for-infrastructure-sectors.md` — all four sections (I cross-cutting drivers · II power: generation, distribution, transmission, solar, wind · III annuity and HAM roads · IV toll roads), plus the P90 annexure. **Also read in full 06-Sep-2026:** `crisils-criteria-for-expected-loss-ratings-for-infrastructure-projects.md` (see §9). **Not read:** the separately published mobile-telephony and municipal/ULB methodologies this file refers out to. Treat any gap here as "not yet extracted."

---

## 1. Infrastructure INVERTS three corporate business-risk instincts

The corporate criteria still apply as the base (CRISIL says so explicitly), but three drivers behave the opposite way, and carrying corporate reflexes across is the failure-mode-33 trap in its infrastructure form.

| Driver | Corporate reading | Infrastructure reading |
|---|---|---|
| **Pricing flexibility** | Market-driven; flexibility is normal | **Limited by design.** Tariff is set by government or regulator. **Regulator-set beats government-set:** CRISIL "favourably views entities whose tariff structures are determined by regulators" (SERCs for power, partly TRAI for telecom) because those balance service-provider returns against consumer interest; government-influenced tariffs (state transport, petroleum products, aviation, water and sewerage) are viewed **unfavourably**, with the credit view "driven by the extent of the influence". |
| **Demand risk** | A major business-risk driver | **Low, and viewed favourably.** Demand generally outstrips supply; in water, airports and urban infrastructure the gap is significant. "Demand risks are likely to remain low over the medium term, which has a positive impact." |
| **Monopoly / market share** | A sizeable share is generally a positive | **Monopoly alone does NOT improve the credit profile.** "The ability to earn profits is critical." SEBs were monopolies and made huge losses because state governments blocked rational tariff increases; AAI was a congested monopoly that nonetheless booked large profits. **The capability to convert monopoly status into profit is the rating factor — not the status.** |

**A stated override worth remembering:** *"if the liquidity of the company is weak, industry risk or other business-related factors may exert minimal influence on the final rating."* Weak liquidity dominates the business-risk read, it does not average against it — the same shape as failure mode 53's gate.

**Three categories of rated infrastructure entity:** basic service providers with moderate commercial viability (water/sewerage boards, state transport corporations, state gencos/transcos/discoms); commercial service providers (telecom, aviation infrastructure, toll operators, central/independent generators and transmitters, oil and gas); and SPVs floated by state and local governments with minimal commercial viability, seeking **guarantee-supported** ratings.

**Financial risk uses the corporate framework** — existing position, future profile, cash-flow adequacy, financial flexibility — **except for state governments and ULBs**, which have their own framework because they are driven by social rather than financial objectives and can raise funds through taxation. Because infrastructure cash flows are contractually more stable, CRISIL leans on **DSCR and Debt/EBITDA** and says such assets **support higher leverage** than manufacturing or services.

## 2. ⚠ The DSCR formula, and the exclusion this project must not get wrong

CRISIL states the same formula **three separate times** — power utilities, annuity/HAM roads, and toll roads — with the same qualifier each time:

> **DSCR = (Profit after tax + Depreciation + Interest) / (Interest + Repayment)**
>
> *"The calculation shall solely be based on project cash flows, **without considering parent support or debt service reserve account (DSRA)**."*

**This is the trap.** A project SPV's whole liquidity case rests on its DSRA and its sponsor, so the instinct is to let both into the coverage number. CRISIL excludes both **by design**, precisely so that DSCR measures the asset and the DSRA/sponsor are assessed separately as *liquidity* and *support*. A DSCR quoted with the DSRA inside it is not a CRISIL DSCR, and it will not reconcile with anything the agency publishes.

Further discipline on the same ratio:
- It is a **cash-accruals-based** approach, computed **over the loan life**, and may be driven by **minimum DSCR, average DSCR, or a combination**, chosen on the variability of the cash flows.
- **Refinancing risk:** where debt tenor (often ~3-5 years, bullet) is shorter than asset life (e.g. 25 years for solar), CRISIL tests whether project cash flows can support the debt over the asset's life and the amount expected to be refinanced, with **tail-period** assumptions. It may compute **PLCR = PV of CFADS over the asset's life (discounted at the cost of debt) / outstanding debt**.
- **Debt/EBITDA = Adjusted Total Debt / EBITDA**, used for entities funding multiple projects off their own balance sheet with regular expansionary capex. May be struck on **net** debt where the company's stated policy is to hold cash it could use to repay — note "Adjusted Total debt" carries CRISIL's wide debt definition (failure mode 47).

### DSCR is calibrated BY ASSET CLASS, and CRISIL ranks them

> *"Transmission projects can operate with thin DSCR because of the predictability of their cash flow. This is in contrast to toll road and renewable (wind and solar) power projects. Toll projects have uncertain cash flow due to demand and price risk… For renewable power projects, seasonal PLFs lead to uncertain output. Hence, these projects need higher DSCR."*

So a 1.15x DSCR is not one thing: it is comfortable for a transmission SPV and thin for a toll road. **Never compare a DSCR across asset classes without saying which class it belongs to.** CRISIL also notes that because developers want a reasonable return, **project DSCR and liquidity in renewables "are unlikely to be substantially high"** — a high renewable DSCR should prompt a check of the assumptions, not a celebration.

## 3. DSRA and liquidity — sized to counterparty risk, with hard seasonality floors

Liquidity requirement is **directly proportional to counterparty delay and cash-flow variability**, and **lower** where the structure leaves an adequate time gap between inflow and outflow. A stronger counterparty justifies a smaller DSRA; a weaker one demands a larger.

**A bank guarantee may substitute for cash DSRA only if BOTH hold:** the BG has **recourse to the parent**, and CRISIL satisfies itself that **the parent maintains sufficient liquidity to cover it**. A BG without parent recourse gives no liquidity benefit at all.

**Seasonality floors — these are the numbers:**

| Technology | Seasonal deficit | CRISIL's requirement |
|---|---|---|
| **Solar** | about **2 months** of debt obligation | liquidity sized to cover it, plus counterparty delay |
| **Wind** | **4-5 months** of debt servicing | *"Operational wind power projects should… have a base case cash liquidity equivalent to at least four months of maturing debt"* — some projects need more |

CRISIL's own worked wind example: peak season (months 1-4) produces ~70% of annual output, lean season (months 5-12) ~30%; on a 1 MW project at Rs 6 crore, 3:1 debt:equity, P90 PLF 20%, Rs 5/unit, 12-year debt at 11%, the cumulative lean-season shortfall is Rs 22.38 lakh against Rs 5.6 lakh of monthly maturing debt — **4.0 months**.

**Parent liquidity can count**, but only where the parent has a *policy* of holding a buffer on its balance sheet for its SPVs' cash-flow mismatches. The requirement is otherwise to be met **at project level**.

## 4. Renewables — P90 is mandatory, and the PLF track record is a rating modifier

**CRISIL uses the P90 annual PLF, not P50, to compute DSCR for both solar and wind.** P50 is the expected average (equal chance of being above or below); **P90 is the level the asset is 90% likely to exceed in a given year**. International practice is the same.

Estimation variability differs sharply by technology and is worth quoting: **standard deviation of PLF estimation is 2-3% for solar (on a P50 of ~20%) against 4-6% for wind** — wind is roughly twice as variable, which is why its seasonality floor is double solar's.

**Reading the PLF track record (a genuine modifier, in both directions):**
- Output **at sub-P90 for two to three years** → the power curve has probably shifted (faster degradation, weaker radiation, or a mis-estimated wind resource) → **constrains the rating**.
- Output in the early years **between P50 and P75**, i.e. materially above P90 → **still consistent with the expected curve**. This is not outperformance and must not be read as a strength.
- A **new study** showing a higher P90 → CRISIL adopts the new P90.

**PPA tenure and renewal risk:** PPA tenure shorter than debt tenure creates pricing risk, worsening as the gap widens. A PPA priced **at or below** the prevailing market rate has **low** renewal risk; one priced **considerably above** market faces renewal risk at expiry — *"the higher the current tariff from the market rate, the greater the project's risk exposure."* Non-amortising structures with a large bullet add refinancing risk.

**Portfolio diversification is an explicit NOTCH-UP source:** *"Crisil Ratings notches up the rating of an SPV if it has greater stability in cash flow on account of portfolio diversification."* Geographic spread decorrelates the resource (for wind, "the farther the locations are from each other, the lesser the correlation between their wind speed patterns", reducing inter-annual standard deviation); counterparty spread decorrelates payment risk.

**Multiple SPVs under one promoter** are consolidated using the **homogenous-group methodology** (see `CRISIL_BANKS_NBFC_CONVENTIONS.md` §9, including the 10%-of-group-EBITDA rule) where cash flows are fungible and management has articulated intent to support.

## 5. ⚠ Counterparty payment risk is NOT counterparty credit quality

> *"The payment risk is not the same as the counterparty's credit quality. Often, state discoms with weak credit risk profiles continue to make payments to power generation companies, albeit with delays."*

Weak discoms often keep paying because the state government backs them, and some have a **better payment record for renewable purchases specifically**. CRISIL maintains **payment-risk categories** for state discoms, assessed on:

| Risk factor | Aspects analysed |
|---|---|
| Business profile | track record of recent tariff increases · **AT&C losses** · profit gap (Rs per unit, on a subsidy-booked basis) |
| Financial profile | networth · debt · losses |
| State government's ability to support | release of subsidy · **the state government's own rating** |
| Payment track record | payment behaviour over the past few years |

A base-case payment delay is assumed from the category; where a specific asset's observed pattern differs materially and persistently, that is factored in as a modifier.

## 6. Transmission — line availability thresholds and the PoC pooling effect

- **Natural monopoly**: demand risk negligible (duplicating lines is implausible); pricing risk negligible (tariff by competitive bidding, CERC-approved, TSAs typically **25-35 years**; asset life **30-35 years**, usually exceeding loan tenure).
- **Line availability is the operating metric**, with a banded incentive structure: below an **upper threshold (say 98%)** transmission charges are reduced; below a **lower threshold (say 95%)** an additional penalty applies; above the upper threshold, incentives raise cash inflow. **Most operational assets run at 99%+**, and CRISIL treats the track record of holding availability above normative levels as a key input.
- **Stabilisation takes up to 18 months** post-construction, depending on counterparty payment behaviour; **PoC-mechanism SPVs stabilise faster**. Operational metrics should not be tested against base-case assumptions until stabilised.
- **PoC (Point of Connection) mechanism, interstate:** ISTS licensees pool collections through the CTU (a wholly-owned PGCIL subsidiary), which bills, collects and disburses pro rata. **A shortfall is borne collectively in proportion to pool share** — CRISIL's worked example: on Rs 100 owed across four licensees at Rs 25 each, a Rs 10 collection shortfall costs each licensee Rs 2.5, where without pooling the single exposed SPV would have borne the whole Rs 10. CTU/PGCIL collection has run **~98%+**, normalising to **98-99%+** over longer horizons. **Interstate PoC projects therefore carry materially lower counterparty risk than intrastate ones.**
- **Intrastate:** the counterparty is a single STU dependent on state discoms — **no diversification benefit, no pooling bargaining power**. Assessed on the STU's own payment track record against the discom payment-risk categories above.

## 7. Roads — annuity and HAM

**No demand risk and no price risk** in either: annuity roads receive fixed semi-annual payments from NHAI or a state authority irrespective of traffic; HAM adds interest on residual annuities and inflation-linked maintenance compensation. The residual risks are **cost adequacy**, **inflation/interest basis risk**, and **counterparty payment delay**.

**Construction stage:**
- **HAM: 80% ROW available before work begins**, with an option to descope or delink if the authority fails to hand over ROW in time (PCOD granted for the completed stretch, annuities received on it) — this materially reduces the land-acquisition delay that dominates road-project risk.
- **HAM: construction support of 40% of construction cost** for NHAI HAM roads, reducing funding risk.
- Annuity roads carry the full implementation and funding risk; terrain complexity (hills, forests, rivers) raises it. Road construction **technology risk is nil** — well established.

**Two model concession agreement amendments that changed the risk profile — check which vintage a project is:**
- **November 2020:** interest on residual annuities moved from *bank rate + 3%* to **MCLR + 1.25%**, paid semi-annually. Since SPV borrowings are typically MCLR-linked, this **nullifies the nominal basis risk for projects awarded after Nov-2020**. Projects awarded **before** 2021 retain bank-rate-vs-MCLR basis risk and require sensitivity analysis.
- **May 2022:** bid evaluation now on **Bid Project Cost alone**, with maintenance compensation paid as a **fixed percentage of BPC** — largely removing the risk of under-bidding maintenance.

**Calibrating maintenance:** CRISIL tests adequacy of MMR and O&M costs (state roads see less traffic and lower wear than national highways; high-quality roads may defer MMR frequency; freight-intensive zones, difficult terrain and the developer's maintenance track record all bear), then sensitises **inflation** and **interest rates**. Non-maintenance can delay or **suspend annuity payments until road quality is restored** — a direct cash-flow consequence, not just an operational one.

**Delinking from the sponsor:** *"Assessment of the SPV's ability to carry out maintenance without seeking support from the sponsor is important. This helps in delinking the credit risk profile of the SPV from that of the sponsor."* This is the analytical root of failure mode 52 — CRISIL's 1-2 notch cap on infrastructure-SPV parent support exists because the criteria are actively trying to keep the SPV standalone.

## 8. Roads — toll

Revenue risk is real here, unlike annuity: **revenue = traffic volume × toll rate**.

- **Traffic forecasting:** origin-destination surveys by reputed consultants, seasonal variation, traffic mix by vehicle type. **A balanced vehicle mix improves viability**; a road used mainly by freight raises O&M cost and is exposed to seasonal (post-harvest) and industrial-cycle swings. Existing roads do not disappear and compete; **excessive dependence on a few feeder roads** is a risk. CRISIL notes plainly that *"in many instances, the traffic volume was highly overestimated"* and always runs a traffic sensitivity.
- **Toll rate revisions pegged to a price index are a positive** — they offset maintenance cost inflation.
- **Willingness to pay** is assessed against user benefit: savings in vehicle operating cost, transit time and distance.
- **A variable concession period reduces risk** relative to a fixed one, because the operator can extend if revenue underperforms rather than having to set a high initial toll.
- **Construction:** revised BOT MCA (August 2020, March 2024) requires **90% of ROW for the "construction zone" before the Appointed Date** — a higher bar than HAM's 80% — with **deemed descoping of encumbrance-free land not provided 180 days after AD**. Enhancement projects (4→6 lane) carry lower risk than greenfield and can bid for **construction support up to 40% of project cost, paid in ten equal instalments** by NHAI.
- **A specific, checkable red flag:** *"Any situation wherein the penalty payable by the project contractor is less than the liability towards the proposed debt holders is viewed unfavourably."* Compare the liquidated-damages cap against the debt service it is meant to protect.
- **TOT (toll-operate-transfer) is assessed on the same basis as an operational toll road.**

**Portfolio diversification for InvITs and restricted groups:** geographic, traffic-driver and traffic-composition diversity reduce cross-correlation and cash-flow volatility. **Adding HAM/annuity assets to a toll portfolio improves it further**, because annuity income is stable and uncorrelated with traffic.

---

## 9. Expected Loss (EL) ratings — a SEPARATE SCALE this project does not currently support

**Source, read in full 06-Sep-2026:** `crisils-criteria-for-expected-loss-ratings-for-infrastructure-projects.md`.

### Why the scale exists

A conventional rating is an opinion on **probability of default alone**. That systematically under-rates infrastructure, because infra projects are funded with debt far shorter than their economic lives, go through unpredictable ramp-up, and suffer cash-flow mismatches from counterparty payment delay. CRISIL states the consequence plainly: *"even operational infrastructure projects that are fundamentally viable but face short-term liquidity crunch would have constrained credit ratings on the conventional rating scale"* — while *"the cash-flow mismatches… may not eventually translate into sizeable losses to the investors."* PPP projects in particular carry **termination payments and contractual protections** that cap ultimate loss.

So the same asset can be genuinely weak on PD and genuinely strong on loss. **Instruments with identical PD can have different LGD, and therefore different EL.** EL ratings are offered **only for the infrastructure sector** (plus municipal bonds financing infrastructure assets, per SEBI circular of May 2025), across the whole project life cycle, for both SPVs and infrastructure corporates.

### The scale — seven points, with published numeric bands

| Rating | Meaning | Indicative EL over the life of the instrument |
|---|---|---|
| **Crisil EL 1** | lowest expected loss | **≤ 1.25%** |
| **Crisil EL 2** | very low | **1.25% < X ≤ 3.5%** |
| **Crisil EL 3** | low | **3.5% < X ≤ 7.5%** |
| **Crisil EL 4** | moderate | **7.5% < X ≤ 15%** |
| **Crisil EL 5** | high | **15% < X ≤ 25%** |
| **Crisil EL 6** | very high | **25% < X ≤ 35%** |
| **Crisil EL 7** | highest | **> 35%** |

Aligned to SEBI's scale in July 2021; the pre-2021 symbols were `CRISIL INFRA EL 1-7` over identical bands.

**`Rating_Scorecard.xlsx` cannot express any of this.** `Ref_Scales` holds a long-term and a short-term scale only. An EL mandate cannot be run through the scorecard at all — it is not a scaling problem but a missing scale, and the workbook would silently print a conventional grade instead. Rate an EL mandate outside the scorecard, as the tool already requires for insurers.

### Computing it: EL = PD × LGD

CRISIL's own worked example — a 10-year zero-coupon bond rated `A` on the conventional scale:

| | |
|---|---|
| PD (from CRISIL's default statistics for `A`) | 5% |
| LGD (illustrative) | 30% |
| **EL = PD × LGD** | **1.5%** over the 10-year life → **EL 2** |
| Annualised EL | 0.15% |

**"Life of the instrument" = ORIGINAL maturity**, plus a possible cushion for recoveries arriving after maturity (relevant mainly for short instruments) — but **in no event may instrument life exceed project life**.

**Typical project lives CRISIL publishes:**

| Sector | Project life |
|---|---|
| Annuity roads · Toll roads · Sea ports | as per the concession agreement |
| **Solar** | **15-18 years** |
| **Wind** | **18-20 years** |
| **Thermal power** | **~25 years** |
| **Transmission** | **~35 years** |

### ⚠ PD and LGD are computed on DIFFERENT scenario sets — this is the conceptual trap

> *"The PD assessment typically assumes a **normal business course and base case conditions**… LGD assessment, on the other hand, incorporates **tail scenarios** to identify possible material events that may lead the asset into a default."*

Running one scenario set and reading both numbers off it is wrong in both directions: a base-case-only LGD understates loss because it never reaches the events that cause default, and a tail-only PD overstates default probability. CRISIL's thermal illustration:

| Base case (drives PD) | Tail scenario (drives LGD) |
|---|---|
| PPA, FSA and other legal agreements will be honoured | The agreements are not, or only partially, honoured → default |
| Counterparty payment delay does not stretch for a prolonged period | Payment delays stretch for a prolonged period → default |

### LGD is a two-step build: enterprise level, then instrument level

**Enterprise-level LGD**
1. **Identify the default events** — a mix of sector-specific (from sectoral trends) and asset-specific. Where the asset is near or already in default these can be estimated with high certainty; otherwise CRISIL estimates a relative probability for each from sector expertise and prevailing market, regulatory and economic conditions. **Each tail event is assumed mutually exclusive.**
2. **Pick a resolution strategy per event** — debt restructuring, business restructuring, asset sale, or liquidation — **selected on the asset's economic viability**: low viability points to **liquidation**; high viability points to **debt restructuring with liquidity support** (working capital or equity infusion). CRISIL assumes the **current liability structure stays in place until resolution**.
3. **Value the distressed asset per event**, on severity and cash-flow impact, residual value, production capacity, utilisation, cost structure, industry and macro conditions.
4. **Enterprise LGD per event** = distressed asset value against **total outstanding debt including accrued interest** at the time of default, assuming **a single class of debt and a consolidated entity structure**.
5. **Final enterprise LGD = the probability-weighted average** across all events.

**Instrument-level LGD** — because step 4's single-debt-class assumption breaks wherever there are multiple layers with distinct claim priority. **Loss is absorbed in order: equity first, then subordinated lenders, then senior lenders.** CRISIL then adjusts for collateral value on secured instruments, the insolvency regime, and operational or legal expenses needed to keep the asset alive.

**An EL rating moves if either PD or LGD moves.** LGD is explicitly not static — it differs between construction and operational stages, and shifts with credit and market conditions, regulatory frameworks and sectoral trends.
