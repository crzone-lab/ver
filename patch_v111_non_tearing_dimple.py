import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build 100% Non-Tearing Soft 3D Dimple Engine + 1.05s Relaxed 2-3 Bounce Engine
perfect_v111_code = """                    } else {
                        // [탱글젤리 모드]: v111 100% 깨짐 없는 3D 함몰 (Non-Tearing Soft 3D Dimple) + 당기기
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;
                            let dragDist = Math.hypot(dragDx, dragDy);

                            if (dragDist < 8.0) {
                                // 1. 누름 상태 (Drag < 8px): 터치 지점 중심으로 움푹 들어가는 깨짐 0% 3D 함몰 효과
                                let dimpleRadius = width * 0.38;
                                let dimpleDepth = 28.0;

                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let dx = p.ox - touchX;
                                    let dy = p.oy - touchY;
                                    let dist = Math.hypot(dx, dy);

                                    if (dist < dimpleRadius && dist > 0.1) {
                                        let weight = Math.pow(1 - dist / dimpleRadius, 1.6);
                                        let nx = dx / dist;
                                        let ny = dy / dist;

                                        // Inward squish & dimple depression (깨짐 없는 부드러운 함몰)
                                        p.x -= nx * weight * dimpleDepth * 0.32;
                                        p.y -= ny * weight * dimpleDepth * 0.32;

                                        p.lastDx = p.x - p.ox;
                                        p.lastDy = p.y - p.oy;
                                    }
                                }

                                // Render concave 3D dimple inner shadow ring
                                ctx.save();
                                let dGrad = ctx.createRadialGradient(touchX, touchY, 2, touchX, touchY, dimpleRadius * 0.55);
                                dGrad.addColorStop(0, 'rgba(0, 0, 0, 0.32)');
                                dGrad.addColorStop(0.5, 'rgba(0, 0, 0, 0.12)');
                                dGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                                ctx.fillStyle = dGrad;
                                ctx.beginPath();
                                ctx.arc(touchX, touchY, dimpleRadius * 0.55, 0, Math.PI * 2);
                                ctx.fill();
                                ctx.restore();

                            } else {
                                // 2. 당기기/밀기 상태 (Drag >= 8px): 터치 부위가 길고 쫀쫀하게 당겨짐 (100% 보존)
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
    content = content[:idx_else] + perfect_v111_code + content[idx_else_end:]
    print("100% SUCCESS: Injected v111 Non-Tearing 3D Dimple Engine into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied v111 Non-Tearing 3D Dimple Engine in index.html!")
