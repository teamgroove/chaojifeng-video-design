# From combining expression guidance to implementation

The original motion catalog offers 12 property changes; the expression catalog offers 64 cross-layer expression entries (including 11 knowledge-explainer layers and 14 launch-film elements); the recipe catalog offers 18 combination starting points. The new layers do not replace the underlying stable IDs, and neither the source videos nor the prompts are treated as executable plugins.

## Query by problem

List the scenario candidates first, then look up one to three entries for the problem at hand. Replace SKILL_ROOT with the real path.

```text
python3 SKILL_ROOT/scripts/catalog.py --kind expression list --scenario knowledge-explainer
python3 SKILL_ROOT/scripts/catalog.py --kind expression get narrative.follow-unit
python3 SKILL_ROOT/scripts/catalog.py --kind expression get transition.shared-morph
python3 SKILL_ROOT/scripts/catalog.py --kind expression get sound.event-collision
python3 SKILL_ROOT/scripts/catalog.py --kind recipe list --scenario brand-film
```

| Layer | Problem it solves | Example IDs |
| --- | --- | --- |
| Narrative | In what order the change is organised | narrative.goal-proof、narrative.follow-unit、narrative.energy-arc |
| Camera | How the viewpoint supplies information | camera.focus-frame、camera.waypoint-travel、camera.velocity-match |
| Transition | How two shots keep their relation | transition.shared-morph、transition.match-cut、transition.occlusion-reveal |
| Visual / animation | How structure, quantity and material change | visual.quantity-progress、visual.structure-separate、animation.fill-transfer |
| Type | When the type is read, and when it takes part in the performance | text.semantic-emphasis、text.counter-rotate、text.read-then-move |
| Visual emphasis | Frame the real target, keep labels clear of it and hold their ownership through the camera move | visual.target-callout, paired with camera.focus-frame and text.semantic-emphasis |
| Sound | How beat, action and frequency band relate | sound.beat-map、sound.event-collision、sound.band-response |
| Interaction | How input becomes a reproducible video | interaction.direct-manip、interaction.to-video |
| Style / production | How to keep the rules and exportability | style.token-contract、production.time-function、production.loop-seam |
| Knowledge explainer | How to explain abstract knowledge or news clearly, accurately and layer by layer | knowledge.object-is-explanation、knowledge.layered-reveal、knowledge.truth-ledger、knowledge.evidence-board |
| Launch film | How a product launch film weaves pain, turn, proof and action into one arc | narrative.pain-to-verdict、sound.pivot-drop、narrative.parallel-promise、narrative.cta-as-action、production.dwell-budget |

## See the abstraction layer clearly

Look at tier, source_relation, inputs, parameters, composition, required_capabilities, fallback and verification_questions. A design-control in parameters is a design choice, not an API already implemented or a numeric range. required_capabilities are the semantic capabilities you must probe in order to land the effect; do not copy them into runtime.capabilities and pass them off as measured.

Relation operators, timing constraints, domain operations, combination recipes and production rules can appear together. Letting the type be read to the end before it moves, for example, is a timing constraint; arranging a ring of media around a subject is a composition layout; dissecting a scientific structure needs domain correctness. Do not flatten them all into the same layer of "animation functions".

## Order of implementation

1. Confirm which story beat or information relation it helps; if it does not fit, skip the catalog and design freely.
2. Turn the semantic parameters into this project's executable time, coordinates, material, sound and inputs. A complex effect may be tried on a short segment first; when direct is explicit, make the whole film and check and fix it internally — a test cut is not mandatory.
3. Carry it with an existing motion or the project's own implementation; where there is no ready-made motion, use custom and fill in the original contract's requirements: channels, implementation, composition_reason and the rest.
4. Record the choice in design.expression_ids, design.recipe_id or the shot note. A catalog reference only verifies that the choice exists; it does not arrange shots or drive the renderer.
5. Verify keyframes, continuous motion, sound and semantics for real. When the source only demonstrates part of it, you cannot use that to declare the whole set implemented.

