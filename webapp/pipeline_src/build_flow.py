"""Generate the credit-rating pipeline page (inline SVG, coordinates on a fixed grid)."""
import html

W, H = 760, 2500
L, C, R = 150, 380, 610          # column centres
BW, BH = 200, 50                 # box size
DW, DH = 86, 52                  # diamond half-width / half-height
LPAD = 205                       # left rail that holds the review agents
AGX, AGW, AGH = -88, 154, 46     # agent badge centre-x, width, height
SPINE = AGX - AGW / 2            # the vertical oversight line the badges hang off

svg = []
add = svg.append


def box(x, y, code, label, kind=""):
    cls = "n " + kind
    add(f'<g class="{cls.strip()}"><rect x="{x-BW/2}" y="{y-BH/2}" width="{BW}" height="{BH}" rx="3"/>'
        f'<text class="code" x="{x}" y="{y-6}" text-anchor="middle">{html.escape(code)}</text>'
        f'<text class="lbl" x="{x}" y="{y+13}" text-anchor="middle">{html.escape(label)}</text></g>')


def diamond(x, y, l1, l2, kind=""):
    pts = f"{x},{y-DH} {x+DW},{y} {x},{y+DH} {x-DW},{y}"
    cls = ("d " + kind).strip()
    add(f'<g class="{cls}"><polygon points="{pts}"/>'
        f'<text class="lbl" x="{x}" y="{y-4}" text-anchor="middle">{html.escape(l1)}</text>'
        f'<text class="lbl" x="{x}" y="{y+12}" text-anchor="middle">{html.escape(l2)}</text></g>')


def edge(d, loop=False, head=True):
    cls = "e loop" if loop else "e"
    mk = "ha" if loop else "h"
    tail = f' marker-end="url(#{mk})"' if head else ""
    add(f'<path class="{cls}" d="{d}"{tail}/>')


def chip(x, y, t):
    w = 7.2 * len(t) + 12
    add(f'<g class="chip"><rect x="{x-w/2}" y="{y-9}" width="{w}" height="18" rx="2"/>'
        f'<text x="{x}" y="{y+4}" text-anchor="middle">{html.escape(t)}</text></g>')


def agent(cy, name, role, head=False):
    """A review-agent badge on the left rail: name + one-line role. head = the chief."""
    cls = "ag head" if head else "ag"
    add(f'<g class="{cls}"><rect x="{AGX-AGW/2}" y="{cy-AGH/2}" width="{AGW}" height="{AGH}" rx="4"/>'
        f'<text class="agcode" x="{AGX}" y="{cy-3}" text-anchor="middle">{html.escape(name)}</text>'
        f'<text class="agrole" x="{AGX}" y="{cy+13}" text-anchor="middle">{html.escape(role)}</text></g>')


def phase(y, t):
    add(f'<line class="ph" x1="16" y1="{y}" x2="724" y2="{y}"/>'
        f'<text class="phl" x="16" y="{y-8}">{html.escape(t)}</text>')


# ------------------------------------------------------------------ 1 scope and read
phase(24, "01 · SCOPE AND READ")
box(C, 70, "S1", "Intake, engagement type")
edge(f"M{C},95 V123")
box(C, 150, "S1a · script", "Pre-flight search", "mech")
edge(f"M{C},175 V206")
diamond(C, 260, "Information", "adequate?")
edge(f"M{C-DW},260 H{L} V343"); chip(222, 260, "fail")
box(L, 370, "HALT", "Ask issuer for documents", "side")
edge(f"M{C},312 V343"); chip(C, 328, "pass")
box(C, 370, "S1b", "Read every document")
edge(f"M{C},395 V423")
box(C, 450, "S2–S3", "Route, read methodology")
edge(f"M{C},475 V506")
diamond(C, 560, "Scope statement", "fits the issuer?")
edge(f"M{C-DW},560 H{L} V643"); chip(222, 560, "no")
box(L, 670, "REJECT", "Drop file, record why", "side")
edge(f"M{L-BW/2},670 H34 V450 H{C-BW/2-2}", loop=True); chip(158, 450, "re-route")
edge(f"M{C},612 V643"); chip(C, 628, "yes")
box(C, 670, "S4", "Learn craft from peers")

