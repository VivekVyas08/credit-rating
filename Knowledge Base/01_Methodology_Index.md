# 01 — METHODOLOGY INDEX · ICRA · CRISIL · CareEdge (ONE index, all three agencies)

> **Flow:** `UNIFIED_RATING_GUIDE.md` (root) is the 19-step process with a gate at every step. This file is the reference detail — **all three agencies in one place**.

**Which library you are in decides how you route:**

| | **ICRA** — `Methodology/` | **CRISIL** — `CRISIL/Methodology/` | **CareEdge** — `CareEdge/Methodology/` |
|---|---|---|---|
| Files | **120** | **20** | **73** |
| Structure | **One file per sector** + `960 Corporate` master | **Consolidated masters** — one file bundles many sectors as internal **Sections** | **One paper per sector** + a **Manufacturing** or **Services** base master |
| How to route | Pick the sector file + the master | Pick the FILE, then the **Section inside it** (each file has a Contents page) | Pick the base master + the sector paper (if one exists) |
| Always add | `927` ratios · `1014` liquidity · `934` consolidation · `963` support · `110` outlook · `134` default · `138` complexity | `basics-of-ratings` + `criteria-for-consolidation` | the always-on policy set (Default · Short Term Instruments · Financial Ratios – Non-financial · Outlook & Watch · Consolidation · Liquidity · Withdrawal) |
| Known gaps | archived files must not be used for new ratings (see §H) | — | **no sector paper** for FMCG, IT, mining, oil & gas, PV/2W/tractors, chemicals -> Manufacturing master alone |

**Sector -> methodology for all three agencies side by side: see `02_Sector_Routing_Map.md` Part A.**

---

# PART 1 — ICRA methodology library (120 files)

*Format: filename → when to use. ACTIVE unless marked (Archived). Archived files are retained for reference/learning but superseded versions or the Corporate Credit Rating Methodology apply for new ratings.*

> **Count note (de-duplicated 16-Jul-2026):** the library previously showed 123 files on disk, but three were **byte-identical download copies** (`4 (1).md`, `952~Mining … Jun 2025 (1).md`, `961~Foreign domiciled support … Jul 2025 (1).md`, each md5-verified identical to its twin) and were removed; `418~Issuer Rating Methodology, Jul 2005` had a stray `…(1).md` filename that was renamed to its clean published name. The library is now **120 distinct methodologies** — the figure used here and in `00`, the root guide, AGENCIES.md and SESSION_HANDOFF.

## A. Sector methodologies — Corporates (use WITH 960~Corporate Credit Rating Methodology)

