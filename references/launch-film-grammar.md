# Launch-film grammar: pull one reference film apart into transferable orchestration elements

For 30–45 second product launch films and feature introduction films; it can also shrink to an 8–15 second single-feature film. The source is a frame-by-frame, source-code and audio study of a public launch film, [HyperFrames "PR → Video"](https://github.com/heygen-com/hyperframes-launches/tree/d7ac35069d74a3a437780579b3b7fe2f3eeace5f/pr-to-video-launch); the method is in [Reference-film study](reference-film-study.md). This text only writes "why it is arranged this way, how to transfer it, how it fails": it does not reproduce that film, does not take its numbers, brand, fonts or score as defaults, and does not claim these practices are more effective on viewers.

When choosing a recipe: first use `product-task-proof` from [Product expression](product-expression.md) to fix the task and the evidence; for a launch film with a full emotional arc (pain → turn → self-proof → action) use `launch-film-arc`; to prove several features chapter by chapter use `feature-chapter-reel`; for a single feature see section 5.

## Evidence levels

| Level | Source | How to write it |
| --- | --- | --- |
| E1 | Source code at a fixed commit: timing, easing, copy, parameters | May write "this film does it this way" |
| E2 | Extracted frames from the finished film, cut detection, palette sampling | May write "the finished film presents as" |
| E3 | Instrument measurement of the audio track: loudness, energy valleys, transients | Only write "measured"; **no listening pass**, so do not write how it sounds |
| E4 | Inference: why it works, how to transfer it | Must be marked "inference"; there are no audience experiments |

Every number below is a reference starting point from that film, not a default; each film re-determines them for its own content, reading window and aspect ratio.

## 1. Arc: pain → turn → self-proof → action → sign-off

| Section | Position in the reference film | Share* | What the viewer gets | Main elements |
| --- | --- | --- | --- | --- |
| Hook: a real input | 0–5.2s | 16% | A real situation: someone sends in something that has to be dealt with | typed-voice, pull-back-reveal, action-seam |
| Pain: measurable | 5.2–8.4s | 10% | "Why it is hard" shown with numbers and real objects | magnitude-whip, replica-ui |
| Verdict | 8.4–9.3s | 3% | One line that names the state | verdict-card |
| The failed alternative | 9.3–12.3s | 9% | Even the most natural approach fails; demonstrate it with its real output | pain-to-verdict, verdict-card |
| Turn | 12.3s | — | The world flips: the sound drops first, the ground colour flips after it, and immediately the user invokes the product for the first time | two-ground-world, pivot-drop |
| Invocation | 12.3–16.1s | 12% | Start the product with one sentence | typed-voice, replica-ui |
| Self-proof: parallel chapters | 16.1–25.6s | 30% | Several promises, each with a piece of finished output as evidence | parallel-promise, output-as-proof, compressed-inner-clock |
| Action | 25.6–30.0s | 14% | The viewer's own first step | cta-as-action |
| Sign-off | 30.0–32.1s | 7% | Brand signature (a separate animation, appended at finished-film time) | — |

\*Counted on 32.1 seconds. The first 12.3 seconds (38%) all make the viewer feel the difficulty first-hand; that is this film's choice for a developer audience; when the pain is already familiar you can keep only one layer of verdict, or omit it entirely (see the `problem-reframe-opening` branch of `product-task-proof`).

### Deriving duration for your own film

1. First write one sentence per section for "what the viewer gets"; delete sections where you cannot write new information.
2. For every image write the shortest readable window: readable characters ÷ reading speed + settle. That film's shortest card is 0.9 seconds, holding 3 words. If there are many characters, split the card or cut words; do not speed up.
3. Pain-section length is proportional to how unfamiliar the pain is to the audience (inference): familiar → shorten; unfamiliar → use real numbers, not adjectives.
4. The proof section derives as "number of chapters × (one chapter's shortest readable window + switch)"; chapters are bounded at 3–4, what the viewer can hold at once (inference).
5. Total length is settled last: lay out the arc first, then add up; do not fix 30 seconds first and stuff content in.

## 2. The fourteen elements

Each item is written as "observation → principle → transfer → starting point → failure signal"; IDs can be looked up with `catalog.py --kind expression get <ID>`.

### 1. Pain is the evidence, the verdict ladder `narrative.pain-to-verdict`

- Observation (E1/E2): first let the viewer "see the difficulty" for themselves through real artifacts — 629 files, −87,291 lines, 4 commits, numbers typed out digit by digit; then one verdict line *Hard to read*. Next the conventional alternative (let AI summarise) takes the stage; its real output is a wall of long text, then one line *Still too long*. Only after two verdict cards does the product appear.
- Principle (inference): the verdict line only names the state, the evidence comes first; the failed alternative must be something real people would try first, and its own output demonstrates the failure — do not use voiceover to belittle it.
- Transfer: find the "most natural first reaction" the product replaces, and put its real result on screen. Add only one kind of new friction per layer; do not amplify the same difficulty twice.
- Starting point: 0–2 layers; 1–3 seconds of evidence per layer; verdict line 1–3 words.
- Failure signal: the verdict comes before the evidence; the alternative is a straw man; the two layers of difficulty are actually the same thing.

### 2. Typing is the narrator `text.typed-voice`

- Observation (E1): the whole film has no voiceover and no subtitles; intent is carried by "the typed word". A long sentence of 85 characters types out in 1.5 seconds (about 57 characters/second), a command of 17–43 characters in 0.8–1.4 seconds (21–31 characters/second), chapter titles after inner-clock compression 24–53 characters/second. Long links are not typed; use paste: the whole string appears at once, marked in blue, with a pop sound. Sending is a visible action: the cursor clicks the return key (shrinks to 0.84 then springs back, one ripple), and the input field clears immediately afterwards.
- Principle (inference): the way something appears carries meaning — typing = someone is expressing something, pasting = quoting an external object, clearing = submitted. The viewer reads "who is doing what".
- Transfer: write the product input as one sentence a user would really say; long sentences type fast, short commands type slow; URLs, paths and accounts are pasted; after typing, leave a reading window before sending; after sending the input field must change.
- Starting point: see the observation; this is a rhythm parameter, not a readability guarantee.
- Failure signal: a whole paragraph of typing drags the rhythm; a click stacked on every character; no change at all after sending.

### 3. The verdict card, three type voices `text.verdict-card`

- Observation (E1/E2): a verdict card is one or two words on a flat single-colour full frame, serif large type at about 9.5% of the frame width, floating up and fading in over 0.28 seconds, staying 0.9 seconds and then leaving. Across the film three type voices each own one job: serif = human judgement; sans and mono = system and interface; heavy black caps = chapter promise.
- Principle (inference): one card says one human sentence; the type voice tells the viewer "who is speaking".
- Transfer: keep the verdict line short enough to read in half a second; make the ground colour contrast with the previous section; add no icons, no subtitle and no second action.
- Starting point: with words ≤3 the minimum dwell is 0.9 seconds; entrance 0.25–0.3 seconds.
- Failure signal: the card carries an explanation; dwell shorter than the reading; no change of ground colour or sound before and after, so it reads like an ordinary subtitle.

### 4. Magnitude whip and digit-by-digit counting `visual.magnitude-whip`

- Observation (E1/E2): prove "many" with "a real long list scrolling up fast": the inner layer runs y to −3600px over 1.7 seconds `power2.in` (accelerating out of frame), with 0→2px blur at the same time; statistics type out digit by digit (`steps(n)`, 0.2–0.7 seconds each, with a cursor), numbers in the accent colour, the label in small grey type.
- Principle (inference): magnitude is felt first through "speed × quantity", then confirmed through the number; accelerating out of frame carries "there is much more" off-frame.
- Transfer: use the product's real data volume, and the numbers must share the same source as the visible footage; the last item landing on the smallest number (4 commits) can also form the contrast.
- Failure signal: numbers do not match the footage; constant-speed scrolling with no sense of acceleration; so much blur that you cannot tell what it is.

### 5. Two-ground world `style.two-ground-world`

- Observation (E2): dark full frame `#1D1F1F` = inside the tool, being judged; cream stage `#F0EFE9` = standing outside, giving the answer; the dark tool shrinks into a floating window on the stage. After the 12.3-second turn the stage never returns to a dark full frame. There is only one accent colour (`#D97757`: key nouns, links, numbers); green and red serve interface semantics only.
- Principle (inference): the ground colour is a narrative state, not decoration; the contrast itself is "problem → answer".
- Transfer: pick two "grounds" by product character (dark or light, sharp or soft, crowded or empty all work), bind the problem to one and the answer to the other, and let the turn happen only once. The product's own brand colours take priority.
- Failure signal: switching between the two grounds more than twice; more than one accent colour; success/error colours used as decoration.

### 6. Turn lands on the beat `sound.pivot-drop`

- Observation (E3, **no listening pass**; supplemented by E1): full-band energy from 9.8 seconds on is about 12 dB above the previous section and lasts about 1.4 seconds (mostly low frequency); after falling back it drops to about −23…−28 dB at 11.7–11.95 seconds (`film_probe` records a valley at 11.87 seconds lasting 0.33 seconds, 14 dB deep); at 12.0–12.1 seconds it returns to about −11 dB and moves into the beat, with the onset measured at 12.045 seconds, about 0.25 seconds before the picture flip at 12.3 seconds. Each seam also has a shallow valley of 0.1–0.3 seconds (2.52, 5.60, 8.40 seconds). The source code for this section holds only three short sound effects — type, click, swish — and no long riser, so it is inferred (E4) that the build, the break and the drop come from the arrangement of the music bed, not from added SFX.
- Principle (inference): hear the turn before you see it; the short silence before the turn gives the drop its weight; the turn is carried by the music section, and SFX only confirm the action.
- Transfer: when choosing or cutting music look for a "build → break → drop" structure and align the break and the drop to the turn; make the film's one big turn only once, make the other seams shallow valleys only, do not whoosh everywhere. If no fitting section exists, write a short one and actually audition it.
- Starting point: build 1–3 seconds; break 0.3–0.4 seconds; drop 0.2–0.4 seconds ahead of the picture; seam valley 0.1–0.3 seconds.
- Failure signal: the same big sound effect on every transition; the drop after the picture; a break so long it becomes a dropout; stacking SFX to manufacture a "turn".

### 7. Pull-back reveal and click-through `camera.pull-back-reveal`

- Observation (E1/E2): the opening input field fills the frame (scaled 1.85×), so the viewer first sees only "one sentence". After sending it pulls back over 0.55 seconds `power2.inOut` into a floating window on the stage, then the cursor walks to the link and clicks, and the picture zooms 1.6× from the clicked point as origin, 8px blur, 0.4 seconds `power2.in`, travelling through into the next scene.
- Principle (inference): give the nearest thing first, then pull back to explain "where you are", then travel through a clicked target into the next scene.
- Transfer: open with the smallest readable unit filling the frame; trigger the pull-back from "send/confirm" rather than pulling because the time has come.
- Failure signal: pull-back with no triggering action; content inside the window unreadable after the pull-back; the through-origin not on the clicked target.

### 8. Replica interface with a recognisable shell `visual.replica-ui`

- Observation (E1/E2): the interface is replicated in HTML — red-yellow-green window buttons, address bar, tabs, chips, a pixel mascot. There are small "live" details (mascot walking, cursor blinking, thinking animation). Information overload is expressed with a faded wall of text, without asking the viewer to actually read it.
- Principle (inference): if the shell is recognisable the content needs no explanation; replicate the structure the viewer knows, not pixel for pixel.
- Transfer: verify the current entry point, behaviour and result first, and take the copy from the current product; a string or an old screenshot alone cannot prove a feature. Record the manual rebuild and its basis in the project; on the viewer side choose the disclosure by misrecognition risk, user and actual channel requirements, see [Asset selection](asset-routing.md#how-re-creation-and-explanation-enter-the-picture). Do not stage states the product does not have; verify small type is legible at finished size.
- Failure signal: a feature appears that the product does not have; type too small; too close to a third party's real brand interface, causing misunderstanding.

### 9. Action-causality seam `transition.action-seam`

- Observation (E1/E2): every big scene change is caused by a visible action — click a link → zoom through, click send → pull back, return-key pulse → into the sign-off. The other seams use 0.28–0.35 second cross dissolves (`power1.inOut`), or "land to the ground colour and rise again".
- Principle (inference): the viewer should be able to answer "why did it change now" — because someone clicked. The transition toolkit is small: action through, land to ground, quick dissolve.
- Transfer: write "triggering action + in/out objects" for every seam; with no visible trigger use a quick dissolve, do not show off.
- Failure signal: a different transition style at every seam; action and transition out of sync; a cursor appears but clicks nothing.

### 10. The finished output is the evidence, label excerpts `narrative.output-as-proof`

- Observation (E1/E2): the self-proof section shows the product's own output, inside a player with progress bar, timecode and *scene n / 6*; the four chapters are the 1st, 2nd, 5th and 6th of 6 scenes, and the interface says outright that these are excerpts. The demo input is the product's own real artifacts (PR #1635, 629 files) — "eating its own dog food".
- Principle (inference): evidence comes from the product's real output, excerpts must be labelled honestly, and inputs should be real rather than invented examples.
- Transfer: find the one piece of output that proves the product best; an excerpt that would be mistaken for the whole must state its scope. Manual mock-ups or generated images carry explanation only and cannot prove real output; when the real result is missing, shrink the claim or change the shot, and decide the disclosure position per [Asset selection](asset-routing.md#how-re-creation-and-explanation-enter-the-picture).
- Failure signal: images in the player that were not produced by the product yet carry proof of a real result; the excerpt makes the viewer think it is the whole. Replace with the real result or adjust the claim; keep source records internal, do not patch it up with a production watermark.

### 11. Parallel promise chapters `narrative.parallel-promise`

- Observation (E1/E2): the four chapter titles share one sentence pattern *SHOW YOUR CODE / FEATURE / REVIEW / CONTRIBUTOR*, heavy black caps, typed with an orange cursor; stage, player and layout stay unchanged, only the noun and the output change.
- Principle (inference): parallelism plus a stable stage — the viewer does not have to learn a new layout, only read the one noun that changed; the noun should be something the viewer owns.
- Transfer: write one promise pattern first (verb + your ___), then fill in the nouns, 3–4 chapters.
- Failure signal: the pattern drifts; the layout change between chapters steals attention; the noun is a product-internal term.

### 12. Inner-clock compression `production.compressed-inner-clock`

- Observation (E1): the player's internal timeline is built at natural pace, then compressed with `timeScale` 2.0–2.56 into 2.0–2.6 seconds (4.1–6.6 seconds of authored time). The player timecode (0:02→0:32) is presentation, not event time of the outer film.
- Principle: design the content at natural pace until it is comprehensible, then compress uniformly; verify the reading window separately after compression.
- Transfer: record `authored_seconds`, `playback_rate`, `film_seconds`; timecodes do not go into facts; after compression the sound events must be re-laid-out to match (see section 3).
- Failure signal: text unreadable after compression; the inner-clock timecode taken as a fact about the outer film; SFX not updated with it.

### 13. Action as call to action `narrative.cta-as-action`

- Observation (E1/E2): the CTA is not a slogan but a real invocation — the large type *Create your PR video today* is typed out (product noun in the accent colour), the title moves up to make room, the input field appears, a real command is typed and an example link pasted, the return key pulses orange; then the brand sign-off takes over (a separate animation, appended at finished-film time).
- Principle (inference): the action entry matches how the product is used; the viewer sees "this is what I do next".
- Transfer: per the actual channel and user constraints, show the real executable first step (e.g. picking an image inside the product), or close only with purpose and brand; do not default to search, QR code or download as the funnel. Write placeholders explicitly as placeholders.
- Failure signal: a placeholder taken as a real address; the command shown does not run; the sign-off steals focus from the action.

### 14. Dwell budget `production.dwell-budget`

- Observation (E2): shortest card 0.9 seconds, longest 5.2 seconds; problem:invocation:proof:action:sign-off ≈ 38:12:30:14:7.
- Principle: compute the shortest window the viewer needs to read, watch and listen, then add up — do not fix the total length first.
- Transfer: write `read_budget` for every shot; the total length is the sum; if you overshoot the target, delete shots, do not speed up.
- Failure signal: every shot the same length; padding the duration by speeding up.

## 3. Sound: write the event map first, then lay out the timeline

The reference film's sound divides by function: typing, clicks, pop, swish, several whooshes, risers, chord hits; the music bed sits at `data-volume=0.5`. The finished film is about −13.5 LUFS, LRA 5.7 (E3).

**Counter-example (E1+E2+E3)**: the SFX starting points in that film's opening were not re-laid-out when the picture changed; the declared moment, the picture action and the measured onset compare as follows (measurements from `audio_event_audit.py`, anchoring on the declared moment and checking row by row).

| Event | Picture action | Declared SFX moment | Measured onset | Measured deviation |
| --- | --- | --- | --- | --- |
| Paste link | 2.10s | 2.7s | 2.65s | +0.56s |
| Click send | 2.30s | 3.5s | 3.52s | +1.22s |
| Pull back | 2.55s | 3.7s | 3.70s | +1.15s |
| Click link | 4.20s | 6.0s (the scene is only 5.2s) | 6.02s | +1.82s |

Control group later in the same film: click send 10.15 seconds, measured 10.17 seconds — it lines up. The problem is concentrated in the opening; the two mascot clips embedded in the opening are laid out for 5.27+1.73=7.0 seconds while the scene is only 5.2 seconds, so it is inferred (E4) that the opening was shortened and the SFX were not changed after the picture was re-laid-out. Whether viewers noticed is unknown; there was no listening pass.

Method:

1. Write the event map first ([template](../templates/audio-event-map.json)): event ID, picture action moment, SFX, onset offset, gain. SFX moment = action moment + onset offset; generate the picture events and the sound events from the same data, do not write each separately.
2. After any re-lay-out of time (changing scene length, `timeScale`, deleting shots), regenerate the event map.
3. After the finished film, run `audio_event_audit.py`, compare the schedule against the measured onsets, and fix each row that exceeds tolerance. Events with `sound_start_s` written are anchored on the scheduled moment to find the onset; those without it can only be matched to "the nearest onset" near the action, which may pair the wrong one when SFX are dense. For soft whoosh and swish lower `--hit-db` to about 4; with a music bed, use a mix containing only SFX where possible. It only measures; it does not judge whether it sounds good.

## 4. Do not use this unless these conditions hold

- The pain is not measurable: verdict cards become empty shouting; take the feature-proof route instead.
- There is no real output to show: exit `output-as-proof`, shrink the claim or change to an explicitly explanatory shot; a mock-up cannot replace result evidence.
- The audience already knows the old method's shortcomings: omit the pain section.
- The product has no "input" action (e.g. pure browsing): change typing to selecting, dragging or scanning, keeping the "action → change → output" causality.

## 5. Single-feature film (8–15 seconds) adaptation

The reference film has no single-feature sample; below is this Skill's adaptation (inference, unverified).

| Beat | What to do | Elements |
| --- | --- | --- |
| Promise 1–2s | one "verb + your ___" line, typed out | typed-voice, parallel-promise |
| Trigger 2–4s | one visible action with clear causality | action-seam |
| Change and output 4–8s | the change process plus the settled output, dwell no shorter than the reading window | output-as-proof, replica-ui |
| Sign-off 2–3s | the real entry point or the brand | cta-as-action |

## 6. Finished-film self-check (answer each line; if you cannot, rework)

1. Watch it muted: can you say clearly who is doing what and what the result is?
2. Can you name the triggering action for every scene change?
3. Does the pain have checkable numbers or artifacts?
4. Is the verdict card's dwell long enough to finish reading?
5. At the turn, did both the sound and the ground colour change? Only once?
6. Is the deviation between the audio event map and the finished-film measurement within tolerance? (`audio_event_audit.py`)
7. Does the project record distinguish real screen capture, rebuild and mock-up? Is the business scope accurate, and does it match this film's actual channel and user constraints? Do in-film text, prompts, subtitles, voiceover and public attachments carry no production-identity label or creative self-description? Does the picture itself still imply a false capability?
8. Shrink it to a phone screen: is the main evidence still identifiable?
9. Have you listened? If not, write "not auditioned".

## Boundaries

- Do not distribute the reference film's images, brand, commercial fonts, music and UI; examples and tests use synthetic assets only.
- "Eating its own dog food" holds only when the demo input really is the product's own real artifacts.
- That film's numbers come from a developer audience, 1920×1080, a 30-second-class finished film; changing audience, aspect ratio or duration requires re-determining them.
- There are no audience experiments; the elements' "principles" are inference, not conclusions about effect.
