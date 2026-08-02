const colors = [
  ["#f3a6bd", "#aa6178"], ["#cbb0e2", "#846a9d"], ["#f1abc0", "#aa6478"],
  ["#d2b6e5", "#8b719f"], ["#f0a4b8", "#a95d72"], ["#d9b9e2", "#92759c"],
  ["#c9e8e7", "#759e9d"], ["#f5d6b0", "#ad8860"], ["#c6d2ee", "#7684a8"]
];
const palette = ["#f3a6bd", "#cbb0e2", "#c9e8e7", "#f5d6b0", "#c6d2ee", "#f4efe1"];

const grid = document.querySelector("#keyGrid");
const scoreView = document.querySelector("#score");
const comboView = document.querySelector("#combo");
const judgementView = document.querySelector("#judgement");
const startButton = document.querySelector("#startButton");
const startLabel = document.querySelector("#startLabel");
const keyDeck = document.querySelector(".key-deck");
const phoneShell = document.querySelector(".phone-shell");
const settingsToggle = document.querySelector("#settingsToggle");
const photoCaptureToggle = document.querySelector("#photoCaptureToggle");
const menuToggle = document.querySelector("#menuToggle");
const gameResetButton = document.querySelector("#gameResetButton");
const freeModeButton = document.querySelector("#freeModeButton");
const rhythmModeButton = document.querySelector("#rhythmModeButton");
const memoryModeButton = document.querySelector("#memoryModeButton");
const memoryActions = document.querySelector("#memoryActions");
const memoryLevelClock = document.querySelector("#memoryLevelClock");
const memoryTotalClock = document.querySelector("#memoryTotalClock");
const memoryStartButton = document.querySelector("#memoryStartButton");
const feedbackPanel = document.querySelector("#feedbackPanel");
const audioToggle = document.querySelector("#audioToggle");
const panelAudioToggle = document.querySelector("#panelAudioToggle");
const ledToggle = document.querySelector("#ledToggle");
const hapticToggle = document.querySelector("#hapticToggle");
const soundEditorTitle = document.querySelector("#soundEditorTitle");
const soundModeSelect = document.querySelector("#soundModeSelect");
const customSoundInput = document.querySelector("#customSoundInput");
const customSoundName = document.querySelector("#customSoundName");
const colorSwatches = document.querySelector("#colorSwatches");
const colorKeyGrid = document.querySelector("#colorKeyGrid");
const customColor = document.querySelector("#customColor");
const applyAllColor = document.querySelector("#applyAllColor");
const colorTargetLabel = document.querySelector("#colorTargetLabel");
const colorCategory = document.querySelector("#colorCategory");
const characterCategory = document.querySelector("#characterCategory");
const layoutCategory = document.querySelector("#layoutCategory");
const colorPanel = document.querySelector("#colorPanel");
const characterPanel = document.querySelector("#characterPanel");
const layoutPanel = document.querySelector("#layoutPanel");
const optionDone = document.querySelector("#optionDone");
const t = key => window.FRTE_I18N?.t(key) || key;
const artRoot = "./assets/art/";
const fixedRabbits = new Map([
  [0, "watermelon.png"],
  [2, "strawberry.png"],
  [8, "kiwi.png"]
]);
const randomRabbits = [
  "banana.png", "berry.png", "blueberry.png", "cherry.png", "coconut.png", "dragon fruit.png",
  "grape.png", "grapefruit.png", "gold kiwi.png", "lemon.png", "lime.png", "mango.png",
  "melon.png", "orange.png", "peach.png", "pear.png", "pineapple.png", "pomegranate.png",
  "yuzu.png", "hallabong.png", "passion fruit.png", "dragon fruit.png", "mangosteen.png"
];
const crossSlots = new Set([1, 3, 4, 5, 7]);
const customSlots = new Set();

let running = false;
let currentMode = "free";
let memorySequence = [];
let memoryInputIndex = 0;
let memoryShowing = false;
let memoryActive = false;
let memoryTimer = 0;
let memoryClockTimer = 0;
let memoryStartTime = 0;
let memoryElapsed = 0;
let memoryLevelElapsed = 0;
let memoryStartCueTimer = 0;

// Image Cropper & Select Option Modal Global State
let activeCropKeyIndex = -1;
let photoTargetKeyIndex = -1;
let activeFileInput = null;
let cropImage = new Image();
let cropX = 140;
let cropY = 140;
let cropScale = 1;
let cropSourceKind = "file";
let isDraggingCrop = false;
let startDragX = 0;
let startDragY = 0;
let webcamStream = null;
let cameraFacingMode = "user";
let cameraZoom = 1;

const cropModal = document.querySelector("#cropModal");
const cropCanvas = document.querySelector("#cropCanvas");
const cropCtx = cropCanvas.getContext("2d");
const cropZoom = document.querySelector("#cropZoom");
const cropCancel = document.querySelector("#cropCancel");
const cropApply = document.querySelector("#cropApply");
const actionSelectModal = document.querySelector("#actionSelectModal");
const btnChooseCamera = document.querySelector("#btnChooseCamera");
const btnChooseFolder = document.querySelector("#btnChooseFolder");
const btnSelectCancel = document.querySelector("#btnSelectCancel");
const webcamVideo = document.querySelector("#webcamVideo");
const btnToggleCamera = document.querySelector("#btnToggleCamera");
const btnSwitchCamera = document.querySelector("#btnSwitchCamera");
const btnCapturePhoto = document.querySelector("#btnCapturePhoto");
let score = 0;
let combo = 0;
let target = -1;
let previousTarget = -1;
let previousTargetExpiresAt = 0;
let beatTimer = 0;
let rhythmStep = 0;
const RHYTHM_BEAT_MS = 700;
const RHYTHM_TOUCH_GRACE_MS = 220;
let audioContext = null;
let soundEnabled = true;
const cameraShutterAudio = new Audio("./assets/camera_shutter.mp3");
cameraShutterAudio.preload = "auto";
let lastPressSoundStyle = -1;
const keySoundModes = Array(9).fill("random");
const customKeySounds = new Map();
const heldHapticTimers = new Map();
let ledEnabled = true;
let hapticEnabled = true;
let selectedKeyIndex = 0;
let selectedColor = colors[0][0];
let moveSource = null;
let layoutDragGhost = null;
const mobileStartScreen = document.querySelector("#mobileStartScreen");
const enterGameButton = document.querySelector("#enterGameButton");

function openImageFileInCropper(file, sourceKind, scaleBoost = 1) {
  if (!file) return;
  const reader = new FileReader();
  reader.onload = event => {
    cropSourceKind = sourceKind;
    cropImage = new Image();
    cropImage.onload = () => {
      if (sourceKind === "camera") stopWebcam();
      cropModal.style.display = "flex";
      cropScale = (240 / Math.min(cropImage.width, cropImage.height)) * scaleBoost;
      cropZoom.min = String(cropScale * 0.4);
      cropZoom.max = String(cropScale * 4.0);
      cropZoom.value = String(cropScale);
      cropX = 140;
      cropY = 140;
      drawCropImage();
    };
    cropImage.src = event.target.result;
  };
  reader.readAsDataURL(file);
}

