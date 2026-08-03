with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update applySquishPressing for SUPER DEEP 3D Liquid Indentation
old_squish = """        // ENGINE 2: Morning 3D Liquid Squish Indentation Engine (Deep Bouncy Pressing on Touch/Click)
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            let radius = width * 0.45;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let pdx = p.ox - touchX;
                let pdy = p.oy - touchY;
                let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                if (dist < radius) {
                    let weight = Math.pow(1 - dist / radius, 1.8);
                    p.vx += (touchX - p.ox) * weight * 0.16 * intensity;
                    p.vy += (touchY - p.oy) * weight * 0.16 * intensity;
                }
            }
        }"""

new_squish = """        // ENGINE 2: Super Deep 3D Liquid Squish Indentation Engine
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            let radius = width * 0.48;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.hypot(p.x - touchX, p.y - touchY);
                if (dist < radius) {
                    let weight = Math.pow(1 - dist / radius, 1.5);
                    p.vx += (touchX - p.x) * weight * 0.35 * intensity;
                    p.vy += (touchY - p.y) * weight * 0.35 * intensity;
                }
            }
        }"""

if old_squish in content:
    content = content.replace(old_squish, new_squish)
    print("100% Successfully updated applySquishPressing for super deep liquid squish!")

# 2. Update mousemove and touchmove handlers to call applySquishPressing on click/touch
old_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                // Call Engine 3: Smooth Rounded Dome Stretch
                applyDomeStretch(grabbedPointIndex, mx, my, lastTouchX, lastTouchY);
            } else if (isTouching) {
                // Call Engine 2: Realtime Squish Pressing on Drag
                applySquishPressing(mx, my, 0.8);
            }"""

new_mousemove = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                applyDomeStretch(grabbedPointIndex, mx, my, lastTouchX, lastTouchY);
            } else if (isTouching) {
                applySquishPressing(mx, my, 1.5);
            }"""

if old_mousemove in content:
    content = content.replace(old_mousemove, new_mousemove)
    print("100% Successfully updated mousemove!")

old_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                // Call Engine 3: Smooth Rounded Dome Stretch
                applyDomeStretch(grabbedPointIndex, pos.x, pos.y, lastTouchX, lastTouchY);
            } else {
                // Call Engine 2: Realtime Squish Pressing on Touch Drag
                applySquishPressing(pos.x, pos.y, 0.8);
            }"""

new_touchmove = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                applyDomeStretch(grabbedPointIndex, pos.x, pos.y, lastTouchX, lastTouchY);
            } else {
                applySquishPressing(pos.x, pos.y, 1.5);
            }"""

if old_touchmove in content:
    content = content.replace(old_touchmove, new_touchmove)
    print("100% Successfully updated touchmove!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Super Deep Liquid Squish & Intact Body Drag in index.html!")
