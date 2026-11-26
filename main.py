"""news-image-20261126 entry: copy the rendered image this repository holds
to /output/entry.png.

Standard library only, no network, no randomness, no model calls. The copy
is a plain byte copy, so two runs always write the same bytes. The image is
a 1024x1024 PNG front page summing up Thursday 26 November 2026
(see generate.py for how it was drawn and README.md for the sources).
"""

import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, OUT)

# Fail loudly instead of shipping a truncated file: the gate requires a
# whole PNG, told apart by its first bytes, at most 1 MiB and 1024x1024.
with open(OUT, "rb") as f:
    data = f.read()
if data[:8] != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("entry.png is not a PNG")
if len(data) > 1048576:
    raise SystemExit("entry.png exceeds the 1 MiB gate")
# Gate also caps dimensions at 1024x1024: read them from the PNG IHDR
# (width and height are the first two big-endian uint32s after the header).
width, height = struct.unpack(">II", data[16:24])
if width > 1024 or height > 1024:
    raise SystemExit(f"entry.png is {width}x{height}, over the 1024x1024 gate")
print("wrote", OUT, len(data), "bytes", f"{width}x{height}")
