with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace draw() touch handling with Physical Downward Press Calculation
old_touch_draw = """                // 1. Fixed Body Anchor: Character stays in place, pulled part stretches locally
                if (isTouching) {
                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY;
                        points[grabbedPointIndex].vx = 0;
                        points[grabbedPointIndex].vy = 0;

                        // Local squishy deformation falloff while character body stays anchored at origin (ox, oy)
                        let grabbedPoint = points[grabbedPointIndex];
                        let maxRadius = width * 0.38;
                        for (let i = 0; i < points.length; i++) {
                            if (i === grabbedPointIndex) continue;
                            let p = points[i];
                            let pdx = p.ox - grabbedPoint.ox;
                            let pdy = p.oy - grabbedPoint.oy;
                            let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                            if (dist < maxRadius) {
                                let weight = Math.pow(1 - dist / maxRadius, 2.0);
                                p.x = p.ox + (touchX - grabbedPoint.ox) * weight * 0.65;
                                p.y = p.oy + (touchY - grabbedPoint.oy) * weight * 0.65;
                                p.vx *= 0.5; p.vy *= 0.5;
                            }
                        }
                    } else {
                        // no deformMesh down
                    }
                } else {
                    // Restoring spring physics: ALL points spring back to their fixed anchor origins (p.ox, p.oy)
                    for (let i = 0; i < points.length; i++) {
                        let fx = (points[i].ox - points[i].x) * 0.14;
                        let fy = (points[i].oy - points[i].y) * 0.14;
                        points[i].vx += fx;
                        points[i].vy += fy;
                        points[i].vx *= 0.82;
                        points[i].vy *= 0.82;
                        points[i].x += points[i].vx;
                        points[i].y += points[i].vy;
                    }
                }"""

new_touch_draw = """                // 1. Physical Press Downward Indentation Calculation (누를수록 물리적으로 쑥 내려감)
                if (isTouching) {
                    touchTime++;

                    // Calculate physical press depth based on press duration & intensity:
                    // Soft initial press (15px) -> Deep long press (up to 75px downward indentation)
                    let pressDepth = Math.min(75, 15 + touchTime * 1.6);
                    
                    let maxRadius = width * 0.45;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.8);
                            p.y = p.oy + pressDepth * weight;
                            p.x = p.ox + (touchX - p.ox) * weight * 0.15;
                            p.vx *= 0.5; p.vy *= 0.5;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        let grabbedPoint = points[grabbedPointIndex];
                        grabbedPoint.x = touchX;
                        grabbedPoint.y = touchY + pressDepth * 0.4;
                    }
                } else {
                    touchTime = 0;
                    // Restoring spring physics: ALL points spring back to their fixed anchor origins (p.ox, p.oy)
                    for (let i = 0; i < points.length; i++) {
                        let fx = (points[i].ox - points[i].x) * 0.14;
                        let fy = (points[i].oy - points[i].y) * 0.14;
                        points[i].vx += fx;
                        points[i].vy += fy;
                        points[i].vx *= 0.82;
                        points[i].vy *= 0.82;
                        points[i].x += points[i].vx;
                        points[i].y += points[i].vy;
                    }
                }"""

if old_touch_draw in content:
    content = content.replace(old_touch_draw, new_touch_draw)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Physical Downward Press Sinking Physics in index.html!")
