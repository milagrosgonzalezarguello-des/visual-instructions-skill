# Writing rules: clear, concise, consistent

Read this before writing or editing the text of a manual. Each rule has a before / after, because the pattern is easier to copy than the principle.

The examples are in Spanish; every rule applies the same in English ("In **Period**, select the month. Then select **FILTER**."). Words to cut in English: simply, just, basically, please, in order to, proceed to, click on the X button (-> select **X**), it is important to note that, as shown below.

## Clear

**Where first, then what.** Tell the reader where to look before what to do, in the order their eyes move.
- Before: Select FILTRAR after choosing the period in the Período field.
- After: 1. En **Período**, seleccione el mes. 2. Seleccione **FILTRAR**.

**Condition first.** If a step only applies sometimes, open with the condition, so readers it does not apply to can skip it.
- Before: Seleccione **Ver errores** si el archivo fue rechazado.
- After: Si el archivo fue rechazado, seleccione **Ver errores**.

**Active voice, addressed to the reader, present tense.**
- Before: El archivo deberá ser seleccionado por el usuario.
- After: Seleccione el archivo.

**Say what to do, not what to avoid** - unless avoiding it is the point (then it is an Important).
- Before: No deje el campo Fecha sin completar.
- After: Complete **Fecha**.

**Plain, everyday words.** The word the reader would use, not the system's or the developer's: "archivo" not "recurso", "enviar" not "transmitir", "elegir" not "parametrizar". Explain an unavoidable technical term the first time, in a few words.

**Concrete over abstract.** Name the thing, give the value, show the example.
- Before: Ingrese los datos correspondientes en el formato adecuado.
- After: En **Fecha**, seleccione el día en el calendario.

**One idea per sentence.** If a sentence has "and", "which" or a comma followed by another verb, it is probably two sentences.

**The product's words, not yours.** If the screen says "Envío de Archivos", never write "carga de archivos" or "subida". Internal names, code names and abbreviations the reader never sees on screen stay out.

## Concise

Cut, in this order:

1. **Sentences that announce.** "A continuación se describen los pasos", "Son 4 pasos", "Como se muestra en la imagen", "Es importante destacar que".
2. **Words that soften or pad.** simplemente, básicamente, por favor, deberá proceder a, a fin de, con el objetivo de, en caso de que (-> si), realizar la carga (-> cargar), hacer clic en el botón X (-> seleccione **X**).
3. **Words that repeat the picture.** If the figure shows the button, the text does not describe its colour or position.
4. **What the reader already knows.** What a login is, that they need internet, why the system exists.
5. **Anything said twice.** Once in a card and once in a list; once in the intro and once in the step.

A test for every sentence: if it disappeared, would the reader do anything differently? If not, delete it.

Typical lengths: a step is under 15 words; a callout under 30; a section intro is one sentence or none.

## Consistent

Readers treat any difference as meaningful. If two things differ in wording or look, they assume they differ in fact.

- **One name per thing.** The same screen, button, file or state is always called the same, everywhere - text, figures, captions, table of contents. Keep a short term list while you write (thing -> the one word you use) and check the document against it at the end.
- **One verb per kind of action.** Choose once and keep it: one verb for acting on a control (seleccione), one for typing (escriba), one for dragging (arrastre). No synonyms for variety.
- **Parallel structure.** All steps start with a verb in the same form. All section titles have the same shape (all infinitives: "Cargar un archivo", "Descargar el resultado" - not one infinitive and one noun phrase).
- **Same pattern for the same situation.** If one "choose from a menu" step has a figure with a rectangle, they all do. If one section ends with "Verá:", every section whose result is not obvious does.
- **Same format for the same kind of thing.** Control names always bold. Screen names always the same style. Dates, numbers and units always written the same way. Example data (the invented user, the sample file) identical across all figures, so the story holds together from page to page.
- **Same register.** Formal "usted" or informal "vos"/"tú" - one, from cover to last page, including figures and callouts.

## Steps

- **Context before, action inside.** Why the task matters, when it applies and what can go wrong are said before the steps - in one sentence or a callout. The steps hold only actions. Not "3. Seleccione **Validar**, ya que el sistema necesita comprobar el formato antes de procesar"; instead a note above ("El sistema comprueba el formato antes de procesar.") and "3. Seleccione **Validar**."
- **No narration.** Not "Primero, seleccione X. Luego, complete Y. Por último..." - sequence words are padding once the items are numbered or lettered. Write "a. En **Monto**, escriba el importe." "b. En **Categoría**, seleccione una opción de la lista desplegable."
- **Start with the verb**, imperative, in the organisation's register. One short sentence; detail only some readers need goes in a note.
- **Control names exactly as on screen, in bold.** The reader matches shapes, not meanings.
- **Screen and window names in quotation marks, with the word that says what they are:** la pantalla "Nuevo gasto", la ventana "Mis registros" (the "New expense" screen). Not bold: bold is only for what the reader acts on (buttons, menus, fields), so a glance tells the two apart. Write the name exactly as its title appears on screen and use one kind of quotation mark throughout (" " or « »).
- **Name the field and say how the value goes in.** The kind of control decides what the reader does: *escriba* the amount in **Monto**, *seleccione* the category in the list **Categoría**, *seleccione* the date in the calendar of **Fecha**. Never "complete los tres datos". Read the control type off the screenshot (a dropdown arrow, a calendar icon); if you cannot tell, ask.
- **Say what they will see, and show it.** After an action whose result is not obvious, add "Verá: ..." - and a figure where that result is visible and marked. A result described but not shown is not understood. No capture of that state? Ask for it.
- **Actions and results look different.** Actions are the numbered steps. Results ("Verá:") are un-numbered, in their own style, under the step that causes them. Never number a result; never bury an action inside a description.
- **Examples look different from the instruction.** An example is not something the reader must do, so it must not look like the step. Put it after the instruction, introduced by "Por ejemplo:" / "For example:", in italics (`.ex` in the template): "En **Fecha**, escriba la fecha del comprobante. *Por ejemplo: 05/11/2026.*" Never bold - bold is for control names. The same style for every example in the document.
- **Warnings before the action.** A condition or risk read after acting is too late.
- **Only what the system guarantees.** If it validated a file's format, say "validado", not "procesado".
- **What a control really does, not what its name suggests.** Unsure whether a button keeps or clears the filters? Ask before writing it. A confident wrong sentence is worse than a question.
- **Follow the task outside the product.** If it continues in a result e-mail or a downloaded file, show that too, from a real capture.

