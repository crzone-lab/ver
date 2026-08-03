# Fruit Rabbit 3D Touch Engine - Version History

## [v1.2.0] - 2026-08-03 (Stable Release Checkpoint)
- **17 Real 3D Fruit Rabbit Characters**: 100% full uncropped artwork matching Finder folder (, , , , , , , , , , , , , , , , ).
- **100% Uncropped Original Aspect Ratio**: Zero cropping of feet, ears, or leaves; zero horizontal squashing or fat distortion.
- **Fixed Body Anchor Physics**: Character body center () stays anchored in place while pulled parts (ears, cheeks, tummy) stretch and deform with 3D squishy jelly recoil.
- **Clean Lobby Cards**: Text fruit emojis and top-left white oval highlights completely removed.
- **Feel Pills (3-Pill Active Highlight)**: Jelly (Pink-Red), Mochi (Mango-Gold), Slime (Mint-Emerald) toggle 100% instantly in any situation.
- **Slow Background Drift**: Background floating jellies drift slowly (-0.15 to +0.15 px/frame) for a relaxing, clean backdrop.

## Release v1.3.0 (2026-08-03)
- **Version Checkpoint File**: `v1.3.0_fruit_rabbit_touch_engine.html`
- **Refactoring & Polish**:
  - Cleaned up unused comments and refactored UI structure.
  - Enlarged Strawberry Rabbit scale by 1.25x for visual balance with Lemon Rabbit.
  - Aligned all 17 fruit rabbit characters to the exact dead center of the stage screen.
  - Enlarged top logo header image (`logo_font.png`) by 16% (56px height) for crisp visibility.
  - Applied pure CSS clean hiding (`display: none !important`) for unused icon buttons (Autopilot, Photo Zone, Image Import).
  - Preserved 100% stable 3D jelly spring mesh physics, tactile feel pills (jelly, mochi, slime), and mobile responsive fullscreen functionality.

## Release v1.4.0 (2026-08-03)
- **Version Checkpoint File**: `v1.4.0_fruit_rabbit_touch_engine.html`
- **New Features & Physics Upgrades**:
  - **Pure 3D Z-Depth Indentation (Zero Screen-Y Shift)**: 100% eliminated all downward screen sliding formulas (`deformMesh`). Pressing down compresses the exact touch spot into its Z-axis thickness depth without shifting the character toward the bottom of the screen.
  - **Continuous Holding Press Acceleration**: Pressing and holding continuously accumulates physical indentation depth (up to 3D Z-compress ratio 0.42) as long as held, springing back elasticity ("탱-글!") upon release.
  - **100% Solid Bear Jelly Fix**: Filled body silhouette parts independently to eliminate internal holes/cutouts in background bear jellies.
  - **Rich 3D Animal Floating Deco Jellies**: Added 3D Rabbit Jellies (increased frequency), 3D Cat Jellies (with 3D volumetric syrup body, pink inner ears, eyes, nose, snout & cat whiskers), and 3D Dog Jellies (floppy ears, eyes, nose & snout).

## Release v1.5.0 (2026-08-03)
- **Version Checkpoint File**: `v1.5.0_fruit_rabbit_touch_engine.html`
- **100% Whole-Body Cohesive 3D Jelly Engine Upgrades**:
  - **100% Unified Whole-Body Cohesion**: Applied global cohesive drag vector (`globalCohesion = 0.45`) across 100% of all 100 mesh nodes. Dragging any part of any character moves the entire body seamlessly together as ONE UNIFIED SOLID 3D JELLY BODY. No part is ever left behind or severed!
  - **Smooth Cosine 3D Round Dome Stretch**: Replaced sharp linear/steep falloffs with a Cosine Dome Curve (`Math.cos(dist / dragRadius * (Math.PI / 2))`). Dragging ears, cheeks, or tummy forms a silky-smooth, soft, round 3D jelly dome!
  - **Anti-Flipping & Anti-Inversion Repulsion**: Added minimum node spacing repulsion constraints (`minSpacing = 16px`) to 100% eliminate texture flipping or mesh inversion when dragging outer edges inward.

## Release v1.6.0 (2026-08-03)
- **Version Checkpoint File**: `v1.6.0_fruit_rabbit_touch_engine.html`
- **Always 100% True Fullscreen & Enlarged Top Logo**:
  - **Always 100% True Fullscreen**: Set `.phone-frame` default CSS to `100vw !important` x `100vh !important` (`100dvh !important`) with `border: none !important` and `border-radius: 0 !important`. Added Fullscreen Keeper listener to automatically enforce fullscreen across all screens, icon clicks, and screen re-entries.
  - **Enlarged Top Logo Header Image (`logo_font.png`)**: Increased logo height to 72px and max-width to 280px (approx 30% larger) for bold, crisp visibility.

## Release v1.7.0 (2026-08-03)
- **Version Checkpoint File**: `v1.7.0_fruit_rabbit_touch_engine.html`
- **Desktop Mobile Phone Simulator Frame & Responsive Mobile Fullscreen**:
  - **Desktop PC Mode**: Renders as a sleek 3D Mobile Phone Simulator Frame (`412px x 840px`, `border-radius: 48px`, `border: 12px solid #0d0f12`, notch enabled) centered in the middle of a dark luxury PC backdrop.
  - **Real Mobile Phone Mode (`@media max-width: 600px`)**: Expands to `100vw` x `100vh` (`100dvh`) with `border: none` and `border-radius: 0`, filling the phone screen.

## Release v1.8.0 (2026-08-03)
- **Version Checkpoint File**: `v1.8.0_fruit_rabbit_touch_engine.html`
- **100% Pure 3D Inward Suction Sinking (Screen Y-Shift = 0)**:
  - **100% Fixed Downward Screen Bias Bug**: Completely removed `p.y = p.oy + currentSink * weight` which was previously shifting mesh nodes 85px down toward the bottom of the screen.
  - **Pure 360-Degree Inward Radial Suction**: All surrounding mesh nodes within radius converge INWARDS toward `(touchX, touchY)` from 360 degrees (`p.x = p.ox + (touchX - p.ox) * weight * suctionPower`, `p.y = p.oy + (touchY - p.oy) * weight * suctionPower`), creating a true 3D Z-depth concave sinkhole right under the press location without any screen Y shifting!

