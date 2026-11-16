# /// script
# dependencies = ["pillow"]
# ///
"""Annotate a screenshot for a manual: red rectangles, tags, and instruction cards joined by arrows.

Usage:
    uv run annotate.py spec.json out.png        (or: python annotate.py spec.json out.png)

spec.json:
{
  "image": "screen.png",
  "crop": [x0, y0, x1, y1],            optional, in original pixels
  "zoom": 1.0,                         optional, enlarge a small crop
  "boxes": [[x0, y0, x1, y1], ...],    plain red rectangles (original pixels)
  "tags":  [{"text": "Filtros", "at": [x, y]}],          small red label centred at a point
  "cards": [{"n": "a", "text": "En **Período**, seleccione el mes.",
             "box": [x0, y0, x1, y1], "side": "T", "arrow_x": 900}],
  "explain": false                     true = arrows run from the screenshot to the card, no numbers
}

"side" is where the card sits relative to the screenshot: T (above), B (below), L, R.
"n" is the card's marker: a letter ("a", "b") for actions inside one figure - the instruction is written right beside it, no title.
"title" is optional and meant for explanation cards ("explain": true), where it is the name of the part. "n" may be null. **double asterisks** make a control name bold.
"arrow_x" (original pixels, T/B cards only) moves the arrow away from something it would cross.
The script prints a WARNING when an arrow runs over text or a control inside the screenshot: crop tighter,
move the card to another side, or set "arrow_x". "n" may also be a letter ("a") for cards inside a numbered step.
All coordinates are in the pixels of the ORIGINAL image, whatever the crop or zoom.
"""
import json, math, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

NAVY, INK, RED, LINE = (0, 44, 122), (27, 36, 51), (226, 51, 72), (188, 200, 216)
CARD, CARDLINE = (234, 244, 255), (176, 210, 245)
FONTS = {
    False: ['C:/Windows/Fonts/segoeui.ttf', '/System/Library/Fonts/Supplemental/Arial.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'],
    True: ['C:/Windows/Fonts/segoeuib.ttf', '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
           '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'],
}

def font(size, bold=False):
    for p in FONTS[bold]:
        if os.path.exists(p):
            return ImageFont.truetype(p, int(size))
    return ImageFont.load_default(int(size))


