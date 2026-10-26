# The object as explanation: making abstract knowledge something you can see

Read this when explaining an algorithm, a protocol, a mechanism, a process, an economy or a scientific principle, and when making a single news item clear. The goal is that the audience sees not "blocks with words on them" but a thing whose operation is itself the concept. For the layered telling see [Layered reveal](layered-reveal.md), for terminology and definitions see [Domain standards first](domain-standards.md), for fields and checks see [Knowledge-pack contract](knowledge-pack.md).

The method comes from the core idea of the open-source Skill [Anatomy](https://github.com/wheresryan22/anatomy/tree/1482e8469b0a9e0d8cc18ea2740a01423d29ae80) (MIT, slogan *The object is the explanation*). This text is an independent rewrite for video, to-camera narration and news briefs; it copies none of that project's code, examples or diagrams. The part counts and millisecond timings of its interactive isometric diagrams are starting points only — re-measure them against this film's frame rate and reading time.

## The method in one sentence

First find a real, well-made thing whose operation is the concept itself; then drive it with real numbers, so that every part tells exactly one thing and every number has a source.

Two common failures:

- Too abstract: stacked plates, floating label boxes — you cannot tell what it is.
- Too flat: one big plate plus a few lines, no parts and nothing to discover.

There is a subtler failure: beautiful but wrong. The image looks right while the mechanism contradicts the facts. So establish the facts first, then build the image.

## Workflow

```text
 ① 一句话关系 → ② 行业规范 → ③ 真值账本 → ④ 载体 → ⑤ 部件映射 → ⑥ 分层讲 → ⑦ 画面工艺 → ⑧ 核查
   topic/claim    domain.*      truth.*     carrier.*   mappings     layers      expression_ids  checks
```

1. Write the one-sentence relationship: which relationship the audience can state at the end, and which relation_type it belongs to.
2. Find the domain standards and consensus first, and fix terminology, symbols, units and pronunciation; see [Domain standards first](domain-standards.md).
3. Build the truth ledger (真值账本): every number and fact gets a source or a derivation first; on-screen readouts, captions and voiceover all take their values from it.
4. Choose the carrier: work down the carrier ladder below, starting the questioning from real mechanisms.
5. List the parts and do the one-to-one mapping; every part answers the four questions, and every metaphor gets its break points (断点) written down.
6. Order the entrances per [Layered reveal](layered-reveal.md); each layer adds only one new load.
7. Do the image craft: landed labels, one highlight, take-apart and put-back, motion settle.
8. Check: three kinds of reader, fact reconciliation, frame-by-frame inspection. Whatever was not done stays `not_run`.

## Carrier ladder

```text
 T1 真实机构   一台机器、工具、仪器或家具，其运作就是概念
 T2 空间结构   楼层、房间、地图、线路：解释包含、层级、路径
 T3 过程轨道   传送带、流水线、管道、时间轴：解释顺序与转换
 T4 数据即尺寸 量变成长度、体积、深度：解释比较与规模
 T5 图表或文字 没有诚实载体时的回退：关系图、时序表、对照表
```

Starting at T1 and moving down, ask three things; use a tier only if all three pass:

1. Can you say in one sentence what is moving, and what its movement means?
2. Does every element of the concept land on exactly one part, and does every part map back to an element?
3. Where would it lie to you? Can you write the break points down?

If any question has no answer, drop one tier. Do not build a carrier just to have one: an opinion, a mood or a purely aesthetic judgement with no mechanism to build goes straight to T5, with `carrier.kind=none` and the reason recorded in the knowledge pack. Write the fallback for a failed carrier into `carrier.fallback`.

| Tier | What the concept looks like | Example |
| --- | --- | --- |
| T1 | There is a thing that moves, and the meaning of the movement is the concept | A door lock turns only when all its pins line up, mapping to "recomputation is skipped only when every cache key matches"; a gantry plotter's single print head visits hole after hole, mapping to "one shared GPU context serves several canvases" |
| T2 | The concept is containment, hierarchy, adjacency, path | A file system drawn as floors and rooms; a network drawn as metro lines and transfer stations |
| T3 | The concept is sequence and conversion | Compilation drawn as an assembly line, one operation per station |
| T4 | The concept is size and comparison | Drawer depth equals a byte count; a scale ladder |
| T5 | No honest mechanism is available | Relationship diagram, timeline table, comparison table, highlighted section by section |

Example (T1): the TCP three-way handshake drawn as a reconciliation desk, with a sequence-number dial, an acknowledgement-number dial and a status lamp at each of the two stations, and an envelope carrying a flag tab sliding along the rail. Full structure in [Example plan](../examples/tcp-handshake.plan.json).

## Carrier archetypes by relation type

Decide which class the relationship belongs to first, then take the nearest carrier archetype. Every archetype has break points; the main one must be stated at L6 or in an on-screen corner tag.

| relation_type | Abstract relationship | Carrier archetype | Action visible in frame | Main break point |
| --- | --- | --- | --- | --- |
| process | Sequence and flow | Conveyor, multi-station track carrying envelopes or workpieces | The workpiece is processed station by station | Real processes often branch and run concurrently |
| condition | Condition and matching | Lock and key, sorting gate, mating pins | Released only when every pin lines up | Easily misread as "one unique match" |
| capacity | Capacity and queueing | Funnel, sink, parking lot, drawer | The water level or the drawer depth is the quantity | The difference between discrete and continuous |
| hierarchy | Hierarchy and containment | Nesting dolls, floors, drawer cabinet | Open one layer and see the next | Nesting dolls imply strict nesting |
| comparison | Contrast and trade-off | Balance, side-by-side gauges | Same scale and same unit on both sides | Different definitions cannot share one ruler |
| feedback | Feedback and regulation | Thermostat, governor, float valve | A deviation triggers a correction back to target | Real systems have delay and oscillation |
| transform | Transformation and mapping | Mill, press mould, filter mesh | The same input becomes a new form through the device | Information loss must be shown separately |
| concurrency | Concurrency and contention | Multiple tracks with points, a shared gate | Two tracks contend for one resource | Real timing is non-deterministic |
| probability | Probability and uncertainty | Galton board, sampling box | Many marbles pile up into a distribution | A single outcome is unpredictable |
| growth | Growth and accumulation | Stairs, spiral, piggy bank | The scale changes with the quantity | Linear and exponential scaling must be labelled |
| causal | Cause and effect | Dominoes, lever chain, drivetrain | One push starts the chain | Correlation is not causation; label candidate causes "candidate" |
| event | Event and news | Evidence board | Cards, source tags, timeline, empty slots | Layout is not verification |
| definition | Definition and classification | Specimen box, sorting cabinet, nameplate | Each condition gets one compartment | Edge cases must be shown separately |
| other | Other | First write the relationship as one sentence, then find the nearest archetype | Register it as a new archetype | Write down the break points it has of its own |

## One-to-one mapping, the four questions, break points

- One-to-one mapping: each element of the concept gets exactly one part, and the reverse holds as well. A part with no element is decoration — delete it or demote it to the base; an element with no part means the concept is not yet on screen — add the part. Knowledge-pack validation rejects duplicated concepts or parts.
- The four questions: every part answers "what is it / what is happening now / why is it here / what is it for". In the knowledge pack `what` and `why` are required, `happening` and `use` are written as needed. These four are exactly what beginners leave out; whichever one you skip is the one the comments will ask about.
- Break points: write `breaks_at` for every mapping, stating where the metaphor would lie to you. State the main one at L6, put the minor ones in an on-screen corner tag.
- Fidelity `fidelity`: `exact` is strict geometric or numerical correspondence; `structural` is corresponding relations with indicative numbers; `illustrative` exists only to aid understanding. Claiming one level lower is safer than one level higher.

## Truth ledger

The model comes before the picture. Every number and fact in an on-screen readout, a caption or the voiceover is registered in the knowledge pack's `truth.claims`, in one of three classes:

| kind | Meaning | Requires | How it is handled on screen |
| --- | --- | --- | --- |
| sourced | Comes from a source: a clause of a standard, official documentation, original reporting | `standard_ref` or `source`; for a long source, the location | May be shown directly, with attribution where needed |
| derived | Computed or derived from an already registered claim | `derivation` and `from`, and the chain must not be circular | Show the result, keep the derivation auditable |
| illustrative | Illustrative only: a sliding speed, an indicative colour | `disclosure` | Record internally the purpose, the relationships it can support and the conclusions it cannot; do not render production labels such as "illustrative only" |

- Confirmed by the user on 2026-10-21: keep production provenance and the illustrative nature internal; add no identity labels such as "demo", "illustrative" or "reconstruction" to the outward-facing film. When a relationship or a value does not hold, change the carrier, swap in real evidence or drop the claim — do not disclaim it with a label; the substantive model boundaries and operating conditions are still stated accurately.
- A claim carrying a value must have a `unit`. For counts, say what is counted — items, times, a multiple — do not leave it bare.
- The stage word and the number in a readout come from the same instant and the same source. Example: once the envelope lands, the sequence-number dial and the status lamp change together; the lamp does not light first with the number arriving later.
- Measure before you watch: check values, durations and positions with a script or a calculation first, then look at the image. A good-looking frame does not replace reconciliation.
- If a number appears in frame or in a caption that is not in the ledger, validation returns `number_not_in_ledger`; add it to the ledger first, then show it.

## Landed labels and one highlight

Anatomy puts no text in the frame; its captions sit outside the image. A video viewer cannot pause and cross-check, so this Skill compromises:

- Nameplates (small labels stuck onto a part) and legend chips are allowed; the label lands on the part.
- Leader lines, balloons, floating labels and dimension arrows stay forbidden.
- When a term first appears, light up the part it belongs to, then drop it back once the definition is done. One highlight at a time only; everything else steps down a level.
- Caption, nameplate and voiceover use the same word, one word one meaning.

Tonal hierarchy: base low, structure mid, subject high, with exactly one highlight. Use a single hue unless the colour is itself the subject (RGB channels, say). Every line has to land on something; leave no dangling ends. Keep the whole thing calm — do not prove "designed" with flicker and particles.

## Take-apart and put-back

Corresponds to `visual.structure-separate`. Structure must come from a source or a real object; do not fake an assembly that does not exist with an exploded view.

- Separate along the real disassembly direction; the outer layer leaves first, and the return runs in reverse.
- Every part still has a home once it is off: you can see which group it belongs to, and a fastener follows the end it is actually fixed to.
- The selected part lights up and the rest step down a level; the caption states in sync what that part does.
- Check the mid-state and the reverse: when a half-finished take-apart goes back, no part may pass through another.
- In video, take off one layer at a time and mark each group's entrance with a beat; do not let every part fly out at once.

## Motion settle

Corresponds to `animation.spring-settle`. The following are practices from the Anatomy motion guide, as a starting point:

- Event envelope: attack around 40–120 ms; setting a value to 1 within a single frame is a pop, not a motion.
- Quantities that should not overshoot (tone, brightness, lamps, readouts) settle with critical damping; only a mechanical part with weight may overshoot slightly, once.
- A fade-out only darkens: freeze the current brightness when the stop begins and multiply only by something that decreases.
- When one quantity drives colour, shape and brightness at once, give colour its own slower settle so the three do not jump on the same frame.
- Home first, then move: when an action needs a particular state, bring the machine back to that state first and start the clock only once it is there; never run an action from a half-taken-apart state.

## News briefs: the evidence board

A news brief is not a mechanism, but it has structure: who, did what, on what basis, and what is still unconfirmed. The carrier is the evidence board.

| Part | Corresponds to | Rule |
| --- | --- | --- |
| Event card | Who, did what, when, where | One card, one fact |
| Source tag | Original source, date, type | A fact card must carry a source tag |
| Timeline | Order of events | One scale unit throughout |
| Data gauge | Numbers and definitions | Same definition, same scale; different definitions never share one ruler |
| Empty slot | Unverified, disputed, unknown | Dashed empty box stating why it is empty |
| Version stamp | Cut-off date `as_of` | Every verified fact carries a date |

A news pack has additional requirements: every sourced claim carries an `as_of`; `truth.unknown` lists what is unconfirmed, disputed or unknown, or `unknown_none_reason` if there is nothing. Keep fact, comment and speculation apart; label candidate causes "candidate" and do not draw them as causation. For the evidence-board recipe see `evidence-board-brief`, for the layered telling see [Layered reveal](layered-reveal.md).

## Frame check

Watch like a critic, not only for whether it looks good:

1. Cover the mapping table and look only at the frame: can you say what each part is doing?
2. Cut the sound and watch only the image and the captions: can you follow it?
3. Zoom in: is there any vacant area with no part in it?
4. Does every line land on something at both ends?
5. Can every number in the frame, in the captions and in the voiceover be found in the ledger?
6. Go frame by frame through the first frame, the densest frame, the frame where the relationship lands and the reverse frame.
7. Have someone who knows the domain read it: this is where beautiful-but-wrong shows up fastest.

Write the results of these questions into the knowledge pack's `checks`; whatever was not actually done stays `not_run`, and an impression that it "looks right" is not a pass.

## Relation to the catalog

- Expressions: `knowledge.object-is-explanation`, `knowledge.part-cast`, `knowledge.landed-label`, `knowledge.truth-ledger`, `knowledge.evidence-board`, together with `visual.structure-separate`, `animation.spring-settle`, `visual.target-callout`, `narrative.follow-unit`.
- Recipes: `object-explainer` (mechanisms), `evidence-board-brief` (news), `layered-concept-reveal` (the overall layered structure).
- Every entry is design guidance, not an installed effect, and does not prove the audience understood. Sources and the boundaries of adoption in [Sources and boundaries](sources.md).
