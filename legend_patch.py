import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ecnl_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# 1. Add CSS dot helpers for legend pills
OLD_PILL_CSS = ('  .legend-pill { display:inline-flex; align-items:center; gap:5px; background:var(--surface);\n'
                '    border:1px solid var(--border); padding:5px 10px; border-radius:20px; font-size:11px; }')
NEW_PILL_CSS = ('  .legend-pill { display:inline-flex; align-items:center; gap:6px; background:var(--surface);\n'
                '    border:1px solid var(--border); padding:5px 10px; border-radius:20px; font-size:11px; }\n'
                '  .lp-dot { width:7px; height:7px; border-radius:50%; flex-shrink:0; }\n'
                '  .lp-blue   { background:var(--accent); }\n'
                '  .lp-green  { background:var(--green); }\n'
                '  .lp-gold   { background:var(--gold); }\n'
                '  .lp-purple { background:var(--purple); }\n'
                '  .lp-orange { background:var(--orange); }')
assert OLD_PILL_CSS in html, 'MISSING: legend-pill CSS'
html = html.replace(OLD_PILL_CSS, NEW_PILL_CSS, 1)
changes.append('1. CSS dot helpers added')

# 2. Legend pill HTML: emoji -> colored dots
OLD_PILLS = (
    '  <div class="legend-pill">\U0001f535 Elite Defense</div>\n'
    '  <div class="legend-pill">\U0001f7e2 Elite Offense</div>\n'
    '  <div class="legend-pill">\U0001f947 2025 Champ</div>\n'
    '  <div class="legend-pill">\U0001f948 2025 Final</div>\n'
    '  <div class="legend-pill">\U0001f3c5 Semifinal</div>'
)
NEW_PILLS = (
    '  <div class="legend-pill"><span class="lp-dot lp-blue"></span>Elite Defense</div>\n'
    '  <div class="legend-pill"><span class="lp-dot lp-green"></span>Elite Offense</div>\n'
    '  <div class="legend-pill"><span class="lp-dot lp-gold"></span>2025 Champ</div>\n'
    '  <div class="legend-pill"><span class="lp-dot lp-purple"></span>2025 Final</div>\n'
    '  <div class="legend-pill"><span class="lp-dot lp-orange"></span>Semifinal</div>'
)
assert OLD_PILLS in html, 'MISSING: legend pill HTML'
html = html.replace(OLD_PILLS, NEW_PILLS, 1)
changes.append('2. Legend pills: emoji -> CSS dots')

# 3. Flag section h3 headers
OLD_H3_DEF = ('      <h3 style="color:#58a6ff">\U0001f535 Elite Defense'
              ' — Clean Sheet Leaders (GA/G &lt; 0.65)</h3>')
NEW_H3_DEF = ('      <h3 style="color:#58a6ff">Elite Defense'
              ' — Clean Sheet Leaders (GA/G &lt; 0.65)</h3>')
assert OLD_H3_DEF in html, 'MISSING: defense h3'
html = html.replace(OLD_H3_DEF, NEW_H3_DEF, 1)
changes.append('3. Defense h3: emoji removed')

OLD_H3_OFF = ('      <h3 style="color:#3fb950">\U0001f7e2 Consistent Offense'
              ' — Offensive Leaders (GF/G &gt; 2.50)</h3>')
NEW_H3_OFF = ('      <h3 style="color:#3fb950">Consistent Offense'
              ' — Offensive Leaders (GF/G &gt; 2.50)</h3>')
assert OLD_H3_OFF in html, 'MISSING: offense h3'
html = html.replace(OLD_H3_OFF, NEW_H3_OFF, 1)
changes.append('4. Offense h3: emoji removed')

# 4. Team card style label (lightning bolt emoji)
OLD_PROF_STYLE = (
    "      ${prof.style ? `<div style=\"font-size:11px;color:var(--accent);margin-bottom:6px\">"
    "⚡ ${prof.style}</div>` : ''}"
)
NEW_PROF_STYLE = (
    "      ${prof.style ? `<div style=\"font-size:11px;color:var(--accent);margin-bottom:6px\">"
    "${prof.style}</div>` : ''}"
)
assert OLD_PROF_STYLE in html, 'MISSING: prof.style label'
html = html.replace(OLD_PROF_STYLE, NEW_PROF_STYLE, 1)
changes.append('5. Team card style label: ⚡ removed')

# 5. Team card strengths label (checkmark emoji)
OLD_PROF_STR = (
    "      ${prof.strengths ? `<div style=\"font-size:11px;color:var(--green);margin-top:8px\">"
    "✅ ${prof.strengths}</div>` : ''}"
)
NEW_PROF_STR = (
    "      ${prof.strengths ? `<div style=\"font-size:11px;color:var(--green);margin-top:8px\">"
    "${prof.strengths}</div>` : ''}"
)
assert OLD_PROF_STR in html, 'MISSING: prof.strengths label'
html = html.replace(OLD_PROF_STR, NEW_PROF_STR, 1)
changes.append('6. Team card strengths label: ✅ removed')

# 6. H2H no-meetings icon (clipboard emoji)
OLD_ICON = '        <div class="h2h-no-meetings-icon">\U0001f4cb</div>'
NEW_ICON = '        <div class="h2h-no-meetings-icon" aria-hidden="true">∅</div>'
assert OLD_ICON in html, 'MISSING: no-meetings icon'
html = html.replace(OLD_ICON, NEW_ICON, 1)
changes.append('7. H2H no-meetings: \U0001f4cb -> ∅ (mathematical empty set)')

with open('ecnl_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Changes applied:')
for c in changes:
    print(' ', c)
print('File size: %.1fKB' % (len(html) / 1024))