## Structure that reduces effort

- **Chunk.** A procedure of more than about seven steps is split into named parts ("Complete los datos", "Adjunte el comprobante"), each with its own short run of steps.
- **Most common path first.** Describe the normal case straight through. Variations and exceptions go after it, under their own heading, not woven into the steps.
- **Just in time.** Give each piece of information at the moment it is needed: a file-format rule goes right before the step where the file is chosen, not in an introduction three pages earlier.
- **Name things before using them.** If a step needs a term the reader may not know, explain it in the same place, in a few words - not in a glossary they have to visit.
- **Let the reader confirm.** After the steps that matter (sending, saving, deleting), say and show what confirms it worked.
- **Scannable.** Headings a reader can find by flipping; the first words of each step carry the action; tables for anything with two dimensions (state -> meaning, problem -> what to do).

## Scannable: built for looking things up

Nobody reads a manual from start to finish. The reader arrives with one problem, looks for the section that solves it, and leaves. Design every part for that visit.

- **Tasks, not features.** Organise by what the reader needs to get done ("Cómo configurar una alerta", "Cargar un archivo"), never as a tour of the system's functions or screens.
- **The goal is clear at the start - in the title and one line.** Each chapter or section opens by telling the reader what they will be able to do: the title names the task, and at most one sentence under it says what it covers ("Cómo consultar las mediciones que faltan en un mes."). That sentence is the objective. Do not add an "Objetivos" / "Al terminar usted podrá" box or a prerequisites list - they delay the first step and nobody reads them.
- **Titles say the task in the reader's words.** "Descargar el Excel de faltantes", not "Exportación" or "Funciones adicionales". If the reader would search for it, that word is in the title.
- **Each section stands alone.** Someone who lands on 3.4 from the table of contents must be able to do it without having read 3.1-3.3. Say where to start ("Abra **Historial de Archivos** (3.1)") instead of assuming they came from the previous page.
- **The answer comes first.** Steps before background; the rule before its explanation. Context that only some readers need goes after, in a note.
- **Entry points everywhere.** A clickable table of contents listing every task; a way back to it from every page; in a long manual, a one-page quick reference with the most used tasks and where each is explained.
- **Links between related sections.** Wherever a task continues, depends on, or is easily confused with another, link it right there: "Luego verá el resultado: siga en 2.4", "Para ver los rechazos, consulte el **Historial** (capítulo 3)". The link names the section and its number, so it also works on paper. Never "ver más arriba" or "como se explicó antes".
- **The eye finds things by shape.** Numbered steps, bold control names, tables for anything with two dimensions (state -> meaning, problem -> what to do), and callouts that always look the same. Paragraphs are where information goes to hide.
- **Problems are findable.** Recovery cases sit next to the task they belong to, phrased as what the reader sees on screen ("El botón CONTINUAR no responde"), not as causes.

## White space

- Wide page margins; text lines no longer than about 80 characters.
- Space between paragraphs, more space before a heading than after it, and clear space around every figure and callout.
- Never shrink spacing to fit one more step on a page - let it flow to the next.
- Line spacing 1.5 to 1.7 for anything that wraps.

## Accessible

- Never rely on colour alone: a red rectangle also has a shape; correct / incorrect also have a check and a cross.
- Text contrast high enough to read when printed in grey.
- Every figure has an alt text that says what it shows.

## Structure: shared beginnings and numbering

**Do not repeat a shared beginning.** Before writing, lay the tasks side by side. When two or more start with the same steps (open the same screen, apply the same filters), write those steps once, whichever way is shortest for the reader:

- *Shared start, then a fork:* one run of common steps, then "Para descargar: ..." / "Para ver el detalle: ...", each branch with only its own steps.
- *A short section of its own:* "2.1 Abrir Envío de Archivos"; later tasks begin with one line - "Abra **Envío de Archivos** (2.1)".
- *A variation, not a second procedure:* write A in full and B as "Igual que 2.3, pero en el paso 2 seleccione **ZIP**".

This does not contradict repeating a screenshot inside a task: within one procedure, repeat so the reader never looks back; across procedures, do not make them reread what they already did.

**One numbering per level.** If the main steps are 1, 2, 3, anything inside a step - sub-steps, the cards of its figure - uses letters (a, b) never a second series of numbers. Two series of numbers on one page make the reader ask "which 2?". Section numbers look like section numbers (2.3), step numbers like step numbers.

**A single task has one series of numbers.** In a short guide for one task, the parts ("Complete los datos", "Adjunte el comprobante") carry a title but no number, and the steps count straight through from 1 to the end. "Part 2, step 1" next to "Part 1, step 1" is two series again. Numbered sections (1.1, 1.2) are for manuals with several tasks, and there each task restarts at step 1.

**Keep together what is read together.** A note and the figure it introduces share a page; a section title never sits alone at the bottom of a page.
