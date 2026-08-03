with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update applyDomeStretch for Directional Drag (Outward Dot > 0 vs Inward Dot <= 0)
old_dome = """        // ENGINE 3: 100% Intact Drag Engine (Zero Seam Lines, Zero Cutouts, Zero Tearing)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            // Move 100% of ALL 256 mesh nodes together so the character shape stays 100% PERFECTLY INTACT!
            for (let i = 0; i < points.length; i++) {
                points[i].x += dx;
                points[i].y += dy;
            }
        }"""

new_dome = """        // ENGINE 3: Directional Drag Engine (Outward Stretch vs Inward Shape Preservation)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            if (gIndex === null || !points[gIndex]) return;
            let gPoint = points[gIndex];
            let dx = touchX - lastX;
            let dy = touchY - lastY;

            // Find character center origin
            let centerIdx = Math.floor(rows / 2) * cols + Math.floor(cols / 2);
            let centerX = points[centerIdx] ? points[centerIdx].ox : width / 2;
            let centerY = points[centerIdx] ? points[centerIdx].oy : height / 2;

            // Radial vector from center to grabbed point
            let radX = gPoint.ox - centerX;
            let radY = gPoint.oy - centerY;

            // Dot product to detect OUTWARD (dot > 0) vs INWARD (dot <= 0)
            let dot = dx * radX + dy * radY;

            if (dot > 0) {
                // OUTWARD DRAG: Smooth 3D Bouncy Elastic Jelly Stretch
                let R = width * 0.55;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.hypot(p.ox - gPoint.ox, p.oy - gPoint.oy);
                    if (dist < R) {
                        let w = 0.5 * (1 + Math.cos((dist / R) * Math.PI));
                        p.x += dx * w * 0.88;
                        p.y += dy * w * 0.88;
                    }
                }
            } else {
                // INWARD DRAG: 100% Intact Character Shape Preservation (0% tearing, 0% submerging)
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            }
        }"""

if old_dome in content:
    content = content.replace(old_dome, new_dome)
    print("100% Successfully updated applyDomeStretch for Directional Drag!")

# Update applySquishPressing for Long & Deep Continuous Indentation
old_squish = """        // ENGINE 2: Pure Inward Concave 3D Squish Indentation Engine (0% Outward Bulging)
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            let radius = width * 0.45;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.hypot(p.ox - touchX, p.oy - touchY);
                if (dist < radius) {
                    let weight = Math.pow(1 - dist / radius, 1.6);
                    // Depress INWARD towards touch point (concave indentation)
                    p.x += (touchX - p.ox) * weight * 0.15 * intensity;
                    p.y += (touchY - p.oy) * weight * 0.15 * intensity;
                    p.vx *= 0.4;
                    p.vy *= 0.4;
                }
            }
        }"""

new_squish = """        // ENGINE 2: Long & Deep Continuous 3D Concave Liquid Indentation Engine
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            let radius = width * 0.48;
            
            // Continuous squish depth grows smoothly for as long as press is held down
            let depthFactor = Math.min(0.92, 0.22 + touchTime * 0.035) * intensity;

            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.hypot(p.ox - touchX, p.oy - touchY);
                if (dist < radius) {
                    let weight = Math.pow(1 - dist / radius, 1.5);
                    // Depress INWARD deeply towards touch point
                    p.x += (touchX - p.ox) * weight * depthFactor * 0.25;
                    p.y += (touchY - p.oy) * weight * depthFactor * 0.25;
                    p.vx *= 0.35;
                    p.vy *= 0.35;
                }
            }
        }"""

if old_squish in content:
    content = content.replace(old_squish, new_squish)
    print("100% Successfully updated applySquishPressing for long deep continuous indentation!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Directional Drag & Long Deep Squish Indentation in index.html!")
