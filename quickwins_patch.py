import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ecnl_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ── 1. Hero meta: remove emoji, switch to CSS dot-separators ─────────────
OLD_META_CSS = ('  .hero-meta { display: flex; flex-wrap: wrap; gap: 20px; margin-top: 12px; }\n'
                '  .hero-meta span { font-size: 13px; color: var(--muted); display:flex; align-items:center; gap:5px; }\n'
                '  .hero-meta span b { color: var(--text); }')
NEW_META_CSS = ('  .hero-meta { display: flex; flex-wrap: wrap; gap: 0; margin-top: 14px; align-items: center; }\n'
                '  .hero-meta span { font-size: 13px; color: var(--muted); }\n'
                '  .hero-meta span + span::before { content: "\\00B7"; padding: 0 12px; color: var(--border); }\n'
                '  .hero-meta span b { color: var(--text); font-weight: 600; }')
assert OLD_META_CSS in html, 'MISSING: hero-meta CSS'
html = html.replace(OLD_META_CSS, NEW_META_CSS, 1)
changes.append('1. Hero meta: CSS dot-separator replaces gap+emoji layout')

OLD_META_HTML = ('<div class="hero-meta">\n'
                 '      <span>\U0001f4cd <b>San Diego, CA</b></span>\n'
                 '      <span>\U0001f4c5 <b>June 25, 2026</b></span>\n'
                 '      <span>\U0001f3c6 <b>54 Qualified Teams</b></span>\n'
                 '      <span>⚽ <b>15 Conferences</b></span>\n'
                 '    </div>')
NEW_META_HTML = ('<div class="hero-meta">\n'
                 '      <span><b>San Diego, CA</b></span>\n'
                 '      <span><b>June 25, 2026</b></span>\n'
                 '      <span><b>54 Qualified Teams</b></span>\n'
                 '      <span><b>15 Conferences</b></span>\n'
                 '    </div>')
assert OLD_META_HTML in html, 'MISSING: hero-meta HTML'
html = html.replace(OLD_META_HTML, NEW_META_HTML, 1)
changes.append('2. Hero meta: emoji removed (📍📅🏆⚽)')

# ── 2. Focus rings: raise opacity from 12% to 65% ───────────────────────
OLD_FOCUS1 = ('  .controls input:focus, .controls select:focus { border-color: var(--accent);'
              ' box-shadow: 0 0 0 3px rgba(88,166,255,.12); }')
NEW_FOCUS1 = ('  .controls input:focus, .controls select:focus { border-color: var(--accent);'
              ' box-shadow: 0 0 0 3px rgba(88,166,255,.25); outline: none; }')
assert OLD_FOCUS1 in html, 'MISSING: controls focus ring'
html = html.replace(OLD_FOCUS1, NEW_FOCUS1, 1)
changes.append('3. Controls focus ring: opacity 12% → 25% (WCAG visible)')

OLD_FOCUS2 = '  .h2h-picker select:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(88,166,255,.12); }'
NEW_FOCUS2 = '  .h2h-picker select:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(88,166,255,.25); outline: none; }'
assert OLD_FOCUS2 in html, 'MISSING: h2h picker focus ring'
html = html.replace(OLD_FOCUS2, NEW_FOCUS2, 1)
changes.append('4. H2H picker focus ring: opacity 12% → 25%')

# Also fix general focus for interactive elements (thead th, gl-tab, score-toggle)
OLD_GENERAL_FOCUS = '  thead th:hover { color: var(--accent); }'
NEW_GENERAL_FOCUS = ('  thead th:hover { color: var(--accent); }\n'
                     '  thead th:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; border-radius: 2px; }\n'
                     '  .gl-tab:focus-visible, .score-toggle:focus-visible {\n'
                     '    outline: 2px solid var(--accent); outline-offset: 2px; }\n'
                     '  .h2h-picker select:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }')
assert OLD_GENERAL_FOCUS in html, 'MISSING: thead th:hover'
html = html.replace(OLD_GENERAL_FOCUS, NEW_GENERAL_FOCUS, 1)
changes.append('5. Added :focus-visible outlines for table headers, tabs, score-toggle')

# ── 3. transition: all → specific properties on score-toggle ────────────
OLD_TOGGLE = ('    cursor: pointer; font-weight: 600; letter-spacing: 0.5px;'
              ' transition: all .15s cubic-bezier(.16,1,.3,1); }')
NEW_TOGGLE = ('    cursor: pointer; font-weight: 600; letter-spacing: 0.5px;'
              ' transition: color .15s, border-color .15s, background .15s; }')
assert OLD_TOGGLE in html, 'MISSING: score-toggle transition'
html = html.replace(OLD_TOGGLE, NEW_TOGGLE, 1)
changes.append('6. score-toggle: transition:all → specific properties')

