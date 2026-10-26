# Layered reveal: each layer adds exactly one new load

Read this when you have to turn abstract knowledge into an order the audience can keep up with. A good-looking carrier (see [the object as the explanation](knowledge-visualization.md)) only solves “can be seen”; the layers solve “can be followed”: at any moment the audience carries one more new thing only, and knows where it attaches.

## The seven-layer map

```text
 L0 钩子 ─► L1 黑箱 ─► L2 部件登场 ─► L3 关系 ─► L4 完整一圈 ─► L5 反例与边界 ─► L6 回顾与指路
 为什么要    输入是什么   谁是谁         谁影响谁   用真实数字     拿掉或改变一个     一句话、一屏总览、
 关心        输出是什么   (四问)         怎样影响   跑一遍         东西会怎样         延伸方向、模型边界
```

| Layer | What the audience must answer right now | Frame | Exit check (exit_test) | Common mistake |
| --- | --- | --- | --- | --- |
| L0 Hook | How does this concern me | one concrete question or contradiction; the carrier may stay off screen | can restate the question | opening with a definition |
| L1 Black box | what goes in, what comes out | the carrier appears whole, its parts closed | can state the input, the output and the result | taking all the parts apart up front |
| L2 Parts enter | what each thing is | light one part at a time, each answers the four questions | can say what each part stores and what it does | introducing every part in one breath |
| L3 Relationship | how they affect each other | put two parts side by side and show one relationship with a connector or an action | given an input, can state the matching output | unfolding several relationships at once |
| L4 One full cycle | what it looks like actually running | walk the whole loop once with real numbers, skipping no step | can state what each step does, in order | showing only the smoothest stretch |
| L5 Counter-example and boundary | why it is designed this way | remove or change one part and see what the result is | can say what problem appears without it | arguing the point without letting the audience see the consequence |
| L6 Review and pointers | what to take away, where to continue | return to the overview, state what was not demonstrated, give further reading | can state the boundary and the next step | closing on “thanks for watching” without stating the boundary |

There can be more than one L2 — for example the part's “dial and lamp” first, then “envelope and paddle” — each still adding only one new load. Inside one chapter the layer may only go up; a new chapter that needs new parts starts again with the `chapter` field, walks up from L2 inside that chapter, and still ends on L6.

## Rules

1. One layer, one new load. Write `new_load` as one thing; if it reads as “A, B, C” or as a semicolon-separated list, split it into several layers.
2. Bridge between layers: except the first, every layer writes `bridge_from_previous` and states exactly “which thing in the previous layer becomes which thing in this one”. Keep object identity (the same `continuity_key`) and use the shot or a highlight to point at the part that changed. Jumping levels abruptly — CPU to GPU, say — loses the audience, so you must bridge with a zoom, an expansion or a side-by-side keep.
3. Define a term before using it: at a term's first appearance, give the definition in the same sentence, or in the next sentence, which opens with the term. Define it, light it, then use it once more.
4. The four questions when a part enters: what is it / what is happening now / why is it here / what is it for. Every part answers at least the first two, “what” and “why”.
5. L4 uses real numbers, walks the whole cycle, skips no step. Anything that does not carry a fact — how fast something slides, a colour — is marked “illustrative only” in the frame. Numbers come only from the ground-truth ledger.
6. L5 has at least one counterfactual probe: remove one part, change one condition or add a counter-example, and make the consequence visible. It answers “why can't this be simpler”.
7. L6 must have three things: a review (one sentence plus one overview screen), pointers onward (specific reading or chapters), and the model boundary (what this machine did not demonstrate, where the metaphor starts to lie). The knowledge pack validation requires `model_boundary` and `extension_pointers` on L6.
8. Every scene serves exactly one layer, and every layer covers one or more scenes. A scene with no layer gets a reminder.
9. Each layer from L2 to L5 lights one focal element (`focus_element_id`); everything else steps down.

## Length and chunking

| Duration | Approach |
| --- | --- |
| 30–45 seconds | keep only L0, L1, L4, L6; cut terms to the minimum |
| 60–90 seconds | merge L2 and L3, keep a single probe in L5 |
| 3–5 minutes | use all seven layers, split into several L2s when there are many parts |
| 8 minutes and up | chapter it; each chapter is a small L2-to-L4 loop, end the chapter on a checkpoint, and let the overview map advance with the chapters |

These bands are a design starting point, not validated by audience testing; go by the actual reading and listening.

Checkpoint in a long film: at the chapter's end use a question-and-answer still frame, letting the audience answer in their head before you give the answer. The film cannot interact, so ask with clear space plus a subtitle and do not pretend there is interaction.

Optional “predict — observe — explain”: hold one beat before L4, ask “what do you think happens next”, then run it, then explain. Use it only when the prediction itself carries information; do not ask at every layer.

## The modality ladder for one piece of content

Text, image, web page and video are rising costs. The order is: fix the objects, numbers and terms in the cheapest form first, then move up one level, reusing the same knowledge pack at every level.

```text
 文字稿（受控表达）→ 图（载体与部件）→ 网页或动图（交互与分层）→ 视频（节奏与声音）
        └──────────── 同一个知识包：术语、账本、映射、层次 ────────────┘
```

What you cannot make clear in the script you will not make clear in the video. At the script stage you can already use `controlled_lint.py` to check sentence length, terms and pronunciation; the frame and the video then reuse the same terms and numbers. When you need a poster or a cover, derive it from an L4 or L6 keyframe; do not invent separate numbers.

## The seven layers for a news brief

A news brief has no mechanism, but it needs an order just the same. Use an evidence board as the carrier (see [the object as the explanation](knowledge-visualization.md)).

| Layer | What it holds in a news brief |
| --- | --- |
| L0 | the event in one sentence: who did what, when, as of which date |
| L1 | black box: the event is made of who, what was done, when, and what it affects |
| L2 | the people and objects that enter: each answers “who / what was done / on what basis / what is still missing” |
| L3 | relationship: timeline, candidate causes, points of dispute; mark a candidate cause “candidate” |
| L4 | one complete check: from the original source to the data to the conclusion, along one evidence chain |
| L5 | counter-example and boundary: unknowns, differing definitions, possible contrary evidence; an empty slot states why it is empty |
| L6 | review, pointers to sources, the as-of date `as_of` and the information boundary |

Numbers in a news brief must come with their definition and date; do not put different definitions into the same measure. Keep fact, commentary and speculation apart; a tidy layout does not mean it is verified.

## Audience level

`audience.level` takes novice, practitioner or expert.

- novice: define every term at first use; do not compress L2; use everyday counter-examples in L5.
- practitioner: define only terms this film coins or terms that are easily confused; L2 may be merged; L5 discusses the design trade-off.
- expert: do not define common terms by default (a term card's `define_on_first_use` can require it individually); compress L2 to one screen; L5 covers boundary conditions and known disputes.

## How this maps to the plan

In the knowledge pack each layer writes `scene_ids`, `focus_element_id` (L2 to L5), and optionally `claim_ids` and `element_ids`; L4 should link at least one claim that has a source or a derivation. For the fields and check codes see the [knowledge pack contract](knowledge-pack.md). These are structural checks, not proof of comprehension; whether a layer really adds only one load has to be checked with a novice reader.
