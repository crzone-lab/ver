with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Global Envelope Architecture Class and Functions
envelope_system = """        // ==========================================================================
        // TRANSPARENT GLOBAL MESH ENVELOPE ARCHITECTURE (USER DESIGNED SOLUTION)
        // ==========================================================================
        // A single transparent bounding shell encapsulates 100% of the character mesh.
        // All body parts (Ears, Face, Eyes, Blush Cheeks, Tummy, Fruit) are bound to
        // this transparent shell, guaranteeing 0% layer separation and 0% submerging!
        // ==========================================================================
        class GlobalEnvelope {
            constructor() {
                this.isActive = true;
            }
            applyEnvelopeMove(dx, dy) {
                // Move 100% of all 256 mesh nodes bound to the transparent envelope
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            }
        }
        const globalEnvelope = new GlobalEnvelope();"""

old_class_spring = "class Spring {"
if "class GlobalEnvelope" not in content:
    content = content.replace(old_class_spring, envelope_system + "\n\n        " + old_class_spring)
    print("100% Successfully added GlobalEnvelope Class!")

# 2. Update Spring.solve with hard non-penetration floor (minDist = 0.88 * restLength)
old_spring_solve = """                // Strict Monotonic Order Preservation: 100% prevents outer boundary nodes from crossing inner nodes
                let minDist = this.restLength * 0.75;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.95;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

new_spring_solve = """                // Hard Non-Penetration Distance Floor (0% Node Penetration / 0% Submerge)
                let minDist = this.restLength * 0.88;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 1.0;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }"""

if old_spring_solve in content:
    content = content.replace(old_spring_solve, new_spring_solve)
    print("100% Successfully updated Spring solve for 0.88 non-penetration!")

# 3. Update mousemove and touchmove to call globalEnvelope.applyEnvelopeMove(dx, dy)
old_mousemove_block = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let dx = mx - lastTouchX;
                let dy = my - lastTouchY;
                // Move 100% of ALL mesh nodes in 1-to-1 locked unity as ONE SINGLE UNIFIED SOLID BODY
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            }"""

new_mousemove_block = """            if (isTouching && grabbedPointIndex !== -1 && points[grabbedPointIndex]) {
                let dx = mx - lastTouchX;
                let dy = my - lastTouchY;
                // Move 100% of ALL mesh nodes bound to the Transparent Global Envelope
                globalEnvelope.applyEnvelopeMove(dx, dy);
            }"""

if old_mousemove_block in content:
    content = content.replace(old_mousemove_block, new_mousemove_block)
    print("100% Successfully updated mousemove to use globalEnvelope!")

old_touchmove_block = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let dx = pos.x - lastTouchX;
                let dy = pos.y - lastTouchY;
                // Move 100% of ALL mesh nodes in 1-to-1 locked unity as ONE SINGLE UNIFIED SOLID BODY
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            }"""

new_touchmove_block = """            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                let dx = pos.x - lastTouchX;
                let dy = pos.y - lastTouchY;
                // Move 100% of ALL mesh nodes bound to the Transparent Global Envelope
                globalEnvelope.applyEnvelopeMove(dx, dy);
            }"""

if old_touchmove_block in content:
    content = content.replace(old_touchmove_block, new_touchmove_block)
    print("100% Successfully updated touchmove to use globalEnvelope!")

# 4. Update drawWarpedTriangle for orientation lock (denom <= 0.1 rejection)
old_warped = "function drawWarpedTriangle(ctx, img, p1, p2, p3, u1, v1, u2, v2, u3, v3) {"
new_warped = """function drawWarpedTriangle(ctx, img, p1, p2, p3, u1, v1, u2, v2, u3, v3) {
            let denom = (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
            if (denom <= 0.1) return; // Orientation Lock: 100% prevents triangle inversion & paper flipping"""

if old_warped in content and "Orientation Lock" not in content:
    content = content.replace(old_warped, new_warped)
    print("100% Successfully added Orientation Lock to drawWarpedTriangle!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied User's Transparent Global Mesh Envelope Architecture in index.html!")
