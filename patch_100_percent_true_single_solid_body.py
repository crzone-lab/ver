with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update mousemove: Move 100% of ALL 100 mesh nodes by exact 1-to-1 delta vector (w = 1.0)
old_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let dx = mx - lastTouchX;
                let dy = my - lastTouchY;
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
            lastTouchX = mx;
            lastTouchY = my;"""

new_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let dx = mx - lastTouchX;
                let dy = my - lastTouchY;
                // Move 100% of ALL mesh nodes in 1-to-1 locked unity as ONE SINGLE UNIFIED SOLID BODY
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            }
            lastTouchX = mx;
            lastTouchY = my;"""

if old_mousemove in content:
    content = content.replace(old_mousemove, new_mousemove)
    print("100% Successfully updated mousemove to TRUE 100% Single Solid Body!")
else:
    print("WARNING: old_mousemove not found!")

# Update touchmove: Move 100% of ALL 100 mesh nodes by exact 1-to-1 delta vector (w = 1.0)
old_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
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
            } else {"""

new_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let dx = pos.x - lastTouchX;
                let dy = pos.y - lastTouchY;
                // Move 100% of ALL mesh nodes in 1-to-1 locked unity as ONE SINGLE UNIFIED SOLID BODY
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            } else {"""

if old_touchmove in content:
    content = content.replace(old_touchmove, new_touchmove)
    print("100% Successfully updated touchmove to TRUE 100% Single Solid Body!")
else:
    print("WARNING: old_touchmove not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% True Single Solid Body Physics in index.html!")