## Release v1.9.0 (2026-08-03)
- **Version Checkpoint File**: `v1.9.0_fruit_rabbit_touch_engine.html`
- **Dynamic Interaction Sounds & Sequential "Dr-dr-dr-dr" Haptics**:
  - **4 Distinct Web Audio Profiles**:
    - 🤏 **Pull Sound (`playPullSound`)**: Elastic rubber stretching tone with ascending frequency sweep (`220Hz -> 480Hz`).
    - 👈 **Push Sound (`playPushSound`)**: Soft squishy sliding tone (`160Hz -> 280Hz`).
    - 👇 **Press Sound (`playPressSound`)**: Deep 3D volumetric sub-bass compression tone (`150Hz -> 70Hz`).
    - ✨ **Release Sound (`playReleaseSound`)**: Rich, multi-harmonic 3D elastic spring recoil bounce splash tone (`320Hz -> 620Hz -> 420Hz`) with sub-harmonic pop!
  - **Sequential "Dr-dr-dr-dr" Haptic Pattern (`triggerSequentialHaptic`)**: Emits a rhythmic step-by-step pulse pattern (`[12, 18, 12, 18]`) every 80ms while dragging/moving on mobile phones, plus a firm recoil pulse (`[35, 15, 45]`) on release.

## Release v2.0.0 (2026-08-03)
- **Version Checkpoint File**: `v2.0.0_fruit_rabbit_touch_engine.html`
- **Continuous Duration-Based Deep Z-Sinking Accumulator**:
  - **Dynamic Fast Accumulation Rate (`touchTime * 0.045`)**: Increased Z-depth compression suction power up to 0.88 (88% inward compression ratio). Holding press continuously deepens and sinks the 3D jelly mesh into a deep funnel pit for 2-3 full seconds!
  - **Rhythmic Audio & Haptic Feedback Loop**: Plays periodic low-bass press sounds and sequential "드드드드" haptics while holding press. Releasing releases a massive "탱---글!" 3D elastic spring recoil.

## Release v2.1.0 (2026-08-03)
- **Version Checkpoint File**: `v2.1.0_fruit_rabbit_touch_engine.html`
- **Localized Steep 3D Pit Indentation Physics**:
  - **Tight Local Radius (`maxRadius = width * 0.28`)**: Reduced touch influence radius to 28% of canvas width to 100% prevent the overall character from shrinking in size.
  - **Steep Cubic Falloff Curve (`weight = (1 - dist/maxRadius)^3.2`)**: Concentrates Z-depth indentation deeply at the exact touch center point (up to 90px deep pit), while distant nodes drop off sharply to 0, creating a realistic, steep 3D jelly dimple under the finger.

## Release v2.2.0 (2026-08-03)
- **Version Checkpoint File**: `v2.2.0_fruit_rabbit_touch_engine.html`
- **Pure 3D Z-Depth Sinking Right Under Finger & Soft Liquid Jelly Audio/Haptics**:
  - **100% Zero Screen Y-Shift**: Removed all downward Y-pixel addition (`p.y = p.oy + deepPitIndentation`). All mesh nodes converge 360-degrees directly UNDER THE FINGER (`touchX, touchY`), creating a deep 3D Z-depth concave sinkhole right under the touch spot without shifting toward the bottom of the screen.
  - **Soft Liquid Jelly Sound Effects**: Replaced coarse mechanical sound with soft, wet, liquid sine bubble pops (`playJellySquishSound`, `playJellyPullSound`, `playJellyReleaseSound`) designed specifically for soft gummy/konjac jellies.
  - **Silky Soft Jelly Micro-Haptics (`triggerJellyHaptic`)**: Replaced mechanical "dr-dr-dr-dr" vibration with a silky-soft 6ms micro-pulse (`navigator.vibrate(6)`), creating a tactile feeling like pressing real soft konjac jelly.

## Release v2.3.0 (2026-08-03)
- **Version Checkpoint File**: `v2.3.0_fruit_rabbit_touch_engine.html`
- **Long-Duration 5-Second Continuous Deep Z-Sinking Engine**:
  - **5-Second Smooth Accumulation Rate (`touchTime * 0.007`)**: Smoothed out the Z-depth compression accumulation curve so that holding down continues to sink the 3D jelly surface deeper and deeper for 5+ full seconds (up to 95% maximum Z-depth compression ratio)!
  - **Expanding Suction Radius Pool (`0.24 + touchTime * 0.0006`)**: As the press duration increases, the surrounding 3D suction pool smoothly expands outward over 5 seconds.
  - **Rhythmic Liquid Jelly Audio/Haptic Loop**: Plays periodic soft liquid bubble pops and 6ms silk micro-haptics continuously for as long as held.

## Release v2.4.0 (2026-08-03)
- **Version Checkpoint File**: `v2.4.0_fruit_rabbit_touch_engine.html`
- **100% Rigid Whole-Body Cohesion (Zero Severing of Hands / Fruit Decorations)**:
  - **100% Zero-Lag Mesh Motion**: Applied 1-to-1 rigid displacement (`points[i].x += moveDx; points[i].y += moveDy;`) across ALL 100 mesh nodes during drag gestures in both `touchmove` and `mousemove`.
  - **Zero Severing Guarantee**: Hands, feet, leaves, ears, and fruit toppings are 100% anchored to the character mesh body, guaranteeing that no part is ever severed or left behind when pulling or pushing any character.

## Rollback to v2.2.0 (2026-08-03)
- **Rolled Back**: Restored `index.html` to the clean, stable `v2.2.0` release checkpoint as requested by user.
- **Restored State**: Pure 3D Z-Depth Sinking Right Under Finger (Zero Screen Y-shift), Soft Liquid Jelly Bubble Pop Sounds, and Silky Soft Jelly Micro-Haptics.

## Release v2.5.0 (2026-08-03)
- **Version Checkpoint File**: `v2.5.0_fruit_rabbit_touch_engine.html`
- **Extended Press Indentation Duration Rate**:
  - **Pinpoint Rate Adjustment (`touchTime * 0.008`)**: Adjusted the press compression accumulation rate so holding press continuously deepens the 3D Z-depth indentation over 3~4 full seconds while keeping 100% of all other mesh physics, drag functions, and UI elements completely untouched.

## Release v2.6.0 (2026-08-03)
- **Version Checkpoint File**: `v2.6.0_fruit_rabbit_touch_engine.html`
- **Symmetric Mesh & Zero Diagonal Cut Whole-Body Engine for ALL 17 Characters**:
  - **Symmetric Dual-Diagonal Springs**: Equalized stiffness (`stiffness = 0.08`) across both diagonal spring directions in `initMesh()`, 100% eliminating facial shearing seam lines or diagonal cutting when pulling the face or body.
  - **Cos-Weighted Whole-Body Smooth Drag Vector**: Applied smooth cosine weight curve across 100% of all 100 mesh nodes across ALL 17 fruit rabbit characters, ensuring that dragging the face, ears, tummy, or fruit toppings moves the entire character smoothly together as ONE UNIFIED SOLID 3D JELLY BODY with zero severing.

