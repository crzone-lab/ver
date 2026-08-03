with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_unused_block = """        // Stage (All background jellies deleted)
        let decoJellies = [];
        function generateDecoJellies(baseHue) {
            decoJellies = [];
        }"""

if old_unused_block in content:
    content = content.replace(old_unused_block, "        // Stage Area Background Engine")
    print("100% Successfully cleaned old unused generateDecoJellies(baseHue) block!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html!")
