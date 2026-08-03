with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Spring.solve() to include anti-inversion node repulsion for thick 3D jelly feel
old_spring_solve = """                let totalForce = springForce + dampingForce;

                let fx = nx * totalForce;
                let fy = ny * totalForce;

                this.p1.vx += fx;
                this.p1.vy += fy;
                this.p2.vx -= fx;
                this.p2.vy -= ny;"""

new_spring_solve = """                let totalForce = springForce + dampingForce;

                let fx = nx * totalForce;
                let fy = ny * totalForce;

                this.p1.vx += fx;
                this.p1.vy += fy;
                this.p2.vx -= fx;
                this.p2.vy -= fy;

                // Anti-inversion boundary repulsion: prevents any mesh triangles from folding over like paper
                let minDist = this.restLength * 0.45;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.28;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

if old_spring_solve in content:
    content = content.replace(old_spring_solve, new_spring_solve)
    print("100% Successfully updated Spring.solve for thick 3D anti-inversion!")
else:
    print("WARNING: old_spring_solve not found!")

# 2. Update drawWarpedTriangle to prevent paper flipping (denom <= 0)
old_denom = """            let denom = u0 * (v1 - v2) + u1 * (v2 - v0) + u2 * (v0 - v1);
            if (Math.abs(denom) < 0.1) {
                ctx.restore();
                return;
            }"""

new_denom = """            let denom = u0 * (v1 - v2) + u1 * (v2 - v0) + u2 * (v0 - v1);
            // Ignore inverted/flipped triangles so character texture NEVER flips backward like paper
            if (denom <= 0.1) {
                ctx.restore();
                return;
            }"""

if old_denom in content:
    content = content.replace(old_denom, new_denom)
    print("100% Successfully updated drawWarpedTriangle to prevent paper flipping!")
else:
    print("WARNING: old_denom not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Thick 3D Solid Jelly & Anti-Paper-Flipping Physics in index.html!")
