# H3 Eight-View Action Blocks

Build complete English prompts only for the actions the user requests. These are authoring blocks, not text to paste verbatim with unresolved placeholders. Replace every placeholder using the actual reference image. Keep distinctive features and props in their definitions instead of repeating long descriptions in every section. Count each finished prompt against the actual entry point's limit.

For RUN, also read [run-direction-lock.md](run-direction-lock.md). Use its normal view lock or its stronger orientation-priority variant as appropriate, then add only the kinematic detail needed to address the observed failure.

## Shared Six-Field Scaffold

```text
subject_definitions:
<Picture 1> is the complete 4-column by 2-row idle sheet and defines each view's design, scale, cell and orientation.
<Subject 1> is the top-row first view, facing image down (front).
<Subject 2> is the top-row second view, facing image lower-left in its reference front three-quarter view.
<Subject 3> is the top-row third view, facing image left in its reference profile.
<Subject 4> is the top-row fourth view, facing image upper-left in its reference rear three-quarter view.
<Subject 5> is the bottom-row first view, facing image up (back).
<Subject 6> is the bottom-row second view, facing image upper-right in its reference rear three-quarter view.
<Subject 7> is the bottom-row third view, facing image right in its reference profile.
<Subject 8> is the bottom-row fourth view, facing image lower-right in its reference front three-quarter view.
All eight are directional views of the same {CHARACTER_AND_FEATURES}, with the reference's approximately 4.5-head proportions. {PROPS}

summary:
[reference generation] All eight views perform {ACTION} in synchronized phase, retaining their respective reference directions and original cells.

retention_analysis:
<Subject 1>, <Subject 2>, <Subject 3>, <Subject 4>, <Subject 5>, <Subject 6>, <Subject 7> and <Subject 8> (all appear in [Shot 1]): fully_preserved - retain each view's identity, costume, proportions, direction, cell and original prop ownership.
<Picture 1>: fully_preserved - retain its complete eight-view layout and distinct source perspectives.

detailed_description:
[Shot 1] Eight full-body views occupy the original 4-column by 2-row arrangement in {STYLE}. Use a static shot at a fixed 45-degree orthographic top-down game angle, flat orthographic projection at a constant zoom level. Use a uniform {BACKGROUND} background, neutral overhead lighting and compact dark contact shadows. Each view retains its reference scale and cell origin. {VIEW_LOCK} {ACTION_BLOCK} All limbs, hair, props and effects remain within their respective cells.

overall_soundscape:
{SOUND} Speech-free.

non_diegetic_music:
N/A
```

`{PROPS}` defines the actual quantity, anatomical hand or attachment, owner and position for every view. A statement such as "Each of the eight views carries exactly one lantern in her anatomical left hand beside her left thigh, eight lanterns total" is suitable only when the image supports it. Use reference-correct handedness and visible geometry. If there are no props, omit the sentence. Preserve asymmetric features by reference rather than horizontal mirroring.

`{VIEW_LOCK}` normally preserves each reference heading and near/far surface visibility. RUN has more specific alternatives in the linked reference. ATTACK, MAGIC and HIT may articulate or recoil without changing heading; DIE must allow pitch into the fall while retaining its assigned ground-plane direction. Do not make the RUN upper-body stability rule universal across all actions.

Local frame defaults and their conditions are in SKILL.md. Online duration is selected in seconds through the actual interface; frame counts are not online API durations.

## Action Blocks

### STAND

`{ACTION}`: `a continuous idle breathing loop`

`{ACTION_BLOCK}`:

```text
All eight hold relaxed idle stances with both feet planted, steady knees, centered pelvises and level heads. A gentle inhale lifts the chest and shoulders slightly, followed by a gentle exhale through the same neutral pose. The breathing cycle repeats throughout the clip. Hair and loose fabric follow subtly, while feet, stance width and cell positions remain fixed. Opening and final frames match the same breathing phase for a seamless loop.
```

`{SOUND}`: `Very faint rhythmic cloth rustle, otherwise quiet.`

Keep breathing periodic throughout, rather than one inhale followed by a long still tail. Avoid adding steps or knee bends to an idle request.

### RUN

`{ACTION}`: `a continuous forward-running loop at stationary sprite origins`

`{ACTION_BLOCK}`:

