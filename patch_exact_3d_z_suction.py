with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace lines 4597-4630 in index.html with Pure 3D Inward Suction (Screen Y-shift = 0)
old_touch_code = """                // 1. 3D Sinkhole & Surrounding Inward Suction Physics (누르면 함몰되고 주변 젤리도 중앙으로 같이 쏙 빨려 들어감)
                if (isTouching) {
                    touchTime++;

                    // Calculate deep sinkhole depth & strong inward suction power based on press duration
                    let currentSink = Math.min(85, 18 + touchTime * 1.8);
                    let suctionPower = Math.min(0.55, 0.12 + touchTime * 0.015);
                    
                    let maxRadius = width * 0.52;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 1.5);
                            
                            // 1. Downward sinkhole indentation
                            p.y = p.oy + currentSink * weight;

                            // 2. Strong 3D Inward Suction Pulling Surrounding Jelly Mesh Toward (touchX, touchY)
                            let inwardX = (touchX - p.ox) * weight * suctionPower;
                            let inwardY = (touchY - p.oy) * weight * suctionPower * 0.5;
                            p.x = p.ox + inwardX;
                            p.y += inwardY;

                            p.vx *= 0.4; p.vy *= 0.4;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY + currentSink * 0.5;
                    }
                } else {"""

new_touch_code = """                // 1. Pure 3D Z-Depth Indentation & Surrounding Inward Suction (Screen Y-Shift = 0)
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

if old_touch_code in content:
    content = content.replace(old_touch_code, new_touch_code)
    print("Successfully replaced touch code in index.html!")
else:
    print("WARNING: old_touch_code not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Pure 3D Z-Depth Indentation & Surrounding Inward Suction in index.html!")
