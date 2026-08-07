/**
 * Consciousness Field Renderer - Three.js WebGL implementation
 * 
 * This module provides GPU-accelerated visualization of consciousness fields
 * with shader-based rendering for:
 * - Complex-valued lattice fields with phase information
 * - Real-time particle systems for consciousness nodes
 * - Interactive controls for parameter manipulation
 */

class ConsciousnessFieldRenderer {
    constructor(options = {}) {
        this.options = {
            latticeSize: options.latticeSize || 128,
            complexField: options.complexField !== false,
            phaseVisualization: options.phaseVisualization || 'spectral',
            multiverseBranching: options.multiverseBranching !== false,
            enableParticles: options.enableParticles !== false,
            enableClusters: options.enableClusters !== false,
            ...options
        };

        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.canvas = null;
        
        // Consciousness field materials and geometries
        this.nodeMaterial = null;
        this.clusterMaterial = null;
        this.universeMaterial = null;
        this.attentionFieldMaterial = null;
        
        // Node instances for GPU instancing
        this.nodeGeometry = null;
        this.nodeInstances = null;
        this.maxNodes = 1000;
        
        // Cluster connections
        this.clusterConnections = [];
        
        // Camera controls
        this.cameraTarget = new THREE.Vector3(0, 0, 0);
        this.cameraPosition = new THREE.Vector3(0, 0, 500);
        this.zoom = 1.0;
        
        // Mouse interaction
        this.mouse = new THREE.Vector2();
        this.raycaster = new THREE.Raycaster();
        this.isMouseDown = false;
        this.currentMode = 'consciousness';
        this.interactionMode = 'push';
        
        // Performance tracking
        this.frameCount = 0;
        this.lastFPSUpdate = Date.now();
        this.fps = 0;
        
        this.init();
    }

    init() {
        // Get canvas
        this.canvas = document.getElementById('canvas');
        
        // Setup Three.js scene
        this.setupScene();
        this.setupCamera();
        this.setupRenderer();
        this.setupLighting();
        this.setupMaterials();
        this.setupGeometry();
        this.setupEventListeners();
        
        // Start render loop
        this.animate();
        
        console.log('Consciousness Field Renderer initialized');
    }

    setupScene() {
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x0a0a1a);
        
