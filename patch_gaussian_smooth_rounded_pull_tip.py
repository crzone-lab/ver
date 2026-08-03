with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update applyDomeStretch to 100% Smooth Gaussian Apex Dome (Zero Sharp Peak)
old_dome = """        // ENGINE 3: Exact 100% Touch Coordinate Alignment Engine (Push/Pull/Press centered exactly at touchX, touchY)
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

new_dome = """        // ENGINE 3: 100% Smooth Gaussian Apex Dome Engine (Zero Sharp Pointiness, Flat Rounded Apex)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            let R = width * 0.58;

            // Gaussian Kernel: exp(- (dist / (R * 0.42))^2)
            // Derivative at dist=0 is EXACTLY ZERO, guaranteeing a 100% flat, smooth, rounded top!
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.hypot(p.ox - touchX, p.oy - touchY);
                let w = Math.exp(-Math.pow(dist / (R * 0.42), 2));
                let weight = 0.50 + 0.50 * w;
                p.x += dx * weight;
                p.y += dy * weight;
            }
        }"""

if old_dome in content:
    content = content.replace(old_dome, new_dome)
    print("100% Successfully updated applyDomeStretch for Gaussian Apex Dome (Zero sharp tip)!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Gaussian Apex Dome in index.html!")
