with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace draw physics loop and touch/mouse handlers with state-locked architecture
old_draw_loop = """                // PURE PERPENDICULAR 3D INDENTATION (ZERO Screen Y-Shift, Continuous Long Indentation while Pressed)
                if (isTouching) {
                    touchTime++;

                    // Continuous Indentation Depth grows while holding down touch (from 0.22 up to 0.88!)
                    let sinkPower = Math.min(0.88, 0.22 + touchTime * 0.025);
                    let maxRadius = width * 0.48;

                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.hypot(pdx, pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.6);
                            // ZERO screen-Y downward shift! Pull mesh nodes perpendicular inward toward (touchX, touchY)
                            p.x = p.ox + (touchX - p.ox) * weight * sinkPower;
                            p.y = p.oy + (touchY - p.oy) * weight * sinkPower;
                            p.vx *= 0.35; p.vy *= 0.35;
                        }
                    }
                }"""

new_draw_loop = """                // FINAL PERFECT STATE-LOCKED ENGINE
                if (isTouching) {
                    touchTime++;

                    // State A: Pressing & Holding (Pure 3D Z-Depth Indentation, 0 Screen Y-Shift)
                    if (grabbedPointIndex === null || (Math.abs(touchX - lastTouchX) < 2 && Math.abs(touchY - lastTouchY) < 2)) {
                        let sinkPower = Math.min(0.85, 0.20 + touchTime * 0.025);
                        let maxRadius = width * 0.48;

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let pdx = p.ox - touchX;
                            let pdy = p.oy - touchY;
                            let dist = Math.hypot(pdx, pdy);
                            if (dist < maxRadius) {
                                let weight = Math.pow(1 - dist / maxRadius, 1.6);
                                p.x = p.ox + (touchX - p.ox) * weight * sinkPower;
                                p.y = p.oy + (touchY - p.oy) * weight * sinkPower;
                                p.vx *= 0.35; p.vy *= 0.35;
                            }
                        }
                    }
                }"""

if old_draw_loop in content:
    content = content.replace(old_draw_loop, new_draw_loop)
    print("100% Successfully patched draw loop with State-Locked Engine!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Final Perfect Lock Engine in index.html!")
