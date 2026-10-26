# Review and local revision

| Dimension | What to check | Boundary |
| --- | --- | --- |
| structure | IDs, references, timing, assets, capabilities, plan and artifact agree | automated checks do not verify knowledge or taste |
| semantic | sources, units, cause and branch, function matching the picture | use independent primary material; do not let the same flawed extraction vouch for itself |
| visual | long Chinese text, cropping, contrast, hierarchy, occlusion, subtitle safe area | actually look; filled pixels are not effective information |
| playback | full duration, continuous playback, black and flashed frames, transitions and misalignment | keep metadata, sampling and full playback separate |
| audio | audio track, peaks, intelligibility, landing points, starts and endings | actually listen; declarations and hashes do not guarantee how it sounds |
| comprehension | whether the viewer can correctly explain or act on it | real feedback or experiment; if not done, not_run |

passed records the observation or the path to the evidence. Record the design mock-up, the existence of source, the preview and the export separately. Text on the image can pass a geometric check and still be unreadable; a background SVG raises the density; a static frame can be legitimate reading time, and a large frame difference can be meaningless.

Actually look at the first frame, the densest frame, the moment the relationship lands, on-image text, motion extremes, entrances and exits, and transitions. Contact sheets and dense strips are for locating; then look at full size and in continuous video. If you have not watched or listened, do not mark it passed. Cover long titles, image proportions, text on a dark ground, and changes of type or language. Check shot by shot what the viewer gains, the focus, what the transformation means, conflicts between copy and voiceover, and the dwell. A timing formula is not the whole standard for an audience.

## Default triggers and delivery when a required item fails

For a feed explainer or a promo, always check the first frame and the first three seconds: record the actual range of the first useful information, the first spoken line, the payoff on screen and the handover into the body, and do not let an empty preamble or brand idling hold the opening. For factual visuals check whether primary material was actually retrieved, where the gaps and the generation boundary are; with lyrics check facts, the words actually sung, subtitles, the main action and the phrase handoff line by line. Having read the rules or written a storyboard does not count as having executed them.

When a known core lyric is unsung, a fact is wrong, subtitles are visibly out of place, a long wait does not match the brief, required sound is missing, or a seam the user already rejected is still open, keep locating and rework it; if it cannot be finished, state the specific blocker and label the version explicitly as candidate / not passed. A successful export, a high automatic score or an honest disclosure of defects does not turn a required item into a completed one. Record the technical check, the director's self-review, full viewing, the actual listening pass and user acceptance separately; do not cover failed items with one overall pass count.

After a track change, reset lyric coverage, subtitle/action/SFX sync and the sound checks; keep the old record instead of inheriting the accepted state. Accept lyric-to-voice, timbre, rhythm/melody, mix and seams separately; with no listening capability, leave audio at partial/not_run and list the ranges awaiting a listen — do not claim the sound is up to standard, and do not default to a per-film test-cut confirmation gate because of it.

When you use an asset library, HDRI or Japanese narration, check character and motion fit, source and licence, plan and file hashes against the [production tool contract](production-tool-contract.md), and check the lighting/reflection baseline and candidates for the same shot, the actual still or clip range, and the cost. `production_tools.py check --require-reviewed` rejects only registered but unfinished lighting or listening declarations; it does not replace looking at pixels, listening to sound, or checking the whole film. An available API, a connectable MCP, a successful import and a visual improvement are accepted one by one.

When you use [dynamic annotation](visual-emphasis.md), also check the whole operation unit, label semantics, step or mutual-exclusion numbering, text protection, leader-line ownership, crop re-baseline and following during the move. Look at the full shot, the detail, the contact sheet at the key moment and the continuous clip at the size it will actually be watched; especially check annotation enter/exit, camera extremes, subtitle changes and the target leaving frame. An independent geometry check records the sampling range only and at most reaches awaiting_visual_review; it cannot inherit a pass from screenshots or from an older cut.

## The director's six review questions

Keep a short review record in the project: for each item write the range watched or listened to, the time point of the problem, the reason and the outcome of the revision. delivery.checks evidence can point at the same record; there is no need to rebuild the old delivery contract.

| Dimension | Judgement and failure signal | Delivery check it maps to |
| --- | --- | --- |
| Sound | lead and secondary are clear, action and cause connect, tails and starts and ends are natural; do not just check that a track exists | audio |
| Picture | subject, space, text and continuity are clear; generation faults are handled as a content boundary | visual, playback |
| Taste | type, colour, material, light and the character of the motion match the brand; state the reason for the judgement | visual |
| Rhythm | build, drive, accent, reading and release hold up; fast and loud is not rhythm | playback, audio |
| Narrative | every shot carries a change in information or feeling, and element mission and through-line can be traced; without an audience test do not call comprehension passed | semantic, comprehension |
| Tech feel | precise response, structure, material and sound serve this content; decoration must not hide evidence | visual, semantic, audio |

