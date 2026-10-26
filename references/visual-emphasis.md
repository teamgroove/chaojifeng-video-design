# Let the viewer see what matters right now

Used for emphasis on real screenshots, screen recordings, charts, and feature and result evidence. Ask first where the viewer should look at this moment, what they should know or what they should do, then choose box, label, leader line, focus or local zoom. Not every shot needs a frame; image stories, brand imagery and music performance with no operational teaching point can do without entirely.

This method is distilled from screenshot-annotator's target completeness, text protection, action labels and independent review; the coordinate transforms, timing and handoff on the video side are this Skill's adaptation. Do not require the other Skill to be installed, and do not mistake a static annotation script for a video tracker.

## Choose the emphasis by the expressive task

| Viewer task | Available expressions | What to check |
| --- | --- | --- |
| Find the current entry point | Full control box + short action label, leader line where needed | Include the necessary icon, text and container together; exclude the neighbouring entry point |
| See the feature feedback clearly | Initial state → trigger → result, emphasis moving with the information | Do not let a label conjure a state the product never entered; leave reading time on the result |
| Understand a dense interface | Keep the global context → zoom in or cut to a standalone detail → return | The focused area traces back to the original interface; necessary background is not cropped away |
| Understand a relationship or key data | A few highlights, leader lines, naming and same-scale comparison | Numbers, units, conditions and legends stay readable; lines do not cross key content |
| Tell steps or options apart | Numbers for real steps, letters for mutually exclusive entry points | A single emphasis needs no superfluous 1; a plain information comparison needs no forced A/B |

A label states the action, the visible result or an explanation. For example "Select a task", "Check the run result"; when the picture already shows the action, a short phrase on the payoff also works. Do not paste internal object names or production page numbers, and do not stuff a paragraph of business explanation into a label. Annotation, voiceover and subtitles carry the same point, so the viewer is never reading three pieces of new information at once.

## Accurate targets, labels that get out of the way

The target boundary is a fact about the content. Define must_include and must_exclude and treat it as one complete visual unit; move the label to solve occlusion, never move the real target to suit the layout. A menu includes its icon and text, a download does not bring save-to-cloud along with it, a result row does not bring the table header or other files.

Protect interface text, headings, asterisks, hints and key values, and also the finished film's subtitles, the brand area and any legend that has to stay. OCR helps locate, but you must catch what it misses; without text recognition or observation, keep the state unverified. Labels, numbering and leader lines do not sit on text, box strokes do not cut through letterforms; a box may enclose text, and a label placed in empty space inside the box still has to be checked.

Look first for safe empty space near the target and add a leader line where needed; bottom right is only a candidate. When it is still crowded, shorten the copy, offset the emphasis in time, zoom in or split the shot. Do not pile labels into far-off empty space, and do not shrink them below readability at the actual viewing size. Usually hold one primary focus at a time; several simultaneous emphases need a clear comparative or relational purpose.

Style follows the brand and the current picture; box, label and sound effect share one temperament. The screenshot Skill's orange, its 100px grid and its 44px font size are all configurable starting points, not uniform parameters for video. Keep the functional box and its connection clear; do not cover the evidence with glare, continuous flashing or giant type.

## Keep attribution across time and space

Guide attention first, leave a reading/understanding window, then exit or hand off to the next point. An action trigger can share a beat with a short sound effect, but not every annotation has to make a sound. Avoid continuous text reflow during camera moves; either finish the focus and then read, or keep the label fixed on screen and let a leader line connect the target that has moved.

Keep the original asset and a copy suitable for showing; never redraw a real screenshot into a feature interface that has not been verified. Where redacted privacy is involved, annotations, zooms, frame grabs, contact sheets and later versions all inherit the same verified copy and distribution boundary, and must not go back to the original to expose it again. A watermark does not disappear because the clip is a promo.

Record source-image coordinates, finished-film coordinates and the actual viewing size separately. Recompute the mapping after a crop; box and screenshot share one transform. Fixed labels and subtitles use finished-film screen coordinates, and the leader line points at the transformed target. When the target leaves the screen, is occluded or the layout changes, shorten the current track and re-measure the new segment, or hide it and re-lay it out; do not carry over the old position and do not guess a tracking result.

## An editable annotation track

A simple shot can write its box, text and focus straight into the existing plan's elements/motions. Where there is screenshot cropping, follow-the-camera motion or annotation in several passes, generate a separate `annotation-track.json` inside the project from `templates/annotation-track.json` and keep the stable IDs; it is a geometry/time contract, not a renderer. Not every video has to ship an extra file.

