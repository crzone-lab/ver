with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Comment out all deformMesh calls that push mesh nodes downwards
content = content.replace("deformMesh(touchX, touchY, 12);", "// no deformMesh down")
content = content.replace("deformMesh(pos.x, pos.y, 18);", "// no deformMesh down")
content = content.replace("deformMesh(mx, my, 18);", "// no deformMesh down")
content = content.replace("deformMesh(pos.x, pos.y, 15);", "// no deformMesh down")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("100% Removed all downward-pushing deformMesh calls from index.html!")