| File | Sector trigger |
|---|---|
| 1000~Power (Thermal), Nov 2025 | Coal/gas-based power generators, IPPs |
| 1001~Power (Transmission), Nov 2025 | Power transmission licensees/SPVs |
| 999~Power (Distribution), Nov 2025 | Discoms, distribution franchisees |
| 991~Power (Solar and Wind), Jul 2025 | Renewable IPPs (solar, wind, hybrid) |
| 1002~Roads (Hybrid Annuity), Nov 2025 | HAM road SPVs |
| 1008~Roads (BOT Toll), Jan 2026 | Toll road concessionaires |
| 946~Roads (Annuity), Apr 2025 | Annuity road SPVs |
| 1019~Airports, May 2026 | Airport operators/concessionaires |
| 994~Ports, Aug 2025 | Port operators, terminals |
| 938~Project Finance, Nov 2024 | Under-construction/limited-recourse projects (any sector) |
| 992~InvITs | Infrastructure Investment Trusts |
| 932~Real Estate Investment Trusts, Nov 2024 | REITs |
| 933~Real Estate, Nov 2024 | Residential/commercial developers |
| 1020~Realty (Leasing), May 2026 | Lease-rental assets, LRD, office/retail/warehousing landlords |
| 930~Construction, Oct 2024 | EPC contractors, construction companies |
| 1010~Cement, Feb 2026 | Cement manufacturers |
| 953~Iron & Steel, Jun 2025 | Ferrous metals producers |
| 1016~Non-Ferrous Metals, Mar 2026 | Aluminium, copper, zinc producers |
| 952~Mining, Jun 2025 (two copies) | Mining entities |
| 993~Oil Exploration & Production, Aug 2025 | Upstream oil & gas |
| 955~Refining and Marketing, Jun 2025 | Oil refiners, OMCs |
| 959~City Gas Distribution, July 2025 | CGD companies |
| 1026~Chemicals, Jun 2026 | Chemical manufacturers (commodity & specialty); agrochemicals now here (919 archived) |
| 1015~Fertilisers, Mar 2026 | Urea and P&K fertiliser producers |
| 1011~Pharmaceuticals, Feb 2026 | Pharma formulations/API |
| 811~Diagnostic Service Providers, Jul 2022 | Diagnostic chains/labs |
| 928~Hospitals, Sep 2024 | Hospital chains, healthcare providers |
| 1012~FMCG, Feb 2026 | Fast-moving consumer goods |
| 809~Edible Oil, Jul 2022 | Edible oil refiners/solvent extraction |
| 1004~Sugar, Dec 2025 | Sugar mills (incl. distillery-integrated) |
| 947~Tea, Apr 2025 | Tea producers |
| 951~Rice Mills, Jun 2025 | Rice millers (basmati/non-basmati) |
| 1005~Tractors, Dec 2025 | Tractor manufacturers |
| 1006~Commercial Vehicles, Dec 2025 | CV manufacturers |
| 954~Passenger Cars, Jun 2025 | PV manufacturers |
| 942~Two Wheelers, Jan 2025 | 2W manufacturers |
| 931~Auto Components, Oct 2024 | Auto ancillaries/component suppliers |
| 1023~Automobile Dealers, Jun 2026 | Auto dealerships |
| 935~Construction Vehicles, Nov 2024 | Construction equipment makers |
| 1017~Textiles (Spinning), Mar 2026 | Yarn spinners |
| 1025~Textiles (Fabric), Jun 2026 | Fabric/weaving/processing |
| 1024~Textiles (Apparels), Jun 2026 | Garment makers, branded apparel retailers |
| 997~Footwear, Sep 2025 | Footwear makers/retailers |
| 996~Cut & Polished Diamonds, Sep 2025 | Diamond polishers/traders |
| 1018~Jewellery-Retail, Mar 2026 | Jewellery retailers (e.g. Titan) |
| 990~Retail, Jul 2025 | Organised retail (non-jewellery) |
| 989~Hotels, Jul 2025 | Hotels/hospitality |
| 988~IT (Software & Services), Jul 2025 | IT services companies |
| 957~Telecom Services, Jul 2025 | Telcos/mobile operators |
| 958~Telecom Towers, Jul 2025 | Tower companies |
| 1007~Print Media, Jan 2026 | Newspapers/print |
| 1009~TV Broadcasting, Jan 2026 | Broadcasters |
| 810~Shipping, Jul 2022 | Shipping companies |
| 943~Passenger Road Transport, Feb 2025 | Bus operators etc. |
| 1013~Higher Education, Feb 2026 | Universities, education trusts |
| 384~Trading Companies, 2012 | Trading businesses (old but not archived) |

## B. Financial sector methodologies (do NOT combine with 960)

| File | Trigger |
|---|---|
| 929~Banks & Financial Institutions, Oct 2024 | Banks, AIFIs, small finance banks |
| 1003~NBFCs, Dec 2025 | NBFCs, HFCs (651 HFC methodology archived), MFIs |
| 936~General Insurance, Nov 2024 | General insurers |
| 937~Life Insurance, Nov 2024 | Life insurers |
| 925~Primary Dealers, Jul 2024 | PDs |
| 926~Stockbroking & Allied Services, Aug 2024 | Brokers, wealth/capital-market intermediaries |
| 941~Investment Companies, Jan 2025 | Holding/investment companies |
| 1022~Mutual Funds, June 2026 | MF credit-quality ratings, capital-protection funds |
| 824~Alternative Investment Funds, Nov 2022 | AIFs |

## C. Structured finance

| File | Trigger |
|---|---|
| 950~Securitisation Transactions, Jun 2025 | PTCs, ABS/MBS |
| 940~Collateralised Debt Obligations, Dec 2024 | CDOs |
| 831~Pooled Loan Issuances, Nov 2022 | Pooled bond/loan structures |
| 944~Security Receipts, Feb 2025 | ARC security receipts |

