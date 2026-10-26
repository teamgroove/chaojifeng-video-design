# Let narration, sound and image finish the understanding together

Read this when narration or voiceover is needed; it applies to knowledge explainers, product demos, news briefs, stories and brand films. A task that is only silent motion design, or that keeps its original audio, needs no voiceover work. The capability comes from combining a general script, actual audio and timing records — it does not require installing a personal-avatar to-camera Skill or a fixed cloud service.

## First arrange how the audience will understand

1. State the audience's starting point, the one relationship to be understood this time, and what they can recognise or do at the end. Prove it with existing facts, examples, the interface or source material; choose question → process → result, contrast, or cause and effect to suit the content — do not mechanically impose a uniform three-act.
2. Write short narration passages, one complete thought each. Record separately the pronunciation of terms, numbers, abbreviations, stressed words and pauses; keep fact and metaphor apart. Say what the listener needs to know first; on-screen text adds the key relationship or the result instead of piling up the voiceover word for word.
3. Give each passage its evidence and its share of attention: show the object first, then reveal the change, then hold on the result. Charted relationships, operation feedback and real material come before decoration. Captions, source material, visual emphasis and an optional presenter are separate layers.
4. Once the real voiceover exists, measure the clause timings, then map them onto the existing scene, beat and audio cue. Check the opening, the important causal steps, the action results and the ending separately; an estimate is not a measurement. No second, hand-maintained timeline is needed.
5. When explaining a professional field, a protocol, a mechanism or a news item, register the standards and terminology per [Domain standards first](domain-standards.md) first, then write to controlled expression: one sentence one thing, one word one meaning, pronunciation recorded for non-native words. Layer per [Layered reveal](layered-reveal.md), one new thing per layer. Use `controlled_lint.py` to check sentence length and terminology, and `--emit-speech` to apply the pronunciation table to the script before it goes to voiceover; a passing check does not mean it is read correctly or explained clearly — you still have to listen.

Record alongside the existing plan, as needed: passage ID, script and pronunciation notes, fact sources, the relationship to be understood, on-screen evidence, audio file / hash, source in and out points, time in the main film, reveal and dwell, acceptance status. A simple film can put this in the shot notes directly; no extra table is required.

## Prepare a traceable voice reference

Use a voice the user has licensed. Do not automatically apply a built-in timbre when the user has not asked for this particular person to narrate. Keep the original sample and the derived audio separately, recording source, purpose, hash, format and the actual listening pass; a reference existing does not mean a clone model is trained or an identity is verified.

The public version ships no voice samples. Users prepare a licensed reference inside their own project, build a voice manifest, and record the original file, the processed derivation, SHA256, format, scope of use and actual listening-pass status. A reference passing does not mean the speech engine or the later narration has passed.

An exported project contains only the files licensed for this delivery; a voice reference needs its recipient and distribution scope checked separately.

## In background noise cleanup, protect the voice first

- Identify first: steady noise floor, low-frequency vibration, reverb, background music or other voices — choose the treatment from the actual problem. Ordinary FFT noise reduction is not dereverberation and does not separate background music.
- Keep the original, save a processed copy separately. Use a low cut only on low-frequency interference that needs it; start with light noise reduction, and do not open by stacking a hard gate, heavy compression, a strong low-pass, pitch shifting or brightening. Do not damage consonants, soft speech, breath, sentence endings or the speaker's own vocal texture in pursuit of complete silence.
- Compare the same sentence and the same pause at matched perceived level, and listen for swirling water, metallic edge, pumping, sibilance, clipped tails and a thinned timbre. Waveform, spectrum and silence-section numbers only locate the problem; they cannot replace a listening pass or a voice-similarity judgement.
- After processing, verify sample rate, channels, full duration, head and tail, peaks and decoding. A filter may have tail latency; validate against the real sample length for this job, with the pre-roll and tail pad flush it needs — do not simply trim away voice that has not been output yet.
- When light noise reduction is still not enough, speech enhancement may be tried within existing capability and licence. Audition mouth noise, soft speech and timbre separately, and promise no separation of arbitrary speakers or accompaniment. Re-check after changing the reference; an old candidate's acceptance status does not transfer to the new file.

