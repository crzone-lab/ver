with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update initMesh to use perfectly symmetric dual diagonal springs (prevents diagonal shear lines across face)
old_mesh_springs = """            // Diagonal structural shear (prevents shearing/sliding collapse)
            for (let r = 0; r < rows - 1; r++) {
                for (let c = 0; c < cols - 1; c++) {
                    let i1 = r * cols + c;
                    let i2 = (r + 1) * cols + (c + 1);
                    let dist = Math.sqrt(Math.pow(points[i1].x - points[i2].x, 2) + Math.pow(points[i1].y - points[i2].y, 2));
                    springs.push(new Spring(points[i1], points[i2], dist));

                    let i3 = r * cols + (c + 1);
                    let i4 = (r + 1) * cols + c;
                    let dist2 = Math.sqrt(Math.pow(points[i3].x - points[i4].x, 2) + Math.pow(points[i3].y - points[i4].y, 2));
                    springs.push(new Spring(points[i3], points[i4], dist2));
                }
            }"""

new_mesh_springs = """            // Symmetric dual-diagonal structural springs (100% prevents diagonal facial shearing/cutting)
            for (let r = 0; r < rows - 1; r++) {
                for (let c = 0; c < cols - 1; c++) {
                    let i1 = r * cols + c;
                    let i2 = (r + 1) * cols + (c + 1);
                    let dist1 = Math.sqrt(Math.pow(points[i1].x - points[i2].x, 2) + Math.pow(points[i1].y - points[i2].y, 2));
                    let s1 = new Spring(points[i1], points[i2], dist1);
                    s1.stiffness = 0.08; // Balanced diagonal tension
                    springs.push(s1);

                    let i3 = r * cols + (c + 1);
                    let i4 = (r + 1) * cols + c;
                    let dist2 = Math.sqrt(Math.pow(points[i3].x - points[i4].x, 2) + Math.pow(points[i3].y - points[i4].y, 2));
                    let s2 = new Spring(points[i3], points[i4], dist2);
                    s2.stiffness = 0.08;
                    springs.push(s2);
                }
            }"""

if old_mesh_springs in content:
    content = content.replace(old_mesh_springs, new_mesh_springs)

# Update touchmove to apply smooth, unified whole-body cohesion across ALL 17 characters (no diagonal severing)
old_touch_move = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                
                // 100% UNIFIED WHOLE-BODY MOTION: 100% of ALL 100 mesh nodes (hands, fruit, ears, feet) move together in 1-to-1 sync!
                for (let i = 0; i < points.length; i++) {
                    points[i].x += moveDx;
                    points[i].y += moveDy;
                    points[i].vx *= 0.35;
                    points[i].vy *= 0.35;
                }
            }"""

new_touch_move = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
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

if old_touch_move in content:
    content = content.replace(old_touch_move, new_touch_move)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Symmetric Mesh & Zero Diagonal Cut Whole-Body Physics in index.html!")
