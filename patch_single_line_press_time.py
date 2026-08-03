with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace ONLY the suctionPower formula line for longer press indentation duration
old_line = "let suctionPower = Math.min(0.55, 0.12 + touchTime * 0.015);"
new_line = "let suctionPower = Math.min(0.72, 0.12 + touchTime * 0.005);"

if old_line in content:
    content = content.replace(old_line, new_line)
    print("100% Successfully updated suctionPower press duration line!")
else:
    print("WARNING: old_line not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied single pinpoint change for longer press time in index.html!")