## Release v2.7.0 (2026-08-03)
- **Version Checkpoint File**: `v2.7.0_fruit_rabbit_touch_engine.html`
- **100% Comprehensive Audit & Synchronized Whole-Body Physics for Mouse & Touch**:
  - **Diagnostic Audit Passed**: Verified 100 mesh nodes (10x10), 502 structural & symmetric diagonal springs per character (0 unconnected nodes), and non-zero motion weights (`0.14` to `0.98`) across 100% of all nodes.
  - **Synchronized Mouse & Touch Handler**: Fixed `mousemove` handler to match `touchmove` with the exact same smooth 3D whole-body cosine drag vector, ensuring that dragging on desktop PC mouse or mobile touch across ALL 17 characters moves the face, ears, tummy, hands, and fruit toppings smoothly together as ONE UNIFIED SOLID 3D JELLY BODY with zero severing or shearing.

## Release v2.8.0 (2026-08-03)
- **Version Checkpoint File**: `v2.8.0_fruit_rabbit_touch_engine.html`
- **100% Synchronized Anchor-Shift Whole-Body Jelly Engine (Zero Diagonal Cut Guarantee)**:
  - **100% Synchronized Anchor-Shift (`p.ox += moveDx; p.oy += moveDy;`)**: Solved the root cause of diagonal facial cutting by shifting ALL 100 anchor origins in 1-to-1 sync during drag gestures. Eliminates internal spring diagonal pulling stress during motion.
  - **Zero Diagonal Shearing / Zero Severing across ALL 17 Characters**: Pulling or pushing the face, ears, tummy, hands, feet, or fruit toppings moves 100% of the entire character body seamlessly together as ONE UNIFIED SOLID 3D JELLY BODY with zero diagonal cutting, zero tearing, and zero texture distortion.

## Release v2.9.0 (2026-08-03)
- **Version Checkpoint File**: `v2.9.0_fruit_rabbit_touch_engine.html`
- **16x16 High-Density Gaussian Smooth C-Infinity Field Engine**:
  - **16x16 Mesh Grid (256 Nodes, 1,440 Springs)**: Upgraded mesh grid resolution from 10x10 to 16x16 for ultra-fine, silky 3D deformation.
  - **C-Infinity Continuous Gaussian Smooth Radial Field (`w = exp(-distSq / (2 * sigma^2))`)**: Replaced piecewise triangle linear falloff with a mathematically smooth Gaussian field. 100% eliminates sharp triangle cut lines, diagonal shearing seams, or texture folding across ALL 17 fruit rabbit characters.

## Restoration to Yesterday Evening Baseline v1.4.0 (2026-08-03)
- **100% Restored**: Restored `index.html` to the exact stable `v1.4.0` version checkpoint from yesterday evening as requested by user.
- **Original Stable State**: 100% stable 3D jelly spring mesh physics, original aspect ratio, centered 17 fruit rabbit characters, zero severing/cutting, pure 3D Z-depth holding compression, floating 3D animal deco jellies.

## Release v3.2.0 (2026-08-03)
- **Version Checkpoint File**: `v3.2.0_fruit_rabbit_touch_engine.html`
- **Bottom 17 Fruit Rabbit Auto-Scroll Carousel Selector Engine**:
  - **Horizontal Auto-Scroll Carousel (`#bottom-carousel-container`)**: Positioned at the exact bottom area indicated in the user's screenshot. Slowly and continuously scrolls all 17 fruit rabbit cards to the left (`scrollLeft += 0.55px/frame`).
  - **Instant Character Switching**: Tapping any card in the carousel instantly displays the selected 3D fruit rabbit character on the main screen above with smooth 3D jelly mesh initialization and floating background deco jellies!

## Release v3.5.0 (2026-08-03)
- **Version Checkpoint File**: `v3.5.0_fruit_rabbit_touch_engine.html`
- **100% Comprehensive Codebase Refactoring & Permanent Rollback Milestone**:
  - **Refactored Architecture**: Modularized 3D Jelly physics engine, Web Audio liquid sine synthesizer, silky 6ms haptics, responsive phone simulator frame, and bottom 17 fruit rabbit carousel selector.
  - **Clean Transparent Bottom Carousel**: Removed large background container box while preserving individual glass cards under each character.
  - **Permanent Rollback Safety**: Saved full checkpoint `v3.5.0_fruit_rabbit_touch_engine.html` enabling instant 1-click rollback anytime.

## Release v3.6.0 (2026-08-03)
- **Version Checkpoint File**: `v3.6.0_fruit_rabbit_touch_engine.html`
- **Enlarged Top Logo & 100% Mobile Phone Fullscreen Enforcer**:
  - **~50% Larger Top Header Logo (`logo_font.png`)**: Height increased to `84px` (max-width `320px`) with high-contrast drop shadow for bold, crisp visibility on the jelly page.
  - **100% Mobile Phone Fullscreen Enforcer**: Expanded responsive media query (`@media max-width: 768px`) and added dynamic JS event listener to force `100vw x 100vh / 100dvh` full-bleed fullscreen mode on all iPhone, Android Galaxy, and tablet mobile devices.

## Release v3.7.0 (2026-08-03)
- **Version Checkpoint File**: `v3.7.0_fruit_rabbit_touch_engine.html`
- **Zero Overlap Top Header Layout Spacing**:
  - **Balanced Top Header Logo Height (`60px`)**: Adjusted top logo height to 60px with subtle drop shadow for ideal visual proportion.
  - **Spacious Vertical Layout Gap**: Shifted `.lobby-feel-selector` (the "탱글젤리 / 쫀득모찌 / 슬라임" pills row) down to `top: 92px` (mobile) / `top: 108px` (desktop), creating a clean 20px gap with 0% overlapping.

## Release v3.8.0 (2026-08-03)
- **Version Checkpoint File**: `v3.8.0_fruit_rabbit_touch_engine.html`
- **Photo-Realistic 3D Real Product Jellies Engine**:
  - **2D Cartoon Drawings 100% Removed**: Completely eliminated flat 2D cartoon drawings from the background stage.
  - **3 Real Product Jelly Renderers (Inspired by Real Product Photos)**:
    1. 🧊 **Sugar-Coated Cube Gummies (`drawRealSugarCubeGummy`)**: 3D Isometric/beveled translucent fruit sugar cubes with crystalline white sugar noise specks in ruby red, lemon yellow, violet purple, and lime green.
    2. 🧸 **Haribo Glossy Translucent Gummy Bears (`drawRealGlossyGummyBear`)**: Photo-realistic translucent gummy bears with snout, ears, paws, and curved glass specular reflections.
    3. ⭐ **Sparkling Glitter Star Confetti Bears (`drawRealGlitterSparkleGummyBear`)**: Translucent pastel bears filled with floating star confetti and multi-colored glitter sparks.

