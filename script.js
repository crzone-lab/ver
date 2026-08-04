// --- 1. 과일토끼 일러스트 SVG 데이터 정의 ---
const RABBIT_SVGS = {
    strawberry: `<svg viewBox="0 0 100 100">
        <circle cx="50" cy="55" r="30" fill="#fff" stroke="#ff5e7e" stroke-width="3"/>
        <path d="M35 28 C30 10, 42 10, 42 25 Z" fill="#fff" stroke="#ff5e7e" stroke-width="3"/>
        <path d="M65 28 C70 10, 58 10, 58 25 Z" fill="#fff" stroke="#ff5e7e" stroke-width="3"/>
        <path d="M25 45 C25 35, 75 35, 75 45 C75 58, 25 58, 25 45 Z" fill="#ff4365"/>
        <circle cx="38" cy="48" r="4" fill="#fff"/>
        <circle cx="62" cy="48" r="4" fill="#fff"/>
        <circle cx="48" cy="48" r="2.5" fill="#fff"/>
        <circle cx="52" cy="48" r="2.5" fill="#fff"/>
        <circle cx="50" cy="53" r="1.5" fill="#ffd2e2"/>
        <circle cx="34" cy="56" r="3" fill="#ffb4cf" opacity="0.6"/>
        <circle cx="66" cy="56" r="3" fill="#ffb4cf" opacity="0.6"/>
    </svg>`,
    lemon: `<svg viewBox="0 0 100 100">
        <circle cx="50" cy="55" r="30" fill="#fff" stroke="#ffd23f" stroke-width="3"/>
        <path d="M35 28 C30 12, 41 12, 41 26 Z" fill="#fff" stroke="#ffd23f" stroke-width="3"/>
        <path d="M65 28 C70 12, 59 12, 59 26 Z" fill="#fff" stroke="#ffd23f" stroke-width="3"/>
        <path d="M30 40 C35 32, 65 32, 70 40 C75 50, 25 50, 30 40 Z" fill="#fcf300"/>
        <circle cx="35" cy="53" r="3" fill="#1e2229"/>
        <circle cx="65" cy="53" r="3" fill="#1e2229"/>
        <path d="M48 58 Q50 60 52 58" stroke="#1e2229" stroke-width="2" fill="none"/>
        <circle cx="32" cy="59" r="3.5" fill="#ffa43a" opacity="0.5"/>
        <circle cx="68" cy="59" r="3.5" fill="#ffa43a" opacity="0.5"/>
    </svg>`,
    watermelon: `<svg viewBox="0 0 100 100">
        <circle cx="50" cy="55" r="30" fill="#fff" stroke="#4caf50" stroke-width="3"/>
        <path d="M35 28 C30 11, 41 11, 41 25 Z" fill="#fff" stroke="#4caf50" stroke-width="3"/>
        <path d="M65 28 C70 11, 59 11, 59 25 Z" fill="#fff" stroke="#4caf50" stroke-width="3"/>
        <path d="M22 52 C22 36, 78 36, 78 52 Z" fill="#ff4d6d"/>
        <path d="M22 52 C22 55, 78 55, 78 52" stroke="#4caf50" stroke-width="4" fill="none"/>
        <circle cx="35" cy="46" r="2.5" fill="#1e2229"/>
        <circle cx="65" cy="46" r="2.5" fill="#1e2229"/>
        <path d="M49 50 Q50 51 51 50" stroke="#1e2229" stroke-width="2" fill="none"/>
        <circle cx="40" cy="50" r="1" fill="#1e2229"/>
        <circle cx="60" cy="50" r="1" fill="#1e2229"/>
    </svg>`,
    kiwi: `<svg viewBox="0 0 100 100">
        <circle cx="50" cy="55" r="30" fill="#fff" stroke="#8d6e63" stroke-width="3"/>
        <path d="M35 28 C30 12, 41 12, 41 26 Z" fill="#fff" stroke="#8d6e63" stroke-width="3"/>
        <path d="M65 28 C70 12, 59 12, 59 26 Z" fill="#fff" stroke="#8d6e63" stroke-width="3"/>
        <circle cx="50" cy="55" r="18" fill="#81c784"/>
        <circle cx="50" cy="55" r="7" fill="#fff"/>
        <circle cx="38" cy="52" r="2.5" fill="#1e2229"/>
        <circle cx="62" cy="52" r="2.5" fill="#1e2229"/>
        <circle cx="48" cy="56" r="1" fill="#1e2229"/>
        <circle cx="52" cy="56" r="1" fill="#1e2229"/>
        <circle cx="50" cy="51" r="1" fill="#1e2229"/>
        <circle cx="44" cy="53" r="1" fill="#1e2229"/>
        <circle cx="56" cy="53" r="1" fill="#1e2229"/>
    </svg>`,
    mango: `<svg viewBox="0 0 100 100">
        <circle cx="50" cy="55" r="30" fill="#fff" stroke="#ffb300" stroke-width="3"/>
        <path d="M35 28 C30 11, 41 11, 41 25 Z" fill="#fff" stroke="#ffb300" stroke-width="3"/>
        <path d="M65 28 C70 11, 59 11, 59 25 Z" fill="#fff" stroke="#ffb300" stroke-width="3"/>
        <path d="M26 44 C26 34, 74 34, 74 44 C74 54, 26 54, 26 44 Z" fill="#ffb300"/>
        <circle cx="36" cy="48" r="3" fill="#1e2229"/>
        <circle cx="64" cy="48" r="3" fill="#1e2229"/>
        <path d="M49 51 Q50 52 51 51" stroke="#1e2229" stroke-width="1.5" fill="none"/>
        <circle cx="31" cy="52" r="3" fill="#ffa726" opacity="0.6"/>
        <circle cx="69" cy="52" r="3" fill="#ffa726" opacity="0.6"/>
    </svg>`,
    grape: `<svg viewBox="0 0 100 100">
        <circle cx="50" cy="55" r="30" fill="#fff" stroke="#ab47bc" stroke-width="3"/>
        <path d="M35 28 C30 12, 41 12, 41 26 Z" fill="#fff" stroke="#ab47bc" stroke-width="3"/>
        <path d="M65 28 C70 12, 59 12, 59 26 Z" fill="#fff" stroke="#ab47bc" stroke-width="3"/>
        <circle cx="43" cy="41" r="7" fill="#ba68c8"/>
        <circle cx="57" cy="41" r="7" fill="#ba68c8"/>
        <circle cx="50" cy="48" r="7" fill="#9c27b0"/>
        <circle cx="36" cy="52" r="3" fill="#fff"/>
        <circle cx="64" cy="52" r="3" fill="#fff"/>
        <path d="M48 57 Q50 59 52 57" stroke="#1e2229" stroke-width="1.5" fill="none"/>
    </svg>`,
    blueberry: `<svg viewBox="0 0 100 100">
        <circle cx="50" cy="55" r="30" fill="#fff" stroke="#3f51b5" stroke-width="3"/>
        <path d="M35 28 C30 12, 41 12, 41 26 Z" fill="#fff" stroke="#3f51b5" stroke-width="3"/>
        <path d="M65 28 C70 12, 59 12, 59 26 Z" fill="#fff" stroke="#3f51b5" stroke-width="3"/>
        <circle cx="50" cy="44" r="10" fill="#3f51b5"/>
        <path d="M46 36 L50 39 L54 36" stroke="#1a237e" stroke-width="2" fill="none"/>
        <circle cx="36" cy="53" r="3" fill="#1e2229"/>
        <circle cx="64" cy="53" r="3" fill="#1e2229"/>
        <path d="M48 58 Q50 60 52 58" stroke="#1e2229" stroke-width="2" fill="none"/>
        <circle cx="32" cy="58" r="3" fill="#757de8" opacity="0.6"/>
        <circle cx="68" cy="58" r="3" fill="#757de8" opacity="0.6"/>
    </svg>`,
    peach: `<svg viewBox="0 0 100 100">
        <circle cx="50" cy="55" r="30" fill="#fff" stroke="#ff8a80" stroke-width="3"/>
        <path d="M35 28 C30 10, 41 10, 41 25 Z" fill="#fff" stroke="#ff8a80" stroke-width="3"/>
        <path d="M65 28 C70 10, 59 10, 59 25 Z" fill="#fff" stroke="#ff8a80" stroke-width="3"/>
        <path d="M50 36 C35 36, 32 54, 50 56 C68 54, 65 36, 50 36 Z" fill="#ff8a80"/>
        <circle cx="38" cy="46" r="3.5" fill="#1e2229"/>
        <circle cx="62" cy="46" r="3.5" fill="#1e2229"/>
        <path d="M47 50 Q50 53 53 50" stroke="#1e2229" stroke-width="2" fill="none"/>
        <circle cx="33" cy="51" r="3.5" fill="#ff5252" opacity="0.4"/>
        <circle cx="67" cy="51" r="3.5" fill="#ff5252" opacity="0.4"/>
    </svg>`,
    orange: `<svg viewBox="0 0 100 100">
        <circle cx="50" cy="55" r="30" fill="#fff" stroke="#ff6d00" stroke-width="3"/>
        <path d="M35 28 C30 11, 41 11, 41 25 Z" fill="#fff" stroke="#ff6d00" stroke-width="3"/>
        <path d="M65 28 C70 11, 59 11, 59 25 Z" fill="#fff" stroke="#ff6d00" stroke-width="3"/>
        <circle cx="50" cy="45" r="12" fill="#ffab40"/>
        <line x1="50" y1="45" x2="50" y2="33" stroke="#fff" stroke-width="1.5"/>
        <line x1="50" y1="45" x2="60" y2="51" stroke="#fff" stroke-width="1.5"/>
        <line x1="50" y1="45" x2="40" y2="51" stroke="#fff" stroke-width="1.5"/>
        <circle cx="35" cy="53" r="3" fill="#1e2229"/>
        <circle cx="65" cy="53" r="3" fill="#1e2229"/>
        <path d="M48 58 Q50 60 52 58" stroke="#1e2229" stroke-width="1.5" fill="none"/>
    </svg>`
};

