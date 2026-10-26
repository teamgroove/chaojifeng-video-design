# Industry standards first: find the consensus before you speak

Read this when an explainer touches a professional domain. First find the standards, terminology norms and industry consensus that fit the domain best, then use them to write the script and draw the diagrams, so the expression is shorter and more accurate and the agent does not rewrite industry terms from memory. It applies to narration, subtitles, nameplates and captions; it is not a copy style guide — creative copy may use the exception in the last section.

## Why

Aircraft maintenance manuals rely on ASD-STE100 (Simplified Technical English), a controlled language, so that readers with different native languages read the same meaning. The approach: write information precisely with a limited rule set and a controlled dictionary. Public discussion often sums up the same idea as a ladder of upgrades — controlled language → diagram → web page → video (only second-hand accounts were read, the original post was not obtained, so it is not used as a primary source). This skill borrows that line of thought: every step up in medium reuses the same terminology, numbers and rules, instead of rephrasing at each level.

The boundary has to hold (official Issue 9, 2025-01-15, checked 2026-10-19):

- STE cannot be used on its own; it needs technical publication specifications, style guides and official directives alongside it.
- STE does not govern abbreviations, units of measurement or typography; the project or the industry standard decides those.
- STE was developed for technical documentation only; the official text says only that its rules and controlled dictionary "can help" spoken communication in meetings and presentations — it is not a narration standard.
- STE-zh in this skill is a self-made Chinese rule set, not an official ASD standard, and the numeric thresholds are not ASD numbers; do not claim that anything "complies with ASD-STE100".

## The four steps

```text
 ① 识别领域 → ② 找规范与共识 → ③ 写成术语卡与表达规则 → ④ 全片遵守并核对
  domain.field   domain.standards     domain.terms / expression     controlled_lint.py
```

1. Identify the domain: write it into `domain.field`. Register each domain separately when work crosses domains.
2. Find the standards and consensus, reading in priority order: international standards or IETF RFCs > national standards > industry associations and official documentation > authoritative textbooks and term databases > historical industry consensus. Read the current version and note the version, the locator and the check date.
3. Write term cards: for each term the preferred form, definition, forbidden aliases, abbreviation and pronunciation. Write expression rules: choose `expression.profile`, loosen or tighten sentence length as needed, and add a pronunciation list.
4. Follow it across the film: the same word in narration, subtitles, nameplates and captions; run `controlled_lint.py` for mechanical problems; check the current version once more before the final cut.

When you cannot find a suitable standard, write `kind: none` and the reason truthfully, make term cards for this film only, and do not invent a standard's name.

## Source status

| status | Meaning | Requirement |
| --- | --- | --- |
| verified | the original text was read for this task, version and locator checked | must have `version`, `locator`, `checked_on`; older than a year prompts a re-check |
| seed | only a starting point, the original was not read or only a summary was read | verify version, clause and current status before use; a claim built on a seed is flagged |
| not_found | searched, no suitable source | must write `reason` |
| none | no applicable standard in this domain | appears together with `kind: none`, must write `reason` |

`kind` may be standard, terminology, style-guide, convention, official-doc, consensus, none. When choosing consensus (historical industry consensus), list at least two mutually independent authoritative sources. Do not copy long passages of a standard; record only the locator and the necessary phrases.

## Domain starting points

Starting points only. Items marked "checked" were read during research on 2026-10-19; the "seed" items were not read in the original. Both kinds must be checked again against the current version before use, national standards above all (the GB 3100/3101/3102 series on quantities and units, for example, is being revised and replaced, so the current number and version must be verified before use).

| Domain | Starting source | Status |
| --- | --- | --- |
| Network protocols | IETF RFCs, current version at rfc-editor.org; e.g. RFC 9293 (STD 7, August 2022, obsoletes RFC 793) | checked §3.5, figure 6 and figure 8 of RFC 9293 |
| Technical writing and controlled language | ASD-STE100 Issue 9 (2025-01-15) | checked the rule numbers and the applicability boundary |
| General clear expression | ISO 24495-1:2023 Plain language, Part 1: Governing principles and guidelines | checked that it exists and what it covers; read the original before using a clause |
| Multimedia learning | Mayer's multimedia learning principles (12 in the 2nd edition, 15 in the 3rd edition, 2020) | checked the counts; state which edition you use |
| Chinese punctuation and number usage | GB/T 15834-2011, GB/T 15835-2011 | checked the numbers; confirm they are currently in force before use |
| Chinese scientific and technical terms | China National Committee for Terms in Sciences and Technologies, "术语在线" (Termonline) | checked the entry point; look each term up one by one |
| Anatomy | Terminologia Anatomica, 2nd edition (FIPAT, 2019) | checked |
| Electrical graphical symbols | IEC 60617 | checked |
| Safety signs and colours | ISO 7010:2019, ISO 3864-1 | checked |
| Gears and axonometric drawing | ISO 1122-1:1998, ISO 701:1998, ISO 5456-3:1996 | checked |
| Quantities and units | BIPM SI Brochure, ISO 80000 series, International Vocabulary of Metrology (VIM) | seed |
| Chemistry | IUPAC Gold Book | seed |
| Software and systems engineering terms | ISO/IEC/IEEE 24765 | seed |
| Modelling notation | UML, BPMN (OMG) | seed |
| Aviation radio phraseology | ICAO standard phraseology | seed |
| News writing and verification | AP Stylebook, Reuters Handbook, Xinhua's banned and cautious words in news reporting; IFCN code of principles | seed |
| Data visualisation | Cleveland–McGill perceptual ranking, FT Visual Vocabulary | seed |
| Accessibility and colour | WCAG, Okabe–Ito colour-blind-safe palette | seed |
| Analogy and cognitive load | Gentner's structure mapping, Lakoff–Johnson conceptual metaphor, Sweller's cognitive load, predict–observe–explain | seed |

