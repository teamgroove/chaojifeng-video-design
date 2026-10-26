# Let sound take part in narrative and editing

First decide what carries this section: voice, action, ambience, music, or silence. Rehearse sound alongside the shots; do not wait until the picture is finished and then lay down a default bed of background music. A piece with no voiceover is allowed; when the user asks for sound, you may not quietly deliver silence.

## From intent to a sound map

Record the story-level job in director.sound_arc, then record the actual files and absolute times in scenes.audio_cues. Keep the two layers apart: writing “accent on the reveal” is intent only; it is not done until a real audio track and a landing-point check exist. beat_id is referenced inside each contract separately; story beats and real-time beats are linked through scene.intent.beat_ids and the shot content, with no claim of automatic sync.

| Sound's job (声音职责) | How it can be arranged | Common failure |
| --- | --- | --- |
| Point of view / narration | Clear voiceover, breath, only necessary ambience | Music covers the voice; subtitles and reading compete |
| Action / feedback | Clicks, impacts, starts, landings, tails | Big SFX on every small action; sound arrives before the visible cause |
| Anticipation / reveal | Hear it before you see it, accents, short silences, release | The same whoosh on every transition, no layering |
| Continuity / motif | Ambience across shots, repeated timbre, sound bridges | Timbre jumps between shots; tails cut off |
| Section / performance | Organise by musical section, band, motif, variation | Only loudness changes; the picture has no sectional development |

A music / visual film can mark sections, motifs, energy, and release first, then choose the visuals. An action / sound collision requires the same event to drive both; band response needs real analysis or an explicit procedural score — do not pass random flicker off as music analysis. Keep the generating code, parameters, and file sources for procedural sound; for external assets record author, license, and use.

For track selection, key passages, the music score, the two clocks, and local asset linkage see [Music direction](music-direction.md). Choose the passage by the shot's emotional task; do not let a track title or a “tech” label replace the listening pass. Full tracks, variations on the same track, and bridges across tracks are all decided by the narrative.

## SFX and music share one sound character

Set the film's timbre board first, then pick a few action sounds. Music carries section and emotion; SFX carry visible cause, space, and emphasis — add few ornaments where the music is dense, and let voiceover and necessary feedback stand out where you explain. Keep one action family in one timbre; change scale, force, and tail instead of swapping in a new effect every time.

| Expression task | Timbre and action suggestions | Avoid |
| --- | --- | --- |
| Clear, credible product operation | Gentle short clicks, wood or soft tactile; follow only the actual trigger | High-frequency glass rat-tat, a chime on every character |
| System operation and coupling | Steady low-mid pulse, light air layer, few landings | Continuous scanning whine, meaningless looping alarms |
| Capability reveal and scale | Short low-mid accent with natural decay, space before and after | Bass drop on every transition, sudden full-band impact |
| Intimacy and the emotional close | Ambient tails, gentle organic detail, or silence | A melodic chime that breaks the story's afterglow |

