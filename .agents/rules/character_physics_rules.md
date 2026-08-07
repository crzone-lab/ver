# Character Physics & Texture Interaction Rules

1. **Bottom Base Anchoring (캐릭터 바닥면 100% 바닥 고정)**
   - The bottom row of mesh points (`r = rows - 1`) MUST stay completely pinned to the floor plane (`y = oy`, `vy = 0`).
   - When touched or pressed, expansion/swelling MUST occur upwards and outwards in the middle/upper body, while the bottom base remains glued flat to the floor.

2. **Tankle Jelly Non-Stretch (탱글젤리는 당기면 안 늘어남)**
   - Tankle Jelly (`jelly` mode) MUST NOT stretch or elongate away like a rubber band when pulled/dragged.
   - When pulled, it remains firm and rigid in place.

3. **Jelly Pop Touch Scope Isolation (젤리팝 바탕 터치 무반응)**
   - Jelly Pop (`bubble` mode) bubble inflation MUST ONLY trigger when touching directly ON the character body mesh (`minDist < character_radius`).
   - Touches on the surrounding canvas background MUST be ignored and produce NO reaction.

4. **Jelly Pop 3D Volumetric Bubble Lighting (젤리팝 3D 볼륨 조명 연출)**
   - Each inflating balloon dome MUST have distinct 3D volumetric shading, specular highlights, and contour highlights so users can clearly discern the location and count of each swelling bubble.
