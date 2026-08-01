(() => {
  "use strict";

  const english = {
    start: "START", stop: "STOP", home: "Home", free: "Free Play", rhythm: "Rhythm Game",
    keyColor: "Key Colors", imageReplace: "Replace Image", reposition: "Reposition",
    imageHelp: "Select any of the 9 keys to replace its image from your phone.",
    subtitle: "Touch the glowing keys to the beat.", score: "SCORE", combo: "COMBO", ready: "READY",
    editTitle: "Edit Character", editHelp: "Drag and zoom the image inside the guide.",
    cameraOn: "📷 Open Camera", cameraOff: "📷 Close Camera", capture: "📸 Take Photo",
    cancel: "Cancel", apply: "Apply", chooseTitle: "Replace Character", chooseHelp: "Choose an image source.",
    chooseCamera: "📷 Take a Photo", chooseFolder: "📂 Photo Library", close: "Close",
    menuOpen: "Open app menu", settingsOpen: "Open feedback settings", appMenu: "App menu",
    keypadEdit: "Edit keypad", feedback: "Key feedback settings", colorSettings: "Key color settings",
    selectNine: "Select one of 9 keys", customColor: "Custom color", rhythmKeys: "3 by 3 rhythm keys",
    rabbitAlt: "FruitRabbit strawberry character", key: "Rhythm key", chooseImage: "Choose image for key",
    chooseColor: "Choose color for key", colorLabel: "Keycap color", soundOn: "Sound on", soundOff: "Sound off",
    cameraError: "Camera could not start. Check camera permission.", perfect: "PERFECT!", great: "GREAT!", miss: "MISS"
  };

  const dictionaries = {
    en: english,
    ko: { start:"시작", stop:"정지", home:"홈", free:"자유 연주", rhythm:"리듬 게임", keyColor:"키캡 컬러", imageReplace:"이미지 교체", reposition:"위치 변경", imageHelp:"9개 키 중 원하는 키를 눌러 핸드폰 사진에서 이미지를 교체하세요.", subtitle:"빛나는 키를 박자에 맞춰 터치하세요.", score:"점수", combo:"콤보", ready:"준비", editTitle:"캐릭터 편집", editHelp:"가이드 안에서 이미지를 드래그하고 확대하세요.", cameraOn:"📷 카메라 켜기", cameraOff:"📷 카메라 끄기", capture:"📸 사진 찍기", cancel:"취소", apply:"적용", chooseTitle:"캐릭터 교체", chooseHelp:"이미지를 가져올 방법을 선택하세요.", chooseCamera:"📷 사진 촬영", chooseFolder:"📂 사진 보관함", close:"닫기", menuOpen:"앱 메뉴 열기", settingsOpen:"피드백 설정 열기", appMenu:"앱 메뉴", keypadEdit:"키패드 편집", feedback:"키 피드백 설정", colorSettings:"키캡 컬러 설정", selectNine:"9개 키캡 선택", customColor:"사용자 색상", rhythmKeys:"3 × 3 리듬 키", rabbitAlt:"FruitRabbit 딸기토끼 캐릭터", key:"리듬 키", chooseImage:"키 이미지 선택", chooseColor:"키 색상 선택", colorLabel:"키캡 색상", soundOn:"오디오 켜짐", soundOff:"오디오 꺼짐", cameraError:"카메라를 시작할 수 없습니다. 권한을 확인해주세요.", perfect:"퍼펙트!", great:"좋아요!", miss:"실패" },
    ja: { start:"スタート", stop:"ストップ", home:"ホーム", free:"フリープレイ", rhythm:"リズムゲーム", keyColor:"キー色", imageReplace:"画像変更", reposition:"位置変更", imageHelp:"9個のキーから画像を変更するキーを選んでください。", subtitle:"光るキーをリズムに合わせてタッチ。", score:"スコア", combo:"コンボ", ready:"準備", editTitle:"キャラクター編集", editHelp:"ガイド内で画像を移動・拡大してください。", cameraOn:"📷 カメラを開く", cameraOff:"📷 カメラを閉じる", capture:"📸 撮影", cancel:"キャンセル", apply:"適用", chooseTitle:"キャラクター変更", chooseHelp:"画像の取得方法を選択してください。", chooseCamera:"📷 写真撮影", chooseFolder:"📂 写真ライブラリ", close:"閉じる" },
    zh: { start:"开始", stop:"停止", home:"主页", free:"自由演奏", rhythm:"节奏游戏", keyColor:"键帽颜色", imageReplace:"更换图片", reposition:"调整位置", imageHelp:"选择九个按键之一，从手机相册更换图片。", subtitle:"跟随节拍触摸发光按键。", score:"分数", combo:"连击", ready:"准备", editTitle:"编辑角色", editHelp:"在框内拖动和缩放图片。", cameraOn:"📷 打开相机", cameraOff:"📷 关闭相机", capture:"📸 拍照", cancel:"取消", apply:"应用", chooseTitle:"更换角色", chooseHelp:"请选择图片来源。", chooseCamera:"📷 拍照", chooseFolder:"📂 相册", close:"关闭" },
    es: { start:"INICIAR", stop:"DETENER", home:"Inicio", free:"Juego libre", rhythm:"Juego rítmico", keyColor:"Colores", imageReplace:"Cambiar imagen", reposition:"Reubicar", imageHelp:"Elige una de las 9 teclas para cambiar su imagen.", subtitle:"Toca las teclas iluminadas al ritmo.", score:"PUNTOS", combo:"COMBO", ready:"LISTO", editTitle:"Editar personaje", editHelp:"Arrastra y amplía la imagen dentro de la guía.", cameraOn:"📷 Abrir cámara", cameraOff:"📷 Cerrar cámara", capture:"📸 Tomar foto", cancel:"Cancelar", apply:"Aplicar", chooseTitle:"Cambiar personaje", chooseHelp:"Elige el origen de la imagen.", chooseCamera:"📷 Tomar foto", chooseFolder:"📂 Fototeca", close:"Cerrar" },
    fr: { start:"DÉMARRER", stop:"ARRÊTER", home:"Accueil", free:"Jeu libre", rhythm:"Jeu de rythme", keyColor:"Couleurs", imageReplace:"Changer l’image", reposition:"Déplacer", imageHelp:"Choisissez une touche parmi les 9 pour remplacer son image.", subtitle:"Touchez les touches lumineuses en rythme.", score:"SCORE", combo:"COMBO", ready:"PRÊT", editTitle:"Modifier le personnage", editHelp:"Déplacez et zoomez l’image dans le guide.", cameraOn:"📷 Ouvrir la caméra", cameraOff:"📷 Fermer la caméra", capture:"📸 Prendre une photo", cancel:"Annuler", apply:"Appliquer", chooseTitle:"Changer le personnage", chooseHelp:"Choisissez une source d’image.", chooseCamera:"📷 Prendre une photo", chooseFolder:"📂 Photothèque", close:"Fermer" },
    de: { start:"START", stop:"STOPP", home:"Startseite", free:"Freies Spiel", rhythm:"Rhythmusspiel", keyColor:"Tastenfarben", imageReplace:"Bild ändern", reposition:"Verschieben", imageHelp:"Wähle eine der 9 Tasten, um ihr Bild zu ersetzen.", subtitle:"Berühre die leuchtenden Tasten im Takt.", score:"PUNKTE", combo:"KOMBO", ready:"BEREIT", editTitle:"Figur bearbeiten", editHelp:"Bild innerhalb der Führung ziehen und zoomen.", cameraOn:"📷 Kamera öffnen", cameraOff:"📷 Kamera schließen", capture:"📸 Foto aufnehmen", cancel:"Abbrechen", apply:"Anwenden", chooseTitle:"Figur ersetzen", chooseHelp:"Bildquelle auswählen.", chooseCamera:"📷 Foto aufnehmen", chooseFolder:"📂 Fotomediathek", close:"Schließen" },
    pt: { start:"INICIAR", stop:"PARAR", home:"Início", free:"Jogo livre", rhythm:"Jogo de ritmo", keyColor:"Cores", imageReplace:"Trocar imagem", reposition:"Reposicionar", imageHelp:"Escolha uma das 9 teclas para trocar sua imagem.", subtitle:"Toque nas teclas iluminadas no ritmo.", score:"PONTOS", combo:"COMBO", ready:"PRONTO", editTitle:"Editar personagem", editHelp:"Arraste e amplie a imagem dentro da guia.", cameraOn:"📷 Abrir câmera", cameraOff:"📷 Fechar câmera", capture:"📸 Tirar foto", cancel:"Cancelar", apply:"Aplicar", chooseTitle:"Trocar personagem", chooseHelp:"Escolha a origem da imagem.", chooseCamera:"📷 Tirar foto", chooseFolder:"📂 Galeria", close:"Fechar" },
    ar: { start:"ابدأ", stop:"إيقاف", home:"الرئيسية", free:"عزف حر", rhythm:"لعبة الإيقاع", keyColor:"ألوان المفاتيح", imageReplace:"تغيير الصورة", reposition:"تغيير الموضع", imageHelp:"اختر مفتاحاً من التسعة لتغيير صورته.", subtitle:"المس المفاتيح المضيئة مع الإيقاع.", score:"النقاط", combo:"التتابع", ready:"جاهز", editTitle:"تحرير الشخصية", editHelp:"اسحب الصورة وكبّرها داخل الدليل.", cameraOn:"📷 فتح الكاميرا", cameraOff:"📷 إغلاق الكاميرا", capture:"📸 التقاط صورة", cancel:"إلغاء", apply:"تطبيق", chooseTitle:"تغيير الشخصية", chooseHelp:"اختر مصدر الصورة.", chooseCamera:"📷 التقاط صورة", chooseFolder:"📂 مكتبة الصور", close:"إغلاق" }
  };

  const requested = (navigator.languages && navigator.languages[0]) || navigator.language || "en";
  const language = requested.toLowerCase().split("-")[0];
  const selected = dictionaries[language] || english;
  const translate = key => selected[key] || english[key] || key;

  document.documentElement.lang = language;
  document.documentElement.dir = language === "ar" ? "rtl" : "ltr";
  document.querySelectorAll("[data-i18n]").forEach(element => {
    element.textContent = translate(element.dataset.i18n);
  });
  document.querySelectorAll("[data-i18n-aria]").forEach(element => {
    element.setAttribute("aria-label", translate(element.dataset.i18nAria));
  });
  document.querySelectorAll("[data-i18n-title]").forEach(element => {
    element.setAttribute("title", translate(element.dataset.i18nTitle));
  });

  window.FRTE_I18N = { language, t: translate };
})();
