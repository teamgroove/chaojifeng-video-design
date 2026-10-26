# Asset selection: decide first what it must prove or perform

For every shot, write what the viewer gains first, then choose existing assets, capture, generation or programmatic construction. A shot can mix several asset types; a reliable source, permitted use, editability and fitness for this shot are separate judgments. Read [Asset motion and routing](asset-motion-direction.md) when assets move independently.

## Choose the source by the shot's mission

| What the asset has to do | Where to look first | Boundary of generation and construction |
| --- | --- | --- |
| Prove product capability | A runnable entry point of the current product, real screenshots / controlled screen recording, actual output; check current behaviour and limits in the source | Generated UI, old screenshots and localized strings do not on their own prove current capability; a rebuild cannot invent features |
| Show a real event | The party's own original release, official footage / archives, on-site material the user has cleared; verify original time, place and context | Generated imagery is explanatory re-creation or background only; it cannot stand as visual evidence that the event happened |
| Understand the user's context | Notes, comments, interviews, user material and existing research you are cleared to read | Extract tasks and phrasing; having seen a reference is not clearance to use it in promotion, and a failed read leaves the gap open |
| Build a life and brand world | User / project assets, the local asset library, sources whose use and license match | When no matching asset exists, generate fictional people, environments, textures, objects and decoration; do not pass them off as customer feedback |
| Carry an editable performance | Editable source, detached subject, complete background, mattes and motion headroom | Generate the missing parts when needed; the programmatic layer controls exact text, coordinates, state, occlusion and timing |
| Narration and sound | Cleared audio tracks, clean sound references, actual voiceover, music excerpts and original SFX | Generate what is missing within actual capability; file ready, read correctly and passes the ear are separate |

For real events, find a first-hand source first; when several candidates exist, weigh relevance, creation / modification time and source credibility together, and use available engagement data only as same-metric support. If a source's time or statistics are unknown, record unknown — do not fill in 0. When you put a time on screen, use the time the event happened; upload time cannot stand in for it.

## Finished assets first, build only the gaps

Before modelling, rigging, animating or painting textures, check in shot-task order the project / user's existing assets and cache, then finished-asset libraries whose use and license match; prefer adapting existing models, rigs, motion and materials, and generate or hand-build only for the gap. Do not skip the search just because you could build it yourself, and do not change a confirmed story to suit some asset. Factual evidence still takes the real-source route in the next section; creative assets cannot backfill a historical scene.

For characters check proportions, rig, skinning, facial control and editability; for motion check retargeting, foot contact, hand / prop contact and rhythm; for environments and materials check scale, UV / maps, engine compatibility, reflections and how they read in the actual shot. In the assets row of the [tool contract](production-tool-contract.md) record candidates, reasons for choosing / rejecting, the source-to-derivative chain, scene references, license and the actual file hash; when building or generating from scratch, state what you actually searched and what remains unmet. Record a blocked search honestly; do not retry library after library.

Poly Haven: check HDRI, textures and prop models first; if the Blender MCP has an integration for that library, verify its state first, then search previews and specs, select and import; if the MCP is unavailable you may check public metadata within host capability, but do not write that up as MCP import. Motion sources such as Mixamo are checked separately for actual license and fit; an environment library is not a complete character-motion library.

## Factual imagery: search first by default

This is an actively enforced rule: when people, events, places, historical archives, product behaviour or statistics need concrete imagery, reuse the user / project's existing real material first, then look up original releases, official archives, credible reporting and asset libraries whose use matches. Do not default to generating an image without searching. Use the host's designated browser route for site search, access and capture; on this machine the current rule is a task-dedicated @Chrome reusing an existing session — on failure do not switch to another browser or desktop capability on your own.

Record in the existing asset list or the project research notes: claim / scene ID, query terms and the sources actually covered, candidate original entry points, event time and publication time, context, rights and permitted scope, resolution / crop conditions, reasons for choosing or rejecting. Use available creation / modification times and same-metric engagement signals to support the comparison; unknown stays unknown, do not fill 0. Thumbnails, reposts and search previews are leads only; being publicly visible does not mean downloadable or reusable.

Set a stopping condition from this shot's necessary information and resource budget: once you have a verifiable, usable candidate, stop widening the search; when the source does not exist, is restricted, or no candidate fits, record the actual gap — do not promise you "searched the whole web". You may switch to charts, timelines, maps or text driven by verified facts; generate non-evidence imagery only when you need environment, objects and an emotional carrier. Do not use generated people, on-site photos or product screenshots to backfill facts that did happen. When there is no honest viable expression, change the shot or narrow the claim.

## Decide source and performance separately

Search / generation decides where the asset comes from; motion decides how it performs; the two can be used together. For each shot fix the subject, the exact text / data layer, background, main action, settle and handoff to the next shot, then choose an executor by spatial need, degree of control, existing implementation, editing cost and resources. Reuse an existing project when you can; do not pull in several engines at once to pile up effects.

Remotion, Blender, Three.js, HyperFrames or an existing editor are implementation candidates only; this method does not promise any version's API or untested capability. Before using one, check the current docs and the hardest motion. Cut on subject, shape, direction, scale, causal state or sound; land the key result first, then cut away. Stagger the main action against supporting motion — particles, lyrics, camera; do not rely on full-frame change on every beat for immersion.

