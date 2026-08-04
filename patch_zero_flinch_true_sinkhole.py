import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add touchStartX and touchStartY variables
if 'let touchStartX = 0;' not in content:
    content = content.replace('let isTouching = false;', 'let isTouching = false;\n        let touchStartX = 0, touchStartY = 0;')
    print("Added touchStartX / touchStartY variable declarations!")

# Set touchStartX & touchStartY on touchstart / mousedown
target_ts = "isTouching = true;\n            touchX = pos.x;\n            touchY = pos.y;"
replace_ts = "isTouching = true;\n            touchX = pos.x;\n            touchY = pos.y;\n            touchStartX = pos.x;\n            touchStartY = pos.y;"

if target_ts in content:
    content = content.replace(target_ts, replace_ts)
    print("Added touchStartX / touchStartY assignment in touchstart!")

# Build 100% Zero-Flinch Sinkhole & Spatial Gradient Drag Physics
sinkhole_physics = """                // --- 1. Zero-Flinch Deep Inward Sinkhole & Anchored Drag Physics Engine ---
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
                        // [탱글젤리 모드]: 움찔거림 0% + 누르면 속으로 쏙 들어가는 깊은 3D 함몰 (Deep Inward Sinkhole)
                        let dragFromStart = (typeof touchStartX !== 'undefined' && touchStartX > 0) ? Math.hypot(touchX - touchStartX, touchY - touchStartY) : 0;

                        if (dragFromStart < 14.0) {
                            // 1. 누름/홀드 상태 (dragFromStart < 14px): 움찔거림 0%! 터치 위치 중심 깊은 3D 함몰 (Sinkhole)
                            let sinkRadius = width * 0.45;
                            let sinkDepth = Math.min(58.0, 22.0 + touchTime * 1.8); // Deepens continuously with hold time!

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let dx = p.ox - touchX;
                                let dy = p.oy - touchY;
                                let dist = Math.hypot(dx, dy);

                                if (dist < sinkRadius && dist > 0.1) {
                                    let weight = Math.pow(1 - dist / sinkRadius, 1.6);
                                    let nx = dx / dist;
                                    let ny = dy / dist;

                                    // Pull nodes inward towards sinkhole center (속으로 쏙 빨려 들어감)
                                    p.x -= nx * weight * sinkDepth * 0.40;
                                    p.y -= ny * weight * sinkDepth * 0.40;
                                }
                            }

                            // Render 3D Whirlpool Sinkhole Shadow & Depressed Inner Ring
                            ctx.save();
                            let sGrad = ctx.createRadialGradient(touchX, touchY, 3, touchX, touchY, sinkRadius * 0.60);
                            sGrad.addColorStop(0, 'rgba(0, 0, 0, 0.48)');
                            sGrad.addColorStop(0.45, 'rgba(0, 0, 0, 0.22)');
                            sGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                            ctx.fillStyle = sGrad;
                            ctx.beginPath();
                            ctx.arc(touchX, touchY, sinkRadius * 0.60, 0, Math.PI * 2);
                            ctx.fill();
                            ctx.restore();

                        } else {
                            // 2. 드래그/당기기 상태 (dragFromStart >= 14px): 먼 곳 100% 고정 + 터치 부위만 크게 따라오는 로컬 당기기!
                            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                                let gNode = points[grabbedPointIndex];
                                let dragDx = touchX - touchStartX;
                                let dragDy = touchY - touchStartY;

                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let pdx = p.ox - touchStartX;
                                    let pdy = p.oy - touchStartY;
                                    let dist = Math.hypot(pdx, pdy);

                                    let sigma = 110.0;
                                    let weight = Math.exp(-(dist * dist) / (2.0 * sigma * sigma));

                                    p.x = p.ox + dragDx * weight * 1.10;
                                    p.y = p.oy + dragDy * weight * 1.10;
                                    p.vx *= 0.25; p.vy *= 0.25;
                                }
                            }
                        }
                    }
                } else {
                    touchTime = 0;
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

idx_draw_func = content.find('function draw()')
idx_t_start = content.find('// --- 1.', idx_draw_func)
if idx_t_start == -1: idx_t_start = content.find('if (isTouching)', idx_draw_func)
idx_t_end = content.find('// 2. Solve internal springs every frame', idx_t_start)

if idx_draw_func != -1 and idx_t_start != -1 and idx_t_end != -1:
    content = content[:idx_t_start] + sinkhole_physics + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Injected Zero-Flinch Sinkhole Physics into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Zero-Flinch Sinkhole Engine in index.html!")
