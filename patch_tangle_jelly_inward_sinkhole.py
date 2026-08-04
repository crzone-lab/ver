import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Inward 3D Sinkhole Tangle Jelly Engine (Restoring V113 Sinkhole & Shading)
jelly_sinkhole_code = """                // --- 1. Tangle Jelly Inward 3D Sinkhole & Damped Sine Bounce Engine ---
                let currentMode = (typeof activeTextureMode !== 'undefined') ? activeTextureMode : 'jelly';
                canvas.style.filter = 'drop-shadow(0 12px 28px rgba(0, 0, 0, 0.15))';

                if (isTouching) {
                    touchTime++;

                    // 2-Finger Pinch Balloon Swell
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
                        // [슬라임 모드]: 그대로 보존 (DO NOT TOUCH SLIME)
                        let meltCenter = (grabbedPointIndex !== null && points[grabbedPointIndex]) ? points[grabbedPointIndex] : { ox: width/2, oy: height/2 };
                        let meltAmount = Math.min(0.75, touchTime * 0.032);
                        let wavePulse = Math.sin(touchTime * 0.18) * 0.05 * (1.0 + meltAmount);

                        let scaleX = 1.0 + meltAmount + wavePulse;
                        let scaleY = Math.max(0.50, 1.0 - meltAmount * 0.42 + wavePulse * 0.5);

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - meltCenter.ox;
                            let dy = p.oy - meltCenter.oy;

                            p.x = meltCenter.ox + dx * scaleX;
                            p.y = meltCenter.oy + dy * scaleY;
                        }

                        ctx.save();
                        let poolRadius = width * (0.35 + meltAmount * 0.15);
                        let pGrad = ctx.createRadialGradient(touchX, touchY, 5, touchX, touchY, poolRadius);
                        pGrad.addColorStop(0, 'rgba(255, 255, 255, 0.65)');
                        pGrad.addColorStop(0.5, 'rgba(200, 255, 230, 0.32)');
                        pGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                        ctx.fillStyle = pGrad;
                        ctx.beginPath();
                        ctx.arc(touchX, touchY, poolRadius, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.restore();

                    } else if (currentMode === 'mochi') {
                        // [쫀득모찌 모드]: 찰떡처럼 쫀득하게 당기기
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

                                p.lastDx = p.x - p.ox;
                                p.lastDy = p.y - p.oy;
                            }
                        }
                    } else {
                        // [탱글젤리 모드]: 누르면 속으로 쏙 내려가는 깊은 3D 함몰 (Sinkhole) & 당기기
                        let dragFromStart = (typeof touchStartX !== 'undefined' && touchStartX > 0) ? Math.hypot(touchX - touchStartX, touchY - touchStartY) : 0;

                        if (dragFromStart < 14.0) {
                            // 1. 누름/홀드 상태 (dragFromStart < 14px): 터치 위치 중심 깊은 3D 함몰 (Inward 3D Sinkhole)
                            let sinkRadius = width * 0.45;
                            let sinkDepth = Math.min(58.0, 22.0 + touchTime * 1.8);

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
                                    p.x = p.ox - nx * weight * sinkDepth * 0.40;
                                    p.y = p.oy - ny * weight * sinkDepth * 0.40;

                                    p.lastDx = p.x - p.ox;
                                    p.lastDy = p.y - p.oy;
                                }
                            }

                            // Render 3D Whirlpool Sinkhole Shadow & Depressed Inner Ring (함몰 그림자 음영)
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
                            // 2. 드래그/당기기 상태 (dragFromStart >= 14px): 터치 부위가 길고 쫀쫀하게 당겨짐
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

                                    p.lastDx = p.x - p.ox;
                                    p.lastDy = p.y - p.oy;
                                }
                            }
                        }
                    }
                } else {
                    // --- Release Bounce Mode (Slow, Rhythmic 2-3 Bounces over 1.05s) ---
                    if (touchTime > 0) {
                        releaseTime = 0;
                        touchTime = 0;
                    }

                    releaseTime++;

                    let tSec = releaseTime * 0.016;

                    if (releaseTime <= 65) {
                        let envelope = Math.exp(-2.2 * tSec);
                        let oscillation = Math.cos(7.2 * tSec);
                        let bounceFactor = envelope * oscillation;

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let baseDx = (p.lastDx !== undefined) ? p.lastDx : (p.x - p.ox);
                            let baseDy = (p.lastDy !== undefined) ? p.lastDy : (p.y - p.oy);

                            p.x = p.ox + baseDx * bounceFactor;
                            p.y = p.oy + baseDy * bounceFactor;
                        }
                    } else {
                        for (let i = 0; i < points.length; i++) {
                            points[i].x = points[i].ox;
                            points[i].y = points[i].oy;
                            points[i].vx = 0;
                            points[i].vy = 0;
                            points[i].lastDx = 0;
                            points[i].lastDy = 0;
                        }
                    }
                }"""

# Locate and replace active touch physics inside draw()
idx_draw_func = content.find('function draw()')
idx_t_start = content.find('// --- 1.', idx_draw_func)
if idx_t_start == -1: idx_t_start = content.find('if (isTouching)', idx_draw_func)
idx_t_end = content.find('// 2. Solve internal springs every frame', idx_t_start)

if idx_draw_func != -1 and idx_t_start != -1 and idx_t_end != -1:
    content = content[:idx_t_start] + jelly_sinkhole_code + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Injected Inward 3D Sinkhole Tangle Jelly Engine into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Inward 3D Sinkhole Tangle Jelly Engine in index.html!")
