with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace draw() touch code in v1.4.0 with Pure 3D Inward Suction (Screen Y-shift = 0)
old_touch = """                // 1. 3D Sinkhole & Surrounding Inward Suction Physics (누르면 함몰되고 주변 젤리도 중앙으로 쏙 빨려 들어감)
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

new_touch = """                // 1. Pure 3D Inward Suction Physics (Screen Y-Shift = 0: ZERO downward squishing on hover/touch)
                if (isTouching) {
                    touchTime++;

                    let suctionPower = Math.min(0.55, 0.12 + touchTime * 0.015);
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
                } else {"""

if old_touch in content:
    content = content.replace(old_touch, new_touch)
    print("100% Successfully replaced draw touch code!")
else:
    print("WARNING: old_touch not found!")

# Update mousemove so hover without click does NOT set isTouching = true
old_mousemove = """        canvas.addEventListener('mousemove', (e) => {
            if (!isPlaygroundActive() || isAutopilotActive) return;
            if (e.buttons !== 1) {
                // Ignore hover completely if mouse button is NOT pressed
                if (isTouching) releaseGrab(true);
                return;
            }
            let rect = canvas.getBoundingClientRect();
            let scaleX = canvas.width / rect.width;
            let scaleY = canvas.height / rect.height;
            let mx = (e.clientX - rect.left) * scaleX;
            let my = (e.clientY - rect.top) * scaleY;

            touchX = mx;
            touchY = my;
            isTouching = true;
        });"""

new_mousemove = """        canvas.addEventListener('mousemove', (e) => {
            if (!isPlaygroundActive() || isAutopilotActive) return;
            if (e.buttons !== 1) {
                if (isTouching) releaseGrab(true);
                return;
            }
            let rect = canvas.getBoundingClientRect();
            let scaleX = canvas.width / rect.width;
            let scaleY = canvas.height / rect.height;
            let mx = (e.clientX - rect.left) * scaleX;
            let my = (e.clientY - rect.top) * scaleY;

            touchX = mx;
            touchY = my;
            isTouching = true;
        });"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Pure 3D Inward Suction (Screen Y-shift = 0) in index.html!")
