# Asset stage notes for this shot

Applies to shot / version: fill in the existing scene ID and the current plan version. A simple task can skip this sheet and write the existing direction or shot notes directly.

## Action and grounds

- The change the audience has to see; the real grounds and what must stay unchanged
- Existing assets / editable objects; the complete units that have to be prepared and the processing route
- Trigger → main action → response → settle → handoff; link the existing element / beat / audio_cue IDs

## Parts and coordinates

| Existing asset / element ID | Part job and grouping | Source file / version and derived files | Coordinate space / unit / working size | Crop box / local origin / anchor | Scene transform and display shot |
| --- | --- | --- | --- | --- | --- |
| Fill in per actual | The complete unit; do not split to the finest level by default | Paths follow the project conventions; record a hash where needed | State plainly: original, working source, local, scene or screen | Be explicit about which space it is relative to | Reference it along the existing plan |

## Occlusion and range of motion

| Part | Depth order / linked masks | Area revealed when it moves away, and the grounds | Checked range of move / scale-up / rotation | Content protection and fallback |
| --- | --- | --- | --- | --- |
| Fill in per actual | Separate true occlusion from estimated depth | Real background, painted-in fill or unknown area | Write unchecked if it was not checked | Keep the necessary text, state, identity and data |

## Verification and reuse

- Restoring the source state: the range actually inspected, the differences and how they were handled
- Motion extremes / seams: time, sample-clip version, observation and problem
- Sound / annotations: the actual linkage and re-check; record explicitly what was not heard or not seen
- After changing the source, crop, mask, type, timing or aspect ratio, which shots and caches have to be updated

See [asset performance and routing](../references/asset-motion-direction.md). This is an optional design note, not a new JSON structure, an automatic execution track or a verified state.