## D. Public finance

| File | Trigger |
|---|---|
| 939~State Governments, Dec 2024 | State government ratings |
| 835~Urban Local Bodies, Dec 2022 | Municipal corporations/ULBs |

## E. Cross-cutting rating approaches (apply as relevant to any rating)

| File | Purpose |
|---|---|
| 960~Corporate Credit Rating Methodology, Jul 2025 | Master framework, all non-financial corporates |
| 927~Rating Approach, Financial Ratio Analysis, Sep 2024 | Ratio definitions/computations |
| 1014~Rating Approach, Liquidity Analysis (Non-Financial), Mar 2026 | Liquidity classification |
| 934~Rating Approach, Consolidation, Nov 2024 | Consolidated vs standalone |
| 963~Implicit Parent or Group Support, Jul 2025 | Support notching |
| 962~Explicit Third-Party Support, Jul 2025 | Guarantees/letters of comfort → (CE) ratings |
| 961~Foreign domiciled support provider, Jul 2025 (two copies) | Foreign parent support |
| 817~Partial Guarantee, Sep 2022 | Partial credit enhancement |
| 995~Structural Features, Sep 2025 | DSRA, escrow, waterfall, covenants (non-securitised) |
| 998~Hybrid Instruments, Nov 2025 | Perps, AT-I/Tier-II style hybrids, equity credit |
| 1021~Expected Loss, May 2026 | EL-scale ratings (infrastructure) |
| 418~Issuer Rating Methodology, Jul 2005 | Issuer (entity-level) ratings |
| 415~Commercial Papers (Archived) | CP — now governed by mapping.md linkage |
| mapping.md | LT↔ST rating mapping chart |

## F. Policies & process (compliance layer in every report)

| File | Purpose |
|---|---|
| 107~Policy on Provisional Ratings, Sep 2022 | Provisional ratings rules |
| 110~Policy on Rating Outlook and Rating Watch, Dec 2022 | Stable/Positive/Negative; Watch descriptors |
| 112~Policy for Review of Ratings, Feb 2023 | Surveillance/review timelines, appeals |
| 129~Confidentiality Policy, Oct 2024 | Information handling |
| 130~Policy on Outsourcing, Oct 2024 | Internal ops |
| 132~Policy re non-cooperation, Jan 2025 | INC category rules & report format |
| 134~Policy on Default Recognition, Jan 2025 | What counts as default, curing period, post-default upgrade |
| 135~Functioning of Rating Committee, Apr 2025 | Committee process |
| 136~Gift Entertainment Anti-Bribery Policy, May 2025 | Conduct |
| 138~Complexity Indicator, Dec 2025 | Simple/Moderately Complex/Highly Complex |
| 139~Managing Conflict of Interest, Jan 2026 | Disclosures |
| 140~Policy on Withdrawal of Ratings, Mar 2026 | Withdrawal rules |
| 49~SOP monitoring and recognition of defaults | Default monitoring ops |
| 50~Standardized and Uniform PD Benchmarks, Dec 2019 | PD benchmarks |
| 68~Periodicity of review of rating methodology, Feb 2020 | Methodology review cycle |
| ICRA's rating process.md | End-to-end process flowchart (mandate→surveillance) |
| 16_AACRA.md | ACRAA best practices checklist |

## G. Information-requirement checklists (what to ask the company for)

| File | Entity type |
|---|---|
| 1.md | Asset Reconstruction Companies |
| 2.md | Broking entities |
| 3.md | Corporate sector |
| 4.md, 4 (1).md | Insurance companies |
| 5.md | Banks and NBFCs |
| 6.md | Primary Dealers |
| 7.md | Public finance entities |
| 8.md | (general/other) |

## H. Archived (superseded — flag if user requests; do not use for new ratings)

