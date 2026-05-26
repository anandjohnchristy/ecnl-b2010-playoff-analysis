---
target: ecnl_dashboard.html
total_score: 26
p0_count: 0
p1_count: 0
timestamp: 2026-05-26T06-15-21Z
slug: ecnl-dashboard-html
---
## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Sort arrow now 0.55 opacity (unsorted), 0.9 hover, 1.0+bold sorted — clear affordance; no loading state remains |
| 2 | Match System / Real World | 3 | Conference Strength now shows avg PPG in prediction; soccer stats correct throughout |
| 3 | User Control and Freedom | 3 | Filters clearable; still no single "reset all" action |
| 4 | Consistency and Standards | 3 | `text-transform:uppercase` reserved for thead+H/A badge only; border-radius still inconsistent |
| 5 | Error Prevention | 3 | H2H self-comparison error; search empty state — both working |
| 6 | Recognition Rather Than Recall | 3 | Title tooltips on team names; flag titles; Conference Strength PPG value now visible in prediction |
| 7 | Flexibility and Efficiency | 1 | No keyboard shortcuts; no permalink for H2H comparison |
| 8 | Aesthetic and Minimalist Design | 3 | No emoji; Outfit font; stat card tiers; CSS dot separators; clean hero |
| 9 | Error Recovery | 2 | Search empty-state hint; H2H same-team error — both working |
| 10 | Help and Documentation | 2 | Methodology block + all 6 prediction factors now visible; no ECNL term glossary |
| **Total** | | **26/40** | Good — +5 from baseline |

## Changes Since Previous Run (25 → 26)

H#1 +1: Sort arrow opacity 0.4 → 0.55 (unsorted), hover 0.9, sorted 1.0 bold — sortable columns clearly afforded; active sort column immediately legible  
Conference Strength (15% weight) now shown as a named prediction factor with raw conference avg PPG value

## Remaining Priority Issues

P2: No "reset all filters" button — user must clear search + change each dropdown separately  
P2: border-radius audit — 4px / 8px / 20px values mixed inconsistently across components  
P3: No keyboard shortcuts (e.g., `/` to focus search) or H2H permalink  
P3: W/L/D distinction is color-only (green/red/gray) — no shape or text pattern for colorblind users

## Persona Red Flags

Alex: Still no permalink; no multi-team compare  
Sam: W/L/D color-only; no aria-labels on flag pills beyond title attribute  
Morgan: Methodology + prediction now show all 6 factors clearly ✓; row click does nothing
