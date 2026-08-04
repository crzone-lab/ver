import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Multi-Touch (2~3 Fingers) + 2-Finger Squeeze Balloon Inflation Engine
multi_touch_code = """        // --- Multi-Touch & 2-Finger Pinch Balloon Inflation Engine ---
        let activeTouchList = [];

        const getAllTouchPos = (e) => {
            if (!e.touches || e.touches.length === 0) return [];
            let rect = canvas.getBoundingClientRect();
            let scaleX = canvas.width / rect.width;
            let scaleY = canvas.height / rect.height;
            let list = [];
            for (let i = 0; i < Math.min(e.touches.length, 3); i++) {
                list.push({
                    x: (e.touches[i].clientX - rect.left) * scaleX,
                    y: (e.touches[i].clientY - rect.top) * scaleY
                });
            }
            return list;
        };

        const getTouchPos = (e) => {
            let list = getAllTouchPos(e);
            return list.length > 0 ? list[0] : null;
        };"""

# Replace old getTouchPos definition
idx_gtp = content.find('const getTouchPos =')
idx_gtp_end = content.find('};', idx_gtp) + 2

if idx_gtp != -1:
    content = content[:idx_gtp] + multi_touch_code + "\n" + content[idx_gtp_end:]
    print("100% Successfully updated getAllTouchPos & Multi-Touch helper!")

# Update touchstart and touchmove event listeners
old_ts = "canvas.addEventListener('touchstart', (e) => {"
idx_ts_start = content.find(old_ts)
idx_tm_end = content.find("}, { passive: false });", content.find("canvas.addEventListener('touchmove'")) + 23

updated_listeners = """canvas.addEventListener('touchstart', (e) => {
            if (!isPlaygroundActive() || isAutopilotActive) return;
            stopAutopilot(); releaseGrab(true); releaseGrab(true);
            e.preventDefault();
            
            activeTouchList = getAllTouchPos(e);
            if (activeTouchList.length === 0) return;
            
            let pos = activeTouchList[0];
            let minDist = 99999;
            let closestIdx = -1;
            for (let i = 0; i < points.length; i++) {
                let d = Math.sqrt(Math.pow(points[i].x - pos.x, 2) + Math.pow(points[i].y - pos.y, 2));
                if (d < minDist) {
                    minDist = d;
                    closestIdx = i;
                }
            }
            if (minDist < width * 0.35) {
                grabbedPointIndex = closestIdx;
                playSquishSound(false);
                triggerHaptic(15);
            }
            
            isTouching = true;
            touchX = pos.x;
            touchY = pos.y;
            lastTouchX = pos.x;
            lastTouchY = pos.y;
            touchTime = 0;
        }, { passive: false });

        canvas.addEventListener('touchmove', (e) => {
            if (!isPlaygroundActive() || isAutopilotActive) return;
            e.preventDefault();
            
            activeTouchList = getAllTouchPos(e);
            if (activeTouchList.length === 0) return;
            
            let pos = activeTouchList[0];
            touchX = pos.x;
            touchY = pos.y;
            isTouching = true;

            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                gPoint.x = pos.x;
                gPoint.y = pos.y;
            }
        }, { passive: false });"""

if idx_ts_start != -1 and idx_tm_end != -1:
    content = content[:idx_ts_start] + updated_listeners + content[idx_tm_end:]
    print("100% Successfully updated touch event listeners for Multi-Touch support!")

# Add 2-Finger Squeeze Balloon Inflation Physics in draw()
balloon_physics = """
                // 2-Finger Squeeze Balloon Inflation Physics (두 손가락 꼭 잡으면 가운데 풍선 부풀어 오름)
                if (isTouching && activeTouchList && activeTouchList.length >= 2) {
                    let p1 = activeTouchList[0];
                    let p2 = activeTouchList[1];
                    let midX = (p1.x + p2.x) / 2;
                    let midY = (p1.y + p2.y) / 2;

                    let fingerDist = Math.hypot(p2.x - p1.x, p2.y - p1.y);
                    let swellRadius = Math.max(width * 0.38, fingerDist * 1.2);
                    let bulgeForce = Math.min(38.0, Math.max(12.0, (280.0 - fingerDist) * 0.28));

                    // Push mesh nodes outwards from midpoint between the two fingers
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let dx = p.ox - midX;
                        let dy = p.oy - midY;
                        let dist = Math.hypot(dx, dy);

                        if (dist < swellRadius && dist > 1.0) {
                            let weight = Math.pow(1 - dist / swellRadius, 1.5);
                            let nx = dx / dist;
                            let ny = dy / dist;

                            // Inflate outward like a balloon
                            p.x += nx * weight * bulgeForce * 0.35;
                            p.y += ny * weight * bulgeForce * 0.35;
                        }
                    }

                    // Render 3D swelling balloon light reflection between the two fingers
                    ctx.save();
                    let bGrad = ctx.createRadialGradient(midX, midY, 4, midX, midY, swellRadius * 0.65);
                    bGrad.addColorStop(0, 'rgba(255, 255, 255, 0.65)');
                    bGrad.addColorStop(0.4, 'rgba(255, 240, 200, 0.35)');
                    bGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                    ctx.fillStyle = bGrad;
                    ctx.beginPath();
                    ctx.arc(midX, midY, swellRadius * 0.65, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.restore();
                }"""

# Inject balloon_physics into draw() right after // 2. Render Elastic Deformed 3D Texture Mesh
idx_draw_mesh = content.find('// 2. Render Elastic Deformed 3D Texture Mesh')
if idx_draw_mesh != -1:
    content = content[:idx_draw_mesh] + balloon_physics + "\n\n                " + content[idx_draw_mesh:]
    print("100% Successfully injected 2-Finger Balloon Inflation Physics into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Multi-Touch Balloon Inflation Engine in index.html!")
