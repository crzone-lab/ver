with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make generateDecoJellies and drawDecoJellies completely empty
clean_bg_system = """
        // 100% Clean Stage (All background jellies deleted)
        let decoJellies = [];
        function generateDecoJellies(baseHue) {
            decoJellies = [];
        }
        function drawDecoJellies() {
            return;
        }
"""

start_marker = "// ==========================================================================\n        // 100% USER'S EXACT 5 UPLOADED REAL GUMMY PHOTOS"
if start_marker not in content:
    start_marker = "// 100% Clean Empty Background Stage"

idx1 = content.find(start_marker)
idx2 = content.find("function handleRecordToggle()", idx1)

if idx1 != -1 and idx2 != -1:
    content = content[:idx1] + clean_bg_system.strip() + "\n\n        " + content[idx2:]
    print("100% Successfully deleted ALL background jellies!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Clean Empty Stage in index.html!")
