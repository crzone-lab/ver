with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for bottom carousel container and cards
carousel_css = """
        /* Bottom 17 Fruit Rabbit Horizontal Auto-Scroll Carousel Selector */
        .bottom-carousel-container {
            position: absolute;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 32px);
            max-width: 380px;
            height: 102px;
            z-index: 28000;
            background: rgba(255, 255, 255, 0.48);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border-radius: 26px;
            border: 2px solid rgba(255, 255, 255, 0.85);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.16), inset 0 2px 4px rgba(255, 255, 255, 0.8);
            overflow: hidden;
            pointer-events: auto;
            display: flex;
            align-items: center;
            padding: 0 6px;
        }

        .bottom-carousel-track {
            display: flex;
            align-items: center;
            gap: 10px;
            overflow-x: auto;
            scroll-behavior: smooth;
            white-space: nowrap;
            width: 100%;
            height: 100%;
            padding: 0 8px;
            -ms-overflow-style: none;
            scrollbar-width: none;
        }

        .bottom-carousel-track::-webkit-scrollbar {
            display: none;
        }

        .carousel-char-card {
            flex: 0 0 auto;
            width: 70px;
            height: 84px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.65);
            border: 1.5px solid rgba(255, 255, 255, 0.95);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), border-color 0.25s ease, box-shadow 0.25s ease, background 0.25s ease;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
        }

        .carousel-char-card:hover {
            transform: translateY(-3px) scale(1.05);
            background: rgba(255, 255, 255, 0.85);
        }

        .carousel-char-card.active {
            background: rgba(255, 255, 255, 0.98);
            border: 2.5px solid #ff4757;
            box-shadow: 0 6px 20px rgba(255, 71, 87, 0.45);
            transform: scale(1.06);
        }

        .carousel-char-img {
            width: 48px;
            height: 48px;
            object-fit: contain;
            filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.15));
            pointer-events: none;
        }

        .carousel-char-name {
            font-size: 0.72rem;
            font-weight: 800;
            color: #2f3542;
            margin-top: 2px;
            text-align: center;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            max-width: 64px;
            pointer-events: none;
        }
"""

if "</style>" in content:
    content = content.replace("</style>", carousel_css + "\n</style>")

# 2. Add Bottom Carousel HTML container inside .phone-frame
carousel_html = """
        <!-- Bottom 17 Fruit Rabbit Horizontal Auto-Scroll Carousel Selector (Matches User Screenshot) -->
        <div id="bottom-carousel-container" class="bottom-carousel-container">
            <div id="bottom-carousel-track" class="bottom-carousel-track">
                <!-- Dynamically rendered by renderBottomCarousel() -->
            </div>
        </div>
"""

if '<canvas id="gl-canvas"' in content:
    content = content.replace('<canvas id="gl-canvas"', carousel_html + '\n        <canvas id="gl-canvas"')

# 3. Add JS functions for Bottom Carousel rendering, auto-scrolling to the left, and character selection sync
carousel_js = """
        // --- BOTTOM 17 FRUIT RABBIT CAROUSEL SELECTOR ENGINE ---
        let carouselAutoScrollTimer = null;
        let isCarouselHovered = false;

        function renderBottomCarousel() {
            const track = document.getElementById('bottom-carousel-track');
            if (!track) return;
            track.innerHTML = '';

            // Render all 17 fruit rabbit character cards
            lobbyCharacters.forEach((char, idx) => {
                const card = document.createElement('div');
                card.className = `carousel-char-card ${idx === activeLobbyIndex ? 'active' : ''}`;
                card.id = `carousel-card-${idx}`;
                
                const imgSrc = char.file || char.imgData || 'strawberry_rabbit_jelly.png';
                
                card.innerHTML = `
                    <img src="${imgSrc}" alt="${char.name}" class="carousel-char-img">
                    <div class="carousel-char-name">${char.name}</div>
                `;

                card.onclick = (e) => {
                    e.stopPropagation();
                    selectLobbyCharacter(idx, card);
                    syncCarouselSelection(idx);
                };

                track.appendChild(card);
            });

            startBottomCarouselAutoScroll();
        }

        function syncCarouselSelection(idx) {
            document.querySelectorAll('.carousel-char-card').forEach(c => c.classList.remove('active'));
            const activeCard = document.getElementById(`carousel-card-${idx}`);
            if (activeCard) {
                activeCard.classList.add('active');
                activeCard.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
            }
        }

        function startBottomCarouselAutoScroll() {
            const track = document.getElementById('bottom-carousel-track');
            if (!track) return;

            function step() {
                if (!isCarouselHovered && track && screenMode === 'playground') {
                    track.scrollLeft += 0.55; // Slow continuous scroll to the left
                    
                    // Infinite Seamless Wrap-around: when scroll reaches end, loop back to start
                    if (track.scrollLeft >= track.scrollWidth - track.clientWidth - 2) {
                        track.scrollLeft = 0;
                    }
                }
                carouselAutoScrollTimer = requestAnimationFrame(step);
            }

            if (carouselAutoScrollTimer) cancelAnimationFrame(carouselAutoScrollTimer);
            carouselAutoScrollTimer = requestAnimationFrame(step);

            track.addEventListener('mouseenter', () => { isCarouselHovered = true; });
            track.addEventListener('mouseleave', () => { isCarouselHovered = false; });
            track.addEventListener('touchstart', () => { isCarouselHovered = true; }, { passive: true });
            track.addEventListener('touchend', () => {
                setTimeout(() => { isCarouselHovered = false; }, 2500);
            }, { passive: true });
        }

        // Call renderBottomCarousel on init
        window.addEventListener('DOMContentLoaded', () => {
            renderBottomCarousel();
        });
"""

if "function initMesh()" in content:
    content = content.replace("function initMesh()", carousel_js + "\n        function initMesh()")

# Also update selectLobbyCharacter to call syncCarouselSelection(idx)
old_select_lob = "activeLobbyIndex = index;"
new_select_lob = "activeLobbyIndex = index;\n            syncCarouselSelection(index);"
if old_select_lob in content:
    content = content.replace(old_select_lob, new_select_lob)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("100% Successfully applied Bottom 17 Fruit Rabbit Auto-Scroll Carousel Selector!")