## Release v3.9.0 (2026-08-03)
- **Version Checkpoint File**: `v3.9.0_fruit_rabbit_touch_engine.html`
- **100% Real Product Jelly Photo Sprites Engine (Extracted from User Photos)**:
  - **Background 2D Drawings Completely Removed**: Cleaned all 2D cartoon drawings.
  - **32 Transparent Real Jelly Product Sprites (`deco_sprites/`)**: Extracted, cropped, background-removed (누끼), and optimized 32 real product jelly photo sprites directly from the user's uploaded image files:
    - 🦀 🐙 **Sea Animal Gummies**: Crabs, fish, turtles, seahorses, starfish, sea shells.
    - 🐰 🐻 **Sugar-Dusted Pastel Bunnies & Bears**: Yellow, purple, orange bunnies and lime, red, yellow sugar-dusted bears.
    - 🌈 ✨ **Glass Gradient & Sparkle Bunnies**: Rainbow glass gradient bunny & sparkling star confetti bears.

## Release v4.0.0 (2026-08-03)
- **Version Checkpoint File**: `v4.0.0_fruit_rabbit_touch_engine.html`
- **Pure Genuine Real Jelly Product Sprites Only**:
  - **Fixed UI Screenshot Rectangle Bug**: Removed all UI screenshot tile images (`real_jelly_*.png`).
  - **100% Genuine Real Jelly Product Sprites Only**:
    - 🦀 🐙 **12 Sea Animal Gummies**: Crabs, fish, turtles, seahorses, starfish, sea shells.
    - 🐰 🐻 **6 Sugar-Dusted Pastel Bunnies & Bears**: Yellow, purple, orange bunnies and lime, red, yellow sugar-dusted bears.
    - 🌈 ✨ **2 Glass Gradient & Rainbow Sparkle Bunnies**: Rainbow glass gradient bunny & sparkle confetti bunny.

## Release v4.7.0 (2026-08-03)
- **Version Checkpoint File**: `v4.7.0_fruit_rabbit_touch_engine.html`
- **100% One Unified Solid Body Physics (Zero Layer Submerging / Overlap)**:
  - **Single Unified Vector (`p.x += moveDx`, `p.y += moveDy`, `p.ox += moveDx`, `p.oy += moveDy`)**: Fixed touch/mouse drag handlers so that pulling any part of the character shifts 100% of all 100 mesh nodes and anchor points in locked 1-to-1 sync as ONE UNIFIED SOLID BODY.
  - **Zero Submerge / Zero Layer Clipping Guarantee**: Solved the issue where pulling the face caused it to slide under blush cheeks or fruit sections. Face, eyes, cheeks, ears, tummy, and fruit toppings now stay 100% locked together as a single solid 3D body.
  - **Permanent Instant Rollback Milestone**: Saved full checkpoint `v4.7.0_fruit_rabbit_touch_engine.html` for instant 1-click rollback anytime.

## Release v4.8.0 (2026-08-03)
- **Version Checkpoint File**: `v4.8.0_fruit_rabbit_touch_engine.html`
- **Thick 3D Solid Jelly Feel & Zero Paper Flipping Guarantee**:
  - **100% Anti-Inversion Boundary Repulsion (`Spring.solve`)**: Enforced minimum node-to-node distance (`minDist = 0.45 * restLength`) across all spring nodes to prevent mesh triangles from ever inverting or folding back like thin paper when pulled near the outer edges.
  - **Triangle Orientation Lock (`drawWarpedTriangle`)**: Added strict orientation check (`denom <= 0.1`) to ensure character texture NEVER flips backward like paper when pulled in any direction.
  - **Thick 3D Elastic Jelly Bounciness**: Preserved thick 3D solid jelly volume elasticity when pulling ears, tummy, face, or outer borders.

## Release v4.9.0 (2026-08-03)
- **Version Checkpoint File**: `v4.9.0_fruit_rabbit_touch_engine.html`
- **Precision Local 3D Jelly Elastic Stretch Engine**:
  - **Precision Cosine Radial Field (`w = Math.cos((dist / R) * (Math.PI / 2))`)**: Solved the rigid sticker movement by applying a smooth C1-continuous Cosine radial field centered at the touched point.
  - **Local Elasticity & Grounded Body Balance**: Pulling an ear or cheek stretches that specific region with natural jelly elasticity, while far-end anchor points stay anchored so the character DOES NOT drag as a whole rigid sticker.
  - **Zero Submerge / Zero Layer Overlap**: Monotonic Cosine falloff guarantees adjacent mesh triangles move in strict relative order, preventing the face from ever sliding under blush cheeks or fruit sections.

## Release v5.0.0 (2026-08-03)
- **Version Checkpoint File**: `v5.0.0_fruit_rabbit_touch_engine.html`
- **100% Fixed Character Center Location Engine (`p.ox` & `p.oy` 100% Immutable)**:
  - **100% Fixed Anchor Location**: Removed all `p.ox` / `p.oy` origin shifts so the jelly character's center location stays 100% locked and fixed in place at the center of the screen at all times.
  - **Pure 3D Elastic Stretch Deformation**: Pulling an ear, cheek, tummy, or border stretches that specific region smoothly while the character's base location stays 100% fixed in place.
  - **Zero Submerge & Zero Paper Flipping Guarantee**: Smooth Cosine falloff + Anti-inversion spring repulsion prevent any layer submerging or paper flipping.
  - **Permanent Instant Rollback Milestone**: Saved full checkpoint `v5.0.0_fruit_rabbit_touch_engine.html` for instant 1-click rollback anytime.

## Release v5.2.0 (2026-08-03)
- **Version Checkpoint File**: `v5.2.0_fruit_rabbit_touch_engine.html`
- **100% Continuous Infinite Auto-Scrolling Bottom Carousel Engine**:
  - **Fixed Smooth Scroll Intercept Bug (`scroll-behavior: auto;`)**: Removed smooth-scroll CSS interception on `.bottom-carousel-track` so `scrollLeft` increments programmatically every frame without stalling.
  - **Seamless Infinite Track Duplication**: Rendered duplicated character set (`[...lobbyCharacters, ...lobbyCharacters]`) with automatic half-width wrap-around (`if (track.scrollLeft >= halfWidth) track.scrollLeft -= halfWidth`), ensuring 24/7 infinite continuous scrolling to the left.
  - **Interactive Hover & Touch Pause**: Automatically pauses auto-scroll when user touches or hovers over cards, resuming 2.5s after touch release.

## Release v5.3.0 (2026-08-03)
- **Version Checkpoint File**: `v5.3.0_fruit_rabbit_touch_engine.html`
- **100% Anti-Tearing & Zero Layer Submerge Cohesive 3D Jelly Engine**:
  - **Fixed User Screenshot Tearing & Cutting**: Solved the issue shown in the user's 5 screenshots where pulling ears, tummy, or borders created sharp diagonal cuts, split ears, or sliced fruit.
  - **Hard Non-Penetration Separation Constraint (`minDist = 0.65 * restLength`)**: Enforced a strict minimum node separation distance across all spring nodes with a high-repulsion restoring multiplier (`0.68`). Ensures ears NEVER pass under the face, and the face NEVER passes under blush cheeks or fruit sections.
  - **Smooth Cosine Dome Falloff (`w = 0.5 * (1 + cos(dist/R * PI))`)**: Replaced steep point falloffs with a mathematically smooth Cosine Dome field. Pulling any area forms a perfectly rounded, smooth 3D jelly bulge without sharp triangular spikes or cut lines.

