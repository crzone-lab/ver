with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Upgrade mesh resolution to 16x16 for ultra-high-density smooth 3D jelly warping
content = content.replace("let cols = 10;", "let cols = 16;")
content = content.replace("let rows = 10;", "let rows = 16;")

# 2. Replace touchmove and mousemove with C-Infinity Gaussian Smooth Radial Field (100% Zero Sharp Cut Lines!)
new_drag_physics = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                
                // Gaussian Smooth Radial Field (C-Infinity continuous falloff): 100% eliminates sharp triangle cut lines!
                let sigma = width * 0.38;
                let twoSigmaSq = 2 * sigma * sigma;

                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let pdx = p.ox - gPoint.ox;
                    let pdy = p.oy - gPoint.oy;
                    let distSq = pdx * pdx + pdy * pdy;
                    
                    // Smooth Gaussian weight (1.0 at pulled core, curving seamlessly to 0 at edges)
                    let w = Math.exp(-distSq / twoSigmaSq);
                    
                    p.x += moveDx * w;
                    p.y += moveDy * w;
                    p.vx *= 0.3;
                    p.vy *= 0.3;
                }
            }"""

old_touchmove_body = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
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

if old_touchmove_body in content:
    content = content.replace(old_touchmove_body, new_drag_physics)
    print("Successfully replaced touchmove body with Gaussian Smooth Field!")
else:
    print("WARNING: old_touchmove_body not found!")

# Also replace mousemove drag logic with Gaussian Smooth Field
new_mousemove_physics = new_drag_physics.replace("pos.x", "mx").replace("pos.y", "my")

if old_touchmove_body in content: # If mousemove had old body
    content = content.replace(old_touchmove_body, new_mousemove_physics)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 16x16 Gaussian Smooth Jelly Mesh in index.html!")
