# 2026 ECNL Boys B2010 National Playoff Analysis

Interactive dashboard for analyzing the 54 teams qualified for the 2026 ECNL Boys B2010 (U16) National Playoffs in San Diego, CA (June 25, 2026).

## Features

- **Team rankings** — composite performance score across win rate, goal differential, goals scored/allowed, and points-per-game, weighted by opponent quality
- **Head-to-head lookup** — select any two qualified teams to see their full meeting history, covering both regular season conference games and ECNL showcase events
- **Match predictor** — win probability estimate for a hypothetical San Diego matchup based on H2H record, season stats, and scoring metrics
- **Season stat comparison** — side-by-side W/L/D, GF/G, GA/G, PPG, and postseason pedigree
- **Tactical flags** — elite defense (GA/G < 0.65) and elite offense (GF/G > 2.50) badges
- **Filters** — search by name, filter by conference, defensive/offensive tier, or playoff pedigree

## Data

| Source | Games | Pairs |
|--------|------:|------:|
| Conference regular season (15 conferences) | 144 | 95 |
| ECNL Showcase events (6 events) | 195 | 194 |
| **Total** | **339** | **289** |

### Showcase events included

| Event | Date |
|-------|------|
| Phoenix Showcase | Nov 2025 |
| South Carolina Showcase | Dec 2025 |
| Florida Showcase | Jan 2026 |
| Las Vegas Showcase | Jan 2026 |
| Indianapolis (ECNL) Showcase | Apr 2026 |
| Virginia Showcase | May 2026 |

Game results scraped from the [AthleteOne / TGS API](https://api.athleteone.com).

## Files

| File | Description |
|------|-------------|
| `ecnl_dashboard.html` | Self-contained dashboard (open in any browser) |
| `ecnl_raw_data.json` | Raw conference schedule/standings data |
| `ecnl_h2h_analysis.json` | Processed conference H2H pairs |
| `h2h_map.json` | Conference H2H map (95 pairs, 144 games) |
| `showcase_divs.json` | TGS division/flight IDs for B2010 showcase events |
| `showcase_games_raw.json` | Raw showcase game results (464 B2010 games) |
| `showcase_h2h.json` | Showcase H2H pairs filtered to qualified teams |
| `h2h_map_merged.json` | Merged conference + showcase H2H map |
| `h2h_js.txt` | Final JS `const H2H_MAP` for dashboard injection |

## Usage

Open `ecnl_dashboard.html` directly in a browser — no server or dependencies required.
