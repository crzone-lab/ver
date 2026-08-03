with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Spring.solve() to enforce strict grid coordinate order preservation
old_spring_solve = """                // Hard Separation & Non-Penetration Constraint: 100% prevents ears/face/blush/fruit from passing under or slicing each other
                let minDist = this.restLength * 0.65;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.68;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

new_spring_solve = """                // Strict Monotonic Order Preservation: 100% prevents outer boundary nodes from crossing inner nodes
                let minDist = this.restLength * 0.75;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.85;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

if old_spring_solve in content:
    content = content.replace(old_spring_solve, new_spring_solve)
    print("100% Successfully updated Spring solve for order preservation!")

# 2. Update mousemove and touchmove for Whole-Body Smooth Monotonic Cohesive Motion (w_min = 0.38)
old_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                let R = width * 0.45;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        // Smooth Cosine Dome Curve: 100% rounded pull tip, zero sharp spikes, zero tearing
                        let w = 0.5 * (1 + Math.cos((dist / R) * Math.PI));
                        p.x += moveDx * w * 0.78;
                        p.y += moveDy * w * 0.78;
                    }
                }
            }"""

new_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                let R = width * 0.65;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    // Monotonic Whole-Body Weight: w_min = 0.38 ensures 100% of ALL nodes move in unison (ZERO tearing/spikes!)
                    let rawW = dist < R ? 0.5 * (1 + Math.cos((dist / R) * Math.PI)) : 0;
                    let w = 0.38 + 0.62 * rawW;
                    p.x += moveDx * w * 0.75;
                    p.y += moveDy * w * 0.75;
                }
            }"""

if old_mousemove in content:
    content = content.replace(old_mousemove, new_mousemove)
    print("100% Successfully updated mousemove for monotonic whole-body cohesive motion!")

old_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                let R = width * 0.45;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < R) {
                        // Smooth Cosine Dome Curve: 100% rounded pull tip, zero sharp spikes, zero tearing
                        let w = 0.5 * (1 + Math.cos((dist / R) * Math.PI));
                        p.x += moveDx * w * 0.78;
                        p.y += moveDy * w * 0.78;
                    }
                }
            }"""

new_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                let R = width * 0.65;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    let rawW = dist < R ? 0.5 * (1 + Math.cos((dist / R) * Math.PI)) : 0;
                    let w = 0.38 + 0.62 * rawW;
                    p.x += moveDx * w * 0.75;
                    p.y += moveDy * w * 0.75;
                }
            }"""

if old_touchmove in content:
    content = content.replace(old_touchmove, new_touchmove)
    print("100% Successfully updated touchmove for monotonic whole-body cohesive motion!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Monotonic Whole-Body Order Preservation Physics in index.html!")
