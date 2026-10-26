# Knowledge pack contract

When explaining abstract knowledge or news, use one knowledge pack to record “what standard this follows, which words you use, which thing maps to which concept, where each number comes from, in what order you tell it, what you checked”. Method in [The object is the explanation](knowledge-visualization.md), [Layered progression](layered-reveal.md), [Domain standards first](domain-standards.md). This note covers only the fields, the checks, and the wiring.

A knowledge pack checks structural, referential, and textual mechanical problems only. It cannot judge whether a metaphor fits, whether a fact is true, or whether the audience understood; those stay in `checks`, and remain `not_run` if you did not do them.

## Where it lives

- Embedded in a plan: write it in `plan.knowledge` and also record the `knowledge.*` expressions you use in `design.expression_ids`. `validate_plan.py` checks the scene, element, and voiceover IDs along with it, and runs the controlled-expression check on voiceover and element text.
- Standalone file: when you have only a script and no plan, write it as a separate JSON with `"schema_version": 1` at the top level, and let each layer point at the matching passage in the script with `script_ref`.
- You can make a video without a knowledge pack. These checks trigger only when the plan writes `knowledge` or selects a `knowledge.*` expression; other scene behaviour is unchanged.

```text
python3 SKILL_ROOT/scripts/validate_plan.py plan.json                    # 含 knowledge 时自动一并检查
python3 SKILL_ROOT/scripts/validate_plan.py plan.json --strict-knowledge  # 知识类警告升为错误
python3 SKILL_ROOT/scripts/knowledge_pack.py plan.json                   # 只检查计划里的知识包
python3 SKILL_ROOT/scripts/knowledge_pack.py pack.json --plan plan.json  # 独立知识包对照某个计划
python3 SKILL_ROOT/scripts/controlled_lint.py --text-file script.txt --profile ste-zh-spoken --glossary pack.json
```

`--strict` treats every warning as an error; `--today YYYY-MM-DD` makes the checked-date check reproducible.

## Fill-in order

1. `topic`, `claim`, `relation_type`, `audience`: the relation in one sentence and the audience's starting point.
2. `domain`: find the standard and register its status first, then write the term cards.
3. `truth`: register every number and fact. A news pack also writes `unknown`.
4. `carrier`: choose the carrier, write the part mapping and the break points; if there is no honest carrier, write the fallback.
5. `layers`: arrange the layers, one new load per layer, and write the bridge and the exit test.
6. Write the voiceover or the picture, and use `controlled_lint.py` to check sentence length, terms, and pronunciation.
7. `checks`: change a status only when you actually did the work, and write the evidence.

## Fields

Required fields are marked “req.”. Unless stated otherwise, every string must be non-empty.

| Position | Field | Notes |
| --- | --- | --- |
| Top level | `topic` req., `claim` req. | What it is about; the one sentence the viewer can say at the end |
| Top level | `relation_type` req. | `process` `condition` `capacity` `hierarchy` `comparison` `feedback` `transform` `concurrency` `probability` `growth` `causal` `event` `definition` `other` |
| `audience` | `level` req. | `novice` `practitioner` `expert`; `known`, `unknown` are string arrays |
| `domain` | `field` req., `standards` req., `terms` | Domain name; standard cards; term cards. `notation` can record symbols, units, and capitalisation conventions |
| `standards[]` | `id` `title` `kind` `status` req. | `kind`: `standard` `terminology` `style-guide` `convention` `official-doc` `consensus` `none` |
| | `status` | `verified` checked; `seed` seed source, still to check; `not_found` looked and found none; `none` genuinely not applicable |
| | `version` `locator` `checked_on` | Required for `verified`: which version you checked, which clause, on which day (`YYYY-MM-DD`) |
| | `url` `scope` `sources` | `consensus` needs at least two independent authoritative sources; `none` and `not_found` need a `reason` |
| `terms[]` | `id` `preferred` req. | Preferred word; `abbr` abbreviation; `spoken_as` how it is read aloud |
| | `definition` | One-sentence definition; may be omitted when `known_to_audience: true` |
| | `standard_ref` or `source` | Which standard or which place the word comes from; at least one of the two |
| | `aliases_forbidden` | Forbidden aliases, which may appear neither in narration nor on screen |
| | `define_on_first_use` `known_to_audience` | Booleans; when the former is `false`, the first-use definition is not checked |
| `expression` | `profile` req. | `ste-zh-v1` (subtitles, name plates, captions), `ste-zh-spoken` (voiceover), `none` (must write a `reason`) |
| | `limits` `pronunciations` `allow` `vague_extra` | Override the sentence-length cap; letter and abbreviation readings; check codes allowed for this film; additional vague words |
| `carrier` | `kind` req. | `object` `spatial` `process` `data` `diagram` `none`; `none` needs only a `reason` |
| | `object` `mechanism` `fallback` req. | What the carrier is; how it works; what you fall back to when the carrier fails |
| | `limits` `mappings` | Overall break point; mapping table. At least 3 items for `object`, at least 2 for `spatial` `process` `data` |
| `mappings[]` | `id` `concept` `part` `breaks_at` req. | One concept to one part; where the metaphor will lie to you |
| | `fidelity` req. | `exact` `structural` `illustrative` |
| | `questions` req. | `what` and `why` are required; `happening` `use` optional |
| | `element_id` `layer_id` | The element in the picture; the layer where it first appears |
| `truth.claims[]` | `id` `text` `kind` req. | `sourced` `derived` `illustrative` |
| | `sourced` | `standard_ref` or `source`; a news pack also needs `as_of` |
| | `derived` | `derivation` and `from` (the ID of the source claim, no cycles) |
| | `illustrative` | `disclosure`: internal record of the illustrative purpose, the basis, and the conclusions it cannot support; not rendered as an outward production label |
| | `value` `unit` `as_of` `used_in` | A value needs a unit; the date; the voiceover or element ID that uses it |
| `truth.unknown[]` | `id` `text` `status` req. | `unconfirmed` `disputed` `unknown`; `reason` says why it is not confirmed yet. Required in a news pack; when there are none, write `truth.unknown_none_reason` |
| `layers[]` | `id` `level` `goal` `new_load` `exit_test` req. | `level` runs from `L0` to `L6`; the last layer must be `L6` |
| | `bridge_from_previous` | Required except on the first layer: what of the previous layer becomes what of this one |
| | `scene_ids` `focus_element_id` | Required when embedded in a plan; `L2` to `L5` also need one lit element |
| | `script_ref` | Required in a standalone file; points at the layer marker in the script |
| | `claim_ids` `element_ids` `chapter` | The claims and elements used by this layer; a long film can use `chapter` to climb the layers again |
| | `model_boundary` `extension_pointers` | Required for `L6`: what was not demonstrated, where the metaphor lies; where to read on |
| `checks` | `terminology` `accuracy` `novice_read` `peer_read` `expert_read` | Each item `{status, evidence}`; `status` is `not_run` `passed` `partial` `failed` |

