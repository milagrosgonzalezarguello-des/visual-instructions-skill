# /// script
# dependencies = ["pillow", "numpy"]
# ///
"""Join two captures of one scrolling window into a single image.

Usage:
    uv run stitch.py top.png bottom.png out.png [--skip-top N] [--skip-bottom N]

Both captures must have the same width. The script finds the rows where the bottom of the first capture
repeats at the top of the second, and joins them there.

--skip-top N     ignore the first N rows of the SECOND capture (a header that stays fixed while scrolling)
--skip-bottom N  ignore the last N rows of the FIRST capture (a footer or button bar that stays fixed)
"""
import sys
import numpy as np
from PIL import Image


def stitch(top, bottom, skip_top=0, skip_bottom=0):
    a = Image.open(top).convert('RGB'); b = Image.open(bottom).convert('RGB')
    if a.width != b.width:
        sys.exit(f'widths differ: {a.width} vs {b.width}')
    a = a.crop((0, 0, a.width, a.height - skip_bottom)); b = b.crop((0, skip_top, b.width, b.height))
    ga = np.asarray(a.convert('L'), dtype=np.int16); gb = np.asarray(b.convert('L'), dtype=np.int16)
    best = None
    for h in range(min(ga.shape[0], gb.shape[0]), 23, -1):      # prefer the largest overlap that matches
        if np.abs(ga[-h:] - gb[:h]).mean() < 2.0 and ga[-h:].std() > 4:   # must match and not be a blank area
            best = h; break
    if best is None:
        sys.exit('no overlap found: the captures share no rows (try --skip-top / --skip-bottom)')
    out = Image.new('RGB', (a.width, a.height + b.height - best), 'white')
    out.paste(a, (0, 0)); out.paste(b.crop((0, best, b.width, b.height)), (0, a.height))
    return out, best


if __name__ == '__main__':
    args = sys.argv[1:]; opt = {'--skip-top': 0, '--skip-bottom': 0}
    for k in list(opt):
        if k in args:
            i = args.index(k); opt[k] = int(args[i + 1]); del args[i:i + 2]
    if len(args) != 3:
        sys.exit(__doc__)
    im, h = stitch(args[0], args[1], opt['--skip-top'], opt['--skip-bottom'])
    im.save(args[2]); print(args[2], im.size, 'overlap', h, 'rows')
