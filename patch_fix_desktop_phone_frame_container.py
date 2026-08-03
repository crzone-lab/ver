with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update media query so Desktop maintains a clean centered Phone Frame simulator (width: 412px, height: 840px)
old_media_query = """        @media (max-width: 768px), (max-height: 1024px), (orientation: portrait) {"""

new_media_query = """        @media (max-width: 600px) {"""

if old_media_query in content:
    content = content.replace(old_media_query, new_media_query)
    print("100% Successfully updated media query for desktop phone simulator frame!")
else:
    print("WARNING: old_media_query not found!")

# Also add subtle desktop background styling to body for a beautiful desktop presentation
old_body_css = """        body {
            background: #0d0f12;
            color: #fff;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }"""

new_body_css = """        body {
            background: radial-gradient(circle at center, #1e2029 0%, #0a0b0e 100%);
            color: #fff;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }"""

if old_body_css in content:
    content = content.replace(old_body_css, new_body_css)
    print("100% Successfully updated desktop body gradient background!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Desktop Phone Frame Container Fix in index.html!")
