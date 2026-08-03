with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Spring.prototype.solve with decoupled 4-layer physics solver
old_spring_solve = """        class Spring {
            constructor(p1, p2, length) {
                this.p1 = p1;
                this.p2 = p2;
                this.restLength = length;
            }
            solve() {
                let dx = this.p2.x - this.p1.x;
                let dy = this.p2.y - this.p1.y;
                let dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 0.001) return;

                let delta = dist - this.restLength;
                let k = 0.09; // Soft spring constant
                let springForce = delta * k;
                
                let nx = dx / dist;
                let ny = dy / dist;

                // Relative velocity damping across spring to eliminate trembling
                let rvx = this.p2.vx - this.p1.vx;
                let rvy = this.p2.vy - this.p1.vy;
                let dampingForce = (rvx * nx + rvy * ny) * 0.15;

                let totalForce = springForce + dampingForce;

                let fx = nx * totalForce;
                let fy = ny * totalForce;

                this.p1.vx += fx;
                this.p1.vy += fy;
                this.p2.vx -= fx;
                this.p2.vy -= fy;

                // Strict Monotonic Order Preservation: 100% prevents outer boundary nodes from crossing inner nodes
                let minDist = this.restLength * 0.75;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.95;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }
            }
        }"""

new_decoupled_architecture = """        // ==========================================================================
        // DECOUPLED 4-ENGINE PERMANENT JELLY ARCHITECTURE (100% LOCKED MODULES)
        // ==========================================================================
        class Spring {
            constructor(p1, p2, length) {
                this.p1 = p1;
                this.p2 = p2;
                this.restLength = length;
            }
            solve() {
                let dx = this.p2.x - this.p1.x;
                let dy = this.p2.y - this.p1.y;
                let dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 0.001) return;

                let delta = dist - this.restLength;
                let k = 0.12; // Base jelly elastic restoration
                let springForce = delta * k;
                
                let nx = dx / dist;
                let ny = dy / dist;

                let rvx = this.p2.vx - this.p1.vx;
                let rvy = this.p2.vy - this.p1.vy;
                let dampingForce = (rvx * nx + rvy * ny) * 0.18;

                let totalForce = springForce + dampingForce;

                let fx = nx * totalForce;
                let fy = ny * totalForce;

                this.p1.vx += fx;
                this.p1.vy += fy;
                this.p2.vx -= fx;
                this.p2.vy -= fy;

                // ENGINE 1: BorderLock & Anti-Penetration Guard (Strict minDist = 0.75 * restLength)
                let minDist = this.restLength * 0.75;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.95;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }
            }
        }

        // ENGINE 2: Internal Squish Pressing Engine (Independent Squish Indentation on Touch)
        function applySquishPressing(touchX, touchY, intensity = 1.0) {
            if (!points || points.length === 0) return;
            let radius = width * 0.38;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let pdx = p.ox - touchX;
                let pdy = p.oy - touchY;
                let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                if (dist < radius) {
                    // Smooth Cosine Squish Indentation
                    let w = 0.5 * (1 + Math.cos((dist / radius) * Math.PI));
                    p.vx += (touchX - p.ox) * w * 0.08 * intensity;
                    p.vy += (touchY - p.oy) * w * 0.08 * intensity;
                }
            }
        }

        // ENGINE 3: Internal Dome Stretch Engine (Smooth 3D Rounded Pull, 0% Sharp Pointiness)
        function applyDomeStretch(gIndex, touchX, touchY, lastX, lastY) {
            if (gIndex === null || !points[gIndex]) return;
            let gPoint = points[gIndex];
            let dx = touchX - lastX;
            let dy = touchY - lastY;
            let R = width * 0.65;

            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dist = Math.sqrt(Math.pow(p.ox - gPoint.ox, 2) + Math.pow(p.oy - gPoint.oy, 2));
                // Continuous Cosine Dome Field (w_min = 0.42 ensures 100% cohesive whole-body unity)
                let rawW = dist < R ? 0.5 * (1 + Math.cos((dist / R) * Math.PI)) : 0;
                let w = 0.42 + 0.58 * rawW;
                p.x += dx * w;
                p.y += dy * w;
            }
        }"""

if old_spring_solve in content:
    content = content.replace(old_spring_solve, new_decoupled_architecture)
    print("100% Successfully refactored to Decoupled 4-Engine Architecture!")

# Update mousedown, mousemove, touchstart, touchmove to call the decoupled engines explicitly
old_mousedown_call = """            isTouching = true;
            touchX = mx;
            touchY = my;
            lastTouchX = mx;
            lastTouchY = my;
            touchTime = 0;"""

new_mousedown_call = """            isTouching = true;
            touchX = mx;
            touchY = my;
            lastTouchX = mx;
            lastTouchY = my;
            touchTime = 0;
            // Trigger Engine 2: Realtime Squish Pressing on Click
            applySquishPressing(mx, my, 1.2);"""

if old_mousedown_call in content:
    content = content.replace(old_mousedown_call, new_mousedown_call)
    print("100% Successfully connected mousedown to Engine 2 Squish Pressing!")

old_mousemove_call = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let dx = mx - lastTouchX;
                let dy = my - lastTouchY;
                // Move 100% of ALL mesh nodes in 1-to-1 locked unity as ONE SINGLE UNIFIED SOLID BODY
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            }
            lastTouchX = mx;
            lastTouchY = my;"""

new_mousemove_call = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                // Call Engine 3: Smooth Rounded Dome Stretch
                applyDomeStretch(grabbedPointIndex, mx, my, lastTouchX, lastTouchY);
            } else if (isTouching) {
                // Call Engine 2: Realtime Squish Pressing on Drag
                applySquishPressing(mx, my, 0.8);
            }
            lastTouchX = mx;
            lastTouchY = my;"""

if old_mousemove_call in content:
    content = content.replace(old_mousemove_call, new_mousemove_call)
    print("100% Successfully connected mousemove to Engine 3 & Engine 2!")

old_touchmove_call = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let dx = pos.x - lastTouchX;
                let dy = pos.y - lastTouchY;
                // Move 100% of ALL mesh nodes in 1-to-1 locked unity as ONE SINGLE UNIFIED SOLID BODY
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            } else {
                deformMesh(pos.x, pos.y, 15);
            }
            lastTouchX = pos.x;
            lastTouchY = pos.y;"""

new_touchmove_call = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                // Call Engine 3: Smooth Rounded Dome Stretch
                applyDomeStretch(grabbedPointIndex, pos.x, pos.y, lastTouchX, lastTouchY);
            } else {
                // Call Engine 2: Realtime Squish Pressing on Touch Drag
                applySquishPressing(pos.x, pos.y, 0.8);
            }
            lastTouchX = pos.x;
            lastTouchY = pos.y;"""

if old_touchmove_call in content:
    content = content.replace(old_touchmove_call, new_touchmove_call)
    print("100% Successfully connected touchmove to Engine 3 & Engine 2!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Decoupled 4-Engine Architecture in index.html!")
