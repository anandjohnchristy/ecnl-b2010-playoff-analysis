import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ecnl_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ══════════════════════════════════════════════════════════════════
# 1. ROOT VARIABLES — full light theme token swap
# ══════════════════════════════════════════════════════════════════
OLD_ROOT = ('  :root {\n'
            '    --bg: #0d1117; --surface: #161b22; --surface2: #21262d;\n'
            '    --border: #30363d; --text: #e6edf3; --muted: #8b949e;\n'
            '    --accent: #58a6ff; --green: #3fb950; --red: #f85149;\n'
            '    --yellow: #d29922; --purple: #bc8cff; --orange: #e3a835;\n'
            '    --gold: #ffd700; --silver: #c0c0c0; --bronze: #cd7f32;\n'
            '  }')
NEW_ROOT = ('  :root {\n'
            '    --bg: #f1f5f9; --surface: #ffffff; --surface2: #f8fafc;\n'
            '    --border: #e2e8f0; --text: #0f172a; --muted: #64748b;\n'
            '    --accent: #2563eb; --green: #16a34a; --red: #dc2626;\n'
            '    --yellow: #ca8a04; --purple: #7c3aed; --orange: #ea580c;\n'
            '    --gold: #b45309; --silver: #64748b; --bronze: #92400e;\n'
            '  }')
assert OLD_ROOT in html, 'MISSING: :root'
html = html.replace(OLD_ROOT, NEW_ROOT, 1)
changes.append('1. :root: full light theme token swap')

# ══════════════════════════════════════════════════════════════════
# 2. HERO — keep dark for contrast, add depth gradient
# ══════════════════════════════════════════════════════════════════
OLD_HERO = ('  .hero { background: #080c12; border-bottom: 1px solid var(--border);\n'
            '    padding: 28px 24px 28px; position: relative; overflow: hidden; }')
NEW_HERO = ('  .hero { background: linear-gradient(160deg, #0f172a 0%, #1e293b 100%);\n'
            '    border-bottom: 1px solid #334155;\n'
            '    padding: 28px 24px 28px; position: relative; overflow: hidden; }')
assert OLD_HERO in html, 'MISSING: .hero'
html = html.replace(OLD_HERO, NEW_HERO, 1)
changes.append('2. Hero: flat black → depth gradient (#0f172a → #1e293b)')

# 3. Hero top accent line — update to lighter blues (stays on dark bg)
OLD_BEFORE = '    background: linear-gradient(90deg, #1f6feb, #58a6ff 70%, transparent 95%); }'
NEW_BEFORE = '    background: linear-gradient(90deg, #3b82f6, #60a5fa 70%, transparent 95%); }'
assert OLD_BEFORE in html, 'MISSING: hero::before'
html = html.replace(OLD_BEFORE, NEW_BEFORE, 1)
changes.append('3. Hero::before: updated gradient blues')

# 4. Hero badge — stays on dark hero, keep bright accent tints
OLD_BADGE = '    background:#1f6feb14; border:1px solid #1f6feb55; color:var(--accent);'
NEW_BADGE = '    background:#3b82f618; border:1px solid #3b82f655; color:#60a5fa;'
assert OLD_BADGE in html, 'MISSING: hero-badge tint'
html = html.replace(OLD_BADGE, NEW_BADGE, 1)
changes.append('4. Hero badge: tint updated for new accent on dark bg')

# 5. Badge pulse rgba — stays on dark hero, keep bright
OLD_PULSE = ('    0%, 100% { opacity:1; box-shadow:0 0 0 0 rgba(88,166,255,.45); }\n'
             '    50% { opacity:.5; box-shadow:0 0 0 5px rgba(88,166,255,0); }')
NEW_PULSE = ('    0%, 100% { opacity:1; box-shadow:0 0 0 0 rgba(96,165,250,.45); }\n'
             '    50% { opacity:.5; box-shadow:0 0 0 5px rgba(96,165,250,0); }')
assert OLD_PULSE in html, 'MISSING: badge-pulse rgba'
html = html.replace(OLD_PULSE, NEW_PULSE, 1)
changes.append('5. Badge pulse: updated rgba for new blue')

