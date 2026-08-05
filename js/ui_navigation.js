// ==========================================
// 📱 AGY UI Navigation & Screen State Module
// ==========================================

function setScreenMode(mode) {
    try {
        const lobby = document.getElementById("lobby-screen");
        const splash = document.getElementById("start-splash-screen");
        const btn = document.getElementById("global-home-exit-btn") || document.getElementById("home-btn");
        const topUI = document.querySelector(".top-overlay-ui");
        const feelUI = document.querySelector(".lobby-feel-selector");

        document.querySelectorAll('.pop-overlay').forEach(el => el.style.display = 'none');

        if (mode === "splash") {
            if (splash) {
                splash.style.display = "flex";
                splash.style.opacity = "1";
                splash.style.visibility = "visible";
                splash.style.zIndex = "30000";
                splash.style.pointerEvents = "auto";
            }
            if (lobby) {
                lobby.style.display = "none";
                lobby.style.opacity = "0";
                lobby.style.visibility = "hidden";
                lobby.style.zIndex = "-1";
                lobby.style.pointerEvents = "none";
            }
            if (topUI) topUI.style.display = "none";
            if (feelUI) feelUI.style.display = "none";
        } else if (mode === "lobby") {
            if (splash) { splash.style.display = "none"; splash.style.opacity = "0"; splash.style.pointerEvents = "none"; }
            if (lobby) {
                lobby.style.display = "flex";
                lobby.style.opacity = "1";
                lobby.style.visibility = "visible";
                lobby.style.zIndex = "10000";
                lobby.style.pointerEvents = "auto";
            }
            if (topUI) { topUI.style.display = "flex"; topUI.style.zIndex = "20000"; }
            if (feelUI) { feelUI.style.display = "flex"; feelUI.style.zIndex = "20000"; }

            if (btn) {
                btn.innerHTML = '<img src="out.png" alt="나가기" style="width: 32px; height: 32px; object-fit: contain;">';
                btn.onclick = typeof exitGame === 'function' ? exitGame : null;
                btn.title = "나가기";
            }
        } else if (mode === "playground") {
            if (splash) { splash.style.display = "none"; splash.style.opacity = "0"; splash.style.pointerEvents = "none"; }
            if (lobby) {
                lobby.style.display = "none";
                lobby.style.opacity = "0";
                lobby.style.visibility = "hidden";
                lobby.style.zIndex = "-1";
                lobby.style.pointerEvents = "none";
            }
            const canvasEl = document.getElementById("main-canvas");
            if (canvasEl) {
                canvasEl.style.display = "block";
                canvasEl.style.pointerEvents = "auto";
            }
            if (topUI) { topUI.style.display = "flex"; topUI.style.zIndex = "20000"; }
            if (feelUI) { feelUI.style.display = "flex"; feelUI.style.zIndex = "20000"; }
            const bottomCarousel = document.getElementById("bottom-carousel-container");
            if (bottomCarousel) {
                bottomCarousel.style.display = "flex";
                bottomCarousel.style.zIndex = "28000";
            }
            if (typeof renderBottomCarousel === 'function') renderBottomCarousel();

            if (btn) {
                btn.innerHTML = '<img src="home.png" alt="홈으로" style="width: 32px; height: 32px; object-fit: contain;">';
                btn.onclick = typeof goBackToLobby === 'function' ? goBackToLobby : null;
                btn.title = "홈으로";
            }
        }
    } catch(err) {
        console.error("[UI Module Error in setScreenMode]", err);
    }
}

function selectLobbyCharacter(index, element) {
    try {
        if (typeof stopAutopilot === 'function') stopAutopilot();
        if (typeof releaseGrab === 'function') { releaseGrab(true); releaseGrab(true); }
        
        activeLobbyIndex = index;
        try { syncCarouselSelection(index); } catch(e) {}

        const char = typeof lobbyCharacters !== 'undefined' ? lobbyCharacters[index] : null;
        if (!char) return;

        activeEmoji = char.emoji || '🐰';
        activeBase = char.base;
        activeHue = char.hue || 350;

        const splash = document.getElementById('start-splash-screen');
        if (splash) {
            splash.classList.add('fade-out');
            splash.style.display = 'none';
        }

        const imageSrc = char.imgData || char.file || "strawberry_rabbit_jelly.png";

        jellyImage.onload = function() {
            bakedJellyTexture = jellyImage;
            if (typeof bakeSingleCompositeTexture === 'function') {
                bakeSingleCompositeTexture(jellyImage);
            }
            if (typeof initMesh === 'function') initMesh();
            if (typeof draw === 'function') draw();
        };

        jellyImage.src = imageSrc;
        bakedJellyTexture = jellyImage;

        if (jellyImage.complete && jellyImage.naturalWidth > 0) {
            if (typeof initMesh === 'function') initMesh();
            if (typeof draw === 'function') draw();
        }

        if (typeof initMesh === 'function') initMesh();
        if (typeof generateDecoJellies === 'function') generateDecoJellies(activeHue);
        setScreenMode("playground");
        if (typeof showNotification === 'function') {
            showNotification((char.name || char.title || '토끼') + " 선택되었습니다!");
        }

        document.querySelectorAll('.grid-char-bubble').forEach(b => b.classList.remove('active'));
        if (element) {
            element.classList.add('active');
        } else {
            const bubbles = document.querySelectorAll('.grid-char-bubble');
            if (bubbles[index]) {
                bubbles[index].classList.add('active');
            }
        }
    } catch(err) {
        console.error("[UI Module Error in selectLobbyCharacter]", err);
    }
}
