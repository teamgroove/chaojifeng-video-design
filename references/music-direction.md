# Finding music passages from narrative intent

Use this for choosing, arranging and replacing score. First decide how this segment changes the viewer — from doubt to curiosity, from watching to acting, from tension to relief, for example. Then state the sound's job, the duration you need, voiceover density, the visual landing point and the textures you want to avoid, and search. A single track through the whole film, different sections of the same track, a combination across tracks, and silence can all work; three tracks or three acts are not mandatory.

## Music atlas and agent queries

Read the taxonomy in `catalog/music.json` or run a query instead of loading the full text of 100 tracks at once. `assets/music/index.html` is a self-contained atlas that supports searching by the eight scenario classes, emotion and narrative role, and locating waveforms, change points and candidate passages. The atlas does not contain the original songs; audition the original files only after importing the host registry. When the browser or host cannot play local files, keep the state unverified and do not work around its security restrictions.

```text
python3 SKILL_ROOT/scripts/music_library.py search --scenario product-demo --emotion curious --role establish --narration --avoid-bright --limit 5
python3 SKILL_ROOT/scripts/music_library.py search --scenario brand-film --role payoff --energy high --limit 5
python3 SKILL_ROOT/scripts/music_library.py get jy-137 --registry /project/music-registry.local.json
python3 SKILL_ROOT/scripts/music_library.py health --registry /project/music-registry.local.json
python3 SKILL_ROOT/scripts/music_library.py validate-sheet /project/music-cue-sheet.json --registry /project/music-registry.local.json
python3 SKILL_ROOT/scripts/music_library.py select --recipe knowledge-music-explainer
python3 SKILL_ROOT/scripts/music_library.py search --recipe knowledge-music-explainer --limit 5
python3 SKILL_ROOT/scripts/music_library.py select --recipe knowledge-music-explainer --track TRACK_ID
```

Queries return passages, not just songs. Emotion and usage are directorial suggestions, and the ranking score is not aesthetic quality. When nothing matches, relax one condition, audition other sections of the same track, or find newly cleared music; do not force a fit. Within a track, relative_energy is separate from whole-song arousal: the former is relative signal strength, the latter is an emotional-arousal suggestion still awaiting audition. A low share of low-frequency spectrum does not guarantee a comfortable sound, and a no-vocals first pass does not guarantee the voiceover will not be masked.

The first library of 100 tracks and 298 candidate passages comes from linked Jianying member chart candidates. Each track has a stable ID, source rank, original name/author display text, SHA256, emotion, scenario, narrative role, timbre, avoid-notes and evidence. Titles may contain OCR truncation; keep the captured information and do not invent an accurate author or release identity from it.

The three evidence classes each keep their own state:

- measured: the whole track has had mono 16k signal analysis — roughly per-second energy, spectrum and local change — reusing the original 10-second continuous AudioSet detection. It is not phrase, bar or key detection.
- inferred: a directorial reading supported by the title's claim, the model's instrumental/genre cues and the measured features, with a confidence level and avoid-notes. Where evidence conflicts, keep the note; emotion is never derived from energy alone.
- audition: still not_run for the first batch. After actually listening, record the listener/tool, time, passage, conclusion and evidence in the project; do not upgrade the whole library to passed.

## Default music and candidate pool for concept knowledge explainers

On 2026-10-20 the user supplied "知识分享背景音乐神曲.wav"; on 2026-10-21 it was confirmed as the initial default music for the "concept knowledge explainer" recipe, with support for adding candidates and changing the default. The stable ID is `user-knowledge-sharing-theme`; the original measures about 119.083 s (48 kHz, stereo, 16-bit WAV), and the catalog's exact duration and hash take precedence. The source lives in the host's persistent music directory and is registered in the default registry; later use does not depend on the original in Downloads.

- The music library records track facts and assets; the recipe's `music_policy` records candidates and the default reference. A user specification outranks a project selection, which outranks the recipe default. When this recipe is used and nothing is specified, adopt the current default directly without asking again; a request for no score or for original sound takes precedence. Other recipes configure their own; do not make this track the global default for every explainer or tutorial.
- A one-off specification, a project selection, adding a candidate and setting a default are handled separately. When the user explicitly adds a candidate, register the verified track ID, source, hash, actual duration and purpose, then add it to the recipe pool; only a track already in the pool can be set as default. One selection changes neither the pool nor the default, and a new candidate does not automatically succeed to the default. `select --source-file` applies a track to this project directly; changing the global library first is not mandatory.
- This recipe works backwards from the chosen music: verify the track and the music map first, then allocate the problem, condition, mechanism, reveal and ending, and last the subtitles and motion. After a track change, do not inherit the old track's BPM, hit times, key, continuation or audition conclusions. `select` checks the chosen local source and returns blocked when it is missing or changed; it never swaps tracks silently, and it does not replace a license check, the music analysis or a listening pass.
- Once the user has chosen it: for a shorter video, trim the original; if the film runs longer than the track, continue from the top for a second pass, keeping only the part needed to fill the runtime and cutting the surplus audio after it. If that is still not enough, continue the same way; do not switch tracks or change speed just because the film got longer.
- Direct continuation example for a 120-second video: the first pass plays the original `[0, 119.083)`, the second plays roughly the opening `[0, 0.917)`, landing in the cut at `[0, 119.083)` and `[119.083, 120)` respectively. The example times are rounded; compute with the exact duration. Recompute the fill amount after a crossfade, tail silence or an adjusted cut point. Runtime means the actual length of the whole film.
- For each pass the cue sheet uses a different placement ID with the same track_id and source hash, and records source_in/out and timeline_start/end separately; keep the reason "same track continued to fill the length". A loop is not seamless: audition the seam, the first hit and the tail against the actual voiceover, adjust the cut point, a short fade and the ending fadeout where needed, and keep the finished length exact.
- This track's purpose and its initial default come from the user's instruction; basic signal analysis does not prove emotion, absence of vocals, voiceover fit or how a loop sounds. Audition, beat measurement and key currently remain unverified, and the source is not publicly distributed. The continue-from-the-top method above belongs to this track only; other candidates get their duration fit arranged independently.