For a brand film check the vision and the factual boundary, motif consistency and the emotional arc; for a music film check sections, variation, sound-image linkage and seams, and do not impose a character story. Mute, hidden text and random seek are diagnostics only where they apply, and cannot be prescribed as a pass requirement for every film type. Keep the reviewer's aesthetic judgement separate from the first-time viewer's retelling; do not use directorial intent to prove how the audience feels.

When revising, locate the scene/element/beat/narration ID, read the plan and the implementation first, list the blast radius, then act. Do not regenerate the whole film unnecessarily or ask the user to fix it by hand.

| Change | Dependencies to re-verify |
| --- | --- |
| colour / type / layout | brand, character width, contrast, occlusion, the corresponding frames and artifact |
| title / body copy | facts, capacity, dwell, subtitles and the shots involved |
| voiceover / timbre / pace | measured duration, subtitles, marks, downstream timing, cue and mix |
| motion / camera / transition | property conflicts, cropping, state before and after, clock and boundary |
| box / label / leader line | source-to-screen mapping, the whole target, text and subtitle protection, enter and exit, numbering semantics and the actual displayed type size |
| data / product feature | primary evidence, scale and units, real state and the claim |
| asset or generated content | source, subject consistency, file hash and the shots that use it |
| through-line / character mission / reveal order | story beats, adjacent shots, identity, camera angle, the sound bridge and what the viewer gains |
| music section / rhythm / energy | action landing points, reading windows, voiceover clarity, mix, tails and the loop seam |

Save the revision and the change ID. Re-export and update the hash after the video bytes change; a local preview verifies only the range it covers. Without reliable local rendering you may re-render the whole film, but change only the necessary source. One engine blocking an old audio track does not generalise to every branch.

On failure read the log and the runtime state first, and separate asset, plan, executor, font, encoding, model and policy. Keep the source and the error, fix what can be fixed; if you cannot proceed safely, report the actual artifact and the blocker. Reducing decoration, splitting shots, holding longer or going static are options, but never silently drop required content or sound.

## Product evidence and comparison review

Per chapter, check the claim against readable evidence, and separate input, intermediate state, result and mock-up; check running/success/partial/failure separately, and do not let one successful motion cover every state. Check inner and outer clock against the actual asset range, and check the parent duration, the end of the child animation and the sound tail on their own. When the fixed stage shrinks the evidence, change to a closer shot; after replacing long Chinese text, re-verify the geometry.

For a before/after comparison record the fixed conditions and the single layer that changed; replays of different clips are not a strict A/B, and different loudness is listed separately. Judge clarity, taste and fatigue only after actually watching and listening. When you change a media start, a rate or a shot duration, re-verify the affected annotations, sound-image anchors, tails and downstream timing. Do random seek only on executors that support it; elsewhere verify by sequential playback or a controlled screen recording.

## Measured review of the finished film, and reference-film study

After the cut, use `film_probe.py` to take shot cut points, each section's share, loudness and true peak, energy valleys and the palette, and compare the cut points one by one with the scene starts in the plan; it only says "what appeared" — watching and listening are recorded separately. For SFX use `audio_event_audit.py` on an SFX-only stem with no music: for `schedule_drift` regenerate the schedule from the event map first, for `late` or `early` check `onset_offset_s`, for `missing` check the file, the gain and masking. Loudness and peak are technical parameters and do not prove comfort; with no re-listen, record audio as partial or not_run. Then answer [the finished-film self-check in launch-film grammar](launch-film-grammar.md#6-finished-film-self-check-answer-each-line-if-you-cannot-rework) line by line, and rework anything you cannot answer first.

When you study someone else's finished film, grade it per [reference-film study](reference-film-study.md): source and frames are observation, instrument measurement is measurement, the rest is inference — if you have not listened, write that you have not listened; samples from the same source are not independent evidence, and one film cannot prove that something works.

## Reviewing a knowledge explainer and a news brief

When you use `knowledge-music-explainer`, check per [knowledge explainer direction](knowledge-music-direction.md) who takes the lead beat, the knowledge increment, the reading window after the text has fully appeared, where the visible result lands, the music mapping, hint density and the seam between pieces on the same track. `explainer_timing_audit.py` verifies only the schedule the task table covers, and does not replace checks of actual beat, pixels, SFX onset, listening or comprehension. direct has no test-cut confirmation gate, but the final internal check and the necessary rework still have to be done; staged waits only at the nodes the user named. With no real audience and no platform feedback, record each as not_run; machine checks cannot claim that a film is engaging.

