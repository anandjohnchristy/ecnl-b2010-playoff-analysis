import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ecnl_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ══════════════════════════════════════════════════════════════════
# P4a: KEYBOARD SHORTCUT — / focuses search field
# ══════════════════════════════════════════════════════════════════

# 1. Update search placeholder to hint at the shortcut
OLD_PLACEHOLDER = '<input type="text" id="searchInput" placeholder="\U0001f50d  Search team name...">'
NEW_PLACEHOLDER = '<input type="text" id="searchInput" placeholder="Search team name..." title="Press / to focus">'
assert OLD_PLACEHOLDER in html, 'MISSING: searchInput placeholder'
html = html.replace(OLD_PLACEHOLDER, NEW_PLACEHOLDER, 1)
changes.append('1. Search placeholder: emoji removed, title hint added (Press / to focus)')

# 2. Add keyboard shortcut listener near other event listeners
OLD_LISTENERS = 'function resetFilters() {'
NEW_LISTENERS = ('// Keyboard shortcut: / to focus search (when not in a text field)\n'
                 'document.addEventListener(\'keydown\', e => {\n'
                 '  if (e.key === \'/\' && !\' INPUT SELECT TEXTAREA \'.includes(\' \' + document.activeElement.tagName + \' \')) {\n'
                 '    e.preventDefault();\n'
                 '    document.getElementById(\'searchInput\').focus();\n'
                 '  }\n'
                 '});\n'
                 '\n'
                 'function resetFilters() {')
assert OLD_LISTENERS in html, 'MISSING: resetFilters function'
html = html.replace(OLD_LISTENERS, NEW_LISTENERS, 1)
changes.append('2. Keyboard shortcut: / focuses search field')

# ══════════════════════════════════════════════════════════════════
# P4b: H2H PERMALINK — URL sync + Copy link button
# ══════════════════════════════════════════════════════════════════

# 3. Add CSS for share button
OLD_H2H_CSS = '  .h2h-picker label { display: block; font-size: 11px;\n    color: var(--muted); margin-bottom: 6px; font-weight: 600; }'
NEW_H2H_CSS = ('  .h2h-picker label { display: block; font-size: 11px;\n'
               '    color: var(--muted); margin-bottom: 6px; font-weight: 600; }\n'
               '  .h2h-share { display:none; align-items:center; gap:6px; margin-left:auto;\n'
               '    background:none; border:1px solid var(--border); color:var(--muted);\n'
               '    border-radius:8px; padding:8px 14px; font-size:12px; cursor:pointer;\n'
               '    font-weight:600; transition:color .15s, border-color .15s;\n'
               '    align-self:flex-end; white-space:nowrap; }\n'
               '  .h2h-share:hover { color:var(--accent); border-color:var(--accent); }\n'
               '  .h2h-share.visible { display:flex; }\n'
               '  .h2h-share.copied { color:var(--green); border-color:var(--green); }')
assert OLD_H2H_CSS in html, 'MISSING: h2h-picker label CSS'
html = html.replace(OLD_H2H_CSS, NEW_H2H_CSS, 1)
changes.append('3. h2h-share CSS added')

# 4. Add share button to h2h-pickers div (after last picker, inside the flex row)
OLD_PICKERS = ('  </div>\n'
               '\n'
               '  <div class="h2h-same-err" id="h2hSameTeamErr"')
NEW_PICKERS = ('  <button class="h2h-share" id="h2hShareBtn" onclick="copyH2HLink()"\n'
               '    title="Copy a shareable link to this matchup">\n'
               '    <svg width="13" height="13" viewBox="0 0 16 16" fill="none">'
               '<path d="M6 4H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-2M10 2h4m0 0v4m0-4-6 6"'
               ' stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'
               '</svg>\n'
               '    <span id="h2hShareLabel">Copy link</span>\n'
               '  </button>\n'
               '  </div>\n'
               '\n'
               '  <div class="h2h-same-err" id="h2hSameTeamErr"')
assert OLD_PICKERS in html, 'MISSING: h2h-pickers close / same-err'
html = html.replace(OLD_PICKERS, NEW_PICKERS, 1)
changes.append('4. Share button added inside h2h-pickers')

# 5. runH2H(): clear URL + hide share btn when no selection
OLD_NO_SEL = ('  if (!nameA || !nameB) {\n'
              '    content.style.display = \'none\';\n'
              '    sameErr.style.display = \'none\';\n'
              '    return;\n'
              '  }')
NEW_NO_SEL = ('  const shareBtn = document.getElementById(\'h2hShareBtn\');\n'
              '  if (!nameA || !nameB) {\n'
              '    content.style.display = \'none\';\n'
              '    sameErr.style.display = \'none\';\n'
              '    if (shareBtn) shareBtn.classList.remove(\'visible\');\n'
              '    history.replaceState(null, \'\', window.location.pathname);\n'
              '    return;\n'
              '  }')
assert OLD_NO_SEL in html, 'MISSING: runH2H no-selection guard'
html = html.replace(OLD_NO_SEL, NEW_NO_SEL, 1)
changes.append('5. runH2H: clears URL when no selection')

