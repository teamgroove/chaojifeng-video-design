# Editable plan and delivery contract

schema_version is 1. Paths are relative to the directory that holds the plan file; an explicit absolute path is allowed, but do not write a local personal directory into a template default. All times are seconds counted from the start of the whole film, and the values must be finite. Machine checks guarantee structure and consistency; semantics, the actual frame, the sound and comprehension are verified separately.

## Minimum plan structure

```json
{
  "schema_version": 1,
  "project_id": "sample",
  "revision": 1,
  "goal": "观众看完能够说清的事情",
  "audience": "目标观众",
  "scenario_id": "knowledge-explainer",
  "mode": "recipe",
  "output": {"width": 1920, "height": 1080, "fps": 30, "duration_seconds": 8, "language": "zh-CN", "audio": "silent"},
  "design": {"style_id": "paper-editorial", "rationale": "为什么这种表达适合这段内容", "preserve": []},
  "runtime": {"adapter": "existing-project", "capabilities": []},
  "assets": [],
  "scenes": [{
    "id": "scene-01", "purpose": "理解一个变化", "start": 0, "end": 8,
    "layout": "relation-diagram",
    "elements": [{"id": "object-01", "role": "subject", "content": "内容主体"}],
    "beats": [{"id": "beat-01", "time": 1, "meaning": "主体出现"}],
    "motions": [{"id": "motion-01", "pattern_id": "reveal", "target_id": "object-01", "start": 1, "end": 2, "parameters": {}, "beat_id": "beat-01"}],
    "narration": [], "audio_cues": [], "hold_seconds": 2
  }]
}
```

Required: schema_version, project_id, revision, goal, audience, scenario_id, mode, output, design, runtime, scenes. assets may be omitted or empty; inside a scene, elements is required, while beats/motions/narration/audio_cues may be omitted or empty. A scene needs id/purpose/start/end; each element needs id/role, with content/asset_id/continuity_key optional. A simple single-shot film uses this same contract directly; it is not forced to produce four or five extra documents.

mode is recipe, compose or free. Built-in scenario_id values are in the scenario catalog; for a custom scenario use custom and supply scenario_description. For a custom visual style use design.style_id=custom with design.tokens and rationale. runtime.adapter is the name of the execution route you chose — it is not proof that anything is “installed / ready to render”. runtime.status is unresolved or ready, and omitting it counts as unresolved; capabilities registers only features that have already been probed, while capabilities still to be implemented go in required_capabilities. General motion uses semantic capabilities such as time-control, opacity, position and stroke; DOM/SVG/Canvas or a particular engine is only an implementation choice, not a hard precondition for all motion. unresolved produces an actionable warning and makes no claim that the film can be exported; under ready, a missing required capability is an error. The structural samples use unresolved, and no sample field may stand in for an execution probe.

output width/height/fps/duration_seconds are positive numbers, with width, height and fps as integers, and audio is silent/optional/required. Use the real spec of the current project; changing width and height does not count as completing a re-layout. scenes are sorted by start and cover 0 to the total duration with no gaps; a cross-shot overlap needs overlap_reason on the later shot. hold_seconds is the budget for stable reading inside a shot and does not automatically equal the effective reading time for all the copy.

## Objects, motion and sound

- IDs of each kind are unique within the whole plan and are kept; do not renumber every ID because a colour changed. The same subject across shots uses a different element.id and the same continuity_key. A motion controls only the element of the shot it lives in; a container/camera is also an explicit element.
- beats contains id/time/meaning and may add narration_id. narration contains id/display/spoken/start/duration_seconds/timing; timing is measured or estimated, and asset_id may be added. display is the subtitle text, spoken is how it is read. With no actual audio the timing can only be estimated, and a final acceptance of voiceover sync cannot pass on an estimate.
- motion needs id/pattern_id/target_id/start/end. Built-in pattern_id values are in the motion catalog; parameters/beat_id may be added. A free implementation uses pattern_id=custom, custom=true, channels and implementation, stating which properties it controls and where the implementation lives. channels uses property names such as opacity, position, scale, color, stroke, camera, mask, value; when the same target controls the same property over the same interval, you must state a layering or compositing reason, composition_reason — otherwise it counts as a conflict.
- All element times inside a shot must fall within the shot's range; beat references, asset references and narration references must resolve. beat_id is an association — it does not claim word-level automatic alignment; the actual peaks need a listening pass / waveform or run evidence.
- audio_cues contains id/asset_id/time/role and may add beat_id/gain_db/sync_offset_seconds; role is music, voice or sfx. Asset kind is image/video/audio/font/product/data; an asset needs id/kind/path/source/rights/status, status is ready or missing, and sha256 may be added. A ready local file should exist; citing a remote URL does not mean it is downloaded and usable. A file produced purely by code writes source="procedural", with path pointing at the file actually generated, optional implementation pointing at the generating code, and parameters holding the parameters. DOM/Canvas objects drawn directly do not fake an image-asset row; keep the implementation in element.implementation or in the runtime project.