# ── 4. prefers-reduced-motion: guard badge-pulse ─────────────────────────
OLD_ANIM = ('  @keyframes badge-pulse {\n'
            '    0%, 100% { opacity:1; box-shadow:0 0 0 0 rgba(88,166,255,.45); }\n'
            '    50% { opacity:.5; box-shadow:0 0 0 5px rgba(88,166,255,0); }\n'
            '  }')
NEW_ANIM = ('  @keyframes badge-pulse {\n'
            '    0%, 100% { opacity:1; box-shadow:0 0 0 0 rgba(88,166,255,.45); }\n'
            '    50% { opacity:.5; box-shadow:0 0 0 5px rgba(88,166,255,0); }\n'
            '  }\n'
            '  @media (prefers-reduced-motion: reduce) {\n'
            '    .hero-badge .badge-dot { animation: none; opacity: 1; }\n'
            '  }')
assert OLD_ANIM in html, 'MISSING: badge-pulse keyframes'
html = html.replace(OLD_ANIM, NEW_ANIM, 1)
changes.append('7. badge-pulse: guarded with prefers-reduced-motion')

# ── 5. Flag pills: remove emoji, add title attributes ───────────────────
# Table row flags (lines ~701-708)
OLD_FLAGS = ("""  if (t.isEliteDef) f += '<span class="flag flag-def">\U0001f535 DEF</span>';
  if (t.isEliteOff) f += '<span class="flag flag-off">\U0001f7e2 OFF</span>';
  if (t.h2025 === 'Champion') f += '<span class="flag flag-champ">\U0001f947 2025</span>';
  else if (t.h2025 === 'Finalist') f += '<span class="flag flag-final">\U0001f948 2025F</span>';
  else if (t.h2025 === 'Semi') f += '<span class="flag flag-semi">\U0001f3c5 2025SF</span>';
  else if (t.h2025 === 'QF') f += '<span class="flag flag-qf">⬛ 2025QF</span>';
  if (t.h2024 === 'Champion') f += '<span class="flag flag-champ">\U0001f947 2024</span>';
  else if (t.h2024 === 'Finalist') f += '<span class="flag flag-final">\U0001f948 2024F</span>';""")
NEW_FLAGS = ("""  if (t.isEliteDef) f += '<span class="flag flag-def" title="Elite Defense: GA/G < 0.65">DEF</span>';
  if (t.isEliteOff) f += '<span class="flag flag-off" title="Elite Offense: GF/G > 2.50">OFF</span>';
  if (t.h2025 === 'Champion') f += '<span class="flag flag-champ" title="2025 ECNL National Champion">&#x2605; 2025</span>';
  else if (t.h2025 === 'Finalist') f += '<span class="flag flag-final" title="2025 ECNL National Finalist">2025 Final</span>';
  else if (t.h2025 === 'Semi') f += '<span class="flag flag-semi" title="2025 ECNL National Semifinalist">2025 SF</span>';
  else if (t.h2025 === 'QF') f += '<span class="flag flag-qf" title="2025 ECNL National Quarterfinalist">2025 QF</span>';
  if (t.h2024 === 'Champion') f += '<span class="flag flag-champ" title="2024 ECNL National Champion">&#x2605; 2024</span>';
  else if (t.h2024 === 'Finalist') f += '<span class="flag flag-final" title="2024 ECNL National Finalist">2024 Final</span>';""")
assert OLD_FLAGS in html, 'MISSING: flag pill JS'
html = html.replace(OLD_FLAGS, NEW_FLAGS, 1)
changes.append('8. Flag pills: emoji removed, title attributes added')

# ── 6. Unify team-card transition timing ────────────────────────────────
OLD_CARD_T = ('    transition: border-color .15s, transform .2s cubic-bezier(.16,1,.3,1); }')
NEW_CARD_T = ('    transition: border-color .15s, transform .15s cubic-bezier(.16,1,.3,1); }')
assert OLD_CARD_T in html, 'MISSING: team-card transition'
html = html.replace(OLD_CARD_T, NEW_CARD_T, 1)
changes.append('10. Team card: unified transition timing to .15s')

# ── 7. Extend hero::before gradient line ────────────────────────────────
OLD_BEFORE = "    background: linear-gradient(90deg, #1f6feb, #58a6ff 60%, transparent); }"
NEW_BEFORE = "    background: linear-gradient(90deg, #1f6feb, #58a6ff 70%, transparent 95%); }"
assert OLD_BEFORE in html, 'MISSING: hero::before gradient'
html = html.replace(OLD_BEFORE, NEW_BEFORE, 1)
changes.append('11. hero::before: gradient extends to 70% (more confident line)')

with open('ecnl_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Quick wins applied:')
for c in changes:
    print(' ', c)
print()
print('File size: %.1fKB' % (len(html)/1024))