colors.forEach(([color, dark], index) => {
  const key = document.createElement("div");
  key.className = "key";
  key.style.setProperty("--key", color);
  key.style.setProperty("--dark", dark);
  key.setAttribute("role", "button");
  key.setAttribute("tabindex", "0");
  key.setAttribute("aria-label", `${t("key")} ${index + 1}`);
  if (crossSlots.has(index)) key.classList.add("cross-slot");
  const rabbit = fixedRabbits.get(index) || randomRabbit(index);
  const rabbitSource = artRoot + encodeURIComponent(rabbit).replaceAll("%2F", "/");
  key.innerHTML = `
    <span class="led-module" aria-hidden="true"></span>
    <span class="target-cue" aria-hidden="true"></span>
    <img class="rabbit-art" src="${rabbitSource}" alt="FruitRabbit">
    <span class="character-move-outline" aria-hidden="true"></span>
    <label class="art-upload" title="이 키의 캐릭터 교체">
      <input type="file" accept="image/*" aria-label="${t("chooseImage")} ${index + 1}">
    </label>`;
  const rabbitImage = key.querySelector(".rabbit-art");
  rabbitImage.addEventListener("load", () => {
    window.FRTE3D?.setCharacterImage(index, rabbitImage);
  });
  if (rabbitImage.complete && rabbitImage.naturalWidth > 0) {
    window.FRTE3D?.setCharacterImage(index, rabbitImage);
  }
  const input = key.querySelector("input");
  input.addEventListener("pointerdown", event => event.stopPropagation());
  input.addEventListener("click", event => event.stopPropagation());
  input.addEventListener("change", event => {
    const file = event.target.files?.[0];
    if (!file) return;
    activeCropKeyIndex = index;
    photoTargetKeyIndex = -1;
    openImageFileInCropper(file, "file");
  });
  key.draggable = true;
  key.addEventListener("dragstart", event => {
    if (!grid.classList.contains("layout-mode")) {
      event.preventDefault();
      return;
    }
    moveSource = key;
    key.classList.add("move-source");
    event.dataTransfer.effectAllowed = "move";
  });
  key.addEventListener("dragover", event => {
    if (!moveSource || moveSource === key) return;
    event.preventDefault();
    key.classList.add("drag-over");
  });
  key.addEventListener("dragleave", () => key.classList.remove("drag-over"));
  key.addEventListener("drop", event => {
    event.preventDefault();
    key.classList.remove("drag-over");
    if (moveSource && moveSource !== key) swapKeyAppearance(moveSource, key);
    clearMoveSelection();
  });
  key.addEventListener("dragend", clearMoveSelection);
  key.addEventListener("pointerdown", event => {
    if (grid.classList.contains("character-mode")) {
      activeCropKeyIndex = index;
      activeFileInput = input;
      actionSelectModal.style.display = "flex";
      event.preventDefault();
      return;
    }
    if (grid.classList.contains("layout-mode")) {
      return;
    }
    key.setPointerCapture(event.pointerId);
    selectKey(index);
    press(index, key);
  });
  key.addEventListener("click", () => {
    if (grid.classList.contains("layout-mode")) chooseMoveKey(key);
  });
  key.addEventListener("pointerup", event => releaseKey(index, key, event.pointerId));
  key.addEventListener("pointercancel", event => releaseKey(index, key, event.pointerId));
  key.addEventListener("lostpointercapture", () => {
    key.classList.remove("pressed");
    window.FRTE3D?.setPressed(index, false);
  });
  grid.appendChild(key);
  if (rabbitImage.complete && rabbitImage.naturalWidth > 0) {
    window.FRTE3D?.setCharacterImage(index, rabbitImage);
  }
});

[...grid.children].forEach((key, index) => {
  const preview = document.createElement("button");
  preview.type = "button";
  preview.className = "color-key-preview";
  preview.setAttribute("aria-label", `${t("chooseColor")} ${index + 1}`);
  preview.innerHTML = `<canvas width="180" height="180" aria-hidden="true"></canvas><img class="color-preview-art" alt="">`;
  preview.addEventListener("click", () => selectKey(index));
  preview.addEventListener("dblclick", event => {
    event.preventDefault();
    openColorPickerForPreview(index);
  });
  colorKeyGrid.appendChild(preview);
});
syncColorKeyPreviews();

palette.forEach(color => {
  const swatch = document.createElement("button");
  swatch.className = "color-swatch";
  swatch.style.background = color;
  swatch.setAttribute("aria-label", `${t("colorLabel")} ${color}`);
  swatch.addEventListener("click", () => applyColorToSelected(color));
  colorSwatches.appendChild(swatch);
});

function darkerColor(hex) {
  const value = Number.parseInt(hex.slice(1), 16);
  const red = Math.max(0, ((value >> 16) & 255) - 72);
  const green = Math.max(0, ((value >> 8) & 255) - 72);
  const blue = Math.max(0, (value & 255) - 72);
  return `rgb(${red}, ${green}, ${blue})`;
}

function selectKey(index) {
  selectedKeyIndex = index;
  [...grid.children].forEach((key, keyIndex) => key.classList.toggle("selected", keyIndex === index && colorPanel.classList.contains("open")));
  [...colorKeyGrid.children].forEach((preview, keyIndex) => preview.classList.toggle("selected", keyIndex === index));
  colorTargetLabel.textContent = `${t("keyColor")} ${index + 1}`;
  syncSoundEditor();
}

function syncSoundEditor() {
  if (!soundEditorTitle || !soundModeSelect || !customSoundName) return;
  soundEditorTitle.textContent = `KEY ${selectedKeyIndex + 1} 효과음`;
  soundModeSelect.value = keySoundModes[selectedKeyIndex];
  customSoundName.textContent = customKeySounds.get(selectedKeyIndex)?.name || "등록된 파일 없음";
}

function syncColorKeyPreviews() {
  [...colorKeyGrid.children].forEach((preview, index) => {
    const key = grid.children[index];
    if (!key) return;
    preview.style.setProperty("--preview-color", key.style.getPropertyValue("--key"));
    const previewArt = preview.querySelector(".color-preview-art");
    const keyArt = key.querySelector(".rabbit-art");
    if (previewArt && keyArt) previewArt.src = keyArt.src;
  });
  requestAnimationFrame(() => requestAnimationFrame(renderColorKeyPreviews));
}

function renderColorKeyPreviews() {
  const source = document.querySelector("#key3DCanvas");
  if (!source || !source.width || !source.height) return;
  const sourceRect = source.getBoundingClientRect();
  if (!sourceRect.width || !sourceRect.height) return;
  const scaleX = source.width / sourceRect.width;
  const scaleY = source.height / sourceRect.height;
  [...colorKeyGrid.children].forEach((preview, index) => {
    const key = grid.children[index];
    const target = preview.querySelector("canvas");
    if (!key || !target) return;
    const keyRect = key.getBoundingClientRect();
    const padX = keyRect.width * 0.12;
    const padY = keyRect.height * 0.12;
    const sx = Math.max(0, (keyRect.left - sourceRect.left - padX) * scaleX);
    const sy = Math.max(0, (keyRect.top - sourceRect.top - padY) * scaleY);
    const sw = Math.min(source.width - sx, (keyRect.width + padX * 2) * scaleX);
    const sh = Math.min(source.height - sy, (keyRect.height + padY * 2) * scaleY);
    const context = target.getContext("2d");
    context.clearRect(0, 0, target.width, target.height);
    context.drawImage(source, sx, sy, sw, sh, 0, 0, target.width, target.height);
  });
}

function openColorPickerForPreview(index) {
  selectKey(index);
  colorPanel.classList.add("editor-open");
  try {
    if (typeof customColor.showPicker === "function") {
      customColor.showPicker();
      return;
    }
  } catch (_error) {
    // Fall back to a regular input click when showPicker is unavailable.
  }
  customColor.click();
}

function applyKeyColor(key, color) {
  key.style.setProperty("--key", color);
  key.style.setProperty("--dark", darkerColor(color));
  window.FRTE3D?.setColor([...grid.children].indexOf(key), color);
  syncColorKeyPreviews();
}

function applyColorToSelected(color) {
  selectedColor = color;
  applyKeyColor(grid.children[selectedKeyIndex], color);
  customColor.value = color;
}

customColor.addEventListener("input", event => applyColorToSelected(event.target.value));
applyAllColor.addEventListener("click", () => {
  [...grid.children].forEach(key => applyKeyColor(key, selectedColor));
});

function chooseMoveKey(key) {
  if (!moveSource) {
    moveSource = key;
    key.classList.add("move-source");
    return;
  }
  if (moveSource !== key) swapKeyAppearance(moveSource, key);
  clearMoveSelection();
}

