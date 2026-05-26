"""Patch ecnl_dashboard.html with:
1. CONF_GAMES_MAP after TOURNAMENT_MAP
2. Quality-weighted Phase 2 showcase IIFE
3. Updated getTeamGameLog() using CONF_GAMES_MAP
4. Updated switchGLTab note
5. Updated methodology label for Showcase Form
6. Updated section-sub description
"""

with open('ecnl_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('conf_games_map_final.js', 'r', encoding='utf-8') as f:
    conf_map_js = f.read()

# ── 1. Insert CONF_GAMES_MAP + replace Phase 2 IIFE ──────────────────────────
OLD_PHASE2 = '''// ============================================================
// PHASE 2: SHOWCASE FORM — cross-conference win% vs qualified opponents
// Placed here (after H2H_MAP) to avoid JavaScript TDZ error
// ============================================================
(function() {
  const _qNames = new Set(RAW.map(r => r[0]));
  const _sfW = {}, _sfGP = {};
  RAW.forEach(r => { _sfW[r[0]] = 0; _sfGP[r[0]] = 0; });
  Object.entries(H2H_MAP).forEach(([key, games]) => {
    const [tA, tB] = key.split('|||');
    if (!_qNames.has(tA) || !_qNames.has(tB)) return;
    games.forEach(g => {
      if (!g.evt) return;
      _sfGP[tA]++; _sfGP[tB]++;
      if (g.hScore > g.aScore) { if (g.home===tA) _sfW[tA]++; else _sfW[tB]++; }
      else if (g.aScore > g.hScore) { if (g.away===tA) _sfW[tA]++; else _sfW[tB]++; }
      else { _sfW[tA]+=0.5; _sfW[tB]+=0.5; }
    });
  });
  teams.forEach(t => {
    t.showcaseWinPct = _sfGP[t.name] > 0 ? _sfW[t.name] / _sfGP[t.name] : null;
    t.showcaseGP = _sfGP[t.name] || 0;
  });
  const _swVals = teams.filter(t => t.showcaseWinPct !== null).map(t => t.showcaseWinPct);
  const _swMean = _swVals.length ? _swVals.reduce((s,v) => s+v, 0) / _swVals.length : 0.5;
  teams.forEach(t => { if (t.showcaseWinPct === null) t.showcaseWinPct = _swMean; });
  norm(teams, 'showcaseWinPct');
  teams.forEach(t => {
    t.score = Math.round(
      t._n_winPct          * 30 +
      t._n_gfpg            * 15 +
      t._n_gapg            * 15 +
      t._n_confStr         * 15 +
      t._n_playoffExp      * 10 +
      t._n_showcaseWinPct  * 20
    );
  });
  teams.sort((a,b) => b.score - a.score);
  teams.forEach((t, i) => t.rank = i + 1);
})();'''

NEW_PHASE2 = conf_map_js + '''

// ============================================================
// PHASE 2: SHOWCASE FORM — quality-weighted, all showcase GP counted
// Placed here (after H2H_MAP) to avoid JavaScript TDZ error.
// Denominator = ALL showcase games (including vs non-qualified teams).
// Numerator   = quality-weighted points for wins/draws vs qualified opponents.
// Quality weight = (66 - opponent_official_seed) / 66 so beating a top seed
// scores higher than beating the 54th seed.
// ============================================================
(function() {
  const _qNames = new Set(RAW.map(r => r[0]));
  const _seedMap = {};
  RAW.forEach(r => { _seedMap[r[0]] = r[1]; }); // name → official ECNL seed
  const SEED_MAX = 66; // 1 above max seed (65) so minimum quality > 0

  const _sfW = {}, _sfGP = {};
  RAW.forEach(r => { _sfW[r[0]] = 0; _sfGP[r[0]] = 0; });

  Object.entries(H2H_MAP).forEach(([key, games]) => {
    const [tA, tB] = key.split('|||');
    const aInField = _qNames.has(tA), bInField = _qNames.has(tB);
    if (!aInField && !bInField) return; // neither team in field

    games.forEach(g => {
      if (!g.evt) return; // showcase games only

      // Count ALL showcase GP for teams in our field (penalises non-qual games)
      if (aInField) _sfGP[tA]++;
      if (bInField) _sfGP[tB]++;

      // Quality credit only when BOTH teams are qualified
      if (!aInField || !bInField) return;

      const qA = Math.max(0, SEED_MAX - _seedMap[tB]) / SEED_MAX; // quality of A's result
      const qB = Math.max(0, SEED_MAX - _seedMap[tA]) / SEED_MAX; // quality of B's result
      const aHome = g.home === tA;
      const aScore = aHome ? g.hScore : g.aScore;
      const bScore = aHome ? g.aScore : g.hScore;

      if (aScore > bScore)      { _sfW[tA] += qA; }
      else if (bScore > aScore) { _sfW[tB] += qB; }
      else                      { _sfW[tA] += qA * 0.5; _sfW[tB] += qB * 0.5; }
    });
  });

  teams.forEach(t => {
    t.showcaseWinPct = _sfGP[t.name] > 0 ? _sfW[t.name] / _sfGP[t.name] : null;
    t.showcaseGP = _sfGP[t.name] || 0;
  });
  const _swVals = teams.filter(t => t.showcaseWinPct !== null).map(t => t.showcaseWinPct);
  const _swMean = _swVals.length ? _swVals.reduce((s,v) => s+v, 0) / _swVals.length : 0.5;
  teams.forEach(t => { if (t.showcaseWinPct === null) t.showcaseWinPct = _swMean; });
  norm(teams, 'showcaseWinPct');
  teams.forEach(t => {
    t.score = Math.round(
      t._n_winPct          * 30 +
      t._n_gfpg            * 15 +
      t._n_gapg            * 15 +
      t._n_confStr         * 15 +
      t._n_playoffExp      * 10 +
      t._n_showcaseWinPct  * 20
    );
  });
  teams.sort((a,b) => b.score - a.score);
  teams.forEach((t, i) => t.rank = i + 1);
})();'''

assert OLD_PHASE2 in html, "Phase 2 IIFE not found"
html = html.replace(OLD_PHASE2, NEW_PHASE2, 1)
print("✓ Phase 2 IIFE replaced + CONF_GAMES_MAP inserted")

# ── 2. Replace getTeamGameLog() ───────────────────────────────────────────────
OLD_GAMELOG = '''function getTeamGameLog(teamName) {
  const conf = [], showcase = [], tourn = [];
  for (const [key, games] of Object.entries(H2H_MAP)) {
    const [tA, tB] = key.split('|||');
    if (tA !== teamName && tB !== teamName) continue;
    games.forEach(g => {
      const isHome = g.home === teamName;
      const opponent = isHome ? g.away : g.home;
      const gf = isHome ? g.hScore : g.aScore;
      const ga = isHome ? g.aScore : g.hScore;
      const result = gf > ga ? 'W' : ga > gf ? 'L' : 'D';
      const entry = { date: g.date, opponent, isHome, gf, ga, result, source: g.conf || g.evt, isShowcase: !!g.evt };
      if (g.conf) conf.push(entry);
      else showcase.push(entry);
    });
  }
  for (const [key, games] of Object.entries(TOURNAMENT_MAP)) {
    const [tA, tB] = key.split('|||');
    if (tA !== teamName && tB !== teamName) continue;
    games.forEach(g => {
      const isHome = g.home === teamName;
      const opponent = isHome ? g.away : g.home;
      const gf = isHome ? g.hScore : g.aScore;
      const ga = isHome ? g.aScore : g.hScore;
      const result = gf > ga ? 'W' : ga > gf ? 'L' : 'D';
      tourn.push({ date: g.date, opponent, isHome, gf, ga, result, source: g.tourn, isShowcase: false, isTournament: true });
    });
  }
  const parseDate = s => {
    const d = new Date(s);
    return isNaN(d.getTime()) ? new Date(s.replace(/(\\w+)\\s+(\\d+),\\s+(\\d+)/, '$2 $1 $3')) : d;
  };
  const byDate = (a, b) => parseDate(a.date) - parseDate(b.date);
  return { conf: conf.sort(byDate), showcase: showcase.sort(byDate), tourn: tourn.sort(byDate) };
}'''

NEW_GAMELOG = r"""function getTeamGameLog(teamName) {
  const parseDate = s => {
    const d = new Date(s);
    return isNaN(d.getTime()) ? new Date(s.replace(/(\w+)\s+(\d+),\s+(\d+)/, '$2 $1 $3')) : d;
  };
  const byDate = (a, b) => parseDate(a.date) - parseDate(b.date);

  // Conference: use CONF_GAMES_MAP (full schedule) if available, else H2H_MAP fallback
  const conf = [];
  let confIsComplete = false;
  if (CONF_GAMES_MAP[teamName]) {
    confIsComplete = true;
    CONF_GAMES_MAP[teamName].forEach(g => {
      const gf = g.h ? g.hs : g.as;
      const ga = g.h ? g.as : g.hs;
      conf.push({ date: g.d, opponent: g.o, isHome: g.h, gf, ga, result: gf > ga ? 'W' : ga > gf ? 'L' : 'D', source: g.c });
    });
  } else {
    // Fallback: H2H_MAP conference games (qualified opponents only)
    for (const [key, games] of Object.entries(H2H_MAP)) {
      const [tA, tB] = key.split('|||');
      if (tA !== teamName && tB !== teamName) continue;
      games.forEach(g => {
        if (!g.conf) return;
        const isHome = g.home === teamName;
        const opponent = isHome ? g.away : g.home;
        const gf = isHome ? g.hScore : g.aScore;
        const ga = isHome ? g.aScore : g.hScore;
        conf.push({ date: g.date, opponent, isHome, gf, ga, result: gf > ga ? 'W' : ga > gf ? 'L' : 'D', source: g.conf });
      });
    }
  }

  // Showcase: from H2H_MAP (evt games only)
  const showcase = [];
  for (const [key, games] of Object.entries(H2H_MAP)) {
    const [tA, tB] = key.split('|||');
    if (tA !== teamName && tB !== teamName) continue;
    games.forEach(g => {
      if (!g.evt) return;
      const isHome = g.home === teamName;
      const opponent = isHome ? g.away : g.home;
      const gf = isHome ? g.hScore : g.aScore;
      const ga = isHome ? g.aScore : g.hScore;
      showcase.push({ date: g.date, opponent, isHome, gf, ga, result: gf > ga ? 'W' : ga > gf ? 'L' : 'D', source: g.evt, isShowcase: true });
    });
  }

  // Tournaments: from TOURNAMENT_MAP
  const tourn = [];
  for (const [key, games] of Object.entries(TOURNAMENT_MAP)) {
    const [tA, tB] = key.split('|||');
    if (tA !== teamName && tB !== teamName) continue;
    games.forEach(g => {
      const isHome = g.home === teamName;
      const opponent = isHome ? g.away : g.home;
      const gf = isHome ? g.hScore : g.aScore;
      const ga = isHome ? g.aScore : g.hScore;
      tourn.push({ date: g.date, opponent, isHome, gf, ga, result: gf > ga ? 'W' : ga > gf ? 'L' : 'D', source: g.tourn, isTournament: true });
    });
  }

  return {
    conf: conf.sort(byDate),
    showcase: showcase.sort(byDate),
    tourn: tourn.sort(byDate),
    confIsComplete
  };
}"""

assert OLD_GAMELOG in html, "getTeamGameLog not found"
html = html.replace(OLD_GAMELOG, NEW_GAMELOG, 1)
print("✓ getTeamGameLog() replaced")

# ── 3. Update switchGLTab conf note ──────────────────────────────────────────
OLD_NOTE = """  if (tab === 'conf') {
    note.textContent = '⚠ Conference results here only include games played against other nationally qualified teams. Each team\\'s full conference schedule includes additional opponents not captured in this dataset.';
    note.style.display = 'block';
  } else if (tab === 'tourn') {"""

NEW_NOTE = """  if (tab === 'conf') {
    if (_glData.confIsComplete) {
      note.style.display = 'none';
    } else {
      note.textContent = '⚠ Full conference schedule data is not yet available for this conference (Heartland, Mountain, New England, Northern Cal). Showing known games vs other nationally qualified teams only.';
      note.style.display = 'block';
    }
  } else if (tab === 'tourn') {"""

assert OLD_NOTE in html, "switchGLTab conf note not found"
html = html.replace(OLD_NOTE, NEW_NOTE, 1)
print("✓ switchGLTab conf note updated")

# ── 4. Update methodology Showcase Form label ─────────────────────────────────
OLD_METHOD = '      <div class="method-item"><div class="pct">20%</div><div class="label">Showcase Form — cross-conf win% vs qualified opponents</div></div>'
NEW_METHOD = '      <div class="method-item"><div class="pct">20%</div><div class="label">Showcase Form — quality-weighted cross-conf results (all showcase GP counted)</div></div>'

assert OLD_METHOD in html, "methodology Showcase label not found"
html = html.replace(OLD_METHOD, NEW_METHOD, 1)
print("✓ Methodology Showcase Form label updated")

# ── 5. Update section-sub description ────────────────────────────────────────
OLD_SUB = '  <div class="section-sub">Select any qualified team to view their game results — conference play (vs. qualified opponents) and all ECNL showcase events.</div>'
NEW_SUB = '  <div class="section-sub">Select any qualified team to view their full conference schedule and all ECNL showcase events. Conference data available for 10 of 15 conferences (Far West, Florida, Mid-America, Mid-Atlantic, North Atlantic, Northwest, Ohio Valley, Southeast, Southwest, Texas).</div>'

assert OLD_SUB in html, "section-sub not found"
html = html.replace(OLD_SUB, NEW_SUB, 1)
print("✓ Section-sub description updated")

with open('ecnl_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\nAll patches applied. File saved.")
print("New file size: %.0fKB" % (len(html) / 1024))
