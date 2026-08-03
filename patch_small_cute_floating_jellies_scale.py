with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update generateDecoJellies scale parameter from (0.12 ~ 0.44) down to (0.05 ~ 0.15) for cute small background jellies
old_scale = "scale: 0.12 + Math.random() * 0.32,"
new_scale = "scale: 0.05 + Math.random() * 0.10,"

if old_scale in content:
    content = content.replace(old_scale, new_scale)
    print("100% Successfully updated floating jellies scale to cute small sizes!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Cute Small Floating Jellies Scale in index.html!")
