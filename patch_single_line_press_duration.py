with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace ONLY the zDepthCompression formula rate to accumulate over a much longer duration
old_line = "let zDepthCompression = Math.min(0.85, 0.20 + touchTime * 0.04);"
new_line = "let zDepthCompression = Math.min(0.88, 0.20 + touchTime * 0.008);"

if old_line in content:
    content = content.replace(old_line, new_line)
    print("100% Successfully updated zDepthCompression duration rate!")
else:
    print("WARNING: old_line not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied single pinpoint change for longer press indentation duration in index.html!")
