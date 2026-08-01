# FRTE Export System Guide

The Export module handles background image renders, frame-based video capturing, and platform file shares.

### Camera Layer Composition
The capture utilizes a dedicated Camera that renders the following layers:
- `PhotoZone Background`
- `Squishy Photo Mesh`
- `Decoration overlays`
- `Surprise effects`

UI buttons, slider anchors, and debug grids are placed on the `Overlay UI` layer and are excluded during render.

### Transparency PNG Renders
- Set `ImageExportOptions.TransparentBackground = true`.
- Deactivate background backdrops.
- The cam clears to alpha zero, creating transparent PNGs (retaining original transparency when sharing to other platforms).
