# FruitRabbit Jelly Style & Physics Engine Technical Architecture

This document describes the offline image processing filter, modular character registration, phase-based haptic/audio logic, and physical deformation solvers.

---

## 1. Photo-to-Jelly Style Engine (얼굴 인식 젤리 필터)
To convert a real photo into a wet, glossy, translucent jelly **while keeping the person 100% recognizable**, we utilize a local GPU Shader-based rendering pipeline instead of heavy server-side AI style transfers.

```text
[Input Photo] 
    → Local Crop (Face only)
    → Apply Specular/Refraction Shader (Translucent glass overlays + specular highlight maps)
    → Deformed Mesh Grid
    ➔ Result: Shiny, translucent jelly face
```

### Specular & Translucency Shader Design:
- **Translucent Albedo**: Keeps the original face image visible but introduces a glossy, wet sheen.
- **Normal Map Generation**: Dynamically constructs a spherical/dome normal map centered around the face center, making the flat photo appear 3D and rounded.
- **Specular Highlight & Reflection Map**: Reflects a bright highlight spot (e.g. window reflections) as the user pushes or pulls the jelly mesh.
- **Refraction Offset**: Bends pixels near the edges of the mesh to simulate refractive glass boundaries.

---

## 2. Modular Character Registries (10~20종 확장 구조)
Adding 10-20 distinct Rabbit characters is handled without modifying code through the `DecorationPreset` and `PhotoZonePreset` ScriptableObjects:
- **Add Rabbit Presets**: Save Rabbit PNGs to `/Art/` directories.
- **Array Registry**: Create corresponding `DecorationPreset` assets and link them to the scroll view controller. The layout dynamically expands to support any number of rabbit types.

---

## 3. Phase-Based Haptic & Audio Feedback (촉감 / 진동 / 효과음)
Touch interactions translate directly to tactile feel through state mappings:

| Touch Phase | Physical Simulation | Haptic Feedback (Vibrations) | Audio Feedback (Sound SFX) |
| :--- | :--- | :--- | :--- |
| **Began** (첫 터치) | Mesh indent/depression | **Pop/Impact Haptic**: Light/Medium pulse. | Short squishy pop/suction sound. |
| **Moved** (당기기/밀기) | Mass-spring stretching | **Friction Rumble**: Continuous low-frequency amplitude vibrations, rising as pull distance increases. | Pitch-bent rubber friction sound (higher pitch when pulled further). |
| **Ended** (손을 뗄 때) | Spring bounce restoration | **Snap-back Impulse**: Strong transient vibration. | Elastic spring snap or bounce squish sound. |

---

## 4. Physics Engine Calculations (질량-스프링-댐퍼 수식)
Each vertex \(i\) on the deformed mesh follows the classical Newton spring equation:

\[M \frac{d^2 \mathbf{x}_i}{dt^2} + C \frac{d\mathbf{x}_i}{dt} + \sum_{j \in N(i)} K (\mathbf{x}_j - \mathbf{x}_i - \mathbf{r}_{ij}) = \mathbf{F}_{touch}\]

Where:
- \(M\) = Vertex Mass (determines wobbliness / inertial drag).
- \(C\) = Damping Coefficient (dampens vibrations so jelly settles).
- \(K\) = Spring Stiffness (elastic recovery pull).
- \(\mathbf{F}_{touch}\) = Indentation force calculated by distance to screen finger coordinates.
