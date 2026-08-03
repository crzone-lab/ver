with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace draw() touch code with Long-Duration 5-Second Continuous Deep Z-Sinking
old_touch_code = """                // 1. Pure 3D Z-Depth Sinking Right Under Finger (Screen Y-Shift = 0)
                if (isTouching) {
                    touchTime++;

                    // Compression factor accumulates continuously into 3D Z-depth (0.20 up to 0.85)
                    let zDepthCompression = Math.min(0.85, 0.20 + touchTime * 0.04);

                    if (touchTime % 4 === 0) {
                        triggerJellyHaptic();
                        if (touchTime % 8 === 0) playJellySquishSound();
                    }

                    // Localized influence radius (30% of width)
                    let maxRadius = width * 0.30;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 2.5);
                            
                            // ZERO screen-Y shift towards bottom of screen!
                            // All points converge 360 degrees directly UNDER THE FINGER into 3D Z-depth
                            p.x = p.ox + (touchX - p.ox) * weight * zDepthCompression;
                            p.y = p.oy + (touchY - p.oy) * weight * zDepthCompression;
                            p.vx *= 0.25; p.vy *= 0.25;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY;
                    }
                } else {"""

new_touch_code = """                // 1. Long-Duration 5-Second Continuous Deep Z-Sinking (누르고 있는 5초 이상 오랫동안 지속해서 쑥 파여 들어감)
                if (isTouching) {
                    touchTime++;

                    // Smooth continuous Z-depth compression factor accumulates for 5+ full seconds (0.18 up to 0.95!)
                    let zDepthCompression = Math.min(0.95, 0.18 + touchTime * 0.007);

                    // Expanding suction pool as duration increases
                    let currentRadiusRatio = Math.min(0.42, 0.24 + touchTime * 0.0006);

                    if (touchTime % 8 === 0) {
                        triggerJellyHaptic();
                        if (touchTime % 16 === 0) playJellySquishSound();
                    }

                    let maxRadius = width * currentRadiusRatio;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 2.2);
                            
                            // ZERO screen-Y shift! All mesh points converge 360 degrees directly UNDER THE FINGER into deep 3D Z-depth
                            p.x = p.ox + (touchX - p.ox) * weight * zDepthCompression;
                            p.y = p.oy + (touchY - p.oy) * weight * zDepthCompression;
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

print("Applied Long-Duration 5-Second Continuous Deep Z-Sinking in index.html!")
