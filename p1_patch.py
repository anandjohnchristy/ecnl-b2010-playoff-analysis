import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ecnl_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ══════════════════════════════════════════════════════════════════
# P1a: UPPERCASE AUDIT — remove from all non-header elements
# Keep ONLY: thead th (table column headers)
# ══════════════════════════════════════════════════════════════════

# 1. .stat-label — stat card labels
OLD = ('  .stat-label { font-size: 11px; color: var(--muted); text-transform: uppercase;\n'
       '    letter-spacing: 0.6px; margin-bottom: 4px; }')
NEW = ('  .stat-label { font-size: 11px; color: var(--muted); font-weight: 500;\n'
       '    margin-bottom: 4px; }')
assert OLD in html, 'MISSING: stat-label'
html = html.replace(OLD, NEW, 1); changes.append('1. .stat-label: uppercase removed')

# 2. .card-rank — "Performance Rank" in team cards
OLD = ('  .card-rank { font-size: 11px; color: var(--muted); text-transform: uppercase;\n'
       '    letter-spacing: 1px; margin-bottom: 6px; }')
NEW = ('  .card-rank { font-size: 11px; color: var(--muted); font-weight: 500;\n'
       '    margin-bottom: 6px; }')
assert OLD in html, 'MISSING: card-rank'
html = html.replace(OLD, NEW, 1); changes.append('2. .card-rank: uppercase removed')

# 3. .h2h-picker label — "Team A / Team B" labels above selects
OLD = ('  .h2h-picker label { display: block; font-size: 11px; text-transform: uppercase;\n'
       '    letter-spacing: 0.8px; color: var(--muted); margin-bottom: 6px; font-weight: 600; }')
NEW = ('  .h2h-picker label { display: block; font-size: 11px;\n'
       '    color: var(--muted); margin-bottom: 6px; font-weight: 600; }')
assert OLD in html, 'MISSING: h2h-picker label'
html = html.replace(OLD, NEW, 1); changes.append('3. .h2h-picker label: uppercase removed')

# 4. .h2h-games-title — "Direct meetings" panel title
OLD = ('  .h2h-games-title { font-size: 12px; font-weight: 700; color: var(--muted);\n'
       '    text-transform: uppercase; letter-spacing: 0.7px; margin-bottom: 12px; }')
NEW = ('  .h2h-games-title { font-size: 12px; font-weight: 600; color: var(--muted);\n'
       '    margin-bottom: 12px; }')
assert OLD in html, 'MISSING: h2h-games-title'
html = html.replace(OLD, NEW, 1); changes.append('4. .h2h-games-title: uppercase removed')

# 5. .h2h-record-label — "W-L-D this season" label
OLD = ('  .h2h-record-label { font-size: 11px; color: var(--muted); text-transform: uppercase;\n'
       '    letter-spacing: 0.6px; margin-bottom: 14px; }')
NEW = ('  .h2h-record-label { font-size: 11px; color: var(--muted);\n'
       '    margin-bottom: 14px; }')
assert OLD in html, 'MISSING: h2h-record-label'
html = html.replace(OLD, NEW, 1); changes.append('5. .h2h-record-label: uppercase removed')

# 6. .h2h-goals-label — "Aggregate score" under the goals display
OLD = ('  .h2h-goals-label { font-size: 10px; color: var(--muted); text-align: center;\n'
       '    text-transform: uppercase; letter-spacing: 0.5px; }')
NEW = ('  .h2h-goals-label { font-size: 10px; color: var(--muted); text-align: center; }')
assert OLD in html, 'MISSING: h2h-goals-label'
html = html.replace(OLD, NEW, 1); changes.append('6. .h2h-goals-label: uppercase removed')

# 7. .pred-title — "Prediction" panel header
OLD = ('  .pred-title { font-size: 13px; font-weight: 700; color: var(--muted);\n'
       '    text-transform: uppercase; letter-spacing: 0.7px; margin-bottom: 16px; }')
NEW = ('  .pred-title { font-size: 13px; font-weight: 700; color: var(--muted);\n'
       '    margin-bottom: 16px; }')
assert OLD in html, 'MISSING: pred-title'
html = html.replace(OLD, NEW, 1); changes.append('7. .pred-title: uppercase removed')

# 8. .pred-factor .lbl — mini factor labels in prediction bars
OLD = ('  .pred-factor .lbl { font-size: 10px; color: var(--muted); text-transform: uppercase;\n'
       '    letter-spacing: 0.5px; margin-bottom: 4px; }')
NEW = '  .pred-factor .lbl { font-size: 10px; color: var(--muted); margin-bottom: 4px; }'
assert OLD in html, 'MISSING: pred-factor lbl'
html = html.replace(OLD, NEW, 1); changes.append('8. .pred-factor .lbl: uppercase removed')

# 9. .gl-stat-lbl — game log stat labels (GP, W, L, D…)
OLD = ('  .gl-stat-lbl { font-size:10px; color:var(--muted); text-transform:uppercase;\n'
       '    letter-spacing:.5px; margin-top:2px; }')
NEW = '  .gl-stat-lbl { font-size:10px; color:var(--muted); margin-top:2px; }'
assert OLD in html, 'MISSING: gl-stat-lbl'
html = html.replace(OLD, NEW, 1); changes.append('9. .gl-stat-lbl: uppercase removed')

