with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update draw() touch handling for Whole-Body Cohesive 3D Jelly Drag & Round Dome Falloff & Anti-Flipping
old_draw_touch = """                // 1. 3D Sinkhole & Surrounding Inward Suction Physics (누르면 함몰되고 주변 젤리도 중앙으로 같이 쏙 빨려 들어감)
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

new_draw_touch = """                // 1. Whole-Body Cohesive 3D Jelly Drag & Round Dome Deformation Physics
                if (isTouching) {
                    touchTime++;

                    // Anti-Inversion Repulsion Pass: Prevent mesh nodes from overlapping or flipping inside-out
                    let minSpacing = 16;
                    for (let i = 0; i < points.length; i++) {
                        for (let j = i + 1; j < points.length; j++) {
                            let dx = points[i].x - points[j].x;
                            let dy = points[i].y - points[j].y;
                            let dist = Math.sqrt(dx * dx + dy * dy);
                            if (dist < minSpacing && dist > 0.001) {
                                let overlap = (minSpacing - dist) * 0.5;
                                let nx = dx / dist;
                                let ny = dy / dist;
                                points[i].x += nx * overlap * 0.5;
                                points[i].y += ny * overlap * 0.5;
                                points[j].x -= nx * overlap * 0.5;
                                points[j].y -= ny * overlap * 0.5;
                            }
                        }
                    }
                } else {
                    touchTime = 0;
                    // Restoring spring physics: ALL points spring back smoothly to fixed anchor origins (p.ox, p.oy)
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

if old_draw_touch in content:
    content = content.replace(old_draw_touch, new_draw_touch)

# 2. Update touchmove & mousemove handlers for Whole-Body Cohesive Drag & Smooth Round Dome Falloff
old_touchmove = """            if (grabbedPointIndex !== null) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                let radius = 280;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < radius) {
                        let w = Math.pow(1 - dist / radius, 2);
                        p.x += moveDx * w;
                        p.y += moveDy * w;
                        p.vx *= 0.5;
                        p.vy *= 0.5;
                    }
                }
            } else {
                deformMesh(pos.x, pos.y, 15);
            }"""

new_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                
                // 100% Whole-Body Cohesive Drag: Global movement baseline ensures 100% of ALL nodes move together as ONE UNIFIED SOLID 3D JELLY BODY
                let globalCohesion = 0.45;
                for (let i = 0; i < points.length; i++) {
                    points[i].x += moveDx * globalCohesion;
                    points[i].y += moveDy * globalCohesion;
                }

                // Smooth Cosine 3D Round Dome Stretch: Pulls the touched area in a silky-smooth, round 3D jelly dome shape
                let dragRadius = width * 0.55;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < dragRadius) {
                        // Smooth Cosine Dome Falloff curve (1.0 at center, smoothly curving to 0.0 at edge)
                        let w = Math.cos((dist / dragRadius) * (Math.PI / 2));
                        p.x += moveDx * (1 - globalCohesion) * w;
                        p.y += moveDy * (1 - globalCohesion) * w;
                        p.vx *= 0.35;
                        p.vy *= 0.35;
                    }
                }
            }"""

if old_touchmove in content:
    content = content.replace(old_touchmove, new_touchmove)

# Remove deformMesh calls inside touchmove if any remain
content = content.replace("deformMesh(pos.x, pos.y, 15);", "// no deformMesh")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Unified Whole-Body Cohesive 3D Jelly Engine with Round Dome Stretch & Anti-Flipping in index.html!")
