with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Adjust top logo height to 60px (perfect proportion)
old_logo = 'style="height: 84px; max-width: 320px; object-fit: contain; filter: drop-shadow(0 4px 10px rgba(0,0,0,0.25));"'
new_logo = 'style="height: 60px; max-width: 240px; object-fit: contain; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));"'

if old_logo in content:
    content = content.replace(old_logo, new_logo)
    print("100% Successfully adjusted logo size to 60px!")
else:
    print("WARNING: old_logo not found!")

# 2. Adjust default .lobby-feel-selector top position in CSS
old_feel_css = """        .lobby-feel-selector {
            position: absolute;
            top: 96px;"""

new_feel_css = """        .lobby-feel-selector {
            position: absolute;
            top: 108px;"""

if old_feel_css in content:
    content = content.replace(old_feel_css, new_feel_css)

# 3. Adjust mobile responsive media query positioning
old_mobile_pos = """            .top-overlay-ui {
                top: 16px !important; /* Shift menu higher */
            }
            .lobby-feel-selector {
                top: 80px !important; /* Move feel preset tabs up */
            }"""

new_mobile_pos = """            .top-overlay-ui {
                top: 14px !important;
            }
            .lobby-feel-selector {
                top: 92px !important; /* Clear gap below top icons */
            }"""

if old_mobile_pos in content:
    content = content.replace(old_mobile_pos, new_mobile_pos)
    print("100% Successfully updated mobile responsive positioning for zero overlap!")
else:
    print("WARNING: old_mobile_pos not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Top Header Spacing Fix in index.html!")
