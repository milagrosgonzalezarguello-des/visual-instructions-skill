---
name: visual-instructions
description: Design user manuals, how-to guides, tutorials, onboarding docs, SOPs and step-by-step instructions that people can follow without reading much - visual, low cognitive load, one action per step, annotated screenshots, concise copy, clear hierarchy. Use this whenever the user asks to write, redesign, review, correct or improve a manual, user guide, instructivo, manual de usuario, guía, paso a paso, tutorial, quick-reference, help article, job aid or any "how do I do X in this app" / "cómo se hace X" document; when they share screenshots or capturas to turn into instructions ("armame el instructivo", "te paso las capturas"); when a client or reviewer sends corrections to a manual; or when they say a guide is confusing, too long, too dense or "nadie lo lee" - even if they never say "instructional design".
---

# Visual instructions

Write instructions for people who will not read them.

The reader is in the middle of a task, a little anxious, glancing between the document and the real screen. They scan for a picture that looks like what they see, find the red mark, do the thing, and look again. Anything that makes them stop and decode - a paragraph, a legend, a number to look up - is where they give up and call someone.

So the job is not "explain the system". It is: **at every moment, make the next action obvious at a glance.**

## What every page must get right

Check these on every page before anything else. They are what a reader notices first when they are wrong.

1. **Every step has its picture.** Always. Each step is shown with a capture and a cue - a red rectangle, an arrow or a highlight - exactly on the button or area. A reader who looks only at the pictures can still complete the task. If a capture is missing, ask for it; never leave a step with text only.
2. **Every rectangle is well placed.** Centred on its control, the same margin on all sides, covering no label. Measured, then checked zoomed in - never estimated.
3. **Screenshots stand apart from instructions.** Every screenshot has a frame and a soft shadow; instruction text is never inside it.
4. **The hierarchy is visible.** Chapter, section, step and callout each look different, and the same level looks the same everywhere.
5. **The numbering is clean.** Sections 1, 1.1; steps 1, 2, 3 restarting in each task; sub-steps a, b. Never two series of numbers competing on a page.
6. **Information comes in chunks.** Short blocks with a heading, a few steps each, air between them.
7. **Visual first.** Visual support is never optional: if something can be shown, it is shown, and words only add what the picture cannot say. The same goes for results ("Verá:"), concepts (draw them) and what arrives outside the product (an e-mail, a file).
8. **White space.** Wide margins, space between paragraphs and around figures. A crowded page is tiring and cannot be scanned.

`assets/examples/` has a good and a bad version of the same figure. Look at them once before drawing your first figure.

## Language

Write the document in the language the user asks for; if they do not say, use the language of their request and of the product's screens. The skill works the same in Spanish and English - the examples in these files are mostly Spanish, so use the equivalents below and never mix the two in one document. Control names stay exactly as on screen, even when the screen is in another language than the document.

| | Español | English |
|---|---|---|
| Act on a control | Seleccione **X** | Select **X** |
| Type / choose / pick a date | Escriba / Seleccione en la lista / Seleccione en el calendario | Type / Choose from the list / Pick in the calendar |
| Result | Verá: | You will see: |
| Actions in one figure | a. En **Monto**, escriba... / b. En **Categoría**, seleccione... | a. In **Amount**, type... / b. In **Category**, choose... |
| Callouts | Importante, Consejo, Nota, Si ve algo distinto | Important, Tip, Note, If you see something different |
| Contents / back link | Índice / ↑ Índice | Contents / ↑ Contents |

**Register is the client's choice, not a default.** Some organisations address their users formally, others informally; both are correct. Find out before writing, in this order:

1. What the user says ("tratalos de vos", "formal").
2. How the product itself talks: read the screens. "Seleccione una categoría" means usted; "Elegí una categoría" means vos; "Elige" means tú.
3. How the organisation's existing manuals or e-mails talk.
4. If none of these settles it, ask once. Do not guess: rewriting every verb later is a full correction round.

| | Formal (usted) | Informal (vos, Río de la Plata) | Informal (tú) | English |
|---|---|---|---|---|
| Act on a control | Seleccione **X** | Seleccioná **X** | Selecciona **X** | Select **X** |
| Type | Escriba | Escribí | Escribe | Type |
| Result | Verá: | Vas a ver: | Verás: | You will see: |
| Recovery callout | Si ve algo distinto | Si ves algo distinto | Si ves algo distinto | If you see something different |
| Possessive | su usuario | tu usuario | tu usuario | your user |

English has one "you"; there the choice is tone: plain and neutral for formal clients ("Select **Send**"), warmer with contractions for informal ones ("You'll see your file in the list").

Whichever is chosen, keep it from the cover to the last page - steps, cards inside figures, callouts and captions. A single "seleccioná" in a formal manual reads as a mistake.

## How to work

1. **Find out who reads it and what they need to get done.** Audience, language, register (formal or informal - see Language) and the list of tasks. Organise by task ("Cargar un archivo"), never by screen or feature, and name chapters the way the product's menu does.
2. **Collect the real material.** Real screenshots, the exact wording of buttons and menus, the source content. Never invent a screen. **Ask which user role each capture was taken with**: an administrator's screen has buttons and filters the reader may not have. If a capture shows another role, or a screen is missing, say so and list the captures you need by name so they can be taken in one pass.
3. **Sanitize every screenshot** before it goes anywhere (below).
4. **Lay the tasks side by side** and find shared beginnings and variations before writing (see `references/writing-rules.md`, "Structure").
5. **Figures first, then words.** Start the document from `assets/template.html` - it already solves the hierarchy, step numbering, callouts with icons, screenshot frame and spacing - and draw figures with `scripts/annotate.py`. Read `references/figure-patterns.md` before drawing and `references/writing-rules.md` before writing.
6. **Review the render, not the source**, figure by figure, against `references/checklist.md`. Run `scripts/contact_sheet.py` to see every mark zoomed in.
7. **Deliver, say what you verified and what you did not, and expect corrections.** When they come, follow `references/revisions.md`.

