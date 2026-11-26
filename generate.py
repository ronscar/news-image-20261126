"""Build-time renderer for the news-image-20261126 entry (NOT run by the grader).

Renders entry.png: a 1024x1024 newspaper front page summing up Thursday
26 November 2026, drawn with Pillow on this machine only. The submitted
program (main.py, standard library only) just copies the rendered file.

v4: a classic broadsheet front page in the style of the New York Times
front page the user sent as reference (STYLE ONLY — no copied nameplate,
motto, stories or people). Our own paper, "The World Ledger", with a
blackletter nameplate (UnifrakturMaguntia, OFL, in fonts/), a motto at
left, a "Late Edition" box at right, a volume/date line, one big lead
photo top-left (the container port) with a caption, a huge classic-serif
headline to its right, dense justified multi-column stories below, an
"INSIDE" index strip and a one-line ticker at the bottom. Classic serif
throughout is Liberation Serif (installed system font); kickers and
labels are Liberation Sans Bold. The square canvas forces a compressed
broadsheet: the lead photo is 474px wide, the middle stories run in
three narrow columns, and the Netanyahu story is a horizontal band.

Photos are AI-generated photo-style illustrations (OpenRouter, free
model recraft-v4.1-flash-v2:free), NOT photographs of the actual events;
they are stored in the repo pre-cropped to each placed size at 2x
resolution (art4-*.jpg), pasted by generate.py. Only the small overlays
stay code-drawn so they stay crisp: the NO DEAL stamp, the OIL UP chip.
Grid, stories and all facts are unchanged from v3.

Stories verified against live reporting on 26 Nov 2026 (see README.md):
  1. Trade (lead): US proposes new tariffs on 14 economies after an
     eight-month Section 301 probe; China 20%, EU 15%, Vietnam up to 35%.
  2. Diplomacy: US-mediated Ukraine talks in Abu Dhabi end without
     progress; Russia holds its territorial claims.
  3. Energy: two tankers catch fire after striking naval mines in the
     Strait of Hormuz; Houthis say they hit Saudi Arabia's largest refinery.
  4. Egypt: fuel tanker crash on Cairo's Ring Road kills at least 31.
  5. Israel: judges recommend prosecutors drop the Netanyahu bribery case.
  6. North Korea: Kim calls for wider tactical nuclear deployment.
  Also (ticker): Ukraine knocks out 5 Russian warplanes, hits 2 refineries;
  Nasdaq falls 4% intraday in the AI sell-off; Shenzhou-24 docks at Tiangong
  with Pakistan's first astronaut aboard.
No headline is invented: every number above comes from the reporting.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (178, 34, 28)
NAVY = (18, 48, 84)
TEAL = (16, 92, 102)
GOLD = (198, 142, 32)
GREY = (90, 86, 78)

HERE = os.path.dirname(os.path.abspath(__file__))
BLACK = os.path.join(HERE, "fonts", "UnifrakturMaguntia-Book.ttf")
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block(draw, x, y, text, fnt, width, fill=INK, leading=1.22):
    """Draw wrapped text; return the y just below the last line."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def justify_lines(draw, text, fnt, width):
    """Greedy word wrap, returning a list of word lists per line."""
    lines, cur = [], []
    for word in text.split():
        trial = cur + [word]
        if draw.textlength(" ".join(trial), font=fnt) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = [word]
    if cur:
        lines.append(cur)
    return lines


def draw_justified(draw, x, y, text, fnt, width, fill=INK, leading=1.22):
    """Draw justified text (last line left-aligned); return y below it."""
    lines = justify_lines(draw, text, fnt, width)
    lh = int(fnt.size * leading)
    for i, words in enumerate(lines):
        if len(words) == 1 or i == len(lines) - 1:
            draw.text((x, y), " ".join(words), font=fnt, fill=fill)
        else:
            words_w = sum(draw.textlength(w, font=fnt) for w in words)
            gap = (width - words_w) / (len(words) - 1)
            xx = x
            for w in words:
                draw.text((xx, y), w, font=fnt, fill=fill)
                xx += draw.textlength(w, font=fnt) + gap
        y += lh
    return y


def fit(y, bottom, what):
    """Fail loudly if a text block runs past its panel (no silent overflow)."""
    if y > bottom:
        raise SystemExit(f"{what} overflows panel: ends {y}, bottom {bottom}")


