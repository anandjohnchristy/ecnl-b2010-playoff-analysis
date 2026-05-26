import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ecnl_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ══════════════════════════════════════════════════════════════════
# P2a: H2H self-comparison — show error instead of silent hide
# ══════════════════════════════════════════════════════════════════

# 1. Add CSS for same-team error
OLD_H2H_CSS = '  .h2h-content { display: none; }'
NEW_H2H_CSS = ('  .h2h-content { display: none; }\n'
               '  .h2h-same-err { display:none; align-items:center; gap:10px;\n'
               '    background:#f8514914; border:1px solid #f8514944; color:var(--red);\n'
               '    border-radius:8px; padding:12px 16px; font-size:13px; margin-bottom:16px; }\n'
               '  .h2h-same-err svg { flex-shrink:0; }')
assert OLD_H2H_CSS in html, 'MISSING: h2h-content CSS'
html = html.replace(OLD_H2H_CSS, NEW_H2H_CSS, 1)
changes.append('1. H2H same-team error CSS added')

# 2. Add error div in HTML (after h2h-pickers, before h2h-content)
OLD_H2H_DIV = '  <div class="h2h-content" id="h2hContent">'
NEW_H2H_DIV = ('  <div class="h2h-same-err" id="h2hSameTeamErr" role="alert">\n'
               '    <svg width="16" height="16" viewBox="0 0 16 16" fill="none">'
               '<circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5"/>'
               '<path d="M8 4.5v4M8 10.5v1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'
               '</svg>\n'
               '    Select two <em>different</em> teams to compare.\n'
               '  </div>\n'
               '  <div class="h2h-content" id="h2hContent">')
assert OLD_H2H_DIV in html, 'MISSING: h2h-content div'
html = html.replace(OLD_H2H_DIV, NEW_H2H_DIV, 1)
changes.append('2. H2H same-team error div added')

# 3. Update runH2H() to show error on same selection
OLD_RUN_H2H = ('  if (!nameA || !nameB || nameA === nameB) {\n'
               '    content.style.display = \'none\';\n'
               '    return;\n'
               '  }')
NEW_RUN_H2H = ('  const sameErr = document.getElementById(\'h2hSameTeamErr\');\n'
               '  if (!nameA || !nameB) {\n'
               '    content.style.display = \'none\';\n'
               '    sameErr.style.display = \'none\';\n'
               '    return;\n'
               '  }\n'
               '  if (nameA === nameB) {\n'
               '    content.style.display = \'none\';\n'
               '    sameErr.style.display = \'flex\';\n'
               '    return;\n'
               '  }\n'
               '  sameErr.style.display = \'none\';')
assert OLD_RUN_H2H in html, 'MISSING: runH2H guard'
html = html.replace(OLD_RUN_H2H, NEW_RUN_H2H, 1)
changes.append('3. runH2H(): same-team shows red error instead of silent hide')

# ══════════════════════════════════════════════════════════════════
# P2b: Search empty state
# ══════════════════════════════════════════════════════════════════

# 4. Add CSS for empty state
OLD_TABLE_CSS = '  .table-wrap { max-width: 1400px; margin: 0 auto; padding: 0 24px 24px; overflow-x: auto; }'
NEW_TABLE_CSS = ('  .table-wrap { max-width: 1400px; margin: 0 auto; padding: 0 24px 24px; overflow-x: auto; }\n'
                 '  .table-empty { display:none; max-width:1400px; margin:0 auto;\n'
                 '    padding:40px 24px; text-align:center; }\n'
                 '  .table-empty-icon { font-size:2rem; margin-bottom:12px; color:var(--border); }\n'
                 '  .table-empty-msg { font-size:15px; font-weight:600; color:var(--text); margin-bottom:6px; }\n'
                 '  .table-empty-hint { font-size:12px; color:var(--muted); }')
assert OLD_TABLE_CSS in html, 'MISSING: table-wrap CSS'
html = html.replace(OLD_TABLE_CSS, NEW_TABLE_CSS, 1)
changes.append('4. Empty state CSS added')

# 5. Add empty state div after table-wrap
OLD_TABLE_WRAP_END = ('</div>\n'
                      '\n'
                      '<!-- METHODOLOGY -->')
NEW_TABLE_WRAP_END = ('</div>\n'
                      '<div class="table-empty" id="tableEmpty" role="status" aria-live="polite">\n'
                      '  <div class="table-empty-icon">&#9651;</div>\n'
                      '  <div class="table-empty-msg">No teams match <span id="tableEmptyTerm"></span></div>\n'
                      '  <div class="table-empty-hint">Check spelling, or search by partial name'
                      ' &mdash; e.g. &ldquo;wichita&rdquo; finds &ldquo;FC Wichita&rdquo;</div>\n'
                      '</div>\n'
                      '\n'
                      '<!-- METHODOLOGY -->')
assert OLD_TABLE_WRAP_END in html, 'MISSING: table-wrap end'
html = html.replace(OLD_TABLE_WRAP_END, NEW_TABLE_WRAP_END, 1)
changes.append('5. Empty state div added after table')

# 6. Update renderTable() to show/hide empty state
OLD_TBODY_END = ("  tbody.innerHTML = filtered.map((t, i) => {\n"
                 "    const winPctStr = (t.winPct*100).toFixed(1)+'%';")
NEW_TBODY_END = ("  const emptyEl = document.getElementById('tableEmpty');\n"
                 "  const emptyTerm = document.getElementById('tableEmptyTerm');\n"
                 "  if (filtered.length === 0) {\n"
                 "    document.getElementById('mainTable').style.display = 'none';\n"
                 "    if (emptyTerm) emptyTerm.textContent = search ? `\"${search}\"` : 'current filters';\n"
                 "    if (emptyEl) emptyEl.style.display = 'block';\n"
                 "    return;\n"
                 "  }\n"
                 "  document.getElementById('mainTable').style.display = '';\n"
                 "  if (emptyEl) emptyEl.style.display = 'none';\n"
                 "  tbody.innerHTML = filtered.map((t, i) => {\n"
                 "    const winPctStr = (t.winPct*100).toFixed(1)+'%';")
assert OLD_TBODY_END in html, 'MISSING: tbody.innerHTML start'
html = html.replace(OLD_TBODY_END, NEW_TBODY_END, 1)
changes.append('6. renderTable(): empty state shown/hidden dynamically')

# ══════════════════════════════════════════════════════════════════
# P2c: Team name title tooltips — conference + seed context on hover
# ══════════════════════════════════════════════════════════════════

# 7. Add title attribute to team-name td
OLD_TD_TEAM = ('      <td class="team-name">${t.name}${flagsHtml(t)}'
               '<span class="conf-badge">${t.conf}</span></td>')
NEW_TD_TEAM = ('      <td class="team-name" title="${t.name} &mdash; ${t.conf} Conference (Seed #${t.seed})">'
               '${t.name}${flagsHtml(t)}<span class="conf-badge">${t.conf}</span></td>')
assert OLD_TD_TEAM in html, 'MISSING: team-name td'
html = html.replace(OLD_TD_TEAM, NEW_TD_TEAM, 1)
changes.append('7. Team name cells: title tooltip with conference + seed')

with open('ecnl_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'P2 fixes applied ({len(changes)} changes):')
for c in changes:
    print(' ', c)
print(f'\nFile size: {len(html)/1024:.1f}KB')