// --- 2. 초기 런타임 세션 상태 객체 ---
let sessionState = {
    // 물리계
    SpringStrength: 180,
    Damping: 12.0,
    TravelDistance: 4.0,   // mm
    ActuationPoint: 2.0,   // mm
    PressMass: 0.12,       // kg
    
    // 연출계
    EnableCompression: true,
    EnableTilt: true,
    MaximumTiltDegrees: 6.5,
    BounceVisualMultiplier: 1.2,
    
    // 오디오계
    AudioEnabled: true,
    AudioMasterVolume: 75,
    PitchMinimum: 1.0,
    BottomOutVolume: 80,
    
    // LED 조명계
    LEDEnabled: true,
    LEDColor: '#5EE0D1',
    LEDMaximumEmission: 1.5,
    LEDPatternSpeed: 1.2,
    LEDPattern: 'chase',
    
    // 비즈니스 상태
    ActiveArtwork: 'strawberry'
};

// Undo / Redo 역사 관리용 스택
let undoStack = [];
let redoStack = [];
const MAX_UNDO_LIMIT = 30;

// 물리 시뮬레이션 상태 변수
let y = 0.0; // 현재 키캡 변위 (mm)
let v = 0.0; // 속도
let isPressed = false;
let clickPosition = { x: 0, y: 0 };
let pressStartTime = 0;

