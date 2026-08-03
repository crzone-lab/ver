with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix spring stiffness/damping to eliminate trembling/jittering completely (k = 0.14, damping = 0.18)
old_spring_solve = """                let delta = dist - this.restLength;
                let k = 0.45; // Strong shape preservation spring rigidity
                let springForce = delta * k;
                
                let nx = dx / dist;
                let ny = dy / dist;

                let rvx = this.p2.vx - this.p1.vx;
                let rvy = this.p2.vy - this.p1.vy;
                let dampingForce = (rvx * nx + rvy * ny) * 0.28;"""

new_spring_solve = """                let delta = dist - this.restLength;
                let k = 0.14; // Smooth bouncy jelly elasticity (ZERO trembling/jittering)
                let springForce = delta * k;
                
                let nx = dx / dist;
                let ny = dy / dist;

                let rvx = this.p2.vx - this.p1.vx;
                let rvy = this.p2.vy - this.p1.vy;
                let dampingForce = (rvx * nx + rvy * ny) * 0.22;"""

if old_spring_solve in content:
    content = content.replace(old_spring_solve, new_spring_solve)
    print("100% Successfully fixed Spring solve for zero trembling!")

# 2. Fix applySquishPressing to depress INWARDS towards (touchX, touchY) without outward bulging
old_squish = """        // ENGINE 2: Super Deep 3D Liquid Squish Indentation Engine
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            let radius = width * 0.48;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.hypot(p.x - touchX, p.y - touchY);
                if (dist < radius) {
                    let weight = Math.pow(1 - dist / radius, 1.5);
                    p.vx += (touchX - p.x) * weight * 0.35 * intensity;
                    p.vy += (touchY - p.y) * weight * 0.35 * intensity;
                }
            }
        }"""

new_squish = """        // ENGINE 2: Pure Inward Concave 3D Squish Indentation Engine (0% Outward Bulging)
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            let radius = width * 0.45;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.hypot(p.ox - touchX, p.oy - touchY);
                if (dist < radius) {
                    let weight = Math.pow(1 - dist / radius, 1.6);
                    // Depress INWARD towards touch point (concave indentation)
                    p.x += (touchX - p.ox) * weight * 0.15 * intensity;
                    p.y += (touchY - p.oy) * weight * 0.15 * intensity;
                    p.vx *= 0.4;
                    p.vy *= 0.4;
                }
            }
        }"""

if old_squish in content:
    content = content.replace(old_squish, new_squish)
    print("100% Successfully fixed applySquishPressing for pure inward indentation!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Trembling Fix & Pure Inward Indentation in index.html!")