Camera and object moving together need an explicit coordinate space and composition; a match cut needs matching composition/direction/sound; use spring only where the subject's material suits it; a graphic's quantity and area must follow the data. When particle depth, 3D structure, fluid or character performance capability falls short, fall back per the catalog and state the loss.

An interactive demo is not a video that exports on its own. Fix the inputs, the state and the applicable random seed and clock, then check the controlled operation and the final playback. Check seek consistency only when the executor declares random seek; where it does not, use a controlled screen recording or a sequential render and record the limitation. An interactive source provides only the input mechanism — adapting fixed inputs into a video is this skill's design recommendation.

## Scope of verification

The catalog starts as guidance with design=authored; preview/exported are registered to the extent actually covered. A small index sample does not cover every entry. 64 entries are not 64 rendered effects, and 18 recipe classes do not guarantee any arbitrary combination. A new source cannot raise historical verification status automatically; an upgrade must keep the counter-examples and failure conditions. Callout tracks and the scope of checks are in [visual emphasis](visual-emphasis.md); sampled geometry showing no collision does not mean every frame, glyph and meaning has passed.

## Entry point for knowledge explainers

When explaining abstract knowledge or news, read [object is explanation](knowledge-visualization.md) first, then choose the recipe: `object-explainer` for mechanisms, `layered-concept-reveal` to take one concept apart layer by layer, `evidence-board-brief` for news. The 11 `knowledge.*` expressions are design guidance: they specify what must be written into the [knowledge pack](knowledge-pack.md) and what must be delivered on screen; they are not installed motion effects. Domain norms, terminology and controlled expression for the first half are in [domain standards first](domain-standards.md), and the layering is in [layered reveal](layered-reveal.md).

If you select a `knowledge.*` expression, write `plan.knowledge` and run `validate_plan.py`; these checks only cover the mechanical issues of structure, references and copy, and do not prove a fact true, a metaphor apt or the audience's comprehension.

For concept knowledge explainers use `knowledge-music-explainer`; choose subtitles/voiceover and direct/staged per [explainer arrangement](knowledge-music-direction.md), derive the sound-image arrangement from the recipe music pool, the current default or the user's chosen track, organise along the existing knowledge pack and sound contract, and do not make test-cut confirmation a universal gate.

When explaining knowledge through rap/hip-hop, select `knowledge-rap-explainer` automatically; per [rap explainer](knowledge-rap-direction.md), tie each line to fact, actual lyrics, asset, accent and motion settle. A background-music explainer does not switch to rap. When you need characters, 3D, lighting and cross-tool composition, choose one or several routes per [scene and tool composition](scene-tool-composition.md), and in the end watch the real MP4 and check the sound; a catalog illustration does not mean the tool is connected.

## Entry point for product expression

The two new recipes and the boundary scan are in [product expression](product-expression.md). Swapping evidence within one frame, escalating difficulty and semantic slots are combination rules; the underlying work still reuses the original 12 motion effects, and each title/player/brand look is not established as a new atom. A shot note does not widen the machine check or the claim about actual effect.

## Entry point for launch films

For a 30-second product launch film or several features chained together, read [launch film grammar](launch-film-grammar.md) first, then choose the recipe: `launch-film-arc` for a whole-film emotional arc, `feature-chapter-reel` to prove three or four features chapter by chapter; `product-task-proof` still owns the minimal structure of "real task and evidence", and the two do not overlap. The 14 launch-film elements are likewise design guidance, not installed motion: they give the observation basis, a way to transfer the writing and the failure signals, and their numbers are only a starting point taken from one reference film. For sound, always write the event map before laying out the timeline and check it with `audio_event_audit.py`; it measures onset times, not the listening impression. The method for studying another reference film is in [reference film study](reference-film-study.md).

When product promotion is told by lyrics and sections together, choose `product-music-story` from [product music story](product-music-story.md), combining along the existing motion, subject continuity and sound expression; check the film-type fit and the feature claim first, then choose the assets, the opening and the actual sound. It crosses product, brand and music scenarios and adds no underlying motion effect or mandatory contract field; the new recipe still awaits a real finished film and effect verification.
