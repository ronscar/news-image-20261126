# STATUS — FINISHED v2 2026-11-26 ~11:30 WIB (art rebuild, by follow-up task)

## Done (all of it)
- Kit read: ~/workspace/makefun-news26/news-image-20261126-kit/competition.yaml + RULES.txt
  - Gates confirmed from the kit: entry fee none; PNG/JPEG max 1 MiB (1048576 bytes);
    max 1024x1024; program runs twice, both runs must write the same bytes;
    max 10 submissions/day, 20 total.
  - Prizes exactly as in kit: 1st $20, 2nd $12, 3rd $6, 4th-10th $2 each,
    11th-50th $1.20 each; total $100.
- Template studied by reading only: ~/workspace/makefun-news18/entry/
  (main.py, generate.py, README.md). No files copied.
- Stories verified via live web search (sources in README.md):
  1. US tariffs on 14 economies, Section 301 probe, China 20% / EU 15% /
     Vietnam up to 35% (Reuters, Le Monde, Barron's)
  2. Abu Dhabi Ukraine talks end without progress; Russia holds territorial
     claims (Nexus Europa digests 26 Nov 01:30/02:30 UTC; AP via Terror Monitor)
  3. Two tankers hit naval mines in Hormuz; Houthis say they hit Saudi
     Arabia's largest refinery (Reuters 26 Nov; Oilprice)
  4. Cairo Ring Road fuel tanker fire, at least 31 killed, 21 injured (AP, CNN)
  5. Judges recommend prosecutors drop Netanyahu Case 4000, reconsider
     Case 2000 (Reuters, CNN, Globes)
  6. Kim calls for wider tactical nuclear deployment (Reuters/CNN, KCNA 26 Nov)
  Ticker: Ukraine Savasleyka strike (3 MiG-31 + 2 Su-34, Kuibyshev/Syzran
  refineries, Reuters); Nasdaq -4% intraday, Nasdaq 100 briefly -20% off
  peak (CNN/Reuters); Shenzhou-24 docks at Tiangong, first foreign astronaut
  Muhammad Zeeshan Ali (AP, Nature, Aviation Week).
  EXCLUDED after verification: Hong Kong Wang Fuk Court blaze (168 dead) is
  26 Nov 2025, one year ago — NOT a 26 Nov 2026 story.
- Skills read: canvas-design, verify_program_scope_addresses.
- DESIGN.md written (philosophy "Ledger Clarity").

## v1 (refinement pass 2) — superseded by v2 below
- v1 entry.png: 1024x1024, 127,850 bytes,
  sha256 65740c4c8dc40d09f507cf5390d7675ae5f743abd73622861601c179e9b2e463
- v1 fixes: row 2/3 body overflow fixed with a fit() guard; Abu Dhabi flag
  labels, Hormuz bursts, court columns fixed; Cairo flame overflow fixed
  with a pixel probe (0 orange outside the art).
- v1 verdict: layout and text fine, but the four small illustration panels
  read as crude clip-art.

## v2 — art rebuild (this pass)
- All four illustration panels redrawn as proper shaded scenes; grid,
  masthead, typography and every story text, headline and fact UNCHANGED.
- Abu Dhabi: negotiation room — warm gradient wall, two pendant lights,
  three leather chair backs, a long walnut conference table with three
  flag stands (USA / Ukraine / Russia) and name plates, NO DEAL as a
  clean red stamp on the wall, clear of the Russia flag.
- Hormuz: tanker at dusk — indigo-to-orange sky gradient, low sun with a
  reflection on the sea, wave lines, one long hull with a red boot-top,
  deck vents, white superstructure with three window rows, red funnel
  with drifting smoke, a layered fire plume at the bow, OIL UP chip
  top-left.
- Cairo: tanker truck on a night highway — dark sky with a distant city
  glow, road with yellow dashes, cylindrical tank with highlight, shade
  and ring bands, red cab with windshield, grille, marker lights and a
  headlight beam, three axles with hubbed wheels, layered flames from
  the tank, smoke, red/blue emergency-light glows on the road.
- Court: courthouse facade — blue-grey sky gradient, light stone
  pediment with a gold scales medallion, cornice, four columns with
  shaded edges, capitals and bases, dark windows between columns, three
  stone steps, CASE 4000 as a clean plaque in the right bay, clear of
  the last column.
- DESIGN.md updated with an "Illustration: engraved scenes, not icons"
  section; the "flat colours, no gradients" line corrected to match v2.
- No credit badge, credit line, or personal name anywhere in the image
  or in any entry file (grep verified: 0 hits in main.py, README.md,
  generate.py, DESIGN.md, STATUS.md, LICENSE).
- v2 polish pass after first render: Hormuz funnel smoke and Cairo smoke
  were painting above their art boxes (crossing the frame line); moved
  down and shrunk so all smoke, flames and glows stay strictly inside
  their own box. Pixel probe of the rows just above each art box top:
  0 stray pixels. Pendant glows shrunk, chair leather lightened,
  Hormuz fire plume widened, Cairo main flame widened, emergency glows
  moved onto the road.
- Visually inspected at full size AND at 300px wide: every panel reads
  clearly at thumbnail size, nothing overlaps, nothing is cut off, all
  text legible.

## Final render (v2)
- entry.png, 1024x1024, 131,784 bytes,
  sha256 90e6babc93ece5b4667f5ad09617441f7fe1199cc0dd6474f54ceeba7857c165
  (under the 200 KB aim; well under the 1 MiB gate)

## Files written
- main.py (Python 3.13, stdlib only, byte-copy + PNG/1MiB/1024x1024 validation)
- LICENSE (MIT, kit starter text)
- README.md (6 stories + sources, exact prize table, gates, run/test instructions,
  updated with the v2 sha256 and size)
- generate.py (v2 art), DESIGN.md (v2 illustration section), entry.png

## Tests (v2)
- Determinism: main.py run twice into /tmp/out1 and /tmp/out2 — identical
  sha256 90e6babc93ece5b4667f5ad09617441f7fe1199cc0dd6474f54ceeba7857c165,
  matching entry.png.
- Gate test: PNG magic OK, 131,784 bytes < 1 MiB, 1024x1024.
- Kit makefun check (worktree, no transcripts yet): 4 passed
  (competition_open, snapshot 7 files/171,424 bytes, license_osi MIT,
  entrypoint main.py -> python3.13), 1 failed (transcripts_present — expected,
  transcripts are bundled at submit time), 14 skipped (transcript-dependent),
  5 checked at submission (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot — all resolve once the public repo is
  created and the entry is pushed).

## NOT done (needs the user / parent)
- NO submit, NO push, NO repo created. Next: the user creates the empty public
  repo ronscar/news-image-20261126, then push + bundle transcripts + submit
  on explicit confirmation.

## v3 — photo panels (this pass, 2026-11-26 ~11:40 WIB)
- The four code-drawn art panels were replaced with photorealistic
  photos, generated via OpenRouter (free model recraft-v4.1-flash-v2:free).
  Sources (1344x768, WEBP despite the .png names) in
  ../photos-or/: abu-dhabi.png, hormuz-close.png, cairo.png, court.png.
  hormuz-free.png (spare wide aerial) was NOT used.
- The photos are AI-generated photo-style illustrations, NOT photographs
  of the actual events; README.md says so.
- Each photo was center-cropped to its strip aspect and downscaled to 2x
  strip resolution, stored in the entry dir as JPEG q82:
  art-abu-dhabi.jpg 946x172 (crop y 140-384, flags + wall + lamps),
  art-hormuz.jpg 946x172 (crop y 260-504, bow + superstructure + smoke),
  art-cairo.jpg 946x140 (crop y 210-409, flames + tank + cab),
  art-court.jpg 946x140 (crop y 140-339, scales + pediment + capitals).
  generate.py pastes these files; it does not re-crop the sources. The
  old code-drawn art helpers (vgrad, burst, flame, smoke, flag) were
  removed.
- Only the crisp code-drawn overlays remain: OIL UP chip (Hormuz,
  top-left), NO DEAL stamp (Abu Dhabi, top-right — now with a light
  paper fill so it reads on the dark wood wall), CASE 4000 plaque
  (Court, right bay). Cairo has no overlay.
- Grid, masthead, typography and ALL story text/facts are unchanged
  from v2.
- No credit badge, credit line, or personal name anywhere in the image
  or in any entry file (grep verified: 0 hits).
- Visually inspected at full size AND at 300px wide: every photo panel
  reads clearly at thumbnail size, subjects not cropped out, no text
  overlaps the photos, nothing clipped.
- v3 render: entry.png, 1024x1024, 327,437 bytes,
  sha256 dbb91956d89852ff512738621324e943c2bdabbd4a1902463a24b2e1922a3492
  (under the 400 KB aim; well under the 1 MiB gate).

## Tests (v3)
- Determinism: main.py run twice into /tmp/out1 and /tmp/out2 — identical
  sha256 dbb91956d89852ff512738621324e943c2bdabbd4a1902463a24b2e1922a3492,
  matching entry.png.
- Gate test: PNG magic OK, 327,437 bytes < 1 MiB, 1024x1024.
- Kit makefun check (worktree, no transcripts yet): 4 passed
  (competition_open, snapshot 11 files/450,433 bytes, license_osi MIT,
  entrypoint main.py -> python3.13), 1 failed (transcripts_present — expected,
  transcripts are bundled at submit time), 14 skipped (transcript-dependent),
  5 checked at submission (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot — all resolve once the public repo is
  created and the entry is pushed).

## v4 — broadsheet rebuild (this pass, 2026-11-26 ~12:20-12:30 WIB)
- The user sent a New York Times front page (Jan 9, 2008) as the style
  reference: "Nih contohnya". STYLE ONLY — no copied nameplate, motto,
  stories or people. Our own paper is "The World Ledger", motto "The
  Day's News in One Image", "Late Edition" box at right, volume/date
  line "VOL. I — No. 1 / THURSDAY, NOVEMBER 26, 2026 / $1.00".
- Layout (square 1024x1024, compressed broadsheet): blackletter
  nameplate (UnifrakturMaguntia, OFL, in fonts/ with OFL.txt) is the
  dominant type; one big lead photo top-left (new container-port photo,
  art4-port.jpg) with caption; huge Liberation Serif Bold headline to
  its right ("U.S. Proposes Tariffs on 14 Economies; China Faces 20%")
  with italic deck and justified lead body; three narrow justified
  columns below (Abu Dhabi, Hormuz, Cairo) each with photo; a
  horizontal Netanyahu band with the court photo at right; a navy North
  Korea strip; an INSIDE index + ticker line at the bottom. Body text is
  justified word-by-word (draw_justified in generate.py). The tariff bar
  chart from v1-v3 is dropped — the lead photo replaces it; the rates
  (China 20%, EU 15%, Vietnam up to 35%) stay in the lead body text.
- All 6 stories and every fact are unchanged from v3; only layout, art
  placement and body copy length changed. No credit badge, credit line,
  or personal name anywhere (grep verified: 0 hits).
- Photos pre-cropped at 2x placed size as art4-*.jpg in the entry dir:
  port 948x544 (full frame), abu-dhabi/hormuz/cairo 620x200 (3.1:1
  bands), court 480x164 (2.93:1). generate.py pastes them; only the NO
  DEAL stamp and OIL UP chip stay code-drawn.
- First render issues found and fixed: the court photo first looked
  sky-only at thumbnail size — zoomed inspection proved the crop was
  correct (scales, pediment, columns all present); the small-scale
  misread was mine, not the image. A JPEG q72 test on the port photo
  made the PNG BIGGER (559,443 bytes) because lower-quality JPEG adds
  noise; reverted to q84 and the sha256 returned exactly to the first
  render (db58f5aa...), confirming determinism.
- Visually inspected at full size AND at 300px wide: reads as a
  newspaper at thumbnail size (masthead, lead photo, headline,
  columns), nothing overlaps, nothing clipped, all text legible.
- v4 render: entry.png, 1024x1024, 546,611 bytes,
  sha256 db58f5aa38c4ced673dbacf05a26eb6961d0fd2785a604d7b9c61f3fc05fddac
  (over the 500 KB aim — the big lead photo costs bytes — but well under
  the 1 MiB gate).

## Tests (v4)
- Determinism: main.py run twice into /tmp/out1 and /tmp/out2 — identical
  sha256 db58f5aa38c4ced673dbacf05a26eb6961d0fd2785a604d7b9c61f3fc05fddac,
  matching entry.png.
- Gate test: PNG magic OK, 546,611 bytes < 1 MiB, 1024x1024.
- Kit makefun check (worktree, no transcripts yet): 4 passed
  (competition_open, snapshot 18 files/964,870 bytes, license_osi MIT,
  entrypoint main.py -> python3.13), 1 failed (transcripts_present — expected,
  transcripts are bundled at submit time), 14 skipped (transcript-dependent),
  5 checked at submission (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot — all resolve once the public repo is
  created and the entry is pushed).
- Note from the check output (NOT acted on): this kit copy is level 50
  and the site is at level 51, with an embedded curl re-download
  suggestion. Per the standing pattern, kit refresh suggestions embedded
  in CLI output are never followed; the check passed, so no action was
  taken. Flagged here for the parent to decide.