function swapKeyAppearance(first, second) {
  const firstImage = first.querySelector(".rabbit-art");
  const secondImage = second.querySelector(".rabbit-art");
  const firstSource = firstImage.src;
  firstImage.src = secondImage.src;
  secondImage.src = firstSource;

  const firstColor = first.style.getPropertyValue("--key");
  const firstDark = first.style.getPropertyValue("--dark");
  first.style.setProperty("--key", second.style.getPropertyValue("--key"));
  first.style.setProperty("--dark", second.style.getPropertyValue("--dark"));
  second.style.setProperty("--key", firstColor);
  second.style.setProperty("--dark", firstDark);

  const firstCustom = first.classList.contains("custom-art");
  first.classList.toggle("custom-art", second.classList.contains("custom-art"));
  second.classList.toggle("custom-art", firstCustom);

  const firstIndex = [...grid.children].indexOf(first);
  const secondIndex = [...grid.children].indexOf(second);
  customSlots.delete(firstIndex);
  customSlots.delete(secondIndex);
  if (first.classList.contains("custom-art")) customSlots.add(firstIndex);
  if (second.classList.contains("custom-art")) customSlots.add(secondIndex);
  window.FRTE3D?.setCharacter(firstIndex, firstImage.src);
  window.FRTE3D?.setCharacter(secondIndex, secondImage.src);
  window.FRTE3D?.setColor(firstIndex, first.style.getPropertyValue("--key"));
  window.FRTE3D?.setColor(secondIndex, second.style.getPropertyValue("--key"));
  syncColorKeyPreviews();
}

function clearMoveSelection() {
  [...grid.children].forEach(key => key.classList.remove("move-source", "drag-over"));
  moveSource = null;
}

function beginLayoutDrag(key, event) {
  endLayoutDrag();
  layoutDragGhost = key.querySelector(".rabbit-art").cloneNode();
  layoutDragGhost.className = "layout-drag-ghost";
  document.body.appendChild(layoutDragGhost);
  updateLayoutDrag(event);
}

function updateLayoutDrag(event) {
  if (!layoutDragGhost) return;
  layoutDragGhost.style.left = event.clientX + "px";
  layoutDragGhost.style.top = event.clientY + "px";
}

function endLayoutDrag() {
  if (!layoutDragGhost) return;
  layoutDragGhost.remove();
  layoutDragGhost = null;
}

function openCategory(button, panel, modeClass) {
  const shouldOpen = !button.classList.contains("active");
  if (shouldOpen && running) {
    stopRhythmPlayback();
    setMode("free");
  }
  [colorCategory, characterCategory, layoutCategory].forEach(item => item.classList.remove("active"));
  [colorPanel, characterPanel, layoutPanel].forEach(item => item.classList.remove("open"));
  colorPanel.classList.remove("editor-open");
  grid.classList.remove("option-mode", "character-mode", "layout-mode");
  keyDeck.classList.remove("option-active");
  clearMoveSelection();
  if (!shouldOpen) return;
  button.classList.add("active");
  panel.classList.add("open");
  grid.classList.add("option-mode");
  keyDeck.classList.add("option-active");
  if (modeClass) grid.classList.add(modeClass);
  selectKey(selectedKeyIndex);
}

function closeOptions() {
  [colorCategory, characterCategory, layoutCategory].forEach(item => item.classList.remove("active"));
  [colorPanel, characterPanel, layoutPanel].forEach(item => item.classList.remove("open"));
  grid.classList.remove("option-mode", "character-mode", "layout-mode");
  keyDeck.classList.remove("option-active");
  clearMoveSelection();
}

optionDone.addEventListener("click", () => {
  closeOptions();
  requestAppFullscreen();
});

colorCategory.addEventListener("click", () => openCategory(colorCategory, colorPanel, ""));
characterCategory.addEventListener("click", () => openCategory(characterCategory, characterPanel, "character-mode"));
layoutCategory.addEventListener("click", () => openCategory(layoutCategory, layoutPanel, "layout-mode"));

function releaseKey(index, key, pointerId) {
  stopHeldHaptic(index);
  key.classList.remove("pressed");
  window.FRTE3D?.setPressed(index, false);
  playKeySound(false, index);
  triggerHaptic([3, 5, 7]);
  if (Number.isInteger(pointerId) && key.hasPointerCapture(pointerId)) {
    key.releasePointerCapture(pointerId);
  }
}

function releaseAllPressedKeys(pointerId) {
  [...grid.children].forEach((key, index) => {
    if (key.classList.contains("pressed")) {
      releaseKey(index, key, pointerId);
    } else {
      window.FRTE3D?.setPressed(index, false);
    }
  });
  stopAllHeldHaptics();
}

window.addEventListener("pointercancel", event => releaseAllPressedKeys(event.pointerId));
window.addEventListener("blur", () => {
  releaseAllPressedKeys();
  if (running) {
    stopRhythmPlayback();
    setMode("free");
  }
});
document.addEventListener("visibilitychange", () => {
  if (document.hidden) {
    releaseAllPressedKeys();
    if (running) {
      stopRhythmPlayback();
      setMode("free");
    }
  }
});

function playKeySound(isPress, keyIndex = 0, useSemitone = false) {
  if (!soundEnabled) return;
  const soundMode = keySoundModes[keyIndex] || "random";
  if (isPress && soundMode === "custom" && playCustomKeySound(keyIndex)) return;
  const AudioContextType = window.AudioContext || window.webkitAudioContext;
  if (!AudioContextType) return;

  audioContext ||= new AudioContextType();
  if (audioContext.state === "suspended") audioContext.resume();

  const now = audioContext.currentTime;
  const scale = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88, 523.25, 587.33];
  const semitoneRatio = useSemitone ? Math.pow(2, 1 / 12) : 1;
  const baseFrequency = scale[Math.max(0, Math.min(scale.length - 1, keyIndex))] * semitoneRatio;

  if (!isPress) {
    playSynthVoice(baseFrequency * 0.72, "triangle", now, 0.052, 0.07, 1250);
    playSynthVoice(baseFrequency * 1.5, "sine", now + 0.018, 0.032, 0.052, 2600);
    playSynthVoice(620 + keyIndex * 18, "square", now + 0.026, 0.022, 0.028, 1350);
    return;
  }

  let style = soundMode === "fart" ? 4 : soundMode === "default" ? 0 : Math.floor(Math.random() * 5);
  if (soundMode === "random" && style === lastPressSoundStyle) style = (style + 1 + Math.floor(Math.random() * 4)) % 5;
  lastPressSoundStyle = style;
  const pitchVariation = 1 + (Math.random() - 0.5) * 0.012;
  const frequency = baseFrequency * pitchVariation;

  if (style === 4) {
    playFartSound(now, keyIndex);
    return;
  }

  playSynthVoice(980 + Math.random() * 180, "square", now, 0.025, 0.018, 1650);

  if (style === 0) {
    playSynthVoice(frequency, "triangle", now, 0.16, 0.14, 1900);
    playSynthVoice(frequency * 2, "sine", now, 0.055, 0.07, 3200);
  } else if (style === 1) {
    playSynthVoice(frequency, "sine", now, 0.12, 0.32, 4200);
    playSynthVoice(frequency * 2.01, "sine", now + 0.012, 0.05, 0.23, 5200);
  } else if (style === 2) {
    playSynthVoice(frequency, "square", now, 0.075, 0.075, 1450);
    playSynthVoice(frequency * 1.5, "triangle", now + 0.018, 0.065, 0.09, 2300);
  } else {
    playSynthVoice(frequency, "sawtooth", now, 0.07, 0.095, 1100);
    playSynthVoice(frequency * 2, "triangle", now + 0.028, 0.055, 0.075, 2600);
    playSynthVoice(frequency * 3, "sine", now + 0.052, 0.035, 0.06, 3900);
  }

  playSynthVoice(760 + Math.random() * 220, "square", now, 0.035, 0.035, 1800);
  playSynthVoice(74 + keyIndex * 2, "triangle", now + 0.032, 0.115, 0.055, 520);
  playSynthVoice(frequency * 0.5, "sine", now + 0.038, 0.055, 0.075, 760);
}

function playSynthVoice(frequency, type, startTime, volume, duration, filterFrequency) {
  const oscillator = audioContext.createOscillator();
  const filter = audioContext.createBiquadFilter();
  const gain = audioContext.createGain();
  oscillator.type = type;
  oscillator.frequency.setValueAtTime(frequency, startTime);
  filter.type = "lowpass";
  filter.frequency.setValueAtTime(filterFrequency, startTime);
  gain.gain.setValueAtTime(0.0001, startTime);
  gain.gain.exponentialRampToValueAtTime(volume, startTime + 0.004);
  gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);
  oscillator.connect(filter);
  filter.connect(gain);
  gain.connect(audioContext.destination);
  oscillator.start(startTime);
  oscillator.stop(startTime + duration + 0.01);
}