// 스위치 트리거 시점 이벤트 플래그
let hasTriggeredActuation = false;
let hasTriggeredBottomOut = false;
let hasTriggeredRelease = false;

// Web Audio API 상태
let audioCtx = null;

// --- 3. 오디오 합성 기능 (Web Audio API) ---
function initAudio() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
}

function playSynthesizedSound(type, velocity = 1.0) {
    if (!sessionState.AudioEnabled) return;
    initAudio();
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }

    const masterVol = (sessionState.AudioMasterVolume / 100) * 0.15; // 마스터 게인 보정
    const pitchMul = sessionState.PitchMinimum;

    // 타건 사운드 노드 생성
    const osc = audioCtx.createOscillator();
    const noise = createNoiseNode();
    const filter = audioCtx.createBiquadFilter();
    const gain = audioCtx.createGain();

    osc.connect(gain);
    if (noise) {
        noise.connect(filter);
        filter.connect(gain);
    }
    gain.connect(audioCtx.destination);

    const now = audioCtx.currentTime;

    if (type === 'actuate') {
        // 청축/갈축 작동 걸쇠 클릭음 합성
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(1400 * pitchMul, now);
        osc.frequency.exponentialRampToValueAtTime(3200 * pitchMul, now + 0.015);

        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(2000 * pitchMul, now);
        filter.Q.setValueAtTime(8, now);

        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(masterVol * 0.7 * velocity, now + 0.002);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.02);

        osc.start(now);
        osc.stop(now + 0.025);
        if (noise) {
            noise.start(now);
            noise.stop(now + 0.025);
        }
    } 
    else if (type === 'bottomout') {
        // 하우징 바닥 부딪힘 묵직한 타건음 합성
        const bottomVol = (sessionState.BottomOutVolume / 100) * masterVol * 1.5;

        osc.type = 'sine';
        osc.frequency.setValueAtTime(95 * pitchMul, now);
        osc.frequency.exponentialRampToValueAtTime(45 * pitchMul, now + 0.04);

        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(300 * pitchMul, now);

        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(bottomVol * velocity, now + 0.004);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.07);

        osc.start(now);
        osc.stop(now + 0.08);
        if (noise) {
            noise.start(now);
            noise.stop(now + 0.08);
        }
    }
    else if (type === 'release') {
        // 스위치 탈출/복귀 시 가벼운 하우징 부딪힘음
        osc.type = 'sine';
        osc.frequency.setValueAtTime(600 * pitchMul, now);
        osc.frequency.exponentialRampToValueAtTime(100 * pitchMul, now + 0.03);

        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(800 * pitchMul, now);

        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(masterVol * 0.4 * velocity, now + 0.003);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.04);

        osc.start(now);
        osc.stop(now + 0.05);
        if (noise) {
            noise.start(now);
            noise.stop(now + 0.05);
        }
    }
}