# 6. Hero meta text — hardcode for dark hero (--text/--muted now dark, won't work on dark bg)
OLD_HMETA_SPAN = '  .hero-meta span { font-size: 13px; color: var(--muted); }'
NEW_HMETA_SPAN = '  .hero-meta span { font-size: 13px; color: #94a3b8; }'
assert OLD_HMETA_SPAN in html, 'MISSING: hero-meta span'
html = html.replace(OLD_HMETA_SPAN, NEW_HMETA_SPAN, 1)
changes.append('6. Hero meta span: hardcoded #94a3b8 (readable on dark hero)')

OLD_HMETA_DOT = '  .hero-meta span + span::before { content: "\\00B7"; padding: 0 12px; color: var(--border); }'
NEW_HMETA_DOT = '  .hero-meta span + span::before { content: "\\00B7"; padding: 0 12px; color: #475569; }'
assert OLD_HMETA_DOT in html, 'MISSING: hero-meta dot separator'
html = html.replace(OLD_HMETA_DOT, NEW_HMETA_DOT, 1)
changes.append('7. Hero meta dot: hardcoded #475569 separator on dark bg')

OLD_HMETA_B = '  .hero-meta span b { color: var(--text); font-weight: 600; }'
NEW_HMETA_B = '  .hero-meta span b { color: #f1f5f9; font-weight: 600; }'
assert OLD_HMETA_B in html, 'MISSING: hero-meta span b'
html = html.replace(OLD_HMETA_B, NEW_HMETA_B, 1)
changes.append('8. Hero meta b: hardcoded #f1f5f9 (bright on dark hero)')

# ══════════════════════════════════════════════════════════════════
# 9. STAT CARDS — add elevation + proper hover
# ══════════════════════════════════════════════════════════════════
OLD_CARD = ('  .stat-card { background: var(--surface); border: 1px solid var(--border);\n'
            '    border-radius: 8px; padding: 16px 18px; transition: border-color .15s; }\n'
            '  .stat-card:hover { border-color: #484f58; }')
NEW_CARD = ('  .stat-card { background: var(--surface); border: 1px solid var(--border);\n'
            '    border-radius: 8px; padding: 16px 18px; transition: border-color .15s, box-shadow .15s;\n'
            '    box-shadow: 0 1px 3px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.04); }\n'
            '  .stat-card:hover { border-color: var(--accent);\n'
            '    box-shadow: 0 4px 12px rgba(0,0,0,.08); }')
assert OLD_CARD in html, 'MISSING: stat-card + hover'
html = html.replace(OLD_CARD, NEW_CARD, 1)
changes.append('9. Stat cards: box-shadow added, hover uses accent border')

# 10. Controls focus ring — lower opacity for light bg
OLD_FOCUS1 = 'box-shadow: 0 0 0 3px rgba(88,166,255,.25); outline: none; }\n  .controls input { flex: 1'
NEW_FOCUS1 = 'box-shadow: 0 0 0 3px rgba(37,99,235,.15); outline: none; }\n  .controls input { flex: 1'
assert OLD_FOCUS1 in html, 'MISSING: controls focus ring'
html = html.replace(OLD_FOCUS1, NEW_FOCUS1, 1)
changes.append('10. Controls focus ring: rgba updated for light bg')

# 11. Score bar fill gradient
OLD_SCORE_BAR = 'background: linear-gradient(90deg, #1f6feb, #58a6ff);'
NEW_SCORE_BAR = 'background: linear-gradient(90deg, #1d4ed8, #2563eb);'
assert OLD_SCORE_BAR in html, 'MISSING: score-bar-fill gradient'
html = html.replace(OLD_SCORE_BAR, NEW_SCORE_BAR, 1)
changes.append('11. Score bar fill: gradient updated')

# ══════════════════════════════════════════════════════════════════
# 12. FLAG PILLS — richer light-mode palette (dark bg → white bg)
# ══════════════════════════════════════════════════════════════════
OLD_FLAGS_CSS = ('  .flag-def { background:#1f6feb22; color:#58a6ff; border:1px solid #1f6feb44; }\n'
                 '  .flag-off { background:#3fb95022; color:#3fb950; border:1px solid #3fb95044; }\n'
                 '  .flag-champ { background:#ffd70022; color:#ffd700; border:1px solid #ffd70044; }\n'
                 '  .flag-final { background:#bc8cff22; color:#bc8cff; border:1px solid #bc8cff44; }\n'
                 '  .flag-semi { background:#e3a83522; color:#e3a835; border:1px solid #e3a83544; }\n'
                 '  .flag-qf { background:#8b949e22; color:#8b949e; border:1px solid #8b949e44; }')
