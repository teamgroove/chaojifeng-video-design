# Composing 3D, compositing and delivery capability for the expression a scene needs

This reference enforces "shot intent → available route → capability evidence → minimal test → resource ceiling → fallback". It applies to the eight existing scene types; it does not set up a new subject-matter taxonomy, and it does not treat any engine as a precondition for all video. First decide what the frame must explain or make the viewer feel, then choose a single tool or a combination. On 2026-10-25 we read the designated repository's DeepWiki structure and Q&A and re-read the official source code / documentation below; documented capability does not mean it is wired up on this machine or that a test cut passed.

## Write the shot before creating objects

Along the existing scene / element / beat IDs, write clearly in the plan or the shot notes:

1. What the viewer newly gains in this shot, and which visible event proves it; record the basis for fact and for creative metaphor separately.
2. Shot size, composition, sightline and primary focus; the empty space subtitles and annotations need.
3. Character intent and change of expression, entry pose → main action → final pose; with no character, write the object's initial state and final state.
4. Camera start point, move, target of attention and settled composition; why the camera move helps understanding or feeling.
5. Key light direction, ambient light and reflection, material silhouette, background and light-dark relationship; keep highlights from covering subtitles, faces and action.
6. Sound anchor, action settle, reading / emotional dwell and the handoff to the next shot; execution frames derive from the single valid schedule.

An expressive character needs actual modelling or a suitable model, rigging / deformation, pose, expression and timing; camera moves also have to be authored and checked — tools do not produce performance on their own. Check silhouette, interpenetration, sightline, ground contact and focus first at low cost with the initial state, the motion extremes and the final state, then finish the continuous shots that are necessary. One handsome still frame does not substitute for character performance or for cinematic shot acceptance.

## Choose responsibilities by the expression required

| Expression task | Route to consider first | Composable parts and boundaries |
| --- | --- | --- |
| A character's expression, body, prop interaction and small-world story | Editable scene, skeleton / deformation and camera in Blender | Hand rendered shots to Remotion or an existing editor for precise text and sound; a model existing does not mean the performance is finished |
| An object / brand shot that needs material, reflection, spatial lighting and photographic composition | Blender, choosing Cycles or EEVEE by visual requirement and resources | Both can do final renders; do not treat EEVEE as preview only, and do not unconditionally specify high-cost path tracing |
| Geometry, spatial relations, particles, computable processes, data-driven 3D explanation | Three.js, or an equivalent procedural route the project already has | Can be combined with Remotion's frame time; 3D is not mandatory — if flat is clearer, use flat |
| Reusable assembly of real video / photos, titles, subtitles, charts and audio | Remotion Composition and Sequence, or an existing compositor | Real media can go in directly; a pre-rendered Blender video does not need converting into a Three.js scene first |
| 3D objects and React layout must work together in the same shot | A verified version of Remotion + `@remotion/three` / React Three Fiber | `ThreeCanvas` runs the 3D scene; it is not a tool that converts any `.blend` losslessly and automatically |
| Encoding, muxing, stream selection and adapting to the delivery format | The FFmpeg and probe tools currently available | Do not repeat lossy transcoding on an export that is already compliant; technical file checks do not replace watching and the listening pass |

The above are design choices formed from what each tool is responsible for, not a "single best" performance ranking. Prefer projects, assets, caches and running instances that already exist; add a tool only when the expressive gain is clear, and default to serial execution for re-renders, model jobs and media processing. Do not spin up three environments just because the process lists three engines.

## Common combinations, chosen per shot