// 틱 소리용 백색 소음 버퍼 노드 생성기
function createNoiseNode() {
    if (!audioCtx) return null;
    const bufferSize = audioCtx.sampleRate * 0.1; // 0.1초 분량
    const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
        data[i] = Math.random() * 2 - 1;
    }
    const noiseNode = audioCtx.createBufferSource();
    noiseNode.buffer = buffer;
    return noiseNode;
}

// --- 4. 스위치 프리셋 정보 데이터 ---
const PRESETS = {
    linear: {
        SpringStrength: 130,
        Damping: 11.5,
        TravelDistance: 4.0,
        ActuationPoint: 2.0,
        PressMass: 0.10,
        PitchMinimum: 0.90,
        BottomOutVolume: 85
    },
    clicky: {
        SpringStrength: 220,
        Damping: 15.0,
        TravelDistance: 4.0,
        ActuationPoint: 1.8,
        PressMass: 0.14,
        PitchMinimum: 1.30,
        BottomOutVolume: 60
    },
    tactile: {
        SpringStrength: 180,
        Damping: 13.0,
        TravelDistance: 4.0,
        ActuationPoint: 2.0,
        PressMass: 0.12,
        PitchMinimum: 1.05,
        BottomOutVolume: 75
    }
};

function applyPreset(presetName) {
    saveToUndoStack();
    const preset = PRESETS[presetName];
    Object.keys(preset).forEach(key => {
        sessionState[key] = preset[key];
        const input = document.getElementById(key);
        if (input) {
            input.value = preset[key];
            updateDisplayValue(key, preset[key]);
        }
    });

    // 프리셋 버튼 활성화 스타일 적용
    document.querySelectorAll('.preset-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.innerText.includes(presetName === 'linear' ? '적축' : presetName === 'clicky' ? '청축' : '갈축')) {
            btn.classList.add('active');
        }
    });
}

// --- 5. 12개 LED 아크릴 전구 인젝션 및 패턴 렌더링 ---
function buildLedBulbs() {
    const container = document.getElementById('bulbsContainer');
    container.innerHTML = '';

    // 사각형 경계선 테두리 오프셋 계산 (px)
    const d = 43; // 반경
    const s = 30; // 간격
    const positions = [
        // 면 1 (Z = +d)
        { x: -s, y: d, z: 6 },  { x: 0, y: d, z: 6 },  { x: s, y: d, z: 6 },
        // 면 2 (Z = -d)
        { x: -s, y: -d, z: 6 }, { x: 0, y: -d, z: 6 }, { x: s, y: -d, z: 6 },
        // 면 3 (X = +d)
        { x: d, y: -s, z: 6 },  { x: d, y: 0, z: 6 },  { x: d, y: s, z: 6 },
        // 면 4 (X = -d)
        { x: -d, y: -s, z: 6 }, { x: -d, y: 0, z: 6 }, { x: -d, y: s, z: 6 }
    ];

    positions.forEach((pos, idx) => {
        const bulb = document.createElement('div');
        bulb.className = 'led-bulb-3d';
        bulb.id = `led-bulb-${idx}`;
        
        // CSS translate3d 적용 (디퓨저 크기인 100x100 기준 중심 정렬 50px 보정)
        const left = pos.x + 50 - 3; // 반값 크기 보정
        const top = pos.y + 50 - 3;
        bulb.style.transform = `translate3d(${left}px, ${top}px, ${pos.z}px)`;
        container.appendChild(bulb);
    });
}

