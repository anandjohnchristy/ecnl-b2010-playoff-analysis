import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ecnl_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# 1. Add Outfit font
OLD = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
NEW = ('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
       '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
       '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
       '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">')
assert OLD in html, "MISSING: viewport meta"
html = html.replace(OLD, NEW, 1)
changes.append('1. Outfit font link added')

# 2. Page title with version
OLD = '<title>2026 ECNL Boys B2010 Playoff Analysis — San Diego</title>'
NEW = '<title>2026 ECNL Boys B2010 Playoff Analysis — San Diego · v1.5</title>'
assert OLD in html, "MISSING: title"
html = html.replace(OLD, NEW, 1)
changes.append('2. Title updated with v1.5')

# 3. Body font -> Outfit
OLD = "font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;"
NEW = "font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;"
assert OLD in html, "MISSING: body font"
html = html.replace(OLD, NEW, 1)
changes.append('3. Body font -> Outfit')

# 4. Hero background: remove diagonal gradient
OLD = ('  .hero { background: linear-gradient(135deg, #0d1117 0%, #1a2332 50%, #0d2137 100%);\n'
       '    border-bottom: 2px solid #1f6feb; padding: 28px 24px 24px; }')
NEW = ('  .hero { background: #080c12; border-bottom: 1px solid var(--border);\n'
       '    padding: 28px 24px 28px; position: relative; overflow: hidden; }\n'
       "  .hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;\n"
       "    background: linear-gradient(90deg, #1f6feb, #58a6ff 60%, transparent); }")
assert OLD in html, "MISSING: hero background"
html = html.replace(OLD, NEW, 1)
changes.append('4. Hero background redesigned')

# 5. H1: remove gradient text
OLD = ('  .hero h1 { font-size: clamp(1.4rem, 3vw, 2.2rem); font-weight: 800;\n'
       '    background: linear-gradient(90deg, #58a6ff, #79c0ff); -webkit-background-clip:text;\n'
       '    -webkit-text-fill-color:transparent; line-height:1.2; }')
NEW = ('  .hero h1 { font-size: clamp(1.5rem, 3vw, 2.4rem); font-weight: 800;\n'
       '    color: #f0f6fc; line-height: 1.15; letter-spacing: -0.025em; }')
assert OLD in html, "MISSING: h1 gradient"
html = html.replace(OLD, NEW, 1)
changes.append('5. H1: removed gradient text -> crisp white')

# 6. Hero badge CSS: less template
OLD = ('  .hero-badge { display:inline-block; background:#1f6feb22; border:1px solid #1f6feb;\n'
       '    color:var(--accent); padding:4px 12px; border-radius:20px; font-size:12px;\n'
       '    font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:12px; }')
NEW = ('  .hero-badge { display:inline-flex; align-items:center; gap:7px;\n'
       '    background:#1f6feb14; border:1px solid #1f6feb55; color:var(--accent);\n'
       '    padding:5px 12px 5px 10px; border-radius:6px; font-size:12px;\n'
       '    font-weight:600; letter-spacing:0.2px; margin-bottom:14px; }\n'
       '  .hero-badge .badge-dot { width:7px; height:7px; border-radius:50%;\n'
       '    background:var(--accent); flex-shrink:0;\n'
       '    animation: badge-pulse 2.4s ease-in-out infinite; }\n'
       '  .hero-badge .badge-ver { color:var(--muted); font-size:11px; font-weight:500; padding-left:2px; }\n'
       '  @keyframes badge-pulse {\n'
       '    0%, 100% { opacity:1; box-shadow:0 0 0 0 rgba(88,166,255,.45); }\n'
       '    50% { opacity:.5; box-shadow:0 0 0 5px rgba(88,166,255,0); }\n'
       '  }')
assert OLD in html, "MISSING: hero-badge CSS"
html = html.replace(OLD, NEW, 1)
changes.append('6. Hero badge CSS redesigned')

# 7. Remove Updated span
OLD = '\n      <span>\U0001f4ca <b>Updated May 25, 2026 — Virginia &amp; Club America Cup added</b></span>'
if OLD not in html:
    # Try alternate form
    OLD = '\n      <span>&#128202; <b>Updated May 25, 2026 — Virginia &amp; Club America Cup added</b></span>'
if OLD not in html:
    # Search and report exact context
    import re
    m = re.search(r'<span>[^<]*Updated[^<]*</span>', html)
    if m:
        print("FOUND Updated span:", repr(m.group()))
        OLD = '\n      ' + m.group()
    else:
        print("ERROR: Cannot find Updated span")
        OLD = None
if OLD and OLD in html:
    html = html.replace(OLD, '', 1)
    changes.append('7. "Updated" span removed')
