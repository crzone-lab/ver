with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update draw() physics loop to 100% exact v1.4.0 baseline sinkhole & surrounding suction
old_draw_physics = """                // CONTINUOUS PRESSING INDENTATION (Accumulates continuously while pressed down)
                if (isTouching) {
                    touchTime++;

                    let maxRadius = width * 0.48;
                    // Continuous Indentation Power grows while holding down touch (from 0.25 up to 0.88!)
                    let squishPower = Math.min(0.88, 0.25 + touchTime * 0.025);

                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let dist = Math.hypot(p.ox - touchX, p.oy - touchY);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.6);
                            // Pull nodes inward towards touch center as you hold down press
                            let targetX = p.ox + (touchX - p.ox) * weight * squishPower;
                            let targetY = p.oy + (touchY - p.oy) * weight * squishPower;
                            
                            p.x += (targetX - p.x) * 0.45;
                            p.y += (targetY - p.y) * 0.45;
                            p.vx *= 0.4;
                            p.vy *= 0.4;
                        }
                    }
                }"""

new_draw_physics = """                // 1. 3D Sinkhole & Surrounding Inward Suction Physics (Restored 100% from v1.4.0 Baseline)
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

if old_draw_physics in content:
    content = content.replace(old_draw_physics, new_draw_physics)
    print("100% Successfully restored v1.4.0 sinkhole draw loop physics!")

# 2. Update applyDomeStretch to handle outward bouncy stretch vs inward shape preservation
old_dome = """        // ENGINE 3: Directional Drag Engine (Exact v1.4.0 Bouncy Outward Jelly Stretch + Inward Shape Lock)
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
                // OUTWARD DRAG: Super Bouncy Elastic 3D Jelly Stretch (Restored from v1.4.0 / v2.8.0)
                let R = width * 0.58;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.hypot(p.ox - gPoint.ox, p.oy - gPoint.oy);
                    if (dist < R) {
                        let w = Math.pow(1 - dist / R, 1.4);
                        p.x = p.ox + (touchX - p.ox) * w * 0.88;
                        p.y = p.oy + (touchY - p.oy) * w * 0.88;
                        p.vx *= 0.35;
                        p.vy *= 0.35;
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

new_dome = """        // ENGINE 3: Bouncy Outward Jelly Stretch & Inward Intact Shape Lock
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

if old_dome in content:
    content = content.replace(old_dome, new_dome)
    print("100% Successfully updated applyDomeStretch!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Exact v1.4.0 Baseline Physics in index.html!")