def kicker(draw, x, y, label, color=RED):
    draw.text((x, y), label, font=font(SANS_B, 15), fill=color)
    return y + 20


def paste_photo(img, x, y, w, h, name):
    """Paste a pre-cropped art photo (exact placed size at 2x) into the box."""
    art = Image.open(os.path.join(HERE, name)).convert("RGB")
    art = art.resize((w, h), Image.LANCZOS)
    img.paste(art, (x, y))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 26
    R = W - M  # 998

    # ---- Masthead: motto left, blackletter nameplate, Late Edition right ----
    d.text((M, 40), "The Day's News", font=font(SERIF_I, 15), fill=INK)
    d.text((M, 60), "in One Image", font=font(SERIF_I, 15), fill=INK)
    d.text((W // 2, 24), "The World Ledger", font=font(BLACK, 80),
           fill=INK, anchor="mt")
    d.text((R, 32), "Late Edition", font=font(SANS_B, 15), fill=INK,
           anchor="rt")
    for i, line in enumerate(("Trade war deepens",
                              "Talks stall in Abu Dhabi",
                              "Markets slide on AI fears")):
        d.text((R, 54 + i * 15), line, font=font(SANS, 11), fill=GREY,
               anchor="rt")
    d.rectangle([M, 112, R, 115], fill=INK)
    d.text((M, 122), "VOL. I — No. 1", font=font(SANS, 12), fill=INK)
    d.text((W // 2, 121), "THURSDAY, NOVEMBER 26, 2026",
           font=font(SERIF_B, 13), fill=INK, anchor="mt")
    d.text((R, 122), "$1.00", font=font(SERIF_B, 13), fill=INK, anchor="rt")
    d.rectangle([M, 146, R, 147], fill=INK)

    # ---- Lead: big port photo left, huge headline right ----
    px, py, pw, ph = M, 156, 474, 272
    paste_photo(img, px, py, pw, ph, "art4-port.jpg")
    d.rectangle([px, py, px + pw, py + ph], outline=INK, width=1)
    y = block(d, px, py + ph + 8,
              "Container cranes at sunset. The proposed duties would cover "
              "goods from 14 economies.",
              font(SERIF_I, 12), pw, fill=GREY, leading=1.25)
    fit(y, 498, "Lead caption")

    tx, tw = 516, R - 516
    y = 156
    y = kicker(d, tx, y, "TRADE  —  TARIFFS")
    y = block(d, tx, y + 2,
              "U.S. Proposes Tariffs on 14 Economies; China Faces 20%",
              font(SERIF_B, 38), tw, leading=1.08)
    y += 6
    y = block(d, tx, y,
              "After an eight-month inquiry into excess factory capacity, "
              "Washington proposes duties on China, the European Union, "
              "Japan and 11 others.",
              font(SERIF_I, 16), tw, leading=1.25)
    y += 6
    y = draw_justified(d, tx, y,
                       "After an eight-month Section 301 investigation into "
                       "excess factory capacity abroad, Washington on "
                       "Thursday proposed new import duties on 14 economies, "
                       "including China, the European Union, Japan and "
                       "Taiwan. China would face a rate of 20 percent, the "
                       "European Union 15 percent and Vietnam as much as 35 "
                       "percent. The proposal opens a comment period before "
                       "any final rates take effect.",
                       font(SERIF, 13), tw, leading=1.22)
    fit(y, 498, "Lead body")
    d.rectangle([M, 504, R, 506], fill=INK)

    # ---- Middle: three narrow justified columns with photos ----
    my, mh = 514, 328
    cw = 314
    cols = [
        ("DIPLOMACY  —  ABU DHABI", NAVY, "art4-abu-dhabi.jpg",
         "Ukraine Talks End Without Progress",
         "Trilateral talks in Abu Dhabi between Ukraine, Russia and the "
         "United States ended without progress, officials said, after "
         "Moscow refused to yield on its territorial claims. Russian "
         "strikes continued against Ukraine's energy grid, while Kyiv said "
         "its forces struck a Russian air base and hit two oil refineries.",
         "nodeal"),
        ("ENERGY  —  STRAIT OF HORMUZ", TEAL, "art4-hormuz.jpg",
         "Mines Hit Tankers; Houthis Strike Saudi Refinery",
         "Two tankers caught fire in the Strait of Hormuz after striking "
         "naval mines, officials said, in the latest disruption to the "
         "world's most important oil artery. Oil prices rose on the news. "
         "Houthi forces said they had also struck Saudi Arabia's largest "
         "refinery.",
         "oilup"),
        ("EGYPT  —  DISASTER", GOLD, "art4-cairo.jpg",
         "Fuel Tanker Fire Kills at Least 31 Near Cairo",
         "At least 31 people were killed and 21 injured when a fuel tanker "
         "crashed and caught fire on the Ring Road in Warraq, Giza. The "
         "blaze engulfed two dozen cars, officials said, in one of the "
         "deadliest road disasters in Egypt in years.",
         None),
    ]
    for i, (kick, color, photo, head, body, overlay) in enumerate(cols):
        x = M + i * (cw + 14)
        y = my
        y = kicker(d, x, y, kick, color)
        y = block(d, x, y + 2, head, font(SERIF_B, 21), cw, leading=1.1)
        y += 4
        paste_photo(img, x, y, cw, 100, photo)
        if overlay == "nodeal":
            sx0, sy0, sx1, sy1 = x + cw - 96, y + 5, x + cw - 6, y + 24
            d.rounded_rectangle([sx0, sy0, sx1, sy1], radius=3,
                                fill=(242, 230, 205),
                                outline=(178, 34, 28), width=2)
            d.text(((sx0 + sx1) // 2, (sy0 + sy1) // 2), "NO DEAL",
                   font=font(SANS_B, 12), fill=(178, 34, 28), anchor="mm")
        elif overlay == "oilup":
            d.rounded_rectangle([x + 6, y + 5, x + 88, y + 24], radius=4,
                                fill=(16, 32, 48),
                                outline=(255, 214, 90), width=1)
            d.text((x + 11, y + 9), "OIL UP", font=font(SANS_B, 12),
                   fill=(255, 214, 90))
        y += 100 + 8
        y = draw_justified(d, x, y, body, font(SERIF, 13), cw, leading=1.22)
        fit(y, my + mh, f"Column {i + 1} body")
        if i < 2:
            d.line([(x + cw + 7, my), (x + cw + 7, my + mh)], fill=GREY,
                   width=1)

    # ---- Netanyahu band: headline + body left, court photo right ----
    ny = 850
    d.rectangle([M, ny - 2, R, ny - 1], fill=INK)
    y = kicker(d, M, ny + 6, "ISRAEL  —  TRIAL", (40, 44, 56))
    y = block(d, M, y + 1, "Judges Urge Dropping Netanyahu Bribery Case",
              font(SERIF_B, 20), 700, leading=1.1)
    y = draw_justified(d, M, y + 3,
                       "Jerusalem judges recommended prosecutors drop the "
                       "bribery charge against Prime Minister Benjamin "
                       "Netanyahu in Case 4000 and reconsider Case 2000. "
                       "It is advice, not a ruling.",
                       font(SERIF, 12), 700, leading=1.2)
    fit(y, 930, "Netanyahu body")
    paste_photo(img, 750, ny + 6, 248, 80, "art4-court.jpg")
    d.rectangle([750, ny + 6, 998, ny + 86], outline=INK, width=1)

    # ---- North Korea strip ----
    ny = 938
    d.rectangle([M, ny, R, ny + 48], fill=NAVY)
    d.text((M + 12, ny + 6), "NORTH KOREA", font=font(SANS_B, 13),
           fill=GOLD)
    d.text((M + 118, ny + 5),
           "Kim calls for wider tactical nuclear deployment.",
           font=font(SERIF_B, 15), fill=(255, 255, 255))
    d.text((M + 12, ny + 27),
           "KCNA: nuclear material output expanding; status as a nuclear "
           "state \u201cabsolutely inviolable\u201d.",
           font=font(SERIF, 14), fill=(255, 255, 255))

    # ---- Bottom: INSIDE index + ticker ----
    d.rectangle([M, 992, R, 993], fill=INK)
    d.text((W // 2, 998),
           "INSIDE — Trade: the tariff list  •  Diplomacy: talks stall  •  "
           "Also: Ukraine knocks out 5 warplanes  •  Nasdaq -4%  •  "
           "Shenzhou-24 docks at Tiangong",
           font=font(SANS, 11), fill=GREY, anchor="mt")

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
