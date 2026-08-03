with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Refactor: Ensure clean comments and formatted structure
content = content.replace("<!-- AUTO icon & Photo zone icon removed per user request -->", "")
content = content.replace("<!-- Bottom photo zone & image buttons removed per user request -->", "")
content = content.replace("// Plus bubble removed per user request", "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleaned up comments and refactored index.html!")
