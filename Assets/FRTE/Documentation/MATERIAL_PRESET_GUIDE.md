# Material Preset Tuning Guide

The SDK supports 12 standard material presets (6 general types + 6 fruit squish profiles):
- **Jelly / Strawberry**: High bounce, moderate dampening.
- **Mochi / Peach**: High stiffness, slow recovery speed.
- **Slime / Kiwi**: Extreme deformation, very low spring strength.
- **Balloon / Grape**: Low mass, instant restoration.

### Custom Presets
To adjust presets in-game:
1. Locate `SquishyMaterialPreset` assets.
2. Adjust `SpringStrength`, `Damping`, `Mass`, and `WobbleAmount` parameters.
3. Call `IMaterialPresetController.ApplyPreset("fruit.strawberry")` to reload parameters onto the physics solver.
