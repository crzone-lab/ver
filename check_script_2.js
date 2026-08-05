
        // Escape KakaoTalk in-app browser to default mobile browser for full features and support
        if (/KAKAOTALK/i.test(navigator.userAgent)) {
            if (navigator.userAgent.match(/Android/i)) {
                location.href = 'intent://' + location.host + location.pathname + location.search + '#Intent;scheme=https;end';
            } else {
                location.href = 'kakaotalk://web/openExternal?url=' + encodeURIComponent(location.href);
            }
        }

        const canvas = document.getElementById('squishy-canvas');
        const ctx = canvas.getContext('2d');

        // Handle page visibility change (exit/suspend/pause game & sounds)
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                stopAutopilot(); releaseGrab(true); releaseGrab(true);
                if (audioCtx && audioCtx.state === 'running') {
                    audioCtx.suspend();
                }
                if (typeof bgmPlayer !== 'undefined' && bgmPlayer.stop) {
                    bgmPlayer.stop();
                }
            } else {
                if (audioCtx && audioCtx.state === 'suspended') {
                    audioCtx.resume();
                }
                const splash = document.getElementById('start-splash-screen');
                if (splash && splash.classList.contains('fade-out')) {
                    if (typeof bgmPlayer !== 'undefined' && bgmPlayer.start) {
                        bgmPlayer.start();
                    }
                }
            }
        });

        const i18n = {
            lang: 'en',
            dict: {
                ko: {
                    "btn-gamestart": "게임 시작",
                    "pill-jelly": "탱글젤리",
                    "pill-mochi": "쫀득모찌",
                    "pill-slime": "슬라임",
                    "btn-exit": "게임나가기",
                    "btn-setting": "설정",
                    "btn-auto": "오토파일럿 테스트",
                    "btn-photo": "사진 촬영",
                    "btn-rec": "영상 녹화",
                    "btn-rec-stop": "녹화 중지",
                    "rec-status": "촬영중",
                    "rec-stop": "정지",
                    "opt-photozone": "포토존",
                    "opt-import": "이미지",
                    "pop-char-title": "🐰 캐릭터 선택",
                    "card-strawberry": "🍓 딸기 토끼",
                    "card-lemon": "🍋 레몬 토끼",
                    "card-peach": "🍑 복숭아 토끼",
                    "card-camera": "내 사진 (얼굴)",
                    "card-illust": "캐릭터 가져오기",
                    "pop-feel-title": "🍮 촉감 선택 (Feel Preset)",
                    "card-feel-jelly": "탱글 젤리",
                    "card-feel-mochi": "쫀득 모찌",
                    "card-feel-slime": "슬라임",
                    "btn-recreate": "다시 만들기",
                    "btn-save-gallery": "갤러리 저장",
                    "btn-reset-settings": "설정 초기화",
                    "label-stiffness": "Spring Stiffness",
                    "label-damping": "Damping",
                    "label-bgm": "BGM 볼륨",
                    "pop-result-title": "🎬 비디오 녹화 미리보기",
                    "btn-home": "홈/메인",
                    "notif-slime": "💧 촉감 프리셋: 슬라임 모드 전환!",
                    "notif-jelly": "🍮 촉감 프리셋: 탱글젤리 모드 전환!",
                    "notif-mochi": "🍡 촉감 프리셋: 쫀득모찌 모드 전환!",
                    "notif-exit": "🚪 게임을 종료하고 로비 설정을 초기화합니다.",
                    "notif-reset-lobby": "🔄 메인 로비 설정 초기화 완료!",
                    "notif-reset-settings": "🔄 물리 및 촉감 설정이 초기화되었습니다!",
                    "notif-rec-complete": "🎬 MP4 영상 녹화가 완료되었습니다. 공유가 가능합니다!",
                    "notif-auto-start": "🤖 오토파일럿 시작!",
                    "notif-auto-stop": "🤖 오토파일럿 중지.",
                    "notif-snapshot": "📸 사진 캡처 완료! 미디어 갤러리에 저장되었습니다.",
                    "notif-char-loaded": "🐰 새 캐릭터가 로드되었습니다!",
                    "notif-feel-sync": "🍮 촉감 프리셋 동기화 완료!",
                    "notif-char-loaded-base": "젤리 캐릭터 불러오기 완료!",
                    "notif-silhouette-mapping": "📸 캐릭터 실루엣 젤리 매핑 완료! 플레이그라운드 활성화!",
                    "notif-illust-crop": "캐릭터 전체 크롭: 젤리 메쉬 자동 생성!",
                    "preview-snapshot-saved": "스냅샷 이미지가 갤러리에 저장되었습니다!",
                    "notif-gallery-saved": "🎬 MP4 영상 파일이 미디어 갤러리에 저장되었습니다.",
                    "notif-char-loaded-play": "로드 완료! 플레이그라운드 활성화!",
                    "word-rabbit": "토끼",
                    "fruit-strawberry_rabbit": "딸기",
                    "fruit-lemon_rabbit": "레몬",
                    "fruit-peach_rabbit": "복숭아",
                    "fruit-grape_rabbit": "포도",
                    "fruit-kiwi_rabbit": "키위",
                    "fruit-watermelon_rabbit": "수박",
                    "fruit-orange_rabbit": "오렌지",
                    "fruit-cherry_rabbit": "체리",
                    "fruit-apple_rabbit": "사과",
                    "fruit-banana_rabbit": "바나나",
                    "fruit-pineapple_rabbit": "파인애플",
                    "fruit-mango_rabbit": "망고",
                    "fruit-melon_rabbit": "멜론",
                    "fruit-blueberry_rabbit": "블루베리",
                    "fruit-coconut_rabbit": "코코넛",
                    "fruit-avocado_rabbit": "아보카도",
                    "fruit-pear_rabbit": "배",
                    "fruit-tangerine_rabbit": "귤",
                    "fruit-tomato_rabbit": "토마토",
                    "fruit-carrot_rabbit": "당근",
                    "btn-toggle-fullscreen": "전체화면 토글",
                    "notif-fullscreen-error": "전체화면을 지원하지 않는 브라우저/환경입니다.",
                    "notif-fullscreen-entered": "🖥️ 전체화면 모드가 활성화되었습니다!",
                    "notif-fullscreen-exited": "🚪 전체화면 모드가 해제되었습니다.",
                    "cam-retake": "다시찍기",
                    "cam-save": "저장",
                    "cam-facing-label": "화면전환",
                    "cam-exit-label": "나가기",
                    "cam-guide-text": "이 영역 안에 얼굴을 맞춰주세요",
                    "cam-draw-guide-text": "손가락으로 얼굴 외곽선을 그려서 잘라보세요! (안 그리면 기본 타원으로 저장)"
                },
                en: {
                    "btn-gamestart": "Game Start",
                    "pill-jelly": "Tangle Jelly",
                    "pill-mochi": "Chewy Mochi",
                    "pill-slime": "Slime",
                    "btn-exit": "Exit Game",
                    "btn-setting": "Settings",
                    "btn-auto": "Autopilot Test",
                    "btn-photo": "Take Photo",
                    "btn-rec": "Record Video",
                    "btn-rec-stop": "Stop Record",
                    "rec-status": "Recording",
                    "rec-stop": "Stop",
                    "opt-photozone": "Photo Zone",
                    "opt-import": "Image",
                    "pop-char-title": "🐰 Select Character",
                    "card-strawberry": "🍓 Strawberry Rabbit",
                    "card-lemon": "🍋 Lemon Rabbit",
                    "card-peach": "🍑 Peach Rabbit",
                    "card-camera": "My Photo (Face)",
                    "card-illust": "Import Character",
                    "pop-feel-title": "🍮 Feel Presets",
                    "card-feel-jelly": "Tangle Jelly",
                    "card-feel-mochi": "Chewy Mochi",
                    "card-feel-slime": "Slime",
                    "btn-recreate": "Recreate",
                    "btn-save-gallery": "Save Gallery",
                    "btn-reset-settings": "Reset Settings",
                    "label-stiffness": "Spring Stiffness",
                    "label-damping": "Damping",
                    "label-bgm": "BGM Volume",
                    "pop-result-title": "🎬 Video Recording Preview",
                    "btn-home": "Home",
                    "notif-slime": "💧 Feel Preset: Slime mode active!",
                    "notif-jelly": "🍮 Feel Preset: Tangle Jelly active!",
                    "notif-mochi": "🍡 Feel Preset: Chewy Mochi active!",
                    "notif-exit": "🚪 Exiting game and resetting lobby settings.",
                    "notif-reset-lobby": "🔄 Main lobby settings reset complete!",
                    "notif-reset-settings": "🔄 Physics and feel settings have been reset!",
                    "notif-rec-complete": "🎬 MP4 recording complete! Ready to share.",
                    "notif-auto-start": "🤖 Autopilot started!",
                    "notif-auto-stop": "🤖 Autopilot stopped.",
                    "notif-snapshot": "📸 Photo capture complete! Saved to gallery.",
                    "notif-char-loaded": "🐰 New character loaded successfully!",
                    "notif-feel-sync": "🍮 Feel preset synced!",
                    "notif-char-loaded-base": "Jelly character loaded successfully!",
                    "notif-silhouette-mapping": "📸 Silhouette mapping complete! Playground activated!",
                    "notif-illust-crop": "Full character cropped: Jelly mesh auto-generated!",
                    "preview-snapshot-saved": "Snapshot image saved to gallery!",
                    "notif-gallery-saved": "🎬 MP4 video file saved to media gallery.",
                    "notif-char-loaded-play": "loaded! Playground activated!",
                    "word-rabbit": "Rabbit",
                    "fruit-strawberry_rabbit": "Strawberry",
                    "fruit-lemon_rabbit": "Lemon",
                    "fruit-peach_rabbit": "Peach",
                    "fruit-grape_rabbit": "Grape",
                    "fruit-kiwi_rabbit": "Kiwi",
                    "fruit-watermelon_rabbit": "Watermelon",
                    "fruit-orange_rabbit": "Orange",
                    "fruit-cherry_rabbit": "Cherry",
                    "fruit-apple_rabbit": "Apple",
                    "fruit-banana_rabbit": "Banana",
                    "fruit-pineapple_rabbit": "Pineapple",
                    "fruit-mango_rabbit": "Mango",
                    "fruit-melon_rabbit": "Melon",
                    "fruit-blueberry_rabbit": "Blueberry",
                    "fruit-coconut_rabbit": "Coconut",
                    "fruit-avocado_rabbit": "Avocado",
                    "fruit-pear_rabbit": "Pear",
                    "fruit-tangerine_rabbit": "Tangerine",
                    "fruit-tomato_rabbit": "Tomato",
                    "fruit-carrot_rabbit": "Carrot",
                    "btn-toggle-fullscreen": "Toggle Fullscreen",
                    "notif-fullscreen-error": "Fullscreen is not supported on this browser/context.",
                    "notif-fullscreen-entered": "🖥️ Fullscreen mode enabled!",
                    "notif-fullscreen-exited": "🚪 Fullscreen mode disabled.",
                    "cam-retake": "Retake",
                    "cam-save": "Save",
                    "cam-facing-label": "Switch Camera",
                    "cam-exit-label": "Exit",
                    "cam-guide-text": "Align your face inside this area",
                    "cam-draw-guide-text": "Trace your face with your finger! (Or save as oval by default)"
                },
                ja: {
                    "btn-gamestart": "ゲーム開始",
                    "pill-jelly": "ぷるぷるゼリー",
                    "pill-mochi": "もっちり餅",
                    "pill-slime": "スライム",
                    "btn-exit": "ゲーム終了",
                    "btn-setting": "設定",
                    "btn-auto": "オートパイロット",
                    "btn-photo": "写真撮影",
                    "btn-rec": "動画録画",
                    "btn-rec-stop": "録画停止",
                    "rec-status": "録画中",
                    "rec-stop": "停止",
                    "opt-photozone": "フォトゾーン",
                    "opt-import": "画像読込",
                    "pop-char-title": "🐰 キャラクター選択",
                    "card-strawberry": "🍓 いちごうさぎ",
                    "card-lemon": "🍋 レモンうさぎ",
                    "card-peach": "🍑 桃うさぎ",
                    "card-camera": "マイフォト (顔)",
                    "card-illust": "キャラ読込",
                    "pop-feel-title": "🍮 触感の選択",
                    "card-feel-jelly": "ぷるぷるゼリー",
                    "card-feel-mochi": "もっちり餅",
                    "card-feel-slime": "スライム",
                    "btn-recreate": "作り直す",
                    "btn-save-gallery": "ギャラリー保存",
                    "btn-reset-settings": "設定初期化",
                    "label-stiffness": "ばねの剛성",
                    "label-damping": "ダンピング",
                    "label-bgm": "BGMの音量",
                    "pop-result-title": "🎬 録画プレビュー",
                    "btn-home": "ホーム/メイン",
                    "notif-slime": "💧 触感プリセット: スライムモード起動!",
                    "notif-jelly": "🍮 触感プリセット: ぷるぷるゼリー起動!",
                    "notif-mochi": "🍡 触感プリセット: もっちり餅起動!",
                    "notif-exit": "🚪 ゲームを終了し、ロビー設定を初期化します。",
                    "notif-reset-lobby": "🔄 メインロビー設定の初期化が完了しました!",
                    "notif-reset-settings": "🔄 物理と触感設定が初期化されました!",
                    "notif-rec-complete": "🎬 MP4録画完了! 共有可能です。",
                    "notif-auto-start": "🤖 オートパイロット開始!",
                    "notif-auto-stop": "🤖 オートパイロット停止。",
                    "notif-snapshot": "📸 写真を撮影しました! ギャラリー保存可能です。",
                    "notif-char-loaded": "🐰 キャラクターがロードされました!",
                    "notif-feel-sync": "🍮 触感同期完了!",
                    "notif-char-loaded-base": "ゼリーキャラクターの読み込み完了！",
                    "notif-silhouette-mapping": "📸 シルエットマッピング完了！プレイグラウンド起動！",
                    "notif-illust-crop": "キャラクター全体クロップ：ゼリーメッシュ自動生成！",
                    "preview-snapshot-saved": "スナップショット画像がギャラリーに保存されました！",
                    "notif-gallery-saved": "🎬 MP4動画ファイルがギャラリーに保存されました。",
                    "notif-char-loaded-play": "ロード完了！プレイグラウンド起動！",
                    "word-rabbit": "うさぎ",
                    "fruit-strawberry_rabbit": "いちご",
                    "fruit-lemon_rabbit": "レモン",
                    "fruit-peach_rabbit": "桃",
                    "fruit-grape_rabbit": "ぶどう",
                    "fruit-kiwi_rabbit": "キウイ",
                    "fruit-watermelon_rabbit": "スイカ",
                    "fruit-orange_rabbit": "オレンジ",
                    "fruit-cherry_rabbit": "チェリー",
                    "fruit-apple_rabbit": "りんご",
                    "fruit-banana_rabbit": "バナナ",
                    "fruit-pineapple_rabbit": "パイナップル",
                    "fruit-mango_rabbit": "マンゴー",
                    "fruit-melon_rabbit": "メロン",
                    "fruit-blueberry_rabbit": "ブルーベリー",
                    "fruit-coconut_rabbit": "ココナッツ",
                    "fruit-avocado_rabbit": "アボカド",
                    "fruit-pear_rabbit": "梨",
                    "fruit-tangerine_rabbit": "みかん",
                    "fruit-tomato_rabbit": "トマト",
                    "fruit-carrot_rabbit": "にんじん",
                    "cam-retake": "撮り直し",
                    "cam-save": "保存",
                    "cam-facing-label": "カメラ切替",
                    "cam-exit-label": "終了",
                    "cam-guide-text": "この枠内に顔を合わせてください",
                    "cam-draw-guide-text": "指で顔の輪郭を描いて切り抜けます！(描かない場合は楕円で保存)"
                },
                zh: {
                    "btn-gamestart": "开始游戏",
                    "pill-jelly": "Q弹果冻",
                    "pill-mochi": "软糯麻薯",
                    "pill-slime": "史莱姆",
                    "btn-exit": "退出游戏",
                    "btn-setting": "设置",
                    "btn-auto": "自动测试",
                    "btn-photo": "拍照截图",
                    "btn-rec": "录制视频",
                    "btn-rec-stop": "停止录制",
                    "rec-status": "录制中",
                    "rec-stop": "停止",
                    "opt-photozone": "拍照墙",
                    "opt-import": "导入图片",
                    "pop-char-title": "🐰 选择角色",
                    "card-strawberry": "🍓 草莓兔",
                    "card-lemon": "🍋 柠檬兔",
                    "card-peach": "🍑 水蜜桃兔",
                    "card-camera": "我的照片 (面部)",
                    "card-illust": "导入角色",
                    "pop-feel-title": "🍮 触感预设",
                    "card-feel-jelly": "Q弹果冻",
                    "card-feel-mochi": "软糯麻薯",
                    "card-feel-slime": "史莱姆",
                    "btn-recreate": "重新制作",
                    "btn-save-gallery": "保存到相册",
                    "btn-reset-settings": "重置设置",
                    "label-stiffness": "弹簧刚度",
                    "label-damping": "阻尼",
                    "label-bgm": "背景音乐音量",
                    "pop-result-title": "🎬 视频录制预览",
                    "btn-home": "返回主页",
                    "notif-slime": "💧 触感预设: 史莱姆模式已激活!",
                    "notif-jelly": "🍮 触感预设: Q弹果冻已激活!",
                    "notif-mochi": "🍡 触感预设: 软糯麻薯已激活!",
                    "notif-exit": "🚪 正在退出游戏并重置大厅设置。",
                    "notif-reset-lobby": "🔄 主大厅设置重置完成!",
                    "notif-reset-settings": "🔄 物理和触感设置已重置!",
                    "notif-rec-complete": "🎬 MP4视频录制完成! 可以分享。",
                    "notif-auto-start": "🤖 自动测试开始!",
                    "notif-auto-stop": "🤖 自动测试停止。",
                    "notif-snapshot": "📸 截图已成功保存!",
                    "notif-char-loaded": "🐰 新角色加载成功!",
                    "notif-feel-sync": "🍮 触感预设已同步!",
                    "notif-char-loaded-base": "果冻角色加载完成！",
                    "notif-silhouette-mapping": "📸 轮廓映射完成！游乐场已激活！",
                    "notif-illust-crop": "角色完整裁剪：自动生成果冻网格！",
                    "preview-snapshot-saved": "截图已成功保存到相册！",
                    "notif-gallery-saved": "🎬 MP4视频文件已保存至相册。",
                    "notif-char-loaded-play": "已加载！游乐场已激活！",
                    "word-rabbit": "兔",
                    "fruit-strawberry_rabbit": "草莓",
                    "fruit-lemon_rabbit": "柠檬",
                    "fruit-peach_rabbit": "水蜜桃",
                    "fruit-grape_rabbit": "葡萄",
                    "fruit-kiwi_rabbit": "猕猴桃",
                    "fruit-watermelon_rabbit": "西瓜",
                    "fruit-orange_rabbit": "橙子",
                    "fruit-cherry_rabbit": "樱桃",
                    "fruit-apple_rabbit": "苹果",
                    "fruit-banana_rabbit": "香蕉",
                    "fruit-pineapple_rabbit": "菠萝",
                    "fruit-mango_rabbit": "芒果",
                    "fruit-melon_rabbit": "哈密瓜",
                    "fruit-blueberry_rabbit": "蓝莓",
                    "fruit-coconut_rabbit": "椰子",
                    "fruit-avocado_rabbit": "牛油果",
                    "fruit-pear_rabbit": "梨",
                    "fruit-tangerine_rabbit": "蜜橘",
                    "fruit-tomato_rabbit": "番茄",
                    "fruit-carrot_rabbit": "胡萝卜",
                    "cam-retake": "重拍",
                    "cam-save": "保存",
                    "cam-facing-label": "切换相机",
                    "cam-exit-label": "退出",
                    "cam-guide-text": "请将脸部对准此区域",
                    "cam-draw-guide-text": "用手指画出脸部轮廓进行裁剪！（不画则默认保存为椭圆）"
                }
            },
            t(key) {
                return (this.dict[this.lang] || this.dict['en'])[key] || key;
            },
            init() {
                const userLang = navigator.language || navigator.userLanguage || 'en';
                const baseLang = userLang.toLowerCase().split('-')[0];
                if (this.dict[baseLang]) {
                    this.lang = baseLang;
                } else {
                    this.lang = 'en';
                }
            }
        };

        function translateDOM() {
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                el.innerText = i18n.t(key);
            });
            document.querySelectorAll('[data-i18n-title]').forEach(el => {
                const key = el.getAttribute('data-i18n-title');
                el.setAttribute('title', i18n.t(key));
            });
        }

        function getRabbitName(char) {
            if (char.base.startsWith('custom_photo_')) {
                return `${char.emoji} ${char.name}`;
            }
            const fruitName = i18n.t('fruit-' + char.base);
            const rabbitWord = i18n.t('word-rabbit');
            const space = (i18n.lang === 'ko' || i18n.lang === 'en') ? ' ' : '';
            return `${char.emoji}${space}${fruitName}${space}${rabbitWord}`;
        }

        let width = 388; // Phone inner width
        let height = 816; // Phone inner height
        canvas.width = width;
        canvas.height = height;

        // Mass Spring Physics parameters
        let stiffness = 50;
        let damping = 8;
        let points = [];
        let springs = [];
        let rows = 10;
        let cols = 10;
        let grabbedPointIndex = null;
        let isTouching = false;
        let touchX = 0;
        let touchY = 0;
        let lastTouchX = 0;
        let lastTouchY = 0;
        let touchTime = 0;
        let touchHapticFrame = 0;

        
        /* ==========================================================================
           FRUIT RABBIT MALRANGI 3D JELLY ENGINE v3.5.0 (STABLE RELEASE)
           - 100% Unified Whole-Body Cohesion & Pure 3D Inward Z-Depth Physics
           - Soft Liquid Sine Bubble Audio Synthesizer & Silky 6ms Micro-Haptics
           - Bottom 17 Fruit Rabbit Auto-Scroll Carousel Selector Engine
           ========================================================================== */

        let activeBase = 'strawberry_rabbit';
        let activeEmoji = '🍓';
        let activeFeel = 'jelly';
        let activeHue = 350; // default theme hue
        
        // 3D Ear Dome Rounding for Strawberry Rabbit Artwork
        function roundStrawberryArtworkEars(src, callback) {
            const img = new Image();
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.naturalWidth || 512;
                canvas.height = img.naturalHeight || 512;
                const ctx = canvas.getContext('2d');
                const w = canvas.width;
                const h = canvas.height;
                
                // Draw original image
                ctx.drawImage(img, 0, 0, w, h);
                
                // Draw Left & Right 3D Round Strawberry Ear Caps over flat top edge
                ctx.save();
                const leftGrad = ctx.createRadialGradient(w * 0.37, h * 0.20, 5, w * 0.37, h * 0.25, h * 0.12);
                leftGrad.addColorStop(0, '#ff7a8b');
                leftGrad.addColorStop(0.5, '#ff4757');
                leftGrad.addColorStop(0.85, '#e83949');
                leftGrad.addColorStop(1, '#c02232');
                
                ctx.fillStyle = leftGrad;
                ctx.beginPath();
                ctx.ellipse(w * 0.37, h * 0.24, w * 0.11, h * 0.08, 0, 0, Math.PI * 2);
                ctx.fill();

                const rightGrad = ctx.createRadialGradient(w * 0.63, h * 0.20, 5, w * 0.63, h * 0.25, h * 0.12);
                rightGrad.addColorStop(0, '#ff7a8b');
                rightGrad.addColorStop(0.5, '#ff4757');
                rightGrad.addColorStop(0.85, '#e83949');
                rightGrad.addColorStop(1, '#c02232');
                
                ctx.fillStyle = rightGrad;
                ctx.beginPath();
                ctx.ellipse(w * 0.63, h * 0.24, w * 0.11, h * 0.08, 0, 0, Math.PI * 2);
                ctx.fill();

                // Specular Highlights
                ctx.fillStyle = 'rgba(255, 255, 255, 0.75)';
                ctx.beginPath();
                ctx.ellipse(w * 0.34, h * 0.21, w * 0.035, h * 0.018, -Math.PI / 6, 0, Math.PI * 2);
                ctx.fill();

                ctx.beginPath();
                ctx.ellipse(w * 0.60, h * 0.21, w * 0.035, h * 0.018, -Math.PI / 6, 0, Math.PI * 2);
                ctx.fill();

                ctx.restore();
                callback(canvas.toDataURL('image/png'));
            };
            img.src = src;
        }

        let defaultStrawberrySrc = '';

        const jellyImage = new Image();
        jellyImage.onload = function() {
            initMesh();
            draw();
        };
        jellyImage.onerror = function() { this.src = "1_512.png"; };
        jellyImage.src = "strawberry_rabbit_jelly.png";

        class MeshPoint {
            constructor(x, y) {
                this.ox = x;
                this.oy = y;
                this.x = x;
                this.y = y;
                this.vx = 0;
                this.vy = 0;
            }
            update() {
                // High damping for silky smooth jelly elasticity without jittering
                this.vx *= 0.78;
                this.vy *= 0.78;

                const maxSpeed = 15;
                this.vx = Math.min(maxSpeed, Math.max(-maxSpeed, this.vx));
                this.vy = Math.min(maxSpeed, Math.max(-maxSpeed, this.vy));
                
                this.x += this.vx;
                this.y += this.vy;
                
                // Canvas boundary guard
                const pad = 15;
                const canvasW = width || 388;
                const canvasH = height || 840;
                if (this.x < pad) { this.x = pad; this.vx *= -0.2; }
                if (this.x > canvasW - pad) { this.x = canvasW - pad; this.vx *= -0.2; }
                if (this.y < pad) { this.y = pad; this.vy *= -0.2; }
                if (this.y > canvasH - pad) { this.y = canvasH - pad; this.vy *= -0.2; }
            }
        }

                // ==========================================================================
        // TRANSPARENT GLOBAL MESH ENVELOPE ARCHITECTURE (USER DESIGNED SOLUTION)
        // ==========================================================================
        // A single transparent bounding shell encapsulates 100% of the character mesh.
        // All body parts (Ears, Face, Eyes, Blush Cheeks, Tummy, Fruit) are bound to
        // this transparent shell, guaranteeing 0% layer separation and 0% submerging!
        // ==========================================================================
        class GlobalEnvelope {
            constructor() {
                this.isActive = true;
            }
            applyEnvelopeMove(dx, dy) {
                // Move 100% of all 256 mesh nodes bound to the transparent envelope
                for (let i = 0; i < points.length; i++) {
                    points[i].x += dx;
                    points[i].y += dy;
                }
            }
        }
        const globalEnvelope = new GlobalEnvelope();

        class Spring {
            constructor(p1, p2, length) {
                this.p1 = p1;
                this.p2 = p2;
                this.restLength = length;
            }
            solve() {
                let dx = this.p2.x - this.p1.x;
                let dy = this.p2.y - this.p1.y;
                let dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 0.001) return;

                let delta = dist - this.restLength;
                let k = 0.09; // Soft spring constant
                let springForce = delta * k;
                
                let nx = dx / dist;
                let ny = dy / dist;

                // Relative velocity damping across spring to eliminate trembling
                let rvx = this.p2.vx - this.p1.vx;
                let rvy = this.p2.vy - this.p1.vy;
                let dampingForce = (rvx * nx + rvy * ny) * 0.15;

                let totalForce = springForce + dampingForce;

                let fx = nx * totalForce;
                let fy = ny * totalForce;

                this.p1.vx += fx;
                this.p1.vy += fy;
                this.p2.vx -= fx;
                this.p2.vy -= fy;

                // Strict Monotonic Order Preservation: 100% prevents outer boundary nodes from crossing inner nodes
                let minDist = this.restLength * 0.75;
                if (dist < minDist) {
                    let repForce = (minDist - dist) * 0.85;
                    this.p1.vx -= nx * repForce;
                    this.p1.vy -= ny * repForce;
                    this.p2.vx += nx * repForce;
                    this.p2.vy += ny * repForce;
                }
            }
        }

        
        // --- BOTTOM 17 FRUIT RABBIT CAROUSEL SELECTOR ENGINE ---
        let carouselAutoScrollTimer = null;
        let isCarouselHovered = false;

        function renderBottomCarousel() {
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
        }

        // Call renderBottomCarousel on init
        window.addEventListener('DOMContentLoaded', () => {
            renderBottomCarousel();
        });

        
        // Automatic Mobile Fullscreen Enforcer
        function enforceMobileFullscreen() {
            if (window.innerWidth <= 768 || /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
                const frame = document.querySelector('.phone-frame');
                if (frame) {
                    frame.style.setProperty('width', '100vw', 'important');
                    frame.style.setProperty('height', '100vh', 'important');
                    frame.style.setProperty('height', '100dvh', 'important');
                    frame.style.setProperty('border', 'none', 'important');
                    frame.style.setProperty('border-radius', '0', 'important');
                }
            }
        }
        window.addEventListener('resize', enforceMobileFullscreen);
        window.addEventListener('orientationchange', enforceMobileFullscreen);
        document.addEventListener('DOMContentLoaded', enforceMobileFullscreen);
        enforceMobileFullscreen();

        function initMesh() {
            points = [];
            springs = [];

            let canvasW = width || 388;
            let canvasH = height || 840;

            // Preserve 100% exact aspect ratio of the original character image
            let imgAspect = 1.0;
            if (jellyImage && jellyImage.complete && jellyImage.naturalWidth > 0 && jellyImage.naturalHeight > 0) {
                imgAspect = jellyImage.naturalWidth / jellyImage.naturalHeight;
            }

            let sizeScale = 1.0;
            if (activeBase === "strawberry_rabbit" || (jellyImage && jellyImage.src && jellyImage.src.includes("strawberry_rabbit"))) {
                sizeScale = 1.35;
            }

            let maxW = canvasW * 0.78 * sizeScale;
            let maxH = canvasH * 0.49 * sizeScale;

            let meshW = maxW;
            let meshH = meshW / imgAspect;

            if (meshH > maxH) {
                meshH = maxH;
                meshW = meshH * imgAspect;
            }

            let startX = (canvasW - meshW) / 2;
            let startY = (canvasH - meshH) / 2;

            // 1. Create Points within Rabbit Bounds
            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols; c++) {
                    let px = startX + (c / (cols - 1)) * meshW;
                    let py = startY + (r / (rows - 1)) * meshH;
                    points.push(new MeshPoint(px, py));
                }
            }

            // 2. Connect Neighbor Springs
            // Horizontal structural
            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols - 1; c++) {
                    let i1 = r * cols + c;
                    let i2 = r * cols + (c + 1);
                    let dist = Math.sqrt(Math.pow(points[i1].x - points[i2].x, 2) + Math.pow(points[i1].y - points[i2].y, 2));
                    springs.push(new Spring(points[i1], points[i2], dist));
                }
            }
            // Vertical structural
            for (let r = 0; r < rows - 1; r++) {
                for (let c = 0; c < cols; c++) {
                    let i1 = r * cols + c;
                    let i2 = (r + 1) * cols + c;
                    let dist = Math.sqrt(Math.pow(points[i1].x - points[i2].x, 2) + Math.pow(points[i1].y - points[i2].y, 2));
                    springs.push(new Spring(points[i1], points[i2], dist));
                }
            }
            // Diagonal structural shear (prevents shearing/sliding collapse)
            for (let r = 0; r < rows - 1; r++) {
                for (let c = 0; c < cols - 1; c++) {
                    let i1 = r * cols + c;
                    let i2 = (r + 1) * cols + (c + 1);
                    let dist = Math.sqrt(Math.pow(points[i1].x - points[i2].x, 2) + Math.pow(points[i1].y - points[i2].y, 2));
                    springs.push(new Spring(points[i1], points[i2], dist));

                    let i3 = r * cols + (c + 1);
                    let i4 = (r + 1) * cols + c;
                    let dist2 = Math.sqrt(Math.pow(points[i3].x - points[i4].x, 2) + Math.pow(points[i3].y - points[i4].y, 2));
                    springs.push(new Spring(points[i3], points[i4], dist2));
                }
            }
            // Bending constraints (distance 2 connections for structural bulk shape recovery)
            for (let r = 0; r < rows; r++) {
                for (let c = 0; c < cols - 2; c++) {
                    let i1 = r * cols + c;
                    let i2 = r * cols + (c + 2);
                    let dist = Math.sqrt(Math.pow(points[i1].x - points[i2].x, 2) + Math.pow(points[i1].y - points[i2].y, 2));
                    springs.push(new Spring(points[i1], points[i2], dist));
                }
            }
            for (let r = 0; r < rows - 2; r++) {
                for (let c = 0; c < cols; c++) {
                    let i1 = r * cols + c;
                    let i2 = (r + 2) * cols + c;
                    let dist = Math.sqrt(Math.pow(points[i1].x - points[i2].x, 2) + Math.pow(points[i1].y - points[i2].y, 2));
                    springs.push(new Spring(points[i1], points[i2], dist));
                }
            }
        }

        function deformMesh(mx, my, force) {
            let canvasW = width || 388;
            let maxRadius = canvasW * 0.55;
            for (let i = 0; i < points.length; i++) {
                let p = points[i];
                let dx = p.x - mx;
                let dy = p.y - my;
                let dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < maxRadius) {
                    let weight = Math.pow(1 - (dist / maxRadius), 2);
                    // Dramatic deep 3D downward press indentation
                    p.vy += force * weight * 2.8;
                    p.y += force * weight * 1.6;
                    if (dist > 1) {
                        p.vx -= (dx / dist) * force * weight * 1.2;
                        p.vy -= (dy / dist) * force * weight * 0.8;
                    }
                }
            }
        }

        // Toggle advanced configurations
        function toggleAdvancedSettings() {
            stopAutopilot(); releaseGrab(true); releaseGrab(true);
            const el = document.getElementById('advanced-drawer');
            el.style.display = el.style.display === 'flex' ? 'none' : 'flex';
        }

        // Close settings drawer when clicking outside
        document.addEventListener('pointerdown', (e) => {
            const drawer = document.getElementById('advanced-drawer');
            const toggleBtn = document.getElementById('settings-toggle-btn');
            if (drawer && drawer.style.display === 'flex') {
                if (!drawer.contains(e.target) && !toggleBtn.contains(e.target)) {
                    drawer.style.display = 'none';
                }
            }
        });

        function syncSliderLabels() {
            const stiffnessEl = document.getElementById('spring-stiffness');
            const dampingEl = document.getElementById('dampening');
            const bgmEl = document.getElementById('bgm-volume');
            
            if (stiffnessEl) document.getElementById('stiffness-val').innerText = stiffnessEl.value;
            if (dampingEl) document.getElementById('damping-val').innerText = dampingEl.value;
            if (bgmEl) document.getElementById('bgm-val').innerText = bgmEl.value + '%';
        }

        function updateSliders() {
            stiffness = parseFloat(document.getElementById('spring-stiffness').value);
            damping = parseFloat(document.getElementById('dampening').value);
            syncSliderLabels();
        }

        // Pop-up Overlays UI controllers
        function openPop(id) {
            document.querySelectorAll('.pop-overlay').forEach(el => el.style.display = 'none');
            const el = document.getElementById(id);
            if (el) el.style.display = 'flex';
        }

        function closePop(id) {
            const el = document.getElementById(id);
            if (el) el.style.display = 'none';
        }

        function selectBaseCard(baseId, emoji, cardId) {
            stopAutopilot(); releaseGrab(true); releaseGrab(true);
            const foundIdx = lobbyCharacters.findIndex(c => c.base === baseId);
            if (foundIdx >= 0) {
                selectLobbyCharacter(foundIdx, null);
            } else {
                activeBase = baseId;
                activeEmoji = emoji;
                showNotification(`${emoji} ` + i18n.t('notif-char-loaded-base'));
            }

            document.querySelectorAll('#character-pop .grid-card').forEach(el => el.classList.remove('active'));
            const cardEl = document.getElementById(cardId);
            if (cardEl) cardEl.classList.add('active');
            closePop('character-pop');
        }

        function importFromCameraCard(cardId) {
            document.getElementById('camera-input').click();
            
            document.querySelectorAll('#character-pop .grid-card').forEach(el => el.classList.remove('active'));
            document.getElementById(cardId).classList.add('active');
            closePop('character-pop');
        }

        function handleCameraUpload(event) {
            try {
                const file = (event && event.target && event.target.files) ? event.target.files[0] : null;
                if (!file) {
                    console.warn("handleCameraUpload: No file found in event.");
                    return;
                }

                if (typeof logImportDiagnostic === 'function') {
                    logImportDiagnostic(`> 이미지 파일 선택됨: ${file.name}`);
                }

                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = new Image();
                    img.onload = function() {
                        if (typeof logImportDiagnostic === 'function') {
                            logImportDiagnostic(`> 이미지 로드 완료 (${img.naturalWidth}x${img.naturalHeight}). AI 누끼 가공 시작...`);
                        }
                        
                        // Execute High-Precision Dual-Mode AI Cutout Engine
                        if (typeof processImageCutout === 'function') {
                            processImageCutout(img, function(cutoutPNG) {
                                renderCutoutJellyToStage(cutoutPNG);
                            });
                        } else {
                            renderCutoutJellyToStage(e.target.result);
                        }
                    };
                    img.onerror = function(err) {
                        console.error("Image decode error:", err);
                        showNotification("이미지 디코딩 실패!");
                    };
                    img.src = e.target.result;
                };
                reader.readAsDataURL(file);

                if (event.target) {
                    event.target.value = ''; // Reset input for next selection
                }
            } catch (err) {
                console.error("handleCameraUpload exception:", err);
            }
        }

        // Render cutout jelly image onto stage, add to carousel, & save to phone localStorage
        function renderCutoutJellyToStage(cutoutPNG) {
            try {
                if (typeof customPhotoCounter === 'undefined') customPhotoCounter = 1;
                
                const newChar = {
                    emoji: '📸',
                    name: `내 그림 ${customPhotoCounter++}`,
                    base: `custom_photo_${Date.now()}`,
                    hue: 355,
                    imgData: cutoutPNG
                };

                if (typeof lobbyCharacters !== 'undefined' && Array.isArray(lobbyCharacters)) {
                    lobbyCharacters.push(newChar);
                    activeLobbyIndex = lobbyCharacters.length - 1;
                }

                // Update 3D Stage Jelly Texture
                if (typeof jellyImage !== 'undefined') {
                    jellyImage.onload = function() {
                        if (typeof initMesh === 'function') initMesh();
                        if (typeof draw === 'function') draw();
                    };
                    jellyImage.src = cutoutPNG;
                }

                // Initialize spring mesh physics immediately
                if (typeof initMesh === 'function') initMesh();
                if (typeof draw === 'function') draw();

                // Save to phone localStorage
                if (typeof saveCustomRabbitToPhone === 'function') {
                    saveCustomRabbitToPhone(cutoutPNG);
                }

                // Update bottom carousel UI
                if (typeof renderLobbyGrid === 'function') {
                    renderLobbyGrid();
                }

                // Make sure stage is visible
                if (typeof setScreenMode === 'function') {
                    setScreenMode('lobby');
                }

                if (typeof showNotification === 'function') {
                    showNotification("🎉 새로운 젤리 캐릭터가 무대에 올라왔습니다!");
                }
            } catch (err) {
                console.error("renderCutoutJellyToStage exception:", err);
            }
        }

        // ✍️ 손가락 드로잉 오리기(자르기) 상태 변수
        let drawCropPoints = [];
        let isDrawingCrop = false;

        function initDrawingCrop() {
            const drawCanvas = document.getElementById('camera-draw-crop-canvas');
            if (!drawCanvas) return;
            
            drawCropPoints = [];
            isDrawingCrop = false;
            
            // Set canvas resolution using actual parent container size to ensure 100% alignment
            const container = document.querySelector('.camera-video-container');
            let w = container ? container.clientWidth : 0;
            let h = container ? container.clientHeight : 0;
            
            // Apply viewport and min dimension fallbacks to prevent 0-size canvas collapse on Safari/iOS
            if (w <= 0 || h <= 0) {
                w = drawCanvas.clientWidth || window.innerWidth || 360;
                h = drawCanvas.clientHeight || window.innerHeight || 640;
            }
            if (w < 100) w = 360;
            if (h < 100) h = 640;
            
            drawCanvas.width = w;
            drawCanvas.height = h;
            
            const ctx = drawCanvas.getContext('2d');
            ctx.clearRect(0, 0, drawCanvas.width, drawCanvas.height);
        }

        function setupDrawingCropListeners() {
            const drawCanvas = document.getElementById('camera-draw-crop-canvas');
            if (!drawCanvas) return;
            
            function getPos(e) {
                const rect = drawCanvas.getBoundingClientRect();
                let clientX = e.clientX;
                let clientY = e.clientY;
                
                if (e.touches && e.touches.length > 0) {
                    clientX = e.touches[0].clientX;
                    clientY = e.touches[0].clientY;
                } else if (e.changedTouches && e.changedTouches.length > 0) {
                    clientX = e.changedTouches[0].clientX;
                    clientY = e.changedTouches[0].clientY;
                }
                
                const widthBound = rect.width || 1;
                const heightBound = rect.height || 1;
                
                return {
                    x: (clientX - rect.left) / widthBound,
                    y: (clientY - rect.top) / heightBound
                };
            }
            
            function handleStart(e) {
                if (e.cancelable) e.preventDefault();
                isDrawingCrop = true;
                drawCropPoints = [getPos(e)];
                drawPath();
            }
            
            function handleMove(e) {
                if (!isDrawingCrop) return;
                if (e.cancelable) e.preventDefault();
                drawCropPoints.push(getPos(e));
                drawPath();
            }
            
            function handleEnd(e) {
                if (!isDrawingCrop) return;
                if (e.cancelable) e.preventDefault();
                isDrawingCrop = false;
                if (drawCropPoints.length > 2) {
                    drawCropPoints.push({ x: drawCropPoints[0].x, y: drawCropPoints[0].y });
                }
                drawPath();
            }
            
            function drawPath() {
                const ctx = drawCanvas.getContext('2d');
                ctx.clearRect(0, 0, drawCanvas.width, drawCanvas.height);
                if (drawCropPoints.length < 2) return;
                
                // Draw a beautiful semi-transparent neon glow red path line
                ctx.strokeStyle = '#ff4757';
                ctx.lineWidth = 5;
                ctx.lineCap = 'round';
                ctx.lineJoin = 'round';
                ctx.shadowColor = '#ff4757';
                ctx.shadowBlur = 10;
                
                ctx.beginPath();
                ctx.moveTo(drawCropPoints[0].x * drawCanvas.width, drawCropPoints[0].y * drawCanvas.height);
                for (let i = 1; i < drawCropPoints.length; i++) {
                    ctx.lineTo(drawCropPoints[i].x * drawCanvas.width, drawCropPoints[i].y * drawCanvas.height);
                }
                ctx.stroke();
                
                // Draw fill tint to visualize crop area
                ctx.shadowBlur = 0;
                ctx.fillStyle = 'rgba(255, 71, 87, 0.15)';
                ctx.fill();
            }
            
            drawCanvas.addEventListener('pointerdown', handleStart);
            drawCanvas.addEventListener('pointermove', handleMove);
            drawCanvas.addEventListener('pointerup', handleEnd);

            drawCanvas.addEventListener('touchstart', handleStart, { passive: false });
            drawCanvas.addEventListener('touchmove', handleMove, { passive: false });
            drawCanvas.addEventListener('touchend', handleEnd, { passive: false });
            
            drawCanvas.addEventListener('mousedown', handleStart);
            drawCanvas.addEventListener('mousemove', handleMove);
            drawCanvas.addEventListener('mouseup', handleEnd);
        }

        async function openCustomCamera() {
            stopAutopilot(); releaseGrab(true); releaseGrab(true);
            bgmPlayer.stop(); // Stop all sound when camera overlay is active
            const overlay = document.getElementById('custom-camera-overlay');
            const video = document.getElementById('camera-video');
            const preview = document.getElementById('camera-preview');
            const retakeBtn = document.getElementById('cam-btn-retake');
            const saveBtn = document.getElementById('cam-btn-save');
            const captureBtn = document.getElementById('cam-btn-capture');
            const guide = document.getElementById('camera-face-guide');
            const drawCanvas = document.getElementById('camera-draw-crop-canvas');

            if (!overlay || !video) return;

            // Reset UI state
            video.style.display = 'block';
            if (preview) preview.style.display = 'none';
            if (retakeBtn) retakeBtn.style.display = 'none';
            if (saveBtn) saveBtn.style.display = 'none';
            if (captureBtn) captureBtn.style.display = 'inline-block';
            if (guide) guide.style.display = 'flex';
            if (drawCanvas) drawCanvas.style.display = 'none';

            overlay.style.display = 'flex';

            // Start stream
            try {
                if (cameraStream) {
                    cameraStream.getTracks().forEach(track => track.stop());
                }
                cameraStream = await navigator.mediaDevices.getUserMedia({
                    video: { facingMode: cameraFacingMode },
                    audio: false
                });
                video.srcObject = cameraStream;
                if (cameraFacingMode === 'user') {
                    video.style.transform = 'scaleX(-1)';
                } else {
                    video.style.transform = 'scaleX(1)';
                }
            } catch (err) {
                console.log("Camera access error:", err);
                showNotification(i18n.t('notif-camera-error') || "Camera access failed. Try file upload.");
                // Trigger fallback input
                document.getElementById('camera-input').click();
                closeCustomCamera();
            }
        }

        function closeCustomCamera() {
            const overlay = document.getElementById('custom-camera-overlay');
            if (overlay) overlay.style.display = 'none';
            if (cameraStream) {
                cameraStream.getTracks().forEach(track => track.stop());
                cameraStream = null;
            }
            const video = document.getElementById('camera-video');
            if (video) video.srcObject = null;
            const guide = document.getElementById('camera-face-guide');
            if (guide) guide.style.display = 'none';
            const drawCanvas = document.getElementById('camera-draw-crop-canvas');
            if (drawCanvas) drawCanvas.style.display = 'none';

            // Restore BGM if returning to playground, keep stopped if returning to lobby
            const lobby = document.getElementById('lobby-screen');
            if (lobby && lobby.style.display === 'none') {
                if (audioCtx && audioCtx.state === 'suspended') {
                    audioCtx.resume();
                }
                bgmPlayer.start();
            } else {
                bgmPlayer.stop();
            }
        }

        async function toggleCameraFacing() {
            cameraFacingMode = (cameraFacingMode === 'user') ? 'environment' : 'user';
            // Restart stream with new facing mode
            await openCustomCamera();
        }

        
                const cameraShutterAudio = new Audio("data:audio/mp3;base64,//PkZAAAAAGkAAAAAAAAA0gAAAAATEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//PkZAADWBAAAHf+AAAAA0gAAAAAOfBqMo4sPXGpJjGI0BJrENmiLOjtb9VOWsplMQU1FMy4xMDBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVdFUKn5KmVuOKwpowUHzE8gOLHkt0qBMeUu2/wKEBIaDRekSPAQC2lqKrsia4iYtVPNBRwLuUOW/7SSWEtfeB9VKkgVdIGFn1hUAYwEXhDky7iT6ZxcRhS1FptyYgqSBL8dc1dbgMZW+4jtzU5U537lnCVwUoUW0GQwce1tXbgTsTd1t2GOi1dCQh+lcXoYZNuhm1xLxF8vkHGF2FTpUKzts8KSami73/ljYgcI/9eu3BfKQIKLAhRCeDWgkEOqDtDVDA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VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//PkZAAANAIAADwAAABwBAAAeAAACHANqYgpqKZlxiYGCqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq//PkZAAAAAGkAAAAAAAAA0gAAAAATEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq//PkZAAAAAGkAAAAAAAAA0gAAAAATEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq//PkZAAAAAGkAAAAAAAAA0gAAAAATEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq//PkZAAAAAGkAAAAAAAAA0gAAAAATEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq");
        
        function playShutterSound() {
            try {
                cameraShutterAudio.currentTime = 0;
                const playPromise = cameraShutterAudio.play();
                if (playPromise !== undefined) {
                    playPromise.catch(err => {
                        console.log("Audio play error:", err);
                    });
                }
            } catch(e) {
                console.log("Shutter audio error:", e);
            }
        }

        function capturePhoto() {
            playShutterSound();
            try {
                const video = document.getElementById('camera-video');
                const preview = document.getElementById('camera-preview');
                const captureBtn = document.getElementById('cam-btn-capture');
                const retakeBtn = document.getElementById('cam-btn-retake');
                const saveBtn = document.getElementById('cam-btn-save');
                const guide = document.getElementById('camera-face-guide');
                const drawCanvas = document.getElementById('camera-draw-crop-canvas');

                if (!cameraStream || !video) return;

                // Get camera container dimensions
                const container = document.querySelector('.camera-video-container');
                let viewWidth = container ? container.clientWidth : 0;
                let viewHeight = container ? container.clientHeight : 0;
                if (viewWidth <= 0 || viewHeight <= 0) {
                    viewWidth = video.clientWidth || window.innerWidth || 360;
                    viewHeight = video.clientHeight || window.innerHeight || 640;
                }
                if (viewWidth < 100) viewWidth = 360;
                if (viewHeight < 100) viewHeight = 640;

                const canvas = document.getElementById('camera-canvas') || document.createElement('canvas');
                canvas.width = viewWidth;
                canvas.height = viewHeight;
                const ctx = canvas.getContext('2d');

                let attempt = 0;
                function tryCapture() {
                    try {
                        // Temporarily clear transform style to avoid Safari transform capture bugs
                        const originalTransform = video.style.transform;
                        video.style.transform = 'none';
                        video.offsetHeight; // trigger reflow
                        
                        ctx.clearRect(0, 0, canvas.width, canvas.height);
                        
                        // Reset transform before drawing if mirrored
                        ctx.setTransform(1, 0, 0, 1, 0, 0);
                        if (cameraFacingMode === 'user') {
                            ctx.translate(canvas.width, 0);
                            ctx.scale(-1, 1);
                        }
                        
                        // Draw entire video frame to canvas using 5-argument drawImage to prevent iOS WebKit hardware decoding blank canvas bugs
                        let vW = video.videoWidth || 1280;
                        let vH = video.videoHeight || 720;
                        if (vW > 0 && vH > 0) {
                            let vAspect = vW / vH;
                            let cAspect = canvas.width / canvas.height;
                            let sx = 0, sy = 0, sWidth = vW, sHeight = vH;
                            if (vAspect > cAspect) {
                                sWidth = vH * cAspect;
                                sx = (vW - sWidth) / 2;
                            } else {
                                sHeight = vW / cAspect;
                                sy = (vH - sHeight) / 2;
                            }
                            ctx.drawImage(video, sx, sy, sWidth, sHeight, 0, 0, canvas.width, canvas.height);
                        } else {
                            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                        }
                        
                        // Restore transform on video element
                        video.style.transform = originalTransform;
                        
                        // Check if captured frame is blank/black
                        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                        const data = imageData.data;
                        let isBlank = true;
                        // Check every 10th pixel for performance
                        for (let i = 0; i < data.length; i += 40) {
                            const r = data[i];
                            const g = data[i+1];
                            const b = data[i+2];
                            const a = data[i+3];
                            if (a > 0 && (r > 0 || g > 0 || b > 0) && (r < 255 || g < 255 || b < 255)) {
                                isBlank = false;
                                break;
                            }
                        }
                        
                        if (isBlank && attempt < 3) {
                            attempt++;
                            console.log("Captured frame is blank, retrying attempt " + attempt + "...");
                            setTimeout(tryCapture, 80);
                        } else {
                            // Apply captured frame to preview image safely
                            if (preview) {
                                preview.src = canvas.toDataURL('image/png');
                                preview.style.display = 'block';
                            }
                            video.style.display = 'none';
                            if (guide) guide.style.display = 'none';

                            // Show and init finger tracing crop canvas overlay
                            if (drawCanvas) {
                                drawCanvas.style.display = 'block';
                                setTimeout(initDrawingCrop, 50);
                            }

                            // Toggle button states
                            if (captureBtn) captureBtn.style.display = 'none';
                            if (retakeBtn) retakeBtn.style.display = 'inline-block';
                            if (saveBtn) saveBtn.style.display = 'inline-block';

                            showNotification(i18n.t('cam-draw-guide-text') || "손가락으로 얼굴을 그려서 잘라보세요!");
                            triggerHaptic(40);
                        }
                    } catch (captureErr) {
                        console.error("Internal tryCapture error:", captureErr);
                        if (attempt < 3) {
                            attempt++;
                            setTimeout(tryCapture, 80);
                        } else {
                            throw captureErr;
                        }
                    }
                }
                
                tryCapture();
            } catch (err) {
                console.error("capturePhoto error:", err);
                showNotification("Photo capture failed: " + err.message);
            }
        }

        function retakePhoto() {
            const video = document.getElementById('camera-video');
            const preview = document.getElementById('camera-preview');
            const captureBtn = document.getElementById('cam-btn-capture');
            const retakeBtn = document.getElementById('cam-btn-retake');
            const saveBtn = document.getElementById('cam-btn-save');
            const guide = document.getElementById('camera-face-guide');
            const drawCanvas = document.getElementById('camera-draw-crop-canvas');

            if (video) video.style.display = 'block';
            if (preview) preview.style.display = 'none';
            if (captureBtn) captureBtn.style.display = 'inline-block';
            if (retakeBtn) retakeBtn.style.display = 'none';
            if (saveBtn) saveBtn.style.display = 'none';
            if (guide) guide.style.display = 'flex';
            if (drawCanvas) {
                drawCanvas.style.display = 'none';
                drawCropPoints = [];
            }
        }

        function getFaceGuideRelativeCenter() {
            const guide = document.getElementById('camera-face-guide');
            const container = document.querySelector('.camera-video-container');
            if (guide && container) {
                const gRect = guide.getBoundingClientRect();
                const cRect = container.getBoundingClientRect();
                if (cRect.width > 0 && cRect.height > 0) {
                    return {
                        cx: (gRect.left + gRect.width / 2 - cRect.left) / cRect.width,
                        cy: (gRect.top + gRect.height / 2 - cRect.top) / cRect.height,
                        rx: (gRect.width / 2) / cRect.width,
                        ry: (gRect.height / 2) / cRect.height
                    };
                }
            }
            return { cx: 0.5, cy: 0.35, rx: 0.26, ry: 0.35 }; // fallback matching 15% top styling
        }

        function savePhotoToGrid() {
            const preview = document.getElementById('camera-preview');
            const cameraCanvas = document.getElementById('camera-canvas');
            let imgSrc = (preview && preview.src && !preview.src.startsWith('data:image/svg+xml')) ? preview.src : null;
            if (!imgSrc && cameraCanvas) {
                try {
                    imgSrc = cameraCanvas.toDataURL('image/png');
                } catch(e) {}
            }
            if (!imgSrc) {
                showNotification("사진을 먼저 캡처해 주세요!");
                return;
            }

            const guideCenter = getFaceGuideRelativeCenter();

            const img = new Image();
            img.onload = function() {
                const splash = document.getElementById('start-splash-screen');
                if (splash) {
                    splash.classList.add('fade-out');
                    splash.style.display = 'none';
                    splash.style.opacity = '0';
                    splash.style.visibility = 'hidden';
                }
                const path = (drawCropPoints && drawCropPoints.length > 5) ? drawCropPoints : null;
                processImageToJelly(img, true, path, guideCenter);
                closeCustomCamera();
                setScreenMode('lobby');
                showNotification("사진 캐릭터가 성공적으로 등록되었습니다!");
            };
            img.src = imgSrc;
        }

        function processImageToJelly(img, isCamera = false, customPath = null, guideCenter = null) {
            try {
                const size = 512;
                
                let imgW = img.naturalWidth || img.width || 512;
                let imgH = img.naturalHeight || img.height || 512;
                if (imgW <= 0) imgW = 512;
                if (imgH <= 0) imgH = 512;
                
                let aspect = imgW / imgH;
                if (isNaN(aspect) || aspect <= 0) aspect = 1;

                // Canvas A: Original Image centered or cropped
                const imgCanvas = document.createElement('canvas');
                imgCanvas.width = size;
                imgCanvas.height = size;
                const imgCtx = imgCanvas.getContext('2d');
                
                if (isCamera) {
                    function mapViewportToJellyCanvas(px, py) {
                        let cx, cy;
                        const safetyX = isNaN(px) ? 0.5 : px;
                        const safetyY = isNaN(py) ? 0.5 : py;
                        if (aspect < 1) {
                            cx = safetyX * size;
                            cy = (safetyY - 0.5) * (size / aspect) + (size / 2);
                        } else {
                            cx = (safetyX - 0.5) * (size * aspect) + (size / 2);
                            cy = safetyY * size;
                        }
                        if (isNaN(cx)) cx = size / 2;
                        if (isNaN(cy)) cy = size / 2;
                        return { x: cx, y: cy };
                    }

                    imgCtx.save();
                    imgCtx.beginPath();
                    if (customPath && customPath.length > 5) {
                        const pt0 = mapViewportToJellyCanvas(customPath[0].x, customPath[0].y);
                        imgCtx.moveTo(pt0.x, pt0.y);
                        for (let i = 1; i < customPath.length; i++) {
                            const pt = mapViewportToJellyCanvas(customPath[i].x, customPath[i].y);
                            imgCtx.lineTo(pt.x, pt.y);
                        }
                        imgCtx.closePath();
                    } else {
                        const gc = guideCenter || { cx: 0.5, cy: 0.40, rx: 0.35, ry: 0.45 };
                        const center = mapViewportToJellyCanvas(gc.cx, gc.cy);
                        const rx = size * 0.45;
                        const ry = size * 0.48;
                        
                        let finalRx = isNaN(rx) ? 133 : rx;
                        let finalRy = isNaN(ry) ? 179 : ry;
                        if (!isFinite(finalRx) || finalRx <= 0) finalRx = 133;
                        if (!isFinite(finalRy) || finalRy <= 0) finalRy = 179;
                        
                        imgCtx.ellipse(center.x, center.y, finalRx, finalRy, 0, 0, Math.PI * 2);
                    }
                    imgCtx.clip();

                    const scale = Math.max(size / imgW, size / imgH);
                    const w = imgW * scale;
                    const h = imgH * scale;
                    const x = (size - w) / 2;
                    const y = (size - h) / 2;
                    imgCtx.drawImage(img, x, y, w, h);
                    imgCtx.restore();
                } else {
                    const margin = 45;
                    const fitSize = size - margin * 2;
                    const scale = Math.min(fitSize / imgW, fitSize / imgH);
                    const w = imgW * scale;
                    const h = imgH * scale;
                    const x = (size - w) / 2;
                    const y = (size - h) / 2;
                    imgCtx.drawImage(img, x, y, w, h);

                    // Check if image is already a transparent PNG (e.g. imported character graphics)
                    const imgData = imgCtx.getImageData(0, 0, size, size);
                    const pixels = imgData.data;

                    // Inspect 4 corner pixels to detect if background is already transparent
                    const cornerAlpha1 = pixels[3];
                    const cornerAlpha2 = pixels[(size - 1) * 4 + 3];
                    const cornerAlpha3 = pixels[((size - 1) * size) * 4 + 3];
                    const cornerAlpha4 = pixels[(size * size - 1) * 4 + 3];

                    const isAlreadyTransparent = (cornerAlpha1 === 0 || cornerAlpha2 === 0 || cornerAlpha3 === 0 || cornerAlpha4 === 0);

                    if (!isAlreadyTransparent) {
                        // Image has solid opaque background (e.g. JPG photo) -> Run background keyer
                        const solidOutline = new Uint8Array(size * size);
                        for (let i = 0; i < pixels.length; i += 4) {
                            const r = pixels[i];
                            const g = pixels[i+1];
                            const b = pixels[i+2];
                            const a = pixels[i+3];
                            if (a > 50 && (r < 220 || g < 220 || b < 220)) {
                                solidOutline[i / 4] = 1;
                            }
                        }

                        const closedOutline = new Uint8Array(size * size);
                        const r_dilate = 3;
                        for (let y = 0; y < size; y++) {
                            for (let x = 0; x < size; x++) {
                                if (solidOutline[y * size + x]) {
                                    for (let dy = -r_dilate; dy <= r_dilate; dy++) {
                                        const ny = y + dy;
                                        if (ny >= 0 && ny < size) {
                                            for (let dx = -r_dilate; dx <= r_dilate; dx++) {
                                                const nx = x + dx;
                                                if (nx >= 0 && nx < size) {
                                                    closedOutline[ny * size + nx] = 1;
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }

                        const transparentBackground = new Uint8Array(size * size);
                        const queue = [];
                        
                        for (let x = 0; x < size; x++) {
                            if (!closedOutline[x]) { transparentBackground[x] = 1; queue.push(x); }
                            const bottomIdx = (size - 1) * size + x;
                            if (!closedOutline[bottomIdx]) { transparentBackground[bottomIdx] = 1; queue.push(bottomIdx); }
                        }
                        for (let y = 0; y < size; y++) {
                            const leftIdx = y * size;
                            if (!closedOutline[leftIdx]) { transparentBackground[leftIdx] = 1; queue.push(leftIdx); }
                            const rightIdx = y * size + (size - 1);
                            if (!closedOutline[rightIdx]) { transparentBackground[rightIdx] = 1; queue.push(rightIdx); }
                        }

                        while (queue.length > 0) {
                            const idx = queue.shift();
                            const cx = idx % size;
                            const cy = Math.floor(idx / size);

                            const neighbors = [
                                {x: cx - 1, y: cy}, {x: cx + 1, y: cy},
                                {x: cx, y: cy - 1}, {x: cx, y: cy + 1}
                            ];

                            for (const n of neighbors) {
                                if (n.x >= 0 && n.x < size && n.y >= 0 && n.y < size) {
                                    const nIdx = n.y * size + n.x;
                                    if (!closedOutline[nIdx] && !transparentBackground[nIdx]) {
                                        transparentBackground[nIdx] = 1;
                                        queue.push(nIdx);
                                    }
                                }
                            }
                        }

                        for (let i = 0; i < pixels.length; i += 4) {
                            const idx = i / 4;
                            if (transparentBackground[idx]) {
                                pixels[i + 3] = 0;
                            }
                        }
                        imgCtx.putImageData(imgData, 0, 0);
                    }
                }

                // Canvas B: Solid Character Mask Canvas
                const maskCanvas = document.createElement('canvas');
                maskCanvas.width = size;
                maskCanvas.height = size;
                const maskCtx = maskCanvas.getContext('2d');
                maskCtx.drawImage(imgCanvas, 0, 0);
                
                const maskData = maskCtx.getImageData(0, 0, size, size);
                const mPixels = maskData.data;
                for (let i = 0; i < mPixels.length; i += 4) {
                    const alpha = mPixels[i + 3];
                    if (alpha > 10) {
                        mPixels[i] = 255;
                        mPixels[i+1] = 255;
                        mPixels[i+2] = 255;
                        mPixels[i+3] = 255;
                    } else {
                        mPixels[i+3] = 0;
                    }
                }
                maskCtx.putImageData(maskData, 0, 0);

                // Canvas C: 100% Clean 3-Step Composited Texture (NO SOLID WHITE MASKS, NO SAFARI BUGS!)
                const finalCanvas = document.createElement('canvas');
                finalCanvas.width = size;
                finalCanvas.height = size;
                const finalCtx = finalCanvas.getContext('2d');

                // Step 1: Soft Drop Shadow underneath character
                finalCtx.save();
                finalCtx.shadowColor = 'rgba(0, 0, 0, 0.35)';
                finalCtx.shadowBlur = 16;
                finalCtx.shadowOffsetY = 8;
                finalCtx.drawImage(maskCanvas, 0, 0);
                finalCtx.restore();

                // Step 2: Clear inside of drop shadow area so original colors are 100% pure
                finalCtx.globalCompositeOperation = 'destination-out';
                finalCtx.drawImage(maskCanvas, 0, 0);
                finalCtx.globalCompositeOperation = 'source-over';

                // Step 3: Draw original crisp image/photo (100% crisp original artwork/photo)
                finalCtx.drawImage(imgCanvas, 0, 0);
                if (typeof applyTopBottomDomeCaps === 'function') { applyTopBottomDomeCaps(finalCtx); }

                


                
                // Round off any flat top edge on rabbit ears with smooth dome mask
                imgCtx.save();
                imgCtx.globalCompositeOperation = 'destination-in';
                imgCtx.beginPath();
                imgCtx.ellipse(size / 2, size / 2 + 15, size * 0.48, size * 0.46, 0, 0, Math.PI * 2);
                imgCtx.fill();
                imgCtx.restore();

                const finalImgData = finalCanvas.toDataURL('image/png');
                
                if (isInitializingDefaultJelly) {
                    defaultStrawberrySrc = finalImgData;
                    isInitializingDefaultJelly = false;
                    
                    jellyImage.src = finalImgData;
                    initMesh();
                    renderLobbyGrid();
                    const thumb = document.getElementById('card-strawberry-thumb');
                    if (thumb) {
                        thumb.style.backgroundImage = `url(${finalImgData})`;
                    }
                    return;
                }

                const newChar = {
                    emoji: '📸',
                    name: `${i18n.t('card-camera') || '내 사진'} ${customPhotoCounter++}`,
                    base: `custom_photo_${Date.now()}`,
                    hue: 355,
                    imgData: finalImgData
                };
                lobbyCharacters.push(newChar);
                activeLobbyIndex = lobbyCharacters.length - 1;
                
                activeEmoji = newChar.emoji;
                activeBase = newChar.base;
                activeHue = newChar.hue;
                
                jellyImage.onload = function() {
                    initMesh();
                    draw();
                };
                jellyImage.onload = function() {
                    initMesh();
                    draw();
                };
                jellyImage.src = finalImgData;
                initMesh();
                generateDecoJellies(355);
                renderLobbyGrid();
                setScreenMode('lobby');
                showNotification(i18n.t('notif-silhouette-mapping'));
            } catch (err) {
                console.error("processImageToJelly error:", err);
                showNotification("Image processing failed: " + err.message);
            }
        }

        function importFromIllustrationCard(cardId) {
            activeEmoji = '🎨';
            activeBase = 'illust_body';
            showNotification(i18n.t('notif-illust-crop'));

            document.querySelectorAll('#character-pop .grid-card').forEach(el => el.classList.remove('active'));
            document.getElementById(cardId).classList.add('active');
            closePop('character-pop');
        }

        function selectFeelCard(feel, cardId) {
            activeFeel = feel;
            document.querySelectorAll('#feel-pop .grid-card').forEach(el => el.classList.remove('active'));
            document.getElementById(cardId).classList.add('active');

            if (feel === 'jelly') {
                stiffness = 50; damping = 8;
            } else if (feel === 'mochi') {
                stiffness = 110; damping = 18;
            } else { // slime
                stiffness = 15; damping = 3;
            }

            document.getElementById('spring-stiffness').value = stiffness;
            document.getElementById('dampening').value = damping;

            if (feel === 'jelly') {
                showNotification(i18n.t('notif-jelly'));
            } else if (feel === 'mochi') {
                showNotification(i18n.t('notif-mochi'));
            } else {
                showNotification(i18n.t('notif-slime'));
            }
            closePop('feel-pop');
        }

        // Instant Photo Snapshot Capture (with flash animation overlay)
        function capturePhotoInstant() {
            const stage = document.querySelector('.stage-area');
            const flash = document.createElement('div');
            flash.style.position = 'absolute';
            flash.style.top = 0; flash.style.left = 0; flash.style.width = '100%'; flash.style.height = '100%';
            flash.style.backgroundColor = '#fff'; flash.style.zIndex = 999;
            flash.style.transition = 'opacity 0.2s ease-out';
            stage.appendChild(flash);
            
            setTimeout(() => {
                flash.style.opacity = 0;
                setTimeout(() => flash.remove(), 200);
            }, 50);

            document.getElementById('preview-box').innerHTML = '<div style="font-size: 3rem; margin-bottom:12px;">📸</div>' + i18n.t('preview-snapshot-saved');
            openResultModal();
            showNotification(i18n.t('notif-snapshot'));
        }

        // 100% Clean Stage (All background jellies deleted)
        
        function generateDecoJellies(baseHue) {
            decoJellies = [];
        }
                // ==========================================================================
        // 100% UNTOUCHED USER DECO JELLIES FLOATING STAGE ENGINE (jy-01 ~ jy-19)
        // ==========================================================================
        let decoJellyImages = [];
        let decoJellies = [];
        const DECO_FILE_NAMES = [
            'jy-01.png', 'jy-02.png', 'jy-03.png', 'jy-04.png', 'jy-05.png',
            'jy-06.png', 'jy-07.png', 'jy-08.png', 'jy-09.png', 'jy-10.png',
            'jy-11.png', 'jy-12.png', 'jy-13.png', 'jy-14.png', 'jy-15.png',
            'jy-16.png', 'jy-17.png', 'jy-18.png', 'jy-19.png'
        ];

        function loadDecoJellySprites() {
            decoJellyImages = [];
            for (let i = 0; i < DECO_FILE_NAMES.length; i++) {
                let img = new Image();
                img.src = `deco_sprites/${DECO_FILE_NAMES[i]}`;
                decoJellyImages.push(img);
            }
        }
        loadDecoJellySprites();

        function generateDecoJellies() {
            decoJellies = [];
            let stageW = width || 388;
            let stageH = height || 800;

            for (let i = 0; i < DECO_FILE_NAMES.length; i++) {
                decoJellies.push({
                    imgIndex: i,
                    x: Math.random() * stageW,
                    y: Math.random() * stageH,
                    vx: (Math.random() - 0.5) * 0.15, // Ultra-slow relaxing drift
                    vy: (Math.random() - 0.5) * 0.15,
                    scale: 0.05 + Math.random() * 0.10, // Diverse sizes (small to large)
                    angle: Math.random() * Math.PI * 2,
                    vRot: (Math.random() - 0.5) * 0.005,
                    bobOffset: Math.random() * Math.PI * 2
                });
            }
        }

        function drawDecoJellies() {
            if (!decoJellies || decoJellies.length === 0) {
                generateDecoJellies();
            }

            let stageW = width || 388;
            let stageH = height || 800;
            let time = Date.now() * 0.0015;

            for (let i = 0; i < decoJellies.length; i++) {
                let j = decoJellies[i];
                let img = decoJellyImages[j.imgIndex];

                // Slow random floating drift
                j.x += j.vx;
                j.y += j.vy + Math.sin(time + j.bobOffset) * 0.12;
                j.angle += j.vRot;

                // Infinite wrap-around
                if (j.x < -60) j.x = stageW + 60;
                if (j.x > stageW + 60) j.x = -60;
                if (j.y < -60) j.y = stageH + 60;
                if (j.y > stageH + 60) j.y = -60;

                if (img && img.complete && img.naturalWidth > 0) {
                    ctx.save();
                    ctx.translate(j.x, j.y);
                    ctx.rotate(j.angle);
                    ctx.scale(j.scale, j.scale);
                    ctx.globalAlpha = 0.88;

                    // Soft ambient shadow
                    ctx.fillStyle = 'rgba(0, 0, 0, 0.10)';
                    ctx.beginPath();
                    ctx.ellipse(0, 45, 45, 15, 0, 0, Math.PI * 2);
                    ctx.fill();

                    // Render untouched user original jelly image
                    ctx.drawImage(img, -img.naturalWidth / 2, -img.naturalHeight / 2);
                    ctx.restore();
                }
            }
        }

        function handleRecordToggle() {
            stopAutopilot(); releaseGrab(true); releaseGrab(true);
            if (isRecording) {
                stopVideoRecording();
            } else {
                startVideoRecording();
            }
        }

        // 📹 녹화 시작
        function startVideoRecording() {
            if (isRecording) return;
            
            const countdown = document.getElementById('countdown-overlay');
            countdown.style.display = 'flex';
            let count = 3;
            countdown.innerText = count;

            countdownInterval = setInterval(() => {
                count--;
                if (count > 0) {
                    countdown.innerText = count;
                } else {
                    clearInterval(countdownInterval);
                    countdown.style.display = 'none';
                    triggerRecLoop();
                }
            }, 800);
        }

        function triggerRecLoop() {
            isRecording = true;
            
            // Update icon to stop symbol (⏹️)
            const globalBtn = document.getElementById('global-rec-btn');
            if (globalBtn) { 
                globalBtn.innerHTML = '<img src="stop.png" alt="중지" style="width: 32px; height: 32px; object-fit: contain;">'; 
                globalBtn.title = '녹화 중지'; 
            }

            const pill = document.getElementById('recording-indicator');
            pill.style.display = 'flex';

            let duration = 0;
            document.getElementById('rec-timer').innerText = '00:00';

            // Start Canvas Stream Recording
            if (window.MediaRecorder && canvas) {
                recordedChunks = [];
                let stream = null;
                try {
                    // Capture canvas at 30 FPS
                    stream = canvas.captureStream(30);
                } catch (e) {
                    console.log("captureStream(30) failed, falling back to captureStream() without parameters", e);
                    stream = canvas.captureStream ? canvas.captureStream() : null;
                }

                if (stream) {
                    let options = {};
                    const codecs = [
                        'video/mp4',
                        'video/webm;codecs=vp9',
                        'video/webm;codecs=vp8',
                        'video/webm',
                        'video/quicktime'
                    ];
                    for (const codec of codecs) {
                        if (MediaRecorder.isTypeSupported(codec)) {
                            options.mimeType = codec;
                            break;
                        }
                    }

                    try {
                        mediaRecorder = new MediaRecorder(stream, options);
                    } catch (e2) {
                        console.log("MediaRecorder initialization with options failed, fallback to default", e2);
                        try {
                            mediaRecorder = new MediaRecorder(stream);
                        } catch (e3) {
                            console.error("MediaRecorder fallback failed:", e3);
                            mediaRecorder = null;
                        }
                    }

                    if (mediaRecorder) {
                        mediaRecorder.ondataavailable = function(e) {
                            if (e.data && e.data.size > 0) {
                                recordedChunks.push(e.data);
                            }
                        };
                        mediaRecorder.onstop = function() {
                            if (recordedChunks.length > 0) {
                                const type = mediaRecorder.mimeType || 'video/webm';
                                lastRecordedBlob = new Blob(recordedChunks, { type: type });
                                const videoURL = URL.createObjectURL(lastRecordedBlob);
                                const previewVideo = document.getElementById('result-video-preview');
                                if (previewVideo) {
                                    previewVideo.src = videoURL;
                                }
                            }
                        };
                        mediaRecorder.start();
                    }
                }
            }
            
            recordingTimerInterval = setInterval(() => {
                duration++;
                const pad = duration < 10 ? '0' : '';
                document.getElementById('rec-timer').innerText = `00:${pad}${duration}`;
                
                // Max recording duration: 15 seconds
                if (duration >= 15) {
                    stopVideoRecording();
                }
            }, 1000);
        }

        // ⏹️ 녹화 정지
        function stopVideoRecording() {
            if (!isRecording) {
                // If countdown is active, cancel it
                if (countdownInterval) {
                    clearInterval(countdownInterval);
                    countdownInterval = null;
                    const countdown = document.getElementById('countdown-overlay');
                    if (countdown) countdown.style.display = 'none';
                }
                return;
            }

            isRecording = false;
            
            if (recordingTimerInterval) {
                clearInterval(recordingTimerInterval);
                recordingTimerInterval = null;
            }

            // Hide recording pill
            const pill = document.getElementById('recording-indicator');
            if (pill) pill.style.display = 'none';

            // Reset icon back to video symbol (📹)
            const globalBtn = document.getElementById('global-rec-btn');
            if (globalBtn) { 
                globalBtn.innerHTML = '<img src="movie.png" alt="녹화" style="width: 32px; height: 32px; object-fit: contain;">'; 
                globalBtn.title = i18n.t('btn-rec'); 
            }

            // Stop Canvas recording
            if (mediaRecorder && mediaRecorder.state !== 'inactive') {
                try {
                    mediaRecorder.stop();
                } catch (e) {
                    console.error("Error stopping media recorder:", e);
                }
            }

            openResultModal();
            showNotification(i18n.t('notif-rec-complete'));
        }

        function openResultModal() {
            document.getElementById('result-modal').style.display = 'flex';
        }

        function closeResultModal() {
            document.getElementById('result-modal').style.display = 'none';
            const previewVideo = document.getElementById('result-video-preview');
            if (previewVideo) {
                previewVideo.src = '';
            }
        }

        function saveToGallery() {
            if (!lastRecordedBlob) {
                showNotification("No recorded video found.");
                return;
            }
            closeResultModal();
            
            let ext = 'webm';
            let mime = 'video/webm';
            if (lastRecordedBlob.type.includes('mp4')) {
                ext = 'mp4';
                mime = 'video/mp4';
            } else if (lastRecordedBlob.type.includes('quicktime')) {
                ext = 'mov';
                mime = 'video/quicktime';
            }

            const filename = `squishy-rabbit-${Date.now()}.${ext}`;
            const file = new File([lastRecordedBlob], filename, { type: mime });

            // 📱 Web Share API support check (highly reliable for mobile gallery saving/sharing)
            if (navigator.canShare && navigator.canShare({ files: [file] })) {
                navigator.share({
                    files: [file],
                    title: 'Fruitrabbit Malrangi Video',
                    text: 'Check out my squishy rabbit video!'
                }).then(() => {
                    showNotification(i18n.t('notif-gallery-saved'));
                }).catch(err => {
                    console.log("Web share failed, fallback to download:", err);
                    triggerDirectDownload(filename);
                });
            } else {
                triggerDirectDownload(filename);
            }
        }

        function triggerDirectDownload(filename) {
            const url = URL.createObjectURL(lastRecordedBlob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            setTimeout(() => {
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            }, 150);
            showNotification(i18n.t('notif-gallery-saved'));
        }

        function showNotification(msg) {
            console.log(msg);
            const toast = document.getElementById('toast-el');
            if (!toast) return;
            toast.innerText = msg;
            toast.classList.add('active');
            
            if (window.toastTimeout) clearTimeout(window.toastTimeout);
            window.toastTimeout = setTimeout(() => {
                toast.classList.remove('active');
            }, 2500);
        }

        function drawWarpedTriangle(ctx, img, p0, p1, p2, imgW, imgH) {
            let minOx = points[0].ox;
            let maxOx = points[cols - 1].ox;
            let minOy = points[0].oy;
            let maxOy = points[(rows - 1) * cols].oy;

            let meshWidth = maxOx - minOx;
            let meshHeight = maxOy - minOy;

            // 100% FULL texture mapping to exact original image bounds (0 to imgW, 0 to imgH)
            let u0 = ((p0.ox - minOx) / meshWidth) * imgW;
            let v0 = ((p0.oy - minOy) / meshHeight) * imgH;
            let u1 = ((p1.ox - minOx) / meshWidth) * imgW;
            let v1 = ((p1.oy - minOy) / meshHeight) * imgH;
            let u2 = ((p2.ox - minOx) / meshWidth) * imgW;
            let v2 = ((p2.oy - minOy) / meshHeight) * imgH;

            let x0 = p0.x;
            let y0 = p0.y;
            let x1 = p1.x;
            let y1 = p1.y;
            let x2 = p2.x;
            let y2 = p2.y;

            ctx.save();
            ctx.beginPath();
            ctx.moveTo(x0, y0);
            ctx.lineTo(x1, y1);
            ctx.lineTo(x2, y2);
            ctx.closePath();
            ctx.clip();

            // Solve affine matrix: u * A + B = x
            let denom = u0 * (v1 - v2) + u1 * (v2 - v0) + u2 * (v0 - v1);
            // Ignore inverted/flipped triangles so character texture NEVER flips backward like paper
            if (denom <= 0.1) {
                ctx.restore();
                return;
            }

            let a = (x0 * (v1 - v2) + x1 * (v2 - v0) + x2 * (v0 - v1)) / denom;
            let b = (y0 * (v1 - v2) + y1 * (v2 - v0) + y2 * (v0 - v1)) / denom;
            let c = (x0 * (u2 - u1) + x1 * (u0 - u2) + x2 * (u1 - u0)) / denom;
            let d = (y0 * (u2 - u1) + y1 * (u0 - u2) + y2 * (u1 - u0)) / denom;
            let e = x0 - a * u0 - c * v0;
            let f = y0 - b * u0 - d * v0;

            ctx.transform(a, b, c, d, e, f);
            ctx.drawImage(img, 0, 0);
            ctx.restore();
        }

        // Draw loop
        let lastDrawErrorTime = 0;
        
        function draw() {
            try {
                ctx.clearRect(0, 0, width, height);

                // Dynamic theme-matched background gradient
                let bgGrad = ctx.createLinearGradient(0, 0, 0, height);
                bgGrad.addColorStop(0, `hsla(${activeHue}, 75%, 90%, 1)`); // soft pastel top
                bgGrad.addColorStop(1, `hsla(${activeHue}, 65%, 78%, 1)`); // slightly richer bottom
                ctx.fillStyle = bgGrad;
                ctx.fillRect(0, 0, width, height);

                // Draw floating decorative background jellies
                drawDecoJellies();

                                                                // --- 1. Soft Tangle Jelly (Inward Dimple + Soft Drag) & Single-Mass Gravity Gel Slime ---
                let currentMode = (typeof activeTextureMode !== 'undefined') ? activeTextureMode : 'jelly';

                if (isTouching) {
                    touchTime++;

                    let maxRadius = width * 0.48;

                    // 2-Finger Pinch Balloon Swell (두 손가락 핀치 시 가운데 풍선 부풀어 오름)
                    if (activeTouchList && activeTouchList.length >= 2) {
                        let t1 = activeTouchList[0];
                        let t2 = activeTouchList[1];
                        let midX = (t1.x + t2.x) / 2;
                        let midY = (t1.y + t2.y) / 2;
                        let fDist = Math.hypot(t2.x - t1.x, t2.y - t1.y);

                        let swellRadius = Math.max(width * 0.42, fDist * 1.35);
                        let bulgeForce = Math.min(50.0, Math.max(18.0, (300.0 - fDist) * 0.38));

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - midX;
                            let dy = p.oy - midY;
                            let dist = Math.hypot(dx, dy);

                            if (dist < swellRadius && dist > 1.0) {
                                let weight = Math.pow(1 - dist / swellRadius, 1.5);
                                let nx = dx / dist;
                                let ny = dy / dist;

                                p.x += nx * weight * bulgeForce * 0.42;
                                p.y += ny * weight * bulgeForce * 0.42;
                            }
                        }

                        // Render 3D swelling balloon specular light reflection
                        ctx.save();
                        let bGrad = ctx.createRadialGradient(midX, midY, 5, midX, midY, swellRadius * 0.70);
                        bGrad.addColorStop(0, 'rgba(255, 255, 255, 0.78)');
                        bGrad.addColorStop(0.35, 'rgba(255, 245, 210, 0.42)');
                        bGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
                        ctx.fillStyle = bGrad;
                        ctx.beginPath();
                        ctx.arc(midX, midY, swellRadius * 0.70, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.restore();
                    } else if (currentMode === 'slime') {
                        // [슬라임 모드]: 100% 1개 단일 덩어리 보존 (잘림/찢어짐 0%) + 중력 기반 바닥 겔 퍼짐 (Gravity Gel Pooling)
                        let pressRadius = width * 0.55;
                        let gravityForce = Math.min(58.0, 18.0 + touchTime * 1.25);

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let dx = p.ox - touchX;
                            let dy = p.oy - touchY;
                            let dist = Math.hypot(dx, dy);

                            if (dist < pressRadius && dist > 0.1) {
                                let weight = Math.pow(1 - dist / pressRadius, 1.3);
                                let nx = dx / dist;

                                // Single solid mass gravity pooling: Gel spreads horizontally and settles downward under gravity
                                p.x += nx * weight * gravityForce * 0.48; // Horizontal gel expansion to left & right
                                p.y += weight * gravityForce * 0.32;      // Gravity gel settling towards floor
                            }
                        }
                    } else if (currentMode === 'mochi') {
                        // [쫀득모찌 모드]: 찰떡처럼 쫀득하게 천천히 늘어나는 플라스틱 모찌
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let distSq = pdx * pdx + pdy * pdy;
                                let weight = Math.exp(-distSq / (150.0 * 150.0));

                                p.x = p.ox + dragDx * weight * 0.92;
                                p.y = p.oy + dragDy * weight * 0.92;
                                p.vx *= 0.12; p.vy *= 0.12;
                            }
                        }
                                        } else {
                        // [탱글젤리 모드]: v111 100% 깨짐 없는 3D 함몰 (Non-Tearing Soft 3D Dimple) + 당기기
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;
                            let dragDist = Math.hypot(dragDx, dragDy);

                            if (dragDist < 8.0) {
                                // 1. 누름 상태 (Drag < 8px): 터치 지점 중심으로 움푹 들어가는 깨짐 0% 3D 함몰 효과
                                let dimpleRadius = width * 0.38;
                                let dimpleDepth = 28.0;

                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let dx = p.ox - touchX;
                                    let dy = p.oy - touchY;
                                    let dist = Math.hypot(dx, dy);

                                    if (dist < dimpleRadius && dist > 0.1) {
                                        let weight = Math.pow(1 - dist / dimpleRadius, 1.6);
                                        let nx = dx / dist;
                                        let ny = dy / dist;

                                        // Inward squish & dimple depression (깨짐 없는 부드러운 함몰)
                                        p.x -= nx * weight * dimpleDepth * 0.32;
                                        p.y -= ny * weight * dimpleDepth * 0.32;

                                        p.lastDx = p.x - p.ox;
                                        p.lastDy = p.y - p.oy;
                                    }
                                }

                                // Render concave 3D dimple inner shadow ring
                                ctx.save();
                                let dGrad = ctx.createRadialGradient(touchX, touchY, 2, touchX, touchY, dimpleRadius * 0.55);
                                dGrad.addColorStop(0, 'rgba(0, 0, 0, 0.32)');
                                dGrad.addColorStop(0.5, 'rgba(0, 0, 0, 0.12)');
                                dGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                                ctx.fillStyle = dGrad;
                                ctx.beginPath();
                                ctx.arc(touchX, touchY, dimpleRadius * 0.55, 0, Math.PI * 2);
                                ctx.fill();
                                ctx.restore();

                            } else {
                                // 2. 당기기/밀기 상태 (Drag >= 8px): 터치 부위가 길고 쫀쫀하게 당겨짐 (100% 보존)
                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let pdx = p.ox - gNode.ox;
                                    let pdy = p.oy - gNode.oy;
                                    let dist = Math.hypot(pdx, pdy);

                                    let sigma = 100.0;
                                    let weight = Math.exp(-(dist * dist) / (2.0 * sigma * sigma));

                                    p.x = p.ox + dragDx * weight * 1.35;
                                    p.y = p.oy + dragDy * weight * 1.35;

                                    p.lastDx = p.x - p.ox;
                                    p.lastDy = p.y - p.oy;
                                }
                            }
                        }
                    }

        body {
            font-family: 'Inter', sans-serif;
            background: radial-gradient(circle at center, #1b2029 0%, #07080a 100%);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        /* 2. Phone Simulator (Viewport) Centered */
        .phone-frame {
            width: 412px !important;
            height: 840px !important;
            max-width: 412px !important;
            max-height: 840px !important;
            margin: auto !important;
            flex-shrink: 0 !important;
            background: #000;
            border-radius: 48px !important;
            border: 12px solid #232a37 !important;
            position: relative;
            overflow: hidden;
            box-shadow: 0 25px 60px rgba(0,0,0,0.85), 0 0 0 1px rgba(255,255,255,0.1);
            display: flex;
            flex-direction: column;
        }

        /* Notch representation */
        .phone-notch {
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 140px;
            height: 28px;
            background: var(--phone-border);
            border-bottom-left-radius: 18px;
            border-bottom-right-radius: 18px;
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .phone-notch::before {
            content: '';
            width: 50px;
            height: 4px;
            background: #0d0f12;
            border-radius: 2px;
        }

        /* Full Screen Interactive Canvas Area */
        .stage-area {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(180deg, #ff4757 0%, #ff6b81 100%);
            z-index: 1;
        }

        canvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        /* Minimal Top Bar UI Overlay */
        .top-overlay-ui {
            position: absolute;
            top: 40px;
            left: 0;
            width: 100%;
            padding: 0 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1010; /* Float above both lobby and playground screen stages */
        }

        .action-circle-btn {
            width: 36px;
            height: 36px;
            background: transparent;
            border: none;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            cursor: pointer;
            backdrop-filter: none;
            transition: all 0.2s ease;
            box-shadow: none;
        }

        .action-circle-btn:hover {
            transform: scale(1.12);
        }

        .action-circle-btn img {
            width: 28px !important;
            height: 28px !important;
            object-fit: contain;
        }

        /* Game Start Splash Screen Style */
        .start-splash-screen { 
            display: flex;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #090712 0%, #120e24 50%, #1c1535 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 2500; /* Float over everything */
            transition: opacity 0.6s cubic-bezier(0.25, 1, 0.5, 1), visibility 0.6s;
            padding: 24px;
            box-sizing: border-box;
        }

        .start-splash-screen.fade-out {
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
        }

        .start-logo-container {
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 50px;
            filter: drop-shadow(0 10px 25px rgba(0, 0, 0, 0.55));
        }

        .start-logo-img {
            width: 100%;
            max-width: 320px;
            height: auto;
            object-fit: contain;
            animation: floatLogo 4s ease-in-out infinite;
        }

        @keyframes floatLogo {
            0% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-12px) rotate(1deg); }
            100% { transform: translateY(0px) rotate(0deg); }
        }

        .start-game-btn {
            background: linear-gradient(135deg, #ff4757, #ff6b81);
            color: white;
            border: none;
            border-radius: 24px;
            padding: 16px 48px;
            font-size: 1.35rem;
            font-weight: 800;
            box-shadow: 0 8px 24px rgba(255, 71, 87, 0.45), 0 0 0 4px rgba(255, 71, 87, 0.2);
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            animation: pulseBtn 2s infinite;
            font-family: 'Outfit', 'Inter', sans-serif;
        }

        .start-game-btn:hover {
            transform: scale(1.08);
            background: linear-gradient(135deg, #ff6b81, #ff4757);
            box-shadow: 0 10px 28px rgba(255, 71, 87, 0.55), 0 0 0 6px rgba(255, 71, 87, 0.3);
        }

        @keyframes pulseBtn {
            0% { transform: scale(1); }
            50% { transform: scale(1.03); }
            100% { transform: scale(1); }
        }

        .start-footer-text {
            position: absolute;
            bottom: 24px;
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.35);
            font-weight: 600;
            letter-spacing: 0.5px;
        }

        .recording-pill {
            background: rgba(255, 71, 87, 0.25);
            border: 1.5px solid var(--active-color);
            color: #ff4757;
            padding: 6px 16px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.8rem;
            display: flex;
            align-items: center;
            gap: 6px;
            animation: pulse 1.5s infinite;
        }

        .blinking-dot {
            width: 8px;
            height: 8px;
            background: #ff4757;
            border-radius: 50%;
            display: inline-block;
            animation: blink-dot 0.8s infinite alternate;
        }

        @keyframes blink-dot {
            from { opacity: 0.3; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1.2); }
        }

        /* Bottom Floating Drawer Sheet */
        .bottom-drawer {
            position: absolute;
            bottom: 24px;
            left: 16px;
            right: 16px;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 28px;
            padding: 20px;
            backdrop-filter: blur(25px);
            z-index: 20;
            box-shadow: 0 15px 40px rgba(0,0,0,0.4);
            display: flex;
            flex-direction: column;
            gap: 16px;
            transition: transform 0.3s ease;
        }

        .drawer-row {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .row-title {
            font-family: 'Outfit', sans-serif;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--text-secondary);
            display: flex;
            justify-content: space-between;
        }

        /* Horizontal Scroll Trays */
        .scroll-tray {
            display: flex;
            gap: 12px;
            overflow-x: auto;
            padding-bottom: 6px;
            scrollbar-width: none; /* Hide scrollbar for clean UI */
        }

        .scroll-tray::-webkit-scrollbar {
            display: none;
        }

        .tray-item {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 12px 18px;
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            white-space: nowrap;
            font-weight: 600;
            font-size: 0.85rem;
            transition: all 0.2s ease;
        }

        .tray-item:hover {
            background: rgba(255, 71, 87, 0.1);
            border-color: rgba(255, 71, 87, 0.3);
        }

        .tray-item.active {
            background: var(--active-color);
            border-color: var(--active-color);
            color: #fff;
            box-shadow: 0 0 15px var(--accent-glow);
        }

        .tray-emoji {
            font-size: 1.4rem;
        }

        /* Advanced Options Overlay */
        .advanced-settings-drawer {
            position: absolute;
            top: 155px;
            left: 16px;
            right: 16px;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 16px;
            backdrop-filter: blur(25px);
            z-index: 1050;
            display: none;
            flex-direction: column;
            gap: 12px;
            font-size: 0.8rem;
        }

        .advanced-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        input[type="range"] {
            width: 140px;
            accent-color: var(--active-color);
        }

        /* Pop-up Modals CSS styling */
        .pop-overlay {
            position: absolute;
            bottom: 24px;
            left: 20px;
            right: 20px;
            background: var(--glass-bg);
            border: 1.5px solid var(--glass-border);
            border-radius: 28px;
            padding: 20px;
            backdrop-filter: blur(25px);
            z-index: 50;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            gap: 16px;
            animation: slideUp 0.3s cubic-bezier(0.1, 0.76, 0.55, 0.94);
        }

        @keyframes slideUp {
            from { transform: translateY(100px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        .pop-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'Outfit', sans-serif;
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .close-pop-btn {
            font-size: 1.2rem;
            cursor: pointer;
            color: var(--text-secondary);
            padding: 4px 8px;
            transition: color 0.2s;
        }
        .close-pop-btn:hover {
            color: var(--active-color);
        }

        .pop-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
        }

        .grid-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 20px;
            padding: 12px 6px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .grid-card:hover {
            background: rgba(255, 71, 87, 0.08);
            border-color: rgba(255, 71, 87, 0.2);
        }

        .grid-card.active {
            background: rgba(255, 71, 87, 0.15);
            border-color: var(--active-color);
            box-shadow: 0 0 12px rgba(255, 71, 87, 0.2);
        }

        .card-thumb {
            width: 54px;
            height: 54px;
            border-radius: 12px;
            background-size: cover;
            background-position: center;
            background-color: rgba(255,255,255,0.05);
        }

        .card-thumb-emoji {
            font-size: 2.2rem;
            width: 54px;
            height: 54px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card-name {
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-primary);
            text-align: center;
        }

        /* 3. Screen Record Toast */
        .countdown-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.6);
            display: none;
            align-items: center;
            justify-content: center;
            font-size: 5rem;
            font-weight: 800;
            color: #fff;
            z-index: 90;
        }

        /* Share / Result modal */
        .result-modal {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.85);
            display: none;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px;
            z-index: 110;
        }

        .preview-box {
            width: 100%;
            aspect-ratio: 9/16;
            background: #111;
            border-radius: 20px;
            border: 1px solid var(--glass-border);
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.9rem;
            color: var(--text-secondary);
            position: relative;
        }

        .modal-buttons {
            display: flex;
            gap: 12px;
            width: 100%;
        }

        .modal-btn {
            flex: 1;
            background: var(--active-color);
            border: none;
            color: #fff;
            padding: 14px;
            border-radius: 12px;
            font-weight: 700;
            cursor: pointer;
        }

        .modal-btn.secondary {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
        }

        /* General layout guidance outside phone */
        .studio-background-info {
            position: absolute;
            left: 40px;
            max-width: 320px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .studio-background-info h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            background: linear-gradient(45deg, #ff4757, #ff6b81);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .info-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 18px;
            font-size: 0.85rem;
            line-height: 1.6;
            color: var(--text-secondary);
        }

        .info-card b {
            color: #fff;
        }

        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }

        /* Dynamic Toast Notification */
        .toast-notification {
            position: absolute;
            top: 70px;
            left: 50%;
            transform: translateX(-50%) translateY(-20px);
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            backdrop-filter: blur(15px);
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            z-index: 2000;
            white-space: nowrap;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        .toast-notification.active {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }

        /* Lobby Screen Layout Styles */
        .lobby-screen {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #151329 0%, #290a36 50%, #0d0f1a 100%);
            display: flex;
            flex-direction: column;
            padding: 170px 20px 20px 20px; /* Clean space below top bar and feel selector */
            box-sizing: border-box;
            z-index: 10000;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .lobby-top-bar {
            display: none; /* Removed as we are using global top menu */
        }

        .lobby-feel-selector {
            position: absolute;
            top: 108px;
            left: 24px;
            right: 24px;
            display: flex;
            justify-content: space-between;
            gap: 8px;
            z-index: 1010; /* On top of lobby screen */
        }

        .feel-pill {
            flex: 1;
            padding: 10px 0;
            border-radius: 14px;
            font-size: 0.85rem;
            font-weight: 700;
            text-align: center;
            cursor: pointer;
            pointer-events: auto !important;
            user-select: none;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }

        #pill-jelly {
            background: rgba(125, 28, 36, 0.5) !important;
            color: rgba(255, 255, 255, 0.7) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            transform: scale(1);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }
        #pill-mochi {
            background: rgba(128, 74, 24, 0.5) !important;
            color: rgba(255, 255, 255, 0.7) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            transform: scale(1);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }
        #pill-slime {
            background: rgba(8, 84, 64, 0.5) !important;
            color: rgba(255, 255, 255, 0.7) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            transform: scale(1);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }

        #pill-jelly.active {
            background: linear-gradient(135deg, #ff4757, #ff6b81) !important;
            color: #ffffff !important;
            border: 2px solid #ffffff !important;
            box-shadow: 0 8px 24px rgba(255, 71, 87, 0.85), 0 0 12px #ffffff !important;
            transform: scale(1.08) !important;
        }

        #pill-mochi.active {
            background: linear-gradient(135deg, #ff9f43, #f39c12) !important;
            color: #ffffff !important;
            border: 2px solid #ffffff !important;
            box-shadow: 0 8px 24px rgba(255, 159, 67, 0.85), 0 0 12px #ffffff !important;
            transform: scale(1.08) !important;
        }

        #pill-slime.active {
            background: linear-gradient(135deg, #10ac84, #1dd1a1) !important;
            color: #ffffff !important;
            border: 2px solid #ffffff !important;
            box-shadow: 0 8px 24px rgba(16, 172, 132, 0.85), 0 0 12px #ffffff !important;
            transform: scale(1.08) !important;
        }

        .lobby-grid-container {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow-y: auto;
            scrollbar-width: none;
        }
        .lobby-grid-container::-webkit-scrollbar {
            display: none;
        }

        .character-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            justify-items: center;
            align-content: start;
            margin-bottom: 30px;
        }

        .grid-char-bubble {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: radial-gradient(circle at 35% 35%, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0.05) 55%, rgba(0,0,0,0.2) 100%);
            border: 1.5px solid rgba(255,255,255,0.12);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            cursor: pointer;
            position: relative;
            box-shadow: 0 6px 16px rgba(0,0,0,0.25);
            transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .grid-char-bubble::after {
            display: none !important;
        }

        .grid-char-bubble.active {
            border-color: var(--active-color);
            box-shadow: 0 0 15px rgba(255, 77, 87, 0.5);
            background: radial-gradient(circle at 35% 35%, rgba(255, 255, 255, 0.3) 0%, rgba(255, 77, 87, 0.15) 50%, rgba(255, 77, 87, 0.3) 100%);
        }

        .grid-char-bubble:hover {
            transform: scale(1.12);
            border-color: rgba(255,255,255,0.25);
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }

        .grid-char-bubble:active {
            transform: scale(0.95);
        }

        .bottom-option-row {
            display: flex;
            justify-content: start;
            gap: 20px;
            padding-top: 15px;
            border-top: 1px solid rgba(255,255,255,0.06);
            margin-top: auto;
        }

        .option-circle {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            cursor: pointer;
        }

        .option-icon {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: rgba(255,255,255,0.05);
            border: 1.5px dashed rgba(255,255,255,0.25);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            transition: all 0.2s ease;
        }

        .option-circle:hover .option-icon {
            background: rgba(255,255,255,0.1);
            border-color: #fff;
            transform: scale(1.05);
        }

        .option-label {
            font-size: 0.72rem;
            font-weight: 700;
            color: rgba(255,255,255,0.7);
        }

        /* 📱 Responsive Mobile Overrides (True Fullscreen on Mobile Devices) */
        @media (max-width: 480px) and (pointer: coarse) {
            body {
                background: #000;
                padding: 0;
                margin: 0;
                min-height: 100vh;
                min-height: 100dvh;
            }
            .phone-frame {
                width: 100vw !important;
                height: 100vh !important;
                height: 100dvh !important;
                border: none !important;
                border-radius: 0 !important;
                box-shadow: none !important;
            }
            .phone-notch {
                display: none !important; /* Hide mock notch on real devices */
            }
            .top-overlay-ui {
                top: 14px !important;
            }
            .lobby-feel-selector {
                top: 92px !important; /* Clear gap below top icons */
            }
            .lobby-screen {
                padding: 140px 16px 16px 16px !important;
            }
            .advanced-settings-drawer {
                top: 135px !important; /* Keep settings below tabs */
                width: calc(100% - 32px) !important;
                left: 16px !important;
            }
        }

        /* 📸 Custom Camera Overlay CSS */
        .camera-overlay {
            display: none;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 2600;
            background: #000;
            flex-direction: column;
            justify-content: space-between;
            padding: 24px;
            box-sizing: border-box;
        }
        
        /* 📸 Face Silhouette Guide overlay inside camera preview */
        .camera-face-guide-container {
            position: absolute;
            top: 15%; /* Raised high up close to top front camera lens */
            left: 50%;
            transform: translateX(-50%);
            width: 240px;
            height: 320px;
            z-index: 3;
            pointer-events: none;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .camera-face-guide-oval {
            width: 100%;
            height: 100%;
            border: 4px dashed rgba(255, 255, 255, 0.7);
            border-radius: 50% / 50%;
            box-shadow: 0 0 0 9999px rgba(0, 0, 0, 0.55); /* Dim dark transparent backdrop outside */
            position: relative;
        }

        .camera-face-guide-text {
            position: absolute;
            bottom: -55px;
            white-space: nowrap;
            color: #ffffff;
            font-size: 0.95rem;
            font-weight: 600;
            background: rgba(0, 0, 0, 0.65);
            padding: 6px 16px;
            border-radius: 16px;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
            animation: pulse-opacity 1.8s infinite alternate;
        }

        @keyframes pulse-opacity {
            0% { opacity: 0.65; }
            100% { opacity: 1; }
        }
        
        .camera-video-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .camera-video-container video, 
        .camera-video-container canvas {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .camera-top-bar {
            display: flex;
            justify-content: space-between;
            width: 100%;
            z-index: 5;
            margin-top: 16px;
        }

        .camera-bottom-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            gap: 24px;
            z-index: 5;
            margin-bottom: 24px;
        }

        .camera-action-btn {
            background: rgba(0, 0, 0, 0.55);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.2s ease;
            outline: none;
        }

        .camera-action-btn:active {
            transform: scale(0.9);
            background: rgba(0, 0, 0, 0.8);
        }

        .camera-capture-trigger {
            width: 72px;
            height: 72px;
            border-radius: 50%;
            background: #ffffff;
            border: 6px solid rgba(255, 255, 255, 0.3);
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            transition: all 0.2s ease;
            outline: none;
        }

        .camera-capture-trigger:active {
            transform: scale(0.92);
            background: #e0e0e0;
        }

        .camera-glass-pill {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            border-radius: 24px;
            padding: 12px 24px;
            color: #ffffff;
            font-size: 0.95rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            outline: none;
        }

        .camera-glass-pill:active {
            transform: scale(0.95);
            background: rgba(255, 255, 255, 0.3);
        }

        .camera-glass-pill.save-pill {
            background: linear-gradient(135deg, #ff4757, #ff6b81);
            border: none;
            box-shadow: 0 4px 15px rgba(255, 71, 87, 0.45);
        }
        
        .camera-glass-pill.save-pill:active {
            background: linear-gradient(135deg, #ff6b81, #ff4757);
        }
    
        .toggle-switch {
            position: relative;
            display: inline-block;
            width: 48px;
            height: 26px;
        }
        .toggle-switch input { opacity: 0; width: 0; height: 0; }
        .toggle-slider {
            position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0;
            background-color: #ccc; transition: .3s; border-radius: 26px;
        }
        .toggle-slider:before {
            position: absolute; content: ""; height: 20px; width: 20px; left: 3px; bottom: 3px;
            background-color: white; transition: .3s; border-radius: 50%;
        }
        input:checked + .toggle-slider { background: linear-gradient(135deg, #ff4757, #ff6b81); }
        input:checked + .toggle-slider:before { transform: translateX(22px); }

        /* Cleanly hide Autopilot and Photo Zone / Image icons per user request */
        #autopilot-btn,
        .bottom-option-row,
        .action-circle-btn[onclick*="handlePhotoZoneGlobal"] {
            display: none !important;
        }
    
        /* Bottom 17 Fruit Rabbit Horizontal Auto-Scroll Carousel Selector */
        .bottom-carousel-container {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 412px;
            height: 98px;
            z-index: 28000;
            background: transparent;
            backdrop-filter: none;
            -webkit-backdrop-filter: none;
            border-radius: 0;
            border: none;
            box-shadow: none;
            overflow: hidden;
            pointer-events: auto;
            display: flex;
            align-items: center;
            padding: 0 4px;
        }

        .bottom-carousel-track {
            display: flex;
            align-items: center;
            gap: 10px;
            overflow-x: auto;
            scroll-behavior: auto;
            -webkit-overflow-scrolling: touch;
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

</style>
<script>
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
