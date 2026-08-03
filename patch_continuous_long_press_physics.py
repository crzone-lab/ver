with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace draw() touch handling with Continuous Accumulating Downward Press Physics
old_touch_draw = """                // 1. Physical Press Downward Indentation Calculation (누를수록 물리적으로 쑥 내려감)
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

new_touch_draw = """                // 1. Continuous Accumulating Downward Press Physics (길게 누를수록 연속으로 쑥 깊이 내려감)
                if (isTouching) {
                    touchTime++;

                    // Continuous physical press force calculation:
                    // Short press = gentle initial push force
                    // Long hold = accumulating physical downward force (creates deep 3D sinking bowl)
                    let currentForce = Math.min(4.8, 0.8 + touchTime * 0.12);
                    
                    let maxRadius = width * 0.48;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.6);
                            // Apply continuous downward acceleration force to physics velocity
                            p.vy += currentForce * weight;
                            // Apply subtle volumetric inward squeeze
                            p.vx += (touchX - p.ox) * 0.02 * weight;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY;
                    }
                } else {
                    touchTime = 0;
                    // Restoring spring physics: ALL points spring back to their fixed anchor origins (p.ox, p.oy)
                    for (let i = 0; i < points.length; i++) {
                        let fx = (points[i].ox - points[i].x) * 0.16;
                        let fy = (points[i].oy - points[i].y) * 0.16;
                        points[i].vx += fx;
                        points[i].vy += fy;
                        points[i].vx *= 0.84;
                        points[i].vy *= 0.84;
                        points[i].x += points[i].vx;
                        points[i].y += points[i].vy;
                    }
                }"""

if old_touch_draw in content:
    content = content.replace(old_touch_draw, new_touch_draw)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Continuous Accumulating Downward Press Physics in index.html!")
