
        window.addEventListener('DOMContentLoaded', function() {
            try {
                if (typeof setScreenMode === 'function') setScreenMode('splash');
            } catch(e) {}
        });
    // Guaranteed global touch handler registration
        function handleGlobalTouchStart(e) {
            const splash = document.getElementById('start-splash-screen');
            if (splash && splash.style.display !== 'none' && !splash.classList.contains('fade-out')) return;
            let touch = e.touches ? e.touches[0] : e;
            if (!touch) return;
            let rect = canvas.getBoundingClientRect();
            let tx = (touch.clientX - rect.left) * (canvas.width / rect.width);
            let ty = (touch.clientY - rect.top) * (canvas.height / rect.height);
            
            let minDist = 999999;
            let closestIdx = null;
            for (let i = 0; i < points.length; i++) {
                let dx = points[i].x - tx;
                let dy = points[i].y - ty;
                let d = dx*dx + dy*dy;
                if (d < minDist) { minDist = d; closestIdx = i; }
            }
            if (closestIdx !== null && minDist < (width * 0.45) * (width * 0.45)) {
                grabbedPointIndex = closestIdx;
                isTouching = true;
                touchX = tx;
                touchY = ty;
                touchStartX = tx;
                touchStartY = ty;
            }
        }

        function handleGlobalTouchMove(e) {
            if (!isTouching) return;
            let touch = e.touches ? e.touches[0] : e;
            if (!touch) return;
            let rect = canvas.getBoundingClientRect();
            touchX = (touch.clientX - rect.left) * (canvas.width / rect.width);
            touchY = (touch.clientY - rect.top) * (canvas.height / rect.height);
            try { e.preventDefault(); } catch(err) {}
        }

        function handleGlobalTouchEnd() {
            isTouching = false;
            grabbedPointIndex = null;
        }

        // Handlers delegated cleanly to canvas scope
