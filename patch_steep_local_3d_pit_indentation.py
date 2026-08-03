with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace draw() touch code with Localized Steep 3D Pit Indentation (Cubic 3.2 Curve + Tight 0.28 Radius)
old_touch_code = """                // 1. Continuous Accumulating Deep 3D Z-Depth Sinking (누르고 있는 시간 동안 지속해서 깊이 쑥 파여 들어감)
                if (isTouching) {
                    touchTime++;

                    // Suction & Z-depth compression factor accumulates CONTINUOUSLY with holding duration (0.15 up to 0.88!)
                    let suctionPower = Math.min(0.88, 0.15 + touchTime * 0.045);
                    
                    // Trigger continuous "드드드드" haptics & deep press pitch glide sound while holding
                    if (touchTime % 5 === 0) {
                        triggerSequentialHaptic();
                        if (touchTime % 10 === 0) playPressSound();
                    }

                    let maxRadius = width * 0.52;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.4);
                            
                            // Pull ALL surrounding mesh nodes CONTINUOUSLY INWARD toward (touchX, touchY) into 3D Z-depth
                            p.x = p.ox + (touchX - p.ox) * weight * suctionPower;
                            p.y = p.oy + (touchY - p.oy) * weight * suctionPower;
                            p.vx *= 0.25; p.vy *= 0.25;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY;
                    }
                } else {"""

new_touch_code = """                // 1. Steep Localized 3D Pit Indentation (누른 곳이 깊숙하게 푹 파이고, 멀어질수록 미세해짐)
                if (isTouching) {
                    touchTime++;

                    // Deep local indentation accumulates smoothly with holding duration (25px up to 90px deep pit!)
                    let deepPitIndentation = Math.min(90, 25 + touchTime * 2.2);

                    if (touchTime % 5 === 0) {
                        triggerSequentialHaptic();
                        if (touchTime % 10 === 0) playPressSound();
                    }

                    // Tight local radius (28% of width) prevents whole character from shrinking!
                    let maxRadius = width * 0.28;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            // Cubic steep falloff (power = 3.2): Center sinks DEEPLY, distant nodes remain untouched!
                            let weight = Math.pow(1 - dist / maxRadius, 3.2);
                            
                            // 1. Steep local Z-depth downward pit
                            p.y = p.oy + deepPitIndentation * weight;

                            // 2. Subtle local inward squeeze at press core
                            p.x = p.ox + (touchX - p.ox) * weight * 0.35;
                            p.vx *= 0.25; p.vy *= 0.25;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY + deepPitIndentation * 0.45;
                    }
                } else {"""

if old_touch_code in content:
    content = content.replace(old_touch_code, new_touch_code)
    print("Successfully replaced touch code in index.html!")
else:
    print("WARNING: old_touch_code not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Steep Localized 3D Pit Indentation Physics in index.html!")
