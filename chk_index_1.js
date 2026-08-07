
    window.startGameSession = function() {
        console.log("startGameSession executed!");
        var splash = document.getElementById("start-splash-screen");
        if (splash) {
            splash.style.display = "none";
            splash.style.opacity = "0";
            splash.style.pointerEvents = "none";
        }

        var canvas = document.getElementById("canvas");
        if (canvas) {
            canvas.style.display = "block";
            canvas.style.visibility = "visible";
            canvas.style.opacity = "1";
            canvas.style.zIndex = "10";
        }

        var feelUI = document.querySelector(".lobby-feel-selector");
        if (feelUI) {
            feelUI.style.display = "flex";
            feelUI.style.zIndex = "25000";
            feelUI.style.pointerEvents = "none";
        }

        var topUI = document.querySelector(".top-overlay-ui");
        if (topUI) {
            topUI.style.display = "flex";
            topUI.style.zIndex = "30000";
            topUI.style.pointerEvents = "none";
        }

        if (typeof selectLobbyCharacter === "function") {
            selectLobbyCharacter(0, null);
        }
        if (typeof initMesh === "function") initMesh();
        if (typeof draw === "function") draw();
    };