For cutting a segment out of an original music track and placing it, write a separate music-cue-sheet.json per [music direction](music-direction.md); source_in/out belong to the original track, timeline_start/end belong to the whole film — do not mix them. The file actually trimmed/mixed still goes through the assets/audio_cues contract above; do not treat a candidate cue ID as an audio file that already exists.

Knowledge explainers can use the optional [sound-and-image task sheet](../templates/knowledge-music-score.json) and `explainer_timing_audit.py`: they reference existing scene/element/beat/claim/layer and audio cue entries by the current plan hash, and add no required field to the main plan; direct/staged only records the delivery rhythm the user asked for. Music-source anchors are derived per the cue sheet onto the whole film, a positive offset means the sound is later, and the reading window runs from the beat where the copy is fully readable to the exit beat. This check covers only the declared schedule; it cannot prove measured beat hits, pixel-level legibility or how it sounds. For the fields see [explainer sequencing](knowledge-music-direction.md).

Dynamic annotation can use the original elements/motions directly; a complex screenshot crop, camera follow or multi-segment emphasis can be saved separately as annotation-track.json — see [visual emphasis](visual-emphasis.md) and the [track template](../templates/annotation-track.json). It records source coordinates, screen coordinates, the full target/exclusion regions, protected areas and absolute times, and can be checked by a standalone tool. `--plan` additionally checks the scene/element references; the original plan gains no required fields, and a track neither drives the executor automatically nor raises the visual acceptance state.

## Delivery manifest

```json
{
  "schema_version": 1,
  "project_id": "sample",
  "plan_sha256": "计划文件当前原始字节的SHA256",
  "producer": {"tool": "实际执行工具", "model": "实际模型或unknown", "run_id": "可核验的运行标识或unknown"},
  "outputs": [{"kind": "video", "path": "final.mp4", "sha256": "文件当前SHA256"}],
  "checks": {
    "structure": {"status": "not_run", "evidence": []},
    "semantic": {"status": "not_run", "evidence": []},
    "visual": {"status": "not_run", "evidence": []},
    "playback": {"status": "not_run", "evidence": []},
    "audio": {"status": "not_run", "evidence": []},
    "comprehension": {"status": "not_run", "evidence": []}
  }
}
```

Output kind is video/source/preview/audio. An outputs path is relative to the delivery manifest, not to the plan file; asset paths inside the plan are relative to the plan file. A check status is passed/partial/failed/not_run/not_applicable, and passed must carry a verifiable evidence path or an observation record. With silent you may write audio as not_applicable, but when the user asked for sound you may not quietly change it to silent. If no reader test was run, write comprehension as not_run. Probing video properties is not the same as continuous playback; an image existing is not the same as having been watched.

After you change the plan or a required asset, the old checks no longer represent the new film. Save the revision, the scope of change and the dependencies, rebuild the matching preview/audio track/video, and update plan_sha256 and the artifact sha256. A hash proves only that the bytes correspond; it does not prove it looks good, is correct, or sounds right.

## Catalog contract

catalog/scenarios.json, styles.json and motions.json are all {"schema_version":1,"items":[...]}. Every item requires id/name/intent/constraints/fallback/verification. The verification structure is {"design":{"status":"authored","evidence":[]},"preview":{"status":"not_run","evidence":[]},"exported":{"status":"not_run","evidence":[]}}. design status is authored/reviewed; preview/exported is not_run/passed/partial/failed. When verification has actually happened, add environment, scope and the concrete artifact; a pass for one parameter or one engine may not be written as a pass for the whole category or for other environments. Do not record a source demo as verification in the current environment.

A scenario item additionally holds required_inputs, narrative_options, layouts, style_ids, motion_ids; a style item additionally holds tokens, motion_character, avoid; a motion item additionally holds channels, required_capabilities, parameters. The query tools output stable IDs and their purpose, and an agent may freely implement anything not catalogued, as long as it still obeys the plan and acceptance contracts. The catalog is for bounded choices; it makes no promise that every style and every motion can be arranged in any combination.

## Director extension (keeps schema_version=1)

Existing plans keep working. A simple film only needs viewer change, through-line and sound-and-image responsibilities written into design.rationale; a complex film uses the optional director in the same plan — see the [director template](../templates/director.json). These fields record intent and check references; they are not proof of taste, narrative or audience comprehension.

