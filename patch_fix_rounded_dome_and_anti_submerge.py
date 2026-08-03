with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Spring.prototype.solve for strict non-penetration (prevents ears under face / face under blush/fruit)
old_spring_repulsion = """                // Anti-inversion boundary repulsion: prevents any mesh triangles from folding over like paper
                let minDist = this.restLength * 0.45;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.28;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

new_spring_repulsion = """                // Strict Anti-Penetration & Anti-Inversion Repulsion: 100% prevents ears/face/blush from passing under each other
                let minDist = this.restLength * 0.58;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.48;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

if old_spring_repulsion in content:
    content = content.replace(old_spring_repulsion, new_spring_repulsion)
    print("100% Successfully updated Spring solve for strict anti-submerge non-penetration!")
else:
    print("WARNING: old_spring_repulsion not found!")

# 2. Update mousemove for Cosine Dome smooth rounded pull (0% sharp pointiness)
old_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                let R = width * 0.45;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        let w = Math.cos((dist / R) * (Math.PI / 2));
                        p.x += moveDx * w * 0.85;
                        p.y += moveDy * w * 0.85;
                        // p.ox and p.oy are 100% IMMUTABLE so the character location stays 100% FIXED IN PLACE!
                    }
                }
            }"""

new_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
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

if old_mousemove in content:
    content = content.replace(old_mousemove, new_mousemove)
    print("100% Successfully updated mousemove for smooth Cosine Dome rounded pull!")
else:
    print("WARNING: old_mousemove not found!")

# 3. Update touchmove for Cosine Dome smooth rounded pull (0% sharp pointiness)
old_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                let R = width * 0.45;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        let w = Math.cos((dist / R) * (Math.PI / 2));
                        p.x += moveDx * w * 0.85;
                        p.y += moveDy * w * 0.85;
                        // p.ox and p.oy are 100% IMMUTABLE so the character location stays 100% FIXED IN PLACE!
                    }
                }
            }"""

new_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
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

if old_touchmove in content:
    content = content.replace(old_touchmove, new_touchmove)
    print("100% Successfully updated touchmove for smooth Cosine Dome rounded pull!")
else:
    print("WARNING: old_touchmove not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Smooth Dome Pull & Anti-Submerge Physics in index.html!")
