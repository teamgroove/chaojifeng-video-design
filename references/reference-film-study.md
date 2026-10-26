# Reference film study: take a finished film apart into a transferable method

Read this when the user hands over a finished film and wants to "study its technique and abstract it into a reusable method". The goal is to leave behind **rules that still hold when the product changes**, not a reproduction of this film. Launch-film elements already extracted are in [launch film grammar](launch-film-grammar.md); that is one result produced with this method, not the end of the study.

## The study process

| Step | What to do | Tool | Output | Evidence |
| --- | --- | --- | --- | --- |
| 1 Register | Path, hash, specs; write down what is *not* there (no voiceover, no subtitles) | `film_probe.py` | Specs and list of gaps | E2 |
| 2 Find the source | Check in-film titles, watermarks, filenames and user clues for public source code; with a public GitHub project, go through DeepWiki for the architecture first, and only if that fails take the source at a pinned commit and record the commit hash | DeepWiki, pinned-commit source | Source timeline, easing, copy | E1 |
| 3 Cut the structure | Detect cut points and split into scenes; cross-check against the source timings and investigate any mismatch | `film_probe.py` | Cut-point table, scene share | E2 |
| 4 Look at frames | For each segment look at the first frame, the densest frame, the settled frame and transition boundaries; read the contact sheet first, then single frames at the key moments | `film_probe.py --sheet-step` | Observation notes | E2 |
| 5 Measure sound | Loudness, energy troughs, onsets; line them up against picture events. **If you did not listen, write that you did not listen** | `film_probe.py`, `audio_event_audit.py` | Audio event map | E3 |
| 6 Keep a ledger | Every observation carries a time, an evidence level and the raw numbers | — | Observation ledger | E1–E3 |
| 7 Abstract | Climb the abstraction ladder (next section) | — | Element draft | E4 |
| 8 Record flaws | Write down the reference film's own problems too, as counter-examples | As above | Counter-examples | E1–E3 |
| 9 Write it down | Turn it into catalog entries and a recipe, write the sources and boundaries | `catalog.py` | Expressions, recipes | — |

The probe tools only measure: cut points come from frame differences, audio events from the energy envelope, the palette from 3×3 block averages; parameters are in each script's `--help`. Cross-dissolve detection starts later than the real start and slow gradients can be missed; the lower the threshold, the more readily an in-interface animation is taken for a cut. When source code exists, the source wins.

## The abstraction ladder

Every conclusion has to climb all the way up before it is promoted to an element; if it cannot, it stays an observation.

| Layer | Question | Example |
| --- | --- | --- |
| Observation | What happens in the picture or the sound, and what is the evidence | At 9.3–12.3 s a wall of long AI summary text appears first, then *Still too long* |
| Intent | What the creator wants the viewer to come away with (mark it as inference) | Let viewers see for themselves that the usual approach does not work either |
| Principle | A rule that still holds once this film's concrete content is removed | The failing alternative demonstrates itself with its own output, without a voiceover putting it down |
| Starting parameters | This film's numbers, marked as reference, not as defaults | 1–3 s per layer, a 1–3 word verdict line |
| Boundary | When not to use it, and how it fails | The alternative is a straw man; the pain point is already well known |
| Transfer test | Swap in a completely different product — can you write the corresponding image | Photo-resize tool: post the square image directly → *Too square*; use photo-editing software → *Too many steps* |

Rules:

- A principle must be statable independently of this film's content; if you cannot, it is only an observation.
- Write parameters as "reference starting points", never as executable fields in the catalog.
- Separate creative choice from tool limitation: the same practice may just be a product of the tools of the time.
- Do not count same-source material as two independent samples. Example: the `full-film.mp4` the user supplied is the finished film of the HyperFrames "PR → Video" project (in-film titles and cut points agree with the source-code timing).
- One film can only support "this practice exists and can be pulled off"; it cannot prove "it works".

## When there is a creative conversation, trace how decisions became the artifact

First lock the user-specified session and time range, run a structural scan, then read back the substantive instructions, corrections, key versions and corresponding artifacts; exclude system injections, automatic receipts and irrelevant material, and do not take model reasoning or self-description as user confirmation. Read only the material you need — one session ID does not justify scanning the whole history. Without the film you can study the process, but you cannot claim to have seen or heard the work.

| Relationship to trace | What to record and check |
| --- | --- |
| Instruction → choice | When audience, purpose, length, sound or channel constraints changed; keep the original words separate from the agent's explanation |
| Version → finished film | Which plan, code and assets correspond to the final hash; an early contact sheet cannot stand in for a newer version |
| Claim → evidence | Current product behaviour, where the events come from and the real results; what generated footage, reconstruction and metaphor each carry |
| Asset → derivative | Which original image or audio was cropped, layered, generated or redrawn; the basis for accepting it, the loss record and what was not verified |
| Failure → revision | The original method, the verifiable symptom, the change and what remains; parts not re-run or not auditioned keep their gap |
| Metric → conclusion | Sampling frame rate, thresholds, totals and the audited subset; instrument results do not replace taste, listening or reach |

Carry the failure conditions forward with the original version, then do the "principle → boundary → different product" transfer. A user cutting an explanation or a call to action in a single film only proves a limit for that film; fixed colour, gendered aesthetics, BPM, duration and amount of motion do not become defaults. A single case can produce guidance candidates, but cannot be promoted to a method that holds across scenarios. Product singing and the first three seconds can be checked for transferable relationships against [product music narrative](product-music-story.md) and [opening design](opening-design.md).

A research report may keep entry points to private raw material; the general Skill takes in only the method, anonymised failure conditions and source boundaries, and packages no conversations, personal voice or project assets.

## Counter-examples and flaws

A reference film is not a perfect answer. That film's opening sound effect was never re-timed to the picture (see [launch film grammar · sound](launch-film-grammar.md#3-sound-write-the-event-map-first-then-lay-out-the-timeline)) — that is what steps 5 and 8 of this document turned up. When you record a counter-example, state: the evidence, the inference, whether it was listened to, and the corresponding preventive measure.

## Attribution and distribution

- Do not package the original film, picture, music, fonts, branding or interface; examples and tests use synthetic material only.
- Cite pinned-commit links, do not copy source code; licenses for commercial fonts and assets are checked separately.
- Source links and boundaries go into [sources.md](sources.md); where you did not read something, write that you did not read it.
- When the user's film is private material, study it locally only, and let no whole-segment content that could reconstruct the film appear in the notes.

## Deliverables checklist

- Observation ledger (time, evidence level, numbers), contact sheets and key frames
- Element draft: observation → intent → principle → starting point → boundary → transfer test
- Counter-examples and an unverified list (not listened to, no audience test done, certain passages not watched)
- The catalog entries and recipes as landed, and how they relate to existing entries (do not duplicate IDs)
