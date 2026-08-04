import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build 100% Tangle Jelly Long Elastic Stretch & In-Place Honey Slime Spreading Engine
perfect_jelly_slime_code = """                // --- 1. Distinct 3 Texture Modes (Jelly, Mochi, Slime) & Multi-Touch Balloon Engine ---
                let currentMode = (typeof activeTextureMode !== 'undefined') ? activeTextureMode : 'jelly';

                if (isTouching) {
                    touchTime++;

                    let maxRadius = width * 0.45;

                    // 2-Finger Pinch Balloon Swell (두 손가락 꼭 집으면 가운데 풍선 부풀어 오름)
                    if (activeTouchList && activeTouchList.length >= 2) {
                        let t1 = activeTouchList[0];
                        let t2 = activeTouchList[1];
                        let midX = (t1.x + t2.x) / 2;
                        let midY = (t1.y + t2.y) / 2;
                        let fDist = Math.hypot(t2.x - t1.x, t2.y - t1.y);

                        let swellRadius = Math.max(width * 0.40, fDist * 1.3);
                        let bulgeForce = Math.min(48.0, Math.max(16.0, (300.0 - fDist) * 0.35));

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - midX;
                            let dy = p.oy - midY;
                            let dist = Math.hypot(dx, dy);

                            if (dist < swellRadius && dist > 1.0) {
                                let weight = Math.pow(1 - dist / swellRadius, 1.5);
                                let nx = dx / dist;
                                let ny = dy / dist;

                                p.x += nx * weight * bulgeForce * 0.40;
                                p.y += ny * weight * bulgeForce * 0.40;
                            }
                        }

                        // Render 3D swelling balloon specular light reflection between the two fingers
                        ctx.save();
                        let bGrad = ctx.createRadialGradient(midX, midY, 5, midX, midY, swellRadius * 0.70);
                        bGrad.addColorStop(0, 'rgba(255, 255, 255, 0.75)');
                        bGrad.addColorStop(0.35, 'rgba(255, 245, 210, 0.40)');
                        bGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                        ctx.fillStyle = bGrad;
                        ctx.beginPath();
                        ctx.arc(midX, midY, swellRadius * 0.70, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.restore();
                    } else if (currentMode === 'slime') {
                        // [슬라임 모드]: 제자리 위치 고정 + 꿀처럼 바닥으로 찰랑하게 넓게 퍼짐 (In-Place Viscous Liquid Flatten & Radial Spread)
                        let pushRadius = width * 0.52;
                        let spreadForce = Math.min(55.0, 15.0 + touchTime * 1.1);

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - touchX;
                            let dy = p.oy - touchY;
                            let dist = Math.hypot(dx, dy);

                            if (dist < pushRadius && dist > 0.1) {
                                let weight = Math.pow(1 - dist / pushRadius, 1.3);
                                let nx = dx / dist;
                                let ny = dy / dist;

                                // ZERO downward translation! In-place horizontal liquid pool spreading & vertical flattening
                                p.x += nx * weight * spreadForce * 0.42; // Spreads horizontally outward to left & right
                                p.y += ny * weight * spreadForce * 0.18; // Flattens vertically in-place (No downward sliding!)
                            }
                        }
                    } else if (currentMode === 'mochi') {
                        // [쫀득모찌 모드]: 찰떡처럼 쫀득하게 천천히 늘어나는 모찌
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let distSq = pdx * pdx + pdy * pdy;
                                let weight = Math.exp(-distSq / (140.0 * 140.0));

                                p.x = p.ox + dragDx * weight * 0.90;
                                p.y = p.oy + dragDy * weight * 0.90;
                                p.vx *= 0.12; p.vy *= 0.12;
                            }
                        }
                    } else {
                        // [탱글젤리 모드]: 1개의 단일 3D 덩어리 보존 + 더 잘 늘어나는 정밀 탄성 (Long Elastic Stretch: 75px Range)
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            let dragDist = Math.hypot(dragDx, dragDy);
                            let maxStretch = 75.0; // Increased max stretch range to 75px for superior elasticity!
                            if (dragDist > maxStretch) {
                                dragDx = (dragDx / dragDist) * maxStretch;
                                dragDy = (dragDy / dragDist) * maxStretch;
                            }

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let distSq = pdx * pdx + pdy * pdy;
                                let weight = Math.exp(-distSq / (175.0 * 175.0)); // Smooth long spatial influence!

                                p.x = p.ox + dragDx * weight;
                                p.y = p.oy + dragDy * weight;
                                p.vx *= 0.28; p.vy *= 0.28;
                            }
                        }
                    }
                } else {
                    touchTime = 0;
                    let modeSpring = (currentMode === 'slime') ? 0.03 : (currentMode === 'mochi' ? 0.07 : 0.14);
                    let modeDamping = (currentMode === 'slime') ? 0.94 : (currentMode === 'mochi' ? 0.88 : 0.82);

                    for (let i = 0; i < points.length; i++) {
                        let fx = (points[i].ox - points[i].x) * modeSpring;
                        let fy = (points[i].oy - points[i].y) * modeSpring;
                        points[i].vx = (points[i].vx + fx) * modeDamping;
                        points[i].vy = (points[i].vy + fy) * modeDamping;
                        points[i].x += points[i].vx;
                        points[i].y += points[i].vy;
                    }
                }"""

# Locate and replace active touch physics inside draw()
idx_draw_func = content.find('function draw()')
idx_t_start = content.find('// --- 1.', idx_draw_func)
if idx_t_start == -1: idx_t_start = content.find('if (isTouching)', idx_draw_func)
idx_t_end = content.find('// 2. Solve internal springs every frame', idx_t_start)

if idx_draw_func != -1 and idx_t_start != -1 and idx_t_end != -1:
    content = content[:idx_t_start] + perfect_jelly_slime_code + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Updated touch physics in draw() for Long Elastic Jelly Stretch & In-Place Slime!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Perfect Jelly Stretch & In-Place Slime in index.html!")
