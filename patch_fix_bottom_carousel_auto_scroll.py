with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS: set scroll-behavior: auto; on .bottom-carousel-track
old_track_css = """        .bottom-carousel-track {
            display: flex;
            align-items: center;
            gap: 10px;
            overflow-x: auto;
            scroll-behavior: smooth;"""

new_track_css = """        .bottom-carousel-track {
            display: flex;
            align-items: center;
            gap: 10px;
            overflow-x: auto;
            scroll-behavior: auto;
            -webkit-overflow-scrolling: touch;"""

if old_track_css in content:
    content = content.replace(old_track_css, new_track_css)
    print("100% Successfully updated CSS to scroll-behavior: auto!")

# 2. Update renderBottomCarousel & startBottomCarouselAutoScroll for continuous smooth scrolling
old_carousel_js = """        function renderBottomCarousel() {
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
        }"""

new_carousel_js = """        function renderBottomCarousel() {
            const track = document.getElementById('bottom-carousel-track');
            if (!track) return;
            track.innerHTML = '';

            // Render duplicated set of all 17 fruit rabbit cards for 100% seamless infinite scroll loop
            const fullList = [...lobbyCharacters, ...lobbyCharacters];

            fullList.forEach((char, fullIdx) => {
                const idx = fullIdx % lobbyCharacters.length;
                const card = document.createElement('div');
                card.className = `carousel-char-card ${idx === activeLobbyIndex ? 'active' : ''}`;
                card.id = `carousel-card-${fullIdx}`;
                
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
        }"""

if old_carousel_js in content:
    content = content.replace(old_carousel_js, new_carousel_js)
    print("100% Successfully updated renderBottomCarousel for infinite duplicated track!")

# 3. Update startBottomCarouselAutoScroll step loop
old_scroll_js = """        function startBottomCarouselAutoScroll() {
            const track = document.getElementById('bottom-carousel-track');
            if (!track) return;

            function step() {
                if (!isCarouselHovered && track && true) {
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
        }"""

new_scroll_js = """        function startBottomCarouselAutoScroll() {
            const track = document.getElementById('bottom-carousel-track');
            if (!track) return;

            function step() {
                if (!isCarouselHovered && track) {
                    track.scrollLeft += 0.65; // Smooth continuous leftward scroll
                    
                    let halfWidth = track.scrollWidth / 2;
                    if (track.scrollLeft >= halfWidth) {
                        track.scrollLeft -= halfWidth; // Infinite seamless loop wrap-around
                    }
                }
                carouselAutoScrollTimer = requestAnimationFrame(step);
            }

            if (carouselAutoScrollTimer) cancelAnimationFrame(carouselAutoScrollTimer);
            carouselAutoScrollTimer = requestAnimationFrame(step);

            track.onmouseenter = () => { isCarouselHovered = true; };
            track.onmouseleave = () => { isCarouselHovered = false; };
            track.ontouchstart = () => { isCarouselHovered = true; };
            track.ontouchend = () => {
                setTimeout(() => { isCarouselHovered = false; }, 2500);
            };
        }"""

if old_scroll_js in content:
    content = content.replace(old_scroll_js, new_scroll_js)
    print("100% Successfully updated startBottomCarouselAutoScroll!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Bottom Carousel Auto-Scroll Fix in index.html!")