# ------------------------------------------------------------------ 2 data work
phase(730, "02 · INDEPENDENT DATA WORK")
edge(f"M{C},695 V753")
box(C, 780, "S5–S6 · code", "Extract, compute ratios")
edge(f"M{C},805 V836")
diamond(C, 890, "Tie-outs reconcile,", "coverage measured?", "mech")
edge(f"M{C+DW},890 H{R-BW/2-2}"); chip(488, 890, "fail")
box(R, 890, "FIX", "Fix or declare divergence", "side")
edge(f"M{R},865 V780 H{C+BW/2+2}", loop=True); chip(R, 826, "retry")
edge(f"M{C},942 V1003"); chip(C, 960, "pass")
edge(f"M{C},975 H{L} V1003")
edge(f"M{C},975 H{R} V1003")
box(L, 1030, "S7", "Trace every claim")
box(C, 1030, "S7b", "Instrument details")
box(R, 1030, "S8", "Materiality sweep")
edge(f"M{L},1055 V1085 H{C}", head=False)
edge(f"M{R},1055 V1085 H{C}", head=False)
edge(f"M{C},1055 V1103")
box(C, 1130, "S9", "Save the workpaper")

# ------------------------------------------------------------------ 3 view
phase(1180, "03 · INDEPENDENT RATING VIEW")
edge(f"M{C},1155 V1203")
edge(f"M{C},1195 H{L} V1203")
edge(f"M{C},1195 H{R} V1203")
box(L, 1230, "S10–S11", "Compliance map, liquidity")
box(C, 1230, "S12", "Forward view")
box(R, 1230, "S12b · workbook", "Scorecard anchor", "mech")
edge(f"M{L},1255 V1288 H{C}", head=False)
edge(f"M{R},1255 V1288 H{C}", head=False)
edge(f"M{C},1255 V1303")
box(C, 1330, "S13 · prior report unopened", "Form the rating view")
edge(f"M{C},1355 V1383")
box(C, 1410, "S14 · divergence table", "Open prior report")
edge(f"M{C},1435 V1466")
diamond(C, 1520, "Anchor within", "±2 notches?")
edge(f"M{C+DW},1520 H{R-BW/2-2}"); chip(488, 1520, "no")
box(R, 1520, "ARGUE", "Name what it cannot see", "side")
edge(f"M{R},1545 V1630 H{C+BW/2+2}")
edge(f"M{C},1572 V1603"); chip(C, 1588, "yes")
box(C, 1630, "S15", "Analytical package")

# ------------------------------------------------------------------ 4 draft and decide
phase(1690, "04 · DRAFT AND DECIDE")
edge(f"M{C},1655 V1713")
box(C, 1740, "S16", "Draft from skeleton")
edge(f"M{C},1765 V1793")
box(C, 1820, "S17", "Two drift checks")
edge(f"M{C},1845 V1876")
diamond(C, 1930, "Section audit", "exits 0?", "mech")
edge(f"M{C-DW},1930 H{L+BW/2+2}"); chip(272, 1930, "fail")
box(L, 1930, "FIX", "Fix the draft", "side")
edge(f"M{L},1905 V1740 H{C-BW/2-2}", loop=True); chip(L, 1822, "redraft")
edge(f"M{C},1982 V2016"); chip(C, 1999, "pass")
diamond(C, 2070, "Reviewer", "signs off?")
edge(f"M{C+DW},2070 H{R-BW/2-2}"); chip(488, 2070, "return")
box(R, 2070, "RETURN", "Back to failing step", "side")
edge(f"M{C},2122 V2153"); chip(C, 2137, "sign-off")
box(C, 2180, "S17c", "Committee decides", "decide")

