with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Home button onclick in HTML
content = content.replace(
    'id="global-home-exit-btn" onclick="exitGame()"',
    'id="global-home-exit-btn" onclick="goBackToLobby()"'
)

# 2. Fix Strawberry Rabbit sizeScale to 1.45x
content = content.replace(
    'let sizeScale = 1.0;\n            if (activeBase === "strawberry_rabbit" || (jellyImage && jellyImage.src && jellyImage.src.includes("strawberry_rabbit"))) {\n                sizeScale = 1.30;\n            }',
    'let sizeScale = 1.0;\n            if (activeBase === "strawberry_rabbit" || (jellyImage && jellyImage.src && jellyImage.src.includes("strawberry_rabbit"))) {\n                sizeScale = 1.45;\n            }'
)

# 3. Replace deformMesh in draw() with Solid Cohesive Drag (No downward squishing)
old_draw_block = """                // 1. Fixed Body Anchor: Character stays in place, pulled part stretches locally
                if (isTouching) {
                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY;
                        points[grabbedPointIndex].vx = 0;
                        points[grabbedPointIndex].vy = 0;

                        // Local squishy deformation falloff while character body stays anchored at origin (ox, oy)
                        let grabbedPoint = points[grabbedPointIndex];
                        let maxRadius = width * 0.38;
                        for (let i = 0; i < points.length; i++) {
                            if (i === grabbedPointIndex) continue;
                            let p = points[i];
                            let pdx = p.ox - grabbedPoint.ox;
                            let pdy = p.oy - grabbedPoint.oy;
                            let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                            if (dist < maxRadius) {
                                let weight = Math.pow(1 - dist / maxRadius, 2.0);
                                p.x = p.ox + (touchX - grabbedPoint.ox) * weight * 0.65;
                                p.y = p.oy + (touchY - grabbedPoint.oy) * weight * 0.65;
                                p.vx *= 0.5; p.vy *= 0.5;
                            }
                        }
                    } else {
                        deformMesh(touchX, touchY, 12);
                    }
                } else {"""

new_draw_block = """                // 1. Single Solid Cohesive Touch Drag Physics (No downward squishing!)
                if (isTouching) {
                    let dx = touchX - lastTouchX;
                    let dy = touchY - lastTouchY;
                    lastTouchX = touchX;
                    lastTouchY = touchY;

                    // Move 100% of all points together smoothly as ONE SINGLE SOLID COHESIVE BODY
                    for (let i = 0; i < points.length; i++) {
                        points[i].x += dx;
                        points[i].y += dy;
                        points[i].vx *= 0.5;
                        points[i].vy *= 0.5;
                    }
                } else {"""

if old_draw_block in content:
    content = content.replace(old_draw_block, new_draw_block)
    print("Successfully replaced deformMesh in draw()!")
else:
    print("WARNING: old_draw_block not found in content!")

# 4. Make sure goBackToLobby is 100% robust
old_goback = """        function goBackToLobby() {
            stopAutopilot(); releaseGrab(true); releaseGrab(true);
            setScreenMode('lobby');
            renderLobbyGrid();
        }"""

new_goback = """        function goBackToLobby() {
            try {
                releaseGrab(true); releaseGrab(true);
                setScreenMode('lobby');
                renderLobbyGrid();
            } catch(e) {
                console.error("goBackToLobby error:", e);
                setScreenMode('lobby');
            }
        }"""

if old_goback in content:
    content = content.replace(old_goback, new_goback)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied patch_fix_hover_and_home.py to index.html!")