```text
python3 SKILL_ROOT/scripts/catalog.py --kind expression get visual.target-callout
python3 SKILL_ROOT/scripts/validate_annotation_track.py /project/annotation-track.json --plan /project/plan.json --output /project/qa/annotation-check.json
```

The checker currently works to these conventions; the render pipeline must adopt the same mapping, or output resolved geometry that matches reality, before checking:

- rect_format=xyxy. The width/height of sources, crop_rect, target_rect, must_include/exclude and the source protected regions are all in source-image pixels; a rectangle is `[left,top,right,bottom]`, never mixed with a width/height format or with browser preview coordinates.
- sources.source_to_screen supports only a positive uniform scale and translate_x/y, with explicit linear keyframes spanning the whole film. The mapping is `screen_x=source_x*scale+translate_x`, and the same for y. A crop does not re-base automatically; if the crop's left edge is c and you want it at frame position x, set translate_x to x-c*scale. Do not subtract the crop and then subtract the translation a second time.
- target_geometry=static_source, meaning the target itself is fixed within that source image. The box is projected through the source transform. This suits a static screenshot that the camera pans and scales over; in a screen recording, control reflow, scrolling or a changing popover must be split into tracks whose targets were measured again. Automatic detection, target tracking, rotation, perspective, non-linear easing and complex masks are outside this checker's scope.
- The start/end of tracks, reading_window and all keyframe times are absolute seconds of the whole film; visible intervals are left-closed, right-open. A track must not run past the point where its target still holds. label.space=screen means label keyframes use finished-film pixels and must cover the track interval; label.rect should be the bounding box after the actual text has been laid out — the script does no font shaping.
- A source is visible for the whole film by default; declare the actual interval with visible_start/visible_end. An annotation must not outlast the asset's visible time. The protected regions of every visible asset take part in avoidance even when that asset carries no annotation at this moment; protected regions that are cropped out of view do not.
- semantic_role is single/sequence/alternative. single needs no numbering; the other two get group_id/index and the matching marker, numbered consecutively within the group, and real steps do not contradict the time order. marker.rect is a conservative bounding box in finished-film pixels, not the same thing as a round glyph mask.
- target_contract declares the complete unit; source.protected_regions and screen_protected_regions declare protected regions, optionally with start/end. source.text_regions_status=reviewed records only observation that was actually carried out — it is not a placeholder value for getting past automated QA.
- connector.enabled states explicitly whether there is a leader line; max_gap_px is the label-to-target distance this film accepts. When enabled, give stroke_width_px; the leader endpoints are computed from the current target and the label rectangle, and complex polylines need separate verification in the pipeline. readability.view_width_px and minimum_label_px are chosen for the actual use and serve to estimate scaled font size; they are not general reading thresholds.
- You may add path/sha256 to a source and verify the asset inside the project; `--plan` separately checks project_id, aspect ratio, duration and each track's scene_id/element_id references. Track paths and hashes belong in the delivery source manifest; an old check does not vouch for a revised version.

## Checks and actually watching

The script checks target include/exclude, crop and canvas bounds, collisions of label/marker/box stroke/leader line with the declared protected regions, numbering semantics, subtitle conflicts, mapping and clock. The report keeps the input hashes and the resolved key-moment positions and supports minimal rework by ID. By default it adds keyframes every 0.1 s and checks visible boundaries and reading boundaries, with a sampling budget; over budget you split the range or change the checked scope explicitly, never let checks drop out silently.

What gets checked is the declared linear geometry and protected regions. A conservative rectangle can report rounded-corner whitespace as a collision, and a missing protected region can let one through; no collision at the sampled times does not mean zero collisions on every frame, and an estimated font size is not proof that the glyphs read. The tool has no OCR, no auto-tracking, no video rendering and no visual understanding; the best success state is awaiting_visual_review, never passed.

Actually look at the whole shot, the target area, keyframe contact sheets and continuous segments, covering the densest moment, the camera extremes, annotation entry and exit, subtitle changes and transition boundaries; at the final viewing size verify target completeness, attribution, letterforms, the voiceover/text relationship and the dwell. A contact sheet does not replace continuous playback. If it was not watched, visual/playback stays not_run; where human sign-off is needed, record reviewer, time, scope and evidence separately — a script does not produce a pass verdict.

When composing, reuse `camera.focus-frame`, `text.semantic-emphasis`, `text.read-then-move` and highlight/trace/reveal/exit/hold; only `visual.target-callout` is new — do not rebuild a second set of effects for the same focus. Try the hardest follow and the seams first, then integrate into the existing project.
