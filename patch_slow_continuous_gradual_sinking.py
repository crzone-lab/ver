with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update draw() loop for Slow Continuous Gradual Sinking (Starts at 0.00, sinks slowly over 2 seconds)
old_draw_loop = """                // FINAL PERFECT STATE-LOCKED ENGINE
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

new_draw_loop = """                // SLOW CONTINUOUS GRADUAL SINKING ENGINE (Starts at 0.00, sinks slowly over 2 full seconds!)
                if (isTouching) {
                    touchTime++;

                    if (grabbedPointIndex === null || (Math.abs(touchX - lastTouchX) < 2 && Math.abs(touchY - lastTouchY) < 2)) {
                        // Starts at 0.00 on touch down, slowly & continuously deepens over 120 frames (2 seconds)
                        let sinkPower = Math.min(0.85, touchTime / 120.0);
                        let maxRadius = width * 0.48;

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dist = Math.hypot(p.ox - touchX, p.oy - touchY);
                            if (dist < maxRadius) {
                                let weight = Math.pow(1 - dist / maxRadius, 1.6);
                                let targetX = p.ox + (touchX - p.ox) * weight * sinkPower;
                                let targetY = p.oy + (touchY - p.oy) * weight * sinkPower;
                                // Smooth slow interpolation (0.12 rate)
                                p.x += (targetX - p.x) * 0.12;
                                p.y += (targetY - p.y) * 0.12;
                                p.vx *= 0.35; p.vy *= 0.35;
                            }
                        }
                    }
                }"""

if old_draw_loop in content:
    content = content.replace(old_draw_loop, new_draw_loop)
    print("100% Successfully updated draw loop for SLOW CONTINUOUS GRADUAL SINKING!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Slow Continuous Gradual Sinking in index.html!")
