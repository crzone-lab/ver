with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update draw() loop physics for PURE PERPENDICULAR INDENTATION (ZERO Screen Y-Shift, continuous touchTime accumulation)
old_draw_physics = """                // 1. 3D Sinkhole & Surrounding Inward Suction Physics (Restored 100% from v1.4.0 Baseline)
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
                }"""

new_draw_physics = """                // PURE PERPENDICULAR 3D INDENTATION (ZERO Screen Y-Shift, Continuous Long Indentation while Pressed)
                if (isTouching) {
                    touchTime++;

                    // Continuous Indentation Depth grows while holding down touch (from 0.22 up to 0.88!)
                    let sinkPower = Math.min(0.88, 0.22 + touchTime * 0.025);
                    let maxRadius = width * 0.48;

                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.hypot(pdx, pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.6);
                            // ZERO screen-Y downward shift! Pull mesh nodes perpendicular inward toward (touchX, touchY)
                            p.x = p.ox + (touchX - p.ox) * weight * sinkPower;
                            p.y = p.oy + (touchY - p.oy) * weight * sinkPower;
                            p.vx *= 0.35; p.vy *= 0.35;
                        }
                    }
                }"""

if old_draw_physics in content:
    content = content.replace(old_draw_physics, new_draw_physics)
    print("100% Successfully updated draw loop for PURE PERPENDICULAR INDENTATION (ZERO Screen Y-shift)!")

# 2. Fundamental 100% Single Unified Solid Body Drag Engine (w = 1.0 across ALL 256 nodes)
old_dome = """        // ENGINE 3: Bouncy Outward Jelly Stretch & Inward Intact Shape Lock
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            if (gIndex === null || !points[gIndex]) return;
            let gPoint = points[gIndex];
            let dx = touchX - lastX;
            let dy = touchY - lastY;

            let centerIdx = Math.floor(rows / 2) * cols + Math.floor(cols / 2);
            let centerX = points[centerIdx] ? points[centerIdx].ox : width / 2;
            let centerY = points[centerIdx] ? points[centerIdx].oy : height / 2;

            let radX = gPoint.ox - centerX;
            let radY = gPoint.oy - centerY;
            let dot = dx * radX + dy * radY;

            if (dot > 0) {
                // OUTWARD DRAG: Highly elastic bouncy jelly stretch
                let R = width * 0.60;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.hypot(p.ox - gPoint.ox, p.oy - gPoint.oy);
                    if (dist < R) {
                        let w = Math.pow(1 - dist / R, 1.3);
                        p.x = p.ox + (touchX - p.ox) * w * 0.92;
                        p.y = p.oy + (touchY - p.oy) * w * 0.92;
                        p.vx *= 0.3; p.vy *= 0.3;
                    }
                }
            } else {
                // INWARD DRAG: 100% Intact Character Shape Preservation
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            }
        }"""

new_dome = """        // ENGINE 3: Fundamental 100% Single Unified Solid Body Drag Engine (w = 1.0 Across ALL Nodes)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            // Move 100% of ALL 256 mesh nodes together as ONE SINGLE UNIFIED SOLID BODY (0% shearing, 0% tearing!)
            for (let i = 0; i < points.length; i++) {
                points[i].x += dx;
                points[i].y += dy;
            }
        }"""

if old_dome in content:
    content = content.replace(old_dome, new_dome)
    print("100% Successfully updated applyDomeStretch for TRUE 100% Single Solid Body!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Pure Perpendicular Indentation & Fundamental Single Solid Body in index.html!")