function updateLedEffects() {
    if (!sessionState.LEDEnabled) {
        document.querySelectorAll('.led-bulb-3d').forEach(bulb => {
            bulb.style.background = 'rgba(255,255,255,0.05)';
            bulb.style.boxShadow = 'none';
        });
        document.querySelector('.led-diffuser-3d').style.boxShadow = 'none';
        return;
    }

    const speed = sessionState.LEDPatternSpeed;
    const maxEmission = sessionState.LEDMaximumEmission;
    const color = sessionState.LEDColor;
    const time = Date.now() * 0.001 * speed;

    document.querySelectorAll('.led-bulb-3d').forEach((bulb, idx) => {
        let intensity = 0.0;

        if (sessionState.LEDPattern === 'chase') {
            // 시계 방향 순차 회전 패턴
            const angle = (idx / 12) * Math.PI * 2;
            const wave = Math.sin(time * 5 + idx * (Math.PI / 6));
            intensity = Math.max(0.1, (wave + 1) * 0.5);
        } 
        else if (sessionState.LEDPattern === 'wave') {
            // 좌우 물결 파동 패턴
            const wave = Math.sin(time * 4 + idx * 0.5);
            intensity = Math.max(0.1, (wave + 1) * 0.5);
        }
        else if (sessionState.LEDPattern === 'rainbow') {
            // 무지개색 그라데이션
            const hue = (idx / 12) * 360 + time * 60;
            const dynamicColor = `hsl(${hue % 360}, 90%, 65%)`;
            bulb.style.background = dynamicColor;
            bulb.style.boxShadow = `0 0 ${10 * maxEmission}px ${dynamicColor}`;
            return;
        }

        const finalColor = hexToRgb(color);
        const finalEmission = intensity * maxEmission;
        bulb.style.background = `rgba(${finalColor.r}, ${finalColor.g}, ${finalColor.b}, ${Math.min(1.0, finalEmission + 0.3)})`;
        bulb.style.boxShadow = `0 0 ${12 * finalEmission}px rgba(${finalColor.r}, ${finalColor.g}, ${finalColor.b}, 1.0)`;
    });

    // 투명 아크릴 디퓨저 레이어도 LED 패턴에 맞춰 은은하게 전체적으로 글로우 발광
    const baseCol = hexToRgb(color);
    const diffuserGlow = 0.15 * maxEmission;
    const diffFace = document.querySelector('.led-diffuser-3d');
    if (diffFace) {
        diffFace.style.boxShadow = `0 0 25px rgba(${baseCol.r}, ${baseCol.g}, ${baseCol.b}, ${diffuserGlow})`;
    }
}

// 헥사 색상코드 RGB 파싱 헬퍼 함수
function hexToRgb(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : { r: 94, g: 224, b: 209 };
}

// --- 6. 과일토끼 선택 패널 인젝션 및 토끼 배치 ---
function buildArtworkSelector() {
    const grid = document.getElementById('artworkGrid');
    grid.innerHTML = '';
    
    Object.keys(RABBIT_SVGS).forEach(key => {
        const item = document.createElement('div');
        item.className = 'artwork-item' + (sessionState.ActiveArtwork === key ? ' active' : '');
        item.onclick = () => selectArtwork(key);
        item.innerHTML = `
            ${RABBIT_SVGS[key]}
            <span>${key === 'strawberry' ? '딸기' : key === 'lemon' ? '레몬' : key === 'watermelon' ? '수박' : key === 'kiwi' ? '키위' : key === 'mango' ? '망고' : key === 'grape' ? '포도' : key === 'blueberry' ? '블루베리' : key === 'peach' ? '복숭아' : '오렌지'}</span>
        `;
        grid.appendChild(item);
    });

    // 3D 키캡 상단 데칼에도 토끼 캐릭터 렌더링
    document.getElementById('activeCharacterArt').innerHTML = RABBIT_SVGS[sessionState.ActiveArtwork];
}

function selectArtwork(key) {
    saveToUndoStack();
    sessionState.ActiveArtwork = key;
    document.querySelectorAll('.artwork-item').forEach(item => item.classList.remove('active'));
    buildArtworkSelector();
}

// --- 7. 물리 실시간 시뮬레이션 프레임 연산 ---
let lastTime = performance.now();
let fpsInterval = 0;

