---
name: chaojifeng-video-design
description: Design and produce product demos, knowledge explainers (including rap), news briefs, image-driven films, stories, feature motion, brand films and music visuals. Supports choosing or extending video styles, combining motion effects, strengthening the first three seconds, asset routing, music arrangement, reference-film study and local revision; from directorial intent to an editable plan, production, review and a playable film — or delivery of just the plan or the storyboard. Model- and engine-neutral; loads style packs and technical capabilities per task.
---

# Chaojifeng's video design methodology

Decide first what the audience must understand or feel, then organise shots, assets, text and sound. The story belongs to the subject at hand; the style supplies material and a grammar of expression; realisation is done with the tools actually available.

## Fix the scope first

1. Read the [confirmed learnings](data/memory.md), the user's input and any project-specific notes. Reuse existing projects, assets, processes and renderers, and verify who owns each resource.
2. "Make a video / a promo / generate the finished film" delivers a playable video, the necessary editing sources and a verification summary. When only a plan, a storyboard or a single motion effect is asked for, deliver exactly that scope. A local revision of an existing piece keeps the rest of the content and the stable IDs.
3. Fill in audience, viewer change, facts, brand, assets, aspect ratio, duration, sound and purpose from context. Decide low-impact choices yourself; ask only when facts, required assets or cost authorisation genuinely block the result.
4. With an explicit "direct", complete the whole film, the internal checks and any necessary rework in one continuous run, without adding test cuts or direction sign-off gates. Wait at the agreed checkpoints only when the user asks for "staged". In both modes, check facts, reading, sound and the actual export.

## Load by responsibility

| Problem to solve | Read and do |
| --- | --- |
| Story, shots, sound, viewer change | [DIRECTOR.md](DIRECTOR.md), then load the relevant methods per [task routing](references/task-routing.md) |
| Choosing, varying, borrowing or adding a style | Use the [style gallery](assets/gallery/index.html) to see the frames, source samples and side-by-side comparisons; look up the exact ID / Chinese name / English name per the [style pack contract](references/style-pack-contract.md), and read only the chosen pack's STYLE.md and what it references |
| Tools, engines, assets, actual production | [TECHNIQUE.md](TECHNIQUE.md); probe the capabilities, then produce along the existing project |
| First extension, maintenance, import and catalog generation | [MAINTAINING.md](MAINTAINING.md); keep maintaining the library separate from producing the current piece |
| From plan to finished film | [production workflow](references/production-workflow.md), [plan contract](references/plan-contract.md) and [review and revision](references/review-and-revision.md) |

Three entry points stay available: `recipe` picks a scene recipe, `compose` combines local layouts and motion, `free` is open design. Scenarios, styles, motion, expressions and recipes are queried on demand through the [catalog tools](references/commands.md); the counts follow the generated catalog. An expression is guidance, the source code is the implementation reference; neither means that a given host has installed or rendered it successfully.

```sh
python3 SKILL_ROOT/scripts/catalog.py --kind style list --scenario knowledge-explainer
python3 SKILL_ROOT/scripts/stylepacks.py resolve 中国水墨
python3 SKILL_ROOT/scripts/catalog.py --kind recipe get knowledge-rap-explainer
python3 SKILL_ROOT/scripts/validate_plan.py /project/video/plan.json
python3 SKILL_ROOT/scripts/check_delivery.py /project/video/plan.json /project/video/delivery.json --probe --require-video
```

## Keep applying during production

- Write the viewer change, the through-line, each element's mission and the job of the sound before choosing effects. For key shots state the new information, the focus, the reveal order, a stable dwell and the handoff to the next shot. Keep simple tasks light.
- For factual shots look for the real product, the original photos, recordings, archives and data first; check the project cache and the licensed assets and fill only the gaps. If that cannot hold, change the shot or shrink the claim.
- For information-flow explainers and promos, check the first frame and the first three seconds by default; for concept explainers verify facts, standards and terminology first, then reveal layer by layer; for rap verify the knowledge and the singable lyrics first, then arrange against the real audio track.
- When there is narration or lyrics, get the real audio and tie every line to picture and subtitles; after replacing a track, re-measure, re-arrange and re-check. Music selection follows the order: user choice, already chosen in the project, recipe default; keep the candidate pool separate from the default and never promote one track to a global default.
- Use absolute seconds of the whole film and stable IDs for timing; picture, sound and subtitles derive from the same schedule. With many sound effects use the [audio event map](templates/audio-event-map.json) and, where needed, measure with `film_probe.py` and `audio_event_audit.py`. A unified clock, a random seek or sound sync may only be logged as passed after measurement.
- The full rules and the reusable sources of an upstream style are part of the pack. Fix the intent of this film first, then read the case implementation; this film's brand, facts, chosen music, language, aspect ratio and delivery requirements take precedence. Never infer asset, model or tool licences from the code licence.
- Keep internal sources, reconstruction and execution records separately. Body copy, business prompts, visible paths, subtitles, voiceover and exported attachments face the audience directly — do not attach production identity labels or making-of notes automatically; keep the necessary factual boundaries and licence checks.
- Rework until the required conditions pass. Record structure, source usability, the actual export, watching, listening and audience comprehension separately; a candidate version cannot inherit a pass status from an older version or from an upstream case.

## Revision, delivery and memory

Locate a revision by shot, object or time window and re-verify the dependencies; re-measure the timing when the voice changes, re-check sources and graphic semantics when facts change, and do not needlessly redo the sound when only the colour changes. For extension read the [extension contract](references/extension.md); a variant of one film belongs in the project, a stable personal style belongs in an external pack with a new ID.

Deliver the actual video, the necessary editing sources, asset references and a verification summary; state the tools actually used, what is unfinished and which resources were retained. Do not upload or publish without a request. Clean up the resources clearly owned by this run that are no longer needed.

Run logs stay inside the project; only short results, explicit preferences and verifiable problems go into `data/memory.md`, the last 20 runs, with no private assets or long conversations. Changing the skill, the style-pack spec or the behaviour still follows the host's authorised confirmation flow. For sources and licences see [sources.md](references/sources.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
