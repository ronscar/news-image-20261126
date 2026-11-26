# Design philosophy — "Ledger Clarity"

## The movement

A front page is a ledger of one day, kept with the discipline of a
typesetter who has set the same page a thousand times. Nothing shouts for
attention except the one story that earned it; everything else waits its
turn in order. The page is built, not decorated: every rule, every gap,
every colour is doing a job, and anything that does no job is removed.
The result should look as though it took countless hours to set — because
the care is in the alignment, the spacing, and the restraint, the product
of deep expertise and painstaking attention to the smallest detail.

## One lead, one page

A single story dominates. It takes the full width and the largest picture,
because a reader who glances for one second must leave knowing the day's
most consequential event. The remaining stories step down in strict
order: two of equal weight, then two smaller, then a strip, then a ticker.
No two stories compete at the same size. Scale is the table of contents.

## Colour as a signpost, not decoration

Each section carries one colour, and that colour is its name: red for
trade and war, navy for diplomacy, teal for energy, gold for disaster,
dark slate for the courts. The reader never has to read a section label
twice to know where they are. Colour never appears for its own sake; it
marks a boundary, a kicker, a number. The paper stays warm and quiet so
the ink and the colours can speak.

## Space is the craft

White space is not empty. The margins are wide, the gutters are even,
and no panel touches another. Text never crowds its frame; every block
has room to breathe, and every line ends before its edge. Nothing
overlaps, nothing is cut off, nothing leans on its neighbour. The
precision of the grid is what makes the page feel meticulously crafted:
a reader feels the order before they read a word.

## Typography that is sharp at any size

Type is drawn, not rendered from a photograph, so every letter stays
crisp. A heavy serif carries the headlines, a plain sans carries the
labels, and the masthead date is the largest type on the page, because
the date is the first thing a judge of one day's news must see. The
smallest text on the page is still legible when the whole image is
shrunk to 300 pixels across: no line is set smaller than it needs to be,
and no headline wraps onto a word it cannot hold.

## How this page follows it

- Masthead: "26 NOVEMBER 2026" in 66pt serif, the dominant type.
- Lead: the US tariff proposal, full width, with a drawn bar chart of the
  proposed rates — the day's biggest story, the biggest panel.
- Two rows of two stories each, stepping down in size and weight.
- A full-width strip for North Korea, then a one-line ticker for the
  remaining news.
- Kicker tags in section colours; paper background; thin black rules.
- PNG kept small (limited palette, gradients drawn as solid rows, no
  photographic noise) so the file stays far under the 1 MiB gate and
  small enough to help the size tie-break. v3: the four photo panels add
  photographic noise, so they are stored pre-cropped at 2x strip
  resolution as JPEGs and the total stays well under the gate.

## Broadsheet, not a grid (v4)

v4 rebuilds the page as a classic broadsheet, in the style of the New
York Times front page (style only — our own name, motto and stories).
A broadsheet is dense on purpose: the masthead is the biggest type on
the page, the lead is one big photograph with a caption and a headline
that could fill a wall, and the rest of the news is set in narrow
justified columns that invite the eye down, not across. The square
canvas forces a compressed broadsheet — the lead photograph is 474px
wide instead of full-bleed, the middle stories run in three narrow
columns instead of five, and the trial story is a horizontal band
instead of a column — but the grammar is the same: nameplate, dateline,
lead photograph, headline, columns, index, ticker. The blackletter
nameplate ("The World Ledger") carries the page's authority; the
classic serif (Liberation Serif, a Times-like face) carries the news.
Body text is justified, because a broadsheet's columns are flush on
both sides; the justification is drawn word by word so no line is
stretched or gapped. Thin rules separate the masthead, the lead, the
columns and the bottom band, the way a real front page is ruled. At
300px wide the page must still read as a newspaper — masthead, lead
photograph, headline, columns — even though the body text itself is too
small to read there, exactly as on a real broadsheet seen from across
the room.

## Photographs, not illustrations

v3 replaced the drawn scenes with photorealistic photos. Each panel is
a real-looking place at a real hour: a wood-panelled negotiation room,
a tanker at dusk, a night highway on fire, a stone courthouse. The
photos are AI-generated photo-style illustrations, not photographs of
the actual events; they are pre-cropped to each strip and stored at 2x
strip resolution, so the page keeps its crisp drawn type and only the
photographs carry noise. Every photo is built from one dominant subject
— three flags over a table, one long hull, one burning tank, one
pediment with scales — so it still reads at 300px wide, where the judge
sees it. The small labels stay drawn, never photographed: the OIL UP
chip, the NO DEAL stamp, the CASE 4000 plaque. Nothing is allowed to
cross its panel edge, and no text ever sits on a busy part of a photo:
each overlay sits on a quiet corner of its picture.
