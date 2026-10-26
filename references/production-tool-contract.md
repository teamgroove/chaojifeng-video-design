# Production tools and project-artifact contract

This contract turns asset-first, tool choice, HDRI comparison and Japanese narration into reusable tools. Reuse the existing plan's scene/asset/beat identity and time; do not add required fields to the main plan. The tools do not install software, do not start renderers, do not download models and do not change scenes; actual production is still carried out by capabilities the host has already authorised.

## Look up responsibility by task first, then probe capability

The tool table is [production-tools.json](../catalog/production-tools.json); `tasks` states the fitting responsibility, `adapter` states the action this script provides. `candidate` is only a candidate pending verification, `guidance` only gives selection guidance; `verification=not_run` is not permanently unavailable and must not be changed to "installed". Write the concrete status into this project's receipt; do not hard-code local machine state into the tool table.

```text
python3 SKILL_ROOT/scripts/production_tools.py list --task environment
python3 SKILL_ROOT/scripts/production_tools.py list --task japanese-narration
python3 SKILL_ROOT/scripts/production_tools.py probe
python3 SKILL_ROOT/scripts/production_tools.py polyhaven-search --query studio --type hdris --limit 5 --cache-dir /project/video/cache/polyhaven
python3 SKILL_ROOT/scripts/production_tools.py aivis-speakers
python3 SKILL_ROOT/scripts/production_tools.py check /project/video/production-job.json
python3 SKILL_ROOT/scripts/production_tools.py check /project/video/production-job.json --require-reviewed
```

Save the JSON output into the project; terminal printing cannot stand in for project evidence. `list` returns responsibility candidates and does not automatically create a fixed pipeline; the Agent picks one or several tools per this shot's intent and records the reason. Mixamo/Unreal are candidates; verify current licence, resources and integration before use; when the existing Blender/Three.js can do the job, do not force a switch. Japanese narration and BGM are separated; ACE-Step keeps the music responsibility, Aivis does not promise singing or rap.

`probe` only checks the common local entry points and default ports; a TCP connection does not mean the protocol, plugin, model, permission or voice is actually usable, so note the scope when other configured ports are not covered. It does not connect into user scenes to execute commands and does not start duplicate services. `aivis-speakers` only accesses the local engine's `/speakers` to obtain actual speaker/style information; it does not hard-code a particular style ID and does not generate or audition audio.

`polyhaven-search` only takes metadata from the public API, returning a few ranked candidates with the original page and keeping source order; do not treat ranking scores as art quality. Use a project-owned cache, by default caching locally for 1 hour to reduce repeated requests; this is this tool's throttling policy and does not represent server quota. Responses are limited to 2MB; 429/503 and other errors are reported as they are, not retried automatically, respecting Retry-After and the task budget. Metadata success is not marked as MCP retrieval, download, import, usage-rights review or picture approval.

Website operation still follows the host browser route; an applicable API/MCP goes through the interface that currently has evidence. Asset download and MCP import are executed separately per the actual tool and authorisation; do not derive authorisation to modify scenes or to install from a read-only probe.

## Use one project artifact to link decisions and evidence

Copy [production-job.json](../templates/production-job.json) into the project and fill it in along what this run needs. An empty template is only a draft; validation will warn that there is no production evidence; unused arrays may stay empty. When you need to bind the main plan, add `plan_path` and `plan_sha256`; the former is relative to the artifact directory, the latter binds the main plan's current raw bytes. Re-check the link after the main plan changes; do not copy a competing clock.

### Tool choice `tool_choices[]`

Each item contains `id`, the `tool_id` from the tool table, the corresponding `task`, and this shot's `reason`; attach `scene_ids` and the actual-capability receipt path as needed. Tool documentation, current integration, actual execution, artifacts and quality acceptance are each evidenced separately; do not merge them into one "available" status.

### Assets `assets[]`

| Field | Convention |
| --- | --- |
| id | follow the plan asset ID; purely internal candidates use a standalone ID, and a mapping is established once chosen |
| role | event-proof/illustration/model/motion/environment/material/audio |
| action | reuse/library/adapt/generate/scratch |
| origin | project/user/library/generated/procedural; consistent with the actual source |
| status | planned/ready/unavailable; ready only means the file is ready |
| source, rights | original entry point / asset ID and the basis for actual use; do not substitute "publicly visible" for a licence |
| path, sha256 | required when ready, with the path relative to this artifact's directory; validation checks the hash by streaming |
| search | before generate/scratch, record status=completed or blocked, plus the sources array actually checked |
| gap_reason | why existing assets do not fit and why the gap needs production; required when generating / from scratch |