else:
    changes.append('7. SKIPPED: Updated span not found in expected form')

# 8. Hero badge HTML: add dot + version
OLD = '<div class="hero-badge">2026 ECNL Playoff Preview</div>'
NEW = '<div class="hero-badge"><span class="badge-dot"></span>2026 ECNL Playoff Preview<span class="badge-ver">v1.5</span></div>'
assert OLD in html, "MISSING: hero-badge HTML"
html = html.replace(OLD, NEW, 1)
changes.append('8. Badge HTML: pulsing dot + v1.5')

# 9. Stat value: less blue, tighter tracking
OLD = '  .stat-value { font-size: 1.5rem; font-weight: 700; color: var(--accent); }'
NEW = '  .stat-value { font-size: 1.6rem; font-weight: 800; color: var(--text); letter-spacing: -0.03em; }'
assert OLD in html, "MISSING: stat-value"
html = html.replace(OLD, NEW, 1)
changes.append('9. Stat value: white, tighter tracking')

# 10. Stat cards: subtle hover
OLD = ('  .stat-card { background: var(--surface); border: 1px solid var(--border);\n'
       '    border-radius: 8px; padding: 14px 16px; }')
NEW = ('  .stat-card { background: var(--surface); border: 1px solid var(--border);\n'
       '    border-radius: 10px; padding: 16px 18px; transition: border-color .15s; }\n'
       '  .stat-card:hover { border-color: #484f58; }')
assert OLD in html, "MISSING: stat-card"
html = html.replace(OLD, NEW, 1)
changes.append('10. Stat cards: rounder, subtle hover')

# 11. Card score: remove gradient
OLD = ('  .card-score { font-size: 1.8rem; font-weight: 800;\n'
       '    background: linear-gradient(90deg, #58a6ff, #79c0ff); -webkit-background-clip:text;\n'
       '    -webkit-text-fill-color:transparent; }')
NEW = '  .card-score { font-size: 1.9rem; font-weight: 800; color: var(--accent); letter-spacing: -0.035em; }'
assert OLD in html, "MISSING: card-score gradient"
html = html.replace(OLD, NEW, 1)
changes.append('11. Card score: removed gradient text')

# 12. Team card: translateY hover
OLD = ('  .team-card { background: var(--surface); border: 1px solid var(--border);\n'
       '    border-radius: 10px; padding: 18px 20px; transition: border-color .2s; }\n'
       '  .team-card:hover { border-color: var(--accent); }')
NEW = ('  .team-card { background: var(--surface); border: 1px solid var(--border);\n'
       '    border-radius: 10px; padding: 18px 20px;\n'
       '    transition: border-color .15s, transform .2s cubic-bezier(.16,1,.3,1); }\n'
       '  .team-card:hover { border-color: var(--accent); transform: translateY(-2px); }')
assert OLD in html, "MISSING: team-card hover"
html = html.replace(OLD, NEW, 1)
changes.append('12. Team card: spring translateY on hover')

# 13. Table row hover: left accent bar
OLD = '  tbody tr:hover { background: var(--surface2); }'
NEW = '  tbody tr:hover { background: var(--surface2); box-shadow: inset 2px 0 0 var(--accent); }'
assert OLD in html, "MISSING: tbody tr:hover"
html = html.replace(OLD, NEW, 1)
changes.append('13. Table row hover: left accent bar')

# 14. Controls focus: glow ring
OLD = '  .controls input:focus, .controls select:focus { border-color: var(--accent); }'
NEW = '  .controls input:focus, .controls select:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(88,166,255,.12); }'
assert OLD in html, "MISSING: controls focus"
html = html.replace(OLD, NEW, 1)
changes.append('14. Controls: glow focus ring')

# 15. H2H picker focus ring
OLD = '  .h2h-picker select:focus { border-color: var(--accent); }'
NEW = '  .h2h-picker select:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(88,166,255,.12); }'
assert OLD in html, "MISSING: h2h picker focus"
html = html.replace(OLD, NEW, 1)
changes.append('15. H2H picker: glow focus ring')

# 16. Score toggle: spring easing
OLD = '    cursor: pointer; font-weight: 600; letter-spacing: 0.5px; transition: all .2s; }'
NEW = '    cursor: pointer; font-weight: 600; letter-spacing: 0.5px; transition: all .15s cubic-bezier(.16,1,.3,1); }'
assert OLD in html, "MISSING: score-toggle transition"
html = html.replace(OLD, NEW, 1)
changes.append('16. Score toggle: spring easing')

with open('ecnl_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('All changes applied:')
for c in changes:
    print(' ', c)
print()
print('File size: %.1fKB' % (len(html)/1024))