## STE-zh: controlled expression

`controlled_lint.py` checks mechanical problems only: sentence length, semicolons, passive voice, vague words, whether a term is defined at first use, forbidden aliases, and pronunciation for narration. It does not judge whether a fact is correct, whether a metaphor fits, or whether the audience understood.

| Check code | Which STE rule it comes from | Chinese adaptation | Default level |
| --- | --- | --- | --- |
| sentence_over_target / sentence_too_long | 5.1 procedural sentences ≤20 words; 6.3 descriptive sentences ≤25 words | by character count: description and notes 22/30, procedure and warning 18/24 (target / hard ceiling) | over target is a hint, over the hard ceiling a warning |
| too_many_sentences | 6.6 paragraphs ≤6 sentences | ≤6 sentences per paragraph | warning |
| semicolon | 8.1 no semicolons | same | warning |
| passive_marker | 3.6 use the active voice | detects "被" sentences | warning; a hint in the spoken profile |
| multiple_instructions | 5.2 one instruction per sentence | conjunctions joining parallel actions in procedure and warning sentences | warning |
| forbidden_alias | 1.11 do not use different technical names for the same thing | the term card's `aliases_forbidden` | error |
| undefined_on_first_use | 1.8 use technical names accepted in the field | define it at first use (an addition by this skill) | warning |
| vague_word, unclear_reference | similar in spirit, no direct clause | vague-word list, pronouns at the start of a sentence | warning, hint |
| colloquial | 1.10 no slang and no jargon | colloquial word list | warning in the technical-text profile; off in the spoken profile |
| missing_pronunciation, symbol_in_speech | STE does not cover spoken delivery | spoken-profile addition: foreign words with no pronunciation, symbols in narration | warning, hint |
| placeholder_text | none | TODO, 待填写, 待补充, TBD | error |

The sentence-length numbers are a listening estimate: about 4–5 characters per second, so a hard ceiling of 30 characters is about 6–7 seconds. A project may override them in `expression.limits`. The STE controlled dictionary (part 2) is not copied here; term cards replace it — they cover only the words this film uses.

Two profiles:

- `ste-zh-v1`: technical text, subtitles, nameplates, captions.
- `ste-zh-spoken`: narration and voiceover. Friendly colloquial speech is allowed, but terms, sentence length and pronunciation stay controlled.

```text
python3 SKILL_ROOT/scripts/controlled_lint.py --text-file script.md --profile ste-zh-spoken --glossary pack.json
python3 SKILL_ROOT/scripts/controlled_lint.py --text-file script.md --glossary pack.json --emit-speech speech.txt
```

`--glossary` may be a knowledge pack or a plan with an inline `knowledge`. After the check passes, `--emit-speech file` applies the pronunciation list to the script and writes out text you can hand to speech synthesis; it refuses to overwrite an existing target file, and it does not judge whether the reading is right. In the script, a line of its own, `<!-- kind=procedure layer=L2 id=seg-03 defines=term-a lint=off speak=off -->`, annotates the next paragraph with its type, layer and already-defined terms, or turns off the check and the reading.

## Pronunciation dictionary

Speech synthesis often misreads English abbreviations. Foreign words and abbreviations that appear in narration must have their reading written in `expression.pronunciations` or in the term card's `spoken_as`, for example write "SYN" as "S Y N". `plan.scenes[].narration[].spoken` holds the final reading after the pronunciation list has been applied, `display` holds the canonical subtitle form; it is normal for the two to differ. Numbers that look like identifiers (a standard number, say) also get a reading of their own.

## Exceptions

Creative copy, poetic voiceover and brand slogans may set `expression.profile` to `none` and write a `reason`. The standard gives way to audience comprehension: do not turn natural speech into awkward speech just to pass the check. Passing the check does not prove it is well told; whether it is well told is checked by novice readers and by readers who know the field (see the [knowledge pack contract](knowledge-pack.md)).

## Minimum term card

```json
{
  "id": "term-seq", "preferred": "序号", "abbr": "SEQ",
  "definition": "发送方给报文段编的号",
  "standard_ref": "std-rfc9293", "aliases_forbidden": ["序列号"]
}
```

The preferred form, forbidden aliases and abbreviation are unified across the film; the definition stays short and is written the way a viewer could say it out loud.