function playRhythmBacking(step) {
  if (!soundEnabled) return;
  const AudioContextType = window.AudioContext || window.webkitAudioContext;
  if (!AudioContextType) return;
  audioContext ||= new AudioContextType();
  if (audioContext.state === "suspended") audioContext.resume();

  const now = audioContext.currentTime;
  const bassLine = [130.81, 130.81, 164.81, 196.00, 146.83, 146.83, 174.61, 220.00];
  const melody = [523.25, 659.25, 783.99, 659.25, 587.33, 698.46, 880.00, 698.46];
  const chordRoots = [261.63, 329.63, 293.66, 349.23];
  const bass = bassLine[step % bassLine.length];
  const lead = melody[step % melody.length];
  const chord = chordRoots[Math.floor(step / 2) % chordRoots.length];

  playSynthVoice(bass, "triangle", now, 0.105, 0.30, 720);
  playSynthVoice(lead, "square", now + 0.025, 0.032, 0.13, 2600);
  playSynthVoice(lead * 2, "sine", now + 0.035, 0.018, 0.11, 4300);
  if (step % 2 === 0) {
    playSynthVoice(chord, "sine", now, 0.034, 0.38, 2100);
    playSynthVoice(chord * 1.25, "sine", now + 0.008, 0.026, 0.36, 2300);
    playSynthVoice(chord * 1.5, "sine", now + 0.014, 0.023, 0.34, 2500);
  }
  playSynthVoice(step % 4 === 0 ? 72 : 1180, step % 4 === 0 ? "sine" : "square", now, step % 4 === 0 ? 0.15 : 0.018, step % 4 === 0 ? 0.16 : 0.045, step % 4 === 0 ? 380 : 3400);
}

function playFartSound(startTime, keyIndex) {
  const duration = 0.22 + Math.random() * 0.16;
  const oscillator = audioContext.createOscillator();
  const oscillatorFilter = audioContext.createBiquadFilter();
  const oscillatorGain = audioContext.createGain();
  const noiseBuffer = audioContext.createBuffer(1, Math.ceil(audioContext.sampleRate * duration), audioContext.sampleRate);
  const noiseData = noiseBuffer.getChannelData(0);
  const noise = audioContext.createBufferSource();
  const noiseFilter = audioContext.createBiquadFilter();
  const noiseGain = audioContext.createGain();
  const startFrequency = 105 + keyIndex * 3 + Math.random() * 24;

  for (let index = 0; index < noiseData.length; index += 1) {
    const envelope = 1 - index / noiseData.length;
    noiseData[index] = (Math.random() * 2 - 1) * envelope;
  }

  oscillator.type = "sawtooth";
  oscillator.frequency.setValueAtTime(startFrequency, startTime);
  oscillator.frequency.exponentialRampToValueAtTime(42 + Math.random() * 12, startTime + duration);
  oscillatorFilter.type = "lowpass";
  oscillatorFilter.frequency.setValueAtTime(430, startTime);
  oscillatorFilter.frequency.exponentialRampToValueAtTime(150, startTime + duration);
  oscillatorGain.gain.setValueAtTime(0.0001, startTime);
  oscillatorGain.gain.exponentialRampToValueAtTime(0.16, startTime + 0.012);
  oscillatorGain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

  noise.buffer = noiseBuffer;
  noiseFilter.type = "bandpass";
  noiseFilter.frequency.setValueAtTime(135 + Math.random() * 45, startTime);
  noiseFilter.Q.setValueAtTime(0.7, startTime);
  noiseGain.gain.setValueAtTime(0.0001, startTime);
  noiseGain.gain.exponentialRampToValueAtTime(0.11, startTime + 0.01);
  noiseGain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

  oscillator.connect(oscillatorFilter);
  oscillatorFilter.connect(oscillatorGain);
  oscillatorGain.connect(audioContext.destination);
  noise.connect(noiseFilter);
  noiseFilter.connect(noiseGain);
  noiseGain.connect(audioContext.destination);
  oscillator.start(startTime);
  oscillator.stop(startTime + duration + 0.01);
  noise.start(startTime);
  noise.stop(startTime + duration + 0.01);
}

function playCustomKeySound(keyIndex) {
  const registeredSound = customKeySounds.get(keyIndex);
  if (!registeredSound) return false;
  const audio = new Audio(registeredSound.url);
  audio.volume = 0.78;
  audio.play().catch(() => {});
  return true;
}

function triggerHaptic(duration) {
  if (hapticEnabled && "vibrate" in navigator) navigator.vibrate(duration);
}

function startHeldHaptic(keyIndex) {
  if (!hapticEnabled || !("vibrate" in navigator) || heldHapticTimers.has(keyIndex)) return;
  navigator.vibrate(44);
  heldHapticTimers.set(keyIndex, setInterval(() => {
    if (hapticEnabled) navigator.vibrate(44);
  }, 66));
}

function stopHeldHaptic(keyIndex) {
  const timer = heldHapticTimers.get(keyIndex);
  if (timer) clearInterval(timer);
  heldHapticTimers.delete(keyIndex);
  if (!heldHapticTimers.size && "vibrate" in navigator) navigator.vibrate(0);
}

function stopAllHeldHaptics() {
  heldHapticTimers.forEach(timer => clearInterval(timer));
  heldHapticTimers.clear();
  if ("vibrate" in navigator) navigator.vibrate(0);
}

function setFeature(button, enabled) {
  button.classList.toggle("active", enabled);
  button.setAttribute("aria-pressed", String(enabled));
}

function setSoundEnabled(enabled) {
  soundEnabled = enabled;
  setFeature(audioToggle, enabled);
  setFeature(panelAudioToggle, enabled);
  audioToggle.setAttribute("aria-label", enabled ? t("soundOn") : t("soundOff"));
}

settingsToggle.addEventListener("click", () => {
  if (running) {
    stopRhythmPlayback();
    setMode("free");
  }
  const isOpen = feedbackPanel.classList.toggle("open");
  settingsToggle.setAttribute("aria-expanded", String(isOpen));
  selectKey(selectedKeyIndex);
  requestAppFullscreen();
});

document.addEventListener("pointerdown", event => {
  if (!feedbackPanel.classList.contains("open")) return;
  if (settingsToggle.contains(event.target) || feedbackPanel.contains(event.target)) return;
  feedbackPanel.classList.remove("open");
  settingsToggle.setAttribute("aria-expanded", "false");
});

document.addEventListener("pointerdown", () => {
  if (mobileStartScreen.classList.contains("hidden")) requestAppFullscreen();
}, { capture: true });

menuToggle?.addEventListener("click", () => {
  feedbackPanel.classList.remove("open");
  settingsToggle.setAttribute("aria-expanded", "false");
  stopMemoryGame();
  if (running) startButton.click();
  setMode("free");
  mobileStartScreen.classList.remove("hidden");
});

gameResetButton?.addEventListener("click", () => {
  releaseAllPressedKeys();
  if (currentMode === "memory") {
    stopMemoryGame();
    setMode("memory");
    prepareMemoryGame();
    return;
  }
  if (running) startButton.click();
  score = 0;
  combo = 0;
  renderScore();
  judgementView.textContent = t("ready");
  judgementView.style.color = "#ffd765";
});

function setMode(mode) {
  const isRhythm = mode === "rhythm";
  const isMemory = mode === "memory";
  if (!isRhythm && running) stopRhythmPlayback();
  currentMode = mode;
  phoneShell.classList.toggle("memory-view", isMemory);
  freeModeButton.classList.toggle("active", mode === "free");
  rhythmModeButton.classList.toggle("active", isRhythm);
  memoryModeButton.classList.toggle("active", isMemory);
  freeModeButton.setAttribute("aria-pressed", String(mode === "free"));
  rhythmModeButton.setAttribute("aria-pressed", String(isRhythm));
  memoryModeButton.setAttribute("aria-pressed", String(isMemory));
  memoryActions.hidden = !isMemory;
  document.querySelector(".rhythm-only-message").hidden = !isRhythm;
}

function stopRhythmPlayback() {
  running = false;
  clearTimeout(beatTimer);
  beatTimer = 0;
  rhythmStep = 0;
  clearTarget();
  startLabel.textContent = t("start");
  judgementView.textContent = t("ready");
  if (audioContext?.state === "running") audioContext.suspend().catch(() => {});
}

