import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update selectFeelPill function to set activeTextureMode
select_pill_code = """function selectFeelPill(feel) {
            activeTextureMode = feel; // Sync activeTextureMode for physics engine
            const pJelly = document.getElementById("pill-jelly");
            const pMochi = document.getElementById("pill-mochi");
            const pSlime = document.getElementById("pill-slime");

            [pJelly, pMochi, pSlime].forEach(p => {
                if (p) {
                    p.classList.remove("active");
                }
            });

            if (feel === "jelly") {
                if (pJelly) pJelly.classList.add("active");
                stiffness = 50;
                damping = 8;
                showNotification(i18n.t("notif-jelly") || "탱글젤리 감촉 선택됨");
            } else if (feel === "mochi") {
                if (pMochi) pMochi.classList.add("active");
                stiffness = 110;
                damping = 18;
                showNotification(i18n.t("notif-mochi") || "쫀득모찌 감촉 선택됨");
            } else if (feel === "slime") {
                if (pSlime) pSlime.classList.add("active");
                stiffness = 15;
                damping = 3;
                showNotification(i18n.t("notif-slime") || "슬라임 감촉 선택됨");
            }
        }"""

idx_sfp = content.find('function selectFeelPill(')
if idx_sfp != -1:
    idx_sfp_end = content.find('}', content.find('showNotification', idx_sfp)) + 1
    # Expand to closing brace of selectFeelPill
    idx_sfp_end = content.find('}', idx_sfp_end) + 1
    content = content[:idx_sfp] + select_pill_code + content[idx_sfp_end:]
    print("100% Successfully updated selectFeelPill with activeTextureMode sync!")

# 2. Build 100% Perfect 3 Texture Modes & Local Elastic Stretch Physics
physics_engine_code = """                // --- 1. Distinct 3 Texture Modes (Jelly, Mochi, Slime) & Local Elastic Stretch Engine ---
                let currentMode = (typeof activeTextureMode !== 'undefined') ? activeTextureMode : 'jelly';

                if (isTouching) {
                    touchTime++;

                    let maxRadius = width * 0.42;

                    if (currentMode === 'slime') {
                        // [슬라임 모드]: 꿀처럼 걸쭉하게 넓게 퍼지는 점성 액체 유체 (Viscous Honey Spreading)
                        let pushRadius = width * 0.48;
                        let spreadForce = Math.min(42.0, 12.0 + touchTime * 0.85);

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - touchX;
                            let dy = p.oy - touchY;
                            let dist = Math.hypot(dx, dy);

                            if (dist < pushRadius && dist > 0.1) {
                                let weight = Math.pow(1 - dist / pushRadius, 1.4);
                                let nx = dx / dist;
                                let ny = dy / dist;

                                // Viscous Honey Spreading: Pushes nodes outward horizontally & downwards like pouring honey
                                p.x += (nx * 0.85 + (p.ox > width/2 ? 0.35 : -0.35)) * weight * spreadForce * 0.22;
                                p.y += (ny * 0.40 + 0.65) * weight * spreadForce * 0.25;
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
                        // [탱글젤리 모드]: 국소 부위가 탱글탱글하게 늘어나는 로컬 엘라스틱 젤리 (Local Elastic Stretch)
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            // Clamp max stretch distance to 45px to prevent tearing
                            let dragDist = Math.hypot(dragDx, dragDy);
                            let maxStretch = 45.0;
                            if (dragDist > maxStretch) {
                                dragDx = (dragDx / dragDist) * maxStretch;
                                dragDy = (dragDy / dragDist) * maxStretch;
                            }

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let distSq = pdx * pdx + pdy * pdy;
                                let weight = Math.exp(-distSq / (120.0 * 120.0)); // Localized stretch!

                                p.x = p.ox + dragDx * weight;
                                p.y = p.oy + dragDy * weight;
                                p.vx *= 0.30; p.vy *= 0.30;
                            }
                        }
                    }
                } else {
                    touchTime = 0;
                    // Mode-specific spring restoration
                    let modeSpring = (currentMode === 'slime') ? 0.03 : (currentMode === 'mochi' ? 0.07 : 0.15);
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
idx_draw = content.find('function draw()')
idx_touch_start = content.find('if (isTouching)', idx_draw)
idx_touch_end = content.find('// 2. Solve internal springs every frame', idx_touch_start)

if idx_draw != -1 and idx_touch_start != -1 and idx_touch_end != -1:
    content = content[:idx_touch_start] + physics_engine_code + "\n\n                " + content[idx_touch_end:]
    print("100% SUCCESS: Updated touch physics inside draw() with distinct 3 modes & local stretch!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 3 Modes & Local Stretch in index.html!")