NEW_FLAGS_CSS = ('  .flag-def { background:#dbeafe; color:#1e40af; border:1px solid #bfdbfe; }\n'
                 '  .flag-off { background:#dcfce7; color:#15803d; border:1px solid #bbf7d0; }\n'
                 '  .flag-champ { background:#fef3c7; color:#92400e; border:1px solid #fde68a; }\n'
                 '  .flag-final { background:#ede9fe; color:#5b21b6; border:1px solid #ddd6fe; }\n'
                 '  .flag-semi { background:#ffedd5; color:#9a3412; border:1px solid #fed7aa; }\n'
                 '  .flag-qf { background:#f1f5f9; color:#475569; border:1px solid #e2e8f0; }')
assert OLD_FLAGS_CSS in html, 'MISSING: flag pill CSS'
html = html.replace(OLD_FLAGS_CSS, NEW_FLAGS_CSS, 1)
changes.append('12. Flag pills: semantic light-mode palette')

# 13. Hist pills — same palette treatment
OLD_HIST = ('  .hist-champ { background:#ffd70033; color:#ffd700; }\n'
            '  .hist-final { background:#bc8cff33; color:#bc8cff; }\n'
            '  .hist-semi { background:#e3a83533; color:#e3a835; }\n'
            '  .hist-qf { background:#8b949e33; color:#8b949e; }\n'
            '  .hist-none { color:#8b949e; font-size:11px; }')
NEW_HIST = ('  .hist-champ { background:#fef3c7; color:#92400e; }\n'
            '  .hist-final { background:#ede9fe; color:#5b21b6; }\n'
            '  .hist-semi { background:#ffedd5; color:#9a3412; }\n'
            '  .hist-qf { background:#f1f5f9; color:#475569; }\n'
            '  .hist-none { color:var(--muted); font-size:11px; }')
assert OLD_HIST in html, 'MISSING: hist-pill colors'
html = html.replace(OLD_HIST, NEW_HIST, 1)
changes.append('13. Hist pills: semantic light-mode palette')

# 14. Flag item metric-def — hardcoded #58a6ff → accent var
OLD_METRIC_DEF = '  .flag-item .metric-def { color: #58a6ff; }'
NEW_METRIC_DEF = '  .flag-item .metric-def { color: var(--accent); }'
assert OLD_METRIC_DEF in html, 'MISSING: metric-def color'
html = html.replace(OLD_METRIC_DEF, NEW_METRIC_DEF, 1)
changes.append('14. Flag item metric-def: #58a6ff → var(--accent)')

# 15. H2H picker focus ring
OLD_H2H_FOCUS = 'box-shadow: 0 0 0 3px rgba(88,166,255,.25); outline: none; }\n  .h2h-vs'
NEW_H2H_FOCUS = 'box-shadow: 0 0 0 3px rgba(37,99,235,.15); outline: none; }\n  .h2h-vs'
assert OLD_H2H_FOCUS in html, 'MISSING: h2h picker focus ring'
html = html.replace(OLD_H2H_FOCUS, NEW_H2H_FOCUS, 1)
changes.append('15. H2H picker focus ring: rgba updated')

# 16. H2H team header A tint
OLD_H2H_A = '  .h2h-team-header.a { background: #1f6feb22; color: var(--accent); border-right: 1px solid var(--border); }'
NEW_H2H_A = '  .h2h-team-header.a { background: #eff6ff; color: var(--accent); border-right: 1px solid var(--border); }'
assert OLD_H2H_A in html, 'MISSING: h2h-team-header.a'
html = html.replace(OLD_H2H_A, NEW_H2H_A, 1)
changes.append('16. H2H team header A: #1f6feb22 → #eff6ff')

