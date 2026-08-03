with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update applyDomeStretch to use exact touchX, touchY coordinates as absolute center origin
old_dome = """        // ENGINE 3: Smooth Rounded 3D Jelly Dome Engine (0% Sharp Pointiness)
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

new_dome = """        // ENGINE 3: Exact 100% Touch Coordinate Alignment Engine (Push/Pull/Press centered exactly at touchX, touchY)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            let R = width * 0.52;

            // Use exact touchX, touchY as 100% precise center origin
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.hypot(p.ox - touchX, p.oy - touchY);
                let w = dist < R ? 0.5 * (1 + Math.cos((dist / R) * Math.PI)) : 0;
                let finalWeight = 0.45 + 0.55 * w;
                p.x += dx * finalWeight;
                p.y += dy * finalWeight;
            }
        }"""

if old_dome in content:
    content = content.replace(old_dome, new_dome)
    print("100% Successfully updated applyDomeStretch for Exact 100% Touch Coordinate Alignment!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Exact Touch Coordinate Alignment in index.html!")
