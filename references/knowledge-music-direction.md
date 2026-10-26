# Concept knowledge explainer: recipe, music pool and sound-image arrangement

For the `knowledge-music-explainer` recipe. Reuses the knowledge pack, layer-by-layer explanation, the music cue sheet and the SFX event map; it introduces no new engine, paid service, model or required field in the master plan.

This recipe handles subtitled/voiceover explainers that music drives forward. When rap, hip-hop or spoken-word rap is explicitly required for the knowledge, switch automatically to [hip-hop knowledge explainer](knowledge-rap-direction.md) and `knowledge-rap-explainer`, verifying the lyrics and the actual performance before arranging anything; background music alone does not trigger the switch. The two recipes choose their audio track independently, and the new recipe does not inherit this recipe's default music or continuation rules; the existing music pool policy stands.

## Choose the track inside the recipe, derive the arrangement from the music

The recipe's display name is "concept knowledge explainer"; it keeps the original ID for compatibility with existing plans. Elements supply reusable expressions, rules constrain facts, reading and sound-image, the recipe organises the narrative, and direct/staged decides the delivery rhythm; music is a recipe configuration and can be added or swapped in future.

`music_policy.candidate_track_ids` is the candidate list, `default_track_id` is one of them, `planning_mode=music_first`, `default_requires_confirmation=false`. The current initial default is `user-knowledge-sharing-theme`. Read the configuration at run time; never hard-code a track name or ID as a permanent default. An explicit user choice wins, then the project's earlier choice, and with neither, use the recipe default directly — stop asking film by film whether to use the signature track; a request for no music or for original audio is honoured first.

When the user names a track from the library, a track from outside the pool may be used; this choice does not change the music pool. With a new local file specified, check the audio metadata and hash and use it for the current piece; only on an explicit "add it to the recipe" do you register the verified track in the music library and add it to the pool, and only on an explicit "make it the default" do you update the default reference. A new candidate never becomes the default automatically. The default reference and the candidates must resolve; when a source is missing or its hash has changed, name the specific gap — do not quietly switch to the next track.

```text
python3 SKILL_ROOT/scripts/music_library.py select --recipe knowledge-music-explainer
python3 SKILL_ROOT/scripts/music_library.py search --recipe knowledge-music-explainer --limit 5
python3 SKILL_ROOT/scripts/music_library.py select --recipe knowledge-music-explainer --track TRACK_ID
python3 SKILL_ROOT/scripts/music_library.py select --recipe knowledge-music-explainer --project-track TRACK_ID
python3 SKILL_ROOT/scripts/music_library.py select --recipe knowledge-music-explainer --source-file /project/music/chosen.wav
```

`search --recipe` lists only that recipe's candidate clips and returns the default ID; `--silent` or `--original-audio` preserve the corresponding user requirement. `select` only chooses and verifies the chosen local source — it does not render, does not change the default, does not add to the candidates, and does not prove the scope of the music's use or how it sounds. The output is saved into the project as the basis for this choice; source paths still go through the local registry, and files are not copied into the recipe.

Once a track is chosen, analyse its actual sections, density, phrases and checkable anchors first, then hand the knowledge tasks to the places that suit them: establishing the question, setting up the conditions, unfolding the mechanism, revealing the result, comparing the counter-example and closing. Subtitles and motion land after that. With the topic already fixed, keep that topic and its facts — music cannot generate a knowledge conclusion; with the topic open, you may propose a subject that suits this musical expression, but the facts are still verified separately. Necessary conditions, a complete mechanism and reading time come first; if the music is too short, narrow this film's knowledge scope or continue per that track's actual strategy — never delete a key condition to hit the beat.

## Choose the lead mode and the delivery rhythm first

| Branch | How it is organised | Fallback when it fails |
| --- | --- | --- |
| subtitle | Short lines carry the explanation, graphics show the relationships, music drives the sections; once the text is fully on screen, leave time to read and compare | Shorten, split the shot, spread across several beat hits or switch to voiceover; do not delete a necessary condition to hit the beat |
| narration | Get the real voiceover first and measure it, reveal along the semantics; music supports the emphasis and the pauses | Lower the score/prompt density, extend the mechanism demonstration, switch to sentence-level reveal |

