with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update mousemove handler to apply 1-to-1 rigid shift across ALL 100 points
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

            if (isTouching && grabbedPointIndex !== -1) {
                let dx = mx - lastTouchX;
                let dy = my - lastTouchY;
                // Move 100% of ALL 100 mesh nodes and anchor origins together as ONE UNIFIED SOLID BODY
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                    points[i].ox += dx;
                    points[i].oy += dy;
                }
            }

            lastTouchX = mx;
            lastTouchY = my;
            touchX = mx;
            touchY = my;
            isTouching = true;
        });"""

if old_mousemove in content:
    content = content.replace(old_mousemove, new_mousemove)
    print("100% Successfully updated mousemove for ONE UNIFIED SOLID BODY!")
else:
    print("WARNING: old_mousemove not found!")

# 2. Update touchmove handler similarly
old_touchmove = """        canvas.addEventListener('touchmove', (e) => {
            if (!isPlaygroundActive() || isAutopilotActive) return;
            let rect = canvas.getBoundingClientRect();
            let scaleX = canvas.width / rect.width;
            let scaleY = canvas.height / rect.height;
            let tx = (e.touches[0].clientX - rect.left) * scaleX;
            let ty = (e.touches[0].clientY - rect.top) * scaleY;

            touchX = tx;
            touchY = ty;
            isTouching = true;
        });"""

new_touchmove = """        canvas.addEventListener('touchmove', (e) => {
            if (!isPlaygroundActive() || isAutopilotActive) return;
            let rect = canvas.getBoundingClientRect();
            let scaleX = canvas.width / rect.width;
            let scaleY = canvas.height / rect.height;
            let tx = (e.touches[0].clientX - rect.left) * scaleX;
            let ty = (e.touches[0].clientY - rect.top) * scaleY;

            if (isTouching && grabbedPointIndex !== -1) {
                let dx = tx - lastTouchX;
                let dy = ty - lastTouchY;
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                    points[i].ox += dx;
                    points[i].oy += dy;
                }
            }

            lastTouchX = tx;
            lastTouchY = ty;
            touchX = tx;
            touchY = ty;
            isTouching = true;
        });"""

if old_touchmove in content:
    content = content.replace(old_touchmove, new_touchmove)
    print("100% Successfully updated touchmove for ONE UNIFIED SOLID BODY!")
else:
    print("WARNING: old_touchmove not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied One Unified Solid Body Physics in index.html!")
