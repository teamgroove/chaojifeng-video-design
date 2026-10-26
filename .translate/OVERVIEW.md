# Map of this skill — what each document is for, and how the neighbours differ

English translation of a Chinese video-design methodology ("Chaojifeng's video design methodology").
This file is orientation only: it is not loaded by the skill at run time.

## 1. What the repository actually is

One skill, not many. `SKILL.md` is the only entry point an agent reads; everything else is loaded
on demand from it.

| Part | Count | Role |
|---|---|---|
| `SKILL.md` | 1 | the entry point: scope, routing table, production rules, delivery |
| `DIRECTOR.md`, `TECHNIQUE.md`, `MAINTAINING.md` | 3 | the three specialised views: content/sound, engineering/capability, library maintenance |
| `references/*.md` | 36 | the actual methods, loaded one or two at a time by task |
| `templates/*` | 10 md + 8 json | optional fill-in sheets and artifact skeletons (plan, delivery, audio events, beat sheet …) |
| `styles/<id>/STYLE.md` | 66 | style packs: material, colour, type, motion, camera, sound grammar |
| `catalog/*.json` | 7 | the data the agent and the gallery query (scenarios, styles, motions, expressions, recipes, production tools) |
| `scripts/*.py` | ~32 | catalog queries, plan validation, delivery checks, media probing, imports, tests |

It is model- and engine-neutral by construction: the plan describes what must be true, the style
pack describes how it looks, and the production route is whatever the host can actually run.

## 2. The mental model — read this before anything else

Three layers, deliberately independent:

1. **Director and plan** — viewer change, shot jobs, sound, the whole-film schedule.
2. **Style pack** — material, colour, type, motion, camera, sound; it defines *effects and
   implementation references*, it is **not** a renderer.
3. **Production route** — the engine actually present (HTML/Canvas/WebGL, Remotion/HyperFrames,
   Blender/Three.js, footage compositing, generation tools); capabilities are only logged after
   real probing and export.

Three entry points into any scene: `recipe` (a scene recipe), `compose` (combine local layouts and
motion), `free` (open design). Looking up an entry is not the same as invoking an effect.

## 3. Reading order

1. `SKILL.md` — scope, routing table, non-negotiables.
2. `DIRECTOR.md` — how intent becomes shots and sound.
3. `references/task-routing.md` — pick the one row for your current task.
4. The one or two references that row names.
5. `TECHNIQUE.md` only when the question is "how do I actually build and deliver this".

`MAINTAINING.md` is not part of producing a film; it is for changing the library itself.

## 4. Which document answers which question — and what separates the neighbours

