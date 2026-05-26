---
target: ecnl_dashboard.html
total_score: 25
p0_count: 0
p1_count: 0
timestamp: 2026-05-26T06-11-35Z
slug: ecnl-dashboard-html
---
## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 2 | Sort arrow still faint; no loading/rendering indicator |
| 2 | Match System / Real World | 3 | Soccer stats correct; "confStr" still a code variable in column label |
| 3 | User Control and Freedom | 3 | Filters clearable; still no single "reset all" action |
| 4 | Consistency and Standards | 3 | `text-transform:uppercase` reduced 14→2 types; border-radius still inconsistent across elements |
| 5 | Error Prevention | 3 | H2H self-comparison now shows red error; search returns no-results state ✓ |
| 6 | Recognition Rather Than Recall | 3 | Title tooltips added for team names (conf + seed); flag pill titles added; abbreviations still unexplained in table |
| 7 | Flexibility and Efficiency | 1 | No keyboard shortcuts; no permalink for H2H comparison |
| 8 | Aesthetic and Minimalist Design | 3 | All emoji removed; Outfit font loaded; stat card tier hierarchy (leader/champ borders); hero meta CSS dots |
| 9 | Error Recovery | 2 | Search shows "No teams match X" with partial-name hint ✓; H2H same-team error with inline message ✓ |
| 10 | Help and Documentation | 2 | Methodology visible; no tooltip/glossary for ECNL-specific terms (confStr, showcase form) |
| **Total** | | **25/40** | Good — +4 from baseline |

## Changes Since Baseline (21 → 25)

H#4 +1: `text-transform:uppercase` stripped from 14 element types; kept only on `thead th` and H/A badge  
H#5 +1: H2H self-comparison shows red alert div; search no-results has message + helpful hint  
H#8 +1: All emoji replaced with CSS primitives (dots, `·`, `★`, `∅`); Outfit font; stat card visual tiers  
H#9 +1: Search empty state "No teams match X — check spelling, or search by partial name"; H2H error message  

Also resolved from P2 checklist:
- `prefers-reduced-motion` guard on badge-pulse animation
- Focus rings raised 12% → 25%; `:focus-visible` rules on headers, tabs, score-toggle
- Legend pills: emoji → colored CSS dots (`.lp-dot`)
- Flag pills: emoji removed, `title` attributes with plain-English labels
- Hero meta: emoji removed, CSS `::before` dot separators

## Remaining Priority Issues

P2: "confStr" column label — replace with "Conf Strength" or "Conference Strength"  
P2: Sort direction indicator — faint 0.4 opacity arrow; add active-sort class with full opacity  
P2: border-radius inconsistency — audit and consolidate to 3 values (4px / 8px / 20px)  
P3: No keyboard shortcut or permalink for H2H pairings  
P3: Team abbreviations in table unexplained (title tooltip on the stat column headers could help)

## Persona Red Flags

Alex: Still no permalink; multi-team compare not present; sort UX low-contrast  
Sam: Flag pills now have titles ✓; W/L/D still color-only distinction  
Morgan: "confStr" still a code variable; showcase form weight undocumented in methodology blurb
