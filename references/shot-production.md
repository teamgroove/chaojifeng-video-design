# Shot production planning: plan first, then implement

Applies to product, explainer, news, image, story, feature, brand and music videos. This organises content, tools and assets; it is not a new scenario, and not a process exclusive to generative models. With [creative direction](creative-direction.md), fix the through-line, the aesthetic boundary and the key events first; expand this reference for complex tasks, and keep only the necessary decisions for simple ones.

## Choose the production route by real capability

Write the key expression as “shot intent → available route → capability evidence / unknown → smallest test → resource ceiling → alternative”. Along the existing project, choose components, drawn code, screenshots, screen recording, existing media or an approved generative tool; look first at which one preserves fidelity and delivers the intent best. The division of labour here is production responsibility; it does not automatically authorise multiple models, multiple agents or spending.

Keep documented claims separate from what was actually tried on this machine; record the outcome as verified, unverified or currently unavailable. Fields and real run state still follow the [plan contract](plan-contract.md); do not write untested capabilities into verified capabilities. For tool APIs, inputs, limits and how to pass references, consult current documentation under the host's rules — do not settle it from a name or an old memory.

For a route you are not yet familiar with but that looks promising, pick one small sample inside the existing authorisation and resources that can settle the risk. Check the actual result, then decide whether to stay with it, layer it, split the shot, change the angle or replace it; do not mechanically repeat a failing call. A test is an internal quality check — add no confirmation gate the user did not ask for. For asset reuse and serialised heavy jobs see [runtime and delivery](runtime-and-delivery.md).

For characters, 3D and cinematic camera work, write the shot, the expression/pose, the camera move and the final pose before any object is created, recorded along the existing IDs; design spatial lighting, material reflection and subtitle clear space together. Per [scene and tool composition](scene-tool-composition.md), allocate Blender, Three.js, Remotion and delivery responsibilities — one alone or several combined is allowed; the concrete executor is decided by expressive payoff, existing capability and resources, and a full toolchain install is not mandatory.

## Let each reference do its own job; separate the fixed from the varying

In the project notes, link the existing asset IDs, version/hash and the shots that use them, and state exactly what the reference is responsible for. Take the rows below as the task needs them; not every film has to produce character sheets or an image-generation style sheet.

| Reference's job | Must stay fixed | May vary — and must be re-checked |
| --- | --- | --- |
| Person / subject identity | required appearance, name, relationships and the basis for identity | pose, action, camera position and environment may vary; actually check identity across shots |
| Product / information evidence | real interface, state, data, units and source | focus and layout may vary; capability, result or the meaning of a ratio may not change |
| Composition / space | required relative positions, eyelines and handoff positions | shot size, crop and lens vary by intent; check direction and occlusion |
| Style / world | the colour and light, materials, type and sound character agreed for this film | vary by section; change must have a purpose, not drift |
| Action / time | key before and after states, feedback and the actual anchors | timing and motion follow the expression; re-check cause and effect and the seams |

Reference images, source code and the original video are all material; passing a reference in does not prove identity or style is locked. Record what was actually read, watched and auditioned. Read only assets that are relevant and permitted; avoid unbounded traversal of all private material.

## Asset workability before any specific motion promise

When an existing image or piece of media has to be cut apart, pushed out of frame, recomposed or used across shots, use [asset performance and routing](asset-motion-direction.md) to check the complete unit, the source-to-scene coordinates, occlusion and exposed background, and reuse the parts already prepared. Keep the content intent first, then correct the motion to the range that is actually workable; a correct static put-back still needs the maximum motion checked. Complex tasks can use the [asset stage note](../templates/asset-stage.md), recorded along the existing IDs, without adding required tracks or an automatic layering dependency.

## Write each shot's production task before generating or capturing

Record the following decisions along the existing scene, element, beat, asset and continuity IDs; they can sit in purpose, intent, direction or the shot notes — these are not new required JSON fields.

- What information or feeling this shot adds, where the basis comes from, and which subject carries the change.
- The state on entry, the key action, the state on exit, and how the next shot catches it.
- Point of view and primary motion; secondary response, settling and reading window; who controls the same property.
- Which reference is used, and whether it constrains identity, composition, style or action; the parts that must be kept and the parts allowed to vary.
- Position and appearance time for the subject, exact copy, subtitles, annotations, data and decoration; sound's job and the existing time anchors.
- The actual production route, risks, alternatives, scope of observation and acceptance conditions.

