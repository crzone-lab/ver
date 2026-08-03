with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update TOTAL_DECO_SPRITES to 7
old_total = "const TOTAL_DECO_SPRITES = 19;"
new_total = "const TOTAL_DECO_SPRITES = 7;"

if old_total in content:
    content = content.replace(old_total, new_total)
    print("100% Successfully updated TOTAL_DECO_SPRITES to 7!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html!")