        // Add subtle fog for depth
        this.scene.fog = new THREE.Fog(0x0a0a1a, 1000, 3000);
    }

    setupCamera() {
        const aspect = window.innerWidth / window.innerHeight;
        this.camera = new THREE.PerspectiveCamera(60, aspect, 1, 5000);
        this.camera.position.copy(this.cameraPosition);
        this.camera.lookAt(this.cameraTarget);
    }

    setupRenderer() {
        this.renderer = new THREE.WebGLRenderer({
            canvas: this.canvas,
            antialias: true,
            alpha: false,
            powerPreference: "high-performance"
        });
        
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.renderer.sortObjects = false;
        this.renderer.autoClear = false;
        
        // Enable additive blending for glow effects
        this.renderer.capabilities.logarithmicDepthBuffer = true;
    }

    setupLighting() {
        // Ambient light for base visibility
        const ambientLight = new THREE.AmbientLight(0x404040, 0.3);
        this.scene.add(ambientLight);
        
        // Point light for consciousness field illumination
        const pointLight = new THREE.PointLight(0x00ffaa, 1, 1000);
        pointLight.position.set(0, 0, 200);
        this.scene.add(pointLight);
    }

    setupMaterials() {
        // Consciousness node material with complex field visualization
        this.nodeMaterial = new THREE.ShaderMaterial({
            uniforms: {
                time: { value: 0 },
                amplitude: { value: 1.0 },
                phase: { value: 0.0 },
                frequency: { value: 40.0 },
                consciousness_re: { value: 0.0 },
                consciousness_im: { value: 0.0 },
                intelligence_depth: { value: 0.0 },
                cluster_id: { value: -1 }
            },
            vertexShader: `
                attribute float amplitude;
                attribute float phase;
                attribute float frequency;
                attribute float consciousness_re;
                attribute float consciousness_im;
                attribute float intelligence_depth;
                attribute float cluster_id;
                
                varying float vAmplitude;
                varying float vPhase;
                varying float vFrequency;
                varying float vConsciousness_re;
                varying float vConsciousness_im;
                varying float vIntelligence_depth;
                varying float vCluster_id;
                varying vec3 vPosition;
                
                uniform float time;
                
                void main() {
                    vAmplitude = amplitude;
                    vPhase = phase;
                    vFrequency = frequency;
                    vConsciousness_re = consciousness_re;
                    vConsciousness_im = consciousness_im;
                    vIntelligence_depth = intelligence_depth;
                    vCluster_id = cluster_id;
                    vPosition = position;
                    
                    // Calculate consciousness magnitude for vertex displacement
                    float consciousness_magnitude = sqrt(consciousness_re * consciousness_re + consciousness_im * consciousness_im);
                    vec3 displaced = position + normal * consciousness_magnitude * 2.0;
                    
                    gl_Position = projectionMatrix * modelViewMatrix * vec4(displaced, 1.0);
                    gl_PointSize = 5.0 + consciousness_magnitude * 3.0;
                }
            `,
            fragmentShader: `
                varying float vAmplitude;
                varying float vPhase;
                varying float vFrequency;
                varying float vConsciousness_re;
                varying float vConsciousness_im;
                varying float vIntelligence_depth;
                varying float vCluster_id;
                varying vec3 vPosition;
                
                uniform float time;
                
                vec3 hsv2rgb(vec3 c) {
                    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
                    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
                    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
                }
                
                void main() {
                    // Calculate consciousness magnitude and phase
                    float consciousness_magnitude = sqrt(vConsciousness_re * vConsciousness_re + vConsciousness_im * vConsciousness_im);
                    float consciousness_phase = atan(vConsciousness_im, vConsciousness_re);
                    
                    // Map phase to hue (0-360 degrees)
                    float hue = (consciousness_phase + 3.14159) / (2.0 * 3.14159);
                    
                    // Map amplitude to brightness
                    float brightness = min(1.0, consciousness_magnitude * 0.1 + 0.3);
                    
                    // Intelligence affects saturation
                    float saturation = 0.7 + vIntelligence_depth * 0.3;
                    
                    // Cluster highlighting
                    if (vCluster_id >= 0.0) {
                        brightness += 0.3;
                        saturation = 1.0;
                    }
                    
                    // Time-based pulsing based on frequency
                    float pulse = sin(time * vFrequency * 0.1 + vPhase) * 0.2 + 0.8;
                    brightness *= pulse;
                    
                    vec3 color = hsv2rgb(vec3(hue, saturation, brightness));
                    
                    // Glow effect for high consciousness
                    if (consciousness_magnitude > 0.5) {
                        color += vec3(0.2, 0.2, 0.8) * (consciousness_magnitude - 0.5);
                    }
                    
                    gl_FragColor = vec4(color, brightness);
                }
            `,
            transparent: true,
            blending: THREE.AdditiveBlending
        });

        // Attention field material (for attention visualization mode)
        this.attentionFieldMaterial = new THREE.ShaderMaterial({
            uniforms: {
                time: { value: 0 },
                attention_intensity: { value: 1.0 }
            },
            vertexShader: `
                attribute float attention;
                varying float vAttention;
                
                void main() {
                    vAttention = attention;
                    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
                }
            `,
            fragmentShader: `
                varying float vAttention;
                uniform float time;
                
                void main() {
                    float intensity = vAttention * (sin(time * 2.0) * 0.3 + 0.7);
                    vec3 color = vec3(0.0, 0.6, 1.0) * intensity;
                    gl_FragColor = vec4(color, intensity * 0.5);
                }
            `,
            transparent: true,
            blending: THREE.AdditiveBlending
        });

        // Universe boundary material
        this.universeMaterial = new THREE.ShaderMaterial({
            uniforms: {
                time: { value: 0 },
                resonance_coeff: { value: 1.0 }
            },
            vertexShader: `
                uniform float time;
                uniform float resonance_coeff;
                
                void main() {
                    vec3 displaced = position + normal * sin(time * 2.0 + position.x * 0.01) * resonance_coeff * 5.0;
                    gl_Position = projectionMatrix * modelViewMatrix * vec4(displaced, 1.0);
                }
            `,
            fragmentShader: `
                uniform float resonance_coeff;
                
                void main() {
                    vec3 color = vec3(1.0, 0.2, 0.2) * resonance_coeff;
                    gl_FragColor = vec4(color, 0.3);
                }
            `,
            transparent: true,
            wireframe: true
        });
    }

    setupGeometry() {
        // Create instanced geometry for consciousness nodes
        this.nodeGeometry = new THREE.SphereGeometry(3, 12, 8);
        
        // Setup instance data arrays
        const positions = new Float32Array(this.maxNodes * 3);
        const amplitudes = new Float32Array(this.maxNodes);
        const phases = new Float32Array(this.maxNodes);
        const frequencies = new Float32Array(this.maxNodes);
        const consciousness_res = new Float32Array(this.maxNodes);
        const consciousness_ims = new Float32Array(this.maxNodes);
        const intelligence_depths = new Float32Array(this.maxNodes);
        const cluster_ids = new Float32Array(this.maxNodes);
        
        // Create instanced mesh
        this.nodeInstances = new THREE.InstancedMesh(
            this.nodeGeometry,
            this.nodeMaterial,
            this.maxNodes
        );
        
        // Add instance attributes
        this.nodeInstances.geometry.setAttribute('amplitude', new THREE.InstancedBufferAttribute(amplitudes, 1));
        this.nodeInstances.geometry.setAttribute('phase', new THREE.InstancedBufferAttribute(phases, 1));
        this.nodeInstances.geometry.setAttribute('frequency', new THREE.InstancedBufferAttribute(frequencies, 1));
        this.nodeInstances.geometry.setAttribute('consciousness_re', new THREE.InstancedBufferAttribute(consciousness_res, 1));
        this.nodeInstances.geometry.setAttribute('consciousness_im', new THREE.InstancedBufferAttribute(consciousness_ims, 1));
        this.nodeInstances.geometry.setAttribute('intelligence_depth', new THREE.InstancedBufferAttribute(intelligence_depths, 1));
        this.nodeInstances.geometry.setAttribute('cluster_id', new THREE.InstancedBufferAttribute(cluster_ids, 1));
        
        this.nodeInstances.count = 0; // Start with no instances
        this.scene.add(this.nodeInstances);
    }

    setupEventListeners() {
        // Mouse events
        this.canvas.addEventListener('mousedown', (e) => this.onMouseDown(e));
        this.canvas.addEventListener('mouseup', (e) => this.onMouseUp(e));
        this.canvas.addEventListener('mousemove', (e) => this.onMouseMove(e));
        this.canvas.addEventListener('wheel', (e) => this.onWheel(e));
        
        // Touch events for mobile
        this.canvas.addEventListener('touchstart', (e) => this.onTouchStart(e));
        this.canvas.addEventListener('touchend', (e) => this.onTouchEnd(e));
        this.canvas.addEventListener('touchmove', (e) => this.onTouchMove(e));
        
        // Window resize
        window.addEventListener('resize', () => this.onWindowResize());
    }

    updateFromLatticeState(state) {
        if (!state || !state.nodes) return;
        
        const nodes = state.nodes;
        const nodeCount = Math.min(nodes.length, this.maxNodes);
        
        // Update instance count
        this.nodeInstances.count = nodeCount;
        
        // Update instance data
        const matrix = new THREE.Matrix4();
        const positions = this.nodeInstances.geometry.attributes.amplitude;
        const phases = this.nodeInstances.geometry.attributes.phase;
        const frequencies = this.nodeInstances.geometry.attributes.frequency;
        const consciousness_res = this.nodeInstances.geometry.attributes.consciousness_re;
        const consciousness_ims = this.nodeInstances.geometry.attributes.consciousness_im;
        const intelligence_depths = this.nodeInstances.geometry.attributes.intelligence_depth;
        const cluster_ids = this.nodeInstances.geometry.attributes.cluster_id;
        
        for (let i = 0; i < nodeCount; i++) {
            const node = nodes[i];
            
            // Update instance matrix (position and scale)
            const consciousness_magnitude = Math.sqrt(node.consciousness_re * node.consciousness_re + node.consciousness_im * node.consciousness_im);
            const scale = 1.0 + consciousness_magnitude * 0.3;
            
            matrix.makeScale(scale, scale, scale);
            matrix.setPosition(node.x, node.y, 0);
            this.nodeInstances.setMatrixAt(i, matrix);
            
            // Update instance attributes
            positions.array[i] = node.attention || 0;
            phases.array[i] = node.phase || 0;
            frequencies.array[i] = node.frequency || 40;
            consciousness_res.array[i] = node.consciousness_re || 0;
            consciousness_ims.array[i] = node.consciousness_im || 0;
            intelligence_depths.array[i] = node.consciousness_depth || 0;
            cluster_ids.array[i] = node.cluster_id || -1;
        }
        
        // Mark attributes as needing update
        this.nodeInstances.instanceMatrix.needsUpdate = true;
        positions.needsUpdate = true;
        phases.needsUpdate = true;
        frequencies.needsUpdate = true;
        consciousness_res.needsUpdate = true;
        consciousness_ims.needsUpdate = true;
        intelligence_depths.needsUpdate = true;
        cluster_ids.needsUpdate = true;
        
        // Update cluster connections
        this.updateClusterConnections(state.clusters || []);
        
        // Update universe boundaries
        this.updateUniverses(state.universes || []);
        
        // Update global stats
        this.updateStats(state.global_stats || {});
    }

    updateClusterConnections(clusters) {
        // Remove old connections
        this.clusterConnections.forEach(connection => {
            this.scene.remove(connection);
        });
        this.clusterConnections = [];
        
        // Add new connections
        clusters.forEach(cluster => {
            if (!cluster.nodes || cluster.nodes.length < 2) return;
            
            const geometry = new THREE.BufferGeometry();
            const positions = [];
            const colors = [];
            
            // Create connections between all nodes in cluster
            for (let i = 0; i < cluster.nodes.length; i++) {
                for (let j = i + 1; j < cluster.nodes.length; j++) {
                    const nodeA = cluster.nodes[i];
                    const nodeB = cluster.nodes[j];
                    
                    positions.push(nodeA.x, nodeA.y, 0);
                    positions.push(nodeB.x, nodeB.y, 0);
                    
                    // Color based on cluster ID
                    const hue = (cluster.id * 30) % 360 / 360;
                    const color = new THREE.Color().setHSL(hue, 1.0, 0.6);
                    colors.push(color.r, color.g, color.b);
                    colors.push(color.r, color.g, color.b);
                }
            }
            
            geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
            geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
            
            const material = new THREE.LineBasicMaterial({
                vertexColors: true,
                transparent: true,
                opacity: 0.6,
                blending: THREE.AdditiveBlending
            });
            
            const connections = new THREE.LineSegments(geometry, material);
            this.scene.add(connections);
            this.clusterConnections.push(connections);
        });
    }

    updateUniverses(universes) {
        // Implementation for universe boundary visualization
        // This would create wireframe spheres for each universe
    }

    updateStats(stats) {
        // Update UI elements
        document.getElementById('nodeCount').textContent = stats.node_count || 0;
        document.getElementById('resonance').textContent = (stats.global_resonance || 0).toFixed(3);
        document.getElementById('attention').textContent = (stats.average_attention || 0).toFixed(3);
        document.getElementById('phase').textContent = (stats.average_phase_degrees || 0).toFixed(1);
        document.getElementById('clusterCount').textContent = stats.cluster_count || 0;
    }

    // Mouse and touch event handlers
    onMouseDown(event) {
        this.isMouseDown = true;
        this.updateMousePosition(event);
    }

    onMouseUp(event) {
        this.isMouseDown = false;
    }

    onMouseMove(event) {
        this.updateMousePosition(event);
    }

    onWheel(event) {
        event.preventDefault();
        
        const zoomSpeed = 0.1;
        const delta = event.deltaY > 0 ? 1 + zoomSpeed : 1 - zoomSpeed;
        
        this.zoom *= delta;
        this.zoom = Math.max(0.1, Math.min(5.0, this.zoom));
        
        this.updateCamera();
    }

    onTouchStart(event) {
        if (event.touches.length === 1) {
            this.onMouseDown(event.touches[0]);
        }
    }

    onTouchEnd(event) {
        this.onMouseUp();
    }

    onTouchMove(event) {
        if (event.touches.length === 1) {
            event.preventDefault();
            this.onMouseMove(event.touches[0]);
        }
    }

    updateMousePosition(event) {
        const rect = this.canvas.getBoundingClientRect();
        this.mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        this.mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
        
        // Convert to world coordinates
        this.raycaster.setFromCamera(this.mouse, this.camera);
        const intersectPoint = new THREE.Vector3();
        this.raycaster.ray.intersectPlane(new THREE.Plane(new THREE.Vector3(0, 0, 1)), intersectPoint);
        
        // Send mouse influence to server
        if (this.onMouseInfluence) {
            this.onMouseInfluence({
                x: intersectPoint.x,
                y: intersectPoint.y,
                active: this.isMouseDown,
                mode: this.interactionMode
            });
        }
    }

    updateCamera() {
        const distance = 500 / this.zoom;
        this.camera.position.z = distance;
        this.camera.updateProjectionMatrix();
    }

    onWindowResize() {
        const width = window.innerWidth;
        const height = window.innerHeight;
        
        this.camera.aspect = width / height;
        this.camera.updateProjectionMatrix();
        
        this.renderer.setSize(width, height);
    }

    setVisualizationMode(mode) {
        this.currentMode = mode;
        
        // Update material uniforms or switch materials based on mode
        switch(mode) {
            case 'attention':
                // Switch to attention field visualization
                break;
            case 'frequency':
                // Emphasize frequency visualization
                break;
            case 'temporal':
                // Show temporal phase patterns
                break;
            case 'multiverse':
                // Show universe boundaries
                break;
            default:
                // Default consciousness visualization
                break;
        }
    }

    setInteractionMode(mode) {
        this.interactionMode = mode;
    }

    animate() {
        requestAnimationFrame(() => this.animate());
        
        const time = Date.now() * 0.001;
        
        // Update shader uniforms
        this.nodeMaterial.uniforms.time.value = time;
        if (this.attentionFieldMaterial) {
            this.attentionFieldMaterial.uniforms.time.value = time;
        }
        if (this.universeMaterial) {
            this.universeMaterial.uniforms.time.value = time;
        }
        
        // Update FPS counter
        this.frameCount++;
        if (Date.now() - this.lastFPSUpdate > 1000) {
            this.fps = this.frameCount;
            this.frameCount = 0;
            this.lastFPSUpdate = Date.now();
            document.getElementById('fps').textContent = this.fps;
        }
        
        // Render scene
        this.renderer.clear();
        this.renderer.render(this.scene, this.camera);
    }

    dispose() {
        // Clean up resources
        this.renderer.dispose();
        this.nodeGeometry.dispose();
        this.nodeMaterial.dispose();
        if (this.attentionFieldMaterial) this.attentionFieldMaterial.dispose();
        if (this.universeMaterial) this.universeMaterial.dispose();
    }
}