# ------------------------------------------------------------------ 5 publish and monitor
phase(2240, "05 · PUBLISH AND MONITOR")
edge(f"M{C},2205 V2263")
box(C, 2290, "S18b", "Issuer review, bring-down")
edge(f"M{C},2315 V2343")
box(C, 2370, "S18–S19", "Deliver, log lessons")
edge(f"M{C},2395 V2423")
box(C, 2450, "S20–S21", "Surveillance")
edge(f"M{C+BW/2},2450 H742 V70 H{C+BW/2+2}", loop=True); chip(611, 2450, "trigger: re-run")

# ------------------------------------------------------------------ review-agent rail (left)
# Each phase (or group of steps) has an agent that reviews the work and fixes what it finds;
# the head agent (rating-chief) re-runs each phase's gate to confirm the fix landed before it
# signs the case off. The badges hang off the chief's vertical oversight spine.
add(f'<text class="phl" x="{SPINE}" y="30">REVIEW AGENTS</text>')
add(f'<path class="agspine" d="M{SPINE},89 V2075"/>')
agent(66, "rating-chief", "HEAD · verifies each phase", head=True)
for cy, nm, role in [(300, "rating-intake", "Ph 1 · scope & read"),
                     (900, "rating-ratios", "Ph 2 · ratios"),
                     (1400, "rating-analysis", "Ph 3 · rating view"),
                     (1875, "rating-draft", "Ph 4 · draft"),
                     (2072, "rating-reviewer", "17b · four-eyes")]:
    agent(cy, nm, role)
    add(f'<path class="agtick" d="M{AGX+AGW/2},{cy} H8" marker-end="url(#ha)"/>')  # reviews & fixes

defs = ('<defs>'
        '<marker id="h" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="8" markerHeight="8" '
        'orient="auto-start-reverse"><path class="mh" d="M0,0 L8,4 L0,8 z"/></marker>'
        '<marker id="ha" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="8" markerHeight="8" '
        'orient="auto-start-reverse"><path class="mha" d="M0,0 L8,4 L0,8 z"/></marker>'
        '</defs>')

# Draw edges first so boxes sit on top of line ends.
edges = [s for s in svg if s.startswith("<path") or s.startswith('<line')]
rest = [s for s in svg if s not in edges]
body_svg = (f'<svg class="flow" viewBox="{-LPAD} 0 {W+LPAD} {H}" role="img" aria-label="Credit '
            'rating pipeline: five phases from intake to surveillance, with six gates. Failing a '
            'gate either halts the case, loops back to the step that produced the problem, or '
            'forces the divergence to be argued in writing; nothing reaches the Rating Committee '
            'without passing the section audit and reviewer sign-off. A left rail of six review '
            'agents - one per phase plus an independent reviewer - hangs off a head agent, '
            'rating-chief, which re-runs each phase gate to confirm the fix landed before sign-off.">'
            + defs + "".join(edges) + "".join(rest) + "</svg>")

import os

HERE = os.path.dirname(os.path.abspath(__file__))
page = open(os.path.join(HERE, "flow_template.html"), encoding="utf-8").read()
out = page.replace("<!--SVG-->", body_svg)

# The web tool frames this file from webapp/static/ (the /process route), so it is written there
# as a complete document: the charset keeps the middle dots and dashes intact, and body{margin:0}
# keeps the iframe's height-to-content fit exact. Writing straight to static/ is the point - the
# tool used to serve a hand-copied file that silently fell behind every change made here.
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       '<style>body{margin:0}</style>\n'
       + out.replace('\n<div class="wrap">', '\n</head>\n<body>\n<div class="wrap">', 1).rstrip()
       + '\n\n</body></html>')
dst = os.path.normpath(os.path.join(HERE, "..", "static", "credit_rating_pipeline.html"))
open(dst, "w", encoding="utf-8").write(doc)
print("written", len(doc), "bytes ->", dst)