- **Knowledge rap**: real archives / photos and verified charts carry the facts; use Three.js when a computable spatial mechanism is needed, and Blender for character or object performance passages as required; Remotion or the existing compositor unifies lyrics, music, shots and transitions, and FFmpeg comes last as delivery requires.
- **Character film short**: write the shot, expression, pose and camera move first; Blender delivers editable performance and lighting and outputs media per shot, the compositor organises subtitles, sound and the whole film; with no complex layout need you can deliver straight from the Blender project and not force Remotion in.
- **Product / brand film**: real operation and output stay as evidence; 3D object and material shots carry image and mood, graphics and titles stay controlled on editable layers, and a 3D metaphor must not pass itself off as a product capability that does not exist.
- **Mechanism / data explainer**: start with a clear relationship diagram and variables; use Three.js or Blender only where spatial relations really exist; exact labels, values and subtitles stay editable and share one source with the computation.

These combinations can be mixed within the whole film or within one shot. Shots hand off through subject, action, direction, scale, coloured light or sound — do not split the film into unrelated chapters by tool.

## HDRI, world lighting and reflections

[Poly Haven](https://polyhaven.com/license) is an optional source of HDRI, textures and 3D models, not a lighting engine. Its official licence page source and English body state that these assets use CC0, allow commercial use and redistribution, and require no attribution; still keep source and asset ID internal. Website / API access rules and asset licensing are separate matters: this reference does not promise unlimited harvesting, API quotas, or a licence inferred on behalf of another asset library.

HDRI can serve environment lighting and material reflection; whether it can show as a background, and how shadows form, depend on the actual engine, materials and configuration. In Three.js, `Scene.background` and `Scene.environment` control the background and the environment map separately; showing only a background image does not prove objects already receive the same lighting. Blender configures through World, materials and the chosen renderer; add key light, rim light, contact relationships and local control as the shot requires.

Keep the original entry point, asset ID, licence, download spec, local path and hash of every HDRI / texture / model used in the project notes. Validate composition, environment direction and reflection first at a resolution that is enough, then raise the spec to match the output; do not default to downloading the largest file. Check faces, metal / glass, shadow-side silhouette, ground contact, exposure, background-subject separation, and whether highlights and shadows stay natural through a continuous camera move. No lossless equivalence of lighting, material or colour management is promised between engines; verify the actual render before compositing.

The goal of reasonable use is an observable improvement in this shot's material feel, sense of space and mood. Per the [tool contract](production-tool-contract.md), keep a baseline / candidate for the same shot, compare light direction and colour, subject silhouette, exposure, material reflection, ground contact and motion seams, and record the load / render cost; if the new option is worse, keep the original. A still frame cannot verify continuous highlights, and a successful download / import cannot verify the art result. UltraHDR JPEG and a fixed compression ratio are only case leads from a user screenshot; do not set a default format before verifying current decoding and export, and do not fix "500KB" as a quality or size standard.

## Blender MCP: an optional hookup for interactive authoring

The designated [MCP for Blender](https://github.com/ahujasid/mcp-for-blender) is a community project; its README states plainly that it is not an official Blender product. It works through an MCP server and an add-on inside Blender talking over a connection; it can inspect the scene, execute Blender code and grab viewport screenshots, and it includes Poly Haven asset access. Rendering and saving `.blend` still need real execution and a read-back — a successful MCP connection is not a finished scene or film.

For interactive set building and the "check → change → look at the result" loop, reuse the MCP that is already connected first; repeatable rendering and batch jobs can also use existing `bpy` / headless scripts. Verify the running Blender, scene ownership, MCP server, add-on and protocol version first; do not start the server twice for the same task, and do not take over a scene the user has not authorised. When the hookup is missing, handle it per the actual task — reading this reference does not mean automatically changing global configuration or running a one-click install.

The project can execute Python code, and safe mode is not a guarantee of process isolation. Before connecting, check the execution scope, external generation services, cost and data flow of the current source and configuration; enable only the part this task needs. In the source we read, a minimal anonymous usage record can still be sent when no detailed-data consent is given, so it cannot be called "fully telemetry-free by default"; check detailed collection of prompts, code / scenes separately from basic telemetry. Whether variables like `DISABLE_TELEMETRY` are actually supported depends on that revision's source — do not guess from the name. This is the factual boundary for this hookup; it does not change the user's existing settings or consent state.

Run the asset route as "existing / cached → licensed library → adapt → fill the gap". Before calling, distinguish Poly Haven status, metadata query, download and import; source support for a command does not mean it is wired up on this machine, and a port answering does not mean the protocol works. The project receipt records the actual tool, request scope, asset IDs and imported scenes — do not pass a public API search off as an MCP call. Use [production_tools.py](../scripts/production_tools.py) for light probes, cache queries and record checks; inputs and outputs are in the [production tool contract](production-tool-contract.md).

## Japanese voiceover and other tool candidates

Query the tool table by task; single use or combination are both allowed: Blender handles character, skeleton, expression and adaptation; Mixamo is a candidate motion / character source, check licence and retargeting before use; Unreal Engine is a candidate for complex environments, lighting and cameras — assess first whether the existing project can finish the job, and switch only when the gain is clear; Poly Haven supplies environment and prop assets; the existing ACE-Step 1.5 covers BGM / song production, which does not make it the voiceover engine for every language. Nothing here promises that Mixamo / Unreal current licensing, connections and real-hardware compatibility have been verified.

When a Japanese voiceover is needed, you may choose AivisSpeech Engine within the user's constraints and actual capability. It is a Japanese TTS candidate; check the terms for the software and for the voice models separately; discover the actual styles from the local `/speakers`, and do not hard-code one voice. Generate whole semantic sentences / passages, get real audio timings, and run a listening pass on voice character and pauses before organising subtitles; the engine's WAV concatenation only joins waveforms and does not by itself improve tone, breath or joins. If existing audio only needs stitching, reuse FFmpeg / the existing project instead of installing the whole speech application.

The upstream project keeps unused VOICEVOX singing code, which is no basis for claiming singing / rap support; the actual engine's singer interface is marked unsupported. Go by this revision's official README and the engine implementation; do not treat an inherited interface, old documentation or an API type as proof of capability. Choose separate routes for voiceover, music and singing, and re-verify along the existing contract whenever the audio track changes.

Sources: [AivisSpeech README](https://github.com/Aivis-Project/AivisSpeech/blob/77a3675f7b76865cfa0253ac30f41ef1dd822e27/README.md), [Engine API usage](https://github.com/Aivis-Project/AivisSpeech-Engine/blob/master/README.md), [WAV concatenation implementation](https://github.com/Aivis-Project/AivisSpeech-Engine/blob/2537cdbdda42b3554f1b873e8cc085e8c515d58f/voicevox_engine/tts_pipeline/connect_base64_waves.py), [singer interface](https://github.com/Aivis-Project/AivisSpeech-Engine/blob/2537cdbdda42b3554f1b873e8cc085e8c515d58f/voicevox_engine/app/routers/character.py). The relevant scope was read on 2026-10-25, without local synthesis or listening pass; DeepWiki's inference about inherited Sing Editor support conflicts with the first-hand statement, and this method goes by first-hand evidence.

## Remotion's reusable compositions and the official agent guidance

Per the current official documentation, organise subject, shot assets, titles, subtitles, audio tracks and the required parameters into a reusable Composition; Sequence and media source ranges derive from the project's valid schedule. Save the source project, dependency lock file, asset list and necessary configuration — do not deliver only an MP4.

Projects that actually use Remotion check the installed official Agent Skills and their version first, and reuse the guidance the host already provides; when a project-local install is needed, run the entry point the user gave from the root of the actual render project, following the [official Agent Skills documentation](https://www.remotion.dev/docs/ai/skills):

```sh
npx skills add remotion-dev/skills
```

Verify the install target and scope first: do not blind-install into a generic Context directory, do not overwrite this methodology, and do not install the same named capability twice. Official guidance is a project / host capability that can be updated — do not copy a whole third-party Skill into this Skill; before running, check the current CLI options against the host's install rules. A command appearing in the documentation does not mean it has been run here or loaded on the client.

Three.js itself has animation clips, blending, skeletons and deformation — do not describe it as "having no animation"; scheduling, frame extraction and encoding for a complete video still need project organisation. The official `@remotion/three` documentation requires animation to be driven declaratively by `useCurrentFrame()`, avoiding direct dependence on real-time accumulation. Asset preparation, randomness and time basis all have to be controlled; `EffectComposer` manages post-processing passes and does not by itself guarantee time determinism. For the concrete media and ThreeCanvas APIs, this project's current version documentation is authoritative.

## Cross-tool handoff and acceptance on a real MP4

Record for every shot handoff: source scene ID, project version / hash, camera, frame rate, frame range, resolution, source in and out points and the landing point in the main film, whether it carries alpha, colour / transparency interpretation, dependent assets and sound responsibility. Before adopting video or an image sequence, check what both sides actually support; when Blender materials need no cross-engine editing, prefer handing over pre-rendered media rather than pretending editable 3D is preserved automatically.

Use FFmpeg to encode, mux or select streams as actually needed; explicitly check the video, audio, subtitles and metadata to be kept, so automatic stream selection does not drop necessary sound. After re-encoding, re-check loudness / true peak, start and end, duration, sound-image landing points and full-film decode; record the current project and final file hashes.

Watch the actual output MP4 and check first frame, densest stretch, action settle, expression and pose, camera move, transitions and ending; on sound check lyrics, intelligibility, foreground-background, rhythm, tails and seams. A web preview or viewport screenshot cannot replace the final MP4; a clean decode cannot replace continuous watching and listening either. Deliver the editable `.blend` and related assets, the Three.js source actually used, the Remotion project and the final file according to the chosen route; do not fabricate projects that were not used. Book unfinished listening passes, playback or comprehension checks honestly.

## First-hand sources and scope

- [Blender official repository](https://github.com/blender/blender): DeepWiki structure and two targeted Q&As covering animation, skeletons, camera, World, Cycles and EEVEE; these capabilities were not run on this machine, and no untested version parameters are given.
- [Three.js Scene source](https://github.com/mrdoob/three.js/blob/dev/src/scenes/Scene.js): background / environment fields read; animation and post-processing boundaries cross-checked via the repository's DeepWiki.
- [Remotion official Agent Skills source docs](https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/ai/skills.mdx), [ThreeCanvas source docs](https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/three-canvas.mdx): read; supports the install entry point and the frame-driving boundary; the division between pre-rendered media and running 3D was cross-checked via repository Q&A.
- [Poly Haven licence page source](https://github.com/Poly-Haven/polyhaven.com/blob/master/pages/license.tsx), [English body](https://github.com/Poly-Haven/polyhaven.com/blob/master/public/locales/en/license.json): read; separates asset CC0 from website code licensing; the full text of the dynamic terms of service was not obtained.
- [Blender MCP README](https://github.com/ahujasid/mcp-for-blender/blob/main/README.md), [telemetry source](https://github.com/ahujasid/mcp-for-blender/blob/main/src/blender_mcp/telemetry.py): relevant scope read; concrete installation and compatibility still have to be checked at the time of the task.
- The [official FFmpeg documentation](https://ffmpeg.org/ffmpeg.html) and its [original source](https://github.com/FFmpeg/FFmpeg/blob/master/doc/ffmpeg.texi): input and output, option scope and stream selection read; concrete delivery parameters are verified per project.

Search date 2026-10-25; relevance rests on the shot and combination requirements designated for this round, authority is judged by the responsibility scope stated in official source / project maintainer documentation, and creation / modification and traffic-reaction metrics were not obtained one by one — none are guessed. The responsibility combinations and the shot-first rule above are this method's own adaptation; document research does not represent installation, an actual 3D test cut, or sound or cross-tool finished-film verification.
