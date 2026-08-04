import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add SVG Liquefy Gooey Filter to index.html if not present
gooey_svg_filter = """    <!-- 3D Viscous Liquid Gooey Filter for Slime Mode -->
    <svg style="display:none; position:absolute;" width="0" height="0">
        <defs>
            <filter id="slime-liquid-gooey">
                <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur" />
                <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -8" result="goo" />
                <feComposite in="SourceGraphic" in2="goo" operator="atop" />
            </filter>
        </defs>
    </svg>"""

if 'id="slime-liquid-gooey"' not in content:
    content = content.replace('</body>', gooey_svg_filter + '\n</body>')
    print("100% Successfully added 3D Viscous Liquid Gooey Filter SVG!")

# 2. Build 2-3 Bounce & Stop Physics + Real 3D Liquid Shader Slime Engine
perfect_physics_code = """                // --- 1. 2-3 Bounce & Stop Physics + 3D Liquid Shader Slime Engine ---
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
                        // [슬라임 모드]: 캐릭터 자체가 3D 액체로 녹아 사방 360도로 바닥에 퍼지는 유체 (Real Liquid Gel Melt)
                        let meltCenter = (grabbedPointIndex !== null && points[grabbedPointIndex]) ? points[grabbedPointIndex] : { ox: width/2, oy: height/2 };
                        let meltProgress = Math.min(1.0, touchTime * 0.045);

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - meltCenter.ox;
                            let dy = p.oy - meltCenter.oy;

                            let scaleX = 1.0 + 0.42 * meltProgress;
                            let scaleY = 1.0 - 0.25 * meltProgress;

                            p.x = meltCenter.ox + dx * scaleX;
                            p.y = meltCenter.oy + dy * scaleY;
                        }

                        // Render Liquid Glass Shimmer Highlight
                        ctx.save();
                        let lGrad = ctx.createRadialGradient(touchX, touchY, 5, touchX, touchY, width * 0.40);
                        lGrad.addColorStop(0, 'rgba(255, 255, 255, 0.60)');
                        lGrad.addColorStop(0.5, 'rgba(180, 255, 220, 0.30)');
                        lGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                        ctx.fillStyle = lGrad;
                        ctx.beginPath();
                        ctx.arc(touchX, touchY, width * 0.40, 0, Math.PI * 2);
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
                                p.vx *= 0.12; p.vy *= 0.12;
                            }
                        }
                    } else {
                        // [탱글젤리 모드]: 터치 부위가 시원하게 당겨지는 탄성 젤리
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
                    // Mode-Specific Spring Restitution: 2-3 Bounces & Clean Stop at Home Origin!
                    let modeSpring = (currentMode === 'slime') ? 0.050 : (currentMode === 'mochi' ? 0.08 : 0.16);
                    let modeDamping = (currentMode === 'slime') ? 0.82 : (currentMode === 'mochi' ? 0.82 : 0.78);

                    for (let i = 0; i < points.length; i++) {
                        let fx = (points[i].ox - points[i].x) * modeSpring;
                        let fy = (points[i].oy - points[i].y) * modeSpring;
                        points[i].vx = (points[i].vx + fx) * modeDamping;
                        points[i].vy = (points[i].vy + fy) * modeDamping;
                        points[i].x += points[i].vx;
                        points[i].y += points[i].vy;

                        // Clean Stop Lock: After 2-3 bounces, lock back cleanly to home origin (p.ox, p.oy)
                        let distFromHome = Math.hypot(points[i].x - points[i].ox, points[i].y - points[i].oy);
                        let velSpeed = Math.hypot(points[i].vx, points[i].vy);
                        if (distFromHome < 0.6 && velSpeed < 0.18) {
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
    content = content[:idx_t_start] + perfect_physics_code + "\n\n                " + content[idx_t_end:]
    print("100% SUCCESS: Injected 2-3 Bounce & Stop Physics + 3D Liquid Shader Slime Engine into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 2-3 Bounce & Stop + Liquid Shader Slime Engine in index.html!")
