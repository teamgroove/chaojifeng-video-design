# 中国水墨

Organise the current subject with the materials, composition, motion and sound-image grammar of Chinese Ink Wash.

## Order of use

Fix this film's through-line and each shot's purpose first, then read the [upstream style rules](STYLE.upstream.md) in full. Take its materials, colour, type, motion, camera, sound, native moves and failure repairs; this pack includes the sections Essence, and what it is not、Materials & rendering、Colour logic、Type & subtitles、Motion quality、Camera grammar、Sound palette、Native moves、Pitfalls of the medium、Engine、Variation space。

This film's facts, brand, user-specified music, language, aspect ratio and delivery cadence take precedence. A fixed model, 120 BPM, bilingual subtitles, a mandatory fictional product, a prescribed opening and ending, a fixed silence or a fixed number of camera moves are source constraints: judge them against this film's explicit requirements, and when the core of the style changes, record the reason for the override. Native materials and moves need a matching implementation; the lookup palette does not represent this style's appearance.

## Implementation and case

Once this film's structure is fixed, read the [case notes](DEMO.md) and use its Engine section to locate the code in `demo/`; reuse its brushes, masks, materials, characters, camera or sound-image schedule. Leave the source code as it is, copy it into the project and fix the asset paths first — do not run the in-repo build.sh directly. Shared tooling sits in `../../vendor/lemo-opuscar/`; that is a source reference and needs probing and wiring in this film's environment.

After reading the [asset sources](demo/CREDITS), reuse this film's licensed assets first, then fill in type, sound or models. Register source code, asset readiness, keyframes, the finished export, watching and the listening pass separately; this pack has not yet passed a full-film production acceptance check on this machine.

## Combining and extending

Per-film colour and timbre go into plan.design.style_overrides; a stable personal style is registered in a collection outside the project with a new ID and extends. borrows only declares where a borrow comes from — the borrowed moves themselves and any conflict handling go into the shots; it does not merge scenes or override sound automatically.
