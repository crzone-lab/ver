with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

dup_decl = """        // Stage (All background jellies deleted)
        let decoJellies = [];"""

clean_decl = """        // Background Stage Jellies"""

if dup_decl in content:
    content = content.replace(dup_decl, clean_decl)
    print("100% Successfully removed duplicate let decoJellies declaration!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Duplicate Fix in index.html!")