# 17. H2H winner-a tint
OLD_WIN_A = '  .h2h-val.winner-a { background: #1f6feb11; }'
NEW_WIN_A = '  .h2h-val.winner-a { background: #eff6ff; }'
assert OLD_WIN_A in html, 'MISSING: winner-a tint'
html = html.replace(OLD_WIN_A, NEW_WIN_A, 1)
changes.append('17. H2H winner-a: tint → #eff6ff')

# 18. H2H winner-b tint (green tint needs light mode version too)
OLD_WIN_B = '  .h2h-val.winner-b { background: #3fb95011; }'
NEW_WIN_B = '  .h2h-val.winner-b { background: #f0fdf4; }'
assert OLD_WIN_B in html, 'MISSING: winner-b tint'
html = html.replace(OLD_WIN_B, NEW_WIN_B, 1)
changes.append('18. H2H winner-b: tint → #f0fdf4')

# 19. H2H sum-team tints
OLD_SUM_A = '  .h2h-sum-team.a { background: #1f6feb18; border-right: 1px solid var(--border); }'
NEW_SUM_A = '  .h2h-sum-team.a { background: #eff6ff; border-right: 1px solid var(--border); }'
assert OLD_SUM_A in html, 'MISSING: h2h-sum-team.a'
html = html.replace(OLD_SUM_A, NEW_SUM_A, 1)
changes.append('19. H2H sum-team A: #1f6feb18 → #eff6ff')

OLD_SUM_B = '  .h2h-sum-team.b { background: #3fb95018; text-align: right; }'
NEW_SUM_B = '  .h2h-sum-team.b { background: #f0fdf4; text-align: right; }'
assert OLD_SUM_B in html, 'MISSING: h2h-sum-team.b'
html = html.replace(OLD_SUM_B, NEW_SUM_B, 1)
changes.append('20. H2H sum-team B: #3fb95018 → #f0fdf4')

# 20. Prediction bar A gradient
OLD_PRED_A = '  .pred-bar-a { background: linear-gradient(90deg, #1f6feb, #58a6ff);'
NEW_PRED_A = '  .pred-bar-a { background: linear-gradient(90deg, #1d4ed8, #2563eb);'
assert OLD_PRED_A in html, 'MISSING: pred-bar-a gradient'
html = html.replace(OLD_PRED_A, NEW_PRED_A, 1)
changes.append('21. Prediction bar A: gradient updated')

# 21. Prediction bar D — surface2 barely visible on light bg, use border color
OLD_PRED_D = '  .pred-bar-d { background: var(--surface2); display: flex; align-items: center;'
NEW_PRED_D = '  .pred-bar-d { background: var(--border); display: flex; align-items: center;'
assert OLD_PRED_D in html, 'MISSING: pred-bar-d background'
html = html.replace(OLD_PRED_D, NEW_PRED_D, 1)
changes.append('22. Prediction bar D: surface2 → border (visible on light bg)')

# 22. GL tab active tint
OLD_GL_ACTIVE = '  .gl-tab.active { background:#58a6ff22; border-color:var(--accent); color:var(--accent); }'
NEW_GL_ACTIVE = '  .gl-tab.active { background:#dbeafe; border-color:var(--accent); color:var(--accent); }'
assert OLD_GL_ACTIVE in html, 'MISSING: gl-tab active'
html = html.replace(OLD_GL_ACTIVE, NEW_GL_ACTIVE, 1)
changes.append('23. GL tab active: #58a6ff22 → #dbeafe')

# 23. Defense section h3 inline style
OLD_DEF_H3 = '      <h3 style="color:#58a6ff">Elite Defense'
NEW_DEF_H3 = '      <h3 style="color:#1d4ed8">Elite Defense'
assert OLD_DEF_H3 in html, 'MISSING: defense h3 style'
html = html.replace(OLD_DEF_H3, NEW_DEF_H3, 1)
changes.append('24. Defense h3: #58a6ff → #1d4ed8 (visible on white)')

# 24. NQ badge text — white text on accent bg (accent is now dark blue)
OLD_NQ = 'background:var(--accent);color:#000;border-radius:3px'
NEW_NQ = 'background:var(--accent);color:#fff;border-radius:3px'
assert OLD_NQ in html, 'MISSING: NQ badge color'
html = html.replace(OLD_NQ, NEW_NQ, 1)
changes.append('25. NQ badge: color:#000 → color:#fff (dark accent needs white text)')

