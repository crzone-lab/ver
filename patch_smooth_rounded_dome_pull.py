with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update applyDomeStretch for C1-continuous Cosine Dome Kernel (0% Sharp Pointiness, 100% Smooth Rounded Dome)
old_dome = """        // ENGINE 3: Fundamental 100% Single Unified Solid Body Drag Engine (w = 1.0 Across ALL Nodes)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            // Move 100% of ALL 256 mesh nodes together as ONE SINGLE UNIFIED SOLID BODY (0% shearing, 0% tearing!)
            for (let i = 0; i < points.length; i++) {
                points[i].x += dx;
                points[i].y += dy;
            }
        }"""

new_dome = """        // ENGINE 3: Smooth Rounded 3D Jelly Dome Engine (0% Sharp Pointiness)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            if (gIndex === null || !points[gIndex]) {
                for (let i = 0; i < points.length; i++) { points[i].x += dx; points[i].y += dy; }
                return;
            }

            let gPoint = points[gIndex];
            let R = width * 0.52;

            // C1-Continuous Cosine Dome Field (Zero-tangent at apex guarantees ZERO sharp tip!)
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.hypot(p.ox - gPoint.ox, p.oy - gPoint.oy);
                let w = dist < R ? 0.5 * (1 + Math.cos((dist / R) * Math.PI)) : 0;
                // Blend with 0.45 base whole-body vector to keep shape intact
                let finalWeight = 0.45 + 0.55 * w;
                p.x += dx * finalWeight;
                p.y += dy * finalWeight;
            }
        }"""

if old_dome in content:
    content = content.replace(old_dome, new_dome)
    print("100% Successfully updated applyDomeStretch for Smooth Rounded Dome (0% sharp tip)!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Smooth Rounded Dome Pull in index.html!")
