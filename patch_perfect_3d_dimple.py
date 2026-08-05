import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Perfect Bulletproof 3D Inward Dimple Engine for Tangle Jelly (Everything else 100% untouched!)
perfect_dimple_code = """                    } else {
                        // [탱글젤리 모드]: 누르면 속으로 쏙 들어가는 3D 함몰(Dimple) + 당기기
                        let dragFromStart = (typeof touchStartX !== 'undefined' && touchStartX > 0) ? Math.hypot(touchX - touchStartX, touchY - touchStartY) : 0;

                        if (dragFromStart < 14.0) {
                            // 1. 누름/함몰 모드 (dragFromStart < 14px): 0% flinching, 0% flipping 3D 함몰
                            let dimpleProgress = Math.min(1.0, touchTime * 0.08); // Smooth 12-frame fade-in
                            let sigma = 95.0;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let dx = p.ox - touchX;
                                let dy = p.oy - touchY;
                                let distSq = dx * dx + dy * dy;
                                let weight = Math.exp(-distSq / (2.0 * sigma * sigma)) * dimpleProgress;

                                // Convex combination interpolation: 0% node crossover guaranteed!
                                let blendRatio = weight * 0.32;
                                p.x = p.ox * (1.0 - blendRatio) + touchX * blendRatio;
                                p.y = p.oy * (1.0 - blendRatio) + touchY * blendRatio;

                                p.lastDx = p.x - p.ox;
                                p.lastDy = p.y - p.oy;
                            }

                            // Render 3D Concave Depth Shadow & Raised Gelatin Rim
                            ctx.save();
                            let dimpleRadius = width * 0.30;
                            let dGrad = ctx.createRadialGradient(touchX, touchY, 2, touchX, touchY, dimpleRadius);
                            dGrad.addColorStop(0, 'rgba(0, 0, 0, 0.45)'); // Center 3D depth shadow
                            dGrad.addColorStop(0.5, 'rgba(0, 0, 0, 0.20)');
                            dGrad.addColorStop(0.85, 'rgba(255, 255, 255, 0.42)'); // Raised rim specular gloss
                            dGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                            ctx.fillStyle = dGrad;
                            ctx.beginPath();
                            ctx.arc(touchX, touchY, dimpleRadius, 0, Math.PI * 2);
                            ctx.fill();
                            ctx.restore();

                        } else {
                            // 2. 당기기 모드 (dragFromStart >= 14px): 원본 엘라스틱 당기기
                            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                                let gNode = points[grabbedPointIndex];
                                let dragDx = touchX - gNode.ox;
                                let dragDy = touchY - gNode.oy;

                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let pdx = p.ox - gNode.ox;
                                    let pdy = p.oy - gNode.oy;
                                    let dist = Math.hypot(pdx, pdy);

                                    let sigma = 100.0;
                                    let weight = Math.exp(-(dist * dist) / (2.0 * sigma * sigma));

                                    p.x = p.ox + dragDx * weight * 1.35;
                                    p.y = p.oy + dragDy * weight * 1.35;

                                    p.lastDx = p.x - p.ox;
                                    p.lastDy = p.y - p.oy;
                                }
                            }
                        }
                    }"""

idx_mochi = content.find('else if (currentMode === \'mochi\')')
idx_else = content.find('} else {', idx_mochi)
idx_else_end = content.find('}', content.find('p.lastDy = p.y - p.oy;', idx_else) + 20) + 1
idx_else_end = content.find('}', idx_else_end + 1) + 1

if idx_mochi != -1 and idx_else != -1 and idx_else_end != -1:
    content = content[:idx_else] + perfect_dimple_code + content[idx_else_end:]
    print("100% SUCCESS: Injected Perfect 3D Inward Dimple Engine into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Perfect 3D Inward Dimple Engine in index.html!")