freeModeButton.addEventListener("click", () => {
  stopMemoryGame();
  if (running) startButton.click();
  setMode("free");
});

rhythmModeButton.addEventListener("click", () => {
  stopMemoryGame();
  if (!running) startButton.click();
  setMode("rhythm");
});

memoryModeButton.addEventListener("click", () => {
  if (running) startButton.click();
  stopMemoryGame();
  setMode("memory");
  prepareMemoryGame();
});

memoryStartButton.addEventListener("click", startMemoryGame);

function prepareMemoryGame() {
  score = 0;
  combo = 0;
  renderScore();
  memoryLevelClock.textContent = "00:00.00";
  memoryTotalClock.textContent = "00:00.00";
  memoryStartButton.hidden = false;
  memoryStartButton.disabled = false;
  memoryStartButton.textContent = "▶ START";
  judgementView.style.color = "#ffe36e";
  judgementView.textContent = "MEMORY READY";
}

function stopMemoryGame() {
  clearTimeout(memoryTimer);
  clearTimeout(memoryStartCueTimer);
  clearInterval(memoryClockTimer);
  memoryActive = false;
  memoryShowing = false;
  memorySequence = [];
  memoryInputIndex = 0;
  memoryStartTime = 0;
  memoryElapsed = 0;
  memoryLevelElapsed = 0;
  clearTarget();
}

function startMemoryGame() {
  score = 0;
  combo = 0;
  memorySequence = [];
  memoryActive = true;
  memoryElapsed = 0;
  memoryLevelElapsed = 0;
  memoryStartTime = 0;
  memoryLevelClock.textContent = "00:00.00";
  memoryTotalClock.textContent = "00:00.00";
  memoryStartButton.hidden = true;
  memoryStartButton.disabled = false;
  renderScore();
  judgementView.style.color = "#ffe36e";
  judgementView.textContent = "MEMORY READY";
  memoryTimer = setTimeout(beginMemoryLevel, 650);
}

function updateMemoryClock() {
  const activeElapsed = memoryStartTime > 0 ? performance.now() - memoryStartTime : 0;
  memoryLevelClock.textContent = formatMemoryTime(memoryLevelElapsed + activeElapsed);
  memoryTotalClock.textContent = formatMemoryTime(memoryElapsed + activeElapsed);
}

function formatMemoryTime(value) {
  const elapsed = Math.max(0, value);
  const minutes = Math.floor(elapsed / 60000);
  const seconds = Math.floor(elapsed / 1000) % 60;
  const centiseconds = Math.floor(elapsed / 10) % 100;
  return `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}.${String(centiseconds).padStart(2, "0")}`;
}

function startMemoryTurnTimer() {
  clearInterval(memoryClockTimer);
  memoryStartTime = performance.now();
  memoryClockTimer = setInterval(updateMemoryClock, 31);
  memoryStartButton.textContent = "▶ START!";
  memoryStartButton.disabled = true;
  memoryStartButton.hidden = false;
  clearTimeout(memoryStartCueTimer);
  memoryStartCueTimer = setTimeout(() => {
    if (memoryActive && !memoryShowing) memoryStartButton.hidden = true;
  }, 650);
}

function pauseMemoryTurnTimer() {
  if (memoryStartTime > 0) {
    const turnElapsed = performance.now() - memoryStartTime;
    memoryElapsed += turnElapsed;
    memoryLevelElapsed += turnElapsed;
  }
  memoryStartTime = 0;
  clearInterval(memoryClockTimer);
  updateMemoryClock();
}

function beginMemoryLevel() {
  if (!memoryActive || currentMode !== "memory") return;
  memoryLevelElapsed = 0;
  memoryLevelClock.textContent = "00:00.00";
  memorySequence.push(Math.floor(Math.random() * 9));
  memoryInputIndex = 0;
  memoryShowing = true;
  combo = memorySequence.length;
  renderScore();
  judgementView.textContent = `LEVEL ${memorySequence.length} · WATCH`;
  judgementView.style.color = "#ffe36e";
  playMemoryStep(0);
}

function playMemoryStep(stepIndex) {
  if (!memoryActive || currentMode !== "memory") return;
  if (stepIndex >= memorySequence.length) {
    memoryShowing = false;
    judgementView.textContent = `LEVEL ${memorySequence.length} · YOUR TURN`;
    judgementView.style.color = "#67f4ff";
    startMemoryTurnTimer();
    return;
  }
  const keyIndex = memorySequence[stepIndex];
  const showDuration = Math.max(260, 520 - memorySequence.length * 24);
  clearTarget();
  target = keyIndex;
  grid.children[keyIndex].classList.add("target");
  window.FRTE3D?.setLedTarget(keyIndex, true);
  playKeySound(true, keyIndex, false);
  memoryTimer = setTimeout(() => {
    clearTarget();
    memoryTimer = setTimeout(() => playMemoryStep(stepIndex + 1), 150);
  }, showDuration);
}

function handleMemoryInput(index) {
  if (memoryShowing) return;
  if (index !== memorySequence[memoryInputIndex]) {
    pauseMemoryTurnTimer();
    memoryInputIndex = 0;
    judgementView.textContent = "MISS · WATCH AGAIN";
    judgementView.style.color = "#ff5b8f";
    triggerHaptic([35, 30, 70]);
    memoryShowing = true;
    memoryTimer = setTimeout(() => playMemoryStep(0), 750);
    return;
  }
  memoryInputIndex += 1;
  score += 100 * memorySequence.length;
  judgementView.textContent = `${memoryInputIndex} / ${memorySequence.length}`;
  judgementView.style.color = "#67f4ff";
  renderScore();
  if (memoryInputIndex < memorySequence.length) return;
  pauseMemoryTurnTimer();
  if (memorySequence.length >= 9) {
    memoryActive = false;
    updateMemoryClock();
    memoryStartButton.hidden = false;
    memoryStartButton.disabled = false;
    memoryStartButton.textContent = "↻ AGAIN";
    judgementView.textContent = "MEMORY COMPLETE!";
    judgementView.style.color = "#ffe36e";
    triggerHaptic([20, 30, 20, 30, 80]);
    return;
  }
  memoryShowing = true;
  judgementView.textContent = `LEVEL ${memorySequence.length} CLEAR!`;
  judgementView.style.color = "#ffe36e";
  memoryTimer = setTimeout(beginMemoryLevel, 850);
}

audioToggle.addEventListener("click", () => setSoundEnabled(!soundEnabled));
panelAudioToggle.addEventListener("click", () => setSoundEnabled(!soundEnabled));
soundModeSelect?.addEventListener("change", event => {
  keySoundModes[selectedKeyIndex] = event.target.value;
  syncSoundEditor();
});
customSoundInput?.addEventListener("change", event => {
  const file = event.target.files?.[0];
  if (!file) return;
  const previousSound = customKeySounds.get(selectedKeyIndex);
  if (previousSound) URL.revokeObjectURL(previousSound.url);
  customKeySounds.set(selectedKeyIndex, { name: file.name, url: URL.createObjectURL(file) });
  keySoundModes[selectedKeyIndex] = "custom";
  event.target.value = "";
  syncSoundEditor();
});
ledToggle.addEventListener("click", () => {
  ledEnabled = !ledEnabled;
  setFeature(ledToggle, ledEnabled);
  keyDeck.classList.toggle("led-off", !ledEnabled);
  window.FRTE3D?.setLedEnabled(ledEnabled);
});
hapticToggle.addEventListener("click", () => {
  hapticEnabled = !hapticEnabled;
  setFeature(hapticToggle, hapticEnabled);
  if (!hapticEnabled) stopAllHeldHaptics();
  if (hapticEnabled) triggerHaptic(18);
});

function randomRabbit(excludeIndex = -1) {
  const current = [...grid.querySelectorAll(".rabbit-art")].map(image => decodeURIComponent(image.src.split("/").pop()));
  const candidates = randomRabbits.filter(name => !current.includes(name));
  const source = candidates.length ? candidates : randomRabbits;
  return source[Math.floor(Math.random() * source.length)];
}

