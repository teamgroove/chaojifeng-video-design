# Asset performance and routing

Read this when an existing image, interface, chart, logo, or media clip has to move on its own, be put back, hand off (接力), or be reused across shots. First pin down the change you want to express along [Shot production planning](shot-production.md), then judge which assets can be operated on safely; adjust the shot by what was actually prepared. The method applies to every scene; it does not require layering every image or a big move in every shot.

## First define the complete unit of motion

Identify the subject, evidence, label, and background that genuinely have to carry the motion. Prefer existing editable components, vectors, separate images, or reliable original pixels; where the tools fall short you can select the complete region by hand. Use matting, background fill, depth, or generative tools within current authorisation and actual capability — this skill ships none of those executors and downloads no model by default.

- Group by function and semantics: a control together with its necessary states, a value together with its unit, a person together with the appearance that must hold, an object together with the attached parts that must move with it.
- Split smaller only where the motion truly needs it; keep parts whose relationship is unclear in one group. A pixel layer is not a real engineering structure, and you may not infer internal assembly from an occluded area.
- Mark the text, data, identity, and product states that must be protected. Move a rigid unit as a whole or split it explicitly; avoid accidentally stretching letterforms, faces, and product proportions.
- Give every main action a destination or a visible consequence. A camera move, a change of environment, or small local motion can also serve the content; do not judge quality by the number of moves or the size of a displacement.

## Build a reusable part record

A complex asset can be recorded along [Asset stage notes](../templates/asset-stage.md); a simple task needs only a few sentences. Records link to the existing asset / scene / element / beat IDs and add no required plan fields and no separate execution protocol.

| Record | Purpose |
| --- | --- |
| Original basis and derivation | Original file, scope of use, version / hash; normalised working source, processing method, and paths of derived parts |
| Complete unit | Object's job, the parts that move together, facts that must not change, and protected regions |
| Coordinates and anchors | Coordinate space it belongs to, canvas size, crop box, local origin, rotation / scale anchor, source-to-scene mapping |
| Occlusion and exposed backing (露底) | Front-to-back order, related masks, occluded or unobserved regions, the background exposed after the move, and the credible range |
| Motion and binding | Shots used, elements, main action, responding events, valid time range, landing state, and handoff to the next shot |
| Evidence and limits | Source states actually checked, motion range, and sample clips; missing parts, substitutes, cache dependencies, and open items |

A file existing does not mean it is usable; a part that stacks back statically does not mean it can be rotated, scaled up, or leave its position freely. Record only enough to support the current action, and do not scan or copy the whole asset library.

## State the spatial relationships clearly

Note the transform and the unit along “original file → normalised working source → local coordinates of the cropped part → scene → output screen”. After a change of original orientation, resampling, crop, scale, or aspect ratio, re-check the mapping; you may not treat local coordinates as screen coordinates directly.

The subject in the scene moves with the camera; on-screen subtitles and fixed labels stay on the screen layer as their use requires. Say which properties the camera, the container, and the object each own, and avoid duplicate pan / scale. Existing [Motion annotation](visual-emphasis.md) keeps using the same mapping, targets, and protected regions instead of inventing a competing coordinate contract.

Depth estimation is only a spatial hint. Order by the actual occlusion relationships; a crossing occlusion may need grouping, masking, or a different camera position; you may not infer the full front-to-back relationship from a single average depth value, and certainly may not promise real 3D from any angle on the strength of one image.

## Let the exposed-backing condition set the range of motion

Look first at what appears once the subject moves away. Distinguish a real existing background, a simple graphic continuation, an explicit creative fill, and unknown hidden content; a patched or generated background may not pass as the original photo, product interface, or data evidence.

When an unreliable region would enter frame, choose a smaller displacement, keep the occlusion, move the whole thing, change the shot size, adjust the camera relationship, or add real footage. Keep the reason for the choice; you may not hide necessary information long-term behind smoke, glow, or decoration. Check transparent objects, reflections, thin edges, hair, holes, and large exposed areas at actual size, and do not pass them because a mask file exists.

## Organise motion around one event

First write “trigger → main object acts → arrives / contacts → related objects respond → result lands → handoff”. Cut by content; a collision-free, silent, or reading-dwell passage is allowed; do not let each layer play its own unrelated loop.

A path, a distance, a section, or a real operation can set the response order; concrete times land along the existing shot, beat, and audio_cue. Sound and picture bind to the same event, with estimate and measurement kept apart. When an object hands over between containers, state when display and control transfer, so that two copies of the subject never appear and no shadow / label is lost.

Reuse existing expressions by goal: visual.structure-separate where the structure has a basis; transition.frame-breakout or narrative.follow-unit for an object handoff; transition.occlusion-reveal for an occlusion reveal; animation.path-reveal, stagger, and sound.event-collision for paths and responses; parallax for spatial layering; animation.spring-settle for the landing. They are expression choices and do not prepare assets or give you execution capability on their own.

## Restore first, then test maximum motion

1. Put the parts back into the agreed source state and check for missing edges, misalignment, ghosting, layer order, necessary text, and protected regions. A difference needs a judgement: is it an error, or a new composition / creative change you already stated.
2. Check the actual motion's maximum displacement, scale-up, rotation, occlusion change, camera bounds, and newly exposed background; look at the short passage most likely to break first, then complete the corresponding range.
3. Check the continuous passage and the shot seams at real viewing size, and listen to the related sound where needed. Automatic geometry, pixel, or frame-difference checks only locate candidate problems; they do not prove completeness, aesthetics, or comprehension.

Save range, problem, change, and re-check along [Review method](review-and-revision.md). A local pass does not extend to the whole asset, all parameters, or all shots; unseen, unheard, or unmeasured stays a gap.

## Reuse across shots and output

One part reuses its prepared result; each shot binds its own motion and does not reprocess the same source image. After a change of source file, working size, crop, mask, background, or type, re-check the shots and annotations that depend on it. Keep the original basis and the necessary editable source; cleanup touches only intermediate files clearly owned by this task and no longer needed.

Reuse frame caches by valid version of asset, layout, time, frame rate, seed, and render environment; reuse a new format only when the picture sequence still applies and the output spec is met. Changing the aspect ratio requires re-checking the composition; do not auto-crop an old cut.

A single reveal, a continuous environment, a cross-shot handoff, and a loop are all options. When you need a loop, check start and end position, speed, occlusion, and sound along production.loop-seam; extra reset frames also count into film duration, so you may not quietly lengthen the shot. When a silent visual passage enters a film with sound, continue to composite and accept it along the original sound contract.

This reference is independently written method guidance; the sources drawn on and the boundary of actual observation are in [sources.md](sources.md). It contains no third-party implementation, work, or model, and it does not treat the asset-processing pass as an installed engine or a verified finished film.