For models, characters, motion, HDRIs and textures check the project/cache first, then licence-appropriate asset libraries, prefer adaptation, and only fill the missing part last. When retrieval is blocked, record the blockage and the alternative expression truthfully; do not fake "checked". Check characters by proportions, rig, skinning and facial control; check motion by retargeting, foot contact, hand contact and timing. Adaptation records, source-to-derivative relations and imported scene IDs can sit in the same asset row; do not create another duplicate asset ledger.

event-proof must keep the original evidence; a staged or procedurally built scene cannot prove that an event happened. Relationship diagrams, created models and environments are registered by their real role; do not use prettier assets to expand a factual claim.

### HDRI and picture `lighting_reviews[]`

Each item contains `id`, `scene_id`, environment `asset_id`, `status` (not_run/passed/partial/failed), the actual `scope` (still/clip) and `finding`. When passing, provide different local evidence files `baseline_evidence[]` and `candidate_evidence[]`; identical content under a new name is rejected; the evidence should come from the same shot, the same composition and comparable output conditions, and should state explicitly what alone was changed. If light, material and exposure are changed together, record a multi-variable change and do not attribute it to the HDRI alone.

Describe separately in the finding or an attached record: light direction/colour, exposure, silhouette and subject separation, material reflection, contact shadow, sense of space, highlights and seams in continuous motion, plus download/load/render cost. You may keep the original option or judge the new one worse; not every shot has to change HDRI. Check background and lighting separately; an asset existing does not mean it is used reasonably; with stills only you cannot write `motion_continuity` as passed.

Compare at sufficient specification first, then raise the specification where the shot needs it. The user screenshot's "20MB compressed to about 500KB UltraHDR JPEG" serves only as a case clue; it does not become a default compression ratio, format or effect promise; before use, verify the current executor, decoding, brightness range and actual export result separately.

### Japanese narration `voice_jobs[]`

Each item contains `id`, `language`, `mode`, `tool_id`, `status` and an explicit `listening` record. The Aivis branch is `language=ja`, `mode=narration`; write the basis for using the model/voice in `model_rights`; when ready, give the actual `path` and `sha256`. Candidate selected, software present, style discovered, generation succeeded and listening approved are each recorded separately.

Generate from complete semantic sentences/paragraphs, keep one voice and one style, and measure the real audio before laying out subtitles. The Aivis engine can join WAV, but concatenation does not automatically improve pauses, breathing, volume or voice line; when existing audio only needs joining you can reuse FFmpeg or the existing project. Listening approval first requires the audio to be ready with a matching hash, then `listening.status=passed`, `method=listened` or `user-feedback` and the actual record paths in `evidence[]`; ASR/waveform/concatenation exit codes cannot substitute. Subtitle and audio-track changes are still re-verified per the existing sound contract.

Verify the Aivis program licence and the voice-model conditions separately; free software does not imply any use of a voice. Report gaps accurately when something is not integrated, no suitable model exists, or the singing task is unsupported; candidates do not automatically switch to a paid service or download a model. For sources see [Scene and tool composition](scene-tool-composition.md#japanese-voiceover-and-other-tool-candidates).

## Validation boundary and actual delivery

`check` returns valid, errors, warnings and `scope=declared-production-evidence-only`, checking tool/task matching, asset-first records, factual-picture source boundaries, file hashes, plan drift, comparison evidence and sound acceptance declarations. It does not go online to verify licences, does not understand pixels, does not listen to sound and does not prove the records are true; even when a declaration has passed, its own `media_review` remains not_run.

By default it allows a draft with un-reviewed items and gives a warning; `--require-reviewed` turns unfinished items among registered lighting/listening into errors, and an empty artifact also fails. It covers only the scope registered in this artifact and cannot replace whole-film knowledge, reading, sound-image, continuous-playback and delivery checks. Actual adoption, film review and rework follow [Review and revision](review-and-revision.md); the end still delivers a real MP4, the necessary editable sources and an artifact-consistency record.
