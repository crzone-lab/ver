with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update mousemove handler to mirror touchmove whole-body drag logic
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
                
                // 100% UNIFIED WHOLE-BODY MOTION: ALL 100 mesh nodes (hands, fruit, ears, feet) move together in 1-to-1 sync!
                for (let i = 0; i < points.length; i++) {
                    points[i].x += moveDx;
                    points[i].y += moveDy;
                }
            }
        });"""

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

if old_mousemove in content:
    content = content.replace(old_mousemove, new_mousemove)

# Update touchmove handler for 100% UNIFIED WHOLE-BODY MOTION (Zero severing of hands/fruit/ears)
old_touchmove_body = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                
                // 100% Whole-Body Cohesive Drag: Global movement baseline ensures 100% of ALL nodes move together as ONE UNIFIED SOLID 3D JELLY BODY
                let globalCohesion = 0.45;
                for (let i = 0; i < points.length; i++) {
                    points[i].x += moveDx * globalCohesion;
                    points[i].y += moveDy * globalCohesion;
                }

                // Smooth Cosine 3D Round Dome Stretch: Pulls the touched area in a silky-smooth, round 3D jelly dome shape
                let dragRadius = width * 0.55;
                for (let i = 0; i < points.length; i++) {
                    let p = points[i];
                    let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                    if (dist < dragRadius) {
                        // Smooth Cosine Dome Falloff curve (1.0 at center, smoothly curving to 0.0 at edge)
                        let w = Math.cos((dist / dragRadius) * (Math.PI / 2));
                        p.x += moveDx * (1 - globalCohesion) * w;
                        p.y += moveDy * (1 - globalCohesion) * w;
                        p.vx *= 0.35;
                        p.vy *= 0.35;
                    }
                }
            }"""

new_touchmove_body = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let gPoint = points[grabbedPointIndex];
                let moveDx = pos.x - gPoint.x;
                let moveDy = pos.y - gPoint.y;
                
                // 100% UNIFIED WHOLE-BODY MOTION: 100% of ALL 100 mesh nodes (hands, fruit, ears, feet) move together in 1-to-1 sync!
                for (let i = 0; i < points.length; i++) {
                    points[i].x += moveDx;
                    points[i].y += moveDy;
                    points[i].vx *= 0.35;
                    points[i].vy *= 0.35;
                }
            }"""

if old_touchmove_body in content:
    content = content.replace(old_touchmove_body, new_touchmove_body)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% Unified Whole-Body Cohesion (Zero Severing of hands/fruit) in index.html!")
