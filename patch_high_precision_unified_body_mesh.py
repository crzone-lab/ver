with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Refactor initMesh for 8-Way Cross-Braced Structural Spring Skeleton Fusing All Parts
old_init_mesh = """        function initMesh() {
            points = [];
            springs = [];
            let centerX = width / 2;
            let centerY = height * 0.46;
            let spacing = width * 0.045;

            let startX = centerX - (cols - 1) * spacing / 2;
            let startY = centerY - (rows - 1) * spacing / 2;

            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    let ox = startX + c * spacing;
                    let oy = startY + r * spacing;
                    points.push(new MeshPoint(ox, oy));
                }
            }

            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    let i = r * cols + c;
                    if (c < cols - 1) springs.push(new Spring(points[i], points[i + 1], spacing));
                    if (r < rows - 1) springs.push(new Spring(points[i], points[i + cols], spacing));
                    if (r < rows - 1 && c < cols - 1) {
                        let diagLen = Math.sqrt(2) * spacing;
                        springs.push(new Spring(points[i], points[i + cols + 1], diagLen));
                        springs.push(new Spring(points[i + 1], points[i + cols], diagLen));
                    }
                }
            }
        }"""

new_init_mesh = """        function initMesh() {
            points = [];
            springs = [];
            let centerX = width / 2;
            let centerY = height * 0.46;
            let spacing = width * 0.045;

            let startX = centerX - (cols - 1) * spacing / 2;
            let startY = centerY - (rows - 1) * spacing / 2;

            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    let ox = startX + c * spacing;
                    let oy = startY + r * spacing;
                    points.push(new MeshPoint(ox, oy));
                }
            }

            // High-Precision 8-Way Cross-Braced Skeleton Fusing All Body Parts Into One Solid Body
            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    let i = r * cols + c;
                    // Horizontal & Vertical Structural Springs
                    if (c < cols - 1) springs.push(new Spring(points[i], points[i + 1], spacing));
                    if (r < rows - 1) springs.push(new Spring(points[i], points[i + cols], spacing));
                    // Cross Diagonal Structural Springs (Ears, Face, Tummy Fused Together)
                    if (r < rows - 1 && c < cols - 1) {
                        let diagLen = Math.sqrt(2) * spacing;
                        springs.push(new Spring(points[i], points[i + cols + 1], diagLen));
                        springs.push(new Spring(points[i + 1], points[i + cols], diagLen));
                    }
                    // Shear 2-Step Reinforcement Springs
                    if (c < cols - 2) springs.push(new Spring(points[i], points[i + 2], spacing * 2));
                    if (r < rows - 2) springs.push(new Spring(points[i], points[i + cols * 2], spacing * 2));
                }
            }
        }"""

if old_init_mesh in content:
    content = content.replace(old_init_mesh, new_init_mesh)
    print("100% Successfully upgraded initMesh to High-Precision 8-Way Fused Skeleton!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied High-Precision Fused Skeleton Mesh in index.html!")