## The rules in brief

Each of these is expanded, with examples, in the reference named beside it.

**Steps and figures** (`references/figure-patterns.md`)
- One action per step; "review and send" is two steps.
- Group actions in one figure only when they are simple and belong together (typing, choosing from a list on one form). Anything complex - it opens something, needs explaining, has a result to check, cannot be undone - is its own step with its own figure. When in doubt, separate.
- One moment per picture: never show a state the reader has not reached yet. When the screen changes, use a new figure.
- Mark the control with a red rectangle. No numbered pins to decode.
- Do not narrate the order ("Primero..., luego..., por último..."). Give each action a marker and the instruction: "a. En **Monto**, escriba el importe." "b. En **Categoría**, seleccione una opción de la lista desplegable."
- Instruction text lives outside the screenshot, in a tinted card joined to its rectangle by an arrow - and is not repeated as a list below.
- Arrows first, references last. When a figure covers several parts, an arrow joins each part to its text; arrows may bend at a right angle, never cross each other, a title or a control; cards are balanced and follow left-to-right reading. Lettered references only when arrows cannot work, and then the text sits beside its letter, with no legend underneath.
- Crop so the labels can be read; never cut through a row, logo or control.

**Words** (`references/writing-rules.md`)
- Clear, concise, consistent: one reading per sentence, no sentence the reader could lose without acting differently, one name per thing and one verb per kind of action.
- Where before what, condition before action. Three formats, never mixed: **bold** for controls the reader acts on, "quotation marks" for names of screens and windows (la pantalla "Nuevo gasto"), *italics* for examples - all spelled as on screen.
- A step that fills a field names the field and says how the value goes in (typed, chosen from a list, picked in a calendar).
- Examples come after the instruction, introduced by "Por ejemplo:".
- Actions are numbered; what the reader will see ("Verá:") is not, looks different, and is shown in a figure.
- Context and action are kept apart: the "why", conditions and warnings come before the steps (one sentence or a callout); the steps themselves contain only what to do. No theory inside a step.
- Plain, everyday words; active voice and the imperative, verb first ("Seleccione **Guardar**", not "El botón Guardar debe ser presionado").
- Do not announce the obvious ("son 4 pasos"), and never claim more than the system guarantees or guess what a control does - ask.

**Callouts: standard alerts**
- Four kinds, each with its own box colour and icon, identical everywhere in the document, so the reader knows what it is before reading a word:

| Kind | Español | Icon | Use it for |
|---|---|---|---|
| Warning | **Importante** (or **Advertencia** - pick one) | warning sign | a risk: losing data, an error, something that cannot be undone |
| Tip | **Consejo** | light bulb | a shortcut or best practice - real advice |
| Note | **Nota** | "i" | useful information about how something works |
| Recovery | **Si ve algo distinto** | wrench | what to do when the screen does not match, one row per situation |

- If it is not advice it is not a Consejo; if nothing can go wrong it is not an Importante. A mislabelled callout teaches readers to ignore all of them.
- Keep titles calm - never "Si algo sale mal", "Errores" or "Problemas".
- Several points inside a callout are bullets. A warning goes before the action it affects.

**Structure and layout** (`references/writing-rules.md`, "Structure")
- Split a procedure of more than about seven steps into named parts. Normal path first, exceptions after.
- Never repeat a shared beginning: write it once, then fork, reference it, or describe the variation.
- One numbering per level; large titles; line spacing 1.5-1.7 for anything that wraps; one accent colour reserved for "look here".
- Tasks, not features. Each chapter and section states its goal up front: the title names the task and one line says what the reader will be able to do - no "Objetivos" box.
- Chunk dense information into small steps and short blocks; never a long run of continuous text. Descriptive titles, subtitles, bold and numbered lists lead the eye.
- Scannable: the reader looks things up, never reads start to finish. Titles name the task in the reader's words, each section stands alone, the answer comes first.
- Clickable table of contents, a way back to it from every page, and links between related sections wherever a task continues or depends on another ("siga en 2.4"). A note stays with its figure; a title never sits alone at the bottom of a page.

**Sanitizing**
- Replace anything real: user names (a plausible invented person, not "QA"), e-mails, customers, agents, device or account identifiers, sensitive amounts. Use obviously generic values ("AGENTE1", "MEDIDOR 1") and keep the same example data across all figures.
- Check half-visible rows at the image edge and dimmed content behind dialogs. Remove personal browser details; redraw system dialogs in the document's language.
- Tell the user what you replaced and with what.

## Output

Unless asked otherwise, produce a PDF for reading and an editable source (Word or the HTML it was built from).

Deliver a finished document: no placeholder text, no "screenshot goes here" boxes. If something is missing (a capture, a fact about how a control behaves), finish everything else and list what is missing in your message, not inside the document.

When reviewing someone else's manual, go through `references/checklist.md` and report findings ordered by how much they hurt a reader who does not read - not as a list of style remarks - and include the corrected version.
