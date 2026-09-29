# CRISIL — reference data

Drop CRISIL source material here. Same three-part layout as ICRA (which lives at the project root).

| Folder | What to put here |
|---|---|
| `Methodology/` | CRISIL rating criteria / methodology documents (Corporate, sector criteria, Financial Ratio analysis, etc.), as `.md` or `.pdf`. |
| `Report for Reference/` | Published CRISIL **Rating Rationales** (one company per file). These teach CRISIL's format, section order, house style and calibration — they are a CRAFT source, never a source of facts for a new report. |
| `Knowledge Base/` | CRISIL-specific distilled files (methodology index, sector→criteria routing map, report template with CRISIL's section order, rationale-construction library) — to be built the same way the ICRA Knowledge Base was, once enough Methodology + Report files are present. |

**Rating scale:** long-term `CRISIL AAA … CRISIL D` (with `+`/`-` modifiers AA to C); short-term `CRISIL A1+ … CRISIL A4, CRISIL D`. Symbols follow the SEBI-standardised structure (same letters as ICRA/CARE, different prefix).

**Naming convention (recommended):** `<Company>_<DD Mon YYYY>_<code>.md` for rationales, matching the ICRA `Report for Reference` convention so the tooling and routing map work identically.

Do NOT mix CRISIL and ICRA files in the same folder — the agency is inferred from which folder a file sits in.
