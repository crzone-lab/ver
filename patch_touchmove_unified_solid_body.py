with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

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

print("Applied One Unified Solid Body in index.html!")