# 10. .gl-game-hdr — game log table column header row
OLD = ('  .gl-game-hdr { background:var(--surface); font-size:10px; color:var(--muted);\n'
       '    font-weight:600; text-transform:uppercase; letter-spacing:.5px; }')
NEW = '  .gl-game-hdr { background:var(--surface); font-size:10px; color:var(--muted); font-weight:600; }'
assert OLD in html, 'MISSING: gl-game-hdr'
html = html.replace(OLD, NEW, 1); changes.append('10. .gl-game-hdr: uppercase removed')

# 11. .gl-ha — HOME/AWAY badges (keep uppercase; very short badge, appropriate;
#     just remove excess letter-spacing)
OLD = ('  .gl-ha { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:.5px;\n'
       '    background:var(--surface2); border-radius:4px; padding:2px 5px; text-align:center; }')
NEW = ('  .gl-ha { font-size:10px; font-weight:700; text-transform:uppercase;\n'
       '    background:var(--surface2); border-radius:4px; padding:2px 5px; text-align:center; }')
assert OLD in html, 'MISSING: gl-ha'
html = html.replace(OLD, NEW, 1); changes.append('11. .gl-ha: letter-spacing removed (kept uppercase for H/A badge)')

# 12. score-toggle residual letter-spacing
OLD = ('    cursor: pointer; font-weight: 600; letter-spacing: 0.5px;'
       ' transition: color .15s, border-color .15s, background .15s; }')
NEW = ('    cursor: pointer; font-weight: 600;'
       ' transition: color .15s, border-color .15s, background .15s; }')
assert OLD in html, 'MISSING: score-toggle letter-spacing'
html = html.replace(OLD, NEW, 1); changes.append('12. .score-toggle: residual letter-spacing removed')

# ══════════════════════════════════════════════════════════════════
# P1b: STAT CARD DIFFERENTIATION — 3 visual tiers via left border
# ══════════════════════════════════════════════════════════════════

# 13. Add tier CSS after .stat-card block
OLD = ('  .stat-card:hover { border-color: #484f58; }')
NEW = ('  .stat-card:hover { border-color: #484f58; }\n'
       '  .stat-card.stat-leader { border-left: 3px solid var(--green); padding-left: 15px; }\n'
       '  .stat-card.stat-def    { border-left-color: var(--accent); }\n'
       '  .stat-card.stat-champ  { border-left: 3px solid var(--gold); padding-left: 15px; }\n'
       '  .stat-card.stat-seed   { border-left-color: var(--accent); }\n'
       '  .stat-card.stat-name .stat-value { font-size: 1.1rem; }')
assert OLD in html, 'MISSING: stat-card hover'
html = html.replace(OLD, NEW, 1); changes.append('13. Stat card tier CSS added (leader/champ/seed)')

# 14. Update JS to assign tier classes + remove inline font-size hack
OLD = ("""  document.getElementById('statsBar').innerHTML = [
    ['54', 'Qualified Teams', `${confs} conferences`],
    [totalGF.toLocaleString(), 'Total Goals Scored', `${(totalGF/totalGP).toFixed(2)} per game`],
    [avgPPG, 'Avg PPG (Field)', 'All 54 teams'],
    [topOff.gfpg.toFixed(2), 'Top GF/G', topOff.name],
    [topDef.gapg.toFixed(2), 'Lowest GA/G', topDef.name],
    ['Legends FC', '2025 Champion', 'Defending title'],
    ['LAFC So Cal', '2024 Champion', '2023-24 U14'],
    ['XF Academy', '#1 Seed', `${teams.find(t=>t.name==='XF Academy').score} pts score`],
  ].map(([v,l,s]) => `<div class="stat-card"><div class="stat-label">${l}</div>
    <div class="stat-value" style="font-size:${v.length>8?'1rem':'1.4rem'}">${v}</div>
    <div class="stat-sub">${s}</div></div>`).join('');""")
NEW = ("""  document.getElementById('statsBar').innerHTML = [
    ['54',                      'Qualified Teams',   `${confs} conferences`,                          ''],
    [totalGF.toLocaleString(),  'Total Goals Scored',`${(totalGF/totalGP).toFixed(2)} per game`,     ''],
    [avgPPG,                    'Avg PPG (Field)',    'All 54 teams',                                  ''],
    [topOff.gfpg.toFixed(2),   'Top GF/G',           topOff.name,                                   'stat-leader'],
    [topDef.gapg.toFixed(2),   'Lowest GA/G',         topDef.name,                                  'stat-leader stat-def'],
    ['Legends FC',              '2025 Champion',      'Defending title',                              'stat-champ stat-name'],
    ['LAFC So Cal',             '2024 Champion',      '2023-24 U14',                                  'stat-champ stat-name'],
    ['XF Academy',              '#1 Seed',            `${teams.find(t=>t.name==='XF Academy').score} pts score`, 'stat-champ stat-name stat-seed'],
  ].map(([v,l,s,cls]) => `<div class="stat-card ${cls}"><div class="stat-label">${l}</div>
    <div class="stat-value">${v}</div>
    <div class="stat-sub">${s}</div></div>`).join('');""")
assert OLD in html, 'MISSING: statsBar JS'
html = html.replace(OLD, NEW, 1); changes.append('14. Stat card JS: tier classes assigned, inline font-size hack removed')

with open('ecnl_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'P1 fixes applied ({len(changes)} changes):')
for c in changes:
    print(' ', c)
print(f'\nFile size: {len(html)/1024:.1f}KB')
