# Jelly Pop Mode - Pure Character Mesh Balloon Inflation Rules

Whenever editing or updating `index.html` or jelly pop balloon inflation code, YOU MUST READ AND FOLLOW THESE MANDATORY RULES:

1. **High Mesh Density for Silky Smooth Round Domes (각짐 100% 제거)**:
   - Set mesh grid `rows = 26; cols = 26;` (1,250+ triangles) so that balloon swells form **perfectly smooth, round curved domes** without any sharp angular polygon corners.
   - Use Gaussian weight curves with controlled sigma (`sigma = Math.max(22, rbf.currentRadius * 0.70)`) to maintain smooth circular curvature.

2. **4~5 Distinct Separated Swells Across Character Body (4-5개 위치 & 크기 랜덤)**:
   - When touching and holding, spawn 4 to 5 separate balloon control points distributed across different parts of the character (offsets of 45px to 110px).
   - Each control point inflates independently at its own position with random initial size (`initR = 10~18px`) and growth speed (`growthSpeed = 0.04~0.08px/frame`), staying visually distinct!

3. **Very Slow Swelling Speed (누르는 동안 천천히 커짐)**:
   - Inflation MUST be ultra-slow (`growthSpeed = 0.04 ~ 0.08px/frame`). The user must press and hold for several seconds until 1 balloon reaches its burst limit (`burstThreshold`).

4. **Center Sharp Slit Tear & Flying Shards on Pop (가운데 날카로운 찢어짐 & 파편 흩날림)**:
   - When the largest balloon reaches `burstThreshold`, it POPS:
     - **Center Slit Tear (가운데 날카로운 찢어짐)**: Radiate sharp jagged tearing slit lines across the center of the balloon dome and physically pull mesh vertices apart along the slit axis.
     - **Flying Shards (파편 흩날림)**: Explosion of 35~45 flying balloon shards (`largeShards`) bursting outward from the tear origin into the air.
