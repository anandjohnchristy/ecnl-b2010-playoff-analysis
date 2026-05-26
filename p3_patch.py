import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ecnl_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ══════════════════════════════════════════════════════════════════
# P3a: BORDER-RADIUS AUDIT — consolidate to 4px / 8px / 20px
# (3px for thin bars, 50% for circles stay as-is)
# ══════════════════════════════════════════════════════════════════

# 1. hero-badge: 6px → 4px (it's a chip/badge, not an input)
OLD = '    padding:5px 12px 5px 10px; border-radius:6px; font-size:12px;'
NEW = '    padding:5px 12px 5px 10px; border-radius:4px; font-size:12px;'
assert OLD in html, 'MISSING: hero-badge radius'
html = html.replace(OLD, NEW, 1); changes.append('1. hero-badge: 6px → 4px')

# 2. controls input + select: 6px → 8px
OLD = '    padding: 8px 12px; border-radius: 6px; font-size: 13px; outline: none; }'
NEW = '    padding: 8px 12px; border-radius: 8px; font-size: 13px; outline: none; }'
assert OLD in html, 'MISSING: controls input/select radius'
html = html.replace(OLD, NEW, 1); changes.append('2. controls input/select: 6px → 8px')

# 3. score-toggle: 6px → 8px
OLD = '    color: var(--muted); padding: 8px 14px; border-radius: 6px; font-size: 12px;'
NEW = '    color: var(--muted); padding: 8px 14px; border-radius: 8px; font-size: 12px;'
assert OLD in html, 'MISSING: score-toggle radius'
html = html.replace(OLD, NEW, 1); changes.append('3. score-toggle: 6px → 8px')

# 4. hist-pill: 12px → 20px (it's a pill shape, same as legend-pill)
OLD = '  .hist-pill { display:inline-block; font-size:10px; padding:2px 7px; border-radius:12px; font-weight:600; }'
NEW = '  .hist-pill { display:inline-block; font-size:10px; padding:2px 7px; border-radius:20px; font-weight:600; }'
assert OLD in html, 'MISSING: hist-pill radius'
html = html.replace(OLD, NEW, 1); changes.append('4. hist-pill: 12px → 20px')

# 5. stat-card: 10px → 8px
OLD = '    border-radius: 10px; padding: 16px 18px; transition: border-color .15s; }'
NEW = '    border-radius: 8px; padding: 16px 18px; transition: border-color .15s; }'
assert OLD in html, 'MISSING: stat-card radius'
html = html.replace(OLD, NEW, 1); changes.append('5. stat-card: 10px → 8px')

# 6. method-item: 6px → 8px
OLD = '  .method-item { background: var(--surface2); border-radius: 6px; padding: 12px 14px; }'
NEW = '  .method-item { background: var(--surface2); border-radius: 8px; padding: 12px 14px; }'
assert OLD in html, 'MISSING: method-item radius'
html = html.replace(OLD, NEW, 1); changes.append('6. method-item: 6px → 8px')

# 7. team-card: 10px → 8px
OLD = '    border-radius: 10px; padding: 18px 20px;'
NEW = '    border-radius: 8px; padding: 18px 20px;'
assert OLD in html, 'MISSING: team-card radius'
html = html.replace(OLD, NEW, 1); changes.append('7. team-card: 10px → 8px')

# 8. card-stat: 6px → 8px
OLD = '  .card-stat { text-align: center; background: var(--surface2); border-radius: 6px; padding: 6px; }'
NEW = '  .card-stat { text-align: center; background: var(--surface2); border-radius: 8px; padding: 6px; }'
assert OLD in html, 'MISSING: card-stat radius'
html = html.replace(OLD, NEW, 1); changes.append('8. card-stat: 6px → 8px')

# 9. h2h-compare-grid AND h2h-summary share: 10px + overflow:hidden + margin-bottom → both 8px
OLD = ('    background: var(--surface); border: 1px solid var(--border); border-radius: 10px;\n'
       '    overflow: hidden; margin-bottom: 20px; }')
NEW = ('    background: var(--surface); border: 1px solid var(--border); border-radius: 8px;\n'
       '    overflow: hidden; margin-bottom: 20px; }')
count = html.count(OLD)
assert count == 2, f'EXPECTED 2 occurrences of h2h-grid/summary radius, found {count}'
html = html.replace(OLD, NEW); changes.append('9. h2h-compare-grid + h2h-summary: 10px → 8px (2 replacements)')

# 10. h2h-game-score: 6px → 8px
OLD = '    background: var(--surface2); padding: 4px 10px; border-radius: 6px; min-width: 60px; text-align: center; }'
NEW = '    background: var(--surface2); padding: 4px 10px; border-radius: 8px; min-width: 60px; text-align: center; }'
assert OLD in html, 'MISSING: h2h-game-score radius'
html = html.replace(OLD, NEW, 1); changes.append('10. h2h-game-score: 6px → 8px')

# 11. h2h-games-panel: 10px → 8px
OLD = '    border-radius: 10px; padding: 16px 20px; margin-bottom: 20px; }'
NEW = '    border-radius: 8px; padding: 16px 20px; margin-bottom: 20px; }'
assert OLD in html, 'MISSING: h2h-games-panel radius'
html = html.replace(OLD, NEW, 1); changes.append('11. h2h-games-panel: 10px → 8px')

# 12. h2h-no-meetings: 10px → 8px
OLD = ('    border-radius: 10px; padding: 20px 24px; margin-bottom: 20px;\n'
       '    display: flex; align-items: center; gap: 14px; }')
NEW = ('    border-radius: 8px; padding: 20px 24px; margin-bottom: 20px;\n'
       '    display: flex; align-items: center; gap: 14px; }')
