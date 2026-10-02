# 02 — SECTOR ROUTING MAP · ICRA · CRISIL · CareEdge (ONE map, all three agencies)

> **Flow:** `UNIFIED_RATING_GUIDE.md` (root). This file is the routing LOOKUP for all three agencies.

*Part A = conceptual routing (sector -> methodology, all three side by side). Part B = empirical routing: what each agency ACTUALLY cited, pivoted by company so you see all three at once. **1220 companies** (de-duplicated 16-Jul-2026 — 24 name-variant / duplicate-report rows merged, e.g. "&"/"and", erstwhile/formerly renames, Co/Company, and `Rationale-…` slug rows whose reports were byte-content-identical to a clean-named report), of which **320 are covered by more than one agency** — those rows are the cross-agency gold: they show how the same issuer routes differently per agency.*

**Limitations:** (1) criteria names are as cited at each report's publication date — map to the CURRENT file via `01_Methodology_Index`; (2) ICRA rows come from 491 parsed reports (older-format/INC reports could not be parsed — absence means nothing); (3) a company's past routing is not binding — if its business mix changed (demerger, new dominant segment), re-derive from the current profile; (4) extraction is automated — verify against the company's own latest report before use; (5) a few automated sector tags are spurious (a manufacturer/telecom cannot have cited "Banks"/"Cement" criteria — such tokens are extraction noise), so treat any single surprising tag as noise pending verification. **Routing use only: per R2 these reference reports never supply data.**

## Part A — Conceptual routing: sector -> methodology, ALL THREE AGENCIES side by side

*Pick the row for the company's business; read across for whichever agency you are rating on. Always verify the file's own scope statement before citing it (failure mode 4).*

| Sector / entity type | **ICRA** (one file per sector + `960` master) | **CRISIL** (consolidated master -> internal Section) | **CareEdge** (base master + sector paper) |
|---|---|---|---|
| **Generic / diversified corporate** | `960 Corporate Credit Rating Methodology` | `manufacturing-trading-and-corporate-services` -> **I** (master) + **IV** (ratios) | `Manufacturing Companies` **or** `Services Sector` master |
| Cement | `1010 Cement` | master -> **V Materials** | `Criteria for Rating Cement Companies` |
| Iron & steel | `953 Iron & Steel` | master -> **V Materials** | `CARE_Ratings_criteria_for_Iron_&_Steel` |
| Non-ferrous metals | `1016 Non-Ferrous Metals` | master -> **V Materials** | `Rating Methodology - Non-Ferrous Metals` |
| Mining | `952 Mining` | master -> **V Materials** | *(no paper — Manufacturing master alone)* |
| Chemicals | `1026 Chemicals` | master -> **V Materials** | *(no paper — Manufacturing master alone)* |
| Agrochemicals | *(in `1026 Chemicals`; `919` archived)* | master -> **V Materials** | `Pesticides_Agrochemicals` |
| Fertilisers | `1015 Fertilisers` | master -> **V Materials** | `Criteria Paper Fertilizer` |
| Pharmaceuticals | `1011 Pharmaceuticals` | master -> **IX Pharmaceuticals** | `Rating Methodology Pharmaceutical Sector` |
| Hospitals | `928 Hospitals` | master -> corporate services | `Hospital_Criteria_Paper` |
| Diagnostics | `811 Diagnostic Service Providers` | master -> corporate services | *(no paper — Services master)* |
| FMCG | `1012 FMCG` | master -> **VIII Consumer staples & discretionary** | *(no paper — Manufacturing master alone)* |
| Retail (organised) | `990 Retail` | master -> **VIII** | `Organized Retail Companies` |
| Jewellery retail | `1018 Jewellery-Retail` | master -> **VIII** | *(no paper — Manufacturing/Services master)* |
| Textiles (spinning/fabric/apparel) | `1017` / `1025` / `1024` | master -> **VIII** | `Cotton Textile Manufacturing` |
| Sugar | `1004 Sugar` | master -> **V Materials** | `Rating_Methodology_Sugar_Sector` |
| Edible oil | `809 Edible Oil` | master -> **VIII** | *(no paper)* |
| Tea / rice mills | `947 Tea` / `951 Rice Mills` | master -> **VIII** | *(no paper)* |
| Auto OEM (PV / CV / 2W / tractors) | `954` / `1006` / `942` / `1005` | master -> **VII Automotive** | `Commercial-Vehicle-Industry` *(PV/2W/tractors: no paper)* |
| Auto components | `931 Auto Components` | master -> **VII** | `Auto Components & Equipments` |
| Auto dealership | `1023 Automobile Dealers` | master -> **VII** | `Auto-Dealership-Criteria` |
| IT / software services | `988 IT (Software & Services)` | master -> **X Software** | *(no paper — Services master alone)* |
| Telecom services | `957 Telecom Services` | master -> **XI Mobile telephony** | `Mobile_Service_Providers` |
| Telecom towers | `958 Telecom Towers` | `infrastructure-sectors` -> I | *(no paper — Infra master)* |
| Oil & gas (E&P / refining) | `993` / `955` | master -> **XII Oil & gas** | *(no paper — Manufacturing master alone)* |
| City gas distribution | `959 City Gas Distribution` | master -> **XII** | `City_Gas_Distribution_Companies` |
| Paper & packaging | *(`368` archived -> `960`)* | master -> **V Materials** | `Paper_and_Paper_Products` |
| Cut & polished diamonds | `996 Cut & Polished Diamonds` | master -> **VIII** | `Cut and Polished Diamond Industry` |
| Hotels | `989 Hotels` | master -> corporate services | `Hotel_Industry` |
| Education | `1013 Higher Education` | master -> **III Education institutions** | `Education Sector` |
| Shipping | `810 Shipping` | master -> corporate services | `Shipping_companies` |
| Trading / distribution | `384 Trading Companies` | **II Trading companies** | `Wholesale_Trading` |
| Construction / EPC | `930 Construction` | `infrastructure-sectors` -> I | `Construction_Sector` |
| Real estate developer | `933 Real Estate` | `real-estate-developers-lrd-and-cmbs` | `Real_Estate_Sector` |
| Lease rental discounting | `1020 Realty (Leasing)` | `real-estate-developers-lrd-and-cmbs` | `Debt_Backed_by_Lease_Rentals_Discounting` |
| REIT / InvIT | `932 REITs` / `992 InvITs` | `crisil-ratings-criteria-for-reits-and-invits` | `REIT Methodology` / `Infrastructure_Investment_Trusts` |
| **Bank / SFB / AIFI** | `929 Banks & FIs` **ALONE** (hybrids inside it) | `criteria-for-banks-and-financial-institutions` (CRAMEL) | `Rating_Methodology_Banks` + `hybrid-Instruments-issued-by-Banks` + `Financial Ratios - Financial Sector` |
| **NBFC / MFI** | `1003 NBFCs` | `finance-and-securities-companies` -> **I** | `CARE_NBFC_Criteria` + Financial-sector ratios |
| **HFC** | `1003 NBFCs` (`651` archived) | `finance-and-securities-companies` -> **I** | `Housing_Finance_Companies` |
| Broking / securities | `926 Stockbroking & Allied` | `finance-and-securities-companies` -> **III** | `criteria-broking-criteria` |
| Investment / holding co | `941 Investment Companies` | `criteria-for-holding-companies` | `Rating-of-Investment-Holding-Companies-Debt` |
| Mutual fund / bond fund | `1022 Mutual Funds` | `credit-quality-ratings-of-bond-funds` | `Fund_Credit_Quality_Rating` |
| **General insurance** | `936 General Insurance` | `criteria-for-insurance-companies` -> I | `Non-Life-Insurance-Sector` + insurance ratios |
| **Life insurance** | `937 Life Insurance` | `criteria-for-insurance-companies` -> II | `Financial-Ratios-Life-Insurance-Sector` |
| Power — thermal | `1000 Power (Thermal)` | `infrastructure-sectors` -> **II Power** | `Thermal Power Producers` |
| Power — solar/wind | `991 Power (Solar and Wind)` | `infrastructure-sectors` -> **II** | `Solar-Power-Projects` / `Wind Power Projects` |
| Power — transmission | `1001 Power (Transmission)` | `infrastructure-sectors` -> **II** | `Power-Transmission` |
| Power — distribution | `999 Power (Distribution)` | `infrastructure-sectors` -> **II** | `Power-Distribution-Companies` |
| Roads — toll | `1008 Roads (BOT Toll)` | `infrastructure-sectors` -> **IV Toll** | `Toll-Road-Projects` |
| Roads — HAM / annuity | `1002` / `946` | `infrastructure-sectors` -> **III** | `Hybrid-Annuity-Road-Projects` / `Road-Assets-Annuity` |
| Airports | `1019 Airports` | `infrastructure-sectors` -> I | `Airport-Companies` |
| Ports | `994 Ports` | `infrastructure-sectors` -> I | `Port-and-Port-Services` |
| Urban infrastructure | `835 Urban Local Bodies` | `criteria-for-public-finance` -> I | `Urban_Infrastructure` |
| **Under-construction project** | `938 Project Finance` | `infrastructure-sectors` -> I | `Project_Stage_Entities` |
| Expected-loss infra rating | `1021 Expected Loss` | `crisils-criteria-for-expected-loss-ratings` | `Expected_Loss_Ratings_for_Infrastructure_Projects` |
| **Securitisation (ABS/RMBS/PTC)** | `950 Securitisation` | `criteria-for-securitisation-transactions` -> II/IV | `Asset-Mortgage-Backed-Securitisation` |
| CDO | `940 CDOs` | securitisation -> **III CDO** | *(no paper)* |
| Pooled loans / wholesale pools | `831 Pooled Loan Issuances` | securitisation | `Pools-Backed-by-Wholesale-Assets` |
| Security receipts | `944 Security Receipts` | `recovery-risk-ratings-to-security-receipts` | `Rating_Methodology_Recovery_Ratings` |
| Future flow | *(`995 Structural Features`)* | `criteria-for-future-flow-transactions` | *(no paper)* |
| Credit-enhanced / guaranteed debt | `962 Explicit Third-Party Support` / `817 Partial Guarantee` | `factoring-parent-group-government-linkages` | `Criteria_on_rating_credit_enhanced_debt` |
| ICE / residual debt | *(n/a)* | `independent-credit-evaluation...stressed-assets` | `Independent-Credit-Evaluation-of-Residual-Debt` |
| **State government** | `939 State Governments` | `criteria-for-public-finance` -> II | `State_Governments` |
| **CROSS-CUTTING (any rating)** | `927` ratios · `1014` liquidity · `934` consolidation · `963`/`962` support · `995` structural · `998` hybrids · `110` outlook · `134` default · `mapping.md` · `138` complexity | `basics-of-ratings` (scales/process/default/ST) · `criteria-for-consolidation` · `factoring-parent-group-government-linkages` | Default · `Rating of Short Term Instruments` · `Financial Ratios - Non financial` · Outlook & Watch · `Consolidation-and-Combined-Approach` · Liquidity · Withdrawal · `Notching...Parent`/`...Govt` |

---

## Part B — Empirical routing, pivoted: what each agency actually cited, per company

