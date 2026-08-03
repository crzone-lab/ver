with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Restore Morning Squish Physics (deformMesh) and 100% Intact Rigid Whole-Body Drag (Zero Seam Tearing)
old_dome = """        // ENGINE 3: Internal Dome Stretch Engine (Smooth 3D Rounded Pull, 0% Sharp Pointiness)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            if (gIndex === null || !points[gIndex]) return;
            let gPoint = points[gIndex];
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            let R = width * 0.65;

            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                let rawW = dist < R ? 0.5 * (1 + Math.cos((dist / R) * Math.PI)) : 0;
                let w = 0.45 + 0.55 * rawW;
                p.x += dx * w;
                p.y += dy * w;
            }
        }"""

new_dome = """        // ENGINE 3: 100% Intact Drag Engine (Zero Seam Lines, Zero Cutouts, Zero Tearing)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            // Move 100% of ALL 256 mesh nodes together so the character shape stays 100% PERFECTLY INTACT!
            for (let i = 0; i < points.length; i++) {
                points[i].x += dx;
                points[i].y += dy;
            }
        }"""

if old_dome in content:
    content = content.replace(old_dome, new_dome)
    print("100% Successfully updated applyDomeStretch for 100% intact drag!")

# Restore Morning Squish Indentation Engine (applySquishPressing)
old_squish = """        // ENGINE 2: Internal Squish Pressing Engine (Pure 3D Z-Depth Liquid Compression as You Press Deeper)
        let activeZPressDepth = 0;
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            activeZPressDepth = Math.min(1.0, activeZPressDepth + 0.12 * intensity);
            let radius = width * 0.42;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let pdx = p.ox - touchX;
                let pdy = p.oy - touchY;
                let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                if (dist < radius) {
                    let w = 0.5 * (1 + Math.cos((dist / radius) * Math.PI));
                    // Mild 3D inward Z-compression velocity
                    p.vx += (touchX - p.ox) * w * 0.03 * intensity;
                    p.vy += (touchY - p.oy) * w * 0.03 * intensity;
                }
            }
        }"""

new_squish = """        // ENGINE 2: Morning 3D Liquid Squish Indentation Engine (Deep Bouncy Pressing on Touch/Click)
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            let radius = width * 0.45;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let pdx = p.ox - touchX;
                let pdy = p.oy - touchY;
                let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                if (dist < radius) {
                    let weight = Math.pow(1 - dist / radius, 1.8);
                    p.vx += (touchX - p.ox) * weight * 0.16 * intensity;
                    p.vy += (touchY - p.oy) * weight * 0.16 * intensity;
                }
            }
        }"""

if old_squish in content:
    content = content.replace(old_squish, new_squish)
    print("100% Successfully restored Morning Squish Indentation Engine!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Morning Physics & 100% Intact Shape Drag in index.html!")
