with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace draw() touch code with Continuous Accumulating Deep Suction & Spring Relaxation
old_touch_code = """                // 1. Pure 3D Z-Depth Indentation & Surrounding Inward Suction (Screen Y-Shift = 0)
                if (isTouching) {
                    touchTime++;

                    // Suction & Z-depth compression factor accumulates with holding duration (0.15 up to 0.58)
                    let suctionPower = Math.min(0.58, 0.15 + touchTime * 0.018);
                    
                    let maxRadius = width * 0.48;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.6);
                            
                            // ZERO screen-Y shift! Pull ALL surrounding mesh nodes INWARD toward (touchX, touchY) from 360 degrees
                            p.x = p.ox + (touchX - p.ox) * weight * suctionPower;
                            p.y = p.oy + (touchY - p.oy) * weight * suctionPower;
                            p.vx *= 0.35; p.vy *= 0.35;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY;
                    }
                } else {"""

new_touch_code = """                // 1. Continuous Accumulating Deep 3D Z-Depth Sinking (누르고 있는 시간 동안 지속해서 깊이 쑥 파여 들어감)
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

if old_touch_code in content:
    content = content.replace(old_touch_code, new_touch_code)
    print("Successfully replaced touch code in index.html!")
else:
    print("WARNING: old_touch_code not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Continuous Accumulating Deep Suction Physics in index.html!")