When you use a [knowledge pack](knowledge-pack.md), treat `checks` as the structure of the review record: terminology checks term consistency and pronunciation, accuracy reconciles the ground-truth ledger with the primary source, and novice_read, peer_read and expert_read ask a newcomer, a peer and someone who knows the field to read it. Each kind of reader describes independently "what I saw, what I learned, what is wrong", then compare with directorial intent; when the same agent checks, say that it is a self-check. What was not really done stays `not_run`; "looks right" cannot be written as `passed`.

| Change | Dependencies to re-verify |
| --- | --- |
| number, fact or source | the ground-truth ledger, every derived value and every voiceover, subtitle and readout that cites it; an existing `passed` on accuracy and expert_read is reset |
| term or reading | the term card, wording across the film, the pronunciation list and the voice track; terminology is reset |
| layer order, bridge or new load | the bridge between adjacent layers, the exit test, the key element; novice_read is reset |
| carrier or mapping | one-to-one mapping, the four questions, the break point, the model boundary in L6 |
| standard version or check date | the standard's status, the claims and terms that cite it; a check older than one year is looked up again |

For a news brief check in addition: each fact's `as_of`, whether numbers on different definitions are put on the same ruler, and whether unconfirmed and disputed items stay visible. A tidy layout does not mean it has been verified.

## Reference comparison and bounded rework

The review uses this brief, the factual basis, the chosen reference range, the actual artifact and the check target; let the reviewer describe what they see independently first, then compare with directorial intent. Choose a genuinely available independent reviewer according to host permissions and the task's authorisation; when the same agent checks, write that it is a self-check and do not pass it off as a fresh review. With no separate instance, do not invent a reviewer identity. You may concentrate reviews on the sample of the hardest relationship, the key rough cut and the final cut, rather than opening a new agent for every shot or every export.

Record the table below in the review file the project already has, and let delivery.checks.evidence point at it; there is no obligation to create a ledger.md or to extend the validator. For reference gaps and key moments see [creative direction](creative-direction.md).

| Record item | Requirement |
| --- | --- |
| Object and range | revision, artifact hash, scene/element/beat ID and the range actually watched or listened to |
| Problem and level | time point or frame range, blocking / major / minor, the specific observation and its effect on the viewer |
| Evidence | full-size frames, continuous clips, measured data or a description of the actual listening; a value not measured is recorded as unknown |
| Revision and re-check | what changes, why it comes first, which dependencies it affects, the re-check method, range and result |
| Conclusion and remainder | fixed, not fixed or awaiting verification; self-check or independent reviewer identity, resource ceiling and reason for stopping |

You may use a muted retelling to locate a problem in the visual through-line, but the reviewer's retelling is not a user comprehension experiment; a pure audio check also cannot prove the full sound-and-image experience. Choose the frame-sampling density by motion, seams and risk; do not fix one frame every 0.2 seconds for the whole film. When you compare against a reference, state the specific goal and the gap; do not just rate it "premium / shippable".

Fix the biggest problem first, and re-verify the affected range serially; after a full export run the necessary finished-film checks again for the delivery scope, instead of carrying over the conclusions from before the change. Write the iteration ceiling and the stop condition before you start; when the requirements are not met, record the remaining problems and the usable version rather than reworking indefinitely. A reviewer saying it is deliverable is not the user approving a public release; actual playback, the listening pass and audience tests are each accounted separately.

## Realising the expression, and cross-shot continuity

Check the actual clip against the key changes and the aesthetic boundary in [creative direction](creative-direction.md): does the product show a real operational consequence, does the knowledge present the right conditions and relations, does the news brief separate the basis from the unknown, does the story carry the action forward, do the brand or the music have a discernible development and release. Record the expectation, the actual sound-image evidence, the gap and the reason for restraint; this is not counting effects, and it does not require a fixed hook or twist in every film.

Check fixed and variable items along [shot production planning](shot-production.md). After a shot change, re-verify adjacent identity or product state, spatial direction, colour and light, reference responsibility, text space, sound tails and downstream timing; a local pass is not inherited as a pass for the whole film. When you check only source or key frames, keep the viewing gap; when you have not listened, keep the listening gap; user comprehension and distribution effect still need real feedback.

## Re-checking asset parts and the motion range

When you use [asset motion and routing](asset-motion-direction.md), account on three levels: whether the source state composites back correctly; whether the actual motion extremes show a missing edge, a repeated subject, wrong layering, a wrong mapping or an implausible reveal of the ground; whether information, seams and sound hold up in the continuous clip. A pixel difference may come from a justified new composition, and zero difference does not prove the move is free of defects; judge by content and do not apply one similarity threshold.

After changing the source, normalising the size, cropping, masking, filling the base, the anchor or the font, re-check the shots, cameras and annotations that reference that part. When you only sample, record the range; a static restoration or a structural pass does not upgrade to a watchable full section, a usable whole displacement or a completed listening pass. When a loop is needed, re-check the extra return duration, the velocity across the boundary and the sound, not just the first and last images.
