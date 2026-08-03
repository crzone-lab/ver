with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update touchmove logic for 100% Whole-Body Synchronized Unity
old_touchmove_code = """            if (grabbedPointIndex !== null) {
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
            }"""

new_touchmove_code = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                // Shift 100% of ALL mesh points and anchor origins together as ONE UNIFIED SOLID BODY
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    p.x += moveDx;
                    p.y += moveDy;
                    p.ox += moveDx;
                    p.oy += moveDy;
                }
            }"""

if old_touchmove_code in content:
    content = content.replace(old_touchmove_code, new_touchmove_code)
    print("100% Successfully updated touchmove for ONE UNIFIED SOLID BODY!")
else:
    print("WARNING: old_touchmove_code not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied One Unified Solid Body Physics in index.html!")