def annotate(spec, out):
    src = Image.open(spec['image']).convert('RGB')
    crop = spec.get('crop') or [0, 0, src.width, src.height]
    zoom = spec.get('zoom', 1.0)
    shot = src.crop(tuple(crop))
    if zoom != 1:
        shot = shot.resize((int(shot.width * zoom), int(shot.height * zoom)), Image.LANCZOS)
    cx0, cy0 = crop[0], crop[1]
    T = lambda b: [(b[0] - cx0) * zoom, (b[1] - cy0) * zoom, (b[2] - cx0) * zoom, (b[3] - cy0) * zoom]
    cards = spec.get('cards', [])
    explain = spec.get('explain', False)
    sides = {s: [c for c in cards if c.get('side', 'R') == s] for s in 'LRTB'}

    # scale text and strokes to the final width, so labels read the same on every figure
    k = shot.width * (1 + .44 * bool(sides['L']) + .44 * bool(sides['R'])) / 1500
    kf = k * 1.04
    FT, FD, FB, FN = font(38 * kf, True), font(33 * kf), font(33 * kf, True), font(36 * kf, True)
    PAD = 24; G = int(64 * k); R = int(28 * kf); LH = int(45 * kf); CP = int(24 * kf); lw = max(4, int(5 * k))
    tmp = ImageDraw.Draw(Image.new('RGB', (10, 10)))

    def layout(text, maxw):
        toks = [(w, i % 2 == 1) for i, seg in enumerate(text.split('**')) for w in seg.split()]
        lines, cur, curw = [], [], 0
        sp = tmp.textlength(' ', font=FD)
        for w, bold in toks:
            ww = tmp.textlength(w, font=FB if bold else FD)
            glue = w[0] in ',.;:)' and bool(cur)
            if cur and not glue and curw + sp + ww > maxw:
                lines.append(cur); cur, curw = [], 0
            curw += (sp if cur and not glue else 0) + ww
            cur.append((w, bold, glue))
        if cur: lines.append(cur)
        return lines

    def inline(c):
        # a lettered card with no title: "a  En Monto, escriba el importe." - the instruction starts beside the letter
        return not c.get('title') and c.get('n') is not None and not explain

    def card_size(c, cw):
        if inline(c):
            lines = layout(c.get('text', ''), cw - 2 * CP - 2 * R - int(22 * kf))
            return lines, CP + max(2 * R, len(lines) * LH) + CP
        lines = layout(c.get('text', ''), cw - 2 * CP)
        return lines, CP + 2 * R + int(14 * kf) + len(lines) * LH + CP - int(8 * kf)

    LW = int(.40 * shot.width) if sides['L'] else 0
    RW = int(.40 * shot.width) if sides['R'] else 0
    def row(cs):
        cw = int(min(.46 * shot.width, (LW + shot.width + RW - (len(cs) - 1) * G) / max(1, len(cs))))
        return cw, [card_size(c, cw) for c in cs]
    tcw, tcards = row(sides['T']); bcw, bcards = row(sides['B'])
    TH = (max(c[1] for c in tcards) + G) if tcards else 0
    BH = (max(c[1] for c in bcards) + G) if bcards else 0
    bare = not cards
    W = PAD + LW + (G if LW else 0) + shot.width + (G if RW else 0) + RW + PAD
    ox = PAD + LW + (G if LW else 0); oy = PAD + TH
    H0 = oy + shot.height + BH + PAD
    cv = Image.new('RGB', (W, H0 + 900), 'white'); used = [H0]

    # the screenshot keeps its own frame and shadow, so it never blends with the instructions
    sh = Image.new('L', cv.size, 0)
    ImageDraw.Draw(sh).rounded_rectangle([ox, oy + 6, ox + shot.width, oy + shot.height + 10], 10, fill=110)
    cv.paste(Image.new('RGB', cv.size, (0, 27, 77)), (0, 0), sh.filter(ImageFilter.GaussianBlur(12)))
    cv.paste(shot, (ox, oy)); d = ImageDraw.Draw(cv)
    d.rectangle([ox, oy, ox + shot.width - 1, oy + shot.height - 1], outline=LINE, width=2)

    def rbox(b):
        x0, y0, x1, y1 = T(b)
        d.rounded_rectangle([ox + x0 - 4, oy + y0 - 4, ox + x1 + 4, oy + y1 + 4], int(14 * k), outline=(255, 255, 255), width=lw + 4)
        d.rounded_rectangle([ox + x0, oy + y0, ox + x1, oy + y1], int(12 * k), outline=RED, width=lw)
    for b in spec.get('boxes', []): rbox(b)
    for c in cards: rbox(c['box'])

    for t in spec.get('tags', []):
        f = font(30 * k, True); tw = d.textlength(t['text'], font=f)
        x = ox + (t['at'][0] - cx0) * zoom; y = oy + (t['at'][1] - cy0) * zoom; px, py, th = int(16 * k), int(9 * k), int(30 * k)
        d.rounded_rectangle([x - tw / 2 - px - 4, y - th / 2 - py - 4, x + tw / 2 + px + 4, y + th / 2 + py + 4], int(13 * k), fill='white')
        d.rounded_rectangle([x - tw / 2 - px, y - th / 2 - py, x + tw / 2 + px, y + th / 2 + py], int(11 * k), fill=RED)
        d.text((x, y), t['text'], font=f, fill='white', anchor='mm')

    def arrow(pts):
        if explain:
            pts = pts[::-1]; r = int(8 * k)
            d.ellipse([pts[0][0] - r, pts[0][1] - r, pts[0][0] + r, pts[0][1] + r], fill=RED)
        d.line(pts, fill=RED, width=lw, joint='curve')
        (x0, y0), (x1, y1) = pts[-2], pts[-1]
        a = math.atan2(y0 - y1, x0 - x1); L = 26 * k
        d.polygon([(x1, y1), (x1 + L * math.cos(a + .42), y1 + L * math.sin(a + .42)), (x1 + L * math.cos(a - .42), y1 + L * math.sin(a - .42))], fill=RED)

    px = shot.load(); warnings = []

    def check(c, xa, ya, xb, yb):
        # warn when the arrow segment (canvas coordinates, inside the screenshot) runs over content
        n = int(max(abs(xb - xa), abs(yb - ya))); edges = 0; prev = None
        for i in range(n):
            x = int(xa + (xb - xa) * i / max(1, n) - ox); y = int(ya + (yb - ya) * i / max(1, n) - oy)
            if not (0 <= x < shot.width and 0 <= y < shot.height): continue
            cur = px[x, y]
            if prev is not None and sum(abs(a - b) for a, b in zip(cur, prev)) > 45: edges += 1
            prev = cur
        if edges >= 4:
            warnings.append('WARNING: the arrow of card "%s" crosses content in the screenshot (%d edges). '
                            'Crop tighter, move the card to another side, or set arrow_x.' % (c.get('title', c.get('n')), edges))

    def draw_card(x, y, cw, ch, c, lines):
        d.rounded_rectangle([x, y, x + cw, y + ch], int(18 * kf), fill=CARD, outline=CARDLINE, width=3)
        d.rounded_rectangle([x, y, x + int(10 * kf), y + ch], int(5 * kf), fill=NAVY)
        cx = x + CP + int(6 * kf); cy = y + CP + R
        if c.get('n') is None or explain:
            d.text((cx, cy), c.get('title', ''), font=FT, fill=NAVY, anchor='lm')
        else:
            d.ellipse([cx, cy - R, cx + 2 * R, cy + R], fill=NAVY); d.text((cx + R, cy - 2), str(c['n']), font=FN, fill='white', anchor='mm')
            d.text((cx + 2 * R + 14 * kf, cy), c.get('title', ''), font=FT, fill=NAVY, anchor='lm')
        yy = cy + R + int(14 * kf); sp = d.textlength(' ', font=FD); tx = cx
        if inline(c):
            tx = cx + 2 * R + int(16 * kf); yy = cy - R + max(0, (2 * R - LH) // 2)
        for ln in lines:
            xx = tx
            for w, bold, glue in ln:
                f = FB if bold else FD
                if glue: xx -= sp
                d.text((xx, yy), w, font=f, fill=NAVY if bold else INK); xx += d.textlength(w, font=f) + sp
            yy += LH
        used.append(y + ch + PAD)

    for side in 'LR':
        prev = oy
        for c in sorted(sides[side], key=lambda c: c['box'][1]):
            x0, y0, x1, y1 = T(c['box']); by = oy + (y0 + y1) / 2
            cw = LW if side == 'L' else RW
            lines, ch = card_size(c, cw)
            cy = max(by - ch / 2, prev, PAD); prev = cy + ch + int(22 * k)
            ay = min(max(by, cy + 24), cy + ch - 24)
            if side == 'L':
                draw_card(PAD, cy, cw, ch, c, lines)
                start, end, jx = (PAD + cw + 8, ay), (ox + x0 - 12, by), ox - G / 2; check(c, ox + 2, by, ox + x0 - 14, by)
            else:
                lx = ox + shot.width + G
                draw_card(lx, cy, cw, ch, c, lines)
                start, end, jx = (lx - 8, ay), (ox + x1 + 12, by), ox + shot.width + G / 2; check(c, ox + x1 + 14, by, ox + shot.width - 2, by)
            arrow([start, end] if abs(ay - by) < 2 else [start, (jx, ay), (jx, by), end])

    for side, cw, sized in (('T', tcw, tcards), ('B', bcw, bcards)):
        cs = sides[side]
        if not cs: continue
        order = sorted(range(len(cs)), key=lambda i: cs[i]['box'][0])
        pos = {}; prev_right = PAD - G
        for i in order:
            x0, y0, x1, y1 = T(cs[i]['box'])
            ax = ox + ((cs[i]['arrow_x'] - cx0) * zoom if 'arrow_x' in cs[i] else (x0 + x1) / 2)
            left = min(max(ax - cw / 2, prev_right + G, PAD), W - PAD - cw)
            pos[i] = [left, ax]; prev_right = left + cw
        nxt = W - PAD + G
        for i in reversed(order):
            pos[i][0] = min(pos[i][0], nxt - G - cw); nxt = pos[i][0]
        for i in order:
            c = cs[i]; left, ax = pos[i]; lines, ch = sized[i]; x0, y0, x1, y1 = T(c['box'])
            ax = min(max(ax, left + 40), left + cw - 40)
            if side == 'T':
                cy = oy - G - ch; draw_card(left, cy, cw, ch, c, lines); arrow([(ax, cy + ch + 8), (ax, oy + y0 - 12)]); check(c, ax, oy + 2, ax, oy + y0 - 14)
            else:
                cy = oy + shot.height + G; draw_card(left, cy, cw, ch, c, lines); arrow([(ax, cy - 8), (ax, oy + y1 + 12)]); check(c, ax, oy + y1 + 14, ax, oy + shot.height - 2)

    cv = cv.crop((0, 0, W, int(max(used))))
    cv.save(out)
    for w in warnings: print(w)
    return cv.size


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    spec = json.load(open(sys.argv[1], encoding='utf-8'))
    base = os.path.dirname(os.path.abspath(sys.argv[1]))
    if not os.path.isabs(spec['image']):
        spec['image'] = os.path.join(base, spec['image'])
    print(sys.argv[2], annotate(spec, sys.argv[2]))