# 25. Table empty icon — border color (now #e2e8f0) nearly invisible on white
OLD_EMPTY_ICON = '  .table-empty-icon { font-size:2rem; margin-bottom:12px; color:var(--border); }'
NEW_EMPTY_ICON = '  .table-empty-icon { font-size:2rem; margin-bottom:12px; color:var(--muted); }'
assert OLD_EMPTY_ICON in html, 'MISSING: table-empty-icon'
html = html.replace(OLD_EMPTY_ICON, NEW_EMPTY_ICON, 1)
changes.append('26. Table empty icon: var(--border) → var(--muted)')

# ══════════════════════════════════════════════════════════════════
# 26. CARD ELEVATION — box shadows for light mode depth
# ══════════════════════════════════════════════════════════════════
OLD_TEAM_CARD = ('  .team-card { background: var(--surface); border: 1px solid var(--border);\n'
                 '    border-radius: 8px; padding: 18px 20px;\n'
                 '    transition: border-color .15s, transform .15s cubic-bezier(.16,1,.3,1); }\n'
                 '  .team-card:hover { border-color: var(--accent); transform: translateY(-2px); }')
NEW_TEAM_CARD = ('  .team-card { background: var(--surface); border: 1px solid var(--border);\n'
                 '    border-radius: 8px; padding: 18px 20px;\n'
                 '    box-shadow: 0 1px 3px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.04);\n'
                 '    transition: border-color .15s, transform .15s cubic-bezier(.16,1,.3,1), box-shadow .15s; }\n'
                 '  .team-card:hover { border-color: var(--accent); transform: translateY(-3px);\n'
                 '    box-shadow: 0 10px 24px rgba(0,0,0,.1), 0 4px 8px rgba(0,0,0,.06); }')
assert OLD_TEAM_CARD in html, 'MISSING: team-card'
html = html.replace(OLD_TEAM_CARD, NEW_TEAM_CARD, 1)
changes.append('27. Team cards: box-shadow elevation added')

# Flag panels + methodology section shadow
OLD_FLAG_PANEL = ('  .flag-panel { background: var(--surface); border: 1px solid var(--border);\n'
                  '    border-radius: 8px; padding: 16px 18px; }')
NEW_FLAG_PANEL = ('  .flag-panel { background: var(--surface); border: 1px solid var(--border);\n'
                  '    border-radius: 8px; padding: 16px 18px;\n'
                  '    box-shadow: 0 1px 3px rgba(0,0,0,.05); }')
assert OLD_FLAG_PANEL in html, 'MISSING: flag-panel'
html = html.replace(OLD_FLAG_PANEL, NEW_FLAG_PANEL, 1)
changes.append('28. Flag panels: box-shadow added')

OLD_METHOD = ('  .methodology { background: var(--surface); border: 1px solid var(--border);\n'
              '    border-radius: 8px; padding: 20px; margin-bottom: 24px; }')
NEW_METHOD = ('  .methodology { background: var(--surface); border: 1px solid var(--border);\n'
              '    border-radius: 8px; padding: 20px; margin-bottom: 24px;\n'
              '    box-shadow: 0 1px 3px rgba(0,0,0,.05); }')
assert OLD_METHOD in html, 'MISSING: methodology'
html = html.replace(OLD_METHOD, NEW_METHOD, 1)
changes.append('29. Methodology panel: box-shadow added')

# H2H form pill D — muted tint on light bg
OLD_FORM_D = '  .h2h-form-pill.D { background: #8b949e22; color: var(--muted); border: 1px solid #8b949e44; }'
NEW_FORM_D = '  .h2h-form-pill.D { background: #f1f5f9; color: var(--muted); border: 1px solid var(--border); }'
assert OLD_FORM_D in html, 'MISSING: h2h-form-pill.D'
html = html.replace(OLD_FORM_D, NEW_FORM_D, 1)
changes.append('30. H2H form pill D: muted tint updated for light bg')

with open('ecnl_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Light theme applied ({len(changes)} changes):')
for c in changes:
    print(' ', c)
print(f'\nFile size: {len(html)/1024:.1f}KB')
