# Privacy Data Flow Document

In accordance with strict personal privacy policies:
1. **Zero External Transfers**: User pictures, photos taken via camera, or loaded from the gallery are stored solely in local volatile memory (`Texture2D` runtime objects).
2. **Offline Masking/Landmarks**: Bounding box extraction and facial landmarks detection run 100% locally on the device.
3. **No Automatic Uploads**: Captures are only saved to the disk when the user clicks the "Save to Gallery" or "Share" button.
4. **Temp Cleanup**: Cached frames in temporary directories are automatically cleared when recording finishes or is canceled.
5. **No Data Tracking**: Custom user photo paths are not printed to logs.
