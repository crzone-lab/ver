with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update mousemove handler to remove p.ox / p.oy mutations
old_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                let R = width * 0.45;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        let w = Math.cos((dist / R) * (Math.PI / 2));
                        p.x += moveDx * w * 0.82;
                        p.y += moveDy * w * 0.82;
                        p.ox += moveDx * w * 0.22;
                        p.oy += moveDy * w * 0.22;
                    }
                }
            }"""

new_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                let R = width * 0.45;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        let w = Math.cos((dist / R) * (Math.PI / 2));
                        p.x += moveDx * w * 0.85;
                        p.y += moveDy * w * 0.85;
                        // p.ox and p.oy are 100% IMMUTABLE so the character location stays 100% FIXED IN PLACE!
                    }
                }
            }"""

if old_mousemove in content:
    content = content.replace(old_mousemove, new_mousemove)
    print("100% Successfully updated mousemove for 100% fixed character location!")
else:
    print("WARNING: old_mousemove not found!")

# Update touchmove handler
old_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                let R = width * 0.45;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        let w = Math.cos((dist / R) * (Math.PI / 2));
                        p.x += moveDx * w * 0.82;
                        p.y += moveDy * w * 0.82;
                        p.ox += moveDx * w * 0.22;
                        p.oy += moveDy * w * 0.22;
                    }
                }
            }"""

new_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                let R = width * 0.45;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        let w = Math.cos((dist / R) * (Math.PI / 2));
                        p.x += moveDx * w * 0.85;
                        p.y += moveDy * w * 0.85;
                        // p.ox and p.oy are 100% IMMUTABLE so the character location stays 100% FIXED IN PLACE!
                    }
                }
            }"""

if old_touchmove in content:
    content = content.replace(old_touchmove, new_touchmove)
    print("100% Successfully updated touchmove for 100% fixed character location!")
else:
    print("WARNING: old_touchmove not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% Fixed Character Location in index.html!")