- director, when present, holds non-empty intent/viewer_end/throughline, structure:{kind,rationale}, entities and beats. viewer_start is optional. Each entities entry has id/kind/role as non-empty strings and identity_constraints as an array of strings; each beats entry has id/function/before/change/after as non-empty strings. The two kinds of ID are each unique within their own kind, kept by responsibility, and not renumbered because the grade changed.
- structure.kind is a name for the structure the content suits and may be named freely; three-act is not mandatory. Character goals and the like are added as needed — product / knowledge / music films can have no characters. Never invent an unknown fact to fill the form.
- sound_arc is optional; every entry has id/beat_id/role/onset_anchor/energy/visual_relation as non-empty strings, and beat_id references director.beats. It records the sound-and-image relationship; it is not playable audio. Actual sound is still written into assets/audio_cues.
- iteration is optional, max_passes is a positive integer and stop_rule is a non-empty string; it is this task's exploration ceiling, authorising neither spending nor unlimited resources. tech_language is optional, with choices/avoid as arrays of strings that say why they are relevant — do not just paste on a “tech feel” label.
- scene.intent is optional; when present, viewer_change is required and non-empty. beat_ids reference director.beats, focus_entity_ids reference director.entities; reveal_order references the element.id of this shot — all arrays of strings. camera, when present, has framing/movement/purpose as non-empty strings. handoff/acceptance, when present, are non-empty strings.
- design.expression_ids is optional, an array of expression IDs from the catalog; design.recipe_id is optional, a single recipe ID. Free creation may omit both. A reference states a choice only; it does not automatically invoke an effect, schedule a clock, create an asset or raise a verification state.

catalog/expressions.json and recipes.json use the same schema_version/items and the common item fields. An expression additionally carries layer/tier/status, inputs, parameters, composition, required_capabilities, existing_motion_ids, verification_questions, source_relation; status=guidance, so a design control does not impersonate an execution API. A recipe additionally carries scenario_ids/style_ids/motion_ids/expression_ids and story_steps. scenario_ids are recommended scenarios, not an exclusive list of engine support; when borrowing across scenarios, explain the adaptation and re-check facts and capabilities — the script warns but does not block. A scenario may attach expression_ids/recipe_ids; the script validates those references. Recipes and expressions are guidance; do not register a source video as passing on this machine.

A recipe may carry an optional `music_policy`: `candidate_track_ids` is a non-empty array of distinct track IDs, `default_track_id` must belong to that pool, `planning_mode` is music_first/content_first/adaptive, and `default_requires_confirmation` is a boolean. The catalog checks its structure and its music-library references, and a recipe that omits the field still applies. `music_library.py select --recipe ID` resolves by user choice, then project choice, then recipe default; `--track` allows explicitly picking a track outside the pool but inside the library, and `--source-file` allows a new source inside the project — neither changes the default or the candidates. A missing chosen source, or a hash/duration mismatch, blocks rather than silently substituting; duration and hash checks cannot prove how it sounds or the scope of use.

## Knowledge pack extension (keeps schema_version=1)

Existing plans keep working. When explaining abstract knowledge or a news brief, you can add an optional `knowledge` at the top level of the plan; for the fields, check codes and fill-in order see the [knowledge pack contract](knowledge-pack.md), and for the template see the [knowledge pack template](../templates/knowledge-pack.json).

- When `knowledge` is present, `validate_plan.py` validates it, checking whether `layers[].scene_ids`, `focus_element_id`, `claim_ids` and `carrier.mappings[].element_id` point at shots and elements that really exist in this plan, and runs the controlled-expression check on narration and element copy. Errors join the plan errors and warnings join the plan warnings; `--strict-knowledge` raises knowledge warnings to errors.
- If `design.expression_ids` contains any `knowledge.*` but there is no `plan.knowledge`, raise a `knowledge_pack_missing` warning; if `plan.knowledge` exists but no `knowledge.*` expression is recorded, raise a `knowledge_expression_unrecorded` warning.
- Layers do not have to map one-to-one onto shots, but every shot serves at least one layer, otherwise raise a `scene_without_layer` warning.
- No required fields are added, and a plan without `knowledge` behaves as before. `knowledge.scope` in the result is `knowledge-pack-contract-only`, which means contract checks only — it does not mean the frame, the sound or comprehension has been verified.

## Product expression notes and the media clock (keeps the old contract)

Read [product expression](product-expression.md) and the [single-shot note](../templates/product-shot.md) as needed. The shot's claim, the input/intermediate/result roles, the basis for a state, semantic slots, seam relationships, sound's job and embedded media mapping are design notes: write them into the existing purpose/intent or the project notes; no required plan field is added. The existing scripts validate neither these semantics, nor the truth of a state, nor timbre, nor edit source in/out points, nor A/B control — do not treat a structural pass as passing those acceptance checks.

The existing scenes.start/end, beats.time, motions.start/end and audio_cues.time remain whole-film seconds; time inside an embedded media source is recorded separately as in/out points, whole-film start and end, rate and replay. An SFX's actual onset is offset from the file start — calibrate it against the original audio_cues/beat and the real asset. A reference mix cannot be registered automatically as standalone SFX; the file actually trimmed/mixed still needs assets source / scope of use / hash.

The two new structural samples keep runtime=unresolved and missing audio: only their structure can be checked, and they can be neither exported directly nor passed through strict-assets. A real project replaces the assets and the implementation, reviews the cut, and only then generates its own delivery — it does not inherit the samples' state.

## Style pack extension (existing plans keep working)

Built-in styles and explicit external sets resolve uniformly. For the fields, inheritance, capability and hash checks of the optional design.style_overrides and design.style_lock see the [style pack contract](style-pack-contract.md). The time-control, graphics-2d, graphics-3d or media-composite that a source style needs are real implementation capabilities — a pack merely existing does not register them as ready.
