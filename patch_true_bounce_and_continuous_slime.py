import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build True 2-3 Spring Bounce on Release & Continuous Flowing Liquid Slime Engine
perfect_bounce_slime_code = """                // --- 1. True 2-3 Spring Bounce on Release & Continuous Liquid Slime Engine ---
                let currentMode = (typeof activeTextureMode !== 'undefined') ? activeTextureMode : 'jelly';

                // Apply/Remove 3D Liquid Shader Filter on Canvas for Slime Mode
                if (currentMode === 'slime') {
                    canvas.style.filter = "url('#slime-liquid-gooey') drop-shadow(0 12px 24px rgba(0,210,140,0.30))";
                } else {
                    canvas.style.filter = "drop-shadow(0 12px 28px rgba(0, 0, 0, 0.15))";
                }

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
                        // [슬라임 모드]: 멈추지 않고 찰랑이며 바닥으로 지속적으로 퍼지는 3D 액체 유체 (Continuous Liquid Gel Pool & Ripple)
                        let meltCenter = (grabbedPointIndex !== null && points[grabbedPointIndex]) ? points[grabbedPointIndex] : { ox: width/2, oy: height/2 };
                        
                        // Continuous liquid melt expansion + gentle liquid ripple wave (NO FREEZING/STOPPING!)
                        let meltGrowth = Math.min(0.85, touchTime * 0.025);
                        let liquidRipple = Math.sin(touchTime * 0.15) * 0.06 * (1.0 + meltGrowth);

                        let scaleX = 1.0 + meltGrowth + liquidRipple;
                        let scaleY = Math.max(0.48, 1.0 - meltGrowth * 0.45 + liquidRipple * 0.5);

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - meltCenter.ox;
                            let dy = p.oy - meltCenter.oy;

                            p.x = meltCenter.ox + dx * scaleX;
                            p.y = meltCenter.oy + dy * scaleY;
                        }

                        // Render Liquid Glass Shimmer Highlight & Wave Ring
                        ctx.save();
                        let lGrad = ctx.createRadialGradient(touchX, touchY, 5, touchX, touchY, width * (0.35 + meltGrowth * 0.15));
                        lGrad.addColorStop(0, 'rgba(255, 255, 255, 0.65)');
                        lGrad.addColorStop(0.5, 'rgba(180, 255, 220, 0.35)');
                        lGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                        ctx.fillStyle = lGrad;
                        ctx.beginPath();
                        ctx.arc(touchX, touchY, width * (0.35 + meltGrowth * 0.15), 0, Math.PI * 2);
                        ctx.fill();
                        ctx.restore();

                    } else if (currentMode === 'mochi') {
                        // [쫀득모찌 모드]: 찰떡처럼 쫀득하게 늘어나는 모찌
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
                            }
                        }
                    } else {
                        // [탱글젤리 모드]: 몸통 고정 + 터치 부위가 시원하게 당겨지는 탄성 젤리
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
                            }
                        }
                    }
                } else {
                    touchTime = 0;
                    // --- Real 2-3 Spring Restitution Bounce & Clean Stop Engine ---
                    let modeSpring = (currentMode === 'slime') ? 0.045 : (currentMode === 'mochi' ? 0.08 : 0.16);
                    let modeDamping = (currentMode === 'slime') ? 0.86 : (currentMode === 'mochi' ? 0.85 : 0.80);

                    for (let i = 0; i < points.length; i++) {
                        // Spring force pulling back to (ox, oy)
                        let fx = (points[i].ox - points[i].x) * modeSpring;
                        let fy = (points[i].oy - points[i].y) * modeSpring;
                        
                        // Apply spring acceleration to velocity
                        points[i].vx = (points[i].vx + fx) * modeDamping;
                        points[i].vy = (points[i].vy + fy) * modeDamping;
                        
                        // Update position
                        points[i].x += points[i].vx;
                        points[i].y += points[i].vy;

                        // Lock cleanly to home origin after 2-3 bounces complete!
                        let distFromHome = Math.hypot(points[i].x - points[i].ox, points[i].y - points[i].oy);
                        let velSpeed = Math.hypot(points[i].vx, points[i].vy);
                        if (distFromHome < 0.8 && velSpeed < 0.25) {
                            points[i].x = points[i].ox;
                            points[i].y = points[i].oy;
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
    content = content[:idx_t_start] + perfect_bounce_slime_code + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Injected True 2-3 Bounce & Continuous Slime Engine into draw()!")

# Update touchend & mouseup to preserve spring release velocity impulse!
release_impulse_code = """        const releaseGrab = (quiet = false) => {
            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                // Give spring release velocity impulse to initiate 2-3 bounces!
                let impulse = 0.45;
                points[grabbedPointIndex].vx = (touchX - lastTouchX) * impulse;
                points[grabbedPointIndex].vy = (touchY - lastTouchY) * impulse;
            }
            grabbedPointIndex = null;
            isTouching = false;
            if (!quiet) {
                playReleaseSound();
            }
        };"""

idx_rg = content.find('const releaseGrab =')
if idx_rg != -1:
    idx_rg_end = content.find('};', idx_rg) + 2
    content = content[:idx_rg] + release_impulse_code + content[idx_rg_end:]
    print("100% SUCCESS: Updated releaseGrab with spring release velocity impulse!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied True 2-3 Bounce & Continuous Slime Engine in index.html!")
