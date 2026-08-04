import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Soft Tangle Jelly with Inward Dimple & Single-Mass Gravity Gel Slime Engine
soft_physics_code = """                // --- 1. Soft Tangle Jelly (Inward Dimple + Soft Drag) & Single-Mass Gravity Gel Slime ---
                let currentMode = (typeof activeTextureMode !== 'undefined') ? activeTextureMode : 'jelly';

                if (isTouching) {
                    touchTime++;

                    let maxRadius = width * 0.48;

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
                        // [슬라임 모드]: 100% 1개 단일 덩어리 보존 (잘림/찢어짐 0%) + 중력 기반 바닥 겔 퍼짐 (Gravity Gel Pooling)
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

                                // Single solid mass gravity pooling: Gel spreads horizontally and settles downward under gravity
                                p.x += nx * weight * gravityForce * 0.48; // Horizontal gel expansion to left & right
                                p.y += weight * gravityForce * 0.32;      // Gravity gel settling towards floor
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
                        // [탱글젤리 모드]: 연하고 말랑말랑한 젤리 + 누르면 움푹 들어가는 3D 함몰 (Inward Dimple + Soft Drag)
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;
                            let dragDist = Math.hypot(dragDx, dragDy);

                            if (dragDist < 6.0) {
                                // 1. 누름 상태 (Drag < 6px): 터치 지점 중심으로 움푹 들어가는 3D 함몰 효과 (Inward Dimple)
                                let dimpleRadius = width * 0.38;
                                let dimpleDepth = 26.0;

                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let dx = p.ox - touchX;
                                    let dy = p.oy - touchY;
                                    let dist = Math.hypot(dx, dy);

                                    if (dist < dimpleRadius && dist > 0.1) {
                                        let weight = Math.pow(1 - dist / dimpleRadius, 1.6);
                                        let nx = dx / dist;
                                        let ny = dy / dist;

                                        // Inward squish & dimple depression
                                        p.x -= nx * weight * dimpleDepth * 0.30;
                                        p.y -= ny * weight * dimpleDepth * 0.30;
                                    }
                                }

                                // Render concave 3D dimple inner shadow ring
                                ctx.save();
                                let dGrad = ctx.createRadialGradient(touchX, touchY, 2, touchX, touchY, dimpleRadius * 0.55);
                                dGrad.addColorStop(0, 'rgba(0, 0, 0, 0.28)');
                                dGrad.addColorStop(0.5, 'rgba(0, 0, 0, 0.10)');
                                dGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                                ctx.fillStyle = dGrad;
                                ctx.beginPath();
                                ctx.arc(touchX, touchY, dimpleRadius * 0.55, 0, Math.PI * 2);
                                ctx.fill();
                                ctx.restore();

                            } else {
                                // 2. 당기기/밀기 상태 (Drag >= 6px): 매우 연하고 말랑말랑하게 쭉 늘어남 (Soft Flexible Stretch: 120px Range)
                                let maxStretch = 120.0; // Soft & long stretch range!
                                if (dragDist > maxStretch) {
                                    dragDx = (dragDx / dragDist) * maxStretch;
                                    dragDy = (dragDy / dragDist) * maxStretch;
                                }

                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let pdx = p.ox - gNode.ox;
                                    let pdy = p.oy - gNode.oy;
                                    let distSq = pdx * pdx + pdy * pdy;
                                    let weight = Math.exp(-distSq / (220.0 * 220.0)); // Soft wide influence

                                    p.x = p.ox + dragDx * weight * 1.15; // Extra soft responsiveness
                                    p.y = p.oy + dragDy * weight * 1.15;
                                    p.vx *= 0.35; p.vy *= 0.35;
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
    content = content[:idx_t_start] + soft_physics_code + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Injected Soft Jelly Dimple & Single-Mass Gravity Gel Slime into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Soft Jelly Dimple & Gravity Gel Slime in index.html!")