`passed` must have evidence stating what was actually done, by whom, and when. Do not write a check you never ran as `passed`.

## Check codes

An error makes `valid` false; a warning is marked (w) and becomes an error in strict mode.

| Scope | Check codes |
| --- | --- |
| Structure | `pack_type` `schema_version` `object_type` `array_type` `string_array` `boolean_type` `required_string` `stable_id` `duplicate_id` `placeholder_text` `template_text` (w) `relation_type` `audience_level` `notation` |
| Standards | `standards_required` `standard_kind` `standard_status` `standard_none_status` `consensus_sources` `verified_incomplete` `checked_on_format` `checked_on_future` `stale_standard_check` (w) `standard_unverified` (w) `no_verified_standard` (w) |
| Terms | `no_terms` (w) `term_standard_reference` `term_source_required` `duplicate_term` `alias_conflict` `alias_is_preferred` |
| Expression | `expression_profile` `expression_limits` `pronunciations`, plus the [controlled-expression check codes](domain-standards.md) forwarded from there |
| Carrier | `carrier_kind` `mapping_count` `mapping_fidelity` `mapping_questions` `unknown_question` (w) `mapping_not_one_to_one` `mapping_layer_reference` `mapping_element_reference` |
| Truth | `claims_required` `claim_kind` `claim_source_required` `claim_standard_reference` `claim_on_unverified_standard` (w) `claim_from_required` `claim_from_reference` `claim_cycle` `claim_value` `claim_unit` `claim_as_of` `claim_used_in_reference` `number_not_in_ledger` (w) |
| News | `event_claim_as_of` `unknown_required` `unknown_status` |
| Layers | `layers_required` `layer_level` `layer_order` `first_layer` `bridge_required` `multiple_new_loads` (w) `layer_claim_reference` `layer_scene_required` `layer_scene_reference` `focus_required` `focus_reference` `layer_element_reference` `layer_unanchored` `closing_layer_required` `closing_incomplete` `run_without_numbers` (w) `run_not_grounded` (w) `scene_without_layer` (w) |
| Checks | `check_status` `check_evidence` `unknown_check` (w) |
| Plan wiring | `knowledge_pack_missing` (w) `knowledge_expression_unrecorded` (w); and, when a `knowledge.*` expression is selected but no matching ID is found, the plan contract reports `design_reference` |

### A few rules that are easy to misread

- One concept to one part, and the reverse as well; a concept or part name appearing twice reports `mapping_not_one_to_one`.
- A standard in `seed` status is usable, but every claim that references it gets a warning; check it before you claim to be ready.
- A `verified` date more than 365 days old gets `stale_standard_check`: standards get revised, so look up the current version again.
- `number_not_in_ledger` scans only numbers of two digits or more, not single digits; what it guards against is “a number on screen that the ledger does not record”.
- The controlled-expression check runs once on the voiceover and once on element text, and reports once when the two are identical.
- A term needs a definition at first appearance: either a cue such as 是指、表示、就是、是一种 in the same sentence, or the next sentence starting with the term or with 它、该 and giving the definition. If neither holds it reports `undefined_on_first_use`.

## Examples

| File | Purpose | Status |
| --- | --- | --- |
| [tcp-handshake.plan.json](../examples/tcp-handshake.plan.json) | Mechanism type on real facts: the carrier is a “reconciliation table”, the standard is taken from RFC 9293 §3.5 | Structural example, no video generated; facts checked on 2026-10-19 |
| [evidence-board.plan.json](../examples/evidence-board.plan.json) | News type: an evidence board; events and numbers are all fictional | Fictional example, must not be published as news |
| [correlation-common-cause.knowledge-pack.json](../examples/correlation-common-cause.knowledge-pack.json) | Falls back to a relation diagram when there is no honest carrier; a standalone knowledge pack, validatable on its own or against an existing plan with `--plan` | Fictional scenario. Standalone it validates without warnings; against the plan it reports one `semicolon` warning because of the semicolon in the plan, which is expected |

Templates in [knowledge-pack.json](../templates/knowledge-pack.json); eval prompts in [knowledge-method-evals.json](../evals/knowledge-method-evals.json).