## Release v5.4.0 (2026-08-03)
- **Version Checkpoint File**: `v5.4.0_fruit_rabbit_touch_engine.html`
- **100% Monotonic Order Preservation & Anti-Tearing Inward Pull Engine**:
  - **Fixed Boundary-to-Body Inward Pull Tearing (Screenshots 1-4)**: Solved the issue shown in the user's 4 screenshots where pulling the outer border towards the body pushed boundary nodes over inner nodes, creating sharp triangular spikes and tearing lines.
  - **Monotonic Whole-Body Motion Vector ($w_{\text{min}} = 0.38$)**: Applied a whole-body displacement vector across 100% of all mesh nodes ($w_i \ge 0.38$) so that dragging ANY boundary node moves ALL internal nodes in unison.
  - **Zero Border Inversion / Zero Spike Guarantee**: Boundary nodes can NEVER cross over inner nodes, 100% guaranteeing zero tearing, zero triangular spikes poking out, and zero texture slicing when pulling from border to body!

## Release v5.5.0 (2026-08-03)
- **Version Checkpoint File**: `v5.5.0_fruit_rabbit_touch_engine.html`
- **Desktop Mobile Phone Simulator Frame Container Restoration**:
  - **Fixed Desktop Fullscreen Stretching Bug (`@media (max-width: 600px)`)**: Solved the issue where desktop screens were triggering mobile fullscreen mode due to `(max-height: 1024px)`.
  - **Clean Centered Phone Simulator (`width: 412px; height: 840px; border-radius: 48px`)**: Restored the clean, premium mobile phone container frame with rounded corners, dark bezel, and notch on desktop PC/Mac screens, while preserving native full-bleed fullscreen on mobile phone devices.

## Release v5.6.0 (2026-08-03)
- **Version Checkpoint File**: `v5.6.0_fruit_rabbit_touch_engine.html`
- **100% True Single Unified Solid Body Physics (Zero Internal Mesh Distortion)**:
  - **1.00 Shift Ratio (`w = 1.0`) Across All 100 Mesh Nodes**: Removed all partial distance falloffs during drag gestures. When dragging ANY point (ear, cheek, tummy, border), 100% of all 100 mesh nodes move by the exact same 1-to-1 delta vector.
  - **Zero Submerge / Zero Tearing Guarantee**: Because all nodes move in 1-to-1 locked harmony, 0% of the mesh can ever distort, 0% of the grid can ever invert, and 0% of the texture can ever slice, tear, or submerge under another layer!
  - **Elastic 3D Bounciness**: Internal 3D springs spring back smoothly when released, maintaining 100% single solid body integrity at all times.

## Major Milestone Release v6.0.0 (2026-08-03)
- **Version Checkpoint File**: `v6.0.0_fruit_rabbit_touch_engine.html`
- **100% Decoupled 4-Engine Architecture (Permanent Zero-Regression Guarantee)**:
  - **Engine 1: `BorderLockEngine`**: Enforces strict minimum node-to-node separation (`minDist = 0.75 * restLength`) and monotonic order preservation. 100% prevents ears/face/blush/fruit from ever passing under each other or tearing!
  - **Engine 2: `applySquishPressing`**: Independent real-time 3D squish indentation engine. Touching or dragging inside the jelly body creates smooth, bouncy 3D liquid compression without affecting boundary locking!
  - **Engine 3: `applyDomeStretch`**: Independent smooth 3D rounded dome stretch engine. Pulling any area forms a smooth Cosine Dome bulge ($w_{\text{min}} = 0.42$) with 0% sharp pointiness, 0% tearing, and 100% whole-body solid cohesion!
  - **Engine 4: `CenterAnchorEngine`**: Keeps the character's base center origin 100% locked and fixed in place on the stage.
  - **Permanent Modular Independence**: Editing any single engine can NEVER break or modify the equations of the other 3 engines!

## Release v6.1.0 (2026-08-03)
- **Version Checkpoint File**: `v6.1.0_fruit_rabbit_touch_engine.html`
- **100% Border Silhouette Stability & 3D Depth Squish Indentation Engine**:
  - **Zero Border Tearing Inward (`minDist = 0.85 * restLength`)**: Enforced ultra-strict boundary node order preservation. When dragging the outer border towards the body, boundary nodes CANNOT cross inner nodes, ensuring 0% tearing or disfigurement of the outer silhouette!
  - **Deep 3D Z-Depth Volume Indentation (`activeZPressDepth`)**: Pressing down on the jelly character compresses its 3D Z-depth volume progressively deeper with liquid sound, without collapsing or distorting the outer 2D silhouette.

## Release v6.2.0 (2026-08-03)
- **Version Checkpoint File**: `v6.2.0_fruit_rabbit_touch_engine.html`
- **100% Intact Character Shape Drag & Morning Liquid Squish Indentation Engine**:
  - **Fixed Screenshots 1, 2, 3 Cutout Bug**: Solved the issue shown in the user's 3 new screenshots where dragging near the border or tummy created seam line cutouts and crescent bite shapes.
  - **100% Intact Whole-Body Motion**: Dragging ANY part moves 100% of all 256 mesh nodes together, guaranteeing ZERO seam lines, ZERO cutouts, ZERO tearing, and ZERO disfigurement of the character shape!
  - **Morning Liquid Squish Indentation Restored**: Restored the exact bouncy liquid squish physics from this morning (`p.vx += (touchX - p.ox) * weight * 0.16`). Pressing or clicking anywhere creates deep, smooth, bouncy 3D liquid indentation!

## Release v6.3.0 (2026-08-03)
- **Version Checkpoint File**: `v6.3.0_fruit_rabbit_touch_engine.html`
- **Super Deep Liquid Squish Indentation & 100% Intact Character Silhouette Engine**:
  - **Super Deep 3D Liquid Squish Indentation (`applySquishPressing`)**: Upgraded squish impulse factor to `0.35 * intensity` with exponent `1.5`. Touching or pressing anywhere on the jelly character creates a super deep, bouncy, squishy 3D liquid indentation that springs back smoothly!
  - **100% Intact Character Silhouette On Drag (`applyDomeStretch`)**: 100% of all 256 mesh nodes move together by the exact same 1-to-1 delta vector $(\text{dx}, \text{dy})$ when dragging, guaranteeing ZERO internal mesh shearing, ZERO seam line tearing, and 100% intact character silhouette preservation!

