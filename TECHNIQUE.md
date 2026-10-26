# Technique: capabilities, engineering and real delivery

The creative plan uses [plan-contract.md](references/plan-contract.md); the actual execution follows [runtime-and-delivery.md](references/runtime-and-delivery.md). Existing projects, assets, dependency caches and tools come first — reinstalling the environment is not the default starting point.

## Three independent layers

| Layer | Content | Boundary |
| --- | --- | --- |
| Director and plan | viewer change, shot jobs, sound, whole-film schedule | do not reverse-engineer a story from a template or a case |
| Style pack | material, colour, type, motion, camera, sound and native moves | defines effects and implementation references; does not become a renderer by itself |
| Actual production route | existing engine, screen recording, asset compositing or generation tools | capabilities are logged only after real probing, integration and export |

The library's query, import and validation scripts use only the Python standard library. Upstream text sources live in each pack's `demo/` and in `vendor/lemo-opuscar/`; their runtime dependencies are prepared on demand by the project making the film — querying never runs that code and never installs dependencies.

## Adapting the execution route

| Existing route | How style capabilities plug in | What verification focuses on |
| --- | --- | --- |
| HTML / Canvas / WebGL | drawing and camera technique can be reused along the upstream `render(t)`, `DUR`, `READY` interface | fonts and assets ready, seeking to any time, identical repeated frames |
| Remotion / HyperFrames | map absolute seconds and events onto the host timeline, reuse material and motion relationships | actual host version, frame count, audio track and export |
| Blender / Three.js | split camera, space, material, lighting and end state per shot | render cost, world-to-screen mapping, actual output |
| Compositing existing footage and screen recordings | keep source in/out points, crop, speed, subtitles and the evidence relationships | asset provenance, occlusion, reading windows and sound seams |

These are adaptation contracts; `runtime.adapter` still records the route actually taken. When capability is missing, report the concrete gap first — do not treat one style pack's source status as support across every engine.

## One clock and one set of resources

Picture, sound effects, narration, subtitles and checks derive from the same effective schedule, using stable object and event IDs. Deterministic implementations compute state from time, fix the random seed, and wait for fonts and assets to be ready; claim repeatability only after comparing forward, reverse and random seeks.

Upstream renderers default to multiple workers; this library produces serially by default, one execution instance per task, with an explicit concurrency cap. Reuse the existing browser, renderer, ports and cache where possible, read the logs first on failure, and clean up only this task's resources at the end. Website operations follow the host's Chrome routing.

The upstream readcheck, ASR, mixing and rendering code can be adapted by the project; the existing `check_delivery`, `film_probe`, `audio_event_audit` and `explainer_timing_audit` check files, media and declared schedules respectively. When a required interface is missing, log it as unchecked — it cannot count as passed.

## Entering a project from source

Read the chosen pack's STYLE.md and STYLE.upstream.md first; fix this film's intent, then read DEMO.md and copy the implementation from `demo/` into the user's project as needed. Correct LIB, imports, asset and build paths, and verify the API against the current official documentation and the local version. Do not run `build.sh` inside the library, and do not copy upstream models, sound services, assets or publishing scripts outright.

For asset use see [asset-routing.md](references/asset-routing.md) and [production-tool-contract.md](references/production-tool-contract.md); for characters, space and cross-engine assembly see [scene-tool-composition.md](references/scene-tool-composition.md).
