# Audio Replacement Guide

Audio clips are stored as assets and referenced in the Audio Mixer configs.

### Custom Sound Steps:
1. Save your custom WAV/MP3 files (mono, 44.1kHz recommended for sound effects) into `Assets/FRTE/Audio/Clips/`.
2. Locate the central Audio Controller configuration or Audio Preset scriptable asset.
3. Replace the fields `TouchSFX`, `DragSFX`, `ReleaseSFX`, and `SurpriseSFX` with your new audio clips.
