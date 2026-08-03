with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace draw() touch handling with 3D Sinkhole & Surrounding Inward Suction Physics
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
                        deformMesh(touchX, touchY, 12);
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

new_touch_draw = """                // 1. 3D Sinkhole & Surrounding Inward Suction Physics (누르면 함몰되고 주변 젤리도 중앙으로 쏙 빨려 들어감)
                if (isTouching) {
                    touchTime++;

                    // Calculate deep sinkhole depth & strong inward suction power based on press duration
                    let currentSink = Math.min(85, 18 + touchTime * 1.8);
                    let suctionPower = Math.min(0.55, 0.12 + touchTime * 0.015);
                    
                    let maxRadius = width * 0.52;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.5);
                            
                            // 1. Downward sinkhole indentation
                            p.y = p.oy + currentSink * weight;

                            // 2. Strong 3D Inward Suction Pulling Surrounding Jelly Mesh Toward (touchX, touchY)
                            let inwardX = (touchX - p.ox) * weight * suctionPower;
                            let inwardY = (touchY - p.oy) * weight * suctionPower * 0.5;
                            p.x = p.ox + inwardX;
                            p.y += inwardY;

                            p.vx *= 0.4; p.vy *= 0.4;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY + currentSink * 0.5;
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

print("Applied 3D Sinkhole & Surrounding Inward Suction Physics in index.html!")
