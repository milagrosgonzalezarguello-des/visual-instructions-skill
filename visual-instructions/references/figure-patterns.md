# Figure patterns

## Why figures are built this way

- **Always a picture.** Every step gets its own capture, even a simple one, and even when the screen has barely changed since the previous step: repeat the capture with the new mark. Readers follow the pictures, not the text. Results the reader must recognise, waiting states ("Descargando...") and anything that arrives outside the product are shown too. The only images to leave out are decorative ones that show nothing the reader will see or do.
- **A cue on every screenshot.** A capture with no mark makes the reader search. Direct the eye to the exact button or area with a rectangle (default), an arrow (to join it to its text), or a highlight/dimming of the rest (for a large region). One style of cue per purpose, the same throughout.
- **One moment per picture.** The reader compares the picture to their screen. If it shows a state they have not reached (a confirmation, a filled field, a later notice), they conclude they did something wrong. Hide toasts that belong to a later moment; when the screen changes, use a new figure. Inside one task, repeat the screenshot in each step rather than making one image serve five.
- **A rectangle, not a code.** A red rectangle says "here" with no decoding. Numbered pins turn the picture into a puzzle: find the number, look it up, go back.
- **Product and instruction never blend.** The screenshot has its own frame and soft shadow; your text sits outside it in a tinted card. If the instruction is in the card, it is not repeated as a list underneath - said twice, readers wonder whether the two versions differ.
- **Readable or useless.** If the button label cannot be read at print size, crop tighter or give the screenshot the full width (cards above and below instead of at the sides).

`assets/examples/good-lettered-cards.png` and `assets/examples/bad-pins.png` show the same screen done both ways.

Six patterns cover almost every figure in a manual. Choose by what the reader needs at that point, not by habit. All of them can be produced with `scripts/annotate.py`.

## 1. Single target

**When:** a step with one action on a screen.
**How:** the screenshot, cropped to the relevant area, with one red rectangle around the control. No number, no label - the step text sits right above it.

```json
{"image": "upload.png", "crop": [0, 300, 1140, 700], "boxes": [[61, 369, 1075, 555]]}
```

## 2. Lettered actions on one screen

**When:** two or three actions on the same screen, in a fixed order.
**How:** rectangles on the controls; one card per action, outside the screenshot, joined to its rectangle by an arrow. Each card carries a **letter and the instruction itself** - nothing else:

- a. En **Monto**, escriba el importe.
- b. En **Categoría**, seleccione una opción de la lista desplegable.
- c. Seleccione **CONTINUAR**.

Do not narrate the order with titles like "Primero", "Después", "Por último" ("First", "Then", "Finally"): the letters already give the order, and the extra word is one more thing to read. Do not repeat the steps below the figure.

Place cards above (`T`) and below (`B`) the screenshot when it is wide, so it keeps the full width; at the sides (`L`, `R`) when it is narrow. Order the cards so that reading order matches action order - "a" must not end up below or to the right of "b".

```json
{"image": "form.png", "crop": [0, 0, 1402, 410],
 "cards": [
   {"n": "a", "text": "En **Período**, seleccione el mes.", "box": [44, 140, 702, 256], "side": "T"},
   {"n": "b", "text": "Seleccione **FILTRAR**.", "box": [712, 307, 1038, 385], "side": "B"}]}
```

**Group only what is simple.** Use your judgement as an instructional designer: actions share one figure when each is trivial and they belong together - typing a value, choosing from a short list, ticking a box, all on one form. Give an action **its own numbered step and its own figure** when any of these is true:

- it opens something (a calendar, a file picker, a dialog, a new screen);
- it needs explaining (a format, a rule, a note or a warning);
- its result must be checked before going on ("Verá: ...");
- it cannot be undone (send, delete, confirm);
- a first-time reader could plausibly get it wrong.

So on a form: "a. En **Monto**, escriba el importe. b. En **Categoría**, seleccione una opción" can share a figure; "Arrastre el comprobante al recuadro" and "Seleccione **ENVIAR**" are separate steps. When in doubt, separate - an extra step costs a few lines, a crowded figure costs the reader.

Letters, not numbers, because this figure usually sits inside a numbered step. If the task has four or more actions, or the screen changes between them, do not use this pattern - go step by step with pattern 1.

## 3. Parts of a screen (explanation, not action)

**When:** telling the reader what each area or option is for.
**How:** a rectangle around each part and a short arrow **from the part to its card** (`"explain": true` reverses the arrow and drops the numbers). Cards carry the part's name as title and one sentence.

For a menu, crop to the menu, put it on the left and the cards on the right, so arrows run left to right.

Keep the cards on one or two sides (right, or right and below), the same width and aligned, so the figure reads as one column of explanations rather than labels scattered around the picture. When one part sits inside another (a column inside a table), do not draw both rectangles with crossing arrows: mark the outer one with a tag on its border (pattern 4) and give the arrow to the inner one, or use two figures.

## 4. Tagged regions

**When:** orienting the reader on a busy screen ("filters are here, results are there").
**How:** a rectangle around each region and a small red tag centred on its top border with the region's name.

```json
{"image": "screen.png", "boxes": [[495, 290, 1853, 686], [495, 716, 1853, 964]],
 "tags": [{"text": "Filtros", "at": [1090, 290]}, {"text": "Tabla", "at": [1050, 716]}]}
```

## 5. Concept illustration

**When:** the thing to understand is not on any screen - a file format, a rule about what can be combined, a before/after.
**How:** draw it. A "correct / incorrect" pair with a green check and a red cross is understood without reading. Keep to the document's colours and line weight so it looks like part of the same family.

## 6. Stitched window

**When:** a dialog or page is taller than the screen and was captured in two or more scrolls.
**How:** find the overlap between the captures (match a strip around a heading that appears in both), join them above a blank line, and present one image. Mention in the caption that the reader will need to scroll.

## Choosing between arrows and references

Default to arrows (patterns 2 and 3): the text sits beside the part, so the reader never looks away. `annotate.py` bends an arrow with one elbow when card and target are not aligned; place cards on the side nearest their targets so the arrows stay short and do not cross. Use lettered references only when the targets are too many or too close for arrows, and then write each text right next to its letter beside the picture - never as a legend underneath.

## Tools

- `scripts/annotate.py spec.json out.png` draws every pattern above. It prints a warning when an arrow passes over text or a control in the screenshot; fix it by cropping the screenshot tighter, moving the card to another side, or setting `arrow_x`.
- `scripts/stitch.py top.png bottom.png out.png` joins two captures of one scrolling window (pattern 6).
- `scripts/contact_sheet.py out.png spec1.json spec2.json ...` builds one sheet with a zoomed close-up of every rectangle in those specs. Look at it before delivering.

## Getting coordinates right

Estimating coordinates by eye from a scaled preview produces marks that are a few pixels off, and readers notice. Prefer, in this order:

1. **OCR word boxes** for anything with text (labels, button captions, menu items). On Windows, the built-in OCR (`Windows.Media.Ocr`) returns word bounding boxes without installing anything; elsewhere use Tesseract.
2. **Colour regions** for buttons and icons: threshold on the control's colour inside a rough search area and take the bounding box.
3. Estimation only as a last resort, followed by a zoomed check.

After drawing, build a contact sheet with a close-up of every mark in the document and look at them together. It takes a minute and catches almost every misplacement.
