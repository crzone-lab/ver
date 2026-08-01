# Known Issues & Limitations

1. **GIF Export Frame Limits**:
   Due to high memory consumption on lower-end Android devices during frame quantization, GIF export is capped at a maximum of 30 frames (approx. 2 seconds at 15 FPS) as a safety mechanism.
2. **ReplayKit Background Sleep**:
   On iOS, if the app transitions to sleep mode while recording via ReplayKit, the encoding process is cancelled automatically.
3. **Editor Frame Recorders**:
   Inside the Unity Editor, the video exporter records utilizing simulated dummy bytes since native platform recorders require silgigi hardware modules.
