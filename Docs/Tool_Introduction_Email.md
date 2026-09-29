**Subject:** The credit rating tool I mentioned — what it does and how it works

Hi [Name],

Thanks for taking the time. As promised, here is a fuller explanation of the credit rating tool I have built. I have kept it plain rather than technical, but gone into enough detail that you can judge whether it is actually useful.

---

## In one line

It is an AI analyst that produces a complete credit rating rationale — the kind ICRA, CRISIL and CareEdge publish — working from a company's own annual reports and quarterly filings, and following the rating agency's own published methodology and report format.

You give it the company's documents. It gives you back a full rating package.

---

## The problem I was trying to solve

Writing a rating rationale is slow, and most of the time does not go into judgement. It goes into extraction, computation, cross-checking, and formatting. An analyst spends days pulling line items out of a 300-page annual report, building the ratio suite, chasing down which subsidiary is consolidated, and making sure no mandatory section is missing.

The second problem is subtler. Mistakes in this work are *repeatable*. The same errors recur — a figure taken from the wrong year, a metric quoted from another sector's template, a number carried over from a previous report instead of computed, a claim that data "was not available" when nobody actually searched for it. Individually each is small. Together they are what separates a report that reads as expert from one that does not.

The tool is built around both problems, and honestly the second one is the more interesting half.

---

## How it works

**1. Pre-flight — it looks before it speaks.**
Before reading anything, a script searches every uploaded document *and* a reference library of ~2,100 published agency reports, and prints what actually exists: prior ratings, the company's own credit-ratings note, subsidiaries, instrument details, capex plans, ESG data, and the key operating metric for that sector.

This has a hard consequence built in: anything the pre-flight finds can never later be written up as "not disclosed". That one rule kills an entire class of error.

**2. It reads every document in full.**
Not skims — reads, section by section, and logs what each one contributed. Annual report notes, the auditor's report, contingent liabilities, related-party disclosures, the borrowings note, the risk factors. Drafting cannot begin until every file is in that log.

**3. Every number is computed in code.**
No figure is ever typed from memory or copied from a previous report. A Python script extracts the line items and computes the full ratio suite using that agency's own definitions — which genuinely differ between agencies, and differ again between corporates, banks and NBFCs.

Each computed figure is then *tied out* against the company's own disclosures. If my EBITDA does not reproduce the company's stated EBITDA, that gap gets investigated and either resolved or disclosed. It never gets quietly forced to match.

**4. It forms its own view before looking at anyone else's.**
The rating opinion is reached from the methodology and the numbers first. Only afterwards does it open the existing ratings to compare — and any difference has to be explained, not smoothed over.

**5. A script decides whether it is allowed to be delivered.**
A final audit checks that every mandatory section is present, that the liquidity descriptor follows from its arithmetic, that rated amounts are stated or explicitly flagged as unconfirmed, and about a dozen other quality tests. If it fails, delivery is blocked. Not "flagged for review" — blocked.

---

## What you actually get

- The full rating rationale in that agency's published format
- A working Excel of the financial spreads, with a tie-out tab showing every reconciliation
- A 5-year three-statement forecast model, including a stress case
- A scorecard giving an independent quantitative "anchor" grade as a cross-check
- A workpaper recording every assumption, every judgement call, and every gap in the data

---

## The part I am actually proud of

The tool keeps a written library of every mistake it has ever made — currently 37 of them, each named, described, and traced to the real case where it happened.

The important rule is that **a lesson is not allowed to stay as advice.** Every one of those 37 has to ship with an automated test that catches it, or an explicit written admission that no test is possible. Writing "be more careful next time" into a manual is not treated as a fix, because it demonstrably is not one.

A recent example, and I will be straightforward that this was my error:

The tool rated a tyre manufacturer one notch too low. The cause was that the company reported its foreign-exchange result in two different places depending on whether it was a gain or a loss — gains in "Other Income", losses buried inside "Other Expenses". The standard operating-margin formula strips out other income, so it removed the gain year automatically but kept the loss year in. The result was a computed margin of 21.3% against a true 24.3%, and a full-year margin that appeared to be *falling* when it was actually *rising*. The entire report was then written around a margin decline that had not happened.

That is now two permanent automated checks: one that opens up those aggregate notes and lists every non-operating item hiding inside them before any margin is calculated, and one that refuses to pass a report which quotes an operating margin without stating how it treated forex and one-offs.

The point is not that the tool is error-free. It is that its errors are converted into tests, so each one can only happen once.

---

## What it is not

Worth being clear, because I would rather set this expectation now than later:

- **It does not issue ratings.** Every output is explicitly labelled an analytical exercise, not an official publication of any agency.
- **It does not replace the analyst or the rating committee.** It produces the package; a human forms the decision. The design deliberately separates who prepares, who reviews, and who decides.
- **It is only as good as the documents it is given.** Where something genuinely is not in the filings, it says so and records the search that proves it — rather than guessing or quietly leaving it out.

---

## Where this could be useful

The obvious uses are first-cut rationales, surveillance reviews where most of the work is refreshing numbers, and internal credit notes at banks and NBFCs that follow a similar structure. It is also quite good as a checking layer over work that has already been done, since the audit scripts run independently of who wrote the report.

I would genuinely value your view on whether this addresses a real bottleneck as you see it, or whether I am solving the wrong half of the problem. Happy to walk you through a live example on a company of your choosing — that tends to be more convincing than a description.

Best regards,
[Your name]
[Phone / LinkedIn]

---
---

# VERSION 2 — Short intro pitch (cold first contact)

**Subject:** Worth your view on a rating-rationale tool

Hi [Name],

Quick introduction — I've built a tool that drafts complete credit rating rationales in ICRA, CRISIL and CareEdge formats, working from a company's own annual reports and quarterly filings.

It's built on the agencies' own published material: 217 rating methodology documents and roughly 2,100 published rationales across the three. The methodologies are what it applies — scope statements, rating factors, indicative metric bands. The published rationales are how it learned the craft: how a sector argument is constructed, which metrics matter in which industry, what separates AAA from A. Facts only ever come from the company's own filings — a published report can teach format, never supply a number.

What comes out of a single run:

- The rationale in that agency's published format and section order
- Financial spreads in Excel, with a tie-out tab reconciling every figure to the company's own disclosures
- A 5-year three-statement forecast model with a stress case
- An independent scorecard grade as a quantitative cross-check
- A workpaper recording every assumption, judgement call and data gap

Every number is computed in code — nothing typed from memory, nothing carried over from a previous report. Before anything is delivered, a script blocks the output if a mandatory section is missing, if the liquidity descriptor doesn't follow from its own arithmetic, or if any of 37 checks for recurring errors fires. Each of those 37 exists because the tool got something wrong once.

To be clear on what it isn't: it doesn't issue ratings, and it doesn't replace the analyst or the committee. It produces the package; a human forms the decision.

You've spent far longer in ratings than I have, and I'd value your read on whether this addresses a real bottleneck. Happy to send a worked example on any company you name — no call needed.

Best regards,
[Your name]
[Phone / LinkedIn]
