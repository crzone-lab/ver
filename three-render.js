(function () {
  "use strict";

  const canvas = document.querySelector("#key3DCanvas");
  const deck = document.querySelector(".key-deck");
  const extendedLedCanvas = document.querySelector("#extendedLedCanvas");
  const phoneShell = document.querySelector(".phone-shell");
  if (!canvas || !deck || !extendedLedCanvas || !phoneShell || !window.THREE) return;

  const scene = new THREE.Scene();
  const ledRainbowColors = [
    0xff2f55, 0xff6b1a, 0xffc400, 0xd8f238,
    0x35e36f, 0x19e6c1, 0x19cfff, 0x2580ff,
    0x684cff, 0xa83dff, 0xf238d1, 0xff3f86
  ].map(function (color) { return new THREE.Color(color); });
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.outputEncoding = THREE.sRGBEncoding;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 0.58;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  const extensionRenderer = new THREE.WebGLRenderer({ canvas: extendedLedCanvas, antialias: true, alpha: true });
  extensionRenderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  extensionRenderer.outputEncoding = THREE.sRGBEncoding;
  extensionRenderer.toneMapping = THREE.ACESFilmicToneMapping;
  extensionRenderer.toneMappingExposure = 0.58;
  extensionRenderer.setClearColor(0x000000, 0);
  extensionRenderer.autoClear = false;

  const camera = new THREE.PerspectiveCamera(31, 1, 0.1, 100);
  camera.position.set(0, -4.8, 17.5);
  camera.lookAt(0, 0, 0);
  const extensionCamera = camera.clone();
  extensionCamera.layers.set(1);
  const extensionProjection = new THREE.Matrix4();

  scene.add(new THREE.HemisphereLight(0xffffff, 0x59627e, 0.54));

  const mainLight = new THREE.DirectionalLight(0xffffff, 0.72);
  mainLight.position.set(-5, 9, 7);
  mainLight.castShadow = true;
  mainLight.shadow.mapSize.set(1024, 1024);
  mainLight.shadow.camera.left = -7;
  mainLight.shadow.camera.right = 7;
  mainLight.shadow.camera.top = 7;
  mainLight.shadow.camera.bottom = -7;
  scene.add(mainLight);

  const fillLight = new THREE.DirectionalLight(0xb8d8ff, 0.32);
  fillLight.position.set(6, 4, 3);
  scene.add(fillLight);

  const rimLight = new THREE.DirectionalLight(0xffb7e7, 0.28);
  rimLight.position.set(0, 4, -7);
  scene.add(rimLight);

  const productGroup = new THREE.Group();
  productGroup.rotation.x = THREE.MathUtils.degToRad(80);
  productGroup.position.y = 0;
  productGroup.scale.setScalar(1.06);
  scene.add(productGroup);

  function roundedShape(width, depth, radius) {
    const shape = new THREE.Shape();
    const left = -width * 0.5;
    const bottom = -depth * 0.5;
    const right = width * 0.5;
    const top = depth * 0.5;
    shape.moveTo(left + radius, bottom);
    shape.lineTo(right - radius, bottom);
    shape.quadraticCurveTo(right, bottom, right, bottom + radius);
    shape.lineTo(right, top - radius);
    shape.quadraticCurveTo(right, top, right - radius, top);
    shape.lineTo(left + radius, top);
    shape.quadraticCurveTo(left, top, left, top - radius);
    shape.lineTo(left, bottom + radius);
    shape.quadraticCurveTo(left, bottom, left + radius, bottom);
    return shape;
  }

  function roundedBoxGeometry(width, depth, height, radius, bevel) {
    const geometry = new THREE.ExtrudeGeometry(roundedShape(width, depth, radius), {
      depth: height,
      bevelEnabled: true,
      bevelSegments: 4,
      steps: 1,
      bevelSize: bevel,
      bevelThickness: bevel,
      curveSegments: 8
    });
    geometry.rotateX(-Math.PI * 0.5);
    geometry.computeVertexNormals();
    return geometry;
  }

  function taperedKeycapGeometry(width, depth, height) {
    const geometry = new THREE.ExtrudeGeometry(roundedShape(width, depth, 0.52), {
      depth: height,
      bevelEnabled: true,
      bevelSegments: 12,
      steps: 1,
      bevelSize: 0.24,
      bevelThickness: 0.22,
      curveSegments: 24
    });
    const position = geometry.attributes.position;
    for (let index = 0; index < position.count; index += 1) {
      const heightRatio = THREE.MathUtils.clamp(position.getZ(index) / height, 0, 1);
      const scale = THREE.MathUtils.lerp(1, 0.87, heightRatio);
      position.setX(index, position.getX(index) * scale);
      position.setY(index, position.getY(index) * scale);
    }
    geometry.rotateX(-Math.PI * 0.5);
    geometry.computeVertexNormals();
    return geometry;
  }

  const baseMaterial = new THREE.MeshPhysicalMaterial({
    color: 0xf4f6fa,
    roughness: 0.24,
    metalness: 0,
    clearcoat: 0.45,
    clearcoatRoughness: 0.22
  });
  const plateMaterial = new THREE.MeshPhysicalMaterial({
    color: 0xe6ebf1,
    roughness: 0.3,
    clearcoat: 0.34
  });
  const switchMaterial = new THREE.MeshPhysicalMaterial({
    color: 0xffffff,
    roughness: 0.04,
    transmission: 0.36,
    transparent: true,
    opacity: 0.58,
    depthWrite: false,
    thickness: 1.05,
    clearcoat: 1,
    clearcoatRoughness: 0.04,
    side: THREE.DoubleSide
  });
  const stemMaterial = new THREE.MeshPhysicalMaterial({
    color: 0xf5f7fb,
    roughness: 0.2,
    clearcoat: 0.55
  });

  const base = new THREE.Mesh(roundedBoxGeometry(9.05, 8.50, 0.52, 0.42, 0.1), baseMaterial);
  base.position.y = -0.58;
  base.position.z = -0.175;
  base.castShadow = true;
  base.receiveShadow = true;
  productGroup.add(base);

  const plate = new THREE.Mesh(roundedBoxGeometry(8.38, 7.95, 0.25, 0.28, 0.06), plateMaterial);
  plate.position.y = -0.08;
  plate.position.z = -0.10;
  plate.receiveShadow = true;
  productGroup.add(plate);

  const floor = new THREE.Mesh(
    new THREE.PlaneGeometry(18, 18),
    new THREE.ShadowMaterial({ color: 0x090b18, opacity: 0.2 })
  );
  floor.rotation.x = -Math.PI * 0.5;
  floor.position.y = -0.96;
  floor.receiveShadow = true;
  scene.add(floor);

  const keycapGeometry = taperedKeycapGeometry(1.96, 1.96, 1.12);
  const switchGeometry = roundedBoxGeometry(1.88, 1.88, 1.46, 0.16, 0.045);
  const acrylicBaseGeometry = roundedBoxGeometry(1.80, 1.80, 0.18, 0.13, 0.025);
  const acrylicPostGeometry = new THREE.CylinderGeometry(0.11, 0.14, 0.7, 12);
  const acrylicRibGeometry = new THREE.BoxGeometry(0.12, 0.62, 0.12);
  const contactGeometry = new THREE.BoxGeometry(0.28, 0.07, 0.09);
  const contactMaterial = new THREE.MeshBasicMaterial({ color: 0x10131b });
  const pcbGeometry = new THREE.BoxGeometry(1.58, 0.08, 1.58);
  const pcbMaterial = new THREE.MeshPhysicalMaterial({
    color: 0x4b5964,
    roughness: 0.32,
    metalness: 0.18,
    transparent: true,
    opacity: 0.72
  });
  const springGeometry = new THREE.TorusGeometry(0.23, 0.025, 8, 20);
  const springMaterial = new THREE.MeshStandardMaterial({
    color: 0xdce6ed,
    roughness: 0.2,
    metalness: 0.82
  });
  const screwGeometry = new THREE.CylinderGeometry(0.07, 0.07, 0.09, 12);
  const screwMaterial = new THREE.MeshStandardMaterial({
    color: 0xc7d1d9,
    roughness: 0.24,
    metalness: 0.76
  });
  const acrylicEdgeGeometry = new THREE.EdgesGeometry(switchGeometry, 32);
  const acrylicEdgeMaterial = new THREE.LineBasicMaterial({
    color: 0xbfefff,
    transparent: true,
    opacity: 0.58
  });
  const stemGeometry = roundedBoxGeometry(0.46, 0.46, 0.54, 0.07, 0.025);
  const ledGeometry = roundedBoxGeometry(1.42, 0.3, 0.09, 0.1, 0.025);
  const ledCoreGeometry = roundedBoxGeometry(1.42, 1.42, 0.12, 0.14, 0.025);
  const ledBulbGeometry = new THREE.SphereGeometry(0.11, 16, 12);
  const glowCanvas = document.createElement("canvas");
  glowCanvas.width = 64;
  glowCanvas.height = 64;
  const glowContext = glowCanvas.getContext("2d");
  const glowGradient = glowContext.createRadialGradient(32, 32, 1, 32, 32, 31);
  glowGradient.addColorStop(0, "rgba(255,255,255,1)");
  glowGradient.addColorStop(0.16, "rgba(255,255,255,.95)");
  glowGradient.addColorStop(0.42, "rgba(255,255,255,.42)");
  glowGradient.addColorStop(1, "rgba(255,255,255,0)");
  glowContext.fillStyle = glowGradient;
  glowContext.fillRect(0, 0, 64, 64);
  const ledGlowTexture = new THREE.CanvasTexture(glowCanvas);

  const rayCanvas = document.createElement("canvas");
  rayCanvas.width = 64;
  rayCanvas.height = 128;
  const rayCtx = rayCanvas.getContext("2d");
  const rayGrad = rayCtx.createLinearGradient(32, 128, 32, 0);
  rayGrad.addColorStop(0, "rgba(255,255,255,1)");
  rayGrad.addColorStop(0.22, "rgba(255,255,255,0.84)");
  rayGrad.addColorStop(0.48, "rgba(255,255,255,0.38)");
  rayGrad.addColorStop(0.72, "rgba(255,255,255,0.12)");
  rayGrad.addColorStop(0.9, "rgba(255,255,255,0.025)");
  rayGrad.addColorStop(1, "rgba(255,255,255,0)");
  rayCtx.fillStyle = rayGrad;
  rayCtx.fillRect(0, 0, 64, 128);
  rayCtx.globalCompositeOperation = "destination-in";
  const raySideFade = rayCtx.createLinearGradient(0, 0, 64, 0);
  raySideFade.addColorStop(0, "rgba(255,255,255,0)");
  raySideFade.addColorStop(0.04, "rgba(255,255,255,.96)");
  raySideFade.addColorStop(0.5, "rgba(255,255,255,1)");
  raySideFade.addColorStop(0.96, "rgba(255,255,255,.96)");
  raySideFade.addColorStop(1, "rgba(255,255,255,0)");
  rayCtx.fillStyle = raySideFade;
  rayCtx.fillRect(0, 0, 64, 128);
  rayCtx.globalCompositeOperation = "source-over";
  const ledRayTexture = new THREE.CanvasTexture(rayCanvas);

  const deckReflectionMaterials = [];
  [
    [7.65, 0.92, 0, -1.28],
    [7.65, 0.92, 0, 1.28],
    [0.92, 7.65, -1.28, 0],
    [0.92, 7.65, 1.28, 0]
  ].forEach(function (values, reflectionIndex) {
    const reflectionMaterial = new THREE.MeshBasicMaterial({
      map: ledGlowTexture,
      color: new THREE.Color().setHSL(reflectionIndex / 4, 0.88, 0.62),
      transparent: true,
      opacity: 0.18,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      depthTest: true,
      side: THREE.DoubleSide,
      toneMapped: false
    });
    const reflection = new THREE.Mesh(
      new THREE.PlaneGeometry(values[0], values[1]),
      reflectionMaterial
    );
    reflection.rotation.x = -Math.PI * 0.5;
    reflection.position.set(values[2], 0.30, values[3]);
    reflection.renderOrder = 1;
    productGroup.add(reflection);
    deckReflectionMaterials.push(reflectionMaterial);
  });

  function createTrapezoidGeometry(startWidth, endWidth, length) {
    const geometry = new THREE.BufferGeometry();
    const halfStart = startWidth / 2;
    const halfEnd = endWidth / 2;
    const vertices = new Float32Array([
      -halfStart, 0, 0,
       halfStart, 0, 0,
      -halfEnd,   length, 0,
       halfStart, 0, 0,
       halfEnd,   length, 0,
      -halfEnd,   length, 0
    ]);
    const uvs = new Float32Array([
      0, 0,
      1, 0,
      0, 1,
      1, 0,
      1, 1,
      0, 1
    ]);
    geometry.setAttribute("position", new THREE.BufferAttribute(vertices, 3));
    geometry.setAttribute("uv", new THREE.BufferAttribute(uvs, 2));
    geometry.computeVertexNormals();
    return geometry;
  }
  // Keep the seam narrow, then let each rainbow beam spread more broadly
  // toward the phone edge. The wider far edge also enlarges the diamond-like
  // light shape without moving the beam above the keycap.
  const rayGeometry = createTrapezoidGeometry(0.30, 2.30, 7.15);

  const decalGeometry = new THREE.PlaneGeometry(1.40, 1.40);
  const textureLoader = new THREE.TextureLoader();
  const keys = [];
  const overlayPoint = new THREE.Vector3();
  const defaultColors = [
    0xf28eae, 0xb996d6, 0xf19ab8,
    0xc09edb, 0xed91ae, 0xc7a4da,
    0xa9ddda, 0xf0c789, 0xaabde8
  ];

  for (let row = 0; row < 3; row += 1) {
    for (let column = 0; column < 3; column += 1) {
      const index = row * 3 + column;
      const group = new THREE.Group();
      group.position.set((column - 1) * 2.56, 0, (row - 1) * 2.56);

      const switchMesh = new THREE.Mesh(switchGeometry, switchMaterial.clone());
      switchMesh.material.emissive.set(defaultColors[index]);
      switchMesh.material.emissiveIntensity = 0.18;
      switchMesh.position.y = 0.06;
      switchMesh.castShadow = true;
      group.add(switchMesh);

      const acrylicEdges = new THREE.LineSegments(acrylicEdgeGeometry, acrylicEdgeMaterial);
      acrylicEdges.position.copy(switchMesh.position);
      group.add(acrylicEdges);

      const acrylicBase = new THREE.Mesh(acrylicBaseGeometry, switchMesh.material);
      acrylicBase.position.y = 0.14;
      group.add(acrylicBase);

      const pcb = new THREE.Mesh(pcbGeometry, pcbMaterial);
      pcb.position.y = 0.22;
      group.add(pcb);

      const acrylicPostPositions = [
        [-0.76, -0.76], [0.76, -0.76],
        [-0.76, 0.76], [0.76, 0.76]
      ];
      acrylicPostPositions.forEach(function (position) {
        const acrylicPost = new THREE.Mesh(acrylicPostGeometry, switchMesh.material);
        acrylicPost.scale.y = 1.42;
        acrylicPost.position.set(position[0], 0.65, position[1]);
        group.add(acrylicPost);
      });

      [-0.56, 0, 0.56].forEach(function (positionX) {
        const acrylicRib = new THREE.Mesh(acrylicRibGeometry, switchMesh.material);
        acrylicRib.scale.y = 1.48;
        acrylicRib.position.set(positionX, 0.62, 0.82);
        group.add(acrylicRib);
      });

      [-0.58, 0.58].forEach(function (positionX) {
        const contact = new THREE.Mesh(contactGeometry, contactMaterial);
        contact.position.set(positionX, 0.12, 1.035);
        group.add(contact);
      });

      for (let springIndex = 0; springIndex < 6; springIndex += 1) {
        const springRing = new THREE.Mesh(springGeometry, springMaterial);
        springRing.rotation.x = Math.PI * 0.5;
        springRing.position.y = 0.4 + springIndex * 0.13;
        group.add(springRing);
      }

      acrylicPostPositions.forEach(function (position) {
        const screw = new THREE.Mesh(screwGeometry, screwMaterial);
        screw.position.set(position[0], 0.18, position[1]);
        group.add(screw);
      });

      const stem = new THREE.Mesh(stemGeometry, stemMaterial);
      stem.position.y = 0.47;
      group.add(stem);

      const ledMaterial = new THREE.MeshBasicMaterial({
        color: defaultColors[index],
        transparent: true,
        opacity: 0.2,
        toneMapped: false
      });
      const led = new THREE.Mesh(ledGeometry, ledMaterial);
      led.position.set(0, 1.30, 0.72);
      led.renderOrder = 4;
      group.add(led);

      const ledCore = new THREE.Mesh(ledCoreGeometry, ledMaterial);
      ledCore.position.y = 1.24;
      ledCore.renderOrder = 3;
      group.add(ledCore);

      const underGlowMaterial = new THREE.MeshBasicMaterial({
        color: defaultColors[index],
        transparent: true,
        opacity: 0.06,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        depthTest: true,
        side: THREE.DoubleSide,
        toneMapped: false
      });
      const underGlow = new THREE.Mesh(
        roundedBoxGeometry(1.76, 1.76, 0.025, 0.34, 0.015),
        underGlowMaterial
      );
      underGlow.position.y = 0.44;
      underGlow.renderOrder = 2;
      underGlow.visible = true;
      group.add(underGlow);

      const reflectionGlowMaterial = new THREE.MeshBasicMaterial({
        map: ledGlowTexture,
        color: defaultColors[index],
        transparent: true,
        opacity: 0.16,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        depthTest: true,
        side: THREE.DoubleSide,
        toneMapped: false
      });
      const reflectionGlow = new THREE.Mesh(new THREE.PlaneGeometry(3.65, 3.65), reflectionGlowMaterial);
      reflectionGlow.rotation.x = -Math.PI * 0.5;
      reflectionGlow.position.y = 0.31;
      reflectionGlow.renderOrder = 1;
      group.add(reflectionGlow);

      const acrylicReflectionLight = new THREE.PointLight(defaultColors[index], 0.62, 4.4, 1.7);
      acrylicReflectionLight.position.set(0, 0.72, 0);
      group.add(acrylicReflectionLight);

      const ledBoundaryMaterial = new THREE.MeshBasicMaterial({
        color: defaultColors[index],
        transparent: true,
        opacity: 0.24,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        depthTest: true,
        toneMapped: false
      });
      const ledBoundaryMeshes = [];
      [
        [1.66, 0.12, 0.08, 0, 1.50, 0.90],
        [1.66, 0.12, 0.08, 0, 1.50, -0.90],
        [0.08, 0.12, 1.66, 0.90, 1.50, 0],
        [0.08, 0.12, 1.66, -0.90, 1.50, 0]
      ].forEach(function (values) {
        const boundary = new THREE.Mesh(
          new THREE.BoxGeometry(values[0], values[1], values[2]),
          ledBoundaryMaterial
        );
        boundary.position.set(values[3], values[4], values[5]);
        boundary.renderOrder = 5;
        boundary.visible = false;
        ledBoundaryMeshes.push(boundary);
      });

      const ledBulbMaterials = [];
      const ledGlowMaterials = [];
      const ledRayMaterials = [];
      const ledBulbPositions = [
        [-0.42, 0.72], [0, 0.72], [0.42, 0.72],
        [0.72, 0.42], [0.72, 0], [0.72, -0.42],
        [0.42, -0.72], [0, -0.72], [-0.42, -0.72],
        [-0.72, -0.42], [-0.72, 0], [-0.72, 0.42]
      ];
      ledBulbPositions.forEach(function (position, bulbIndex) {
        const bulbMaterial = ledMaterial.clone();
        bulbMaterial.opacity = 0.58;
        bulbMaterial.blending = THREE.AdditiveBlending;
        bulbMaterial.depthWrite = false;
        bulbMaterial.depthTest = true;
        const bulb = new THREE.Mesh(ledBulbGeometry, bulbMaterial);
        const bulbScale = 1.25;
        bulb.position.set(position[0] * bulbScale, 1.49, position[1] * bulbScale);
        bulb.renderOrder = 8;
        bulb.visible = false;
        ledBulbMaterials.push(bulbMaterial);

        const glowMaterial = new THREE.SpriteMaterial({
          map: ledGlowTexture,
          color: defaultColors[index],
          transparent: true,
          opacity: 0.12,
          blending: THREE.AdditiveBlending,
          depthWrite: false,
          depthTest: true,
          toneMapped: false
        });
        const glow = new THREE.Sprite(glowMaterial);
        glow.position.set(position[0] * bulbScale, 1.50, position[1] * bulbScale);
        glow.scale.set(0.34, 0.34, 0.34);
        glow.renderOrder = 6;
        glow.visible = false;
        ledGlowMaterials.push(glowMaterial);

        // Light Ray / Beam Plane
        const rayColor = ledRainbowColors[bulbIndex].clone();
        const rayMaterial = new THREE.MeshBasicMaterial({
          map: ledRayTexture,
          color: rayColor,
          transparent: true,
          opacity: 0.08,
          blending: THREE.NormalBlending,
          depthWrite: false,
          depthTest: true,
          side: THREE.DoubleSide
        });
        const rayMesh = new THREE.Mesh(rayGeometry, rayMaterial);
        rayMesh.renderOrder = 2;
        rayMesh.visible = true;
        // Rays are rendered once by the phone-sized renderer. Keeping them off
        // the keycap renderer prevents the old and extended beams overlapping.
        rayMesh.layers.set(1);

        // Position and rotate ray outward
        let posX = position[0] * bulbScale;
        let posZ = position[1] * bulbScale;
        const beamOffset = 0;
        const radialLength = Math.hypot(posX, posZ) || 1;
        posX += (posX / radialLength) * beamOffset;
        posZ += (posZ / radialLength) * beamOffset;
        // Each of the twelve LEDs keeps its own outward angle instead of
        // collapsing into four overlapping bands.
        const rotY = Math.atan2(-posX, -posZ);
        // Start at the original twelve-LED seam between the coloured cap and
        // the clear acrylic switch body (the bulbs are at y = 1.49).
        rayMesh.position.set(posX, 1.49, posZ);
        rayMesh.rotation.set(-Math.PI * 0.5, 0, rotY);
        group.add(rayMesh);
        ledRayMaterials.push({ material: rayMaterial, mesh: rayMesh });
      });

      const capColor = new THREE.Color(defaultColors[index]).multiplyScalar(0.92);
      const capMaterial = new THREE.MeshPhysicalMaterial({
        color: capColor,
        emissive: new THREE.Color(defaultColors[index]).multiplyScalar(0.22),
        emissiveIntensity: 0,
        roughness: 0.48,
        metalness: 0,
        clearcoat: 0.08,
        clearcoatRoughness: 0.55
      });
      const cap = new THREE.Mesh(keycapGeometry, capMaterial);
      cap.position.y = 1.58;
      cap.castShadow = true;
      cap.receiveShadow = true;
      cap.renderOrder = 10;
      group.add(cap);

      // Depth-only copy for the phone-sized ray renderer. It blocks beams
      // behind the translucent coloured cap without drawing a second cap.
      const capRayOccluderMaterial = new THREE.MeshBasicMaterial({
        colorWrite: false,
        depthWrite: true,
        depthTest: true,
        side: THREE.DoubleSide
      });
      const capRayOccluder = new THREE.Mesh(keycapGeometry, capRayOccluderMaterial);
      capRayOccluder.position.copy(cap.position);
      capRayOccluder.renderOrder = 0;
      capRayOccluder.layers.set(1);
      group.add(capRayOccluder);

      const decalMaterial = new THREE.MeshBasicMaterial({
        transparent: true,
        depthTest: true,
        depthWrite: false,
        side: THREE.DoubleSide
      });
      const decal = new THREE.Mesh(decalGeometry, decalMaterial);
      decal.rotation.x = -Math.PI * 0.5;
      decal.position.set(0, 2.96, 0.0);
      decal.renderOrder = 11;
      decal.visible = false;
      group.add(decal);

      productGroup.add(group);
      keys.push({
        group,
        cap,
        capRayOccluder,
        decal,
        capMaterial,
        ledMaterial,
        underGlowMaterial,
        reflectionGlowMaterial,
        acrylicReflectionLight,
        ledBoundaryMaterial,
        ledBoundaryMeshes,
        ledBulbMaterials,
        ledGlowMaterials,
        ledRayMaterials,
        switchMaterial: switchMesh.material,
        currentY: 1.58,
        velocity: 0,
        targetY: 1.58,
        ledEnabled: true,
        pressed: false,
        targeted: false,
        ledPattern: "press-chase",
        texture: null
      });
    }
  }

  function resize() {
    const width = Math.max(1, deck.clientWidth);
    const height = Math.max(1, deck.clientHeight);
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    const pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
    const shellWidth = Math.max(1, phoneShell.clientWidth);
    const shellHeight = Math.max(1, phoneShell.clientHeight);
    extensionRenderer.setPixelRatio(pixelRatio);
    extensionRenderer.setSize(shellWidth, shellHeight, false);
  }

  function renderExtendedLedRays() {
    const shellRect = phoneShell.getBoundingClientRect();
    const deckRect = canvas.getBoundingClientRect();
    const shellWidth = phoneShell.clientWidth;
    const shellHeight = phoneShell.clientHeight;
    if (shellWidth < 1 || shellHeight < 1 || deckRect.width < 1 || deckRect.height < 1) return;
    const deckLeft = Math.max(0, deckRect.left - shellRect.left);
    const deckTop = Math.max(0, deckRect.top - shellRect.top);
    const deckRight = Math.min(shellWidth, deckLeft + deckRect.width);
    const deckBottom = Math.min(shellHeight, deckTop + deckRect.height);
    const scaleX = deckRect.width / shellWidth;
    const scaleY = deckRect.height / shellHeight;
    const offsetX = (2 * deckLeft + deckRect.width) / shellWidth - 1;
    const offsetY = 1 - (2 * deckTop + deckRect.height) / shellHeight;
    extensionProjection.set(
      scaleX, 0, 0, offsetX,
      0, scaleY, 0, offsetY,
      0, 0, 1, 0,
      0, 0, 0, 1
    );
    extensionCamera.position.copy(camera.position);
    extensionCamera.quaternion.copy(camera.quaternion);
    extensionCamera.scale.copy(camera.scale);
    extensionCamera.updateMatrixWorld(true);
    extensionCamera.projectionMatrix.multiplyMatrices(extensionProjection, camera.projectionMatrix);
    extensionCamera.projectionMatrixInverse.copy(extensionCamera.projectionMatrix).invert();
    extensionRenderer.setScissorTest(false);
    extensionRenderer.clear(true, true, true);
    extensionRenderer.setViewport(0, 0, shellWidth, shellHeight);
    extensionRenderer.render(scene, extensionCamera);
  }

  function setPressed(index, pressed) {
    const key = keys[index];
    if (!key) return;
    key.pressed = pressed;
    key.targetY = pressed ? 1.18 : 1.58;
    const coreOpacity = key.ledEnabled ? (pressed ? 0.82 : key.targeted ? 0.58 : 0.14) : 0;
    const bulbOpacity = key.ledEnabled ? (pressed ? 1 : key.targeted ? 0.9 : 0.42) : 0;
    key.ledMaterial.opacity = coreOpacity;
    key.ledBulbMaterials.forEach(function (material) {
      material.opacity = bulbOpacity;
    });
  }

  function setColor(index, color) {
    const key = keys[index];
    if (!key) return;
    key.capMaterial.color.set(color).multiplyScalar(0.92);
    key.capMaterial.emissive.set(color).multiplyScalar(0.22);
    key.underGlowMaterial.color.set(color);
    key.reflectionGlowMaterial.color.set(color);
    key.acrylicReflectionLight.color.set(color);
    key.ledBoundaryMaterial.color.set(color);
    key.switchMaterial.emissive.set(color);
    key.ledMaterial.color.set(color);
    key.ledBulbMaterials.forEach(function (material) {
      material.color.set(color);
    });
    key.ledGlowMaterials.forEach(function (material) {
      material.color.set(color);
    });
    const baseColor = new THREE.Color(color);
    const hsl = {};
    baseColor.getHSL(hsl);
    key.ledRayMaterials.forEach(function (obj, rayIndex) {
      const rayColor = new THREE.Color().setHSL((hsl.h + rayIndex / 12) % 1.0, hsl.s, hsl.l);
      obj.material.color.copy(rayColor);
    });
  }

  function setCharacter(index, source) {
    const key = keys[index];
    if (!key || !source) return;
    textureLoader.load(source, function (texture) {
      texture.encoding = THREE.sRGBEncoding;
      texture.anisotropy = Math.min(8, renderer.capabilities.getMaxAnisotropy());
      if (key.texture) key.texture.dispose();
      key.texture = texture;
      key.decal.material.map = texture;
      key.decal.material.needsUpdate = true;
      key.decal.visible = false;
    });
  }

  function setCharacterImage(index, image) {
    const key = keys[index];
    if (!key || !image || !image.complete || image.naturalWidth === 0) return;
    const texture = new THREE.Texture(image);
    texture.encoding = THREE.sRGBEncoding;
    texture.anisotropy = Math.min(8, renderer.capabilities.getMaxAnisotropy());
    texture.needsUpdate = true;
    if (key.texture) key.texture.dispose();
    key.texture = texture;
    key.decal.material.map = texture;
    key.decal.material.needsUpdate = true;
    key.decal.visible = false;
  }

  function setCustomCharacterImage(index, image) {
    const key = keys[index];
    if (!key || !image || !image.complete || image.naturalWidth === 0) return;
    const texture = new THREE.Texture(image);
    texture.encoding = THREE.sRGBEncoding;
    texture.anisotropy = Math.min(8, renderer.capabilities.getMaxAnisotropy());
    texture.needsUpdate = true;
    if (key.texture) key.texture.dispose();
    key.texture = texture;
    key.decal.material.map = texture;
    key.decal.material.needsUpdate = true;
    key.decal.visible = true;
  }

  function setLedEnabled(enabled) {
    keys.forEach(function (key) {
      key.ledEnabled = enabled;
      const coreOpacity = enabled ? (key.pressed ? 0.82 : key.targeted ? 0.58 : 0.14) : 0;
      const bulbOpacity = enabled ? (key.pressed ? 1 : key.targeted ? 0.9 : 0.42) : 0;
      key.ledMaterial.opacity = coreOpacity;
      key.ledBulbMaterials.forEach(function (material) {
        material.opacity = bulbOpacity;
      });
      key.ledGlowMaterials.forEach(function (material) {
        material.opacity = bulbOpacity * 0.12;
      });
      key.ledRayMaterials.forEach(function (obj) {
        obj.material.opacity = enabled ? (key.pressed ? 0.85 : key.targeted ? 0.42 : 0.08) : 0;
      });
    });
  }

  function setLedTarget(index, targeted) {
    const key = keys[index];
    if (!key) return;
    key.targeted = targeted;
    const coreOpacity = key.ledEnabled ? (key.pressed ? 0.82 : targeted ? 0.58 : 0.14) : 0;
    const bulbOpacity = key.ledEnabled ? (key.pressed ? 1 : targeted ? 0.9 : 0.42) : 0;
    key.ledMaterial.opacity = coreOpacity;
    key.ledBulbMaterials.forEach(function (material) {
      material.opacity = bulbOpacity;
    });
    key.ledGlowMaterials.forEach(function (material) {
      material.opacity = bulbOpacity * 0.12;
    });
    key.ledRayMaterials.forEach(function (obj) {
      obj.material.opacity = key.ledEnabled ? (key.pressed ? 0.85 : targeted ? 0.42 : 0.08) : 0;
    });
  }

  function setLedPattern(index, pattern) {
    const key = keys[index];
    if (!key) return;
    if (pattern === "chase" || pattern === "solid" || pattern === "press-chase") {
      key.ledPattern = pattern;
    }
  }

  let ledMode = "rainbow";
  function setLedMode(mode) {
    ledMode = mode === "rainbow" ? "rainbow" : "solid";
    if (ledMode === "solid") {
      keys.forEach(function (key) {
        key.ledBulbMaterials.forEach(function (material) {
          material.color.copy(key.ledMaterial.color);
        });
        key.ledGlowMaterials.forEach(function (material) {
          material.color.copy(key.ledMaterial.color);
        });
        key.ledRayMaterials.forEach(function (obj) {
          obj.material.color.copy(key.ledMaterial.color);
        });
      });
    }
  }

  let previousTime = performance.now();
  function syncCharacterOverlays() {
    const overlayKeys = document.querySelectorAll("#keyGrid > .key");
    if (overlayKeys.length !== keys.length) return;
    scene.updateMatrixWorld(true);
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    keys.forEach(function (key, index) {
      const points = [
        [-0.76, -0.76], [0.76, -0.76],
        [0.76, 0.76], [-0.76, 0.76]
      ].map(function (point) {
        overlayPoint.set(point[0], key.currentY + 1.16, point[1]);
        key.group.localToWorld(overlayPoint);
        overlayPoint.project(camera);
        return {
          x: (overlayPoint.x * 0.5 + 0.5) * width,
          y: (-overlayPoint.y * 0.5 + 0.5) * height
        };
      });
      const minX = Math.min.apply(null, points.map(function (point) { return point.x; }));
      const maxX = Math.max.apply(null, points.map(function (point) { return point.x; }));
      const minY = Math.min.apply(null, points.map(function (point) { return point.y; }));
      const maxY = Math.max.apply(null, points.map(function (point) { return point.y; }));
      const element = overlayKeys[index];
      element.style.left = minX + "px";
      element.style.top = minY + "px";
      element.style.width = Math.max(1, maxX - minX) + "px";
      element.style.height = Math.max(1, maxY - minY) + "px";
    });
  }

  function render(time) {
    const delta = Math.min((time - previousTime) / 1000, 0.033);
    previousTime = time;
    const anyKeyPressed = keys.some(function (key) { return key.pressed; });
    deckReflectionMaterials.forEach(function (material, reflectionIndex) {
      const hue = (time / (anyKeyPressed ? 820 : 10500) + reflectionIndex * 0.21) % 1;
      material.color.setHSL(hue, 0.94, 0.64);
      material.opacity = anyKeyPressed
        ? 0.52 + Math.sin(time * 0.045 + reflectionIndex) * 0.16
        : 0.15 + Math.sin(time * 0.0012 + reflectionIndex) * 0.035;
    });
    keys.forEach(function (key, keyIndex) {
      const acceleration = (key.targetY - key.currentY) * 125 - key.velocity * 18;
      key.velocity += acceleration * delta;
      key.currentY += key.velocity * delta;
      key.cap.position.y = key.currentY;
      key.capRayOccluder.position.y = key.currentY;
      key.decal.position.y = key.currentY + 1.38;
      const chaseActive = key.ledPattern === "chase"
        || (key.ledPattern === "press-chase" && (key.pressed || key.targeted));
      const bulbCount = key.ledBulbMaterials.length;
      const chaseHead = Math.floor(time / (key.pressed ? 34 : 72) + keyIndex * 2) % bulbCount;
      const idleHead = Math.floor(time / 900 + keyIndex * 2) % bulbCount;
      key.capMaterial.emissiveIntensity = 0;
      key.underGlowMaterial.opacity = key.ledEnabled
        ? (key.pressed ? 1 : key.targeted ? 0.72 : 0.30)
        : 0;
      key.reflectionGlowMaterial.opacity = key.ledEnabled
        ? (key.pressed ? 0.72 : key.targeted ? 0.44 : 0.18)
        : 0;
      key.ledBoundaryMaterial.opacity = key.ledEnabled
        ? (key.pressed ? 0.92 : key.targeted ? 0.62 : 0.30)
        : 0;
      const pressFlash = key.pressed ? 0.72 + Math.sin(time * 0.052 + keyIndex) * 0.28 : 1;
      if (ledMode === "rainbow") {
        const reflectionHue = (time / (key.pressed ? 900 : 12000) + keyIndex / keys.length) % 1;
        key.reflectionGlowMaterial.color.setHSL(reflectionHue, 0.92, 0.62);
        key.acrylicReflectionLight.color.setHSL(reflectionHue, 0.94, 0.62);
      }
      key.acrylicReflectionLight.intensity = key.ledEnabled
        ? (key.pressed ? 4.8 * pressFlash : key.targeted ? 2.4 : 0.72)
        : 0;
      key.acrylicReflectionLight.distance = key.pressed ? 5.8 : 4.4;
      key.switchMaterial.emissiveIntensity = key.ledEnabled
        ? (key.pressed ? 3.40 * pressFlash : key.targeted ? 1.85 : 0.66)
        : 0;
      key.ledBulbMaterials.forEach(function (material, bulbIndex) {
        const glowMaterial = key.ledGlowMaterials[bulbIndex];
        const rayObj = key.ledRayMaterials[bulbIndex];
        if (ledMode === "rainbow") {
          material.color.copy(ledRainbowColors[bulbIndex]);
          glowMaterial.color.copy(material.color);
          rayObj.material.color.copy(material.color);
        }
        if (!key.ledEnabled) {
          material.opacity = 0;
          glowMaterial.opacity = 0;
          return;
        }
        if (!chaseActive) {
          const idleDistance = (bulbIndex - idleHead + bulbCount) % bulbCount;
          if (idleDistance === 0) {
            material.opacity = 0.82;
            glowMaterial.opacity = 0.20;
          } else if (idleDistance === 1 || idleDistance === bulbCount - 1) {
            material.opacity = 0.64;
            glowMaterial.opacity = 0.13;
          } else if (idleDistance === 2 || idleDistance === bulbCount - 2) {
            material.opacity = 0.52;
            glowMaterial.opacity = 0.09;
          } else {
            material.opacity = 0.40;
            glowMaterial.opacity = 0.055;
          }
          return;
        }
        const clockwiseDistance = (bulbIndex - chaseHead + bulbCount) % bulbCount;
        if (clockwiseDistance === 0) {
          material.opacity = 1;
          glowMaterial.opacity = 0.34;
        } else if (clockwiseDistance === 1 || clockwiseDistance === bulbCount - 1) {
          material.opacity = 0.72;
          glowMaterial.opacity = 0.22;
        } else if (clockwiseDistance === 2 || clockwiseDistance === bulbCount - 2) {
          material.opacity = 0.46;
          glowMaterial.opacity = 0.14;
        } else {
          material.opacity = 0.30;
          glowMaterial.opacity = 0.075;
        }
      });

      // Animate Light Rays / Beams
      key.ledRayMaterials.forEach(function (obj, rayIndex) {
        let op = 0;
        let scaleY = 1.0;
        if (key.ledEnabled) {
          if (chaseActive) {
            const clockwiseDistance = (rayIndex - chaseHead + bulbCount) % bulbCount;
            if (clockwiseDistance === 0) {
              op = Math.min(1, 0.90 + pressFlash * 0.10);
              scaleY = 2.15;
            } else if (clockwiseDistance === 1 || clockwiseDistance === bulbCount - 1) {
              op = 0.78;
              scaleY = 1.94;
            } else if (clockwiseDistance === 2 || clockwiseDistance === bulbCount - 2) {
              op = 0.52;
              scaleY = 1.72;
            } else {
              op = 0.18;
              scaleY = 1.46;
            }
            if (key.pressed) {
              op = Math.min(1, op * (1.05 + pressFlash * 0.48));
              scaleY *= 1.24 + pressFlash * 0.22;
            }
          } else {
            op = 0.27;
            scaleY = 1.58;
          }
        }
        obj.material.opacity = op;
        obj.mesh.scale.set(1.0, scaleY, 1.0);
      });
    });
    syncCharacterOverlays();
    renderExtendedLedRays();
    renderer.render(scene, camera);
    requestAnimationFrame(render);
  }

  // 3D Raycast click/touch handler
  const raycaster = new THREE.Raycaster();
  const mouse = new THREE.Vector2();
  let pointerDownKeyIndex = -1;

  function getIntersectedKeyIndex(event) {
    const rect = canvas.getBoundingClientRect();
    const clientX = event.touches ? event.touches[0].clientX : event.clientX;
    const clientY = event.touches ? event.touches[0].clientY : event.clientY;
    mouse.x = ((clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = -((clientY - rect.top) / rect.height) * 2 + 1;
    raycaster.setFromCamera(mouse, camera);

    const capMeshes = keys.map(k => k.cap);
    const intersects = raycaster.intersectObjects(capMeshes);
    if (intersects.length > 0) {
      const hitCap = intersects[0].object;
      return capMeshes.indexOf(hitCap);
    }
    return -1;
  }

  canvas.addEventListener("pointerdown", function (event) {
    const index = getIntersectedKeyIndex(event);
    if (index !== -1) {
      pointerDownKeyIndex = index;
      canvas.setPointerCapture?.(event.pointerId);
      window.FRTE_APP?.handle3DPointerDown(index, event);
    }
  });

  window.addEventListener("pointermove", function (event) {
    if (pointerDownKeyIndex !== -1) window.FRTE_APP?.handle3DPointerMove(event);
  });

  window.addEventListener("pointerup", function (event) {
    const pointerUpKeyIndex = getIntersectedKeyIndex(event);
    if (pointerDownKeyIndex !== -1 && pointerUpKeyIndex !== -1 && pointerDownKeyIndex !== pointerUpKeyIndex) {
      window.FRTE_APP?.handle3DLayoutDrop(pointerDownKeyIndex, pointerUpKeyIndex);
    }
    window.FRTE_APP?.handle3DPointerUp(event);
    pointerDownKeyIndex = -1;
  });

  window.addEventListener("pointercancel", function (event) {
    window.FRTE_APP?.handle3DPointerUp(event);
    pointerDownKeyIndex = -1;
  });

  window.addEventListener("blur", function () {
    window.FRTE_APP?.handle3DPointerUp({ pointerId: -1 });
    pointerDownKeyIndex = -1;
  });

  window.FRTE3D = {
    setPressed,
    setColor,
    setCharacter,
    setCharacterImage,
    setCustomCharacterImage,
    setLedEnabled,
    setLedTarget,
    setLedPattern,
    setLedMode,
    isReady: true
  };

  deck.classList.add("webgl-ready");
  resize();
  const resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(deck);
  resizeObserver.observe(phoneShell);
  window.addEventListener("resize", resize);
  requestAnimationFrame(render);
}());