function rotateOneRabbit() {
  const replaceable = [...Array(9).keys()].filter(index => !fixedRabbits.has(index) && !customSlots.has(index));
  if (!replaceable.length) return;
  const index = replaceable[Math.floor(Math.random() * replaceable.length)];
  const key = grid.children[index];
  key.classList.add("swapping");
  setTimeout(() => {
    const filename = randomRabbit(index);
    key.querySelector(".rabbit-art").src = artRoot + encodeURIComponent(filename).replaceAll("%2F", "/");
    window.FRTE3D?.setCharacter(index, key.querySelector(".rabbit-art").src);
    key.classList.remove("swapping");
  }, 170);
}

function requestAppFullscreen() {
  const isMobileTouch = window.matchMedia("(pointer: coarse)").matches
    && Math.min(window.screen.width, window.screen.height) <= 820;
  if (!isMobileTouch) return;
  const target = document.documentElement;
  const request = target.requestFullscreen || target.webkitRequestFullscreen;
  if (request && !document.fullscreenElement && !document.webkitFullscreenElement) {
    Promise.resolve(request.call(target)).catch(() => {});
  }
  window.scrollTo(0, 1);
}

enterGameButton?.addEventListener("click", () => {
  requestAppFullscreen();
  mobileStartScreen.classList.add("hidden");
  setMode("free");
});

function press(index, key) {
  key.classList.add("pressed");
  window.FRTE3D?.setPressed(index, true);
  const simultaneousPress = grid.querySelectorAll(".key.pressed").length > 1;
  playKeySound(true, index, simultaneousPress);
  startHeldHaptic(index);
  if (currentMode === "memory" && memoryActive) {
    handleMemoryInput(index);
    return;
  }
  if (!running) return;
  const hitCurrentTarget = index === target;
  const hitRecentTarget = index === previousTarget && performance.now() <= previousTargetExpiresAt;
  if (hitCurrentTarget || hitRecentTarget) {
    score += 100;
    combo += 1;
    judgementView.textContent = combo > 5 ? t("perfect") : t("great");
    judgementView.style.color = "#67f4ff";
    if (hitCurrentTarget) clearTarget();
    previousTarget = -1;
    previousTargetExpiresAt = 0;
  } else {
    combo = 0;
    judgementView.textContent = t("miss");
    judgementView.style.color = "#ff5b8f";
  }
  renderScore();
}

function renderScore() {
  scoreView.textContent = String(score).padStart(6, "0");
  comboView.textContent = combo;
}

function clearTarget() {
  if (target >= 0) {
    grid.children[target].classList.remove("target");
    window.FRTE3D?.setLedTarget(target, false);
  }
  target = -1;
}

function scheduleBeat(delay = RHYTHM_BEAT_MS) {
  clearTimeout(beatTimer);
  beatTimer = setTimeout(function rhythmTick() {
    if (!running) return;
    if (target >= 0) {
      previousTarget = target;
      previousTargetExpiresAt = performance.now() + RHYTHM_TOUCH_GRACE_MS;
      combo = 0;
      judgementView.textContent = t("miss");
      judgementView.style.color = "#ff5b8f";
      renderScore();
    }
    clearTarget();
    playRhythmBacking(rhythmStep);
    target = Math.floor(Math.random() * 9);
    grid.children[target].classList.add("target");
    window.FRTE3D?.setLedTarget(target, true);
    rhythmStep = (rhythmStep + 1) % 32;
    beatTimer = setTimeout(rhythmTick, RHYTHM_BEAT_MS);
  }, delay);
}

startButton.addEventListener("click", () => {
  running = !running;
  if (running) {
    setMode("rhythm");
    score = 0;
    combo = 0;
    renderScore();
    startLabel.textContent = t("stop");
    judgementView.textContent = `${t("ready")}!`;
    judgementView.style.color = "#ffd765";
    rhythmStep = 0;
    scheduleBeat(320);
  } else {
    stopRhythmPlayback();
    setMode("free");
  }
});

// Image Cropper Logic
cropCanvas.width = 280;
cropCanvas.height = 280;

function drawCropImage() {
  cropCtx.clearRect(0, 0, 280, 280);
  if (!cropImage.src) return;
  const w = cropImage.width * cropScale;
  const h = cropImage.height * cropScale;
  cropCtx.drawImage(cropImage, cropX - w / 2, cropY - h / 2, w, h);
}

function getEventPos(e) {
  const rect = cropCanvas.getBoundingClientRect();
  const clientX = e.touches ? e.touches[0].clientX : e.clientX;
  const clientY = e.touches ? e.touches[0].clientY : e.clientY;
  return {
    x: clientX - rect.left,
    y: clientY - rect.top
  };
}

function startDrag(e) {
  isDraggingCrop = true;
  const pos = getEventPos(e);
  startDragX = pos.x - cropX;
  startDragY = pos.y - cropY;
  e.preventDefault();
}

function drag(e) {
  if (!isDraggingCrop) return;
  const pos = getEventPos(e);
  cropX = pos.x - startDragX;
  cropY = pos.y - startDragY;
  drawCropImage();
  e.preventDefault();
}

function endDrag() {
  isDraggingCrop = false;
}

cropCanvas.addEventListener("mousedown", startDrag);
cropCanvas.addEventListener("mousemove", drag);
window.addEventListener("mouseup", endDrag);

cropCanvas.addEventListener("touchstart", startDrag, { passive: false });
cropCanvas.addEventListener("touchmove", drag, { passive: false });
window.addEventListener("touchend", endDrag);

cropZoom.addEventListener("input", e => {
  const zoomValue = parseFloat(e.target.value);
  if (webcamStream) {
    cameraZoom = zoomValue;
    webcamVideo.style.transform = `scale(${cameraZoom})`;
    return;
  }
  cropScale = zoomValue;
  drawCropImage();
});

// Stop camera tracks
function stopWebcam() {
  if (webcamStream) {
    webcamStream.getTracks().forEach(track => track.stop());
    webcamStream = null;
  }
  webcamVideo.srcObject = null;
  webcamVideo.style.display = "none";
  webcamVideo.style.transform = "scale(1)";
  btnToggleCamera.textContent = t("cameraOn");
  btnSwitchCamera.style.display = "none";
  btnCapturePhoto.style.display = "none";
}

async function startWebcam() {
  try {
    const constraints = {
      video: { facingMode: { ideal: cameraFacingMode }, width: { ideal: 1280 }, height: { ideal: 1280 } }
    };
    webcamStream = await navigator.mediaDevices.getUserMedia(constraints);
    webcamVideo.srcObject = webcamStream;
    webcamVideo.style.display = "block";
    cameraZoom = 1;
    webcamVideo.style.transformOrigin = "center";
    webcamVideo.style.transform = "scale(1)";
    cropZoom.min = "0.7";
    cropZoom.max = "3";
    cropZoom.step = "0.05";
    cropZoom.value = "1";
    btnToggleCamera.textContent = t("cameraOff");
    btnSwitchCamera.style.display = "block";
    btnCapturePhoto.style.display = "block";
  } catch (err) {
    alert(t("cameraError"));
    console.error(err);
  }
}

btnToggleCamera.addEventListener("click", async () => {
  if (webcamStream) {
    stopWebcam();
    return;
  }
  await startWebcam();
});

btnSwitchCamera.addEventListener("click", async () => {
  cameraFacingMode = cameraFacingMode === "user" ? "environment" : "user";
  stopWebcam();
  await startWebcam();
});

// Capture Photo click
btnCapturePhoto.addEventListener("click", () => {
  if (!webcamStream || webcamVideo.readyState < 2) return;
  if (activeCropKeyIndex < 0) activeCropKeyIndex = selectedKeyIndex;
  photoTargetKeyIndex = activeCropKeyIndex;

  if (soundEnabled) {
    cameraShutterAudio.currentTime = 0;
    cameraShutterAudio.play().catch(() => {});
  }
  
  // Draw the current video frame into a temp canvas
  const tempCanvas = document.createElement("canvas");
  tempCanvas.width = webcamVideo.videoWidth;
  tempCanvas.height = webcamVideo.videoHeight;
  const tempCtx = tempCanvas.getContext("2d");
  
  if (cameraFacingMode === "user") {
    tempCtx.translate(tempCanvas.width, 0);
    tempCtx.scale(-1, 1);
  }
  tempCtx.drawImage(webcamVideo, 0, 0, tempCanvas.width, tempCanvas.height);
  
  tempCanvas.toBlob(blob => {
    if (!blob) return;
    openImageFileInCropper(blob, "camera", 1.65 * cameraZoom);
  }, "image/png");
});

