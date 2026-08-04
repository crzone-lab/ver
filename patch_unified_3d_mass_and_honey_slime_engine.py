import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build 100% Unified 3D Mass Physics & Viscous Honey Slime Engine
honey_slime_engine = """                // --- 1. Single Unified 3D Mass Physics & Viscous Honey Slime Engine ---
                let currentMode = (typeof activeTextureMode !== 'undefined') ? activeTextureMode : 'jelly';

                if (isTouching) {
                    touchTime++;

                    let maxRadius = width * 0.45;
                    let sigma = maxRadius / 2.0;

                    if (currentMode === 'slime') {
                        // [슬라임 모드]: 꿀처럼 걸쭉하게 넓게 퍼지는 점성 액체 유체 (Viscous Honey Liquid Spreading)
                        let pushRadius = width * 0.50;
                        let spreadForce = Math.min(48.0, 15.0 + touchTime * 0.85);

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
                                p.x += (nx * 0.85 + (p.ox > width/2 ? 0.3 : -0.3)) * weight * spreadForce * 0.18;
                                p.y += (ny * 0.40 + 0.65) * weight * spreadForce * 0.22; // Flows downward & spreads outwards
                            }
                        }
                    } else if (currentMode === 'mochi') {
                        # [쫀득모찌 모드]: 찰떡처럼 쫀득하게 천천히 늘어나는 플라스틱 모찌
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let distSq = pdx * pdx + pdy * pdy;
                                let weight = 0.60 + 0.40 * Math.exp(-distSq / (sigma * sigma * 2.5));
                                p.x = p.ox + dragDx * weight * 0.85;
                                p.y = p.oy + dragDy * weight * 0.85;
                                p.vx *= 0.10; p.vy *= 0.10;
                            }
                        }
                    } else {
                        // [탱글젤리 모드]: Single Unified 3D Mass Physics (1개의 단일 3D 덩어리 방어 - 잘림 0%)
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let distSq = pdx * pdx + pdy * pdy;
                                let weight = 0.72 + 0.28 * Math.exp(-distSq / (sigma * sigma * 2.0));
                                p.x = p.ox + dragDx * weight;
                                p.y = p.oy + dragDy * weight;
                                p.vx *= 0.20; p.vy *= 0.20;
                            }
                        }
                    }
                } else {
                    touchTime = 0;
                    // Mode-specific spring restoration
                    let modeSpring = (currentMode === 'slime') ? 0.04 : (currentMode === 'mochi' ? 0.08 : 0.14);
                    let modeDamping = (currentMode === 'slime') ? 0.92 : (currentMode === 'mochi' ? 0.88 : 0.82);

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
    content = content[:idx_touch_start] + honey_slime_engine + "\n\n                " + content[idx_touch_end:]
    print("100% SUCCESS: Injected Single 3D Mass & Viscous Honey Slime Engine into draw()!")

# Fix Python string comment `# [쫀득모찌 모드]` to JS `// [쫀득모찌 모드]`
content = content.replace("# [쫀득모찌 모드]", "// [쫀득모찌 모드]")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Honey Slime Engine in index.html!")
