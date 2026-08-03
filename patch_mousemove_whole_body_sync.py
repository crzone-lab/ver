with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update mousemove handler to mirror touchmove 100% whole-body cosine drag vector
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

            let moveDist = Math.sqrt(Math.pow(mx - touchX, 2) + Math.pow(my - touchY, 2));
            if (moveDist > 6) {
                triggerJellyHaptic();
                if (my < touchY) playJellyPullSound();
                else playJellySquishSound();
            }

            touchX = mx;
            touchY = my;
            isTouching = true;

            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = mx - gPoint.x;
                let moveDy = my - gPoint.y;
                
                let dragRadius = width * 0.75;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    let weight = 0.5 + 0.5 * Math.cos((Math.min(dist, dragRadius) / dragRadius) * Math.PI);
                    p.x += moveDx * weight;
                    p.y += moveDy * weight;
                    p.vx *= 0.35;
                    p.vy *= 0.35;
                }
            }
        });"""

if old_mousemove in content:
    content = content.replace(old_mousemove, new_mousemove)
    print("100% Successfully updated mousemove handler in index.html!")
else:
    print("WARNING: old_mousemove not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Synchronized Whole-Body Drag for Mouse & Touch in index.html!")