When the user explicitly asks for one pass, direct to film, no test cut or no intermediate confirmation, `delivery_mode=direct`: make the whole film directly and complete the internal checks and any necessary rework in the same round; do not force a 10-second render first, do not require picking a direction, approving a test cut or approving section by section. Necessary stills, audio probes and the final check can be done internally — do not dress them up as user confirmation gates. When the user explicitly asks to review stage by stage, use `staged` and wait only at the agreed nodes. When unspecified, decide the necessary low-cost checks yourself and carry on to completion; no fixed stop-and-wait.

Skipping the test cut does not skip the fact, reading-window, audio, continuous-playback and export checks. A missing necessary fact, an unavailable capability or a cost boundary is still reported accurately as a blocker; direct is no licence to fake completion. Honour a specified track, original audio or a no-music requirement; when the user delegates the decision and needs no intermediate confirmation, go ahead and pick a suitable existing candidate.

## Let the content form an explainable relationship first

Write one sentence stating a relationship the viewer can repeat afterwards, verify the terms, the numbers and the conditions under which it holds, then choose the carrier. Place the added load, the bridges and the boundaries on the existing L0–L6; short films merge sections by content — do not fill seven sections to satisfy a template. You may use "question → prediction → visible consequence → explanation → boundary → return"; where the subject does not lend itself to prediction, go straight to comparison or demonstration — do not manufacture suspense.

For each shot write: claim/layer, what the viewer gains, the focus, subtitle or voiceover, the initial state and the visible change, the settle and the reading window, sound's job, the handoff to the next shot. Add relationships along the same object and create variation through close shot size, scale, density and negative space. Where something only moves and carries no new information, cut the motion. The recipe gives a starting point, not a fixed dark ground with gold type, particles, shot count, BPM, length, title timing or turn ratio.

## The music map: reuse the source analysis, recompute the schedule per film

The map binds `track_id` and `source_sha256` and records source-time anchors, type (beat/downbeat/phrase/section), analysis method, evidence and candidate/verified status. It can be stored separately in the project; when filling the task sheet, reference the anchors used exactly as they are. Re-verify after the source hash changes. Automatic candidates work alongside actual listening; do not force a model install for one tempo value.

Tempo describes only fast or slow; beat positions also need the first beat. Half/double time, time signature and local tempo change are judged separately. Only a steady tempo justifies deriving an equidistant grid from the first beat; a changing tempo keeps the actual sequence. Waveform peaks and energy jumps are candidate transients and are not automatically promoted to downbeats or phrase starts. Only a range that was checked is marked verified, and the evidence is kept; a hand-marked range does not automatically cover the whole track either.

The current initial default track `user-knowledge-sharing-theme` already has 119.083 seconds of source audio and basic signal information; the not-auditioned, not-beat-measured state stands until it is actually verified. At run time the default is whatever the recipe currently references; after a track change, re-check the map against the new hash and inherit nothing from the old track's tempo, beats, phrases, key or audition state. The 113 BPM of the reference tutorial and of other works cannot be transplanted.

| Sync level | The task it suits | Handling a conflict |
| --- | --- | --- |
| Beat hit | Lighting up, an impact, one state change | Pick only events with meaning; do not prompt word by word, beat by beat |
| Local accent / bar | Establishing a short line, settling a step | Choose by the actual time signature; do not assume four beats |
| Phrase | One relationship, one comparison, one complete process | Complex knowledge spans several beat hits; keep the reading window |
| Section | Turning from question to explanation, revealing the consequence, the close | Choose by content; do not copy one episode's fixed second marks |

A visual anchor is the moment a keyword becomes fully readable, objects actually touch, a result first holds, or a relationship settles. Animation may start earlier and settle on the anchor; aligning only the animation's start time is not enough. Facts, causality and reading outrank hitting the beat; you may take a later phrase, split the sentence and the shot, or move less. Deliberate off-beat placement records the offset and the reason.

## Sound prompts and continuing the same track

Try a few timbres and their jobs first: first appearance, important result, recap or counter-example. Piano, glockenspiel and wooden single notes are all only candidates — test-mix them against the track's actual pitch, timbre and tails; without a key measurement, do not call them in key. When the music already gives a clear accent, you can skip stacking another sound. Reduce sustained high frequencies, dense transients and stacked long tails; a prompt sound must not mask the voiceover. Where short ducking is needed, treat only the necessary events and listen for pumping or unnaturalness.

