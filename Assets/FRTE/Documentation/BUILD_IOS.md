# Building for iOS Platform

### Xcode Export Prerequisites
- **Target OS Minimum**: iOS 13.0
- **Scripting Backend**: IL2CPP
- **Architecture**: ARM64
- **Haptic Support**: Uses Taptic Engine API.

### Info.plist Privacy Keys
Ensure you populate target usage description keys:
- `NSCameraUsageDescription`: Required for taking custom rabbit selfies.
- `NSPhotoLibraryAddUsageDescription`: Required for exporting squishy images to Camera Roll.
- `NSPhotoLibraryUsageDescription`: Required for choosing custom gallery backdrops.

### Export Pipeline
1. Build the Xcode project from Unity (`Build Settings > Build`).
2. Open the exported directory in Xcode.
3. Select your developer profile team.
4. Run/Archive the application to iOS device.
