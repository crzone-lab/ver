with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace draw() touch handling with 3D Volumetric Thickness Compression & Radial Squish Physics
old_touch_draw = """                // 1. 3D Sinkhole & Surrounding Inward Suction Physics (누르면 함몰되고 주변 젤리도 중앙으로 같이 쏙 빨려 들어감)
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

new_touch_draw = """                // 1. 3D Volumetric Thickness Compression & Radial Squish Physics (3D 젤리 자체 두께감 속으로 누름 물리)
                if (isTouching) {
                    touchTime++;

                    // Calculate 3D thickness compression ratio based on press duration (0.08 to 0.45)
                    let squishAmount = Math.min(0.45, 0.08 + touchTime * 0.012);
                    
                    let maxRadius = width * 0.42;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.8);
                            
                            // Calculate radial 3D thickness squish: pressed spot flattens into its 3D depth, pushing surrounding jelly radially outward
                            let angle = Math.atan2(pdy, pdx);
                            let pushDist = dist * squishAmount * weight;

                            p.x = p.ox + Math.cos(angle) * pushDist;
                            p.y = p.oy + Math.sin(angle) * pushDist;
                            p.vx *= 0.4; p.vy *= 0.4;
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

print("Applied 3D Volumetric Thickness Compression & Radial Squish Physics in index.html!")