Every sound answers "what information does this prompt", and is logged along the existing audio-event-map with the action time, the actual onset, the offset and the tolerance. The task sheet's check compares the schedule only; actual onsets are still measured with the music-free SFX stem and `audio_event_audit.py`, and the mix relationship is listened to separately.

The current signature track keeps the strategy the user confirmed: trim for short films; for long films take the next pass from the top of the track and cut the excess, and continue again only if that is still not enough. Do not silently switch to re-editing, time-stretching or another loop section; other tracks decide their own fitting strategy and do not inherit this continuation rule just by joining this recipe. Each placement gets a different cue ID, same track and same hash, with the source interval and the film interval recorded separately; listen to the seam, the first hit, the tail and the ending. Recompute every mapping and anchor after a picture change; a duration that now adds up does not by itself prove the join is seamless.

## The optional task sheet and the timing check

`templates/knowledge-music-score.json` is an internal optional side record and does not drive rendering automatically. The template references the minimal plan shipped with the pack, with the music empty, for structural checking; after copying, refill it with the current plan hash and the real IDs. Old plans need no backfilled fields.

- `plan_sha256` binds the current master plan's raw bytes. Execution times still live only in the plan's beats/audio_cues; the task sheet references them by ID and no longer hand-writes the same action time.
- `delivery_mode` is direct/staged, `lead_mode` is subtitle/narration; `decision_reason` records the actual basis for the choice and does not fabricate the user's words.
- `reading_windows[]` names the scene, the element, the two beat IDs for fully readable and exit, `min_read_seconds` and `reason`; it may reference `claim_ids` and `layer_id`. Character capacity is a first filter only; formulas, terminology and graphical comparisons get their own time.
- The optional `music_map` holds the source identity, the source-time anchors and the evidence; the optional `sync_points[]` links the plan's visual beat to the cue sheet placement and the source anchor, stating `intended_offset_s` and `tolerance_s`. `audio_cue_id` plus `onset_offset_s` allows checking the SFX schedule, but still does not represent a measurement.
- Source anchor to finished-film time: `timeline_start + (source_time - source_in) / playback_rate`. Check the same hash, the source interval, the rate and the length first; a continuation must pick the right placement ID.

```text
python3 SKILL_ROOT/scripts/explainer_timing_audit.py score.json --plan plan.json --music-sheet music-cue-sheet.json --out timing-audit.json
```

It checks IDs, hashes, windows against the declared tolerances, the source-to-film mapping and schedule drift; it is valid only for what the current task sheet covers, and it does not automatically detect real beats, the pixel readability of subtitles, SFX onsets, harmony, aesthetics or comprehension. Candidate music anchors raise a warning and do not pass themselves off as verified. The master plan and the cue sheet are still validated independently by their own tools.

## Production, transfer and effect

direct completes the whole film in one run, then checks and fixes internally. Other jobs may check the opening, the hardest mechanism and the important turns first, covering them with one short segment where the risks coincide; 10 seconds is only the reference tutorial's opening starting point, and staged waits only at the nodes the user named. Keep stable IDs and rollbacks so the whole film is not regenerated again and again.

Reuse a small set of text, comparison, process-track, chart and emphasis components, and fix the terminology, visual semantics, timbres and time interfaces; each episode swaps the question, the evidence, the carrier and the turn. Validate the transfer first with subjects built on different relationship types, recording factual errors, reading problems, timing drift, rework and cost separately; one film does not declare the method stable.

Record the actual review and the first viewers' retellings separately. Where publication data is available, look at opening drop-off, average view, completion, rewatches, saves and the specific questions, on the same platform and among comparable subjects and lengths; no uniform threshold is preset, and completion is not a stand-in for comprehension. One round of feedback supports revisions in its own scope only and does not automatically become "works for every subject".

Sources: the four steps of the local tutorial and its in-film subtitles are observations; the layered sync, the two branches, direct and the timing check are original adaptations for this Skill. See the [beat note](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C6/C6S2_TempoBeat.html) and the [multimedia learning principles](https://www.cambridge.org/core/books/abs/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning/F29A19FCD34C542806F736E0661C05F5). One tutorial can only support that the method exists, not that this recipe has any audience or distribution effect; the original film, the source audio and private conversations are not distributed.