assert OLD in html, 'MISSING: h2h-no-meetings radius'
html = html.replace(OLD, NEW, 1); changes.append('12. h2h-no-meetings: 10px → 8px')

# 13. pred-panel: 10px → 8px
OLD = '    border-radius: 10px; padding: 20px; }'
NEW = '    border-radius: 8px; padding: 20px; }'
assert OLD in html, 'MISSING: pred-panel radius'
html = html.replace(OLD, NEW, 1); changes.append('13. pred-panel: 10px → 8px')

# 14. gl-tab: 6px → 8px
OLD = '    padding:6px 16px; border-radius:6px; font-size:12px; cursor:pointer; font-weight:600;'
NEW = '    padding:6px 16px; border-radius:8px; font-size:12px; cursor:pointer; font-weight:600;'
assert OLD in html, 'MISSING: gl-tab radius'
html = html.replace(OLD, NEW, 1); changes.append('14. gl-tab: 6px → 8px')

# 15. gl-note: 6px → 8px
OLD = '    background:var(--surface); border:1px solid var(--border); border-radius:6px; }'
NEW = '    background:var(--surface); border:1px solid var(--border); border-radius:8px; }'
assert OLD in html, 'MISSING: gl-note radius'
html = html.replace(OLD, NEW, 1); changes.append('15. gl-note: 6px → 8px')

# ══════════════════════════════════════════════════════════════════
# P3b: RESET ALL FILTERS — button + CSS + JS
# ══════════════════════════════════════════════════════════════════

# 16. Add CSS for reset button (reuse score-toggle style, add display:none)
OLD_BTN_CSS = ('  .score-toggle:hover { border-color: var(--accent); color: var(--accent); }')
NEW_BTN_CSS = ('  .score-toggle:hover { border-color: var(--accent); color: var(--accent); }\n'
               '  .reset-btn { display:none; background:none; border:1px solid var(--border);\n'
               '    color:var(--muted); padding:8px 14px; border-radius:8px; font-size:12px;\n'
               '    cursor:pointer; font-weight:600; white-space:nowrap;\n'
               '    transition:color .15s, border-color .15s; }\n'
               '  .reset-btn:hover { border-color:var(--red); color:var(--red); }\n'
               '  .reset-btn.visible { display:block; }')
assert OLD_BTN_CSS in html, 'MISSING: score-toggle hover'
html = html.replace(OLD_BTN_CSS, NEW_BTN_CSS, 1); changes.append('16. reset-btn CSS added')

# 17. Add reset button in controls HTML (after last legend-pill, before closing </div>)
OLD_CONTROLS_END = ('  <div class="legend-pill"><span class="lp-dot lp-orange"></span>Semifinal</div>\n'
                    '</div>')
NEW_CONTROLS_END = ('  <div class="legend-pill"><span class="lp-dot lp-orange"></span>Semifinal</div>\n'
                    '  <button class="reset-btn" id="resetBtn" onclick="resetFilters()">Clear filters</button>\n'
                    '</div>')
assert OLD_CONTROLS_END in html, 'MISSING: controls closing div'
html = html.replace(OLD_CONTROLS_END, NEW_CONTROLS_END, 1); changes.append('17. reset-btn added to controls HTML')

# 18. Add resetFilters() JS function near renderTable event listeners
OLD_LISTENERS = ('document.getElementById(\'searchInput\').addEventListener(\'input\', renderTable);\n'
                 'document.getElementById(\'confFilter\').addEventListener(\'change\', renderTable);\n'
                 'document.getElementById(\'flagFilter\').addEventListener(\'change\', renderTable);')
NEW_LISTENERS = ('document.getElementById(\'searchInput\').addEventListener(\'input\', renderTable);\n'
                 'document.getElementById(\'confFilter\').addEventListener(\'change\', renderTable);\n'
                 'document.getElementById(\'flagFilter\').addEventListener(\'change\', renderTable);\n'
                 '\n'
                 'function resetFilters() {\n'
                 '  document.getElementById(\'searchInput\').value = \'\';\n'
                 '  document.getElementById(\'confFilter\').value = \'\';\n'
                 '  document.getElementById(\'flagFilter\').value = \'\';\n'
                 '  renderTable();\n'
                 '}')
assert OLD_LISTENERS in html, 'MISSING: filter event listeners'
html = html.replace(OLD_LISTENERS, NEW_LISTENERS, 1); changes.append('18. resetFilters() JS function added')

# 19. Show/hide reset button from inside renderTable()
OLD_RENDER_START = ('function renderTable() {\n'
                    '  const search = document.getElementById(\'searchInput\').value.toLowerCase();\n'
                    '  const conf = document.getElementById(\'confFilter\').value;\n'
                    '  const flag = document.getElementById(\'flagFilter\').value;')
NEW_RENDER_START = ('function renderTable() {\n'
                    '  const search = document.getElementById(\'searchInput\').value.toLowerCase();\n'
                    '  const conf = document.getElementById(\'confFilter\').value;\n'
                    '  const flag = document.getElementById(\'flagFilter\').value;\n'
                    '  const resetBtn = document.getElementById(\'resetBtn\');\n'
                    '  if (resetBtn) resetBtn.classList.toggle(\'visible\', !!(search || conf || flag));')
assert OLD_RENDER_START in html, 'MISSING: renderTable start'
html = html.replace(OLD_RENDER_START, NEW_RENDER_START, 1); changes.append('19. renderTable: shows/hides reset button based on filter state')

with open('ecnl_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'P3 fixes applied ({len(changes)} changes):')
for c in changes:
    print(' ', c)
print(f'\nFile size: {len(html)/1024:.1f}KB')