function physicsTick(timestamp) {
    const dt = Math.min(0.03, (timestamp - lastTime) * 0.001); // 델타 타임 (max 30fps 보호)
    lastTime = timestamp;

    // 프레임 레이트 계산 및 위젯 갱신
    fpsInterval++;
    if (fpsInterval >= 30) {
        document.getElementById('lblFPS').innerText = (1 / dt).toFixed(1);
        fpsInterval = 0;
    }

    const travel = sessionState.TravelDistance; // mm
    const spring = sessionState.SpringStrength; // N/m
    const damping = sessionState.Damping;
    const mass = sessionState.PressMass;

    // 목표 물리 깊이(Target position) 설정
    const targetY = isPressed ? travel : 0.0;

    // 스프링 댐퍼 미분 방정식 가속도 계산: a = (k*(targetY - y) - c*v) / m
    const springForce = spring * (targetY - y);
    const dampingForce = damping * v;
    const a = (springForce - dampingForce) / mass;

    // 오일러-크로머 수치 적분 연산
    v += a * dt;
    y += v * dt;

    // 한계 구간 하드 락
    if (y < 0.0) {
        y = 0.0;
        v = 0.0;
    }
    if (y > travel) {
        y = travel;
        v = 0.0;
    }

    // --- 타건음(Audio) 실시간 시점 트리거링 판정 ---
    const act = sessionState.ActuationPoint;
    const velocityScale = Math.min(2.5, Math.abs(v) / 10.0); // 타건 강도 배율

    if (isPressed) {
        // 1. Contact (닿는 순간)
        if (y >= travel * 0.1 && !hasTriggeredActuation && !hasTriggeredBottomOut) {
            // 가볍게 소리 재생 가능 (필요시)
        }
        // 2. Actuation (스위치 클릭 걸쇠 작동 순간)
        if (y >= act && !hasTriggeredActuation) {
            playSynthesizedSound('actuate', velocityScale);
            hasTriggeredActuation = true;
        }
        // 3. Bottom-out (바닥에 완전히 충돌한 순간)
        if (y >= travel * 0.96 && !hasTriggeredBottomOut) {
            playSynthesizedSound('bottomout', velocityScale * 1.2);
            hasTriggeredBottomOut = true;
            triggerVisualBounce();
        }
    } else {
        // 복귀(Release) 타건음
        if (y <= act && !hasTriggeredRelease) {
            // 걸쇠 복귀 (필요 시 가벼운 소리)
            hasTriggeredRelease = true;
        }
        if (y <= travel * 0.05 && (hasTriggeredActuation || hasTriggeredBottomOut)) {
            // 스위치가 완전히 원위치로 복귀하여 하우징에 부딪히는 소리
            playSynthesizedSound('release', 0.8);
            resetTriggerFlags();
        }
    }

    // --- 3D 키캡 트랜스폼 시각적 갱신 ---
    const scaleFactor = sessionState.EnableCompression ? 1.0 - (y / travel) * 0.06 * sessionState.BounceVisualMultiplier : 1.0;
    
    // 키캡 변위 (TranslateY)
    const displacementPx = -(y / travel) * 15; // 3D 변위를 픽셀단위 오프셋으로
    const keycapBody = document.getElementById('keycapBody');
    if (keycapBody) {
        keycapBody.style.transform = `translate3d(0, 0, ${displacementPx}px) scale3d(1, 1, ${scaleFactor})`;
    }

    // 마우스 누름 지점에 따른 입체적인 틸트(Tilt) 각도 연산
    let rotX = 25;
    let rotY = -40;
    
    if (isPressed && sessionState.EnableTilt) {
        const maxTilt = sessionState.MaximumTiltDegrees;
        const tiltX = (clickPosition.y - 70) / 70 * maxTilt; // 중심 70px 보정
        const tiltY = -(clickPosition.x - 70) / 70 * maxTilt;
        rotX += tiltX;
        rotY += tiltY;
    }

    const keycapRoot = document.getElementById('keycapRoot');
    if (keycapRoot) {
        keycapRoot.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg) rotateZ(0deg)`;
    }

    // 실시간 상태 수치 위젯 갱신
    document.getElementById('lblDisplacement').innerText = `${y.toFixed(2)} mm`;
    document.getElementById('lblVelocity').innerText = `${(v / 100).toFixed(2)} m/s`; // m/s 환산

    updateLedEffects();
    requestAnimationFrame(physicsTick);
}

function resetTriggerFlags() {
    hasTriggeredActuation = false;
    hasTriggeredBottomOut = false;
    hasTriggeredRelease = false;
}

function triggerVisualBounce() {
    const keycapBody = document.getElementById('keycapBody');
    if (keycapBody) {
        keycapBody.style.transition = 'none';
        setTimeout(() => {
            keycapBody.style.transition = 'transform 0.08s ease-out';
        }, 10);
    }
}

// --- 8. 키캡 마우스 누름/해제 이벤트 바인딩 ---
function onKeyPress(event) {
    initAudio();
    isPressed = true;
    resetTriggerFlags();
    pressStartTime = performance.now();

    // 마우스가 클릭된 local 좌표 획득 (Tilt 연산용)
    const rect = document.getElementById('keycapContainer').getBoundingClientRect();
    clickPosition.x = event.clientX - rect.left;
    clickPosition.y = event.clientY - rect.top;
}

function onKeyRelease() {
    isPressed = false;
}

// --- 9. 파라미터 조작 및 표시 갱신 ---
function updateParam(id, val) {
    const numVal = parseFloat(val);
    sessionState[id] = numVal;
    
    // 이슬레이터 배경 실시간 비율 그라데이션 갱신
    const slider = document.getElementById(id);
    const min = parseFloat(slider.min);
    const max = parseFloat(slider.max);
    const pct = ((numVal - min) / (max - min)) * 100;
    
    let colorClass = 'physics-slider';
    if (slider.classList.contains('animation-slider')) colorClass = 'animation-slider';
    else if (slider.classList.contains('audio-slider')) colorClass = 'audio-slider';
    else if (slider.classList.contains('led-slider')) colorClass = 'led-slider';
    
    const activeColor = colorClass === 'physics-slider' ? 'var(--color-physics)' : 
                        colorClass === 'animation-slider' ? 'var(--color-animation)' : 
                        colorClass === 'audio-slider' ? 'var(--color-audio)' : 'var(--color-led)';
    
    slider.style.background = `linear-gradient(to right, ${activeColor} ${pct}%, rgba(245, 242, 234, 0.06) ${pct}%)`;

    updateDisplayValue(id, numVal);
    debouncedSaveToUndoStack();
}

function updateDisplayValue(id, val) {
    const display = document.getElementById(`val-${id}`);
    if (!display) return;
    
    if (id === 'TravelDistance' || id === 'ActuationPoint') {
        display.innerText = `${val.toFixed(1)} mm`;
    } else if (id === 'PressMass') {
        display.innerText = `${val.toFixed(2)} kg`;
    } else if (id === 'Damping') {
        display.innerText = val.toFixed(1);
    } else if (id === 'MaximumTiltDegrees') {
        display.innerText = `${val.toFixed(1)}°`;
    } else if (id === 'BounceVisualMultiplier' || id === 'PitchMinimum' || id === 'LEDPatternSpeed' || id === 'LEDMaximumEmission') {
        display.innerText = `${val.toFixed(1)}x`;
    } else if (id === 'AudioMasterVolume' || id === 'BottomOutVolume') {
        display.innerText = `${Math.round(val)}%`;
    } else {
        display.innerText = val;
    }
}

function updateToggle(id, isChecked) {
    saveToUndoStack();
    sessionState[id] = isChecked;
}

function setLedColor(color, element) {
    saveToUndoStack();
    sessionState.LEDColor = color;
    document.querySelectorAll('.color-option').forEach(opt => opt.classList.remove('active'));
    element.classList.add('active');
}

function setLedPattern(pattern) {
    saveToUndoStack();
    sessionState.LEDPattern = pattern;
    document.querySelectorAll('.preset-btn').forEach(btn => {
        if (btn.id && btn.id.startsWith('pat-')) {
            btn.classList.remove('active');
        }
    });
    document.getElementById(`pat-${pattern}`).classList.add('active');
}

// --- 10. Undo / Redo 및 Baseline 비교 기능 ---
let debounceTimer = null;
function debouncedSaveToUndoStack() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
        saveToUndoStack();
    }, 400); // 0.4초 딜레이
}

function saveToUndoStack() {
    // 변경 상태 복제하여 스택 푸시
    undoStack.push(JSON.stringify(sessionState));
    if (undoStack.length > MAX_UNDO_LIMIT) {
        undoStack.shift();
    }
    redoStack = []; // 새 명령 시 Redo 스택 초기화
    updateHistoryButtons();
}

function undo() {
    if (undoStack.length === 0) return;
    redoStack.push(JSON.stringify(sessionState));
    
    const stateStr = undoStack.pop();
    sessionState = JSON.parse(stateStr);
    applyStateToUI();
    updateHistoryButtons();
}

function redo() {
    if (redoStack.length === 0) return;
    undoStack.push(JSON.stringify(sessionState));
    
    const stateStr = redoStack.pop();
    sessionState = JSON.parse(stateStr);
    applyStateToUI();
    updateHistoryButtons();
}

function updateHistoryButtons() {
    document.getElementById('btnUndo').disabled = undoStack.length === 0;
    document.getElementById('btnRedo').disabled = redoStack.length === 0;
}

// Baseline 데이터 임시 백업
let comparisonBackup = null;
const BASELINE_STATE = {
    SpringStrength: 180,
    Damping: 12.0,
    TravelDistance: 4.0,
    ActuationPoint: 2.0,
    PressMass: 0.12,
    EnableCompression: true,
    EnableTilt: true,
    MaximumTiltDegrees: 6.5,
    BounceVisualMultiplier: 1.2,
    AudioEnabled: true,
    AudioMasterVolume: 75,
    PitchMinimum: 1.0,
    BottomOutVolume: 80,
    LEDEnabled: true,
    LEDColor: '#5EE0D1',
    LEDMaximumEmission: 1.5,
    LEDPatternSpeed: 1.2,
    LEDPattern: 'chase',
    ActiveArtwork: 'strawberry'
};

function compareBaseline(showBaseline) {
    if (showBaseline) {
        comparisonBackup = JSON.stringify(sessionState);
        sessionState = { ...BASELINE_STATE };
        applyStateToUI();
        document.getElementById('btnCompare').classList.add('active');
    } else {
        if (comparisonBackup) {
            sessionState = JSON.parse(comparisonBackup);
            comparisonBackup = null;
            applyStateToUI();
        }
        document.getElementById('btnCompare').classList.remove('active');
    }
}

function applyStateToUI() {
    // 모든 파라미터 슬라이더 갱신
    Object.keys(sessionState).forEach(key => {
        const input = document.getElementById(key);
        if (input) {
            if (input.type === 'checkbox') {
                input.checked = sessionState[key];
            } else {
                input.value = sessionState[key];
                updateDisplayValue(key, sessionState[key]);
                
                // 슬라이더 배경 그라데이션 즉시 갱신
                const min = parseFloat(input.min);
                const max = parseFloat(input.max);
                const val = parseFloat(input.value);
                const pct = ((val - min) / (max - min)) * 100;
                let activeColor = 'var(--color-physics)';
                if (input.classList.contains('animation-slider')) activeColor = 'var(--color-animation)';
                else if (input.classList.contains('audio-slider')) activeColor = 'var(--color-audio)';
                else if (input.classList.contains('led-slider')) activeColor = 'var(--color-led)';
                input.style.background = `linear-gradient(to right, ${activeColor} ${pct}%, rgba(245, 242, 234, 0.06) ${pct}%)`;
            }
        }
    });

    // LED 컬러 피커 액티브 상태 보정
    document.querySelectorAll('.color-option').forEach(opt => {
        opt.classList.remove('active');
        if (opt.style.backgroundColor === sessionState.LEDColor || opt.getAttribute('style').includes(sessionState.LEDColor)) {
            opt.classList.add('active');
        }
    });

    // LED 패턴 액티브 보정
    document.querySelectorAll('.preset-btn').forEach(btn => {
        if (btn.id && btn.id.startsWith('pat-')) {
            btn.classList.remove('active');
            if (btn.id === `pat-${sessionState.LEDPattern}`) btn.classList.add('active');
        }
    });

    // 토끼 아트웍 갱신
    buildArtworkSelector();
}

// --- 11. 초기 시동화 및 첫 프레임 트리거 ---
window.onload = () => {
    buildLedBulbs();
    buildArtworkSelector();
    applyStateToUI();
    
    // 키보드 Spacebar나 키 입력 대응
    window.addEventListener('keydown', (e) => {
        if (e.code === 'Space') {
            e.preventDefault();
            if (!isPressed) {
                onKeyPress({ clientX: window.innerWidth / 2, clientY: window.innerHeight / 2 });
            }
        }
    });
    window.addEventListener('keyup', (e) => {
        if (e.code === 'Space') {
            onKeyRelease();
        }
    });

    requestAnimationFrame(physicsTick);
};