# 6. runH2H(): hide share btn on same-team error
OLD_SAME = ('  if (nameA === nameB) {\n'
            '    content.style.display = \'none\';\n'
            '    sameErr.style.display = \'flex\';\n'
            '    return;\n'
            '  }')
NEW_SAME = ('  if (nameA === nameB) {\n'
            '    content.style.display = \'none\';\n'
            '    sameErr.style.display = \'flex\';\n'
            '    if (shareBtn) shareBtn.classList.remove(\'visible\');\n'
            '    history.replaceState(null, \'\', window.location.pathname);\n'
            '    return;\n'
            '  }')
assert OLD_SAME in html, 'MISSING: runH2H same-team guard'
html = html.replace(OLD_SAME, NEW_SAME, 1)
changes.append('6. runH2H: clears URL on same-team error')

# 7. runH2H(): update URL + show share btn on valid pair (after sameErr hide)
OLD_AFTER_GUARD = ('  sameErr.style.display = \'none\';\n'
                   '\n'
                   '  const tA = teams.find(t => t.name === nameA);')
NEW_AFTER_GUARD = ('  sameErr.style.display = \'none\';\n'
                   '\n'
                   '  // Sync URL for permalink\n'
                   '  const params = new URLSearchParams();\n'
                   '  params.set(\'teamA\', nameA);\n'
                   '  params.set(\'teamB\', nameB);\n'
                   '  history.replaceState(null, \'\', \'?\' + params.toString());\n'
                   '  if (shareBtn) shareBtn.classList.add(\'visible\');\n'
                   '\n'
                   '  const tA = teams.find(t => t.name === nameA);')
assert OLD_AFTER_GUARD in html, 'MISSING: runH2H after guard'
html = html.replace(OLD_AFTER_GUARD, NEW_AFTER_GUARD, 1)
changes.append('7. runH2H: URL updated and share button shown on valid pair')

# 8. Add copyH2HLink() function
OLD_INIT = ('// ============================================================\n'
            '// INIT\n'
            '// ============================================================')
NEW_INIT = ('// ============================================================\n'
            '// H2H PERMALINK — copy button\n'
            '// ============================================================\n'
            'function copyH2HLink() {\n'
            '  const btn = document.getElementById(\'h2hShareBtn\');\n'
            '  const label = document.getElementById(\'h2hShareLabel\');\n'
            '  const url = window.location.href;\n'
            '  if (navigator.clipboard) {\n'
            '    navigator.clipboard.writeText(url).then(() => {\n'
            '      label.textContent = \'Copied!\';\n'
            '      btn.classList.add(\'copied\');\n'
            '      setTimeout(() => { label.textContent = \'Copy link\'; btn.classList.remove(\'copied\'); }, 2000);\n'
            '    });\n'
            '  } else {\n'
            '    const ta = document.createElement(\'textarea\');\n'
            '    ta.value = url; document.body.appendChild(ta); ta.select();\n'
            '    document.execCommand(\'copy\'); document.body.removeChild(ta);\n'
            '    label.textContent = \'Copied!\'; btn.classList.add(\'copied\');\n'
            '    setTimeout(() => { label.textContent = \'Copy link\'; btn.classList.remove(\'copied\'); }, 2000);\n'
            '  }\n'
            '}\n'
            '\n'
            '// ============================================================\n'
            '// INIT\n'
            '// ============================================================')
assert OLD_INIT in html, 'MISSING: INIT comment block'
html = html.replace(OLD_INIT, NEW_INIT, 1)
changes.append('8. copyH2HLink() function added')

# 9. On init: read URL params and restore H2H state
OLD_INIT_END = ('initH2HSelectors();\n'
                'initGameLogSelector();')
NEW_INIT_END = ('initH2HSelectors();\n'
                'initGameLogSelector();\n'
                '\n'
                '// Restore H2H from URL params (permalink support)\n'
                '(function() {\n'
                '  const p = new URLSearchParams(window.location.search);\n'
                '  const a = p.get(\'teamA\'), b = p.get(\'teamB\');\n'
                '  if (a && b) {\n'
                '    document.getElementById(\'h2hTeamA\').value = a;\n'
                '    document.getElementById(\'h2hTeamB\').value = b;\n'
                '    runH2H();\n'
                '    document.getElementById(\'h2hSection\') &&\n'
                '      document.getElementById(\'h2hSection\').scrollIntoView({ behavior: \'smooth\', block: \'start\' });\n'
                '  }\n'
                '})();')
assert OLD_INIT_END in html, 'MISSING: initH2HSelectors / initGameLogSelector'
html = html.replace(OLD_INIT_END, NEW_INIT_END, 1)
changes.append('9. Init: URL params restore H2H state on page load')

with open('ecnl_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'P4 fixes applied ({len(changes)} changes):')
for c in changes:
    print(' ', c)
print(f'\nFile size: {len(html)/1024:.1f}KB')