If the tool cannot listen to audio, keep `not_checked` and hand over the original and the processed version for a listening pass; do not pass a drop in loudness off as the real amount of noise removed or as a clarity gain.

## Separate reference, engine and acceptance

| Status | Evidence required |
| --- | --- |
| reference_ready | The file decodes, and source / licence match the hash; noise reduction has its own derivation record |
| engine_ready | The current engine and the required model can actually generate; record version, resources and billing path |
| text_verified | Check the new script for dropped words, added words, numbers and pronunciation; a transcript is an aid only |
| voice_verified | A listening pass against the licensed reference, recording similarity and naturalness; never inferred from a file existing or from the model's own assessment |
| narration_ready | The chosen actual narration has passed acceptance, its duration measured and bound to this film's timing and version |

TTS means text-to-speech and can be local or cloud; do not equate the name with cost. For a cloud service use the current plan / quote and the authorised budget, not a unit price carried over from an older chat. Prefer the local route the user asked for; if it fails, do not quietly switch to a paid API, a system voice or someone else's voice. Where an existing cloud timbre is involved, establish separately how it relates to the local reference, and do not claim a local WAV is its training sample. Read credentials on demand through the host's vault interface; never write them into the Skill or the project.

## Narration from an ACE voice reference: experimental branch

ACE-Step officially supports a global timbre condition from reference audio plus `[spoken word]`; the community has a TTS-like route that formats a new script as lyrics and adds a reference timbre. These mechanisms are worth measuring; none guarantees word accuracy, no accompaniment, no singing or a stable identity. Record official music capability, community XL examples and this machine's plain Turbo capability separately.

Check the local environment, models and running processes first, and reuse what is already there. With one new script passage and a fixed seed, compare no reference against the licensed voice reference serially; replaying the reference as-is does not count as cloning. For dry Mandarin narration you can experiment with recitation tags and with music semantic planning switched off; take the actual parameters from local code / docs you have verified, and do not transplant another variant's nodes. Initialise once and reuse it across several short trials; do not train first, batch long films or auto-download large models.

Check text, speech versus singing, background music, pauses and complete sentence endings first, then judge similarity to the person, naturalness and listening fatigue. When comparing the effect of the original versus the denoised reference, hold everything else fixed; a dimension you have not measured stays unknown. Only a pass makes it a narration candidate for this project; on failure keep the audio, the parameters and the reason, adjust the most relevant factor, or choose a dedicated local voice route within what the user has licensed. Do not extrapolate from one sample to "this model can or cannot narrate".

Keep experimental scripts and sample clips in this project's output; do not stuff dependency paths, model weights or unaccepted audio tracks into the general Skill. Accept ACE score and ACE narration separately; music sounding good does not prove it reads a script accurately.

## Optional presenter and lip sync

Decide first whether a presenter helps understanding. When one is needed, put the figure, the mouth, the eyes and the source material on separate layers and fix identity and seams; an ordinary explainer can run on material and voiceover alone. Do not treat a whole-body sway as speaking.

Limited volume-driven mouth opening may only be called amplitude-driven; phoneme-level lip sync needs actual alignment evidence. Check mouth closure on pauses, mouth fit, blinking and continuity separately, and keep shot changes on the global time of the whole voiceover. Rebuild dependent tracks after the audio changes; do not carry over the passed status of the old mouth shapes or captions.

## Closing

Per [Sound and rhythm](sound-and-rhythm.md), let score and SFX leave room for the voiceover. Deliver the real voiceover, the necessary captions / timing and edit sources, the tools actually used and the limits of what was verified; without a listening pass, do not write that it is clear, natural or sounds like the person. Record which files are original, denoised reference, generated candidate and final narration, and never let them stand in for one another.
