# Settle why the film holds, in the first pass

These methods are a working contract distilled from published director interviews, production retrospectives and video cases, not a fixed tutorial from one director. Make the judgement first, then pick the effects. A simple task needs three sentences in the same plan: what the audience turns from and into, which line runs through, and how sound and image finish it together. Expand the rest of this page for a complex task; five separate extra documents are not required.

## Intent and through-line

Write down the target audience, the start and the end of their viewing, and the one feeling most worth keeping. The through-line can be a question, a task, the same unit of information, an object, a character's choice, a visual motif or a sound motif. It should explain why the shots connect; it cannot be only the title or "cool, futuristic, striking".

Choose a fitting structure and give the reason: task progression, question and evidence, comparison, progression in time, cause and effect, imagery, or musical sections. These can combine; three-act, a fixed shot count, a twist or character conflict are not required. In news, verification comes first; in knowledge, the relationship; in product, the real operation. A brand film may let mood and imagery lead, and a music film may let sections and variation lead.

A tech feel comes from rules that belong to the content. For example state responses with precise timing, an intelligible spatial hierarchy, consistent material and type, and sound that establishes a clear scale. "Dark, particles, neon" alone does not say why it suits this product. Where a tech feel conflicts with goals such as warmth or ease of use, state the trade-off and test it with the actual image and a listening pass.

## Setting and mission of elements

Give the key elements a stable identity and a duty, instead of anthropomorphising every element.

| Element | Mission it can carry | Must be preserved |
| --- | --- | --- |
| Figure / character | Point of view, choice, obstacle, action, the one affected | Identity, relationships, necessary appearance, spatial direction; the inner life of a real person cannot be invented |
| Product / interface | Carries the initial state, the trigger, the feedback and the result | Version scope, real operation, content and evidence |
| Object / symbol | Connects shots, shows a state or carries a motif | Shape, proportion, rules of change and the meaning it must carry |
| Chart / concept / information unit | Evidence, scale, comparison, process and condition | Source, unit, direction and the boundary within which it holds |
| Sound / musical motif | Signals point of view, expectation, reveal, memory, section and release | Source, usage rights, timing and hierarchy |

A character story writes goal, obstacle, choice and cost as needed; a product or knowledge film can leave character psychology out entirely. The cross-shot object's continuity_key corresponds to visual continuity; the stable ID in director.entities corresponds to the duty carried across the whole film. Neither is an automatic identity lock — you still have to check the image.

## Each shot's job and the shot language

Write first what the audience gains in information or feeling before and after this shot. Then decide the subject, shot size, camera angle, light, movement and dwell. An establishing shot sets the space and the relationships; a detail shot gives evidence; a reaction shot carries the consequence or the understanding; a held empty shot lets a feeling settle. Not every film needs all of these types.

A camera move needs a purpose: push in to make evidence visible, pull back to reveal the environment or the scale, follow to hold the same unit, truck to release information that was hidden. A complex move that brings no new information can become a stable cut or a smaller move. Opening and closing composition, eyeline, direction of movement, subject position, shape or sound can carry the handoff; not every seam needs a hard transition.

scene.intent can record: the story beat it answers to, viewer_change, the focal entity, reveal_order, camera.purpose, handoff, acceptance. The reveal order references this shot's element.id; the focal entity references the film-wide director.entities. These fields in the plan record a choice; they do not prove the audience actually understood.

## Two legitimate production routes

**Precision route** suits product steps, settled data, complex space, and voiceover under time pressure. Lock the facts, the identities, the key states and the sound-and-image durations first, then produce.

**Exploratory route** suits imagery, performance, brand atmosphere and music films. Lock the intent, the identities, the key beats, the necessary facts and the resource ceiling first, and allow sketches, tests and the rough cut to find better connections. A satisfactory accident can be kept, but it must not distort knowledge, the product or a real person.

Both routes can adjust after the rough cut. You may test the hardest shot or the critical seam first; when the user has explicitly asked for a single pass, direct to the finished film, or no test cut, produce the whole film and check and rework it internally — do not insist on a test cut first or wait for a mid-point confirmation. When generation keeps failing, split the shot, add layers, change the angle, or let sound carry the connection. Record why a candidate was chosen, the alternate shots and any intent left unfulfilled. The number of explorations, the cost and the time obey the user's authorisation and the available resources; there is no unlimited retry.

## Stopping and review

The stopping rule should be that the key intent is fulfilled, the required content has no blockers, the film plays and the acceptance gaps are stated — not "it has been generated many times". Take a quality problem back to the specific scene / entity / beat: which relationship is unreadable, where the reading window is too short, which sound covers the information. When the user only changes the palette, do not rewrite the story on your own; when the reveal order changes, re-check the neighbouring shots and the sound.

Sources and the boundaries of what applies are in [sources.md](sources.md). A director's personal aesthetics, working hours, fees or opinions about the models of the day are not general requirements.

## Product tasks and section evidence

A product film starts with [Product expression](product-expression.md): how one task goes through operation and process to a real output. The escalating difficulty and the claim/evidence sections of `product-task-proof` are optional branches only; do not force the old method to fail, a fixed player, a uniform shot count or a fixed fast/slow ratio. Mark each shot's evidence role, let important phrases map to visible elements, and choose the ending by purpose — value, brand, or a next step the viewer can take.