| Company | ICRA cited | CRISIL cited | CareEdge cited |
|---|---|---|---|
| 20 Microns Limited | Corporate Credit Rating Methodology; Chemicals | Manufacturing/Trading/Corporate Services (master) | — |
| 360 ONE WAM Limited | Non-Banking Finance Companies (NBFCs) | — | Services Sector (master); Broking |
| 5Paisa Capital Limited | — | Finance & Securities Companies | — |
| A B Cotspin India Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| AADHAR HOUSING FINANCE LIMITED | Non-banking Finance Companies (NBFCs) | — | Housing Finance Companies |
| Aarti Drugs Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Pharmaceutical |
| Aarti Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Aarti Pharmalabs Ltd. | — | Manufacturing/Trading/Corporate Services (master) | — |
| Aarti Surfactants Limited | — | — | Manufacturing Companies (master) |
| Aavas Financiers Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies | — | Housing Finance Companies |
| ABB India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| ABS Marine Services Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| ACC Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Accelya Solutions India Limited | Rating Methodology for Entities in the information Technology (IT) Services | — | — |
| Accent Microcell Limited | — | — | Manufacturing Companies (master) |
| ACME Solar Holdings Limited | Corporate Credit Rating Methodology; Power-Solar and Wind | Infrastructure sectors | — |
| Action Construction Equipment Ltd. | Corporate Credit Rating Methodology; Construction vehicles; Tractors | — | — |
| ACUTAAS CHEMICALS LIMITED | — | — | Manufacturing Companies (master); Pharmaceutical |
| Adani Energy Solutions Limited | Corporate Credit Rating Methodology; Power Transmission | — | — |
| Adani Enterprises Limited | Airports | — | Manufacturing Companies (master); Services Sector (master); Roads/Toll/HAM; Airport; Wholesale Trading |
| Adani Green Energy Limited | — | — | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Adani Ports and Special Economic Zone Limited | Corporate Credit Rating Methodology; Ports | — | Services Sector (master); Infrastructure; Port |
| Adani Power Limited | — | Infrastructure sectors | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Adani Total Gas Limited | City Gas Distribution; Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | Infrastructure; City Gas |
| ADF Foods Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Aditya Birla Capital Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies (NBFCs) | — | — |
| Aditya Birla Fashion and Retail Limited | Retail | — | — |
| Aditya Birla Lifestyle Brands Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Aditya Birla Real Estate Limited | — | Real Estate / LRD / CMBS | Real Estate; LRD |
| Aditya Birla Sun Life AMC Limited | Mutual Funds | — | — |
| Aditya Infotech Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Aditya Vision Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ador Welding Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| Advance Agrolife Limited | — | — | Manufacturing Companies (master); Chemicals; Agrochemical |
| ADVANCED ENZYME TECHNOLOGIES LIMITED | Corporate Credit Rating Methodology; Pharmaceuticals | Manufacturing/Trading/Corporate Services (master) | — |
| Aegis Logistics Limited | — | — | Services Sector (master) |
| Aequs Limited | — | — | Manufacturing Companies (master) |
| Afcons Infrastructure Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Agarwal Industrial Corporation Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| AGI Greenpac Limited | — | — | Manufacturing Companies (master) |
| AGI Infra Limited | — | — | Manufacturing Companies (master); Real Estate |
| Ahluwalia Contracts (India) Limited | — | — | Infrastructure; Construction |
| AIA Engineering Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Aion-Tech Solutions Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ajanta Pharma Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Ajax Engineering Limited | Corporate Credit Rating Methodology; Construction vehicles | — | — |
| Akme Fintrade (India) Limited | — | — | NBFC |
| Akums Drugs & Pharmaceuticals Limited | Pharmaceuticals; Corporate Credit Rating Methodology | — | — |
| Alankit Limited | — | — | Services Sector (master) |
| Albert David Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Alembic Limited | Corporate Credit Rating Methodology; Investment Companies | — | — |
| Alembic Pharmaceuticals Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Pharmaceutical |
| Alicon Castalloy Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Alkem Laboratories Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Pharmaceutical |
| Alkyl Amines Chemicals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| All Time Plastics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Allcargo Logistics Limited | — | Manufacturing/Trading/Corporate Services (master) | Services Sector (master) |
| Allcargo Terminals limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Allied Digital Services Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Almondz Global Securities Limited | — | — | Services Sector (master) |
| Alok Industries Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| Alpex Solar Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Amanta Healthcare Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Amara Raja Energy & Mobility Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Amber Enterprises India Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| Ambika Cotton Mills Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ambuja Cements Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Cement |
| Amines and Plasticizers Limited | Corporate Credit Rating Methodology; Chemicals | — | — |
| Anand Rathi Share and Stock Brokers Limited | Stockbroking & Allied Services | Finance & Securities Companies | Broking |
| Anant Raj Limited | — | Real Estate / LRD / CMBS | — |
| Andhra Paper Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master); Paper |
| Angel One Limited | Stockbroking & Allied Services | Finance & Securities Companies | Broking |
| Anjani Portland Cement Limited | — | — | Manufacturing Companies (master); Cement |
| Anlon Healthcare Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Anthem Biosciences Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Antony Waste Handling Cell Limited | — | — | Services Sector (master) |
| Anuh Pharma Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Anupam Rasayan India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Apar Industries Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Apcotex Industries Limited | Corporate Credit Rating Methodology; Chemicals | — | Manufacturing Companies (master) |
| Apeejay Surrendra Park Hotels Limited | Corporate Credit Rating Methodology; Hotels | — | — |
| APL Apollo Tubes Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Iron & Steel; Wholesale Trading |
| Apollo Hospitals Enterprise Limited | Corporate Credit Rating Methodology; Hospitals | Manufacturing/Trading/Corporate Services (master) | — |
| Apollo Pipes Limited | Corporate Credit Rating Methodology | — | — |
| Apollo Tyres Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Aptus Value Housing Finance India Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies | — | Housing Finance Companies |
| Archean Chemical Industries Limited | Rating Methodology for Entities in the Chemical Industry | Manufacturing/Trading/Corporate Services (master) | — |
| Arfin India Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Arman Financial Services Limited | Rating Methodology for Securitisation Transactions | — | NBFC |
| Artemis Medicare Services Limited | — | — | Hospital |
| Arvind Fashions Limited | — | — | Retail; Wholesale Trading |
| Asahi India Glass Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Asahi Songwon Colors Limited | — | — | Manufacturing Companies (master) |
| Ashiana Housing Limited | Corporate Credit Rating Methodology; Realty–Commercial/Residential/Retail | — | Real Estate |
| Ashok Leyland Limited | Corporate Credit Rating Methodology; Commercial Vehicles | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Ashoka Buildcon Limited | Corporate Credit Rating Methodology; Construction | Manufacturing/Trading/Corporate Services (master) | Infrastructure; Construction |
| Asian Energy Services Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Asian Paints Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| ASK Automotive Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Associated Alcohols & Breweries Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Astec LifeSciences Limited | Corporate Credit Rating Methodology; Rating Methodology for Entities in the Agrochemicals Industry | — | — |
| Aster DM Healthcare Limited | Corporate Credit Rating Methodology; Hospitals | — | — |
| Astra Microwave Products Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Astral Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Atlanta Electricals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Atul Auto Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| AU Small Finance Bank Limited | Securitisation Transactions | Banks & Financial Institutions | Banks |
| Aurionpro Solutions Limited | — | Manufacturing/Trading/Corporate Services (master) | Services Sector (master) |
| Australian Premium Solar (India) Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| AUTHUM INVESTMENT & INFRASTRUCTURE LIMITED | Securitisation Transactions | Banks & Financial Institutions; Finance & Securities Companies | — |
| Automotive Axles Limited | Corporate Credit Rating Methodology; Rating Methodology for Auto Components | — | — |
| Automotive Stampings and Assemblies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Avadh Sugar & Energy Limited | Rating Methodology for Entities in the Sugar Industry | — | Manufacturing Companies (master); Sugar |
| Avalon Technologies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Avantel Limited | — | — | Manufacturing Companies (master) |
| Avenue Supermarts Limited | Corporate Credit Rating Methodology; Retail | Manufacturing/Trading/Corporate Services (master) | — |
| AVT Natural Products Limited | Corporate Credit Rating Methodology | — | — |
| AWL Agri Business Limited | — | — | Manufacturing Companies (master) |
| Axis Bank Limited | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| Axiscades Technologies Limited | — | — | Manufacturing Companies (master) |
| AYM Syntex Limited | — | — | Manufacturing Companies (master) |
| Azad Engineering Limited | — | — | Manufacturing Companies (master) |
| B. L. Kashyap and Sons Limited | Corporate Credit Rating Methodology; Construction | — | — |
| Baazar Style Retail Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Bafna Pharmaceuticals Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Bajaj Auto Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Bajaj Electricals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Bajaj Finance Limited | Non-banking Finance Companies (NBFCs) | Finance & Securities Companies | NBFC |
| Bajaj Housing Finance Limited | — | Finance & Securities Companies | — |
| Bajel Projects Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Balaji Phosphates Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Balkrishna Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Balmer Lawrie & Company Limited | Corporate Credit Rating Methodology; Chemicals | — | Manufacturing Companies (master); Services Sector (master) |
| Balrampur Chini Mills Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Balu Forge Industries Limited | Corporate Credit Rating Methodology | — | — |
| Banco Products (India) Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Bandhan Bank Limited | ICRA’s Rating Methodology for Banks and Financial Institutions | — | — |
| Bank of Baroda | — | Banks & Financial Institutions | — |
| Bank of India | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| Bank of Maharashtra | ICRA’s Rating Methodology for Banks and Financial Institutions | — | Banks |
| Bannari Amman Sugars Limited | — | — | Manufacturing Companies (master); Sugar |
| Bansal Wire Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| BASF India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Basilic Fly Studio Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Belrise Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| BEML Limited | Rating Methodology for Construction Equipment Manufacturers | — | Manufacturing Companies (master) |
| Best Agrolife Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Chemicals; Agrochemical |
| Beta Drugs Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| BGR Energy Systems Limited | — | — | Manufacturing Companies (master) |
| Bhageria Industries Limited | — | — | Manufacturing Companies (master) |
| Bhagiradha Chemicals and Industries Limited | — | — | Manufacturing Companies (master); Agrochemical |
| Bhagyanagar India Limited | — | — | Manufacturing Companies (master) |
| Bharat Bijlee Limited | Corporate Credit Rating Methodology | — | — |
| Bharat Dynamics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Bharat Forge Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Bharat Gears Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Bharat Heavy Electricals Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Construction |
| Bharat Petroleum Corporation Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Bharat Rasayan Limited | — | — | Manufacturing Companies (master); Chemicals; Agrochemical |
| Bharat Seats Limited | Corporate Credit Rating Methodology; Auto Components | — | — |
| Bharat Wire Ropes Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| BHARTI AIRTEL LIMITED | — | — | Infrastructure; Mobile/Telecom |
| Bhartiya International Limited | Corporate Credit Rating Methodology | — | — |
| Bikaji Foods International Limited | Corporate Credit Rating Methodology; FMCG | — | — |
| Billionbrains Garage Ventures Limited | Stockbroking & Allied Services | — | NBFC; Broking |
| Biocon Limited | Corporate Credit Rating Methodology; Pharmaceuticals | Manufacturing/Trading/Corporate Services (master) | — |
| Birla Cable Limited | — | — | Manufacturing Companies (master) |
| Birla Corporation Limited | Corporate Credit Rating Methodology; Cement | — | Manufacturing Companies (master); Cement |
| BirlaNu Limited | Corporate Credit Rating Methodology | — | — |
| Birlasoft Limited | — | — | Manufacturing Companies (master) |
| Blackbuck Limited | Corporate Credit Rating Methodology | — | — |
| Bliss GVS Pharma Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Blue Dart Express Limited | Corporate Credit Rating Methodology | — | — |
| Blue Jet Healthcare Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Blue Star Limited | — | — | Manufacturing Companies (master) |
| BMW Ventures Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Bombay Super Hybrid Seeds Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Borosil Limited | Corporate Credit Rating Methodology | — | — |
| Borosil Scientific Limited | — | — | Manufacturing Companies (master) |
| Brigade Enterprises Limited | Corporate Credit Rating Methodology; Realty–Commercial/Residential/Retail; Realty–Lease Rental Discounting (LRD); Rating Methodology–Hotels | Real Estate / LRD / CMBS | — |
| Brigade Hotel Ventures Limited | Corporate Credit Rating Methodology; Hotels | — | — |
| Britannia Industries Limited | FMCG | Manufacturing/Trading/Corporate Services (master) | — |
| Brooks Laboratories Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Campus Activewear Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Can Fin Homes Limited | Rating Methodology for Non-banking Finance Companies | — | Housing Finance Companies |
| Canara Bank | — | Banks & Financial Institutions | Banks |
| Canara HSBC Life Insurance Company Limited | — | — | Insurance |
| Canara Robeco Asset Management Company Limited | Mutual Funds | — | — |
| Capital Small Finance Bank Limited | — | — | Banks |
| Carborundum Universal Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Carysil Limited | Corporate Credit Rating Methodology | — | — |
| CEAT Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Ceigall India Limited | — | Infrastructure sectors | — |
| Central Bank of India | ICRA’s Rating Methodology for Banks and Financial Institutions | — | Banks |
| Centum Electronics Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Century Enka Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Century Plyboards (India) Ltd | Corporate Credit Rating Methodology | — | — |
| Cera Sanitaryware Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| CESC Limited | Corporate Credit Rating Methodology; Power-Solar and wind; Power-Thermal | — | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Chalet Hotels Limited | Corporate Credit Rating Methodology; Hotel Industry; Realty–Lease Rental Discounting (LRD); Realty–Commercial/Residential/Retail | Manufacturing/Trading/Corporate Services (master); Real Estate / LRD / CMBS | — |
| Chaman Lal Setia Exports Limited | — | — | Manufacturing Companies (master) |
| Chambal Fertilisers & Chemicals Limited | Corporate Credit Rating Methodology; Fertilizers | — | — |
| Chandan Healthcare Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Chavda Infra Limited | — | — | Infrastructure; Construction |
| Chemfab Alkalis Limited | — | — | Manufacturing Companies (master) |
| Chemplast Sanmar Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Chennai Petroleum Corporation Limited | Refining And Marketing | Manufacturing/Trading/Corporate Services (master) | — |
| Cholamandalam Investment and Finance Company Limited | Securitisation Transactions | — | NBFC |
| Cipla Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| City Union Bank Limited | ICRA’s Rating Methodology for Banks and Financial Institutions | — | Banks |
| Clean Science and Technology Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| CMS Info Systems Limited | Corporate Credit Rating Methodology | — | — |
| Coal India Limited | — | — | Manufacturing Companies (master) |
| Coastal Corporation Limited | — | — | Manufacturing Companies (master) |
| Cochin Shipyard Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Cohance Lifesciences Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Commercial Syn Bags Limited | Corporate Credit Rating Methodology | — | — |
| Concord Biotech Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Consolidated Construction Consortium Limited | Construction; Corporate Credit Rating Methodology | — | Construction |
| Container Corporation of India Ltd. | Corporate Credit Rating Methodology | — | — |
| Cool Caps Industries Limited | — | — | Manufacturing Companies (master) |
| Coromandel International Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Corona Remedies Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Cosmo First Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Country Club Hospitality and Holidays Limited (Formerly Country Club (India) Limited) | Hotels; Corporate Credit Rating Methodology | — | — |
| Craftsman Automation Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Creative Newtech Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| CreditAccess Grameen Limited | Rating Methodology for Securitisation Transactions | Finance & Securities Companies | — |
| Credo Brands Marketing Limited | — | — | Retail |
| Crest Ventures Limited | — | — | NBFC; Investment Holding Co |
| Current Infraprojects Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| CYIENT DLM LIMITED | Corporate Credit Rating Methodology | — | — |
| Cyient Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Dabur India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Dalmia Bharat Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Dalmia Bharat Sugar and Industries Limited | Corporate Credit Rating Methodology; Sugar | — | Manufacturing Companies (master); Sugar |
| Data Patterns (India) Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Datamatics Global Services Limited | Corporate Credit Rating Methodology; IT-Software & Services | — | — |
| Davangere Sugar Company Limited | — | — | Manufacturing Companies (master); Sugar |
| DC Infotech And Communication Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| DCB Bank Limited | ICRA’s Rating Methodology for Banks and Financial institutions | Banks & Financial Institutions; Finance & Securities Companies | Banks |
| DCM Nouvelle Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| DCM Shriram Industries Limited | — | — | Manufacturing Companies (master); Sugar |
| DCM Shriram Limited | Corporate Credit Rating Methodology; Chemicals; Sugar; Fertilizers | — | — |
| DCX Systems Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Deccan Cements Limited | — | — | Manufacturing Companies (master); Cement |
| Dee Development Engineers Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| Deep Industries Limited | — | — | Services Sector (master) |
| Deepak Builders & Engineers India Limited | — | Manufacturing/Trading/Corporate Services (master) | Construction |
| Deepak Fertilisers & Petrochemicals Corporation Limited | Corporate Credit Rating Methodology; Chemicals; Fertilizers | Manufacturing/Trading/Corporate Services (master) | — |
| Deepak Nitrite Limited | Corporate credit rating methodology; Chemical | — | — |
| Delphi World Money Limited | — | — | Services Sector (master) |
| Denta Water and Infra Solutions Limited | — | — | Construction |
| Dhampur Bio Organics Limited | — | — | Manufacturing Companies (master); Sugar |
| Dhampur Sugar Mills Limited | — | — | Manufacturing Companies (master); Sugar |
| Dhanlaxmi Bank Limited | ICRA’s Rating Methodology for Banks and Financial Institutions | — | — |
| Dhanuka Agritech Limited | — | — | Manufacturing Companies (master); Chemicals; Agrochemical |
| Dharmaj Crop Guard Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Chemicals; Agrochemical |
| Diffusion Engineers Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Digitide Solutions Limited | IT-Software & Services; Corporate Credit Rating Methodology | — | — |
| Dilip Buildcon Limited | — | Infrastructure sectors | — |
| Divi's Laboratories Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Divine Power Energy Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Dixon Technologies (India) Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| DLF Limited | Corporate Credit Rating Methodology; Realty - Commercial/Residential/Retail | Real Estate / LRD / CMBS | — |
| Dmcc Speciality Chemicals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Dodla Dairy Limited | Corporate Credit Rating Methodology | — | — |
| Dr. Agarwals Health Care Limited | Corporate Credit Rating Methodology; Hospitals | Manufacturing/Trading/Corporate Services (master) | — |
| Dr. Lal Pathlabs Limited | — | — | Services Sector (master) |
| Dr. Reddy's Laboratories Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Dredging Corporation of India Limited | — | — | Services Sector (master); Infrastructure |
| Dwarikesh Sugar Industries Limited | Corporate Credit Rating Methodology; Sugar | — | — |
| Dynacons Systems & Solutions Limited | — | — | Services Sector (master) |
| Dynamic Cables Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| E2E Networks Limited | Corporate Credit Rating Methodology | — | — |
| Edelweiss Financial Services Limited | — | — | NBFC; Investment Holding Co |
| Effwa Infra & Research Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Eicher Motors Limited | Corporate Credit Rating Methodology; Two-Wheelers | — | — |
| EIH Limited | — | — | Services Sector (master); Hotel |
| Elecon Engineering Company Limited | Corporate Credit Rating Methodology | — | — |
| Electrosteel Castings Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Elgi Equipments Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| ELGI Rubber Company Limited | — | — | Manufacturing Companies (master) |
| Elin Electronics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ellenbarrie Industrial Gases Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Emami Limited | — | — | Manufacturing Companies (master) |
| Emami Paper Mills Limited | — | — | Manufacturing Companies (master); Paper |
| Emcure Pharmaceuticals Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Pharmaceutical |
| Emkay Global Financial Services Limited | Stockbroking & Allied Services | — | — |
| Emmvee Photovoltaic Power Limited | Corporate Credit Rating Methodology | — | — |
| EMS Limited | Construction | Manufacturing/Trading/Corporate Services (master) | — |
| Emudhra Limited | Corporate Credit Rating Methodology; IT-Software & Services | — | — |
| Endurance Technologies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Engineers India Limited | — | — | Construction |
| Entertainment Network (India) Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Enviro Infra Engineers Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Epack Durable Limited | Corporate Credit Rating Methodology | — | — |
| Epack Prefab Technologies Limited | Corporate Credit Rating Methodology | — | — |
| EPIGRAL Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| EPL Limited | — | — | Manufacturing Companies (master) |
| Equitas Small Finance Bank Limited | — | — | Banks |
| ESAF Small Finance Bank Limited | — | — | Banks |
| Escorts Kubota Limited | Rating Methodology for Tractor Manufacturers | — | — |
| Essen Speciality Films Limited | — | — | Manufacturing Companies (master) |
| Ester Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ethos Limited | Retail | — | — |
| Eureka Forbes Limited | — | — | Manufacturing Companies (master) |
| Euro Panel Products Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Eveready Industries India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Everest Industries Limited | Corporate Credit Rating Methodology | — | — |
| Everest Kanto Cylinder Limited | — | — | Manufacturing Companies (master) |
| Excel Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Exicom Tele-Systems Limited | Corporate Credit Rating Methodology | — | Infrastructure |
| Exide Industries Limited | Corporate Credit Rating Methodology; Auto Components | — | — |
| Exim Routes Limited | — | — | Paper; Wholesale Trading |
| Exxaro Tiles Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Fabtech Technologies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Fairchem Organics Limited | — | — | Manufacturing Companies (master) |
| Faze Three Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| Fedbank Financial Services Limited | Rating methodology for non-banking finance companies | — | NBFC |
| Filatex India Limited | — | — | Manufacturing Companies (master) |
| Finkurve Financial Services Limited | — | Finance & Securities Companies | NBFC |
| FINO Payments Bank Limited | Non-Banking Finance Companies (NBFCs) | — | — |
| Firstsource Solutions Limited | — | Manufacturing/Trading/Corporate Services (master) | Services Sector (master) |
| Five-Star Business Finance Limited | Rating Methodology for Securitisation Transactions | — | NBFC |
| Foods and Inns Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Fortis Healthcare Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Freshara Agro Exports Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Fujiyama Power Systems Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Fusion Finance Limited | Rating Methodology for Securitisation Transactions | — | NBFC |
| G R Infraprojects Limited | — | — | Infrastructure; Construction |
| GAIL (India) Limited | Corporate Credit Rating Methodology | — | — |
| Gala Precision Engineering Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Galaxy Surfactants Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Gandhar Oil Refinery (india) Limited | — | — | Manufacturing Companies (master); Wholesale Trading |
| Ganesh Consumer Products Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Ganesh Green Bharat Limited | — | — | Manufacturing Companies (master) |
| Ganesh Infraworld Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ganesha Ecosphere Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Garden Reach Shipbuilders & Engineers Limited | — | — | Manufacturing Companies (master) |
| Garware Hi-Tech Films Limited | — | — | Manufacturing Companies (master) |
| Garware Technical Fibres Limited | Corporate Credit Rating Methodology | — | — |
| GE Vernova T&D India Limited (erstwhile ALSTOM T&D India Limited) | Corporate Credit Rating Methodology | — | — |
| General Insurance Corporation of India | — | — | Insurance |
| Genesys International Corporation Limited | — | — | Services Sector (master) |
| Genus Paper & Boards Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Paper |
| Genus Power Infrastructures Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Geojit Financial Services Limited | Stockbroking and allied services | Finance & Securities Companies | Services Sector (master); Broking |
| GHCL Limited | — | — | Manufacturing Companies (master) |
| GHCL Textiles Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| GIC Housing Finance Limited | — | Finance & Securities Companies | — |
| Gillanders Arbuthnot & Co Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| Ginni Filaments Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master); Textile/Cotton |
| GK ENERGY LIMITED | Corporate Credit Rating Methodology | — | Construction |
| Glenmark Pharmaceuticals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Global Health Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Global Vectra Helicorp Limited | — | — | Services Sector (master) |
| Globus Spirits Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Glottis Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| GMM Pfaudler Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| GMR Airports Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| GNA Axles Limited | Corporate Credit Rating Methodology; Auto Components | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| GNG Electronics Limited | — | — | Manufacturing Companies (master) |
| Go Fashion (India) Limited | Corporate Credit Rating Methodology; Textiles-Apparels | — | — |
| Godavari Biorefineries Limited | — | — | Manufacturing Companies (master); Sugar |
| Godawari Power and Ispat Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Godfrey Phillips India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Godrej Consumer Products Limited | Corporate Credit Rating Methodology; FMCG | — | — |
| Godrej Industries Limited | Corporate Credit Rating Methodology; Investment Companies | — | — |
| Godrej Properties Limited | Corporate Credit Rating Methodology; Realty-Commercial/Residential/Retail | — | — |
| Gokaldas Exports Limited | Corporate Credit Rating Methodology; Textiles-Apparels | Manufacturing/Trading/Corporate Services (master) | — |
| Gokul Agro Resources Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Goodluck India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Gopal Snacks Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Goyal Salt Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| GPT Healthcare Limited | — | Manufacturing/Trading/Corporate Services (master) | Hospital |
| GPT Infraprojects Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Infrastructure; Construction |
| Granules India Limited | Corporate Credit Rating Methodology; Rating Methodology–Pharmaceuticals | — | — |
| Graphite India Limited | Corporate Credit Rating Methodology | — | — |
| Grasim Industries Limited | Corporate Credit Rating Methodology; Chemicals | Manufacturing/Trading/Corporate Services (master); Holding Companies | Manufacturing Companies (master) |
| Gravita India Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Greenlam Industries Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Greenpanel Industries Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Greenply Industries Limited | — | — | Manufacturing Companies (master) |
| GRP Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Gufic Biosciences Limited | Corporate Credit Rating Methodology; Pharmaceuticals | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Pharmaceutical |
| Gujarat Alkalies and Chemicals Limited | — | — | Manufacturing Companies (master) |
| Gujarat Ambuja Exports Limited | — | — | Manufacturing Companies (master) |
| Gujarat Fluorochemicals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Gujarat Gas Limited | — | — | Infrastructure; City Gas |
| Gujarat Industries Power Company Limited | — | — | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Gujarat Mineral Development Corporation Limited | — | — | Manufacturing Companies (master) |
| Gujarat Pipavav Port Limited | — | Manufacturing/Trading/Corporate Services (master); Infrastructure sectors | — |
| Gujarat State Fertilizers and Chemicals Limited | — | — | Manufacturing Companies (master); Fertilizer |
| Gujarat State Petronet Limited | — | — | Infrastructure |
| Gujarat Themis Biosyn Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Gulf Oil Lubricants India Limited | Corporate Credit Rating Methodology | — | — |
| Gulshan Polyols Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| H.G. Infra Engineering Limited | Corporate Credit Rating Methodology; Construction | — | Infrastructure; Construction |
| Happiest Minds Technologies Limited | — | — | Services Sector (master) |
| Happy Forgings Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Hariom Pipe Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Iron & Steel |
| Harrisons Malayalam Limited | — | — | Manufacturing Companies (master) |
| Harsha Engineers International Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Hatsun Agro Product Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Havells India Limited | — | — | Manufacturing Companies (master) |
| HBL Engineering Limited | — | — | Manufacturing Companies (master) |
| HCL Infosystems Limited | — | — | Services Sector (master); NBFC; Investment Holding Co |
| HCL Technologies Limited | Corporate Credit Rating Methodology; IT-Software & Services | — | — |
| HDB FINANCIAL SERVICES LIMITED | Rating Methodology for Securitisation Transactions | Finance & Securities Companies | NBFC |
| HDFC Asset Management Company Limited | Mutual Funds | — | — |
| HDFC Bank Limited | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| HDFC Life Insurance Company Limited | Life Insurance | — | Insurance |
| HDFC_Bank_Limited_23Jun2026 | — | Banks & Financial Institutions | — |
| Healthcare Global Enterprises Limited | Hospitals; Corporate Credit Rating Methodology | — | Manufacturing Companies (master); Hospital |
| Heranba Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Heritage Foods Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Hero MotoCorp Limited | Corporate Credit Rating Methodology; Two-Wheelers | Manufacturing/Trading/Corporate Services (master) | — |
| Hester Biosciences Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| HFCL Limited | — | — | Manufacturing Companies (master); Infrastructure |
| Hi-Green Carbon Limited | — | — | Manufacturing Companies (master) |
| Hi-Tech Pipes Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Hikal Limited | Pharmaceuticals; Agrochemicals | — | — |
| Himadri Speciality Chemical Limited | Corporate Credit Rating Methodology; Chemicals | — | Manufacturing Companies (master) |
| Himatsingka Seide Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Textile/Cotton |
| Hind Rectifiers Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Hindalco Industries Limited | — | — | Manufacturing Companies (master) |
| Hinduja Global Solutions Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Hindustan Aeronautics Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Hindustan Construction Company Limited | Corporate Credit Rating Methodology; Construction | — | Infrastructure; Construction |
| Hindustan Copper Limited | Corporate Credit Rating Methodology; Mining; Non-Ferrous Metals (Primary Producers) | — | — |
| Hindustan Media Ventures Limited | Corporate Credit Rating Methodology; Print Media | — | — |
| Hindustan Petroleum Corporation Limited | Corporate Credit Rating Methodology; Refining and Marketing | Manufacturing/Trading/Corporate Services (master) | — |
| Hindustan Unilever Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Hindustan Zinc Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Hindware Home Innovation Limited | — | — | Manufacturing Companies (master) |
| HLE Glascoat Limited | Corporate Credit Rating Methodology | — | — |
| HMA Agro Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Home First Finance Company India Limited | Non-banking finance companies (NBFCs) | — | Housing Finance Companies |
| Housing and Urban Development Corporation Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies | — | NBFC |
| HP Adhesives Limited | — | — | Manufacturing Companies (master) |
| HP Telecom India Limited | — | — | Wholesale Trading |
| HPL Electric and Power Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| HT Media Limited | Corporate Credit Rating Methodology; Print Media | — | — |
| Huhtamaki India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ice Make Refrigeration Limited | — | — | Manufacturing Companies (master) |
| ICICI Bank Limited | Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| ICICI Lombard General Insurance Company Limited | Rating Methodology–General Insurance | — | — |
| ICICI Prudential Asset Management Company Limited | Mutual Funds | — | — |
| ICICI Prudential Life Insurance Company Limited | Life insurance | — | — |
| IDBI Bank Limited | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| IDFC First Bank Limited | Securitisation Transactions | Banks & Financial Institutions | — |
| IFCI Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies | — | NBFC |
| IFGL Refractories Limited | Corporate Credit Rating Methodology | — | — |
| Igarashi Motors India Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| IIFL Capital Services Limited | Stockbroking and allied services | Finance & Securities Companies | — |
| IIFL Finance Limited | Non-banking Finance Companies | Finance & Securities Companies | NBFC |
| IKIO Technologies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| IL&FS Engineering and Construction Company Limited | — | — | Infrastructure; Construction |
| Imagicaaworld Entertainment Limited | — | — | Services Sector (master) |
| Ind-Swift Laboratories Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| India Glycols Limited | — | — | Manufacturing Companies (master) |
| INDIA MOTOR PARTS & ACCESSORIES LIMITED | Corporate Credit Rating Methodology | — | — |
| India Pesticides Limited | — | — | Manufacturing Companies (master); Chemicals; Agrochemical |
| India Shelter Finance Corporation Limited | Securitisation Transactions | — | Housing Finance Companies |
| India Tourism Development Corporation Limited | — | — | Services Sector (master); Hotel |
| Indian Bank | — | Banks & Financial Institutions | Banks |
| Indian Metals & Ferro Alloys Limited | Corporate Credit Rating Methodology | — | — |
| Indian Oil Corporation Limited | Corporate Credit Rating Methodology; Refining and Marketing | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Indian Overseas Bank | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| Indian Railway Finance Corporation Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies | Finance & Securities Companies | NBFC |
| Indian Renewable Energy Development Agency Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies (NBFCs) | — | NBFC |
| Indigo Paints Limited | — | — | Manufacturing Companies (master) |
| Indiqube Spaces Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Indo Amines Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Indo Count Industries Limited | Corporate Credit Rating Methodology; Textiles-Fabric | — | Manufacturing Companies (master); Textile/Cotton |
| Indoco Remedies Limited | Corporate Credit Rating Methodology; Rating Methodology-Pharmaceuticals | — | — |
| Indogulf Cropsciences Limited | Corporate Credit Rating Methodology; Agrochemicals | — | Manufacturing Companies (master); Agrochemical |
| Indostar Capital Finance Limited | Rating methodology for securitisation transactions | Finance & Securities Companies | NBFC |
| Indraprastha Gas Limited | Rating methodology for City Gas Distribution Companies | — | Infrastructure; City Gas |
| Indraprastha Medical Corporation Limited | Corporate Credit Rating Methodology; Hospitals | — | — |
| Indus Towers Limited | Corporate Credit Rating Methodology; Telecom Towers | Infrastructure sectors | — |
| IndusInd Bank Limited | — | Banks & Financial Institutions | Banks |
| Infibeam Avenues Limited | Corporate Credit Rating Methodology | — | — |
| Infosys Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Innova Captab Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Inox Green Energy Services Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Inox India Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Inox Wind Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Insecticides (India) Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Inspirisys Solutions Limited | — | — | Services Sector (master) |
| Intellect Design Arena Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Interarch Building Solutions Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Interglobe Aviation Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| International Conveyors Limited | — | — | Manufacturing Companies (master) |
| Inventurus Knowledge Solutions Limited | — | — | Services Sector (master) |
| IOL Chemicals and Pharmaceuticals Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| IPCA Laboratories Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| IRB Infrastructure Developers Limited | — | Manufacturing/Trading/Corporate Services (master); Infrastructure sectors; Holding Companies | — |
| IRCON International Limited | — | — | Infrastructure; Construction |
| IRM Energy Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| ISGEC Heavy Engineering Limited | Corporate Credit Rating Methodology | — | — |
| ITC Limited | Corporate Credit Rating Methodology; FMCG | Manufacturing/Trading/Corporate Services (master) | — |
| ITI Limited | Corporate Credit Rating Methodology | — | — |
| iValue Infosolutions Limited | Corporate Credit Rating Methodology | — | — |
| J.G.Chemicals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Jagran Prakashan Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Jagsonpal Pharmaceuticals Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Jai Balaji Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Jain Irrigation Systems Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Jain Resource Recycling Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Jaiprakash Associates Limited | — | — | Construction |
| Jaiprakash Power Ventures Limited | — | Infrastructure sectors | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Jamna Auto Industries Limited | Corporate Credit Rating Methodology; Auto Components | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Jana Small Finance Bank Limited | Rating Methodology for Securitisation Transactions | — | — |
| Jash Engineering Limited | — | — | Manufacturing Companies (master) |
| Jay bee Laminations Limited | — | — | Manufacturing Companies (master) |
| Jay Bharat Maruti Limited | Corporate Credit Rating Methodology; Auto Components | — | — |
| Jayant Agro-Organics Limited | Corporate Credit Rating Methodology; Rating Methodology–Chemicals | — | — |
| JBM Auto Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Jindal Drilling and Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | Services Sector (master) |
| Jindal Poly Films Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Jindal Saw Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| Jindal Stainless Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| Jindal Steel Limited | Corporate Credit Rating Methodology; Iron & Steel | — | Manufacturing Companies (master); Iron & Steel |
| Jinkushal Industries Limited_undated | — | Manufacturing/Trading/Corporate Services (master) | — |
| JK Lakshmi Cement Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Cement |
| JK Paper Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| JK Tyre and Industries Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| JM Financial Limited | Rating Methodology for Stockbroking and Allied Services; Rating Methodology for Non-banking Finance Companies | — | Securitisation / ABS-MBS; Construction; Retail; Education; Wholesale Trading |
| JNK India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| JSW Cement Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Cement |
| JSW Energy Limited | Corporate Credit Rating Methodology; Power–Thermal; Power-Solar and Wind; Power Transmission | — | — |
| JSW Infrastructure Limited | Corporate Credit Rating Methodology; Ports | — | Services Sector (master); Infrastructure; Port |
| JSW Steel Limited | Corporate Credit Rating Methodology; Iron & Steel | — | Manufacturing Companies (master); Iron & Steel |
| JTEKT India Limited | Corporate Credit Rating Methodology; Auto Components | — | — |
| JTL Industries Limited | — | — | Manufacturing Companies (master) |
| Jubilant Agri and Consumer Products Limited | — | — | Manufacturing Companies (master); Chemicals; Fertilizer; Agrochemical |
| Jupiter Lifeline Hospitals Limited | — | — | Services Sector (master); Hospital |
| Jupiter Wagons Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| Jyothy Labs Limited | Corporate Credit Rating Methodology; FMCG | — | Manufacturing Companies (master) |
| K.P.R. Mill Limited | — | — | Manufacturing Companies (master); Sugar; Textile/Cotton |
| Kabra Extrusiontechnik Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Kajaria Ceramics Limited | Corporate Credit Rating Methodology | — | — |
| Kalpataru Limited | Corporate Credit Rating Methodology; Realty-Commercial/Residential/Retail | Real Estate / LRD / CMBS | — |
| Kalpataru Projects International Limited | — | Manufacturing/Trading/Corporate Services (master); Infrastructure sectors | Infrastructure; Construction |
| Kalyan Jewellers India Limited | Corporate Credit Rating Methodology; Jewellery-Retail | — | — |
| Kalyani Forge Limited_undated | — | Manufacturing/Trading/Corporate Services (master) | — |
| Kalyani Steels Limited | Corporate Credit Rating Methodology; Iron & Steel | — | Manufacturing Companies (master); Iron & Steel |
| Kamdhenu Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| Kanoria Chemicals & Industries Limited | — | — | Manufacturing Companies (master) |
| Kanpur Plastipack Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Kansai Nerolac Paints Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Kapston Services Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Kay Cee Energy & Infra Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Kaynes Technology India Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Kddl Limited | Corporate Credit Rating Methodology; Retail | — | — |
| KEC International Limited | Corporate Credit Rating Methodology; Construction | — | Infrastructure; Construction |
| KEI Industries Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Kellton Tech Solutions Limited | Corporate Credit Rating Methodology; IT–Software & Services | — | — |
| Kernex Microsystems (India) Limited | — | — | Manufacturing Companies (master) |
| Kewal Kiran Clothing Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Keystone Realtors Limited | Corporate Credit Rating Methodology; Realty-Commercial/Residential/Retail | — | — |
| Khadim India Limited | — | — | Retail |
| Khaitan Chemicals and Fertilizers Limited | — | — | Manufacturing Companies (master); Fertilizer |
| KIOCL Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Kirloskar Brothers Limited | — | — | Manufacturing Companies (master) |
| Kirloskar Electric Company Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Kitex Garments Limited | Textiles–Apparels | — | — |
| KNOWLEDGE MARINE & ENGINEERING WORKS LIMITED | — | — | Services Sector (master); Infrastructure |
| Kokuyo Camlin Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Kolte-Patil Developers Limited | Corporate Credit Rating Methodology; Rating Methodology for Real Estate Entities | Real Estate / LRD / CMBS | Real Estate |
| Kopran Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Kotak Mahindra Bank Limited | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | — |
| Kothari Petrochemicals Limited | Corporate Credit Rating Methodology; Chemicals | — | — |
| Kothari Sugars and Chemicals Limited | Rating Methodology for Entities in the Sugar Industry | Manufacturing/Trading/Corporate Services (master) | — |
| KPI Green Energy Limited | Power-Solar and Wind; Rating Methodology for Partially Guaranteed Debt | — | — |
| Krishana Phoschem Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Fertilizer |
| Krishna Defence and Allied Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Krishna Institute of Medical Sciences Limited | — | Manufacturing/Trading/Corporate Services (master) | Services Sector (master); Hospital |
| Kriti Industries (India) Limited | — | — | Manufacturing Companies (master) |
| Kriti Nutrients Limited | — | — | Manufacturing Companies (master) |
| KRN Heat Exchanger And Refrigeration Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Krsnaa Diagnostics Limited | Corporate Credit Rating Methodology; Diagnostic Service Providers | — | — |
| Krystal Integrated Services Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| KSB Limited | Corporate Credit Rating Methodology | — | — |
| KSH International Limited | — | — | Manufacturing Companies (master) |
| Kuantum Papers Limited | — | — | Manufacturing Companies (master); Paper |
| L&T Finance Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies | — | — |
| L&T Technology Services Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| La Opala R G Limited | — | — | Manufacturing Companies (master) |
| Larsen & Toubro Limited | Corporate Credit Rating Methodology; Construction; IT-Software & Services | Manufacturing/Trading/Corporate Services (master) | — |
| Laurus Labs Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Laxmi Goldorna House Limited | — | Manufacturing/Trading/Corporate Services (master); Real Estate / LRD / CMBS | — |
| Laxmi Organic Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Le Merite Exports Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Leela Palaces and Resorts Limited | — | — | Services Sector (master); Hotel |
| Leela Palaces Hotels & Resorts Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Lemon Tree Hotels Limited | Corporate Credit Rating Methodology; Hotels | Manufacturing/Trading/Corporate Services (master) | — |
| Liberty Shoes Limited | — | — | Manufacturing Companies (master) |
| LIC Housing Finance Limited | Rating methodology for non-banking finance companies | Finance & Securities Companies | Housing Finance Companies |
| Likhitha Infrastructure Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Lincoln Pharmaceuticals Limited | Corporate Credit Rating Methodology; Pharmaceuticals | Manufacturing/Trading/Corporate Services (master) | — |
| Lloyds Metals and Energy Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Lodha Developers Limited | Corporate Credit Rating Methodology; Realty-Commercial/Residential/Retail | Real Estate / LRD / CMBS | — |
| Lokesh Machines Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Lords Chloro Alkali Limited | Corporate Credit Rating Methodology; Chemicals | — | — |
| LT Foods Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Lumax Auto Technologies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Lumax Industries Limited | Corporate Credit Rating Methodology; Auto Components | — | — |
| Lupin Limited | Pharmaceuticals; Corporate Credit Rating Methodology | — | — |
| M and B Engineering Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| M K Proteins | — | — | Manufacturing Companies (master) |
| Maan Aluminium Limited | Corporate Credit Rating Methodology | — | — |
| Madhya Bharat Agro Products Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Fertilizer |
| Madras Fertilizers Limited | — | — | Manufacturing Companies (master); Fertilizer |
| Magadh Sugar & Energy Limited | Rating Methodology for Entities in the Sugar Industry | — | Manufacturing Companies (master); Sugar |
| Mahanagar Gas Limited | City Gas Distribution; Corporate Credit Rating Methodology | — | — |
| Mahanagar Telephone Nigam Limited | — | — | Infrastructure; Mobile/Telecom |
| Maharashtra Seamless Limited | Corporate Credit Rating Methodology | — | — |
| Mahindra & Mahindra Limited | Corporate Credit Rating Methodology; Rating Methodology for Passenger Cars; Rating Methodology for Commercial Vehicles; Rating Methodology for Tractors | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Mahindra and Mahindra Financial Services Limited | — | Finance & Securities Companies | NBFC |
| Mahindra Lifespace Developers Limited | — | Real Estate / LRD / CMBS | — |
| Mahindra Logistics Limited | Corporate Credit Rating Methodology | — | — |
| Maithan Alloys Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Iron & Steel |
| Mallcom (India) Limited | Corporate Credit Rating Methodology | — | — |
| Man Industries India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Man Infraconstruction Limited | — | — | Real Estate; Construction |
| Manaksia Coated Metals and Industries Limited | — | — | Manufacturing Companies (master) |
| Manaksia Steels Limited | Corporate Credit Rating Methodology; Iron & Steel | — | Manufacturing Companies (master); Iron & Steel |
| Manali Petrochemicals Limited | — | — | Manufacturing Companies (master) |
| Manappuram Finance Limited | — | Finance & Securities Companies | NBFC |
| Manba Finance Limited | — | — | NBFC |
| Mangal Credit And Fincorp Limited | — | Finance & Securities Companies | — |
| Mangal Electrical Industries Private Limited | — | — | Manufacturing Companies (master) |
| Mangalam Cement Limited | — | — | Manufacturing Companies (master); Cement |
| Mangalam Organics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Mangalore Refinery and Petrochemicals Limited | Corporate Credit Rating Methodology; Rating Methodology–Refining and Marketing | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Mankind Pharma Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | Manufacturing Companies (master); Pharmaceutical |
| Manoj Vaibhav Gems 'N' Jewellers Limited | Corporate Credit Rating Methodology; Jewellery–Retail | — | — |
| Manorama Industries Limited | — | — | Manufacturing Companies (master) |
| Marine Electricals (I) Limited | Corporate Credit Rating Methodology | — | — |
| Marksans Pharma Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Maruti Suzuki India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| MAS Financial Services Limited | Rating Methodology for Non-banking Finance Companies | — | NBFC |
| Mawana Sugars Limited | Corporate Credit Rating Methodology; Sugar | — | Manufacturing Companies (master); Sugar |
| Max Healthcare Institute Limited | — | — | Manufacturing Companies (master); Hospital |
| Maxvolt Energy Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Mayur Uniquoters Limited | — | — | Manufacturing Companies (master) |
| Mazda Limited | Corporate Credit Rating Methodology | — | — |
| Medi Assist Healthcare Services Limited | — | — | Services Sector (master) |
| Medicamen Biotech Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Medico Remedies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| MEGASTAR FOODS LIMITED | — | — | Manufacturing Companies (master) |
| Meghmani Organics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Menon Bearings Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Metro Brands Limited | — | — | Retail |
| Metropolis Healthcare Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Minda Corporation Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| MIRC Electronics Limited | — | — | Manufacturing Companies (master) |
| Mirza International Limited | Corporate Credit Rating Methodology; Footwear | Manufacturing/Trading/Corporate Services (master) | — |
| Mishra Dhatu Nigam Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| MMP Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Modison Limited | — | — | Manufacturing Companies (master) |
| MOLD-TEK Packaging Limited | Corporate Credit Rating Methodology | — | — |
| Moneyboxx Finance Limited | — | Finance & Securities Companies | — |
| Monte Carlo Fashions Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| Moschip Technologies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Motherson Sumi Wiring India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Motilal Oswal Financial Services Limited | Stockbroking & Allied Services; Non-banking Finance Companies (NBFCs) | — | — |
| Mphasis Limited | IT-Software & Services; Corporate Credit Rating Methodology | — | — |
| MRF Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Mrs.Bectors Food Specialities Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| MSP Steel & Power Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| MSTC Limited | — | — | Services Sector (master); Wholesale Trading |
| MTAR Technologies Limited | Corporate Credit Rating Methodology | — | — |
| Mukand Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Mukka Proteins Limited | — | — | Manufacturing Companies (master) |
| Munjal Auto Industries Limited | Corporate Credit Rating Methodology; Rating Methodology for Auto Components | — | — |
| Murudeshwar Ceramics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Music Broadcast Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Muthoot Capital Services Limited | Rating Methodology for Securitisation Transactions | Finance & Securities Companies | — |
| Muthoot Finance Limited | ICRA’s Rating Methodology for Non-banking Finance Companies | — | — |
| Muthoot Microfin Limited | Rating Methodology for Securitisation Transactions | Finance & Securities Companies | — |
| N R Agarwal Industries Limited | Corporate Credit Rating Methodology | — | — |
| NACL Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Agrochemical |
| Nahar Capital and Financial Services Ltd | Rating Methodology–Investment Companies | — | — |
| Nahar Poly Films Limited | — | — | Manufacturing Companies (master) |
| Nahar Spinning Mills Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Nandan Denim Limited | Corporate Credit Rating Methodology; Rating Methodology-Textiles Industry (Spinning); Rating Methodology-Textiles Industry (Fabric Making) | — | — |
| Narayana Hrudayalaya Limited | Corporate Credit Rating Methodology; Hospitals | — | — |
| Natco Pharma Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| National Fertilizers Limited | Corporate Credit Rating Methodology; Fertilisers | — | — |
| Nava Limited | — | Manufacturing/Trading/Corporate Services (master); Infrastructure sectors | — |
| Navin Fluorine International Limited | — | — | Manufacturing Companies (master) |
| Navkar Corporation Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Navneet Education Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| NBCC (India) Limited | — | Manufacturing/Trading/Corporate Services (master); Infrastructure sectors; Real Estate / LRD / CMBS | — |
| NCC Limited | — | — | Infrastructure; Construction |
| NCL Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Cement |
| NDR AUTO COMPONENTS LIMITED | Corporate Credit Rating Methodology; Auto Components | — | — |
| Nectar Lifesciences Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| NELCO Limited | — | Manufacturing/Trading/Corporate Services (master) | Infrastructure |
| Neogen Chemicals Limited | Corporate Credit Rating Methodology; Chemicals | Manufacturing/Trading/Corporate Services (master) | — |
| Nestle India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Netweb Technologies India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Network18 Media & Investments Limited | Corporate Credit Rating Methodology; TV Broadcasting | — | — |
| Neuland Laboratories Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Pharmaceutical |
| New Delhi Television Limited (NDTV) | — | — | Services Sector (master) |
| Newgen Software Technologies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| NGL Fine-Chem Limited | Corporate Credit Rating Methodology; Pharmaceuticals | Manufacturing/Trading/Corporate Services (master) | — |
| NHPC Limited | Power–Solar and Wind | — | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Nila Infrastructures Limited | — | — | Infrastructure; Real Estate; Construction |
| Nila Spaces Limited | — | — | Real Estate |
| Nilkamal Limited | — | — | Manufacturing Companies (master) |
| Nippon Life India Asset Management Limited | Mutual Funds | — | — |
| Nitin Spinners Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| Niva Bupa Health Insurance Company Limited | — | — | Insurance |
| NLC India Limited | — | Infrastructure sectors | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| NMDC Steel Limited | Rating Methodology for Iron & Steel | Manufacturing/Trading/Corporate Services (master) | — |
| NOCIL Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Northern ARC Capital Limited | — | — | NBFC |
| Nova Agritech Limited | — | — | Manufacturing Companies (master); Chemicals; Agrochemical |
| NRB Bearings Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| NTPC Green Energy Limited | — | Infrastructure sectors | — |
| NTPC Limited | Power–Thermal | Infrastructure sectors | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Nuvama Wealth Management Limited | — | Finance & Securities Companies | Services Sector (master); Broking |
| Nuvoco Vistas Corporation Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Oberoi Realty Limited | — | — | Real Estate; LRD |
| OBSC Perfection Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| OCCL Ltd | Corporate Credit Ratng Methodology; Chemicals | — | — |
| Oil and Natural Gas Corporation Limited | Oil Exploration & Production | — | Manufacturing Companies (master) |
| Oil India Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Om Infra Limited | — | — | Infrastructure; Construction |
| Omaxe Limited | — | — | Real Estate |
| OneSource Specialty Pharma Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Onward Technologies Limited | Rating Methodology-Information Technology (Services) | — | — |
| Optiemus Infracom Limited | Corporate Credit Rating Methodology | — | — |
| Orbit Exports Limited | Corporate Credit Rating Methodology; Textiles-Fabric | — | — |
| Orbit Resorts Limited | — | — | Services Sector (master) |
| Orchid Pharma Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Oriana Power Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Oricon Enterprises Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Orient Bell Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Orient Cement Limited | — | — | Manufacturing Companies (master); Cement |
| Orient Ceratech Limited | — | — | Manufacturing Companies (master) |
| Orient Electric Limited | — | — | Manufacturing Companies (master) |
| Orient Paper And Industries Limited | — | — | Manufacturing Companies (master); Paper |
| Oriental Hotels Limited | — | — | Services Sector (master); Hotel |
| OSEL Devices Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| OSWAL PUMPS LIMITED | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| P N Gadgil Jewellers Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Pace Digitek Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Page Industries Limited | Corporate Credit Rating Methodology; Textiles (Apparels) | — | — |
| Pakka Limited | — | — | Manufacturing Companies (master); Paper |
| Panama Petrochem Limited | Corporate Credit Rating Methodology; Chemicals | — | Manufacturing Companies (master) |
| Paradeep Phosphates Limited | Corporate Credit Rating Methodology; Fertilizers | — | — |
| Parag Milk Foods Limited | Corporate Credit Rating Methodology | — | — |
| Paramount Communications Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| Paras Defence & Space Technologies Limited | Corporate Credit Rating Methodology | — | — |
| Park Medi World Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Parth Electricals & Engineering Limited | — | — | Manufacturing Companies (master) |
| Pasupati Acrylon Limited | — | — | Manufacturing Companies (master) |
| Patanjali Foods Limited | Edible Oil; FMCG | — | — |
| Paushak Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| PCBL Chemical Limited | Corporate Credit Rating Methodology; Chemicals | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Pearl Global Industries Limited | Corporate Credit Rating Methodology; Textiles-Apparels | — | — |
| Peninsula Land Limited | — | — | LRD |
| Pennar Industries Limited | — | — | Manufacturing Companies (master) |
| Petronet LNG Limited | Corporate Credit Rating Methodology | — | — |
| PG Electroplast Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| PIL Italica Lifestyle Limited | — | — | Manufacturing Companies (master) |
| Pilani Investment and Industries Corporation Limited | — | — | Investment Holding Co |
| Piramal Finance Limited | Securitisation Transactions | Finance & Securities Companies | — |
| Piramal Pharma Limited | Pharmaceuticals | — | Manufacturing Companies (master); Pharmaceutical |
| Pitti Engineering Limited | — | — | Manufacturing Companies (master) |
| Pix Transmissions Limited | — | — | Manufacturing Companies (master) |
| Plastiblends India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| PNB Gilts Limited | Rating Methodology for Primary Dealers | Finance & Securities Companies | — |
| PNB Housing Finance Limited | Rating Methodology for Securitisation Transactions | Finance & Securities Companies | Housing Finance Companies |
| PNC Infratech Limited | — | — | Infrastructure; Construction |
| Poly Medicure Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Polycab India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Polyplex Corporation Limited | — | — | Manufacturing Companies (master) |
| Pondy Oxides and Chemicals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ponni Sugars (Erode) Limited | — | — | Manufacturing Companies (master); Sugar |
| Poonawalla Fincorp Limited | — | Finance & Securities Companies | NBFC |
| Popular Vehicles and Services Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Power Finance Corporation Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies | Finance & Securities Companies | NBFC |
| Power Grid Corporation of India Limited | Corporate Credit Rating Methodology; Power Transmission | Infrastructure sectors | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Power Mech Projects Limited | — | — | Infrastructure; Construction |
| PPAP Automotive Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Prakash Industries Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| Prataap Snacks Limited | Corporate Credit Rating Methodology; Fast Moving Consumer Goods Industry | — | — |
| Pratham EPC projects Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Precision Camshafts Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Precision Wires India Limited | — | — | Manufacturing Companies (master) |
| Precot Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| Premier Energies Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Premier Explosives Limited | Corporate Credit Rating Methodology; Chemicals | — | — |
| Premier Polyfilm Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| Prestige Estates Projects Limited | Corporate Credit Rating Methodology; Realty - Lease Rental Discounting (LRD); Realty - Commercial/Residential/Retail; RatingMethodologyfor hotels | — | — |
| Primo Chemicals Limited | — | — | Manufacturing Companies (master) |
| Prince Pipes and Fittings Limited | — | — | Manufacturing Companies (master) |
| Pritika Auto Industries Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Privi Speciality Chemicals Limited | Corporate Credit Rating Methodology; Chemicals | Manufacturing/Trading/Corporate Services (master) | — |
| Prostarm Info Systems Limited | — | — | Manufacturing Companies (master) |
| PSP Projects Limited | — | — | Infrastructure; Construction |
| PTC India Financial Services Limited | Rating methodology for non-banking finance companies | Finance & Securities Companies | NBFC |
| PTC India Limited | Corporate Credit Rating Methodology | — | — |
| PTC Industries Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master); Iron & Steel |
| Pudumjee Paper Products Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Punjab & Sind Bank | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| Punjab Chemicals and Crop Protection Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Chemicals; Agrochemical |
| Punjab National Bank | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| Puravankara Limited ( Previously Puravankara Projects Limited ) | Corporate Credit Rating Methodology; Realty-Commercial/Residential/Retail | — | — |
| Purple United Sales Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| PVR INOX Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Quess Corp Limited | Corporate Credit Rating Methodology | — | — |
| R Systems International Limited | Corporate Credit Rating Methodology; IT-Software & Services | Manufacturing/Trading/Corporate Services (master) | — |
| RACL Geartech Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Radico Khaitan Limited | — | — | Manufacturing Companies (master) |
| Raghav Productivity Enhancers Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Rail Vikas Nigam Limited | — | — | Infrastructure; Construction |
| Railtel Corporation of India Ltd. | Corporate Credit Rating Methodology; Construction | — | — |
| Rajoo Engineers Limited | — | — | Manufacturing Companies (master) |
| Rajratan Global Wire Limited | Corporate Credit Rating Methodology; Auto Components | Manufacturing/Trading/Corporate Services (master) | — |
| Ram Ratna Wires Limited | — | — | Manufacturing Companies (master) |
| Rama Phosphates Limited | Corporate Credit Rating Methodology; Fertilizers | — | Manufacturing Companies (master) |
| Rama Steel Tubes Limited | Corporate Credit rating Methodology; Iron & Steel | — | Manufacturing Companies (master); Wholesale Trading |
| Ramco Industries Limited | Corporate Credit Rating Methodology; Textiles-Spinning | — | — |
| Ramco Systems Limited | Corporate Credit Rating Methodology; IT- Software & Services | — | — |
| Ramkrishna Forgings Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ramky Infrastructure Limited | — | Manufacturing/Trading/Corporate Services (master) | Infrastructure; Construction |
| Rane (Madras) Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Rashi Peripherals Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Wholesale Trading |
| Rashtriya Chemicals and Fertilizers Limited | Fertilizers; Chemicals | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Fertilizer |
| Rationale-Aarvee_Engineering | Corporate Credit Rating Methodology | — | — |
| Rationale-ABT | Corporate Credit Rating Methodology; Automobile Dealers | — | — |
| Rationale-Amalgamated_Plantations | Corporate Credit Rating Methodology | — | — |
| Rationale-Anil | Corporate Credit Rating Methodology | — | — |
| Rationale-Arliga_Galleria_India | Corporate Credit Rating Methodology; Realty - Leasing | — | — |
| Rationale-ARPEGGIO_INDUSTRIES | Corporate Credit Rating Methodology | — | — |
| Rationale-Ascent_Hotels | Corporate Credit Rating Methodology; Hotels | — | — |
| Rationale-Atc_Foods | Rice Mills; Corporate Credit Rating Methodology | — | — |
| Rationale-B_E_Immuno_Sciences | Corporate Credit Rating Methodology; Realty-Leasing | — | — |
| Rationale-Bapuji | Corporate Credit Rating Methodology; Higher Education | — | — |
| Rationale-Beardsell | Corporate Credit Rating Methodology | — | — |
| Rationale-FP_Ampere_Energy | Corporate Credit Rating Methodology; Power-Solar and Wind | — | — |
| Rationale-FPEL_MAHA_2 | Corporate Credit Rating Methodology; Power-Solar and Wind | — | — |
| Rationale-FPEL_Stellar_Energy | Corporate Credit Rating Methodology; Power-Solar and Wind | — | — |
| Rationale-Garware_Hi-Tech | Corporate Credit Rating Methodology | — | — |
| Rationale-Global | Corporate Credit Rating Methodology | — | — |
| Rationale-Godrej | ICRA’s Credit Rating Methodology for Non-banking Finance Companies (NBFCs) | — | — |
| Rationale-Gokul | Corporate Credit Rating Methodology | — | — |
| Rationale-Haldia | Corporate Credit Rating Methodology; Chemicals | — | — |
| Rationale-Hanuman | Rice Mills; Corporate Credit Rating Methodology | — | — |
| Rationale-Indo_German | Chemicals; Corporate Credit Rating Methodology | — | — |
| Rationale-LT_Sargent_ | Corporate Credit Rating Methodology | — | — |
| Rationale-Mindstone_Mall_Developers | Corporate Credit Rating Methodology; Realty-Leasing | — | — |
| Rationale-Mirha_Exports | Corporate Credit Rating Methodology | — | — |
| Rationale-Neoanthem_Lifesciences | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Rationale-North_Eastern_Development_Finance | Non-banking Finance Companies (NBFCs) | — | — |
| Rationale-PABSCON.md | Corporate Credit Rating Methodology; Construction | — | — |
| Rationale-Rinac | Corporate Credit Ratng Methodology | — | — |
| Rationale-Rugby_Renergy | Corporate Credit Rating Methodology; Power-Solar and Wind | — | — |
| Rationale-SRS | Corporate Credit Rating Methodology; Jewellery-Retail | — | — |
| Rationale-Steamhouse | Corporate Credit Rating Methodology | — | — |
| Rationale-Synthetic_Packers | Corporate Credit Rating Methodology | — | — |
| Rationale-V.S._Jewellery_Wholesaler_Global | Corporate Credit Rating Methodology | — | — |
| Rationale-VSV_offsite | Corporate Credit Rating Methodology; Power-Solar and Wind | — | — |
| Rattanindia Power Limited | — | Infrastructure sectors | — |
| Raymond Lifestyle Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Textile/Cotton |
| Raymond Limited | — | Real Estate / LRD / CMBS | — |
| Raymond Realty Limited | — | — | Real Estate |
| RBL Bank Limited | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| RBZ Jewellers Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Retail |
| REC Limited | — | Finance & Securities Companies | NBFC |
| Redington Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| REDTAPE LIMITED | — | Manufacturing/Trading/Corporate Services (master) | — |
| Regaal Resources Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Relaxo Footwears Limited | Corporate Credit Rating Methodology; Footwear | — | — |
| Reliance Communications Limited | — | — | Infrastructure; Mobile/Telecom |
| Reliance Industries Limited | Oil Exploration & Production; Telecom Services; Retail; Corporate Credit rating Methodology | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Reliance Power Limited | Corporate Credit Rating Methodology; Rating methodology for Power–Thermal; Rating methodology for Power–Solar and Wind | — | — |
| Remsons Industries Limited | Corporate Credit Rating Methodology; Rating Methodology for auto Components | Manufacturing/Trading/Corporate Services (master) | — |
| Renaissance Global Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Repco Home Finance Limited | Securitisation Transactions | — | Housing Finance Companies |
| Repro India Limited | Corporate Credit Rating Methodology | — | — |
| Restaurant Brands Asia Limited | Corporate Credit Rating Methodology | — | — |
| Revathi Equipment India Limited | — | — | Manufacturing Companies (master) |
| Rico Auto Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Rishabh Instruments Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Ritco Logistics Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | Services Sector (master) |
| RITES Limited | — | — | Infrastructure; Construction |
| RNFI Services Limited | — | — | Services Sector (master) |
| Robust Hotels Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Rolex Rings Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Rossari Biotech Limited | Corporate Credit Rating Methodology; Chemicals | — | — |
| Roto Pumps Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Royal Orchid Hotels Limited | Hotels; Corporate Credit Rating Methodology | — | — |
| RPG Life Sciences Limited | Corporate Credit Rating Methodology; Pharmaceutical | — | — |
| RPSG Ventures Limited | — | — | Services Sector (master); Investment Holding Co |
| Ruchira Papers Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master); Paper |
| Rupa & Company Limited_undated | — | Manufacturing/Trading/Corporate Services (master) | — |
| S Chand and Company Limited | Corporate Credit Rating Methodology | — | — |
| S H Kelkar And Company Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Saatvik Green Energy Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sagility Limited | IT-Software & Services | Manufacturing/Trading/Corporate Services (master) | — |
| Sahyadri Industries Limited | Corporate Credit Rating Methodology | — | — |
| Sai Life Sciences Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | Manufacturing Companies (master); Pharmaceutical |
| Sai Silks (kalamandir) Limited | — | — | Retail |
| Sakar Healthcare Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Saksoft Limited | — | — | Services Sector (master) |
| Sakuma Exports Limited | Corporate Credit Rating Methodology | — | — |
| Salzer Electronics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sambhv Steel Tubes Limited | — | — | Manufacturing Companies (master) |
| SAMHI Hotels Limited. | Corporate Credit Rating Methodology; Hotels | — | Services Sector (master); Hotel |
| Sammaan Capital Limited | Rating Methodology for Non-banking Finance Companies | Finance & Securities Companies | NBFC |
| Sanathan Textiles Limited | Corporate Credit Rating Methodology; Textiles-Spinning | — | Manufacturing Companies (master); Textile/Cotton |
| Sandhar Technologies Limited | Corporate Credit Rating Methodology; Auto Components | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Sanghvi Movers Limited | Corporate Credit Rating Methodology; Construction | — | — |
| Sansera Engineering Limited | Corporate Credit Rating Methodology; Auto Components | — | — |
| Sanstar Limited | — | — | Manufacturing Companies (master) |
| Sapphire Foods India Limited | Corporate Credit Rating Methodology | — | — |
| Sarda Energy & Minerals Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Saregama India Limited | Corporate Credit Rating Methodology | — | Services Sector (master) |
| Sasken Technologies Limited | Corporate Credit Rating Methodology; IT-Software & Services | — | — |
| Sathlokhar Synergys E&C Global Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Satin Creditcare Network Limited | Securitisation Transactions | — | NBFC |
| Saurashtra cement limited | Corporate Credit Rating Methodology; Rating Methodology-Cement | — | — |
| Savita Oil Technologies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Savy Infra And Logistics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| SBFC Finance Limited | Non-Banking Finance Companies (NBFCs) | — | NBFC |
| SBI Cards and Payment Services Limited | ICRA’s credit rating methodology for non-banking finance companies | Finance & Securities Companies | — |
| Scoda Tubes Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Iron & Steel |
| Seamec Limited | — | Manufacturing/Trading/Corporate Services (master) | Shipping |
| Senco Gold Limited | Corporate Credit Rating Methodology; Jewellery-Retail | — | Retail |
| SEPC Limited | — | Manufacturing/Trading/Corporate Services (master) | Construction |
| Seshaasai Technologies Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Seshasayee Paper & Boards Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master); Paper |
| SG Finserve Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies (NBFCs); ICRA’s Policy on Provisional Ratings | Finance & Securities Companies | — |
| Shaily Engineering Plastics Limited | — | — | Manufacturing Companies (master) |
| Shakti Pumps (India) Limited | — | — | Manufacturing Companies (master) |
| Shalby Limited | Corporate Credit Rating Methodology; Hospitals | — | — |
| Shalimar Paints Limited | — | — | Manufacturing Companies (master) |
| Shankara Building Products Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Shanthi Gears Limited | Corporate Credit Rating Methodology | — | — |
| Shanti Gold International Limited | — | — | Manufacturing Companies (master) |
| Sharda Cropchem Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sharda Motor Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Share India Securities Limited | Rating Methodology for Entities in the Broking Industry | Finance & Securities Companies | Broking |
| Sheela Foam Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sheetal Cool Products Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Shemaroo Entertainment Limited | — | — | Services Sector (master) |
| Shera Energy Limited | — | — | Manufacturing Companies (master) |
| Shilchar Technologies Limited | — | — | Manufacturing Companies (master) |
| Shivalik Bimetal Controls Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Shivam Autotech Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Shoppers Stop Limited | — | Manufacturing/Trading/Corporate Services (master) | Retail |
| Shree Cement Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Cement |
| Shree Digvijay Cement Co. Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Shree Pushkar Chemicals & Fertilisers Limited | Fertilizers; Corporate Credit Rating Methodology; Chemicals | — | — |
| Shree Rama Newsprint Limited | — | — | Manufacturing Companies (master) |
| Shree Renuka Sugars Limited | Rating Methodology for Entities in the Sugar Industry | — | — |
| Shree Vasu Logistics Limited | — | — | Services Sector (master) |
| Shreeji Shipping Global Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Shreyans Industries Limited | — | — | Manufacturing Companies (master); Paper |
| Shri Ahimsa Naturals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Shriram Finance Limited | — | Finance & Securities Companies | NBFC |
| Shriram Properties Limited | — | Real Estate / LRD / CMBS | Real Estate |
| Shyam Metalics and Energy Limited | — | — | Manufacturing Companies (master) |
| Sical Logistics Limited | Corporate Credit Rating Methodology | — | — |
| Siemens Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sigachi Industries Limited | — | — | Manufacturing Companies (master) |
| Signatureglobal (India) Limited | Rating Methodology for Real Estate Entities | — | — |
| Signpost India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Silver Touch Technologies Limited | — | — | Services Sector (master) |
| Simplex Infrastructures Limited | — | — | Construction |
| Sintercom India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| SIS Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Siyaram Silk Mills Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| SJVN Limited | — | — | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Skipper Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| SKM Egg Products Export India Limited | — | — | Manufacturing Companies (master) |
| Sky Gold and Diamonds Limited | — | — | Manufacturing Companies (master) |
| Smartworks Coworking Spaces Limited | — | Real Estate / LRD / CMBS | LRD |
| SMC Global Securities Limited | Non-banking Finance Companies (NBFCs) | Finance & Securities Companies | — |
| SML Mahindra Limited | Corporate Credit Rating Methodology; Commercial Vehicles | — | — |
| SMS Pharmaceuticals Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Sobha Limited | Corporate Credit Rating Methodology; Realty-Commercial/Residential/Retail | — | — |
| Softtech Engineers Limited | — | — | Services Sector (master) |
| Solar Industries India Limited | Corporate Credit Rating Methodology; Chemicals | Manufacturing/Trading/Corporate Services (master) | — |
| Solarworld Energy Solutions Limited | — | — | Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Solex Energy Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Som Distilleries & Breweries Limited | Corporate Credit Rating Methodology | — | — |
| Somany Ceramics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| South West Pinnacle Exploration Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Spandana Sphoorty Financial Limited | Rating Methodology for Securitisation Transactions | — | NBFC |
| Speciality Restaurants Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Spectrum Electrical Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Spencer's Retail Limited | — | — | Services Sector (master); Retail |
| SPML Infra Limited | Corporate credit rating methodology; Construction | — | — |
| Sportking India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| SPUNWEB NONWOVEN LIMITED | Corporate Credit Rating Methodology | — | — |
| SRF Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| SRG Housing Finance Limited | — | — | Housing Finance Companies |
| SRM Contractors Limited | — | — | Construction |
| Stanley Lifestyles Limited | Corporate Credit Rating Methodology | — | — |
| Star Cement Limited | Rating Methodology-Cement | Manufacturing/Trading/Corporate Services (master) | — |
| Star Health and Allied Insurance Company Limited | — | — | Insurance |
| State Bank of India | ICRA’s Rating Methodology for Banks and Financial Institutions | Banks & Financial Institutions | Banks |
| Steel Authority of India Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| Steel Exchange India Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| Sterling Tools Limited | Corporate Credit Rating Methodology; Auto Components | — | — |
| Sterlite Technologies Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| Stove Kraft Limited | Corporate Credit Rating Methodology | — | — |
| Strides Pharma Science Limited | Corporate Credit Rating Methodology; Rating Methodology for Pharmaceutical Industry | — | Manufacturing Companies (master); Pharmaceutical |
| Studds Accessories Limited | — | — | Manufacturing Companies (master) |
| Stylam Industries Limited | — | — | Manufacturing Companies (master) |
| Styrenix Performance Materials Limited | — | — | Manufacturing Companies (master) |
| Subros Limited | Corporate Credit Rating Methodology; Auto components | — | — |
| Sudarshan Pharma Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sula Vineyards Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| Sumeet Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sumitomo Chemical India Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sun Pharmaceutical Industries Limited | Corporate Credit Rating Methodology; Pharmaceuticals | Manufacturing/Trading/Corporate Services (master) | — |
| Sun TV Network Limited | TV Broadcasting | — | — |
| Sundaram Brake Linings Limited | Corporate Credit Rating Methodology; Auto Components | — | — |
| Sundaram Finance Limited | Securitisation Transactions | Finance & Securities Companies | — |
| Sundaram Home Finance Limited | — | — | Housing Finance Companies |
| Sundaram-Clayton Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sundrop Brands Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Sunflag Iron and Steel Company Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Iron & Steel |
| Sunteck Realty Limited | Rating Methodology for Real Estate Entities | — | Real Estate |
| Suprajit Engineering Limited | Corporate Credit Rating Methodology; Auto Components | Manufacturing/Trading/Corporate Services (master) | — |
| Supreme Petrochem Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Supreme Power Equipment Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| Supriya Lifescience Ltd. | Pharmaceuticals | — | — |
| Suraksha Diagnostic Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Surana Telecom & Power Limited | — | — | Power (Solar/Wind/Thermal/Transmission/Distribution) |
| Surya Roshni Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Suryoday Small Finance Bank Limited | ICRA’s Rating Methodology for Banks and Financial Institutions | — | — |
| Sutlej Textiles and Industries Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| Suven Life Sciences Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Suyog Telematics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Suzlon Energy Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| Swaraj Suiting Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Swelect Energy Systems Limited | Corporate Credit Rating Methodology; Rating Methodology for Solar Power Producers | Manufacturing/Trading/Corporate Services (master); Infrastructure sectors | — |
| Synergy Green Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Syngene International Limited | Corporate Credit Rating Methodology; Pharmaceuticals | Manufacturing/Trading/Corporate Services (master) | — |
| Syrma SGS Technology Limited | — | — | Manufacturing Companies (master) |
| Take Solutions Limited | — | — | Services Sector (master) |
| Talbros Automotive Components Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Tamil Nadu Newsprint & Papers Limited | Corporate Credit Rating Methodology | — | — |
| Tamilnad Mercantile Bank Limited | — | Banks & Financial Institutions | — |
| Tamilnadu Petroproducts Limited | — | — | Manufacturing Companies (master) |
| Tanla Platforms Limited | — | — | Services Sector (master) |
| Tara Chand Infralogistic Solutions Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | Services Sector (master) |
| Tarsons Products Limited | — | — | Manufacturing Companies (master) |
| Tasty Bite Eatables Limited | Corporate Credit Rating Methodology; Rating Methodology for the Entities in the Fast-Moving Consumer Goods (FMCG) Industry; Impact of Parent or Group Support on an Issuer’s Credit Rating | — | — |
| Tata Capital Limited | ICRA’s Credit Rating Methodology for Non-banking Finance Companies | Finance & Securities Companies | NBFC |
| Tata Chemicals Limited | — | — | Manufacturing Companies (master) |
| Tata Communications Limited | — | — | Services Sector (master); Infrastructure |
| Tata Consultancy Services Limited | Corporate Credit Rating Methodology; IT–Software & Services | — | — |
| Tata Consumer Products Limited | Corporate Credit Rating Methodology; FMCG | — | Manufacturing Companies (master) |
| Tata Motors Limited (Erstwhile TML Commercial Vehicles Limited) | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership) |
| Tata Motors Passenger Vehicles Limited | Corporate Credit Rating Methodology; Passenger Cars | Manufacturing/Trading/Corporate Services (master) | — |
| Tata Steel Limited | Corporate Credit Rating Methodology; Iron & Steel | — | Manufacturing Companies (master); Iron & Steel |
| Tata Technologies Limited | — | — | Services Sector (master) |
| Tata Teleservices (Maharashtra) Limited | — | Manufacturing/Trading/Corporate Services (master) | Services Sector (master); Infrastructure |
| Tatva Chintan Pharma Chem Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| TBO Tek Limited | — | — | Services Sector (master) |
| TCI Express Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| TCPL Packaging Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| TD Power Systems Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| TeamLease Services Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| Tech Mahindra Limited | — | — | Services Sector (master) |
| Techno Electric & Engineering Company Limited | Corporate Credit Rating Methodology | — | — |
| Tega Industries Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| TEJAS CARGO INDIA LIMITED | Corporate Credit Rating Methodology | — | — |
| Tejas Networks Limited | Corporate Credit Rating Methodology | — | — |
| Tembo Global Industries Limited | — | — | Manufacturing Companies (master); Power (Solar/Wind/Thermal/Transmission/Distribution); Iron & Steel; Construction; Wholesale Trading |
| Texmaco Infrastructure & Holdings Limited | — | — | LRD; Investment Holding Co |
| Texmaco Rail & Engineering Limited | — | — | Manufacturing Companies (master); Construction |
| Thaai Casting Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Thangamayil Jewellery Limited | Corporate Credit Rating Methodology; Jewellery-Retail | — | — |
| The Anup Engineering Limited | — | — | Manufacturing Companies (master) |
| The Byke Hospitality Limited | — | — | Services Sector (master); Hotel |
| The Federal Bank Limited | — | Banks & Financial Institutions | — |
| The Great Eastern Shipping Company Limited | — | — | Infrastructure; Shipping |
| The Hi-Tech Gears Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| The India Cements Limited | — | — | Manufacturing Companies (master); Cement |
| The Indian Hotels Company Limited | Corporate Credit Rating Methodology; Hotels | — | Services Sector (master); Hotel |
| The Jammu and Kashmir Bank Limited | — | Banks & Financial Institutions | — |
| The Phoenix Mills Limited | — | Real Estate / LRD / CMBS | — |
| The Ramco Cements Limited | Cement; Corporate Credit Rating Methodology | — | — |
| The Ruby Mills Limited | — | — | Manufacturing Companies (master); Real Estate; Textile/Cotton |
| The South Indian Bank Limited | — | — | Banks |
| The Ugar Sugar Works Limited | — | — | Manufacturing Companies (master); Sugar |
| Thejo Engineering Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Themis Medicare Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Thirumalai Chemicals Limited | Corporate Credit Rating Methodology; Chemicals | — | — |
| TIL Limited | — | — | Manufacturing Companies (master) |
| Tilaknagar Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Time Technoplast Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Tinna Rubber & Infrastructure Limited | Corporate Credit Rating Methodology | — | Manufacturing Companies (master) |
| Titan Company Limited | Corporate Credit Rating Methodology; Jewellery-Retail | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Retail |
| Torrent Pharmaceuticals Limited | Pharmaceuticals | — | — |
| Torrent Power Limited | — | Manufacturing/Trading/Corporate Services (master); Infrastructure sectors | — |
| Tourism Finance Corporation of India Limited | — | — | NBFC |
| Transformers And Rectifiers (india) Limited | — | — | Manufacturing Companies (master) |
| Transindia Real Estate Limited | — | — | LRD |
| Transport Corporation of India Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | Services Sector (master) |
| Transrail Lighting Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Trent Limited | Corporate Credit Rating Methodology; Retail | — | Retail |
| TRF Limited | — | — | Manufacturing Companies (master) |
| Trident Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| Trident Techlabs Limited | — | — | Services Sector (master) |
| Triveni Engineering & Industries Ltd. | Corporate Credit Rating Methodology; Sugar | — | — |
| Triveni Turbine Limited | Corporate Credit Rating Methodology | — | — |
| TruAlt Bioenergy Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| TTK Healthcare Limited | Corporate Credit Rating Methodology; FMCG | — | — |
| TTK Prestige Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Tube Investments of India Limited | Corporate Credit Rating Methodology; Auto Component | — | — |
| TV Today Network Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| TVS Holdings Limited | — | — | Investment Holding Co |
| TVS Motor Company Limited | — | — | Manufacturing Companies (master) |
| UCO Bank | — | — | Banks |
| Uflex Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| UFO Moviez India Limited | Corporate Credit Rating Methodology | — | — |
| Ugro Capital Limited | — | Finance & Securities Companies | — |
| UJJIVAN SMALL FINANCE BANK LIMITED | Banks and Financial Institutions | — | Banks |
| Ultratech Cement Limited | — | — | Manufacturing Companies (master); Cement |
| Unichem Laboratories Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Unihealth Hospitals Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Union Bank of India | ICRA’s Rating Methodology for Banks and Financial Institutions | — | Banks |
| Uniparts India Limited | Corporate Credit Rating Methodology; Auto components | — | — |
| United Breweries Limited | Corporate Credit Rating Methodology | — | — |
| UNITED FOODBRANDS LIMITED (Erstwhile Barbeque Nation Hospitality Limited) | Corporate Credit Rating Methodology | — | — |
| Univastu India Limited | — | Infrastructure sectors | — |
| Universal Cables Limited | — | — | Manufacturing Companies (master) |
| Updater Services Limited | Corporate Credit Rating Methodology | — | — |
| UPL Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Chemicals; Agrochemical |
| Urja Global Limited | — | — | Manufacturing Companies (master); Auto (Components/CV/Dealership); Wholesale Trading |
| Usha Martin Limited | — | — | Manufacturing Companies (master) |
| UTI Asset Management Company Limited | Mutual funds | — | Securitisation / ABS-MBS |
| Utkarsh Small Finance Bank Limited | ICRA’s credit rating methodology for banks and financial institutions | — | Banks |
| Utssav CZ Gold Jewels Limited | — | — | Manufacturing Companies (master) |
| Uttam Sugar Mills Limited | — | — | Manufacturing Companies (master); Sugar |
| V-Guard Industries Limited | Corporate Credit Rating Methodology | — | — |
| V-Mart Retail Limited | Corporate Credit Rating Methodology; Retail | — | — |
| V.S.T. Tillers Tractors Limited | Corporate Credit Rating Methodology; Rating Methodology for Tractors | — | — |
| V2 Retail Limited | Corporate Credit Rating Methodology; Retail | — | — |
| Vadilal Industries Limited | — | — | Manufacturing Companies (master) |
| Vaibhav Global Limited | Corporate Credit Rating Methodology; Retail | — | Manufacturing Companies (master); Retail; Diamond |
| Valiant Organics Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Vardhman Textiles Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Varroc Engineering Limited | Rating Methodology for Auto Component Manufacturers | — | — |
| Varun Beverages Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Vasa Denticity Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Vascon Engineers Limited | — | Manufacturing/Trading/Corporate Services (master); Real Estate / LRD / CMBS | — |
| Vedant Fashions Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Vedanta Limited | Corporate Credit Rating Methodology; Non-Ferrous Metals (Primary Producers) | Manufacturing/Trading/Corporate Services (master); Infrastructure sectors | — |
| Veedol Corporation Limited | — | — | Manufacturing Companies (master) |
| Venky`s (india) Limited | — | — | Manufacturing Companies (master) |
| Ventive Hospitality Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Venus Pipes and Tubes Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Vibhor Steel Tubes Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Iron & Steel |
| Viceroy Hotels Limited | — | Manufacturing/Trading/Corporate Services (master) | Services Sector (master); Hotel |
| Vidhi Specialty Food Ingredients Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Vidya Wires Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Vijaya Diagnostic Centre Limited | Rating Methodology–Diagnostic Service Providers | — | — |
| Vikas EcoTech Limited | — | — | Manufacturing Companies (master); Wholesale Trading |
| Vikran Engineering Limited | — | — | Infrastructure; Construction |
| Vilas Transcore Limited | Corporate Credit Rating Methodology | — | — |
| Vimta Labs Limited | — | — | Services Sector (master); Pharmaceutical |
| Vinati Organics Limited | — | — | Manufacturing Companies (master) |
| Vindhya Telelinks Limited | — | — | Infrastructure; Construction |
| Vinyas Innovative Technologies Limited | Corporate Credit Rating Methodology | Manufacturing/Trading/Corporate Services (master) | — |
| VIP Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Visaka Industries Limited | — | — | Manufacturing Companies (master) |
| Vishnu Chemicals Limited | — | — | Manufacturing Companies (master) |
| Vishnu Prakash R Punglia Limited | — | — | Infrastructure; Construction |
| VIVIANA POWER TECH LIMITED | — | — | Services Sector (master); Construction |
| Vodafone Idea Limited | Corporate Credit Rating Methodology; Telecom Services | Manufacturing/Trading/Corporate Services (master) | Infrastructure; Mobile/Telecom |
| Voltamp Transformers Limited | — | — | Manufacturing Companies (master) |
| Voltas Limited | Corporate Credit Rating Methodology | — | — |
| VRAJ Iron And Steel Limited | — | — | Manufacturing Companies (master); Iron & Steel |
| VRL Logistics Limited | Corporate Credit Rating Methodology | — | — |
| VST Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Waaree Energies Limited | — | — | Manufacturing Companies (master) |
| Waaree Renewable Technologies Limited | — | — | Manufacturing Companies (master) |
| Walchandnagar Industries Limited | — | — | Manufacturing Companies (master); Power (Solar/Wind/Thermal/Transmission/Distribution); Cement; Sugar |
| Websol Energy System Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
| Welspun Corp Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| Welspun Enterprises Ltd | Corporate Credit Rating Methodology; Construction | — | — |
| Welspun Living Limited | — | — | Manufacturing Companies (master); Textile/Cotton |
| Wendt (India) Limited | Corporate Credit Rating Methodology | — | — |
| West Coast Paper Mills Ltd. | Corporate Credit Rating Methodology | — | — |
| Western Carriers (India) Limited | — | Manufacturing/Trading/Corporate Services (master) | Services Sector (master) |
| WeWork India Management Limited | Corporate Credit Rating Methodology; Realty-Lease Rental Discounting (LRD) | Real Estate / LRD / CMBS | — |
| Wheels India Limited | Corporate Credit Rating Methodology; Auto Components | — | — |
| Windlas Biotech Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | — |
| Wipro Limited | Corporate Credit Rating Methodology; IT-Software & Services | — | — |
| Wockhardt Limited | Corporate Credit Rating Methodology; Pharmaceuticals | — | Manufacturing Companies (master); Pharmaceutical |
| Wonderla Holidays Limited | Corporate Credit Rating Methodology | — | Services Sector (master) |
| Yasho Industries Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master) |
| YES Bank Limited | — | Banks & Financial Institutions | Banks |
| Yuken India Limited | — | — | Manufacturing Companies (master) |
| Zaggle Prepaid Ocean Services Limited | — | — | Services Sector (master) |
| ZEE Entertainment Enterprises Limited | — | — | Services Sector (master) |
| Zee Media Corporation Limited | — | — | Services Sector (master) |
| Zensar Technologies Limited | Corporate Credit Rating Methodology; IT–Software & Services | — | — |
| Zim Laboratories Limited | — | — | Manufacturing Companies (master); Pharmaceutical |
| Zodiac Clothing Company Limited | — | Manufacturing/Trading/Corporate Services (master) | Manufacturing Companies (master); Retail; Textile/Cotton |
| Zodiac Energy Limited | — | — | Infrastructure; Power (Solar/Wind/Thermal/Transmission/Distribution); Construction |
| Zuari Agro Chemicals Limited | Rating Approach for Fertilisers Sector | — | — |
| Zuari Industries Limited | — | — | Manufacturing Companies (master); Sugar; Investment Holding Co |
| Zydus Lifesciences Limited | — | Manufacturing/Trading/Corporate Services (master) | — |
