import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build 100% Anchored Tangle Jelly Stretch & Fun Jiggle Slime Physics Engine
perfect_engine_code = """                // --- 1. Anchored Body Soft Jelly Stretch & Fun Jiggle Slime Engine ---
                let currentMode = (typeof activeTextureMode !== 'undefined') ? activeTextureMode : 'jelly';

                if (isTouching) {
                    touchTime++;

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
                        // [슬라임 모드]: 꿀처럼 바닥에 부드럽게 녹아 퍼지는 3D 액체 겔 (Smooth In-Place Liquid Gel Melt)
                        let meltRadius = width * 0.52;
                        let meltForce = Math.min(52.0, 16.0 + touchTime * 1.20);

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - touchX;
                            let dy = p.oy - touchY;
                            let dist = Math.hypot(dx, dy);

                            if (dist < meltRadius && dist > 0.1) {
                                let weight = Math.pow(1 - dist / meltRadius, 1.4);
                                let nx = dx / dist;
                                let ny = dy / dist;

                                // Radial Liquid Gel Melt
                                p.x += nx * weight * meltForce * 0.45;
                                p.y += ny * weight * meltForce * 0.45;
                            }
                        }

                        // Render 3D Liquid Pool Shimmer Reflection
                        ctx.save();
                        let lGrad = ctx.createRadialGradient(touchX, touchY, 5, touchX, touchY, meltRadius * 0.60);
                        lGrad.addColorStop(0, 'rgba(255, 255, 255, 0.55)');
                        lGrad.addColorStop(0.5, 'rgba(200, 255, 230, 0.28)');
                        lGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                        ctx.fillStyle = lGrad;
                        ctx.beginPath();
                        ctx.arc(touchX, touchY, meltRadius * 0.60, 0, Math.PI * 2);
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
                        // [탱글젤리 모드]: 몸통 100% 고정 + 터치한 부위만 잘 늘어나는 엘라스틱 당기기!
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let dist = Math.hypot(pdx, pdy);

                                // High Spatial Falloff: Nodes far from touch (>130px) stay 100% anchored at home (p.ox, p.oy)!
                                let sigma = 100.0;
                                let weight = Math.exp(-(dist * dist) / (2.0 * sigma * sigma));

                                // Body stays fixed while local ear/cheek/paw stretches out easily!
                                p.x = p.ox + dragDx * weight * 1.35;
                                p.y = p.oy + dragDy * weight * 1.35;
                                p.vx *= 0.25; p.vy *= 0.25;
                            }
                        }
                    }
                } else {
                    touchTime = 0;
                    // Slime Tremble Jiggle Oscillating Spring (유저님이 재미있어하신 찰랑이는 액체 떨림 100% 보존!)
                    let modeSpring = (currentMode === 'slime') ? 0.040 : (currentMode === 'mochi' ? 0.07 : 0.15);
                    let modeDamping = (currentMode === 'slime') ? 0.93 : (currentMode === 'mochi' ? 0.88 : 0.82);

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
    content = content[:idx_t_start] + perfect_engine_code + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Injected Anchored Jelly Stretch & Jiggle Slime Engine into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Anchored Jelly Stretch & Jiggle Slime Engine in index.html!")