One clear primary motion helps reduce conflicts, but it does not forbid a planned compound shot. Split generative shots into segments according to what the tool can actually do, and state in the prompt the subject, action, point of view, what each reference is for, the consistency choices and the necessary constraints; do not invent supported parameters or fix a duration per segment. Code, screen recording and live-action footage equally need start and end states, copy space and seam planning.

## Copy is part of the composition from the start

Decide first whether the copy is the protagonist, an evidence label, an explanation or a quiet subtitle. When important copy needs presence, make the background and the motion yield attention, and schedule a readable dwell; content the image can already explain can carry less copy. Decoration must be able to say how it relates to what is on screen — when it piles up, delete first.

For titles, data, lyrics and annotations that must be exact and revisable, choose a controllable edit layer according to capability; a native editor, HTML, SVG or an existing compositing route all work — JavaScript is not fixed. The generated plate and the exact copy can be separated, but a real product interface may not be redrawn as a fake and passed off as evidence. Necessary copy inside existing media can be kept as it is; actually re-check its legibility and its source.

When copy and subject conflict, change the composition, the shot size, the information density or the entry timing first — do not just shrink the type. Check the actual viewing size, landscape versus portrait, motion and subtitle changes; a correct static keyframe does not prove the whole section is readable.

## From a single shot to the whole film

Lay out sound and picture on the same valid time basis, and keep source-media time distinct from whole-film time. You can test the hardest relationship and the key seams first, then finish the film; when direct is explicitly asked for, make the whole film straight through, checking and reworking inside the run, with no mandatory test cut and no waiting for approval. An internal sample does not replace final delivery. For key-expression delivery and cross-section checks see [review method](review-and-revision.md).

Once a problem is located, replace only the affected section or component and keep the old version for comparison; after the swap, re-check identity, direction, colour and light, copy, safe area, sound tail and downstream timing in the shots before and after. Emit the necessary versions along the real executor's output; do not rebuild a similar environment for every local revision. Record watched, heard, structurally checked and not yet verified separately.

## Music and generation branches enabled by the task

These conditions are not hard-bound to a film-type name. Honour them whenever a task explicitly locks the original audio; consider lip sync only when a task involves a person speaking.

- **Original audio untouched**: when the user explicitly asks to keep the original track or original sound unaltered, keep the original source, version and hash, and do not crop, reorder, change speed, mix in new sound or change level on your own; if the output encoding unavoidably makes a difference, record the real processing and the gap, and do not claim the audio bytes are identical. If a required sound requirement conflicts, say so first. Ordinary product scoring continues to pick segments per [music direction](music-direction.md) and does not switch this constraint on.
- **Songs and lyrics**: when there are lyrics, check the source and completeness; if it is unclear, do not invent. For song sections, key lyrics, onomatopoeia, stresses and pauses, separate measured, human-judged and estimated, and link them along the existing beat/sound contract; for instrumental music work by motif, timbre and section, and do not force lyrics onto it.
- **Lip sync and generation references**: only when the task needs it, investigate whether the current tool supports the relevant reference and verify the sync; do not assume it works because the prompt mentions it. When the user restricts models, hold the boundary first and let a substitute shot carry the expression.
- **Interactive playback page**: consider chapters, overlay toggles, fullscreen, buffering and debugging only when delivery needs them; verify the real clock, preload and seeking against the executor. An MP4 task does not require a separate player, and the existence of a web page does not prove a complete export.
- **Extra deliverables**: standalone shot assets, bilingual documents or an interactive page as this job needs them; deliver the actual film, the necessary sources and the verification along the existing contract. Verify asset usage and public-release permission against the host's rules, and do not derive publishing rights from creative autonomy.

The general method comes from an MV creation prompt the user supplied on 2026-10-18, adapted originally after the user explicitly confirmed it applies as general guidance for agent video creation; the author and the public entry point are unknown. Only the necessary method is kept here; the full source prompt is not packaged into the skill. Design instructions, tool documentation and structural checks do not prove the quality of the actual work.
