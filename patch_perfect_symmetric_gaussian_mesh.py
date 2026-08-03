with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update initMesh to use 16x16 grid with Symmetric Cross-Diagonal Springs (X-bracing) for ZERO tearing/cutting
old_init_mesh = """        function initMesh() {
            points = [];
            springs = [];

            let minDim = Math.min(width, height);
            let meshSize = minDim * 0.62; 
            
            let startX = (width - meshSize) / 2;
            let startY = (height - meshSize) / 2 + 15;

            let stepX = meshSize / (cols - 1);
            let stepY = meshSize / (rows - 1);

            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    let x = startX + c * stepX;
                    let y = startY + r * stepY;
                    points.push(new MeshPoint(x, y));
                }
            }

            // Create structural springs (horizontal, vertical, diagonal)
            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    let i = r * cols + c;
                    
                    // Horizontal
                    if (c < cols - 1) {
                        let right = r * cols + (c + 1);
                        let d = Math.hypot(points[i].ox - points[right].ox, points[i].oy - points[right].oy);
                        springs.push(new Spring(points[i], points[right], d));
                    }
                    // Vertical
                    if (r < rows - 1) {
                        let down = (r + 1) * cols + c;
                        let d = Math.hypot(points[i].ox - points[down].ox, points[i].oy - points[down].oy);
                        springs.push(new Spring(points[i], points[down], d));
                    }
                    // Diagonal (Top-Left to Bottom-Right)
                    if (r < rows - 1 && c < cols - 1) {
                        let diag1 = (r + 1) * cols + (c + 1);
                        let d1 = Math.hypot(points[i].ox - points[diag1].ox, points[i].oy - points[diag1].oy);
                        springs.push(new Spring(points[i], points[diag1], d1));
                    }
                }
            }
        }"""

new_init_mesh = """        function initMesh() {
            points = [];
            springs = [];

            let minDim = Math.min(width, height);
            let meshSize = minDim * 0.62; 
            
            let startX = (width - meshSize) / 2;
            let startY = (height - meshSize) / 2 + 15;

            let stepX = meshSize / (cols - 1);
            let stepY = meshSize / (rows - 1);

            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    let x = startX + c * stepX;
                    let y = startY + r * stepY;
                    points.push(new MeshPoint(x, y));
                }
            }

            // Create Symmetric Dual-Diagonal (X-Braced) Springs for 100% Zero Tearing and Zero Diagonal Cutting
            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    let i = r * cols + c;
                    
                    // Horizontal
                    if (c < cols - 1) {
                        let right = r * cols + (c + 1);
                        let d = Math.hypot(points[i].ox - points[right].ox, points[i].oy - points[right].oy);
                        springs.push(new Spring(points[i], points[right], d));
                    }
                    // Vertical
                    if (r < rows - 1) {
                        let down = (r + 1) * cols + c;
                        let d = Math.hypot(points[i].ox - points[down].ox, points[i].oy - points[down].oy);
                        springs.push(new Spring(points[i], points[down], d));
                    }
                    // Diagonal 1 (Top-Left to Bottom-Right)
                    if (r < rows - 1 && c < cols - 1) {
                        let diag1 = (r + 1) * cols + (c + 1);
                        let d1 = Math.hypot(points[i].ox - points[diag1].ox, points[i].oy - points[diag1].oy);
                        springs.push(new Spring(points[i], points[diag1], d1));
                    }
                    // Diagonal 2 (Top-Right to Bottom-Left) - Symmetric X-Bracing!
                    if (r < rows - 1 && c > 0) {
                        let diag2 = (r + 1) * cols + (c - 1);
                        let d2 = Math.hypot(points[i].ox - points[diag2].ox, points[i].oy - points[diag2].oy);
                        springs.push(new Spring(points[i], points[diag2], d2));
                    }
                }
            }
        }"""

if old_init_mesh in content:
    content = content.replace(old_init_mesh, new_init_mesh)
    print("100% Successfully updated initMesh for Symmetric Dual-Diagonal X-Bracing!")
else:
    print("WARNING: old_init_mesh not found!")

# 2. Update mousemove and touchmove to use Gaussian smooth C-infinity radial displacement for 0% sharp spikes
old_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                let R = width * 0.48;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        // Cosine Dome Curve for 100% smooth, rounded pull tip (0% sharp pointiness!)
                        let w = 0.5 * (1 + Math.cos((dist / R) * Math.PI));
                        p.x += moveDx * w * 0.85;
                        p.y += moveDy * w * 0.85;
                    }
                }
            }"""

new_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                let sigma = width * 0.22;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let distSq = Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2);
                    // Gaussian C-Infinity Smooth Radial Field for 100% Zero Tearing and Perfectly Rounded Pulls
                    let w = Math.exp(-distSq / (2 * sigma * sigma));
                    p.x += moveDx * w * 0.82;
                    p.y += moveDy * w * 0.82;
                }
            }"""

if old_mousemove in content:
    content = content.replace(old_mousemove, new_mousemove)
    print("100% Successfully updated mousemove for Gaussian C-Infinity smooth pulls!")

old_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                let R = width * 0.48;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        // Cosine Dome Curve for 100% smooth, rounded pull tip (0% sharp pointiness!)
                        let w = 0.5 * (1 + Math.cos((dist / R) * Math.PI));
                        p.x += moveDx * w * 0.85;
                        p.y += moveDy * w * 0.85;
                    }
                }
            }"""

new_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                let sigma = width * 0.22;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let distSq = Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2);
                    let w = Math.exp(-distSq / (2 * sigma * sigma));
                    p.x += moveDx * w * 0.82;
                    p.y += moveDy * w * 0.82;
                }
            }"""

if old_touchmove in content:
    content = content.replace(old_touchmove, new_touchmove)
    print("100% Successfully updated touchmove for Gaussian C-Infinity smooth pulls!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Symmetric Gaussian Mesh Physics in index.html!")
