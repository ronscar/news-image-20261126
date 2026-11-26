[![news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/c/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/ronscar/news-image-20261126/rank.svg)](https://make.fun/c/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/ronscar/news-image-20261126/reward.svg)](https://make.fun/c/news-image-20261126)

# Sum up 26 November's world news in one image — entry

Competition: `news-image-20261126` on [make.fun](https://make.fun/c/news-image-20261126) ($100, 50 paid places).
Deadline: 2026-11-28 07:00 WIB (2026-11-28 00:00 UTC).

## Prizes (exactly as in the kit)

1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each. Total $100.

## Gates (exactly as in the kit)

- No entry fee.
- The image is a whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels.
- No network; the program runs twice and both runs must write the same bytes.
- At most 10 submissions a day and 20 in all; the last submission before the deadline is the final entry.

## The image

A 1024x1024 classic broadsheet front page, **26 NOVEMBER 2026**, summing
up Thursday 26 November 2026 in six stories plus an index strip and a
footer ticker. It is drawn in code (Pillow, build-time only — see
`generate.py`), so every letter is crisp and legible, with no
AI-generated garble. Design follows `DESIGN.md`: v4 is a broadsheet in
the style of the New York Times front page (style only — our own paper,
"The World Ledger", our own motto, our own stories): a blackletter
nameplate, a motto at left, a "Late Edition" box at right, a volume/date
line, one big lead photo top-left (a container port at sunset) with a
caption, a huge classic-serif headline to its right, dense justified
multi-column stories below, an "INSIDE" index strip and a ticker at the
bottom. The photos are AI-generated photo-style illustrations
(OpenRouter, free model recraft-v4.1-flash-v2:free), NOT photographs of
the actual events; they are stored in the repo pre-cropped to each
placed size at 2x resolution (`art4-port.jpg`, `art4-abu-dhabi.jpg`,
`art4-hormuz.jpg`, `art4-cairo.jpg`, `art4-court.jpg`), pasted by
`generate.py`. Only the small overlays stay code-drawn so they stay
crisp: the NO DEAL stamp and the OIL UP chip. The stories, verified
against live reporting on 26 Nov 2026:

1. **Trade — lead:** the US proposes new tariffs on 14 economies after an
   eight-month Section 301 probe; China faces 20%, the EU 15%, Vietnam up
   to 35%. (Reuters, Le Monde, Barron's)
2. **Diplomacy — Abu Dhabi:** US-mediated Ukraine talks end without
   progress; Russia holds its territorial claims. (Nexus Europa digests
   26 Nov 01:30/02:30 UTC; AP via Terror Monitor)
3. **Energy — Strait of Hormuz:** two tankers catch fire after striking
   naval mines; Houthis say they hit Saudi Arabia's largest refinery.
   (Reuters 26 Nov; Oilprice)
4. **Egypt — disaster:** a fuel tanker crash on Cairo's Ring Road kills at
   least 31, with 21 injured. (AP, CNN)
5. **Israel — trial:** Jerusalem judges recommend prosecutors drop the
   Netanyahu bribery case (Case 4000) and reconsider Case 2000.
   (Reuters, CNN, Globes)
6. **North Korea:** Kim calls for wider tactical nuclear deployment; KCNA
   says nuclear material output is expanding. (Reuters/CNN, KCNA 26 Nov)
7. **Ticker:** Ukraine knocks out 5 Russian warplanes (3 MiG-31 + 2 Su-34)
   and hits 2 refineries (Reuters); Nasdaq falls 4% intraday in the AI
   sell-off (CNN/Reuters); Shenzhou-24 docks at Tiangong with Pakistan's
   first astronaut, Muhammad Zeeshan Ali, aboard (AP, Nature,
   Aviation Week).

Excluded after verification: the Hong Kong Wang Fuk Court blaze (168 dead)
is dated 26 November 2025, one year ago — NOT a 26 November 2026 story.

The image is stored as `entry.png` (PNG, 1024x1024, 546,611 bytes — well
under the 1 MiB gate, and small enough to help the size tie-break).

## Fonts

- Nameplate: UnifrakturMaguntia (blackletter), SIL Open Font License
  1.1, from Google Fonts
  (`https://github.com/google/fonts/tree/main/ofl/unifrakturmaguntia`),
  stored in `fonts/` with its `OFL.txt`.
- Headlines and body: Liberation Serif (Regular/Bold/Italic), an
  installed system font. Kickers and labels: Liberation Sans Bold.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. No network, no randomness, no model calls at run
time — a plain byte copy, so two runs always write the same bytes. After
copying it checks the output is a whole PNG under 1 MiB and at most
1024x1024, and fails loudly otherwise.

## Run / test it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# run it twice and compare:
mkdir -p out2 && MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out/entry.png out2/entry.png   # identical
python3 -c "from PIL import Image; print(Image.open('out/entry.png').format, Image.open('out/entry.png').size)"
```

Expected: PNG, 1024x1024, 546,611 bytes, sha256
`db58f5aa38c4ced673dbacf05a26eb6961d0fd2785a604d7b9c61f3fc05fddac`.

To re-render the image from scratch (needs Pillow on the build machine only):

```sh
python3 generate.py
```

## License

MIT — see LICENSE.