Prefer assets you already have clearance for; keep the original license for CC0 and similar sources. Usable libraries include [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds) and [Impact Sounds](https://kenney.nl/assets/impact-sounds) — audition and choose by the actual file; an SFX from a source pack that has not been verified may not be written up as comfortable or as passed. Procedural SFX suit precise feedback: keep the implementation and test-mix it against the real score, and do not let a plain sine sweep stand for the future by default.

When the user reports this round that the sound is harsh, the review pass checks sustained narrow-band highs, dense transients, high-frequency stacking of music and SFX, fatigue, and loudness relationships. A spectrum locates candidate problems; it does not prove how it sounds. Change timbre / reduce stacking first, then control gain, envelope, and EQ as needed — you may not put a uniform low-pass on the finished film and call it solved.

## Rhythm and reading

Distinguish establish, advance, accent, digest, and close; no fixed ratio of fast to slow is required. Let key evidence land, let text be readable, give important changes a before and an after; a musical climax does not have to speed every element up at once. Stable frames, silence, contrast, and empty space can build anticipation. An energy graph is a creative choice; average frame difference or loudness cannot prove the rhythm is good automatically.

Measure the real audio length of the voiceover before laying out subtitles, shots, and motion; keep timings at estimated while they are estimated. Long Chinese titles, dense diagrams, and new concepts may need more dwell. A fast teaser and a teaching film have different goals; do not apply one reading-seconds figure to both. An action hit may land deliberately early or late, but write the intent and actually listen.

For voice reference, background denoise, the person's own timbre, and layering narration, follow [Explainer direction and voice reference](explainer-narration.md). Keep the original recording first, then save a denoised derivative separately; avoid a hard gate that cuts quiet words, sentence ends, and breath. Denoise can also change the voice texture — you may not claim it is clearer or more like the person just because a low-level window got smaller. Compare equal-loudness short passages first, then decide whether the reference and the final narration use the processed version; after changing the actual narration, re-check timing, subtitles, and any related mouth-shape track.

## Mixing and delivery

For musical cues in a knowledge explainer follow [Knowledge music arrangement](knowledge-music-direction.md): a few timbres respectively mark a first appearance, an important result, or a recap; check pitch, tails, masking, and fatigue; where the music already has an accent you may omit the extra cue. Choose the anchor for the main action, for text being fully readable, and for the result landing separately; do not quantise every action to every beat. A one-shot delivery finishes the whole film and checks it internally, with no forced test-cut confirmation, and audio measurement and listening stay consistent.

Separate narration, music, ambience, and SFX layers; keep the edit source or the generating script. Listen for vocal clarity, loudness relationships, peaks, low-end load, transition landings, head / tail, and tails; loudness analysis and the presence of an audio track support technical checks only. Record headphone and speaker checks by what was actually available; do not claim multi-device verification you did not do.

If the host can only generate or analyse audio and cannot play it back, mark audio as partial / not_run and list the waveform, peak, or timing checks done and the items still unheard. You may not count unheard as passed, and you may not call the sound excellent merely because nothing clipped.

## Same-clip A/B and the event list

`sensory-before-after` first fixes the source range, speed, crop, base level, and playback conditions, then changes one layer only; different cuts can only be called a gradual narrative build on the same asset. The options are no SFX / a few soft feedbacks / over-dense feedback, or baseline / plus SFX / plus music — choose after actually listening, and do not assume more is always better.

For each sound write the specific job, visual anchor, asset in and out points, onset offset, film-wide time, gain, and tail. A film-wide mix reference is not a separated SFX track, and an audio element in the code does not mean a stem process was delivered; when old notes / storyboards conflict with the current implementation, read back the actual elements. Waveforms and peaks only assist a technical check; without a listening pass keep not_run / partial. For the detailed method see [Product expression](product-expression.md).

When there are many SFX events (a full launch film), write them into the [audio event map](../templates/audio-event-map.json): `visual_time_s` records the frame of the picture action, `intended_offset_s` records a deliberate lead or lag, `sound_start_s` plus `onset_offset_s` gives the scheduled onset, `tolerance_s` sets the tolerance. The picture action and the sound schedule are generated from the same data; regenerate after any retime; after render, use `audio_event_audit.py` to measure onsets on an SFX-only stem with no music — inside a mix with a music bed every beat hit interferes with the judgement. A single-turn launch film can let the music section carry the main release (break → drop, allowed to lead the picture flip) and keep the other seams lighter; a music film arranges different releases by actual section instead of one drop for the whole film. `film_probe.py` can measure energy valleys and landing points as a technical reference. The tool measures time and energy; the listening pass is logged separately — state the total number of events, the subset actually audited, and what hit and what was not detected, and do not write a subset pass as a whole-track pass. For the method and counter-examples see [Launch film grammar](launch-film-grammar.md#3-sound-write-the-event-map-first-then-lay-out-the-timeline).

## Lyric timing and song revisions

Singing in a song can carry the explanation; do not automatically add TTS or a host. Knowledge rap automatically uses [Rap explainer](knowledge-rap-direction.md); product promotion uses [Product music narrative](product-music-story.md) to judge section jobs; a complex step can cut back to task-led or voiceover-led. For functional lyrics, check the current behaviour, result, and limits first, then make a small sample of the key brand words / feature lines; once the final audio track is fixed, measure the actual sections and durations, and do not substitute estimated beats for lyric in and out points.

For each passage state the method and granularity of the timing: audio measurement, manual marking, recognition, interpolation, or estimate. Sentence-level ASR that splits time evenly across characters can only be logged as interpolation; you may not claim word-level measured sync, and you may not treat recognition accuracy as clarity, timbre, or singing quality. Where necessary, revealing by sentence / phrase only is more honest than unverified fine-grained highlighting.

Log source music time, the post-edit source range, and film time separately; a simple offset can use an explicit mapping, a retime / speed change uses a piecewise relationship; picture, lyrics, SFX, and the audit table all generate from the same valid schedule. A deliberate off-beat gets a written reason and tolerance, and you still have to check the finished film.

To change lyrics, first list the affected claims, singing windows, subtitles, motion, SFX, downstream times, and seams. Reuse the real available stems or replace a local passage, and record honestly when stems are missing; local redraw / vocal suppression may not be judged a pure instrumental just because ASR finds no words. Inside the window listen for residual vocal, timbre, beat, and tails at both ends; outside the window check separately that it held. Unheard stays partial / not_run. Changing only the picture style without regenerating the song keeps the original-audio lock and continues to obey the original constraints.

### Actual sung lyrics, continuity, and version invalidation

Check the final script against the actual sung lyrics line by line; a dropped or wrong word may not be covered up by editing the displayed subtitles; if a necessary factual word is not sung correctly, fix the sound or reword the whole line and verify again. Word-and-note accuracy, consistent voice, developing rhythm / melody, and natural seams are accepted separately. A short passage that earns timbre approval does not cover the whole film's pronunciation, and a similar envelope or a good overall ASR score does not prove line-by-line sync.

When local word fixes keep producing splices, stutter, or voice jumps, stop retrying the same approach, widen to the full phrase / section, and check the context; if continuity is the main problem and the user's constraints allow, consider redoing the whole song. Keep the accepted version and the correct passages, work within the original accompaniment, tool, and resource limits, and do not generalise this one whole-song authorisation into a global default.

A new audio track binds a new hash. After a whole-song regeneration, intro cut, speed change, or retime, the old lyric windows, subtitles, main action, SFX, and downstream timing checks are invalid — re-check the actual sung lyrics first, then measure and re-derive everything from the same valid schedule; you may not just swap the track and keep the old SRT. Sound-and-image notes link claim, lyric, scene, asset, and beat along the [general table](../templates/music-shot-score.md); check key actions at the landing frame where the keyword, accent, or result is visible, not only against the animation start frame.

Check the reading window for each subtitle line and each diagram separately; a section average may not hide a fast line; you can reveal by phrase, continue over two lines, cut modifiers, or run across phrases, but keep numbers, negation, and causal conditions. When audio is unheard, lyrics unverified, or character-level timing is interpolation only, keep the corresponding gap.

## Choose the timekeeper, keep one timing authority

Voiceover-led: use the real per-line audio and measured lengths to lay out reveals and reading. Section-led: lay out visuals by the actual musical sections, accents, gaps, and releases. Task-led: guarantee the cause and the evidence of operation, feedback, and result first, then let the music adapt to the shots. You may switch timekeeper (领拍者) within a film and record why; there is no single rule that the whole music must be locked first.

The story layer follows director.sound_arc, the execution layer follows the existing scenes.audio_cues and the beat_id / scene.intent.beat_ids linkage, keeping main-film absolute time and source in and out points. Any beat / time file exported to the renderer must derive from the same valid plan and record a version or hash; do not build a second, hand-maintained clock. Distinguish measured, manually marked, and estimated. For actions that need strict sync, declare the anchor, offset, and tolerance first and verify at the actual frame rate; a deliberate hear-before-see or a delayed landing is not automatically misaligned, and not every cut and action has to sit on a musical beat.

How prominent an SFX is comes from narrative clarity, action scale, music density, and how it actually sounds; avoid a fixed “always louder than the music” or “always quieter than the music”. Reduce harsh timbres and stacking, then test-mix again, and compare loudness-matched before and after passages; you may not hide the problem by turning everything down.

Choose the loudness target, true-peak ceiling, channels, and delivery spec from the checked requirements of the use or platform, and record the measurement method used; do not set one LUFS number as the standard for all video, and do not treat sample peak as true peak. Verify numeric compliance and comfortable, clear sound separately. When the user needs it you may deliver the music on its own, a mix without voiceover, or usable stems, exported from the real sources; a film-wide mix may not pass as separated music or SFX.

## Content promises and the original-audio constraint

Product feedback, an explanatory turn, a story consequence, a brand motif, and a musical accent can all be important sound events: say why one is needed first, then check along the existing beat / cue and the actual passage whether it is fulfilled. Sound can carry contrast, silence, and bridges; not every event has to be louder and not every beat hit needs an effect; without a listening pass you may not pass it on time labels alone.

When the user explicitly locks the original track or the original sound, use the [conditional branches for shot production planning](shot-production.md#music-and-generation-branches-enabled-by-the-task) and no longer auto-select passages, mix, or add sound; tasks that are not locked continue to arrange by this film's lead sound and narrative jobs. Lyrics, lip sync, and interactive pages are chosen by actual need, are not a requirement for every video, and do not create a second competing timeline.
