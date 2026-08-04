import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Homothetic Radial Liquid Melt Slime & Long Jelly Stretch Engine
unified_liquid_engine = """                // --- 1. Unified Homothetic Liquid Melt Slime & Extended Jelly Stretch Engine ---
                let currentMode = (typeof activeTextureMode !== 'undefined') ? activeTextureMode : 'jelly';

                if (isTouching) {
                    touchTime++;

                    // Instant Tremble Stop on Touch (터치하는 순간 액체 떨림 즉시 스톱!)
                    for (let i = 0; i < points.length; i++) {
                        points[i].vx = 0;
                        points[i].vy = 0;
                    }

                    // 2-Finger Pinch Balloon Swell (두 손가락 핀치 시 가운데 풍선 부풀어 오름)
                    if (activeTouchList && activeTouchList.length >= 2) {
                        let t1 = activeTouchList[0];
                        let t2 = activeTouchList[1];
                        let midX = (t1.x + t2.x) / 2;
                        let midY = (t1.y + t2.y) / 2;
                        let fDist = Math.hypot(t2.x - t1.x, t2.y - t1.y);

                        let swellRadius = Math.max(width * 0.42, fDist * 1.35);
                        let bulgeForce = Math.min(50.0, Math.max(18.0, (300.0 - fDist) * 0.38));

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - midX;
                            let dy = p.oy - midY;
                            let dist = Math.hypot(dx, dy);

                            if (dist < swellRadius && dist > 1.0) {
                                let weight = Math.pow(1 - dist / swellRadius, 1.5);
                                let nx = dx / dist;
                                let ny = dy / dist;

                                p.x += nx * weight * bulgeForce * 0.42;
                                p.y += ny * weight * bulgeForce * 0.42;
                            }
                        }

                        // Render 3D swelling balloon specular light reflection
                        ctx.save();
                        let bGrad = ctx.createRadialGradient(midX, midY, 5, midX, midY, swellRadius * 0.70);
                        bGrad.addColorStop(0, 'rgba(255, 255, 255, 0.78)');
                        bGrad.addColorStop(0.35, 'rgba(255, 245, 210, 0.42)');
                        bGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                        ctx.fillStyle = bGrad;
                        ctx.beginPath();
                        ctx.arc(midX, midY, swellRadius * 0.70, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.restore();
                    } else if (currentMode === 'slime') {
                        // [슬라임 모드]: 전체가 1개의 완벽한 3D 동질 액체로 균일 팽창/녹음 (Homothetic Liquid Pool - 깨짐/잘림 0%)
                        let meltCenter = (grabbedPointIndex !== null && points[grabbedPointIndex]) ? points[grabbedPointIndex] : { ox: width/2, oy: height/2 };
                        let meltScale = Math.min(1.58, 1.0 + touchTime * 0.022); // Smooth uniform liquid expansion

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - meltCenter.ox;
                            let dy = p.oy - meltCenter.oy;

                            // Homothetic 3D Liquid Melting: Scales all vertices uniformly outward as 1 solid liquid pool
                            p.x = meltCenter.ox + dx * meltScale;
                            p.y = meltCenter.oy + dy * meltScale;
                        }

                        // Render Top-Down 3D Liquid Pool Shimmer Reflection
                        ctx.save();
                        let lGrad = ctx.createRadialGradient(touchX, touchY, 5, touchX, touchY, width * 0.35);
                        lGrad.addColorStop(0, 'rgba(255, 255, 255, 0.55)');
                        lGrad.addColorStop(0.5, 'rgba(200, 255, 230, 0.28)');
                        lGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                        ctx.fillStyle = lGrad;
                        ctx.beginPath();
                        ctx.arc(touchX, touchY, width * 0.35, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.restore();

                    } else if (currentMode === 'mochi') {
                        // [쫀득모찌 모드]: 찰떡처럼 쫀득하게 천천히 늘어나는 플라스틱 모찌
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let distSq = pdx * pdx + pdy * pdy;
                                let weight = Math.exp(-distSq / (150.0 * 150.0));

                                p.x = p.ox + dragDx * weight * 0.92;
                                p.y = p.oy + dragDy * weight * 0.92;
                                p.vx *= 0.12; p.vy *= 0.12;
                            }
                        }
                    } else {
                        // [탱글젤리 모드]: 다른 부분 건드리지 않고 훨씬 더 길고 부드럽게 잘 늘어남 (Long Stretch: 220px Range)
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            let dragDist = Math.hypot(dragDx, dragDy);
                            let maxStretch = 220.0; // Increased to 220px for long elastic stretch!
                            if (dragDist > maxStretch) {
                                dragDx = (dragDx / dragDist) * maxStretch;
                                dragDy = (dragDy / dragDist) * maxStretch;
                            }

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let distSq = pdx * pdx + pdy * pdy;
                                let weight = Math.exp(-distSq / (280.0 * 280.0)); // Wide long stretch gradient!

                                p.x = p.ox + dragDx * weight;
                                p.y = p.oy + dragDy * weight;
                                p.vx *= 0.28; p.vy *= 0.28;
                            }
                        }
                    }
                } else {
                    // Slime Tremble Auto-Stop (일정 시간 떠근 후 자동 스톱 & 안정화)
                    let modeSpring = (currentMode === 'slime') ? 0.055 : (currentMode === 'mochi' ? 0.07 : 0.15);
                    let modeDamping = (currentMode === 'slime') ? 0.88 : (currentMode === 'mochi' ? 0.88 : 0.82);

                    if (currentMode === 'slime' && touchTime > 70) {
                        // Auto-stop trembling after ~1.1 seconds of release
                        modeDamping = 0.65; // High damping to freeze trembling cleanly!
                    }

                    for (let i = 0; i < points.length; i++) {
                        let fx = (points[i].ox - points[i].x) * modeSpring;
                        let fy = (points[i].oy - points[i].y) * modeSpring;
                        points[i].vx = (points[i].vx + fx) * modeDamping;
                        points[i].vy = (points[i].vy + fy) * modeDamping;
                        points[i].x += points[i].vx;
                        points[i].y += points[i].vy;

                        // Auto-stop trembling velocity threshold
                        if (currentMode === 'slime' && Math.hypot(points[i].vx, points[i].vy) < 0.08) {
                            points[i].vx = 0;
                            points[i].vy = 0;
                        }
                    }
                }"""

# Locate and replace active touch physics inside draw()
idx_draw_func = content.find('function draw()')
idx_t_start = content.find('// --- 1.', idx_draw_func)
if idx_t_start == -1: idx_t_start = content.find('if (isTouching)', idx_draw_func)
idx_t_end = content.find('// 2. Solve internal springs every frame', idx_t_start)

if idx_draw_func != -1 and idx_t_start != -1 and idx_t_end != -1:
    content = content[:idx_t_start] + unified_liquid_engine + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Injected Unified Liquid Melt Slime & Long Jelly Stretch Engine into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Unified Liquid Melt Slime in index.html!")