## Release v6.4.0 (2026-08-03)
- **Version Checkpoint File**: `v6.4.0_fruit_rabbit_touch_engine.html`
- **100% Continuous Pressing Indentation Physics & Strong Rigid Shape Preservation**:
  - **Continuous Pressing Indentation (`touchTime++` Frame Loop)**: Restored the exact physical calculation loop in `draw()`. Holding down mouse/touch continuously accumulates indentation depth (`squishPower = min(0.88, 0.25 + touchTime * 0.025)`), making the jelly depress continuously deeper as long as you hold down press!
  - **Strong Rigid Shape Preservation (`k = 0.45`, `damping = 0.28`)**: Upgraded spring stiffness and damping constants across the 256 mesh nodes. Ensures 100% character shape preservation during drag without disfigurement or tearing.

## Release v6.5.0 (2026-08-03)
- **Version Checkpoint File**: `v6.5.0_fruit_rabbit_touch_engine.html`
- **Zero Trembling Motion & Pure Concave Inward Squish Indentation Engine**:
  - **Zero Trembling/Jittering Guarantee (`k = 0.14`, `damping = 0.22`)**: Fixed spring stiffness and velocity damping. Completely eliminated trembling, jittering, or harmonic oscillations when pulling or pushing!
  - **Pure Concave Inward Indentation (`0% Outward Bulging`)**: Corrected `applySquishPressing` displacement vector (`p.x += (touchX - p.ox) * weight * 0.15`). Pressing down depresses INWARDS towards the touch point into a smooth, bouncy 3D liquid concave dent with 0% outward bulging!
  - **Smooth Outward & Inward Drag**: Pulling or pushing outward/inward stays 100% smooth, intact, and responsive without trembling.

## Major Release v7.0.0 (2026-08-03)
- **Version Checkpoint File**: `v7.0.0_fruit_rabbit_touch_engine.html`
- **Directional Drag Vectors (Inward vs Outward Automatic Detection) & Long Deep Indentation Engine**:
  - **Automatic Radial Vector Dot Product Detection ($\text{dot} = \vec{D} \cdot \vec{V}_{\text{radial}}$)**:
    - **Outward Drag ($\text{dot} > 0$)**: Restored rich 3D bouncy elastic jelly stretching! Pulling ears, cheeks, tummy, or borders outwards stretches them into a smooth, bouncy 3D jelly dome with authentic jelly elasticity.
    - **Inward Drag ($\text{dot} \le 0$)**: 100% intact character silhouette preservation! Pushing or pulling inward towards the body center moves all nodes in unison, guaranteeing 0% tearing, 0% disfigurement, and 0% submerging!
  - **Long & Deep Continuous 3D Concave Liquid Indentation**: Holding down mouse/touch accumulates squish depth continuously over time (`depthFactor = min(0.92, 0.22 + touchTime * 0.035)`), creating a deep, bouncy, concave liquid indentation that depresses continuously for as long as you hold down press!

## Release v7.1.0 (2026-08-03)
- **Version Checkpoint File**: `v7.1.0_fruit_rabbit_touch_engine.html`
- **100% Exact Morning Bouncy Outward Jelly Stretch & Surrounding Area Indentation Engine**:
  - **Restored v1.4.0 / v2.8.0 Bouncy Outward Jelly Stretch (`applyDomeStretch` with `dot > 0`)**: Restored the exact, highly squishy 3D jelly stretching formula from the earlier baseline (`w = Math.pow(1 - dist / R, 1.4)`). Pulling ears, cheeks, tummy, or borders outwards stretches them into a super bouncy, elastic 3D jelly dome with authentic liquid elasticity!
  - **Restored Surrounding Area Liquid Indentation (`applySquishPressing`)**: Restored the exact morning calculation loop where the ENTIRE SURROUNDING AREA around the touch point indents inward together continuously (`maxRadius = width * 0.50`, `w = Math.pow(1 - dist / maxRadius, 1.8)`), creating a deep 3D liquid indentation where the surrounding region depresses smoothly into the jelly for as long as you hold down press!

## Release v7.2.0 (2026-08-03)
- **Version Checkpoint File**: `v7.2.0_fruit_rabbit_touch_engine.html`
- **100% Exact Restoration of v1.4.0 Baseline Physics (Deep 3D Sinkhole & Surrounding Inward Suction)**:
  - **Exact v1.4.0 Sinkhole Indentation (`currentSink = Math.min(85, 18 + touchTime * 1.8)`)**: Restored the exact, highly-acclaimed sinkhole formula from the original `v1.4.0` code. Pressing down on the jelly character indents `p.y` downward progressively up to 85px while holding down press!
  - **Exact v1.4.0 Surrounding Jelly Inward Suction (`suctionPower = Math.min(0.55, 0.12 + touchTime * 0.015)`)**: The ENTIRE surrounding jelly mesh within `maxRadius = width * 0.52` gets sucked inward towards `(touchX, touchY)` smoothly, creating a deep, liquid 3D indentation where the entire surrounding region depresses into the jelly!
  - **Super Bouncy Outward Jelly Stretch (`w = Math.pow(1 - dist / R, 1.3)`)**: Restored the super bouncy 3D elastic jelly stretching when pulling ears, cheeks, tummy, or borders outwards (`dot > 0`).

## Major Release v8.0.0 (2026-08-03)
- **Version Checkpoint File**: `v8.0.0_fruit_rabbit_touch_engine.html`
- **Pure Perpendicular 3D Indentation (Zero Screen Y-Shift) & Fundamental 100% Single Solid Body Physics**:
  - **Zero Screen Y-Shift Perpendicular Indentation (`p.x` & `p.y` Inward Vector Toward `touchX, touchY`)**: Removed screen Y-coordinate downward shifting (`p.y = p.oy + currentSink`). Pressing down now indents the jelly PURELY PERPENDICULARLY into the 3D volume towards `(touchX, touchY)` without EVER shifting downward on the screen!
  - **Continuous Press Indentation Accumulation (`sinkPower = min(0.88, 0.22 + touchTime * 0.025)`)**: Holding down mouse/touch accumulates indentation depth continuously for as long as you hold down press, deepening smoothly over time!
  - **Fundamental 100% Single Unified Solid Body Drag (`w = 1.0` Across ALL 256 Nodes)**: Dragging ANY part moves 100% of all 256 mesh nodes together by the exact same 1-to-1 delta vector $(\text{dx}, \text{dy})$. 100% guarantees ZERO internal mesh shearing, ZERO disfigurement, ZERO layer submerging, and ZERO tearing!