```text
All eight run in place with moderate strides and brief airborne phases. For each leg, the chronological sequence is forward swing, contact ahead of the pelvis, support beneath the pelvis, rearward push-off, knee flexion with the trailing heel lifted, then forward recovery. The opposite leg performs the complementary half-cycle. Anatomical right-foot contacts occur together across all eight views, followed by synchronized left-foot contacts. Supporting feet travel opposite each subject's own forward ground-plane heading; airborne legs recover along that forward heading. Held props stay controlled and recognizable. Compact arm swings and light secondary motion follow the gait. Running continues throughout, with opening and final frames matching leg, arm, torso-height and prop phases for a seamless loop.
```

`{SOUND}`: `Light even footfalls, soft fabric movement and any faint reference-appropriate prop sounds.`

Use "boots" only if the reference has boots. Ground origins stay fixed while feet articulate; planted feet must not be frozen for the whole RUN. Keep source orientation at the opening pose, without inserting a long idle lead-in. For rear-view reverse running, add the screen-direction table and rear-leg explanation from run-direction-lock.md. For diagonal yaw drift, replace the view-lock clause with its stronger variant instead of appending multiple versions.

### ATTACK

`{ACTION}`: `one {ATTACK_NAME} attack with recovery`

`{ACTION_BLOCK}`:

```text
All eight perform the same attack in synchronized timing. A brief wind-up brings {ATTACK_MEDIUM} into a readable prepared pose while preserving each subject's own heading. At the same moment each executes {ATTACK_DESCRIPTION} toward its own forward direction, with a short clear impact pose. Each then recovers to its own opening stance, preserving handedness, costume silhouette and held props. The action and any requested effect stay within each subject's cell.
```

`{SOUND}`: `A short synchronized strike whoosh and light impact with cloth movement.`

If the attack method is unclear from the user and image, ask briefly rather than inventing a weapon. This is a readable attack with recovery, not an automatic repeated attack unless requested.

### MAGIC

`{ACTION}`: `one character-specific spell with recovery`

`{ACTION_BLOCK}`:

```text
All eight perform one synchronized spell using {MAGIC_MEDIUM}. Each begins {MAGIC_CHARGE}, then completes {MAGIC_RELEASE} along its own forward heading, producing {MAGIC_EFFECT} briefly within its own cell. The effect fades and each returns to its opening stance, preserving direction, outfit, original equipment and prop ownership.
```

`{SOUND}`: `A soft rising magical hum, brief release chime and faint fading particles.`

Choose the medium from visible hands, equipment or character features. If none suggests magic, use a modest hand gesture instead of new permanent equipment. Keep effects compact enough to preserve directional readability.

### DIE

`{ACTION}`: `one defeat and fall to a final still pose`

`{ACTION_BLOCK}`:

```text
All eight begin in their reference standing stances. They react to defeat together, lose balance, descend and fall forward once onto their own ground planes in one continuous movement. Each body settles into a stable prone pose inside its cell, with head and upper torso extending along that view's assigned ground-plane forward direction and hips and feet extending toward the opposite direction. Preserve the original anatomy and recognizable outfit. Each originally held independent prop remains identifiable beside its own character within the same cell. The eight final poses remain still through the final frame.
```

`{SOUND}`: `Synchronized soft impacts, brief equipment and cloth rustle, then quiet.`

Remove the independent-prop sentence if inapplicable. This is one continuous fall with a static ending. The word "forward" means each view's own heading; a fall changes body pitch while retaining its directional identity.

### HIT

`{ACTION}`: `one hit reaction with recovery`

`{ACTION_BLOCK}`:

```text
All eight receive an impact from their own forward directions at the same moment. They recoil briefly opposite their respective headings, the upper bodies flinch, and a corresponding arm reacts while a foot stabilizes each character within its cell. The reaction peaks together, then all eight return to their opening stances with original direction and equipment intact.
```

`{SOUND}`: `A brief synchronized impact thump and cloth rustle.`

Keep presentation effects such as screen shake and damage UI outside the generated sprite footage unless explicitly requested.

## Export Reminder

Key the background while protecting similar-colored foreground accessories; use edge-connected background masks or suitable foreground masks when needed. Quantize all frames and directions together, then downsample with nearest-neighbor sampling. Extract loop frames by motion phase rather than uniform time intervals; keep only one copy of a duplicate boundary pose. Preserve each exported cell origin and ground anchor. Select readable key poses for one-shot actions.

For local ComfyUI MiniMaxH3ReferenceToVideo troubleshooting, check the actual node schema; `ref_images.ref_image_0` is a known reference binding in the workflow used to develop this skill, not a universal web/API field. Prompt format, orthographic geometry, view synchronization and detail retention still require output inspection.
