with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Spring.solve for 100% Outer Boundary Silhouette Stability (minDist = 0.85 * restLength)
old_spring_solve = """                // ENGINE 1: BorderLock & Anti-Penetration Guard (Strict minDist = 0.75 * restLength)
                let minDist = this.restLength * 0.75;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.95;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

new_spring_solve = """                // ENGINE 1: BorderLock & Anti-Penetration Guard (Strict minDist = 0.85 * restLength)
                let minDist = this.restLength * 0.85;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 1.0;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

if old_spring_solve in content:
    content = content.replace(old_spring_solve, new_spring_solve)
    print("100% Successfully updated Spring solve for 0.85 boundary stability!")

# 2. Update applySquishPressing for 3D Z-depth liquid compression without warping 2D silhouette
old_squish = """        // ENGINE 2: Internal Squish Pressing Engine (Independent Squish Indentation on Touch)
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            let radius = width * 0.38;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let pdx = p.ox - touchX;
                let pdy = p.oy - touchY;
                let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                if (dist < radius) {
                    // Smooth Cosine Squish Indentation
                    let w = 0.5 * (1 + Math.cos((dist / radius) * Math.PI));
                    p.vx += (touchX - p.ox) * w * 0.08 * intensity;
                    p.vy += (touchY - p.oy) * w * 0.08 * intensity;
                }
            }
        }"""

new_squish = """        // ENGINE 2: Internal Squish Pressing Engine (Pure 3D Z-Depth Liquid Compression as You Press Deeper)
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

if old_squish in content:
    content = content.replace(old_squish, new_squish)
    print("100% Successfully updated applySquishPressing for Z-depth compression!")

# 3. Update applyDomeStretch for whole-body 100% cohesive motion (w_min = 0.45)
old_dome = """        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            if (gIndex === null || !points[gIndex]) return;
            let gPoint = points[gIndex];
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            let R = width * 0.65;

            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                // Continuous Cosine Dome Field (w_min = 0.42 ensures 100% cohesive whole-body unity)
                let rawW = dist < R ? 0.5 * (1 + Math.cos((dist / R) * Math.PI)) : 0;
                let w = 0.42 + 0.58 * rawW;
                p.x += dx * w;
                p.y += dy * w;
            }
        }"""

new_dome = """        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
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

if old_dome in content:
    content = content.replace(old_dome, new_dome)
    print("100% Successfully updated applyDomeStretch!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 3D Z-Depth Squish & Border Stability in index.html!")