| File | Superseded by |
|---|---|
| 368~Paper, Nov 2015 (Archived) | 960 Corporate |
| 415~Commercial Papers (Archived) | mapping.md linkage approach |
| 651~Housing Finance Companies, Sep 2019 (Archived) | 1003 NBFCs |
| 684~Insurance Hybrids, Jun 2020 (Archived) | 998 Hybrid Instruments |
| 712~IT-Hardware-related Services, Apr 2021 (Archived) | 988 IT / 960 |
| 830~Capital Protection-Oriented Funds, Nov 2022 (Archived) | 1022 Mutual Funds |
| 852~Wind Power Producers, Jul 2023 (Archived) | 991 Power (Solar and Wind) |
| 892~Oilfield Services, Nov 2021 (Archived) | 960 Corporate |
| 904~Media (Films), Jan 2022 (Archived) | 960 Corporate |
| 919~Agrochemicals, Jun 2024 (Archived) | 1026 Chemicals |

---

# PART 2 — CRISIL methodology library (20 consolidated masters)

*Format: filename → when to use. Unlike ICRA (one file per sector), Crisil publishes **consolidated master criteria** — one large document bundles many sectors as internal Sections. Route to the FILE first, then to the Section inside it (each file has a Contents page). All files are current published Crisil Ratings criteria (Crisil Ratings Limited, an S&P Global company).*

## A. The two workhorse masters (most corporate ratings start here)

| File | Internal coverage (Sections) | Use for |
|---|---|---|
| `criteria-for-manufacturing-trading-and-corporate-services-sector.md` (~300 KB) | I Manufacturing & corporate services (master framework) · II Trading companies · III Education institutions · IV **Financial ratios (non-financial)** · V Materials (cement, steel, metals, mining, chemicals) · VI Industrial sector · VII Automotive & auto components · VIII Consumer staples & discretionary (FMCG, retail, textiles) · IX Pharmaceuticals · X Software/IT · XI Mobile telephony · XII Oil & gas | ANY non-financial corporate. Section I + the sector Section + Section IV (ratios) together replace ICRA's "960 Corporate + sector methodology" pairing |
| `basics-of-ratings.md` (~214 KB) | I Rating scales · II Rating process · III Default recognition · V Information adequacy risk (INC) · VI Global↔domestic scale mapping · VIII Short-term debt · IX Fixed deposit programmes; also outlook & watch policy | Rating scales, process, outlook/watch, default/curing, ST instruments, FDs — Crisil's equivalent of ICRA's policy layer + mapping.md |

## B. Financial sector

| File | Coverage | Trigger |
|---|---|---|
| `criteria-for-banks-and-financial-institutions.md` | I Banks & FIs (CRAMEL framework) · II Basel III non-equity capital (AT-I, Tier-II) · III Basel II hybrids | Banks, SFBs, AIFIs and their capital instruments |
| `criteria-for-finance-and-securities-companies.md` | I Finance companies (NBFC/HFC) · III Securities/broking companies; includes financial-sector ratios & hybrids | NBFCs, HFCs, MFIs, brokers |
| `criteria-for-insurance-companies.md` | I General insurance · II Life insurance; incl. ratios & hybrids | Insurers |
| `criteria-for-credit-quality-ratings-of-bond-funds.md` | Bond fund credit quality ratings | Debt mutual fund schemes |
| `Criteria-for-rating-capital-potection-oriented-funds.md` | Capital-protection-oriented funds | CPO funds |
| `criteria-for-rating-intraday-borrowings-by-mutual-funds.md` | MF intraday borrowing lines | MF intraday facilities |
| `criteria-for-holding-companies.md` | Investment holding companies (share-cover approach) | Holdcos rated on portfolio value |

## C. Infrastructure & real assets

| File | Coverage | Trigger |
|---|---|---|
| `criteria-for-infrastructure-sectors.md` (~127 KB) | I Infra rating drivers (master) · II Power (gencos/transcos/discoms) · III Annuity & HAM roads · IV Toll roads | All infra corporates/SPVs; pair Section I with the asset Section |
| `crisils-criteria-for-expected-loss-ratings-for-infrastructure-projects.md` | EL scale, PD×LGD computation | Expected-loss ratings on infra projects |
| `crisil-ratings-criteria-for-reits-and-invits.md` | REITs and InvITs | Listed trusts |
| `criteria-for-real-estate-developers-lrd-and-cmbs.md` | Real estate developers · Lease Rental Discounting · CMBS | Developers, LRD, CMBS |

## D. Structured finance

