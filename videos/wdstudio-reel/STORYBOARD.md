---
format: 1080x1920
duration: 50.5s
message: "Your guest books on your site — no platform, no commission"
arc: Quiet hook → The fee → The alternative → The product, calmly → What you keep → Signature
audience: Luxury villa owners and hospitality businesses
mode: collaborative
music: silent luxury minimal piano, sparse, warm, slow, refined
---

## Changes from v1

- User: use booking-system captures (wdstudio.agency/preview/demo-booking-system.html) instead of client villas; no live client is promoted.
- User: take elements and colours from the deck (wdstudio.agency/preview/deck.html); light is the main colour, not dark.
- User: do not use the villa hero image.
- User: "silent luxury" narrative — fewer words, more space, understatement.

## Video direction

One continuous warm-white room (#FBFAF8). Silence and space: slow eases (power2/power3), nothing faster than 0.8s, no bounce. Gold only in hairlines and labels; green only for money kept. Inter 200/600 display pairs. Booking UI appears as a soft white card with a long, faint shadow. Every seam is a slow dissolve.

## Locked

- v2 approved by user; frame 3: no country named, footnote "Platform fees vary by country."

## Frame 1 — Quiet open

- scene: Warm off-white canvas. A thin gold hairline draws left→right. Small tracked label "WD STUDIO". One light line fades in: "A guest finds your house."
- voiceover: ""
- onscreen: "A guest finds your house."
- duration: 5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/01-open.html
- shots: Scene 1 (0–1.2s): empty canvas, hairline draws L→R (scaleX 0→1, 1.2s, power2.inOut) → Scene 2 (1.2–3s): line 'A guest finds your house.' rises 16px + fades in (1.4s, power3.out) → Scene 3 (3–5s): slow global drift up 8px (camera breath).
- handoff_out: hairline x=230 y=480 width=115 opacity=1; line1 x=230 y=520 opacity=1
- type: hook
- persuasion: Understatement
- beat: calm curiosity
- blueprint: titlecard-reveal
- asset_candidates:

narrativeRole: Begin in silence and space — the brand speaks softly.
keyMessage: It starts with your guest.

## Frame 2 — Then pays a platform

- scene: The line stays; a second line in Inter 600 lands beneath: "Then pays a platform to book it."
- voiceover: ""
- onscreen: "Then pays a platform to book it."
- duration: 5s
- transition_in: cut
- status: animated
- src: compositions/frames/02-platform.html
- shots: Scene 1 (0–0.6s): hold frame-1 state exactly → Scene 2 (0.6–1.6s): line1 greys to #8E8B85 → Scene 3 (1.6–3.2s): bold line 'Then pays a platform to book it.' slides up 20px + fades (1.2s) → Scene 4: hold breath.
- handoff_in: hairline x=230 y=480 width=115 opacity=1; line1 x=230 y=520 opacity=1
- type: problem
- persuasion: Negative contrast
- beat: quiet tension
- blueprint: kinetic-type-beats
- asset_candidates:

narrativeRole: Name the intermediary without drama.
keyMessage: Someone stands between you and your guest.

## Frame 3 — 16%

- scene: Large Inter 200 "16%" counts up from 0; small gold label "THE HOST FEE"; right column, small type: "On 50,000 USD a year — 8,000 USD. Every year."; footnote micro-type bottom-left: "Platform fees vary by country."
- voiceover: ""
- onscreen: "16% of every booking. On 50,000 USD a year — 8,000 USD. Every year. *Platform fees vary by country."
- duration: 7s
- transition_in: crossfade
- status: animated
- src: compositions/frames/03-fee.html
- shots: Scene 1 (0–0.8s): gold label fades → Scene 2 (0.6–3s): '16%' counts 0→16 (2.2s, power2.out), slight scale 0.98→1 → Scene 3 (3–5s): right column lines fade in one by one (0.5s apart), '8,000 USD' last → Scene 4 (5–7s): footnote fades in; hold.
- type: problem
- persuasion: Statistical proof
- beat: clarity
- blueprint: dataviz-countup
- asset_candidates:

narrativeRole: Quantify the cost quietly, with the deck's own figures.
keyMessage: The fee is real and recurring.

## Frame 4 — Your guest books on your site

- scene: Deck title treatment: "Your guest books" (200) / "on your site." (600). Above it, gold label "DIRECT BOOKING".
- voiceover: ""
- onscreen: "Your guest books on your site."
- duration: 5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-direct.html
- shots: Scene 1 (0–0.8s): label → Scene 2 (0.6–2s): 'Your guest books' (200) rises → Scene 3 (1.8–3s): 'on your site.' (600) rises → Scene 4 (3.2–5s): sub-line fades; whole block drifts up 6px.
- type: solution
- persuasion: Reframe
- beat: relief
- blueprint: titlecard-reveal
- asset_candidates:

narrativeRole: The turn — the alternative, stated as simply as possible.
keyMessage: Direct booking, on your own website.

## Frame 5 — The booking, calmly

- scene: The booking UI floats on the canvas as a soft card with a slow drift. Dates step: check-in and range resolve (empty → selected crossfade); then crossfades to Extras. Side labels: "Live availability." "Your rates, your seasons." "Extras you define."
- voiceover: ""
- onscreen: "Live availability. Your rates. Your extras."
- duration: 9s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-booking.html
- shots: Scene 1 (0–1.2s): calendar card (empty) rises 40px + fades, soft shadow → Scene 2 (1.5–3.5s): selected-calendar image crossfades over empty (stay picks itself); label 'Live availability.' → Scene 3 (3.5–5.5s): 'Your rates, your seasons.' → Scene 4 (5.5–7s): extras image crossfades in, 'Extras you define.' (600) → Scene 5: card slow drift up 12px across full duration.
- type: proof
- persuasion: Show-don't-tell proof
- beat: ease + control
- blueprint: device-surface-showcase
- asset_candidates: assets/ui-calendar-empty.png — booking calendar, no dates; assets/ui-calendar-selected.png — calendar with stay selected; assets/ui-extras.png — extras step

narrativeRole: Show the product working — elegant, simple, owned.
keyMessage: A complete booking system on your site.

## Frame 6 — What you keep

- scene: The "Your stay" summary card centred; slow push-in to the green note "Booked direct, this stay keeps $530 USD…"; then "$530" lifts out large in green with a gold hairline: "kept, on a single stay."
- voiceover: ""
- onscreen: "$530 kept. On a single stay."
- duration: 7s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-kept.html
- shots: Scene 1 (0–1s): summary card fades in → Scene 2 (1–4s): slow push-in on card (scale 1→1.12, origin bottom-left toward green note) → Scene 3 (3.5–5s): label 'Booked direct' + '$530' counts 0→530 in green → Scene 4 (5–7s): hairline draws, 'kept, on a single stay.' fades.
- type: proof
- persuasion: Feature-to-benefit translation
- beat: satisfaction
- blueprint: zoom-out-workspace-reveal
- asset_candidates: assets/ui-summary.png — "Your stay" summary with $530 kept note

narrativeRole: Make the margin tangible, with the system's own receipt.
keyMessage: Every direct booking keeps the fee in your pocket.

## Frame 7 — Your house. Your rules.

- scene: Centred: "Your house. Your rules." (200) / "No platform." (600).
- voiceover: ""
- duration: 5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/07-rules.html
- type: cta
- persuasion: Identity / status
- beat: quiet confidence
- asset_candidates:

narrativeRole: The thesis, alone on the canvas.
keyMessage: Independence from platforms.

## Frame 8 — Digital identity

- scene: Centred gold hairline, "Digital identity for the world's most beautiful properties.", wdstudio.agency.
- voiceover: ""
- duration: 4s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-identity.html
- type: cta
- persuasion: Authority
- beat: trust
- asset_candidates:

narrativeRole: Who WD Studio is, and where to go.
keyMessage: wdstudio.agency.

## Frame 9 — Logo

- scene: User's animated WD STUDIO logo (1.23s) on white, then holds on its final frame.
- voiceover: ""
- duration: 3.5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/09-logo.html
- type: cta
- persuasion: Signature
- beat: resolve
- asset_candidates: assets/logo-anim.mp4 — user-supplied animated logo; assets/logo-end.png — its last frame

narrativeRole: Close on the brand mark.
keyMessage: WD Studio.
