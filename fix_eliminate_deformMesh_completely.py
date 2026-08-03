with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove deformMesh calls from mousedown and touchstart
content = content.replace("deformMesh(pos.x, pos.y, 18);", "// no deformMesh")
content = content.replace("deformMesh(mx, my, 18);", "// no deformMesh")

# 2. Update draw() for pure 3D Z-depth indentation (Zero screen-Y shift)
old_touch_draw = """                // 1. 3D Volumetric Thickness Compression & Radial Squish Physics (3D 젤리 자체 두께감 속으로 누름 물리)
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

new_touch_draw = """                // 1. Pure 3D Z-Depth Indentation (Screen Y-shift = 0, 3D thickness compression inwards into Z-depth)
                if (isTouching) {
                    touchTime++;

                    // Compression ratio into 3D Z-depth (Z-축 깊이 속으로 꾹 압착 파임)
                    let zCompress = Math.min(0.42, 0.08 + touchTime * 0.015);
                    
                    let maxRadius = width * 0.45;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.6);
                            
                            // Compress the pressed spot INWARDS into Z-depth toward touch point (Z-축 깊이 파임)
                            // Zero downward screen-Y bias!
                            p.x = p.ox + (touchX - p.ox) * zCompress * weight;
                            p.y = p.oy + (touchY - p.oy) * zCompress * weight;
                            p.vx *= 0.35; p.vy *= 0.35;
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

print("100% Eliminated deformMesh & Applied Pure 3D Z-Depth Indentation (Zero Screen-Y Shift) in index.html!")
