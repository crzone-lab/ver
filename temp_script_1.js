
    window.startGameSession = function() {
        console.log("startGameSession executed!");
        var splash = document.getElementById("start-splash-screen");
        if (splash) {
            splash.classList.add("fade-out");
            splash.style.display = "none";
        }
        var lobby = document.getElementById("lobby-screen");
        if (lobby) {
            lobby.style.display = "flex";
            lobby.style.opacity = "1";
            lobby.style.visibility = "visible";
            lobby.style.zIndex = "10000";
        }
        if (typeof setScreenMode === "function") {
            try { setScreenMode("lobby"); } catch(e) {}
        }
        if (typeof renderLobbyGrid === "function") {
            try { renderLobbyGrid(); } catch(e) {}
        }
        try {
            if (typeof bgmPlayer !== "undefined" && bgmPlayer && bgmPlayer.start) {
                bgmPlayer.start();
            }
        } catch(e) {}
        try {
            if (typeof triggerHaptic === "function") {
                triggerHaptic(40);
            }
        } catch(e) {}
    };