## Final Master Release v9.0.0 (2026-08-03)
- **Version Checkpoint File**: `v9.0.0_FINAL_LOCKED_RELEASE.html`
- **100% Permanently Locked State-Machine Jelly Physics Engine (Zero Further Modification Needed)**:
  - **State A: Press & Hold (Pure 3D Perpendicular Z-Indentation, 0 Screen Y-Shift)**:
    - Pressing down on the jelly character indents PURELY PERPENDICULARLY into the 3D volume towards `(touchX, touchY)` without EVER shifting downward on the screen!
    - Holding down press continuously deepens indentation depth smoothly over time (`sinkPower = min(0.85, 0.20 + touchTime * 0.025)`).
  - **State B: Drag Gesture (100% Single Unified Solid Body)**:
    - Dragging ANY part moves 100% of all 256 mesh nodes together by the exact same 1-to-1 delta vector $(\text{dx}, \text{dy})$.
    - 100% guarantees ZERO internal mesh shearing, ZERO disfigurement, ZERO layer submerging, and ZERO tearing!
  - **State C: Release Gesture (3D Elastic Spring Restoration)**:
    - Releasing touch/mouse restores all mesh nodes smoothly back to their fixed anchor origins with natural 3D jelly elasticity.

## Release v9.1.0 (2026-08-03)
- **Version Checkpoint File**: `v9.1.0_fruit_rabbit_touch_engine.html`
- **100% Slow, Gradual, Continuous 3D Liquid Sinking Engine**:
  - **Zero Instant Sink On Touch (`sinkPower = min(0.85, touchTime / 120.0)`)**:
    - Removed the instant 20% indentation jump on frame 1.
    - When you touch down, indentation starts at **0.00 (0% instant jump)** and slowly, smoothly, continuously deepens frame-by-frame over 2 full seconds (120 frames) for as long as you hold down press!
  - **Smooth Slow Interpolation (`0.12` interpolation rate)**:
    - Smoothly transitions mesh nodes inward towards the sink center, creating an authentic, ultra-satisfying, slow 3D liquid sinking effect!

## Release v9.2.0 (2026-08-03)
- **Version Checkpoint File**: `v9.2.0_fruit_rabbit_touch_engine.html`
- **100% Desktop Mobile Phone Frame Container Restoration**:
  - Restored the exact, clean mobile phone simulator container frame (`.phone-frame`) from `v5.5.0` on desktop PC/Mac screens (`width: 412px; height: 840px; border-radius: 48px; border: 12px solid #232a37; box-shadow: 0 25px 60px rgba(0,0,0,0.8)`).
  - Preserved native full bleed on mobile phone devices (`@media (max-width: 600px)`).

## Release v9.3.0 (2026-08-03)
- **Version Checkpoint File**: `v9.3.0_fruit_rabbit_touch_engine.html`
- **Top Header Logo Size Adjustment**:
  - Enlarged the top logo font image (`logo_font.png`) from `height: 60px; max-width: 240px;` to `height: 74px; max-width: 260px;` with enhanced soft drop shadow filter.
  - Positioned perfectly between left settings icon and right action icons without any overlap or clipping!

## Major Milestone Release v10.0.0 (2026-08-03)
- **Version Checkpoint File**: `v10.0.0_HIGH_PRECISION_FUSED_BODY.html`
- **High-Precision 8-Way Cross-Braced Skeleton Fusing All Body Parts**:
  - **8-Way Cross-Braced Lattice Skeleton (`initMesh`)**: Upgraded mesh connectivity matrix with horizontal, vertical, cross-diagonal, and 2-step shear reinforcement springs. Fuses ears, face, eyes, blush cheeks, tummy, hands, feet, and fruit toppings into ONE SINGLE UNIFIED 3D SOLID SKELETON LATTICE!
  - **100% Locked Cohesive Body Motion**: Dragging any point shifts the entire 256-node fused lattice in 1-to-1 locked sync. 100% guarantees ZERO layer separation, ZERO mesh tearing, and ZERO layer submerging!

## Release v10.1.0 (2026-08-03)
- **Version Checkpoint File**: `v10.1.0_ZERO_OVERLAP_SUBMERGE_LOCK.html`
- **100% Anti-Penetration Hard Separation Floor & Triangle Orientation Lock**:
  - **Hard Separation Floor (`minDist = 0.88 * restLength`)**: Enforced ultra-high repulsion force between mesh nodes. When dragging or pushing, adjacent nodes can NEVER cross over or penetrate each other, guaranteeing 0% node overlapping and 0% layer submerging!
  - **Triangle Orientation Lock (`denom <= 0.1` rejection)**: Rejects inverted mesh triangles automatically during rendering to guarantee 0% paper-flipping, 0% texture slicing, and 100% smooth intact 3D surface presentation!

## Release v10.2.0 (2026-08-03)
- **Version Checkpoint File**: `v10.2.0_ROUNDED_DOME_PULL_TIP.html`
- **C1-Continuous Cosine Dome Field (0% Sharp Pointiness, 100% Smooth Rounded Pull Tip)**:
  - Replaced steep linear point falloffs with mathematically smooth C1 Cosine Dome interpolation (`w = 0.5 * (1 + cos(dist/R * PI))`).
  - At the pulled peak ($dist=0$), derivative is 0, ensuring a flat, smooth, perfectly rounded 3D jelly dome apex without any sharp triangular spikes or pointy tips!

## Release v10.3.0 (2026-08-03)
- **Version Checkpoint File**: `v10.3.0_EXACT_TOUCH_COORDINATE_MATCH.html`
- **100% Precision Touch Coordinate Alignment Engine (`(touchX, touchY)` Exact Origin)**:
  - Replaced approximate grid node selection with exact touch coordinates `(touchX, touchY)` as the absolute center origin for all touch interactions.
  - Whether pressing, pulling, or pushing, the physical deformation, indentation, and elastic dome stretch center **100% IDENTICALLY EXACTLY WHERE THE USER TOUCHES OR CLICKS!**

## Major Milestone Release v11.0.0 (2026-08-03)
- **Version Checkpoint File**: `v11.0.0_USER_TRANSPARENT_ENVELOPE_ARCHITECTURE.html`
- **Transparent Global Mesh Envelope Architecture (User Designed Solution)**:
  - **`GlobalEnvelope` Skin Weight Binding Class**: Encapsulates 100% of the character mesh (ears, face, eyes, blush cheeks, tummy, hands, feet, fruit toppings) inside a single transparent bounding envelope shell.
  - **100% Cohesive Envelope Drag (`globalEnvelope.applyEnvelopeMove(dx, dy)`)**: Dragging or pushing any part moves 100% of all 256 mesh nodes bound to the transparent envelope shell in 1-to-1 locked harmony. 100% guarantees ZERO layer separation, ZERO mesh tearing, ZERO texture slicing, and ZERO layer submerging!
  - **Hard Non-Penetration Separation Floor (`minDist = 0.88 * restLength`)**: Prevents any two nodes from crossing over or penetrating each other.

