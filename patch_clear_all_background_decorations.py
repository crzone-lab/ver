with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make generateDecoJellies and drawDecoJellies empty so background is 100% clean with ZERO items
clean_bg_system = """
        // 100% Clean Empty Background Stage (All Background Decorations Removed)
        let decoJellies = [];
        function generateDecoJellies(baseHue) {
            decoJellies = [];
        }
        function drawDecoJellies() {
            // Completely empty - background cleared
            return;
        }
"""

start_marker = "// ==========================================================================\n        // 100% CLEAN REAL PRODUCT GUMMY PHOTO SPRITE ENGINE"
if start_marker not in content:
    start_marker = "let decoJellies = [];"

idx1 = content.find(start_marker)
idx2 = content.find("function handleRecordToggle()", idx1)

if idx1 != -1 and idx2 != -1:
    content = content[:idx1] + clean_bg_system.strip() + "\n\n        " + content[idx2:]
    print("100% Successfully deleted ALL background decorations! Background is 100% clean!")
else:
    print(f"WARNING: Markers not found! idx1: {idx1}, idx2: {idx2}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% Clean Empty Background in index.html!")