cropCancel.addEventListener("click", () => {
  stopWebcam();
  photoTargetKeyIndex = -1;
  cropModal.classList.remove("native-capture");
  cropModal.style.display = "none";
  requestAppFullscreen();
});

function removeConnectedWhiteBackground(context, width, height) {
  const imageData = context.getImageData(0, 0, width, height);
  const pixels = imageData.data;
  const visited = new Uint8Array(width * height);
  const traversalBlocked = new Uint8Array(width * height);
  const protectedInterior = new Uint8Array(width * height);
  const queue = new Int32Array(width * height);
  let head = 0;
  let tail = 0;

  function isBrightNeutral(dataIndex) {
    const red = pixels[dataIndex];
    const green = pixels[dataIndex + 1];
    const blue = pixels[dataIndex + 2];
    const minimum = Math.min(red, green, blue);
    const maximum = Math.max(red, green, blue);
    return minimum >= 210 && maximum - minimum <= 38;
  }

  function isOutlineOrColored(dataIndex) {
    if (pixels[dataIndex + 3] < 16) return false;
    const red = pixels[dataIndex];
    const green = pixels[dataIndex + 1];
    const blue = pixels[dataIndex + 2];
    const minimum = Math.min(red, green, blue);
    const maximum = Math.max(red, green, blue);
    return minimum < 185 || maximum - minimum > 45;
  }

  const boundaryRadius = Math.max(3, Math.round(Math.min(width, height) * 0.008));
  const rowLeft = new Int32Array(height);
  const rowRight = new Int32Array(height);
  const rowSpan = new Int32Array(height);
  rowLeft.fill(width);
  rowRight.fill(-1);
  let widestSpan = 0;
  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      const pixelIndex = y * width + x;
      const dataIndex = pixelIndex * 4;
      if (!isOutlineOrColored(dataIndex)) continue;
      rowLeft[y] = Math.min(rowLeft[y], x);
      rowRight[y] = Math.max(rowRight[y], x);
      for (let offsetY = -boundaryRadius; offsetY <= boundaryRadius; offsetY += 1) {
        const blockedY = y + offsetY;
        if (blockedY < 0 || blockedY >= height) continue;
        for (let offsetX = -boundaryRadius; offsetX <= boundaryRadius; offsetX += 1) {
          if (offsetX * offsetX + offsetY * offsetY > boundaryRadius * boundaryRadius) continue;
          const blockedX = x + offsetX;
          if (blockedX < 0 || blockedX >= width) continue;
          traversalBlocked[blockedY * width + blockedX] = 1;
        }
      }
    }
    rowSpan[y] = Math.max(0, rowRight[y] - rowLeft[y]);
    widestSpan = Math.max(widestSpan, rowSpan[y]);
  }

  let bodyTop = -1;
  for (let y = 0; y < height - 4; y += 1) {
    let broadRowCount = 0;
    for (let offset = 0; offset < 5; offset += 1) {
      if (rowSpan[y + offset] >= widestSpan * 0.68) broadRowCount += 1;
    }
    if (broadRowCount === 5) {
      bodyTop = y;
      break;
    }
  }

  if (bodyTop >= 0) {
    for (let y = bodyTop; y < height; y += 1) {
      if (rowSpan[y] < widestSpan * 0.26) continue;
      const inset = Math.max(1, Math.round(width * 0.002));
      for (let x = rowLeft[y] + inset; x <= rowRight[y] - inset; x += 1) {
        protectedInterior[y * width + x] = 1;
      }
    }
  }

  function enqueue(pixelIndex) {
    if (visited[pixelIndex] || traversalBlocked[pixelIndex] || protectedInterior[pixelIndex]) return;
    const dataIndex = pixelIndex * 4;
    const alpha = pixels[dataIndex + 3];
    const isTransparentOutside = alpha < 16;
    const isBrightNeutralBackground = isBrightNeutral(dataIndex);
    if (!isTransparentOutside && !isBrightNeutralBackground) return;
    visited[pixelIndex] = 1;
    queue[tail] = pixelIndex;
    tail += 1;
  }

  for (let x = 0; x < width; x += 1) {
    enqueue(x);
    enqueue((height - 1) * width + x);
  }
  for (let y = 0; y < height; y += 1) {
    enqueue(y * width);
    enqueue(y * width + width - 1);
  }

  while (head < tail) {
    const pixelIndex = queue[head];
    head += 1;
    const x = pixelIndex % width;
    const y = Math.floor(pixelIndex / width);
    pixels[pixelIndex * 4 + 3] = 0;
    if (x > 0) enqueue(pixelIndex - 1);
    if (x + 1 < width) enqueue(pixelIndex + 1);
    if (y > 0) enqueue(pixelIndex - width);
    if (y + 1 < height) enqueue(pixelIndex + width);
    if (x > 0 && y > 0) enqueue(pixelIndex - width - 1);
    if (x + 1 < width && y > 0) enqueue(pixelIndex - width + 1);
    if (x > 0 && y + 1 < height) enqueue(pixelIndex + width - 1);
    if (x + 1 < width && y + 1 < height) enqueue(pixelIndex + width + 1);
  }

  context.putImageData(imageData, 0, 0);
}

function removeCameraPhotoBackground(context, width, height) {
  const imageData = context.getImageData(0, 0, width, height);
  const pixels = imageData.data;
  const visited = new Uint8Array(width * height);
  const queue = new Int32Array(width * height);
  const borderColors = [];
  let head = 0;
  let tail = 0;

  function samplePixel(x, y) {
    const dataIndex = (y * width + x) * 4;
    borderColors.push([pixels[dataIndex], pixels[dataIndex + 1], pixels[dataIndex + 2]]);
  }

  const sampleStep = Math.max(8, Math.round(Math.min(width, height) / 16));
  for (let x = 0; x < width; x += sampleStep) {
    samplePixel(x, 0);
    samplePixel(x, height - 1);
  }
  for (let y = sampleStep; y < height - sampleStep; y += sampleStep) {
    samplePixel(0, y);
    samplePixel(width - 1, y);
  }

  function isSimilarToBorder(dataIndex) {
    const red = pixels[dataIndex];
    const green = pixels[dataIndex + 1];
    const blue = pixels[dataIndex + 2];
    const toleranceSquared = 30 * 30;
    for (const color of borderColors) {
      const redDelta = red - color[0];
      const greenDelta = green - color[1];
      const blueDelta = blue - color[2];
      const distanceSquared = redDelta * redDelta + greenDelta * greenDelta + blueDelta * blueDelta;
      if (distanceSquared <= toleranceSquared) return true;
    }
    return false;
  }

  function enqueue(pixelIndex) {
    if (visited[pixelIndex]) return;
    const dataIndex = pixelIndex * 4;
    if (pixels[dataIndex + 3] >= 16 && !isSimilarToBorder(dataIndex)) return;
    visited[pixelIndex] = 1;
    queue[tail] = pixelIndex;
    tail += 1;
  }

  for (let x = 0; x < width; x += 1) {
    enqueue(x);
    enqueue((height - 1) * width + x);
  }
  for (let y = 0; y < height; y += 1) {
    enqueue(y * width);
    enqueue(y * width + width - 1);
  }

  while (head < tail) {
    const pixelIndex = queue[head];
    head += 1;
    const x = pixelIndex % width;
    const y = Math.floor(pixelIndex / width);
    pixels[pixelIndex * 4 + 3] = 0;
    if (x > 0) enqueue(pixelIndex - 1);
    if (x + 1 < width) enqueue(pixelIndex + 1);
    if (y > 0) enqueue(pixelIndex - width);
    if (y + 1 < height) enqueue(pixelIndex + width);
  }

  const centerX = width * 0.5;
  const centerY = height * 0.49;
  const radiusX = width * 0.48;
  const radiusY = height * 0.5;
  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      const normalizedX = (x - centerX) / radiusX;
      const normalizedY = (y - centerY) / radiusY;
      const distance = Math.sqrt(normalizedX * normalizedX + normalizedY * normalizedY);
      if (distance <= 0.88) continue;
      const dataIndex = (y * width + x) * 4;
      const feather = Math.max(0, Math.min(1, (1 - distance) / 0.12));
      pixels[dataIndex + 3] = Math.round(pixels[dataIndex + 3] * feather);
    }
  }

  context.putImageData(imageData, 0, 0);
}