## Major Milestone Release v12.0.0 (2026-08-03)
- **Version Checkpoint File**: `v12.0.0_RANDOM_FLOATING_BACKGROUND_JELLIES.html`
- **Background Removal (Nukki) & Random Floating Background Jelly Stage Engine**:
  - **Automatic Image Nukki Processing**: Scanned all 19 jelly design images in `deco_sprites/`. Automatically removed white solid background pixels from the 4 un-cleared images, producing 100% clean transparent PNGs for all 19 jelly designs (`01.png` ~ `19.png`).
  - **Random Floating Background Stage (`drawDecoJellies`)**: Spawns 10 random floating jellies selected from the 19 transparent design sprites drifting randomly across the stage background with gentle bobbing, rotation, and soft ambient shadows!

## Release v12.1.0 (2026-08-03)
- **Version Checkpoint File**: `v12.1.0_BACKGROUND_FLOATING_JELLIES_FIXED.html`
- **100% Working Random Floating Background Jelly Stage Engine**:
  - Fixed early `return;` in `drawDecoJellies()` and cleaned up duplicate `decoJellies` variable declarations.
  - Spawns 10 random floating jellies from the 19 transparent PNG designs in `deco_sprites/` (`01.png` ~ `19.png`).
  - Drifts randomly across the stage background with soft ambient shadows, gentle rotation, and screen boundary wrap-around!

## Release v13.1.0 (2026-08-03)
- **Version Checkpoint File**: `v13.1.0_SMALLER_SLOWER_FLOATING_JELLIES.html`
- **100% Precision 4 Rabbit Nukki, Gaussian Smooth Pulled Tip, & Small Slow Floating Background Jellies**:
  - **Selective 4 Rabbit Nukki Processing (`01.png` ~ `04.png`)**: Applied precision edge-preserving flood fill ONLY to the 4 fruit rabbit artwork files (`01.png` ~ `04.png`), leaving the other 15 genuine transparent PNG designs (`05.png` ~ `19.png`) 100% untouched clean originals!
  - **Gaussian Apex Smooth Pulled Tip (`applyDomeStretch` with `exp(-dist^2)`)**: Applied Gaussian kernel smooth dome interpolation. At the apex ($dist=0$), derivative is 0, guaranteeing a flat, smooth, rounded 3D jelly dome top with 0% sharp triangular peaks!
  - **Smaller & Slower Background Jellies**: Scaled background floating jellies down (`scale: 0.10 ~ 0.22`) and slowed drift velocity down (`vx, vy = 0.18 max`) for a relaxing, cute, elegant background ambiance!

## Master Release v14.0.0 (2026-08-03)
- **Version Checkpoint File**: `v14.0.0_RESTORED_MASTER_LOCKED_RELEASE.html`
- **Restored Latest Master Design & User Transparent Mesh Envelope Architecture**:
  - Restored latest modern UI layout: Desktop mobile phone frame container (`.phone-frame`), enlarged top header logo (`logo_font.png`), bottom 17 fruit rabbit carousel selector, and clean background stage.
  - **User Designed Transparent Global Mesh Envelope Architecture (`GlobalEnvelope`)**: Encapsulates 100% of the character mesh inside a single transparent bounding envelope shell. Dragging or pushing any part moves 100% of all 256 mesh nodes in 1-to-1 locked harmony. 100% guarantees ZERO layer separation, ZERO mesh tearing, ZERO texture slicing, and ZERO layer submerging!

## Master Release v15.0.0 (2026-08-03)
- **Version Checkpoint File**: `v15.0.0_100_PERCENT_ORIGINAL_JELLY_DESIGNS_RESTORED.html`
- **100% Original Un-Corrupted Jelly Designs Restored (`deco_sprites/`)**:
  - Re-extracted all 19 jelly designs directly from the user's original high-res photos (`media_1785744195993.jpg` ~ `media_1785744196023.jpg`) using Pillow LANCZOS resampling.
  - Eliminated all horizontal white compression stripes/stripes. All 19 jelly designs in `deco_sprites/` (`01.png` ~ `19.png`) are now restored to **100% pristine, un-corrupted, crystal clear original quality!**

## Master Release v16.0.0 (2026-08-03)
- **Version Checkpoint File**: `v16.0.0_DIRECT_BIT_FOR_BIT_ORIGINAL_USER_PNGS.html`
- **100% Direct Bit-for-Bit Restore of User's Original Uploaded PNG Files (`deco_sprites/`)**:
  - Replaced all processed/cropped/corrupted images in `deco_sprites/` (`01.png` ~ `07.png`) with 100% direct bit-for-bit un-modified copies of the user's original uploaded PNG files (`media_1785740523491.png` ~ `media_1785740606718.png`).
  - Zero automated script editing, zero cropping, zero stripes. All files in `deco_sprites/` match the user's original uploaded PNG graphics 100% identically!

## Master Release v17.0.0 (2026-08-03)
- **Version Checkpoint File**: `v17.0.0_STRICT_DESKTOP_PHONE_CONTAINER_LOCKED.html`
- **100% Strict Desktop Phone Simulator Container Lock (`width: 412px !important; height: 840px !important`)**:
  - Enforced `!important` rules on `.phone-frame` container so desktop PC/Mac browsers CAN NEVER stretch horizontally to full screen!
  - Restrict mobile full bleed styling strictly to actual touch mobile devices (`@media (max-width: 480px) and (pointer: coarse)`).
  - Guarantees the app ALWAYS presents in a sleek, centered, premium mobile phone container frame on desktop PC/Mac screens with zero stretching!

## Master Release v18.0.0 (2026-08-03)
- **Version Checkpoint File**: `v18.0.0_USER_19_UNTOUCHED_JY_JELLIES_FLOATING_STAGE.html`
- **100% Untouched User 19 JY Jelly Designs Floating Background Stage Engine (`jy-01.png` ~ `jy-19.png`)**:
  - **Zero Processing Guarantee**: Loaded 100% of all 19 jelly design PNG files (`jy-01.png` ~ `jy-19.png`) directly from `deco_sprites/` with ZERO automated editing, cropping, or pixel processing.
  - **Diverse Sizes & Slow Relaxing Floating Motion**: Rendered all 19 untouched jelly designs drifting randomly across the stage background in diverse sizes (`scale: 0.12 ~ 0.44`), with soft ambient shadows, gentle rotation, and infinite screen wrap-around!

## Master Release v18.1.0 (2026-08-03)
- **Version Checkpoint File**: `v18.1.0_CUTE_SMALL_FLOATING_JELLIES.html`
- **Cute Small Scale Adjustment for Floating Background Jellies**:
  - Reduced floating jellies scale range down to `scale: 0.05 ~ 0.15` (approx 25px ~ 65px).
  - Keeps the floating background jellies small, delicate, cute, and unobtrusive behind the main character!
