with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

carousel_dom = """        <!-- Bottom 17 Fruit Rabbit Horizontal Auto-Scroll Carousel Selector (Matches User Screenshot) -->
        <div id="bottom-carousel-container" class="bottom-carousel-container">
            <div id="bottom-carousel-track" class="bottom-carousel-track">
                <!-- Dynamically rendered by renderBottomCarousel() -->
            </div>
        </div>"""

if 'id="bottom-carousel-container"' not in content:
    content = content.replace('<canvas id="squishy-canvas" style="width: 100%; height: 100%; display: block;"></canvas>', '<canvas id="squishy-canvas" style="width: 100%; height: 100%; display: block;"></canvas>\n' + carousel_dom)
    print("100% Successfully inserted bottom-carousel-container into HTML DOM!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied DOM insertion fix in index.html!")