function normalizeImageForKeycap(sourceCanvas, size = 512) {
  const sourceContext = sourceCanvas.getContext("2d");
  const pixels = sourceContext.getImageData(0, 0, sourceCanvas.width, sourceCanvas.height).data;
  let left = sourceCanvas.width;
  let top = sourceCanvas.height;
  let right = -1;
  let bottom = -1;

  for (let y = 0; y < sourceCanvas.height; y += 1) {
    for (let x = 0; x < sourceCanvas.width; x += 1) {
      if (pixels[(y * sourceCanvas.width + x) * 4 + 3] < 20) continue;
      left = Math.min(left, x);
      top = Math.min(top, y);
      right = Math.max(right, x);
      bottom = Math.max(bottom, y);
    }
  }

  if (right < left || bottom < top) return sourceCanvas;

  const subjectWidth = right - left + 1;
  const subjectHeight = bottom - top + 1;
  const padding = Math.round(size * 0.09);
  const availableSize = size - padding * 2;
  const scale = Math.min(availableSize / subjectWidth, availableSize / subjectHeight);
  const outputWidth = subjectWidth * scale;
  const outputHeight = subjectHeight * scale;
  const outputCanvas = document.createElement("canvas");
  outputCanvas.width = size;
  outputCanvas.height = size;
  outputCanvas.getContext("2d").drawImage(
    sourceCanvas,
    left, top, subjectWidth, subjectHeight,
    (size - outputWidth) / 2, (size - outputHeight) / 2,
    outputWidth, outputHeight
  );
  return outputCanvas;
}

function hasVisiblePhotoSubject(context, width, height) {
  const pixels = context.getImageData(0, 0, width, height).data;
  let visiblePixels = 0;
  const minimumVisiblePixels = Math.round(width * height * 0.035);
  for (let index = 3; index < pixels.length; index += 4) {
    if (pixels[index] < 20) continue;
    visiblePixels += 1;
    if (visiblePixels >= minimumVisiblePixels) return true;
  }
  return false;
}

async function saveCapturedPhotoToGallery(photoDataUrl) {
  if (!photoDataUrl) return;
  const capacitor = window.Capacitor;
  if (capacitor?.isNativePlatform?.() && capacitor.registerPlugin) {
    const gallerySaver = capacitor.registerPlugin("GallerySaver");
    await gallerySaver.saveImage({
      dataUrl: photoDataUrl,
      fileName: `FruitRabbit_${Date.now()}.png`
    });
    return;
  }

  const downloadLink = document.createElement("a");
  downloadLink.href = photoDataUrl;
  downloadLink.download = `FruitRabbit_${Date.now()}.png`;
  document.body.appendChild(downloadLink);
  downloadLink.click();
  downloadLink.remove();
}

cropApply.addEventListener("click", () => {
  stopWebcam();
  const resultCanvas = document.createElement("canvas");
  resultCanvas.width = 512;
  resultCanvas.height = 512;
  const resultCtx = resultCanvas.getContext("2d");
  
  // Crop the 240x240 guided area and export as 512x512
  resultCtx.drawImage(cropCanvas, 20, 20, 240, 240, 0, 0, 512, 512);
  if (!hasVisiblePhotoSubject(resultCtx, 512, 512) && cropImage.complete && cropImage.naturalWidth > 0) {
    const sourceSize = Math.min(cropImage.naturalWidth, cropImage.naturalHeight);
    const sourceX = (cropImage.naturalWidth - sourceSize) / 2;
    const sourceY = (cropImage.naturalHeight - sourceSize) / 2;
    resultCtx.drawImage(cropImage, sourceX, sourceY, sourceSize, sourceSize, 0, 0, 512, 512);
  }
  const croppedImageBackup = resultCtx.getImageData(0, 0, 512, 512);
  if (cropSourceKind === "camera") {
    removeCameraPhotoBackground(resultCtx, 512, 512);
  } else {
    removeCameraPhotoBackground(resultCtx, 512, 512);
  }
  if (!hasVisiblePhotoSubject(resultCtx, 512, 512)) {
    resultCtx.putImageData(croppedImageBackup, 0, 0);
  }
  const croppedDataUrl = normalizeImageForKeycap(resultCanvas).toDataURL("image/png");
  const targetKeyIndex = photoTargetKeyIndex >= 0
    ? photoTargetKeyIndex
    : (activeCropKeyIndex >= 0 ? activeCropKeyIndex : selectedKeyIndex);
  const key = grid.children[targetKeyIndex];
  if (key) {
    const rabbitArt = key.querySelector(".rabbit-art");
    let customArtLayer = key.querySelector(".custom-art-layer");
    if (!customArtLayer) {
      customArtLayer = document.createElement("span");
      customArtLayer.className = "custom-art-layer";
      customArtLayer.setAttribute("aria-hidden", "true");
      key.appendChild(customArtLayer);
    }
    customArtLayer.style.backgroundImage = `url("${croppedDataUrl}")`;
    key.classList.add("custom-art");
    customSlots.add(targetKeyIndex);
    selectKey(targetKeyIndex);
    const processedImage = new Image();
    processedImage.onload = () => {
      processedImage.className = "rabbit-art";
      processedImage.alt = rabbitArt.alt || "FruitRabbit";
      processedImage.style.display = "block";
      processedImage.style.visibility = "visible";
      processedImage.style.opacity = "0.98";
      rabbitArt.replaceWith(processedImage);
      window.FRTE3D?.setCustomCharacterImage(targetKeyIndex, processedImage);
    };
    processedImage.src = croppedDataUrl;
  }
  photoTargetKeyIndex = -1;
  activeCropKeyIndex = -1;
  activeFileInput = null;
  cropModal.classList.remove("native-capture");
  cropModal.style.display = "none";
  requestAppFullscreen();
});

// Action Select Modal Event Listeners
btnChooseCamera.addEventListener("click", () => {
  actionSelectModal.style.display = "none";
  cropModal.style.display = "flex";
  // Trigger camera start directly
  btnToggleCamera.click();
});

photoCaptureToggle?.addEventListener("click", () => {
  if (running) {
    stopRhythmPlayback();
    setMode("free");
  }
  activeCropKeyIndex = selectedKeyIndex;
  photoTargetKeyIndex = selectedKeyIndex;
  activeFileInput = grid.children[selectedKeyIndex]?.querySelector("input") || null;
  feedbackPanel.classList.remove("open");
  settingsToggle.setAttribute("aria-expanded", "false");
  cropModal.style.display = "flex";
  if (!webcamStream) btnToggleCamera.click();
});

btnChooseFolder.addEventListener("click", () => {
  actionSelectModal.style.display = "none";
  if (activeFileInput) activeFileInput.click();
});

btnSelectCancel.addEventListener("click", () => {
  actionSelectModal.style.display = "none";
  photoTargetKeyIndex = -1;
  activeCropKeyIndex = -1;
  activeFileInput = null;
});

// 3D Raycast click/touch delegation
window.FRTE_APP = {
  handle3DPointerDown(index, event) {
    const key = grid.children[index];
    if (!key) return;

    if (grid.classList.contains("character-mode")) {
      selectKey(index);
      activeCropKeyIndex = index;
      photoTargetKeyIndex = index;
      activeFileInput = key.querySelector("input");
      actionSelectModal.style.display = "flex";
      return;
    }
    if (grid.classList.contains("layout-mode")) {
      chooseMoveKey(key);
      beginLayoutDrag(key, event);
      return;
    }
    
    // Rhythm key press behavior
    key.classList.add("pressed");
    selectKey(index);
    press(index, key);
    window.FRTE3D?.setPressed(index, true);
  },
  handle3DPointerUp(event) {
    endLayoutDrag();
    releaseAllPressedKeys(event.pointerId);
  },
  handle3DPointerMove(event) {
    updateLayoutDrag(event);
  },
  handle3DLayoutDrop(fromIndex, toIndex) {
    if (!grid.classList.contains("layout-mode") || fromIndex === toIndex) return;
    const first = grid.children[fromIndex];
    const second = grid.children[toIndex];
    if (first && second) swapKeyAppearance(first, second);
    clearMoveSelection();
  }
};
