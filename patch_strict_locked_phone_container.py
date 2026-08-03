with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update .phone-frame CSS to strictly lock width: 412px and height: 840px on desktop PC/Mac
old_frame_css = """        .phone-frame {
            width: 412px;
            height: 840px;
            background: #000;
            border-radius: 48px;
            border: 12px solid var(--phone-border);
            position: relative;
            overflow: hidden;
            box-shadow: 0 25px 60px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
        }"""

new_frame_css = """        .phone-frame {
            width: 412px !important;
            height: 840px !important;
            max-width: 412px !important;
            max-height: 840px !important;
            margin: auto !important;
            flex-shrink: 0 !important;
            background: #000;
            border-radius: 48px !important;
            border: 12px solid #232a37 !important;
            position: relative;
            overflow: hidden;
            box-shadow: 0 25px 60px rgba(0,0,0,0.85), 0 0 0 1px rgba(255,255,255,0.1);
            display: flex;
            flex-direction: column;
        }"""

if old_frame_css in content:
    content = content.replace(old_frame_css, new_frame_css)
    print("100% Successfully updated .phone-frame CSS for STRICT DESKTOP PHONE CONTAINER LOCK!")

# Also update media query so max-width is only applied on mobile touch devices (max-width: 480px)
old_media = "@media (max-width: 600px) {"
new_media = "@media (max-width: 480px) and (pointer: coarse) {"

if old_media in content:
    content = content.replace(old_media, new_media)
    print("100% Successfully restricted mobile fullscreen to pointer: coarse devices!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Strict Desktop Phone Container Lock in index.html!")
