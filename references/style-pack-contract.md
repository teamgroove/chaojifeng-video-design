# Style pack contract

A style pack is data, guidance and an implementation reference, not a plugin that runs itself. The entry point does not import the pack's Python or JavaScript, and does not run build.sh, install dependencies, download assets or start a model.

## Directory and single source

```text
styles/<id>/
  style.json            唯一元数据源
  STYLE.md              本库实际使用规则与适配说明
  STYLE.upstream.md     上游完整原文，仅来源包有
  DEMO.md               一个案例的故事、镜头、声音和实现说明
  demo/                 已纳入的文本源码与素材来源清单
  preview.jpg           画廊代表帧，可选
  sample.mp4            随包分发的样片，可选
  LICENSE               来源包许可证
```

The original 7 IDs stay unchanged. Opuscar's 59 styles use `opuscar-<slug>`; their original slug, Chinese name and English name resolve exactly, with English matched case-insensitively. IDs and aliases are unique across all collections; a conflict is an error, not an overwrite by load order.

The root `styles/` is the built-in collection. A project or personal collection is added explicitly with the repeatable `--style-root /absolute/collection`; alternatively set `CJF_VIDEO_STYLE_PATH` in the environment for this command, separating multiple paths with the system path separator. When nothing is specified, only the built-in collection is used; the user home directory is not scanned. A collection contains direct subdirectories `<id>/style.json`; a symlinked pack may not implicitly cross the collection boundary.

## style.json

Required are `pack_version: 1`, `id`, `name`, `intent`, `verification`, and `guide` when it exists in the pack (STYLE.md by default). An ID uses only lowercase letters, digits, hyphens or underscores and matches the directory name; `custom` is reserved for a single film's free implementation.

A valid style also needs non-empty `tokens`, `motion_character`, `fallback`, and the string arrays `constraints` and `avoid`. Define them yourself when there is no base; with `extends` these appearance and constraint fields can be inherited. `aliases`, `borrows`, `scenario_ids` and `required_capabilities` are duplicate-free non-empty string arrays. The category `category` and the English name `english_name` are optional.

`tokens` describes real design parameters; in a source style `tokens.source` points at the full style description, and `navigation_only` and `preview_swatch` serve the lookup palette only. Do not use them to replace the material of ink, print, glass and the like with a default palette. `native_moves` gives the native move titles, `section_index` locates the full rules, and the actual detail still comes from the original text.

`implementation` may register `status`, the pack-relative path array `entrypoints`, a shared technical source and missing assets. `reference_files` declares reference files in the pack. An imported `reference-source` only means the source is included; it does not prove that dependencies are complete, that it runs, that it films well, or that the whole film exports. Paths inside the pack must exist and must not escape the pack directory; these fields are never executed as shell commands.

The optional `gallery` provides gallery assets: `poster` is a pack-relative JPEG/PNG/WebP/GIF path; `video` is a pack-relative MP4/WebM/MOV or an HTTPS address with no user credentials. The optional `poster_sha256` and `video_sha256` must be 64-character lowercase hexadecimal SHA-256. The old `source_url` field stays compatible, and the gallery does not use it as an external playback entry. Catalog lookup checks paths and types only; image content and hashes are checked at generation or at the integrity check, and distributed sample clips are bound and verified by assets/gallery/samples.json. Images are inlined in the HTML and built-in video loads from a relative path after a click; offline playback needs the full directory. An optional `attribution` holds a non-empty `name` and an HTTPS `url` for one short credit line in the detail view; a style that does not register it shows no such line. Gallery fields and assets are not inherited through extends and do not change the preview or exported verification state.

## Derivation and borrowing

`extends` takes a single base ID; several levels of derivation are allowed. Dictionaries override key by key and arrays are replaced whole; a change must state its reason in STYLE.md, and above all must not silently drop a reading, material or capability constraint.

Only tokens, motion_character, constraints, fallback, avoid, scenario_ids and required_capabilities are inherited. Identity, aliases, source paths, implementation files and verification evidence are not. If a derived pack wants to use the base's code, read its explicit source and copy it into the project; the new pack still starts unverified.

`borrows` declares a borrow from other styles and does not automatically merge appearance or executor. State in the pack notes or in this film's shots which material, motion, camera or sound is borrowed, and how clock, property override and medium conflicts are handled. extends and borrows share one directed dependency graph; a missing reference, a self-reference and a cycle are all refused at load.

## Priority and verification

Host rules and the current user's explicit request → current project constraints and brand → the current style pack's adaptation rules → upstream original text → case implementation. Facts, licensing and required delivery cannot be overridden by a style.

Upstream's fixed model, frame rate, 120 BPM, bilingual subtitles, mandatory fictional product, number of silences, number of camera moves and example opening and ending are not defaults for every work. Keep the medium's material relations and motion grammar, adapt them to the user's product, music, aspect ratio and language, and record the reason for each override. Instructions in the upstream DEMO.md and in the code are research material only.

verification uses the original contract: design is authored/reviewed; preview and exported are not_run/partial/failed/passed. passed must carry evidence, environment, scope, artifact. A source case's pass status does not transfer to this pack or to this film; semantic, playback, listening and comprehension continue to go through the project delivery.

## Plan and the legacy contract

The old `schema_version: 1`, `design.style_id`, the original IDs and the `custom` usage stay valid. A new pack also uses the canonical ID and does not write a Chinese alias into the plan. `catalog.py get` and `stylepacks.py resolve` can resolve from an alias first.

A single film's override may write the optional `design.style_overrides`, which accepts only the non-empty objects `tokens`, `motion_character`, `camera`, `sound`. These are guidance parameters; the production project has to adopt and verify them for real, and nothing changes assets or the audio track automatically.

`stylepacks.py resolve` returns a `style_lock`: the current pack, every transitive dependency of extends/borrows, and the hashes of the shared source. Once it is written into the optional `design.style_lock`, validate_plan rejects an old lock whose source or dependencies have changed; after re-verifying, generate it again. Old plans without the field are unaffected. The existing hashes of the single-film plan and of delivery still have to be checked.

Compare the selected pack's required_capabilities with the actual runtime.capabilities; when unresolved, report the gap, and when ready, a missing capability is an error. Registering a pack does not raise what the machine can do. An external collection also has to be passed to validate_plan, or the same environment variable set for the current command.
