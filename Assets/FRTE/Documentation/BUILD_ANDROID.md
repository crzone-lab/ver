# Building for Android Platform

### Build Settings
- **Scripting Backend**: IL2CPP
- **Target Architectures**: ARMv7, ARM64
- **Minimum API Level**: API Level 24 (Android 7.0)
- **Target API Level**: Latest stable (API Level 34 recommended)

### Keystore Configuration
- Create or load your release keystore under `Project Settings > Player > Publishing Settings`.
- Sign with your developer key before exporting release bundles (.aab).

### Permissions Required
- Camera (for capture/photo import): Automatically handled by picker.
- Write external storage: Utilizes MediaStore API to bypass legacy permission prompts on Android 10+.
