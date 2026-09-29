"""Positive controls for the prior-rating absence-contradiction probe (failure modes 20/24/29).

The control that matters is the THIRD one: a corrected report necessarily quotes its own former
false claim while correcting it, and a probe that fires on the correction teaches the analyst to
delete the audit trail instead of writing one.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_sections as cs

NAME = "Cochin Minerals and Rutile Limited_13 Sep 2026_CARE_Rating Rationale.md"
results = []
NL = chr(10)


def check(desc, got, want_fire):
    fired = got is not None
    ok = fired == want_fire
    print(f"[{'OK' if ok else 'FAIL'}] {desc}")
    print(f"       fired={fired} (want {want_fire})" + (f"\n       -> {got[:150]}" if got else ""))
    results.append(ok)


# 1. the claim exactly as it shipped - CareEdge's own action is in the library
bad = ("No CRA has published a rating action for this issuer: a word-boundary search of all "
       "three reference libraries returns nothing.")
check("fires on the claim as it actually shipped", cs._prior_rating_absence_contradicted(bad, NAME), True)

# 2. the other two phrasings the same report used
check("fires on 'no rating history exists'",
      cs._prior_rating_absence_contradicted("No rating history exists for this issuer.", NAME), True)

# 3. does NOT fire on the corrected report, which quotes the old claim to supersede it
corrected = ("CORRECTED 13-Sep-2026 - this paragraph previously asserted that no CRA had "
             "published a rating action for this issuer. That was false.")
check("does NOT fire on a correction note quoting the old claim",
      cs._prior_rating_absence_contradicted(corrected, NAME), False)

# 4. does NOT fire for an issuer with no same-issuer library file
check("does NOT fire when the library genuinely holds nothing for this issuer",
      cs._prior_rating_absence_contradicted(bad, "Zzyzx Widgets Limited_01 Jan 2026_Rating Rationale.md"),
      False)

# 5. a peer sharing ONE name token must not count as the same issuer. "Cochin Shipyard" and
#    "Sarda Energy & Minerals" both sit in the libraries and both share a token with this
#    issuer; matching on either would import a peer's rating, which is worse than the
#    absence-claim (failure mode 24 from the other direction).
tokens = cs._issuer_tokens(NAME)
print(f"\n       issuer tokens = {sorted(tokens)}")
strict = tokens >= {"cochin", "minerals", "rutile"}
print(f"[{'OK' if strict else 'FAIL'}] all three name tokens required, so a one-token peer cannot match")
results.append(strict)

# 6. the live corrected report on disk must pass
live = Path(__file__).resolve().parent.parent / "Companies" / "cochin-minerals-and-rutile-limited" / NAME
if live.exists():
    check("live corrected CMRL rationale passes",
          cs._prior_rating_absence_contradicted(live.read_text(encoding="utf-8"), NAME), False)

# 7. the qualified disclosure that produced this probe's first false positive. Happy Forgings
#    says "no prior rating action BY THIS ANALYSIS" and then names the live grade - correct
#    disclosure, not a false absence-claim.
qualified = ("Independent assessment (no prior rating action by this analysis; company carries "
             "an actual outstanding Crisil AA/Stable rating, see divergence below)")
check("does NOT fire on a qualified disclosure that names the live rating",
      cs._prior_rating_absence_contradicted(qualified, "Happy Forgings Limited_11 Aug 2026_CRISIL_Rating Rationale.md"),
      False)

# 8. REGRESSION GUARD. The suppression window must not be keyed on a rating grade appearing
#    nearby: a CareEdge summary table sits directly above the note that carried the original
#    false claim, so a grade-based rule would have passed the very report this probe exists
#    for. This control reproduces that layout.
with_table_above = (
    "|Long-term bank facilities|To be confirmed by issuer|CARE A-; Stable|Assigned|" + NL +
    "|Short-term bank facilities|To be confirmed by issuer|CARE A2+|Assigned|" + NL + NL +
    "Rated amounts are not stated, and that is a finding rather than an omission. "
    "No CRA has published a rating action for this issuer: a word-boundary search "
    "of all three reference libraries returns nothing.")
check("still fires when a rating grade sits in the window (the original CMRL layout)",
      cs._prior_rating_absence_contradicted(with_table_above, NAME), True)

n_fail = sum(1 for r in results if not r)
print(f"\n{len(results)-n_fail}/{len(results)} controls passed" + (f" - {n_fail} FAILED" if n_fail else ""))
sys.exit(1 if n_fail else 0)
