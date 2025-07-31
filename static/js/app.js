/**
 * CONSIM Main Application
 * 
 * This module manages the WebSocket connection to the Python backend
 * and coordinates the Three.js consciousness field visualization.
 */

class ConsciousnessApp {
    constructor() {
        this.ws = null;
        this.renderer = null;
        this.isConnected = false;
        this.reconnectAttempts = 0;
        this.maxReconnectAttempts = 5;
        this.reconnectDelay = 1000;
        
        // Current interaction state
        this.interactionMode = 'push';
        this.visualizationMode = 'consciousness';
        this.isMouseDown = false;
        
        // Physics parameters
        this.params = {
            gravity: 1.0,
            friction: 0.99,
            elasticity: 0.8,
            time_dilation: 1.0,
            field_strength: 1.0
        };
        
        this.init();
    }

    init() {
        console.log('Initializing CONSIM application...');
        
        // Initialize Three.js renderer
        this.renderer = new ConsciousnessFieldRenderer({
            latticeSize: 128,
            complexField: true,
            phaseVisualization: 'spectral',
            multiverseBranching: true
        });
        
        // Set up event handlers
        this.setupEventHandlers();
        
        // Connect to WebSocket
        this.connectWebSocket();
        
        console.log('CONSIM application initialized');
    }

