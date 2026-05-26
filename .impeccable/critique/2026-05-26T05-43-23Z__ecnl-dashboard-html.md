---
target: ecnl_dashboard.html
total_score: 21
p0_count: 0
p1_count: 2
timestamp: 2026-05-26T05-43-23Z
slug: ecnl-dashboard-html
---
## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 2 | Sort direction indicator is faint; no loading state |
| 2 | Match System / Real World | 3 | Soccer stats correct; "confStr" needs plain-English label |
| 3 | User Control and Freedom | 3 | Filters clearable; no single "reset all" action |
| 4 | Consistency and Standards | 2 | 6 border-radius values; uppercase on 14 element types |
| 5 | Error Prevention | 2 | H2H picker allows self-comparison; search returns blank void |
| 6 | Recognition Rather Than Recall | 3 | Columns labeled; team abbreviations unexplained |
| 7 | Flexibility and Efficiency | 1 | No keyboard shortcuts; no permalink/share |
| 8 | Aesthetic and Minimalist Design | 2 | Stats bar + hero + controls + pills compete above fold |
| 9 | Error Recovery | 1 | H2H no-meetings gives no suggestion; empty search gives nothing |
| 10 | Help and Documentation | 2 | Methodology visible; no tooltip/glossary for ECNL terms |
| **Total** | | **21/40** | Acceptable |

## Priority Issues

P1: uppercase on 14 element types kills typographic hierarchy  
P1: 6 identical stat cards — no visual priority  
P2: emoji in hero meta (📍📅🏆⚽) — top AI-generated tell  
P2: prefers-reduced-motion not honored for badge-pulse animation  
P2: focus ring at 12% opacity — fails WCAG 2.1 SC 1.4.11  

## Persona Red Flags

Alex: mouse-only sort; no permalink for H2H comparison; no multi-team compare  
Sam: invisible focus on table rows (hover-only); flag pills no aria-label; W/L/D color-only  
Morgan: "confStr" label is code variable; team abbreviations unexplained; row click does nothing
