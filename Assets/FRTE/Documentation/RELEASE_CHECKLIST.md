# FruitRabbit Squishy Release Checklist

Ensure you complete the following steps before submitting to Google Play or Apple App Store:
- [ ] Replace all procedural debug colors with final artwork.
- [ ] Configure the bundle identifier and package name.
- [ ] Set scripting backend to IL2CPP (mandatory for ARM64).
- [ ] Sign assemblies with release key credentials.
- [ ] Check privacy description strings in Xcode.
- [ ] Deactivate the `Developer Debug Panel` in release configuration.
- [ ] Verify local database PlayerPrefs are not corrupted.