| File | Coverage | Trigger |
|---|---|---|
| `criteria-for-securitisation-transactions.md` (~157 KB) | I Risk primer · II ABS · III CDO · IV RMBS · V Covered bonds | All securitisation / PTC ratings |
| `criteria-for-future-flow-transactions.md` | Future-flow securitisation | Future-receivable structures |
| `criteria-for-assigning-recovery-risk-ratings-to-security-receipts.md` | ARC security receipts (RR scale) | Security receipts |
| `criteria-for-independent-credit-evaluation-of-residual-debt-in-the-resolution-plans-for-stressed-assets.md` | ICE / RP-4 evaluations | Residual debt in IBC/RBI resolution plans |

## E. Cross-cutting analytical approaches (apply on top of B/C as relevant)

| File | Coverage | Trigger |
|---|---|---|
| `criteria-for-consolidation.md` | I Consolidation methodology · II Homogenous corporate groups | Whether/how to consolidate; group-average approach |
| `criteria-for-factoring-parent-group-government-linkages.md` | Parent, group and government support notch-ups/downs | Any entity with support linkages (Crisil's analogue of ICRA 963/962) |

## F. Public finance

| File | Coverage | Trigger |
|---|---|---|
| `criteria-for-public-finance.md` | Municipal/urban local bodies (I) · II State governments | ULBs, state govts |

## Routing quick-reference (Crisil vs ICRA mental map)

- ICRA "960 Corporate + sector file" → Crisil **manufacturing-trading master**: Section I + sector Section + Section IV ratios.
- ICRA policy layer (default, outlook, INC, ST mapping) → Crisil **basics-of-ratings** Sections.
- ICRA 929 Banks / 1003 NBFCs → Crisil **banks-and-FIs** / **finance-and-securities**.
- ICRA infra files (power/roads/airports/ports) → Crisil **infrastructure-sectors** master (power & roads have dedicated Sections; airports/ports use Section I drivers + manufacturing master where relevant).
- Rating scale prefix: `Crisil AAA … Crisil D`, `Crisil A1+ … A4, D` (per AGENCIES.md).

*House-style note: report format, section order and phrasing must be learned from `CRISIL/Report for Reference/` rationales, never assumed (AGENCIES.md rule 3). This index routes methodology only.*

---

# PART 3 — CareEdge methodology library (73 papers)

*Format: filename → when to use. CareEdge (CARE Ratings Ltd) publishes one criteria paper per sector — closer to ICRA's model than Crisil's consolidated masters. Sector papers are applied ON TOP of the relevant base master (Manufacturing or Services or Infrastructure or the financial-sector frameworks). Vintages: mostly the Feb–Mar 2025 refresh; a few older papers remain current (dated in filename). Rating scale: `CARE AAA … CARE D` / `CARE A1+ … A4, D`; deliverable tag `CARE`.*

## A. Base masters (start here for any corporate)

| File | Use for |
|---|---|
| `Criteria_Rating_Methodology_Manufacturing_Companies_March_2025.md` | Master framework for ALL manufacturers (business risk / financial risk / management); CareEdge's analogue of ICRA 960 |
| `Criteria_Rating_Methodology_Services_Sector_March_2025.md` | Master framework for services businesses (non-manufacturing corporates without their own paper) |

## B. Sector papers — corporates (apply WITH the A-master)

| File | Sector trigger |
|---|---|
| `CARE Ratings’ Criteria for Rating Cement Companies September 2024.md` | Cement |
| `CARE_Ratings_criteria_for_Iron_&_Steel_Feb_2025.md` | Ferrous metals |
| `Rating Methodology - Non - Ferrous Metals September 2024.md` | Aluminium, copper, zinc |
| `Criteria Paper Fertilizer May 2024.md` | Fertilisers |
| `Criteria_Rating_Methodology_Pesticides_Agrochemicals.md` | Agrochemicals |
| `Criteria_Rating Methodology Pharmaceutical Sector January 2025.md` | Pharma formulations/API |
| `Criteria_Rating_Methodology_Paper_and_Paper_Products_March_2025.md` | Paper |
| `Rating Methodology - Cotton Textile Manufacturing - December 2024.md` | Cotton textiles/spinning |
| `Rating Methodology Cut and Polished Diamond Industry - December 2024.md` | CPD/gems |
| `Rating_Methodology_Sugar_Sector_March_2025.md` | Sugar mills |
| `Rating Methodology - Auto Components & Equipments 2025.md` | Auto ancillaries |
| `Rating-Methodology-Commercial-Vehicle-Industry-Feb-2025.md` | CV manufacturers |
| `Criteria_Auto-Dealership-Criteria-Dec-2025.md` | Auto dealerships |
| `Criteria_Rating Methodology - Organized Retail Companies January 2025.md` | Organised retail |
| `Criteria_Rating_Methodology_Wholesale_Trading_Mar_2025.md` | Trading companies |
| `Criteria_Rating_Methodology_Hotel_Industry_Feb_2025.md` | Hotels |
| `Criteria_Hospital_Criteria_Paper.md` | Hospitals/healthcare |
| `Rating Methodology - Education Sector December 2024.md` | Schools, universities, edu trusts |
| `Criteria_Rating_Methodoloy_Shipping_companies_March_2025.md` | Shipping |
| `Criteria_Rating_Methodology_Mobile_Service_Providers_March_2025.md` | Telecom operators |
| `Criteria_Rating_Methodology_City_Gas_Distribution_Companies_March_2025.md` | CGD |
| `Criteria_Rating_Methodology_Construction_Sector_March_2025.md` | EPC/construction |
| `Criteria_Rating_Methodology_Real_Estate_Sector_Feb_2025.md` | Developers |
| `REIT Methodology January 2025.md` | REITs |

## C. Infrastructure & project finance

| File | Trigger |
|---|---|
| `Criteria-Methodology-Infrastructure-Sector-Ratings-Mar-2025.md` | Infra master — read WITH the asset paper below |
| `Rating Methodology - Power Generation Projects_Sept2020.md` | Generic power gencos/IPPs |
| `Rating Methodology  Thermal Power Producers - December 2024.md` | Thermal gencos |
| `Rating-Methodology-Solar-Power-Projects-December-2024.md` | Solar IPPs |
| `Rating Methodology - Wind Power Projects - December 2024.md` | Wind IPPs |
| `Rating-Methodology–Power-Transmission-March-2025.md` | Transmission licensees |
| `Criteria-Methodology-Power-Distribution-Companies-March-2025.md` | Discoms |
| `Toll-Road-Projects-March 2025.md` | BOT toll roads |
| `Hybrid-Annuity-Road-Projects-March-2025.md` | HAM road SPVs |
| `Rating-Methodology–Road–Assets-Annuity–March–2025.md` | Annuity roads |
| `Rating–Methodology-Airport–Companies–March-2025.md` | Airports |
| `Rating-Methodology-Port-and-Port-Services-March-2025.md` | Ports |
| `Criteria_Rating_Methodology_Urban_Infrastructure_March_2025.md` | Urban infra (water, metro, city assets) |
| `Criteria_Rating_Methodology_Infrastructure_Investment_Trusts_(InvITs)_March_2025.md` | InvITs |
| `Expected_Loss_Ratings_for_Infrastructure_Projects_Nov_2025.md` | EL-scale infra ratings |
| `Project_Stage_Entities_Feb_2025.md` | Under-construction / project-stage entities (any sector) |

## D. Financial sector (do NOT combine with A-masters)

| File | Trigger |
|---|---|
| `Criteria_Rating_Methodology_Banks_March_2025.md` | Banks, SFBs, RRBs (CAMELS-style quantitative + qualitative) |
| `hybrid-Instruments-issued-by-Banks-March-2025.md` | Basel III AT-I / Tier-II instruments |
| `Criteria_CARE_NBFC_Criteria_February_2025.md` | NBFCs, MFIs |
| `Criteria_Rating_Methodology_Housing_Finance_Companies_March_2025.md` | HFCs |
| `Criteria_Rating_Methodology_Financial_Ratios_Financial_Sector_February_2025.md` | Ratio definitions — financial sector (pair with Banks/NBFC/HFC papers) |
| `criteria-broking-criteria-december-2025.md` | Brokers, capital-market intermediaries |
| `Rating-of-Investment-Holding-Companies-Debt-March-2025.md` | Holdcos rated on portfolio/share cover |
| `Non-Life-Insurance-Sector-March-2025.md` | General insurers |
| `Financial-Ratios–Insurance-Sector.md` | Ratio definitions — insurance |
| `Rating-Methodology-Financial-Ratios-Life-Insurance-Sector-March-2025.md` | Ratio definitions — life insurance |
| `Criteria_Rating_Methodology_Fund_Credit_Quality_Rating_March_2025.md` | Debt MF scheme credit-quality ratings |
| `Criteria_CARE_Ratings_criteria_for_rating_of_Capital_Protection_Oriented_Mutual_Fund_Schemes_March_2025.md` | CPO fund schemes |
| `CARE_Ratings_criteria_for_rating_of_Market_Linked_Debentures_Feb_2025.md` | MLDs (PP-MLD prefix) |

## E. Structured finance & credit enhancement

| File | Trigger |
|---|---|
| `Criteria_Asset-Mortgage-Backed-Securitisation-Transactions-March-2025.md` | ABS / MBS / PTC securitisation |
| `Criteria-Pools-Backed-by-Wholesale-Assets-March-2023.md` | Wholesale-asset pools |
| `Criteria_Rating_Methodology_Debt_Backed_by_Lease_Rentals_Discounting_Feb_2025.md` | LRD debt |
| `Criteria_on_rating_credit_enhanced_debt_march_2025.md` | Guaranteed / credit-enhanced (CE) debt |
| `Rating_Methodology_Recovery_Ratings_March_2025.md` | ARC security receipts (recovery ratings) |
| `Independent-Credit-Evaluation-of-Residual-Debt-March-2025.md` | ICE of residual debt in resolution plans |

## F. Public finance

| File | Trigger |
|---|---|
| `Criteria_Rating_Methodology_State_Governments_March_2025.md` | State government ratings |

## G. Cross-cutting approaches (apply as relevant to any rating)

| File | Purpose |
|---|---|
| `Consolidation-and-Combined-Approach-March-2025.md` | Consolidated vs standalone; combined approach for group entities |
| `Notching_by_Factoring_Linkages_with_Parent_Jan_2025.md` | Parent/group support notching |
| `Notching by Factoring Linkages with Govt_Jan 2025.md` | Government support notching |
| `Issuer_Ratings_Feb_2025.md` | Entity-level issuer ratings |
| `Rating_of_Short_Term_Instruments_Feb_2025.md` | CP/ST instruments, LT↔ST linkage |

## H. Policies & process (compliance layer in every report)

| File | Purpose |
|---|---|
| `Assigning Outlook or Rating Watch to Credit Ratings.md` | Stable/Positive/Negative; Watch descriptors |
| `Policy-on-Withdrawal-of-Ratings_Oct-2025.md` | Withdrawal rules |
| `Policy on Curing Period_Dec 2024.md` | Default cure & post-default upgrade timelines |
| `Policy-on-Assignment-of-Provisional-Ratings_Dec-2025.md` | Provisional ratings |
| `Information_Adequacy_Risk-and-INC_Nov-2025.md` | Issuer-not-cooperating rules & best-available-information ratings |
| `Analytical treatment of restructuring - COVID-Revised (15-7-22).md` | Restructured-debt treatment |

## Known gaps (route to the closest master until CareEdge papers are added)

- No standalone **financial-ratios paper for non-financial corporates** — ratio guidance sits inside the Manufacturing/Services masters (financial-sector, insurance and life-insurance ratios have their own papers in D).
- No dedicated papers for **FMCG, IT/software, mining, oil & gas upstream/refining, passenger vehicles, two-wheelers, tractors** — use the Manufacturing master (B applies only where a sector paper exists).
- No **ULB/municipal** paper (only State Governments) and no **covered bonds / CDO** papers.

*House-style note: report format = CareEdge press-release style — learn section order ("Rationale", "Key Rating Drivers"/strengths-weaknesses, "Analytical Approach", "Applicable Criteria", "Liquidity", annexures with instrument details) from `CareEdge/Report for Reference/` (803 published rationales), never from memory. Every report's "Applicable Criteria" list should name the exact papers used from this index.*
