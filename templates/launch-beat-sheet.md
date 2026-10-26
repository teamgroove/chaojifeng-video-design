# Launch-film beat sheet (a design note, not a required process)

Use it for a 30-second launch film, a promo, or several features chained together; for a single-feature 8–15 second film fill only sections 0, 3 and 5. The method is in [launch film grammar](../references/launch-film-grammar.md); derive every number from your own content, never copy it from a reference film. In a cell with no grounds write "none" — do not make it up.

## 0. In one sentence

- Who the audience is, and how they do this thing today:
- What they can do or want to do after watching:
- Through-line (one sentence, one that every section of the film can point back to):
- Risk: what this film is most likely to be misread as:

## 1. Evidence inventory

| Item | Real grounds (interface, copy, numbers, finished output) | Source and date | Usable in the finished film |
| --- | --- | --- | --- |
| The difficulty of the old way | | | |
| The most natural alternative and what it produces | | | |
| The product's real input | | | |
| The product's real finished output | | | |
| The audience's first step | | | |

Without "the difficulty of the old way" do not force a pain-point section; without a "real finished output" there is no proof section — add the grounds first, or turn it into a labelled illustration.

## 2. Choosing the arc (every section can be cut)

| Section | Keep / cut | Why | Target seconds | Grounds for the minimum window (word count, evidence complexity) |
| --- | --- | --- | --- | --- |
| Hook (one real input) | | | | |
| Pain point (magnitude and numbers) | | | | |
| Verdict ladder (0 to 2 levels) | | | | |
| Turn (once) | | | | |
| Invocation (one sentence that starts the product) | | | | |
| Proof (sections, no more than 3 to 4) | | | | |
| Action (the audience's first step) | | | | |
| Sign-off | | | | |

Total length = the minimum windows added up + seams and settles; when it exceeds the target, cut shots or cut words first, never speed up.

## 3. Shot-by-shot table

| beat_id | Start–end (absolute seconds of the whole film) | What the audience gains | Picture action and visible trigger | Real / rebuilt / illustrated | Sound's job | Reading window |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

For every scene change write the action that triggers it; if you cannot, change it to a fast dissolve.

## 4. Typing script

| Sentence | Intent (state / quote / command) | Word count | Character rate | Reading window after the last character |
| --- | --- | --- | --- | --- |
| | | | | |

For long quoted material switch to paste-and-highlight; speed is a rhythm parameter, not a guarantee of legibility.

## 5. Sound

- Audio event map: `audio-event-map.json` (structure in the [template](audio-event-map.json)); picture action and the sound schedule are generated from the same data.
- The turn: how long the setup runs, how long the beat drops out, how far the landing beat leads the picture (once in the whole film):
- Seams: the depth and length of the shallow trough, and which seams get no sound:
- Music source and licence:
- Post-render audit: run `audio_event_audit.py` on the SFX stem without music, and record the tolerance and the result.
- Listening pass: heard / not heard (write not heard if you have not listened back):

## 6. Interface rebuild checklist

| Interface | Which real screenshot or source it comes from | Recognisable features kept | Where the rebuild label sits | Minimum type size (at delivery size) |
| --- | --- | --- | --- | --- |
| | | | | |

## 7. Self-check before you shoot

Answer the [finished-film self-check](../references/launch-film-grammar.md#6-finished-film-self-check-answer-each-line-if-you-cannot-rework) item by item; rework anything you cannot answer. Three that matter most:

1. Watch it muted: can you name the triggering action at every scene change?
2. Cut the second verdict level or any one section — is it clearer?
3. Shrink it to a phone screen: are the main evidence and the smallest text still legible?

## 8. Register (honestly)

| Item | Status | Evidence path or note |
| --- | --- | --- |
| Design | authored / reviewed | |
| Preview (frame check per section) | not_run / partial / passed | |
| Export and measurement (cuts, loudness, event audit) | not_run / partial / passed | |
| Listening pass | not_run / partial / passed | |
| Audience comprehension | not_run | Keep it at not_run unless you ran an audience test |