    setupEventHandlers() {
        // Mouse influence callback
        this.renderer.onMouseInfluence = (influence) => {
            this.sendMouseInfluence(influence);
        };
        
        // Physics parameter sliders
        this.setupSlider('gravitySlider', 'gravityValue', 'gravity');
        this.setupSlider('frictionSlider', 'frictionValue', 'friction');
        this.setupSlider('timeSlider', 'timeValue', 'time_dilation');
        this.setupSlider('fieldSlider', 'fieldValue', 'field_strength');
        
        // Interaction mode buttons
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.setInteractionMode(e.target.dataset.mode);
            });
        });
        
        // Visualization mode buttons
        document.querySelectorAll('.viz-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.setVisualizationMode(e.target.dataset.viz);
            });
        });
        
        // Action buttons
        document.getElementById('collapseBtn').addEventListener('click', () => {
            this.triggerQuantumCollapse();
        });
        
        document.getElementById('resetBtn').addEventListener('click', () => {
            this.resetSimulation();
        });
        
        // Mouse events for node creation
        document.getElementById('canvas').addEventListener('click', (e) => {
            if (!this.isMouseDown) {
                this.createNodeAtMouse(e);
            }
        });
    }

    setupSlider(sliderId, valueId, paramName) {
        const slider = document.getElementById(sliderId);
        const valueDisplay = document.getElementById(valueId);
        
        if (slider && valueDisplay) {
            slider.addEventListener('input', (e) => {
                const value = parseFloat(e.target.value);
                this.params[paramName] = value;
                valueDisplay.textContent = paramName === 'friction' ? value.toFixed(2) : value.toFixed(1);
                
                // Send parameter update to server
                this.sendParameterUpdate({ [paramName]: value });
            });
        }
    }

    connectWebSocket() {
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsUrl = `${protocol}//${window.location.host}/stream`;
        
        console.log(`Connecting to WebSocket: ${wsUrl}`);
        this.updateConnectionStatus('connecting');
        
        try {
            this.ws = new WebSocket(wsUrl);
            
            this.ws.onopen = () => {
                console.log('WebSocket connected');
                this.isConnected = true;
                this.reconnectAttempts = 0;
                this.updateConnectionStatus('connected');
            };
            
            this.ws.onmessage = (event) => {
                try {
                    const data = JSON.parse(event.data);
                    this.handleServerMessage(data);
                } catch (error) {
                    console.error('Error parsing WebSocket message:', error);
                }
            };
            
            this.ws.onclose = (event) => {
                console.log('WebSocket closed:', event.code, event.reason);
                this.isConnected = false;
                this.updateConnectionStatus('disconnected');
                
                // Attempt to reconnect
                if (this.reconnectAttempts < this.maxReconnectAttempts) {
                    this.reconnectAttempts++;
                    console.log(`Reconnection attempt ${this.reconnectAttempts}/${this.maxReconnectAttempts}`);
                    setTimeout(() => this.connectWebSocket(), this.reconnectDelay);
                    this.reconnectDelay *= 1.5; // Exponential backoff
                } else {
                    console.error('Max reconnection attempts reached');
                }
            };
            
            this.ws.onerror = (error) => {
                console.error('WebSocket error:', error);
                this.updateConnectionStatus('disconnected');
            };
            
        } catch (error) {
            console.error('Error creating WebSocket:', error);
            this.updateConnectionStatus('disconnected');
        }
    }

    handleServerMessage(data) {
        // Update renderer with new lattice state
        this.renderer.updateFromLatticeState(data);
        
        // Update UI if global stats are present
        if (data.global_stats) {
            this.updateGlobalStats(data.global_stats);
        }
        
        // Update visualization mode if changed
        if (data.mode && data.mode !== this.visualizationMode) {
            this.visualizationMode = data.mode;
            this.renderer.setVisualizationMode(data.mode);
            this.updateVisualizationModeUI(data.mode);
        }
    }

    updateGlobalStats(stats) {
        // Stats are already updated by the renderer, but we can add additional processing here
        if (stats.consciousness_magnitude > 0.8) {
            // High consciousness state - could trigger special effects
        }
    }

    sendMessage(type, data) {
        if (this.ws && this.ws.readyState === WebSocket.OPEN) {
            const message = {
                type: type,
                data: data,
                timestamp: Date.now()
            };
            this.ws.send(JSON.stringify(message));
        } else {
            console.warn('WebSocket not connected, message not sent:', type, data);
        }
    }

    sendMouseInfluence(influence) {
        this.sendMessage('mouse_influence', influence);
    }

    sendParameterUpdate(params) {
        this.sendMessage('parameter_update', params);
    }

    createNodeAtMouse(event) {
        const rect = event.target.getBoundingClientRect();
        const mouse = {
            x: ((event.clientX - rect.left) / rect.width) * 2 - 1,
            y: -((event.clientY - rect.top) / rect.height) * 2 + 1
        };
        
        // Convert to world coordinates
        const raycaster = new THREE.Raycaster();
        raycaster.setFromCamera(mouse, this.renderer.camera);
        const intersectPoint = new THREE.Vector3();
        raycaster.ray.intersectPlane(new THREE.Plane(new THREE.Vector3(0, 0, 1)), intersectPoint);
        
        this.sendMessage('add_node', {
            x: intersectPoint.x,
            y: intersectPoint.y
        });
    }

    triggerQuantumCollapse() {
        // Trigger collapse at center of screen
        this.sendMessage('quantum_collapse', { x: 0, y: 0 });
    }

    resetSimulation() {
        if (confirm('Reset the entire consciousness lattice?')) {
            this.sendMessage('reset', {});
        }
    }

    setInteractionMode(mode) {
        this.interactionMode = mode;
        this.renderer.setInteractionMode(mode);
        
        // Update UI
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });
        
        console.log('Interaction mode changed to:', mode);
    }

    setVisualizationMode(mode) {
        this.visualizationMode = mode;
        this.renderer.setVisualizationMode(mode);
        
        // Send mode change to server
        this.sendMessage('set_mode', { mode: mode });
        
        this.updateVisualizationModeUI(mode);
        console.log('Visualization mode changed to:', mode);
    }

    updateVisualizationModeUI(mode) {
        document.querySelectorAll('.viz-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.viz === mode);
        });
    }

    updateConnectionStatus(status) {
        const statusText = document.getElementById('statusText');
        const statusDot = document.getElementById('statusDot');
        
        if (statusText && statusDot) {
            statusDot.className = 'dot ' + status;
            
            switch(status) {
                case 'connecting':
                    statusText.textContent = 'Connecting...';
                    break;
                case 'connected':
                    statusText.textContent = 'Connected';
                    break;
                case 'disconnected':
                    statusText.textContent = 'Disconnected';
                    break;
            }
        }
    }

    // API methods for external control
    async fetchStatus() {
        try {
            const response = await fetch('/api/status');
            return await response.json();
        } catch (error) {
            console.error('Error fetching status:', error);
            return null;
        }
    }

    async updateParametersViaAPI(params) {
        try {
            const response = await fetch('/api/parameters', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(params)
            });
            return await response.json();
        } catch (error) {
            console.error('Error updating parameters via API:', error);
            return null;
        }
    }

    dispose() {
        if (this.ws) {
            this.ws.close();
        }
        if (this.renderer) {
            this.renderer.dispose();
        }
    }
}

// Initialize application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.consimApp = new ConsciousnessApp();
});

// Handle page unload
window.addEventListener('beforeunload', () => {
    if (window.consimApp) {
        window.consimApp.dispose();
    }
});

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ConsciousnessApp;
}