```text
python3 SKILL_ROOT/scripts/music_library.py get user-knowledge-sharing-theme
python3 SKILL_ROOT/scripts/music_library.py search --scenario knowledge-explainer --query user-knowledge-sharing-theme --limit 1
```

## Choosing passages and editorial judgement

For knowledge explainers, [concept knowledge explainer arrangement](knowledge-music-direction.md) builds a hash-bound map of beats, phrases and sections for the chosen source, reusing the analysis and re-sorting it per film; candidates and auditioned anchors stay separate. BPM does not include downbeat or bar information, and one work's tempo cannot be applied to another. Map along the existing cue sheet into the cut, choose landing points for important events, and cross beats or extend when there is not enough reading time. When this recipe has no specification, use its own default music directly; other recipes follow their own configuration. A test-cut confirmation never blocks an explicit direct delivery.

Try the story against a few candidates first; do not pile on tracks blindly while browsing. source_in/source_out in the library are real seconds in the original file, and a passage may be a sparser bed, a stronger push, an energy build or a fall-back candidate; it is no claim to have found the chorus or "the best passage". A low-energy/low-change point near the in point only helps the rough cut — in the end check whether the melody is truncated, whether the first hit is abrupt, whether the tail is cut off. Leave handles before and after, and look for a complete phrase again where needed.

Let the content decide whether to stay on one track. A track change needs a narrative reason, for example moving from the problem to system capability and then landing on the human benefit. Keep a shared rhythmic motif, timbre or sense of space; you can also separate with action sound, an ambience bridge or deliberate silence. Without beat or key measurement, do not claim the same key or tempo, and do not layer long melodies directly; audition the overlap even for a simple fade. A speed change, loop or re-arrangement needs its implementation and listening pass recorded separately, and no passage is stretched to an arbitrary length by default.

A technological feel can come from rhythmic order, layered space, the scale of low and mid frequencies, and precise feedback. When the user reports shrill sound or a monotonous score in a given round, check timbre, section contrast and narrative development together; do not manufacture a technological feel by making every track brighter and louder, and do not fill the whole film with random notes or a single loop.

## Cue sheet and two clocks

Use `templates/music-cue-sheet.json` and keep one copy of the real data in the project. Each placement has a unique id, track_id, cue_id, source_sha256, source_in/out, timeline_start/end, narrative role, fades and the reason for the join. Source-track time and whole-film time stay clearly separate, and intervals are half-open. No speed change by default, so the two spans should be equal; overlap created by a crossfade must be counted in the cut's clock. A complete track may omit cue_id, with the source range covering the part actually used.

The original plan contract does not change: the trimmed/mixed file you finally produce becomes plan.assets, scenes.audio_cues reference the real file by whole-film absolute time, and the cue sheet is the editable source recording the original track's provenance and the edit. `validate-sheet` checks source, clock, hash and the overlap reason; it does not prove the audio is rendered, in the same key, comfortable, or correctly placed against the picture. List permissions, missing assets and anything not yet heard separately.

## Asset location, sources and extension

The skill stores indexes, tags and method; it does not distribute paid music. Local files relate to path/sha256/duration_seconds by track_id inside the registry's assets; prefer `--registry`, then `CJF_VIDEO_MUSIC_REGISTRY`, otherwise look in the current user data directory `$XDG_DATA_HOME/chaojifeng-video-design/music-registries/<library_id>.json` (the same location under `~/.local/share` when the variable is unset). The first batch is registered on this host, so a later chat can get/health without knowing the original output directory. On a new host with no registration, report the files as missing; do not guess a source path. Caches can be cleared at any time — run a health check before use, and do not treat a path's existence as permanent custody or proof of license. After a migration, verify by content hash, and do not silently substitute a file of the same name.

Per-item usage of the first-batch assets is not yet verified, and a membership cannot automatically be taken as permission for outside editing, commercial use or redistribution. Check against the music's current license marking, the platform and the project's purpose, and keep the evidence; assets that restrict outside editing should be arranged within what Jianying permits. If the current render route cannot do that, replace them with tracks carrying the matching usage license and keep the emotion/section requirements; a reference track must never be labelled as the final actual source.

To extend with any lawful local music, follow the schema and taxonomy, add necessary tags with their definitions, and keep source, license, hash and the basis for segmentation. Analyse the actual audio track first, then explain the usage; never claim per-track audition in bulk by song title. Run `validate-catalog`, then audition and render for this film. Do not write the first 100 tracks as a mandatory dependency for every user or host.

Method basis: [AudioLabs music structure analysis](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C4/C4S4_NoveltySegmentation.html) explains local change and section candidates; this library uses a lighter heuristic on the difference between preceding and following features and does not implement its full SSM pipeline. [FFmpeg filters](https://ffmpeg.org/ffmpeg-filters.html#atrim) provide a reference implementation for trimming and bridging; check the current tool's support for the actual parameters first. The first batch's boundary keeps the [Jianying asset agreement](https://sf1-cdn-tos.douyinstatic.com/obj/ies-hotsoon-draft/vco/f72e9cd9-cc19-4db7-ba74-0794833ce854.html) as its source, which does not replace a per-item check of the usage scope.
