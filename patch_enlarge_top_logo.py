with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_logo_html = '<img src="logo_font.png" alt="Logo" style="height: 60px; max-width: 240px; object-fit: contain; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">'
new_logo_html = '<img src="logo_font.png" alt="Logo" style="height: 74px; max-width: 260px; object-fit: contain; filter: drop-shadow(0 4px 10px rgba(0,0,0,0.25)); transition: transform 0.2s ease;">'

if old_logo_html in content:
    content = content.replace(old_logo_html, new_logo_html)
    print("100% Successfully updated top logo size from 60px to 74px!")
else:
    print("WARNING: old_logo_html not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Top Logo Enlargement in index.html!")
