# Performance Optimization Guide

To guarantee stable **60 FPS** on mobile devices:
- **Low Profile (Budget Devices)**: Scales mesh grid down to 10x10, limits surprise effects, and scales video recorder to 720p / 30FPS.
- **Medium Profile (Standard)**: 15x15 mesh grid, 1080p rendering.
- **High Profile (Premium)**: 20x20 mesh grid, 60FPS video capture (high-end iOS/Android).

### GC Zero-Alloc Rule
- Pools all surprise event particle objects using `ISurpriseEffectPool`.
- Avoids LINQ or dynamic closures in the `Update()` touch loop.
- Pre-allocates array buffers for mesh vertices readbacks.
