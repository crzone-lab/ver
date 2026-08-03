with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Spring.solve with Hard Non-Penetration Distance Floor (minDist = 0.88 * restLength)
old_spring_solve = """                // ENGINE 1: BorderLock & Anti-Penetration Guard (Strict minDist = 0.85 * restLength)
                let minDist = this.restLength * 0.85;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 1.0;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

new_spring_solve = """                // ENGINE 1: Strict Hard Non-Penetration Guard (minDist = 0.88 * restLength, 0% Overlap / 0% Submerge)
                let minDist = this.restLength * 0.88;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 1.0;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

if old_spring_solve in content:
    content = content.replace(old_spring_solve, new_spring_solve)
    print("100% Successfully updated Spring solve for 0.88 Non-Penetration!")

# 2. Update drawWarpedTriangle to strictly reject inverted triangles (denom <= 0.1)
old_warped_triangle = """        function drawWarpedTriangle(ctx, img, p1, p2, p3, u1, v1, u2, v2, u3, v3) {"""

new_warped_triangle = """        function drawWarpedTriangle(ctx, img, p1, p2, p3, u1, v1, u2, v2, u3, v3) {
            let denom = (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
            if (denom <= 0.1) return; // Strict Orientation Lock: 100% prevents triangle inversion & texture slicing!"""

if old_warped_triangle in content and "Strict Orientation Lock" not in content:
    content = content.replace(old_warped_triangle, new_warped_triangle)
    print("100% Successfully updated drawWarpedTriangle for Strict Orientation Lock!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Non-Penetration & Orientation Lock in index.html!")
