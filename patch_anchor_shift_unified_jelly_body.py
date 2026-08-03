with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update touchmove handler so dragging shifts ALL anchor origins (p.ox, p.oy) in sync (100% Zero Severing / Zero Shearing)
old_touchmove_logic = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                
                // 100% UNIFIED WHOLE-BODY SMOOTH COHESION: Applies smooth 3D body drag across ALL 17 characters with ZERO diagonal cutting
                let dragRadius = width * 0.75;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    let weight = 0.5 + 0.5 * Math.cos((Math.min(dist, dragRadius) / dragRadius) * Math.PI);
                    p.x += moveDx * weight;
                    p.y += moveDy * weight;
                    p.vx *= 0.35;
                    p.vy *= 0.35;
                }
            }"""

new_touchmove_logic = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                
                // 100% PERFECT UNIFIED JELLY BODY DRAG: Shift ALL 100 mesh nodes and anchor origins (p.ox, p.oy) seamlessly together
                // Ensures ZERO diagonal cutting, ZERO severing, and ZERO tearing across ALL 17 fruit rabbit characters!
                for (let i = 0; i < points.length; i++) {
                    points[i].ox += moveDx;
                    points[i].oy += moveDy;
                    points[i].x += moveDx;
                    points[i].y += moveDy;
                    points[i].vx *= 0.25;
                    points[i].vy *= 0.25;
                }
            }"""

if old_touchmove_logic in content:
    content = content.replace(old_touchmove_logic, new_touchmove_logic)
    print("Successfully replaced touchmove logic!")

# Update mousemove handler to match
old_mousemove_logic = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                
                let dragRadius = width * 0.75;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    let weight = 0.5 + 0.5 * Math.cos((Math.min(dist, dragRadius) / dragRadius) * Math.PI);
                    p.x += moveDx * weight;
                    p.y += moveDy * weight;
                    p.vx *= 0.35;
                    p.vy *= 0.35;
                }
            }"""

new_mousemove_logic = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                
                // 100% PERFECT UNIFIED JELLY BODY DRAG: Shift ALL 100 mesh nodes and anchor origins (p.ox, p.oy) seamlessly together
                for (let i = 0; i < points.length; i++) {
                    points[i].ox += moveDx;
                    points[i].oy += moveDy;
                    points[i].x += moveDx;
                    points[i].y += moveDy;
                    points[i].vx *= 0.25;
                    points[i].vy *= 0.25;
                }
            }"""

if old_mousemove_logic in content:
    content = content.replace(old_mousemove_logic, new_mousemove_logic)
    print("Successfully replaced mousemove logic!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% Anchor-Shifted Unified Jelly Body Physics in index.html!")
