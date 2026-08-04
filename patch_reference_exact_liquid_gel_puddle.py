import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Reference-Exact Translucent Golden Liquid Gel Puddle Slime Engine
reference_slime_code = """                // --- 1. Reference-Exact Translucent Gel Puddle Slime & Spring Bounce Engine ---
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
                        // [슬라임 모드]: 레퍼런스 이미지 그대로! 누르면 투명 젤리 웅덩이가 사방으로 바닥에 번지는 3D 겔 (Translucent Liquid Gel Puddle)
                        let meltCenter = (grabbedPointIndex !== null && points[grabbedPointIndex]) ? points[grabbedPointIndex] : { ox: width/2, oy: height/2 };
                        let meltProgress = Math.min(1.0, touchTime * 0.045);

                        // 1. Render Outer Translucent Glass/Golden Liquid Gel Pool Outline (레퍼런스 이미지 젤리 웅덩이 테두리)
                        ctx.save();
                        let poolRadiusX = width * (0.36 + meltProgress * 0.16);
                        let poolRadiusY = height * (0.36 + meltProgress * 0.12);

                        let pGrad = ctx.createRadialGradient(touchX, touchY, poolRadiusX * 0.2, touchX, touchY, poolRadiusX);
                        pGrad.addColorStop(0, 'rgba(255, 230, 140, 0.45)');
                        pGrad.addColorStop(0.7, 'rgba(255, 200, 90, 0.25)');
                        pGrad.addColorStop(0.95, 'rgba(255, 255, 255, 0.75)');
                        pGrad.addColorStop(1, 'rgba(255, 220, 120, 0.10)');

                        ctx.fillStyle = pGrad;
                        ctx.strokeStyle = 'rgba(255, 255, 255, 0.85)';
                        ctx.lineWidth = 3;

                        ctx.beginPath();
                        ctx.ellipse(touchX, touchY, poolRadiusX, poolRadiusY, 0, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.stroke();
                        ctx.restore();

                        // 2. Homothetic Liquid Flattening (내부 캐릭터가 젤리 웅덩이에 매끈하게 압착)
                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - meltCenter.ox;
                            let dy = p.oy - meltCenter.oy;

                            let scaleX = 1.0 + 0.38 * meltProgress;
                            let scaleY = 1.0 - 0.22 * meltProgress;

                            p.x = meltCenter.ox + dx * scaleX;
                            p.y = meltCenter.oy + dy * scaleY;
                        }

                    } else if (currentMode === 'mochi') {
                        // [쫀득모찌 모드]: 찰떡처럼 쫀득하게 늘어났다가 몇 번 찰랑거리며 복원되는 모찌
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
                        // [탱글젤리 모드]: 당겼다 놓으면 몇 번 튕기면서 안착하는 탄성 젤리
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let dist = Math.hypot(pdx, pdy);

                                let sigma = 100.0;
                                let weight = Math.exp(-(dist * dist) / (2.0 * sigma * sigma));

                                p.x = p.ox + dragDx * weight * 1.35;
                                p.y = p.oy + dragDy * weight * 1.35;
                                p.vx *= 0.25; p.vy *= 0.25;
                            }
                        }
                    }
                } else {
                    touchTime = 0;
                    // Mode-Specific Spring Restitution (놓았을 때 중력/반발력으로 몇 번 튕기며 안착!)
                    let modeSpring = (currentMode === 'slime') ? 0.045 : (currentMode === 'mochi' ? 0.09 : 0.18);
                    let modeDamping = (currentMode === 'slime') ? 0.92 : (currentMode === 'mochi' ? 0.85 : 0.78);

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
    content = content[:idx_t_start] + reference_slime_code + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Injected Reference-Exact Liquid Gel Puddle Slime Engine into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Reference-Exact Liquid Gel Puddle Slime in index.html!")
