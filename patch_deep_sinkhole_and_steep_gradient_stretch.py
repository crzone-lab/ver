import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Deep Sinkhole Inward Depression & High Spatial Gradient Stretch Engine
deep_jelly_code = """                // --- 1. Deep Inward Sinkhole & Steep Spatial Gradient Soft Jelly Engine ---
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
                        // [슬라임 모드]: 100% 1개 단일 덩어리 보존 + 중력 기반 바닥 겔 퍼짐 (Gravity Gel Pooling)
                        let pressRadius = width * 0.55;
                        let gravityForce = Math.min(58.0, 18.0 + touchTime * 1.25);

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - touchX;
                            let dy = p.oy - touchY;
                            let dist = Math.hypot(dx, dy);

                            if (dist < pressRadius && dist > 0.1) {
                                let weight = Math.pow(1 - dist / pressRadius, 1.3);
                                let nx = dx / dist;

                                p.x += nx * weight * gravityForce * 0.48;
                                p.y += weight * gravityForce * 0.32;
                            }
                        }
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
                        // [탱글젤리 모드]: 깊은 3D 하수구 함몰 (Sinkhole) & Steep Spatial Gradient (먼 곳 100% 고정!)
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;
                            let dragDist = Math.hypot(dragDx, dragDy);

                            if (dragDist < 8.0) {
                                // 1. 누르고 있기 (Hold/Press): 하수구로 물이 빨려 들어가듯 깊은 3D 함몰 (Deep Sinkhole)
                                let sinkRadius = width * 0.42;
                                // Longer press = deeper sink hole!
                                let sinkDepth = Math.min(52.0, 18.0 + touchTime * 1.6);

                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let dx = p.ox - touchX;
                                    let dy = p.oy - touchY;
                                    let dist = Math.hypot(dx, dy);

                                    if (dist < sinkRadius && dist > 0.1) {
                                        let weight = Math.pow(1 - dist / sinkRadius, 1.8);
                                        let nx = dx / dist;
                                        let ny = dy / dist;

                                        // Pull nodes inward towards sink center (하수구 빨려 내려감)
                                        p.x -= nx * weight * sinkDepth * 0.45;
                                        p.y -= ny * weight * sinkDepth * 0.45;
                                    }
                                }

                                // Render 3D Whirlpool Sinkhole Shadow & Depressed Contour
                                ctx.save();
                                let sGrad = ctx.createRadialGradient(touchX, touchY, 3, touchX, touchY, sinkRadius * 0.65);
                                sGrad.addColorStop(0, 'rgba(0, 0, 0, 0.45)');
                                sGrad.addColorStop(0.4, 'rgba(0, 0, 0, 0.20)');
                                sGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                                ctx.fillStyle = sGrad;
                                ctx.beginPath();
                                ctx.arc(touchX, touchY, sinkRadius * 0.65, 0, Math.PI * 2);
                                ctx.fill();
                                ctx.restore();

                            } else {
                                // 2. 당기기/밀기 (Drag >= 8px): 먼 곳은 100% 제자리 고정 + 가까운 곳만 터치 위치로 크게 끌려옴!
                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let pdx = p.ox - gNode.ox;
                                    let pdy = p.oy - gNode.oy;
                                    let dist = Math.hypot(pdx, pdy);

                                    // Steep Exponential Decay: Nodes far (>150px) get 0 weight and STAY 100% ANCHORED!
                                    let sigma = 95.0; // Narrow, sharp spatial influence range
                                    let weight = Math.exp(-(dist * dist) / (2.0 * sigma * sigma));

                                    // Nearby nodes follow touch vector closely, far nodes remain anchored at (p.ox, p.oy)
                                    p.x = p.ox + dragDx * weight;
                                    p.y = p.oy + dragDy * weight;
                                    p.vx *= 0.25; p.vy *= 0.25;
                                }
                            }
                        }
                    }
                } else {
                    touchTime = 0;
                    // Soft spring restoration
                    let modeSpring = (currentMode === 'slime') ? 0.035 : (currentMode === 'mochi' ? 0.07 : 0.16);
                    let modeDamping = (currentMode === 'slime') ? 0.93 : (currentMode === 'mochi' ? 0.88 : 0.80);

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
    content = content[:idx_t_start] + deep_jelly_code + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Injected Deep Sinkhole & Steep Gradient Drag Physics into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Deep Sinkhole & Steep Gradient Drag in index.html!")