When you need characters, 3D scenes, world lighting / reflection and cross-tool compositing, assign responsibilities per [Scene and tool composition](scene-tool-composition.md). Poly Haven and the like supply environments and assets; lighting, materials, camera and performance still have to be designed; the priority of real factual material does not change because the route is 3D.

## Check performability before generating assets

"A card flies out of the phone" needs a card that can move on its own, a phone / background that can be restored, and a text layer; "the subject orbits" needs a check of what shows underneath and what occludes at maximum displacement. Plan the parts along the shot's entry state, main action, exit state and handoff to the next shot, instead of first generating a poster with subject, text and background fused together and then promising arbitrary motion.

State each reference's job separately for identity, composition, style and motion, and keep fixed and variable items per [Shot production](shot-production.md). When a complete existing asset is enough, use it directly; do not force every image to be split into layers. When you generate a still and then add parallax or perspective, describe it by what was actually implemented; do not claim you generated continuous character performance or true 3D.

## Connect capabilities through general artifacts

| Example capability | What the director layer gives it | What it should return |
| --- | --- | --- |
| Local asset search, e.g. Eagle | Shot mission, identity and style conditions | Candidate local files, source / rights information, asset ID |
| Platform capture capability | The specific audience question, topic and actually accessible scope | Original entry points, verbatim quotes, times and candidates; an explicit gap when nothing turns up |
| Asset parsing / reuse capability, e.g. media-use | Asset responsibility, timbre or picture conditions | Readable files, metadata and a source ledger |
| Host image generation | Subject / background task, reference roles, fixed items, aspect ratio, negative space and motion headroom | The actual generated image, necessary alpha layers, generation record and derivative relations |
| Voiceover / song generation | Checked script, read, sound's job and demo target | Real audio, obtainable stems and a basis for timing — do not invent stems |
| Scene and media executor, e.g. HyperFrames or an existing editor | Objects, states, time, text and seam agreements | Editable source, preview and actual video |
| Motion research capability | The observable motion to solve and a comparison target | Neutral motion principles, an original implementation and failure conditions |
| Media processing capability, e.g. FFmpeg | Exact source in / out points, target format and relation to sound | Actual derivative files, parameters and verification record |

These are optional responsibility interfaces; they do not require installing a Skill of the same name or a fixed vendor. Probe capability and authorization per the host's current documentation. Connect through asset lists, scripts, real audio, schedules and the project — do not hardcode personal absolute paths, and do not inherit another Skill's default write targets, fees or publishing permissions.

Ordinary image tasks follow the host's default generation entry point; in Codex prefer the built-in image generation and verify that route only when the user explicitly chooses the CLI. Keep program-native text, annotation, geometry and state editable where you can; disclose models, references and actual tools as they are actually recorded. Reuse the environment first; run media generation, recognition and rendering serially per resource conditions, not with unlimited concurrency for a batch of assets.

## Record sources along the existing contract

Assets keep using plan.assets' id, source, rights, status, path and optional sha256; shot notes add as needed purpose, fact time / version, identity constraints, the scene / element used, source-to-derivative relations and the permitted range of modification. Record purely programmatic objects as implementation; do not fake an image row. Keep original files, accepted prompts / parameters and derivative relations in the project's persistent directory, not only in a temp dir or the global generation cache.

The source record says where an asset came from; the evidence role says what it can prove. Asset collection success, model generation success and fitness on screen are accepted separately; file ready does not mean distributable.

## How re-creation and explanation enter the picture

Long-standing rule confirmed by the user on 2026-10-21: first distinguish, in a separate internal record, between real screen recording, manual re-creation, process diagram, creative metaphor and generated material; the source record does not automatically enter the public delivery. Outward picture, subtitles, voiceover, business prompts, file names, captions and attachments present business content directly — do not add production-identity labels such as demo, test, simulation, re-creation, for-display-only, and do not write a self-description that the work was made from some approach; do not keep them by swapping in synonyms or moving them elsewhere.

Bad: "the interface is a re-creation", "this video was made with framework X", "the figures shown are demo data only". Good: delete the pure production markers and present the task, action and result as verified; call the business input "July channel sales table" and keep the nature of the source internal. A normal "demo of how to create a task" or "this round of testing found the export fails" may stay — what you judge is production identity, not an isolated word.

Before generating, check the input and the task window; after generating, check the text and copyable prompts; after export, check the actual picture, subtitles and sound. When an upstream label lands in frame, fix the input and redo the related capture or export — do not cover the words instead of fixing the source, and do not pass a text check off as a pixel or listening pass. When a catalog or old reference demands that the picture disclose it is illustrative, record the production nature in the internal disclosure and do not render it as a label on the work; factual conditions and real model limits are still expressed with accurate content.

If the picture implies a false capability or a false event, prefer swapping in real evidence, narrowing the claim or changing the shot. Delivery notes, in-film notes and platform statements carry different jobs and cannot stand in for one another as done. Channel rules become rules only after you verify the specific platform, form and time; one user restriction does not generalize into a ban on every platform.

Method sources and untested scope: see [sources.md](sources.md#product-music-narrative-and-a-study-of-the-creative-process).
