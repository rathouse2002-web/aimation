# RUN Direction and View Preservation

Read for RUN and for reports of reverse running, diagonal views turning into profiles, or heading drift. Combine with the six-field scaffold and RUN block in action-blocks.md. This file provides targeted additions or replacements, not another full prompt to append.

## Separate the Observed Problems

- Submission failure: a message naming `content[0].text too long` is a length validation failure. Resolve it by counting and shortening the finished prompt.
- Gait failure: a view may retain its heading but appear to run backward. Check the temporal order of stance, push-off and airborne recovery in that view's ground-plane coordinates.
- Orientation failure: a correctly timed run may still change head, torso or pelvis yaw, especially in the four diagonal views. Bind the appearance to source landmarks, then reduce yaw-inducing movement if needed.

In the 2026-10-22 user tests, explicit gait directions and shorter prompts were followed by improved action consistency, while diagonal orientation still drifted. The later fixed-view 2D-rig variant was delivered but had not been generation-tested when this skill was updated. Treat it as a candidate intervention, not a proven fix. The reported 7960-character prompt was explicitly rejected against a 7000-character limit.

## Read the Reference Before Describing the Angle

For views 2 and 8, note the actual visible face area, nose offset, near/far eye visibility when present, and shoulder/chest projection. For views 4 and 6, note the dominant back/head shape, nape, back width and whichever cheek or ear edge is actually visible. Preserve each view's own relationships; do not copy one diagonal's appearance to the other.

Use visible landmarks only. Do not force two visible eyes onto an obscured or nonhuman face, add an ear, or invent precise angular measurements from an approximate drawing. Hair silhouettes, collars, shoulder shapes and asymmetric costume details can serve as anchors. The source view is authoritative even when it is not geometrically exact.

Camera elevation and subject yaw are independent. A 45-degree top-down camera statement does not by itself define or preserve the character's horizontal orientation. Screen headings describe ground-plane locomotion, while reference landmarks describe the appearance to retain.

## Normal RUN View Lock

Use a concise clause such as:

```text
Each view retains its own reference head, chest and pelvis yaw throughout. The four diagonal views preserve the same visible face or back extent and near/far shoulder relationships as their respective source cells. Arms and legs articulate along each view's existing anatomical forward-and-backward axis.
```

Keep torso twist, forward lean and bounce modest when angle fidelity matters. A dramatic running pose may compete with preserving a subtle reference three-quarter angle; describe that tradeoff rather than promising both will be exact.

## Ground-Plane Gait Directions

At a fixed sprite origin, a foot in stance moves from ahead of the pelvis through support beneath it to push-off behind it. The airborne leg recovers forward. These are opposite directions in the character's local ground plane. Lifting a knee or foot also adds image-vertical motion; that lift does not redefine ground-plane forward.

Add this compact table when reverse running has appeared, especially in rear views:

```text
The following directions are ground-plane motion relative to each fixed pelvis; foot lift adds height above that plane.
<Subject 1>: supporting foot moves image up; airborne leg recovers image down.
<Subject 2>: supporting foot moves image upper-right; airborne leg recovers image lower-left.
<Subject 3>: supporting foot moves image right; airborne leg recovers image left.
<Subject 4>: supporting foot moves image lower-right; airborne leg recovers image upper-left.
<Subject 5>: supporting foot moves image down; airborne leg recovers image up.
<Subject 6>: supporting foot moves image lower-left; airborne leg recovers image upper-right.
<Subject 7>: supporting foot moves image left; airborne leg recovers image right.
<Subject 8>: supporting foot moves image upper-left; airborne leg recovers image lower-right.
```

For the rear views, add the reference-appropriate version of:

```text
For <Subject 4>, <Subject 5> and <Subject 6>, the advancing knee reaches away from the viewer along its assigned heading with natural foreshortening. The trailing leg extends toward the viewer before push-off; its heel then rises behind the body as the knee bends. The trailing foot sole may briefly become visible during recovery.
```

Use the corresponding hoof, shoe or other anatomy if the reference differs. Keep chronological forward-running mechanics; an isolated foot's screen motion does not establish gait direction by itself.

## Orientation-Priority Variant for Repeated Diagonal Drift

When the normal view lock has not held the diagonal views, replace it with the block below. Also replace any competing large torso twist, deep lean or dramatic upper-body movement in the existing RUN description. Explain that the upper body will be more restrained. Keep the leg cycle and per-view directions from the previously improved version.

```text
Animate each view like a fixed-view 2D sprite rig. Its head, neck, shoulder girdle, chest and pelvis keep the reference orientation as one stable upper-body unit. Their projected shapes and relative alignment remain consistent while the unit makes a tiny vertical bounce. The torso keeps the reference upright pitch. Express running through articulated legs, compact arm swings and restrained secondary motion.

<Subject 2> retains its own lower-left-facing front three-quarter appearance, including its original facial visibility, nose position and shoulder overlap.
<Subject 8> retains its own lower-right-facing front three-quarter appearance, including its original facial visibility, nose position and shoulder overlap.
<Subject 4> retains its own upper-left-facing rear three-quarter appearance, including its original back-of-head shape, visible back width and visible face-edge contour.
<Subject 6> retains its own upper-right-facing rear three-quarter appearance, including its original back-of-head shape, visible back width and visible face-edge contour.

These four source appearances persist through contact and airborne poses. The shoulder girdle keeps its reference angle while the arms swing independently at the joints.
```

Adapt the face/ear/nose clauses to the actual design. Keep this as one coherent replacement; do not append multiple versions of the same constraints or a growing negative list. Recount the complete assembled prompt, including all six fields, after adding or replacing these clauses.

## Inspect the Result and Change the Input When Needed

Inspect the opening, contact and airborne poses, not only the first frame. Compare head/face visibility, shoulders, chest/back width and pelvis direction separately. Keep reported improvements in cadence, prop retention or gait distinct from unverified angle stability. Ask for a failed frame or short clip when it would locate the remaining drift; do not require it to offer an initial revision.

If the same diagonal drift continues after targeted revision, recommend more explicit input or separate production rather than unlimited prompt expansion:

- Preserve directions that already pass inspection. Crop each failing direction from its original source without mirroring or inventing a replacement view.
- Generate each cropped view separately; for that request, the crop becomes its own reference, and the prompt mapping must be rewritten for the individual view. Do not retain eight Subject definitions in a one-view request.
- If needed, first prepare direction-correct RUN key poses and use the entry point's actually supported keyframe/reference mode. Do not claim a dedicated yaw lock or pose control exists without checking the interface, and do not mix incompatible media modes.
- Match motion phases, scale, origins and palette before recomposing the eight-view sheet. Separate generation can lose synchronization and still needs inspection.

Present this as a recommended workflow change. Respect a user's requirement to keep generating the complete sheet and state the remaining limits. Writing prompts does not authorize paid generation, uploading new media or changing an external workflow.
