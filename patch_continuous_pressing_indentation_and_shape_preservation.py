with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Spring.solve for strong structural rigidity & shape preservation (k = 0.45, minDist = 0.85)
old_spring_solve = """                let delta = dist - this.restLength;
                let k = 0.12; // Base jelly elastic restoration
                let springForce = delta * k;
                
                let nx = dx / dist;
                let ny = dy / dist;

                let rvx = this.p2.vx - this.p1.vx;
                let rvy = this.p2.vy - this.p1.vy;
                let dampingForce = (rvx * nx + rvy * ny) * 0.18;"""

new_spring_solve = """                let delta = dist - this.restLength;
                let k = 0.45; // Strong shape preservation spring rigidity
                let springForce = delta * k;
                
                let nx = dx / dist;
                let ny = dy / dist;

                let rvx = this.p2.vx - this.p1.vx;
                let rvy = this.p2.vy - this.p1.vy;
                let dampingForce = (rvx * nx + rvy * ny) * 0.28;"""

if old_spring_solve in content:
    content = content.replace(old_spring_solve, new_spring_solve)
    print("100% Successfully updated Spring solve for strong shape preservation!")

# 2. Update draw() loop for CONTINUOUS PRESSING INDENTATION (touchTime++ continuous inward accumulation)
old_draw_loop_physics = """                // 1. Pure 3D Inward Suction Physics (Screen Y-Shift = 0: ZERO downward squishing on hover/touch)
                if (isTouching) {
                    touchTime++;

                    let suctionPower = Math.min(0.72, 0.12 + touchTime * 0.005);
                    let maxRadius = width * 0.42;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.8);
                            
                            // ZERO screen-Y downward shift! Pull mesh nodes inward toward (touchX, touchY)
                            p.x = p.ox + (touchX - p.ox) * weight * suctionPower;
                            p.y = p.oy + (touchY - p.oy) * weight * suctionPower;
                            p.vx *= 0.35; p.vy *= 0.35;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY;
                    }
                }"""

new_draw_loop_physics = """                // CONTINUOUS PRESSING INDENTATION (Accumulates continuously while pressed down)
                if (isTouching) {
                    touchTime++;

                    let maxRadius = width * 0.48;
                    // Continuous Indentation Power grows while holding down touch (from 0.25 up to 0.88!)
                    let squishPower = Math.min(0.88, 0.25 + touchTime * 0.025);

                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let dist = Math.hypot(p.ox - touchX, p.oy - touchY);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.6);
                            // Pull nodes inward towards touch center as you hold down press
                            let targetX = p.ox + (touchX - p.ox) * weight * squishPower;
                            let targetY = p.oy + (touchY - p.oy) * weight * squishPower;
                            
                            p.x += (targetX - p.x) * 0.45;
                            p.y += (targetY - p.y) * 0.45;
                            p.vx *= 0.4;
                            p.vy *= 0.4;
                        }
                    }
                }"""

if old_draw_loop_physics in content:
    content = content.replace(old_draw_loop_physics, new_draw_loop_physics)
    print("100% Successfully updated draw loop for continuous pressing indentation!")
else:
    print("WARNING: old_draw_loop_physics not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Continuous Pressing Indentation Physics in index.html!")