| Document | Question it answers | Differs from its neighbours by |
|---|---|---|
| `SKILL.md` | what is in scope, what to load, what "done" means | only routing + hard rules, no craft |
| `DIRECTOR.md` | how intent becomes shots and sound | the three-paragraph craft core; defers all detail |
| `references/director-method.md` | why this film holds at all: through-line, element missions, two production routes, when to stop | the front-end of direction; `creative-direction.md` is the *open* creative mode (motif, primary/secondary motion, aesthetic boundary), `design-method.md` is the short content→visual translation, `shot-production.md` is planning per shot |
| `references/production-workflow.md` | the run itself, start to delivered file | the checklist; the *methods* live elsewhere |
| `references/plan-contract.md` | the schema: what an editable plan and a delivery manifest must contain | `production-tool-contract.md` covers tools/assets/HDRI/voice jobs, `style-pack-contract.md` covers packs, `knowledge-pack.md` covers the knowledge claims |
| `references/review-and-revision.md` | how to watch, judge and rework, and what "measured" means | the human review; `TECHNIQUE.md` + `film_probe.py` are the machine checks — a process check never replaces watching |
| `references/sound-and-rhythm.md` | sound as narrative and editing: sound map, SFX/music character, mixing, lyric timing, one timekeeper | the general sound method; `music-direction.md` is *finding* passages from intent, `knowledge-music-direction.md` is the music-led explainer recipe, `product-music-story.md` is lyrics+product, `knowledge-rap-direction.md` is rap |
| `references/asset-routing.md` | where material comes from: real footage first, build only the gaps, source and performability | `asset-motion-direction.md` is what the asset *does* (motion range, spatial relations, part records) |
| `references/knowledge-visualization.md` | making abstract knowledge visible: carrier ladder, one-to-one mapping, truth ledger, break points | `layered-reveal.md` is the *sequence* (seven layers, one new load each), `domain-standards.md` is factual/terminological authority first, `explainer-narration.md` is voice and lip sync |
| `references/launch-film-grammar.md` | pulling one reference film apart into transferable orchestration elements (arc, 14 elements, evidence levels) | the only *grammar* reference; used for 30 s launch films and chapter reels |
| `references/visual-emphasis.md` | making the viewer see what matters right now: targets, labels, annotation track, occlusion | it is about emphasis inside a shot, not about the story |
| `references/scene-tool-composition.md` | 3D/compositing capability for a scene: HDRI, Blender MCP, Remotion compositions, cross-tool acceptance | the only cross-engine assembly reference |
| `references/opening-design.md` | the first three seconds | a single-purpose reference, default for feed-style work |
| `references/expression-method.md` | how motion/relation/recipe entries combine into an implementation | the bridge from catalog entries to code |
| `references/reference-film-study.md` | taking a finished film apart as *research*, keeping observation/measurement/inference separate | research mode, not production mode |
| `references/extension.md`, `MAINTAINING.md` | adding styles/scenarios/motion without breaking callers | library work, not film work |
| `references/sources.md` | method attribution and the bounds of each borrowed method | provenance; read when you need to know how far a rule reaches |

## 5. Scenarios, and the extra routes

Eight scenarios (chosen by what the audience gains): `product-demo`, `knowledge-explainer`,
`news-brief`, `image-story`, `story-video`, `feature-motion`, `brand-film`, `music-visual`.

Additional routes named by intent: `knowledge-music-explainer` (concept carried by music),
`knowledge-rap-explainer` (rap/hip-hop), `product-music-story` (lyrics + product),
`launch-film-arc` / `feature-chapter-reel` (launch films). Styles and scenarios cross freely.

## 6. Style packs

66 packs, each `styles/<id>/STYLE.md` plus `STYLE.upstream.md` (the upstream rules) and `DEMO.md`
(the case implementation). A pack carries `id`, `name` (Chinese), `aliases`, `category`, colour
tokens, motion character, and pointers into `demo/`. Scripts resolve packs **by id and by Chinese
name** — that is why the Chinese names stay untranslated in this fork.

Rules of use: read the pack's STYLE.md and STYLE.upstream.md, fix this film's intent, then read
DEMO.md and copy only the technique you need into the project. Never run the library's build
scripts in place.

## 7. What is still Chinese, on purpose

- The H1 style names and `aliases` in every `styles/*/STYLE.md` — lookup keys
  (`stylepacks.py resolve 中国水墨`, covered by `test_stylepacks.py`).
- `catalog/*.json` — generated data, keyed by those same names and ids.
- The word lists in `scripts/controlled_lint.py` — it is a Chinese copy linter (`VAGUE_WORDS`,
  `COLLOQUIAL_WORDS`, …). It only makes sense in Chinese.
- Category strings in `scripts/build_gallery.py` (`超级峰原有风格`, `基础风格`).
- A few link anchors that pointed at Chinese headings in upstream documents that are not part of
  this translation.

## 8. Where you actually adapt it

- **Behaviour of a film** → edit the plan (`plan-contract.md` fields: `director`, `scenes[].intent`,
  `viewer_change`, `reveal_order`, `sound`, …). Nothing in the prose needs to change.
- **Look** → a style pack: `stylepacks.py init … --extends <pack>`, then write material, colour,
  type, motion, camera, sound in the new pack's STYLE.md.
- **A recurring kind of film** → a scenario/recipe entry, following `extension.md`.
- **What counts as delivered** → `check_delivery.py` and `plan-contract.md`, not the prose.

The translated prose is documentation for you. The machine contract is the JSON + the scripts.
