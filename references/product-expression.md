# Product expression: making task, evidence and feeling hold together at once

Pick the through-line (main line) from a real task first, then decide how to show it. Default to advancing on a single plan, and unpack the [shot task template](../templates/product-shot.md) only for complex shots; it is a design note, not a new mandatory step.

## Pick the entry point by problem

| Current problem | Entry point | When to skip |
| --- | --- | --- |
| How to turn a feature into a useful product story | `product-task-proof` | For a single local motion effect, write initial state/trigger/end state directly |
| Why the old approach is not enough | recipe branch `problem-reframe-opening` | The old approach is already adequate; the limitation cannot be proven |
| How to prove several capabilities without just listing headlines | recipe branch `claim-evidence-chapters` | One piece of evidence is enough; a fixed frame shrinks the content |
| What the sound/visual enhancement actually changed | `sensory-before-after` | No comparable baseline, no asset rights, or no way to actually watch and listen |
| How to keep in-progress and done apart | `visual.scan-resolve` | Cutting straight to the real result is clearer; there is no processing stage worth explaining |
| The emotional arc of a whole 30-second launch film (hook → pain → turn → self-proof → action → sign-off) | `launch-film-arc`, elements and derivation in [launch-film grammar](launch-film-grammar.md) | An 8–15 second single-feature film takes only one or two elements; if the audience already knows the pain, start at the call |
| How to prove three or four features chapter by chapter with one sentence pattern | `feature-chapter-reel` | Only one feature; the fixed pattern shrinks the content instead |

Escalate difficulty with only as many layers as the content needs. Each layer adds a specific friction; it does not restate the same difficulty louder. The reference film's shot count, opening/result ratio, fast-typing speed and brand aesthetic are not defaults.

## Give every claim its evidence

Tag the shot's material as input, intermediate or result and say what it proves. A prompt image board, a terminal mid-run, a placeholder cell or success text does not by itself prove the whole task completed. Keep real components/screen recording, hand-built reconstruction, process diagram and concept design clearly apart; a diagrammatic frame does not fake the actual runtime.

One section carries one main focus. The headline names the section, the picture proves it, and the camera leaves enough reading time after it settles. A stable stage can carry code, process, review and result, but a player chrome is not required. If it is unreadable on a small screen, drop the shell, enlarge the key point or split the shot — do not rescue it with more rules and borders.

The processing state comes from a real source or an explicitly defined demonstration. Unknown progress gets no precise percentage. success, partial and failure each keep their correct outcome; on failure show a recognisable consequence, never the success celebration. A scan inside an object only shows where attention sits; check `visual.scan-resolve` for its target boundary, state binding and result dwell.

## Shot handoff and template adaptation

- Establish cross-shot object identity first, then choose the anchor: link → page, card → result, or text → composition. Same shape is not the same object, and a semantic link does not force a morph.
- A seam records the outgoing and incoming carrier object, direction, axis, cut point and the reason for locking. Consistent direction does not mean the speeds already match; shot matching still needs an actual viewing.
- When retargeting a template, swap in the product's own input, processing, output and action entry first, then colour/type/brand. Keep the motion relationships that work, and re-flow the geometry once the long Chinese copy, different images and aspect ratio change.
- A drag puts the grab point and the object into the same state relationship; an object entering or leaving a container handles occlusion, and text counter-rotates on its own where needed. Visual preparation may overlap; a real submit/payment/delete confirmation must not succeed early.
- A knowledge explainer can map key phrases onto on-screen elements — read first, then concretise; this is a design mapping, not a claim that arbitrary text compiles itself into scenes.

## Sound: responsibility first, assets second

The lead sound and the music carry comprehension and sectioning; a few same-family action sounds carry operation confirmation, spatial movement, section turns, state settling or brand sign-off. Not every displacement needs a whoosh, not every character a click. A product's lightness, pleasure and technical feel come from rhythm, precise feedback and apt timbre — not from continuous high-pitched tones or bass bombardment.

Write the event and its visible trigger frame first, then choose the actual file, source in/out points, film time, onset offset, gain and tail. A file's start is not necessarily the onset you hear. A stem pulled from an existing mix can only serve as reference, never be labelled a clean effect you can layer on its own. For music selection keep searching moods and key passages per [music direction](music-direction.md); do not use the whole reference track as the default bed.

When there are many effects, write the events into one [event map](../templates/audio-event-map.json): scheduled time = action time + onset offset, generated from that same data and regenerated after any retiming; after render, `audio_event_audit.py` checks the actual onsets against the schedule as anchor. In the reference film the effects declared for the opening ran +0.56 to +1.82 seconds behind the picture action (one declaration even exceeded the length of its own scene), while the send sound in the comparison lined up; the drift looks like effects that were not updated after the opening was retimed — that is an inference, with no production record to prove it. The sound division at turns and seams: see [launch-film grammar](launch-film-grammar.md#3-sound-write-the-event-map-first-then-lay-out-the-timeline).

When you need a comparison: fix the asset interval, speed, crop, base loudness and playback conditions first; change only one sound layer or one visual layer. You can run no effects / a few soft feedbacks / over-dense feedback, or baseline / add effects / add music. Keep the base layer identical and record the loudness difference separately so louder does not pass for better; do not assume more layers are better. Replaying different intervals can serve the narrative but is not a strict A/B. When the current host cannot listen back, keep it un-auditioned — do not let a waveform, a label, a soft filename or a peak level stand in for hearing.

## Inner and outer clocks, and the ending

The plan still uses absolute seconds of the whole film. Embedded media records its own source in/out points, film start and end, rate and replay; the time an in-film player shows is not the outer film's event time. Within a constant-speed forward-play window:

`source_time = source_in + (film_time - timeline_start) * playback_rate`

A speed change, freeze, loop or piecewise remapping must be recorded per segment; a transition overlap does not mean the source media plays from zero. Check the parent scene length, the child animation's end, the audio track's real end and the tail separately. Test seek consistency only where the executor supports random seek; otherwise use sequential playback / controlled screen recording, and do not widen the availability claim.

## Minimum verification

Start with 8–12 seconds of the hardest relationship or one piece of real task evidence, adjusting duration to the content. Check the four task end states, headline/evidence pairs, small-screen readability, sound onsets/tails and seams. Then do one substitution with long Chinese copy/product assets and check local editability; when you need a sound-layer comparison, actually audition the aligned versions. The structural examples are in [task plan](../examples/product-task-proof.plan.json) and [before-and-after plan](../examples/sensory-before-after.plan.json); neither is a rendered piece.

Record design, implementation, keyframe viewing, continuous playback, listening pass and audience feedback item by item. A structural check cannot prove a real task completed, nor taste, comfort or comprehension benefit. Reference scope and ownership: see [sources.md](sources.md).
