with open('v5.5.0_fruit_rabbit_touch_engine.html', 'r', encoding='utf-8') as f:
    v_content = f.read()

# Extract exact style section from v5.5.0
v_style_start = v_content.find('<style>')
v_style_end = v_content.find('</style>')
v_style = v_content[v_style_start:v_style_end + 8]

with open('index.html', 'r', encoding='utf-8') as f:
    i_content = f.read()

i_style_start = i_content.find('<style>')
i_style_end = i_content.find('</style>')

# Replace index.html style section with v5.5.0 exact style section!
new_content = i_content[:i_style_start] + v_style + i_content[i_style_end + 8:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("100% Successfully restored EXACT v5.5.0 CSS styles including Phone Frame Container!")
