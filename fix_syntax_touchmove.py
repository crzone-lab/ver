with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let dx = pos.x - lastTouchX;
                let dy = pos.y - lastTouchY;
                let R = width * 0.65;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    let rawW = dist < R ? 0.5 * (1 + Math.cos((dist / R) * Math.PI)) : 0;
                    let w = 0.42 + 0.58 * rawW;
                    p.x += dx * w;
                    p.y += dy * w;
                }
            }
            lastTouchX = pos.x;
            lastTouchY = pos.y; else {
                deformMesh(pos.x, pos.y, 15);
            }"""

new_code = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let dx = pos.x - lastTouchX;
                let dy = pos.y - lastTouchY;
                let R = width * 0.65;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    let rawW = dist < R ? 0.5 * (1 + Math.cos((dist / R) * Math.PI)) : 0;
                    let w = 0.42 + 0.58 * rawW;
                    p.x += dx * w;
                    p.y += dy * w;
                }
            } else {
                deformMesh(pos.x, pos.y, 15);
            }
            lastTouchX = pos.x;
            lastTouchY = pos.y;"""

if old_code in content:
    content = content.replace(old_code, new_code)
    print("100% Successfully fixed touchmove syntax!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Syntax Fix in index.html!")
