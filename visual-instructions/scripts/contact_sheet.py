# /// script
# dependencies = ["pillow"]
# ///
"""Build one sheet with a zoomed close-up of every red rectangle in the given annotate.py specs.

Usage:
    uv run contact_sheet.py sheet.png spec1.json spec2.json ...

Look at the sheet before delivering: a rectangle must be centred on its control, with the same margin
on every side, and must not cover a label. It is much easier to see here than on the full page.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

RED = (226, 51, 72)


def closeups(spec_path):
    spec = json.load(open(spec_path, encoding='utf-8'))
    img = spec['image'] if os.path.isabs(spec['image']) else os.path.join(os.path.dirname(os.path.abspath(spec_path)), spec['image'])
    src = Image.open(img).convert('RGB')
    boxes = [tuple(b) for b in spec.get('boxes', [])] + [tuple(c['box']) for c in spec.get('cards', [])]
    out = []
    for b in boxes:
        m = max(40, int(.25 * max(b[2] - b[0], b[3] - b[1])))
        region = (max(0, b[0] - m), max(0, b[1] - m), min(src.width, b[2] + m), min(src.height, b[3] + m))
        im = src.crop(region); d = ImageDraw.Draw(im)
        d.rounded_rectangle([b[0] - region[0], b[1] - region[1], b[2] - region[0], b[3] - region[1]], 6, outline=RED, width=3)
        z = min(3.0, 520 / im.width, 300 / im.height)
        out.append((os.path.basename(spec_path), im.resize((max(1, int(im.width * z)), max(1, int(im.height * z))), Image.LANCZOS)))
    return out


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    tiles = [t for p in sys.argv[2:] for t in closeups(p)]
    if not tiles:
        sys.exit('no rectangles found in the specs')
    cols = 3; W, H = 540, 340; rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * W, rows * H), (120, 124, 132)); d = ImageDraw.Draw(sheet)
    try:
        f = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 16)
    except OSError:
        f = ImageFont.load_default()
    for i, (name, im) in enumerate(tiles):
        x, y = (i % cols) * W, (i // cols) * H
        sheet.paste(im, (x + (W - im.width) // 2, y + 26 + (H - 36 - im.height) // 2))
        d.text((x + 8, y + 4), f'{i + 1}. {name}', font=f, fill='white')
    sheet.save(sys.argv[1]); print(sys.argv[1], sheet.size, len(tiles), 'rectangles')
