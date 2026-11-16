# Review checklist

Run this on the rendered document (the PDF or the page as the reader will see it), figure by figure. Each item is phrased as the failure to look for.

## Each figure

- **Step without a picture.** Does every step have its own capture with a mark? A step with text only is a defect - add the capture or ask for it.
- **No cue.** Is there a screenshot with no rectangle, arrow or highlight? The reader has to search.
- **Mixed moments.** Does the picture show a state the reader has not reached yet at this step (a confirmation, a filled field, a later notice)? Split it into consecutive figures.
- **Mark off target.** Zoom in. Is every rectangle centred on its control, with the same margin on all sides? Is anything covering a label?
- **Decoding required.** Are there numbers or letters on the image that send the reader to a legend? Replace with a rectangle, or with a card joined by an arrow.
- **Instruction looks like product.** Could a reader mistake your text for part of the screen? Move it outside the screenshot into a card; give the screenshot its own frame.
- **Too much in one figure.** Does a figure with lettered cards include an action that is not trivial (opens something, needs a note, has a result to check, cannot be undone)? Give that action its own step.
- **Legend below.** Is there a list under the figure explaining its letters or numbers? Move each text beside its part (arrow, or text next to the marker) and delete the list.
- **Unbalanced.** Are the cards different widths, misaligned or piled on one side? Do arrows run diagonally where one elbow would be cleaner? Does card order follow left-to-right reading?
- **Said twice.** Is the instruction in the card repeated as a list below? Keep one.
- **Unreadable.** Can you read the button labels at print size? Crop tighter or give the screenshot more width.
- **Cut elements.** Is a logo, row or control sliced by the crop?
- **Arrows.** Do they run in reading direction, stay short, and avoid crossing other controls?
- **Real data.** Any real user, e-mail, customer, identifier or amount - including half-cut rows and dimmed backgrounds?
- **Wrong language.** Any screenshot or dialog in a language other than the document's?

## Each step

- No narration words (Primero, Luego, Después, Por último / First, Then, Finally): a letter or number and the instruction.
- One action only ("review and send" is two).
- A step that fills a field names the field and says how: typed, chosen from a list, picked from a calendar. No "complete the data".
- Starts with the verb; the same verb is used everywhere for the same kind of action.
- Control names in bold and spelled exactly as on screen.
- Screen and window names in quotation marks (la pantalla "Nuevo gasto"), not bold.
- One short sentence; extra detail moved to a note.
- No theory or "why" inside a step: context and warnings sit before the steps.
- Examples are in italics after the instruction, never in the step's own style.
- States what the reader will see, where that is not obvious - and a figure shows it.
- Actions and results look different: actions are numbered, results are not.
- Claims nothing the system does not guarantee.
- Any warning comes before the action it affects.

## The words

- Every sentence passes the deletion test: without it, the reader would act differently.
- No announcing or padding ("a continuación", "simplemente", "proceda a").
- Where before what; condition before action.
- One name per thing, one verb per kind of action - checked against the term list.
- Steps and titles are parallel in form.
- Example data is the same in every figure.
- One register throughout, and it is the one the client uses (formal or informal) - confirmed, not assumed.

## Each callout

- Is it labelled for what it is? Advice = Tip. Clarification = Note. Risk = Important. Recovery = If you see something different (a calm title, never "If something goes wrong").
- Does it carry its icon (warning sign = Important, light bulb = Tip), the same one everywhere? Several points inside are bullets, not a paragraph.
- In "If you see something different", is each case visibly separate from the next?

## The document

- Organised by task, with chapter names matching the product's menu.
- Numbered sections; titles large enough to find while flipping.
- No two tasks repeat the same opening steps: shared starts are written once (a fork, a section of its own, or "same as X, but...").
- One numbering per level: steps use numbers, sub-steps and figure cards use letters. No two sets of 1-2-3 on the same page.
- White space: wide margins, space between paragraphs and around figures, line spacing 1.5-1.7.
- The accent colour is used only for "look here".
- Clickable table of contents, and a way back to it from every page.
- Scannable: every title names a task in the reader's words; a reader landing on any section can do it without the previous ones.
- Related sections are linked where the reader needs them, by name and number.
- Each chapter and section says up front what the reader will be able to do: task title plus at most one line. No "how to read this manual", no objectives or prerequisites boxes, no restated introductions.
- Nothing announces the obvious: no "there are N steps", no summary list of the steps before the steps.
- No placeholders or unfinished parts.
- No section title alone at the bottom of a page; a note and its figure share a page.
- The cover says who it is for.

## Captures and corrections

- Every capture was taken with the reader's role; any that was not is flagged.
- The same screen looks the same in every figure (no old and new capture mixed), or the exception is reported.
- After a correction round: the change was searched for and applied everywhere it impacts (see `revisions.md`).
