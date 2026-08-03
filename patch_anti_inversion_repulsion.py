with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_spring_end = """                this.p1.vx += fx;
                this.p1.vy += fy;
                this.p2.vx -= fx;
                this.p2.vy -= fy;
            }"""

new_spring_end = """                this.p1.vx += fx;
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
                }
            }"""

if old_spring_end in content:
    content = content.replace(old_spring_end, new_spring_end)
    print("100% Successfully updated Spring.solve for thick 3D anti-inversion!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Anti-Inversion Boundary Repulsion in index.html!")
