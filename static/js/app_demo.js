/**
 * CONSIM Demo Application - HTTP Polling Version
 * 
 * This is a simplified version that uses HTTP polling instead of WebSockets
 * for environments where full dependencies aren't available.
 */

class ConsciousnessApp {
    constructor() {
        this.renderer = null;
        this.isRunning = false;
        this.pollInterval = null;
        this.pollDelay = 100; // 10fps polling for demo
        
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
        console.log('Initializing CONSIM demo application...');
        
        // Check if Three.js is available
        if (typeof THREE === 'undefined') {
            console.warn('Three.js not loaded, using fallback 2D renderer');
            this.initFallbackRenderer();
        } else {
            // Initialize Three.js renderer
            this.renderer = new ConsciousnessFieldRenderer({
                latticeSize: 64,
                complexField: true,
                phaseVisualization: 'spectral',
                multiverseBranching: true
            });
            
            // Set up mouse influence callback
            this.renderer.onMouseInfluence = (influence) => {
                // In demo mode, we can't send real-time mouse data
                // but we can create nodes on click
            };
        }
        
        // Set up event handlers
        this.setupEventHandlers();
        
        // Start polling for updates
        this.startPolling();
        
        // Update connection status
        this.updateConnectionStatus('connected');
        
        console.log('CONSIM demo application initialized');
    }

    initFallbackRenderer() {
        // Simple 2D Canvas fallback renderer
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        
        this.fallbackRenderer = {
            canvas: canvas,
            ctx: ctx,
            width: window.innerWidth,
            height: window.innerHeight,
            
            updateFromLatticeState: (state) => {
                if (!state || !state.nodes) return;
                
                // Clear canvas
                ctx.fillStyle = 'rgba(10, 10, 26, 0.1)';
                ctx.fillRect(0, 0, this.fallbackRenderer.width, this.fallbackRenderer.height);
                
                // Draw nodes
                const centerX = this.fallbackRenderer.width / 2;
                const centerY = this.fallbackRenderer.height / 2;
                const scale = 0.5;
                
                state.nodes.forEach(node => {
                    const x = centerX + node.x * scale;
                    const y = centerY + node.y * scale;
                    const radius = node.radius || 3;
                    
                    // Calculate consciousness magnitude for color
                    const magnitude = Math.sqrt((node.consciousness_re || 0)**2 + (node.consciousness_im || 0)**2);
                    const phase = Math.atan2(node.consciousness_im || 0, node.consciousness_re || 0);
                    
                    // Map phase to hue
                    const hue = (phase + Math.PI) / (2 * Math.PI) * 360;
                    const saturation = 70 + (node.consciousness_depth || 0) * 30;
                    const lightness = 30 + magnitude * 20;
                    
                    ctx.fillStyle = `hsl(${hue}, ${saturation}%, ${lightness}%)`;
                    ctx.shadowColor = ctx.fillStyle;
                    ctx.shadowBlur = 10;
                    
                    ctx.beginPath();
                    ctx.arc(x, y, radius, 0, Math.PI * 2);
                    ctx.fill();
                    
                    ctx.shadowBlur = 0;
                });
                
                // Draw cluster connections
                if (state.clusters) {
                    state.clusters.forEach(cluster => {
                        if (!cluster.nodes || cluster.nodes.length < 2) return;
                        
                        ctx.strokeStyle = `hsl(${(cluster.id * 60) % 360}, 80%, 50%)`;
                        ctx.lineWidth = 1;
                        ctx.globalAlpha = 0.5;
                        
                        for (let i = 0; i < cluster.nodes.length; i++) {
                            for (let j = i + 1; j < cluster.nodes.length; j++) {
                                const nodeA = cluster.nodes[i];
                                const nodeB = cluster.nodes[j];
                                
                                const x1 = centerX + nodeA.x * scale;
                                const y1 = centerY + nodeA.y * scale;
                                const x2 = centerX + nodeB.x * scale;
                                const y2 = centerY + nodeB.y * scale;
                                
                                ctx.beginPath();
                                ctx.moveTo(x1, y1);
                                ctx.lineTo(x2, y2);
                                ctx.stroke();
                            }
                        }
                        
                        ctx.globalAlpha = 1;
                    });
                }
            }
        };
        
        // Resize handler
        const resizeCanvas = () => {
            this.fallbackRenderer.width = canvas.width = window.innerWidth;
            this.fallbackRenderer.height = canvas.height = window.innerHeight;
        };
        
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
    }

    setupEventHandlers() {
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
            this.createNodeAtMouse(e);
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

    async startPolling() {
        this.isRunning = true;
        
        // First update the lattice
        await this.updateLattice();
        
        // Start polling loop
        this.pollInterval = setInterval(async () => {
            if (this.isRunning) {
                await this.fetchAndUpdateState();
                await this.updateLattice();
            }
        }, this.pollDelay);
    }

    stopPolling() {
        this.isRunning = false;
        if (this.pollInterval) {
            clearInterval(this.pollInterval);
            this.pollInterval = null;
        }
    }

    async fetchAndUpdateState() {
        try {
            const response = await fetch('/api/state');
            if (response.ok) {
                const state = await response.json();
                
                // Update renderer
                if (this.renderer && this.renderer.updateFromLatticeState) {
                    this.renderer.updateFromLatticeState(state);
                } else if (this.fallbackRenderer) {
                    this.fallbackRenderer.updateFromLatticeState(state);
                }
                
                // Update stats
                if (state.global_stats) {
                    this.updateStats(state.global_stats);
                }
            }
        } catch (error) {
            console.error('Error fetching state:', error);
            this.updateConnectionStatus('disconnected');
        }
    }

    async updateLattice() {
        try {
            const response = await fetch('/api/update', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({})
            });
            
            if (!response.ok) {
                throw new Error('Update failed');
            }
        } catch (error) {
            console.error('Error updating lattice:', error);
        }
    }

    updateStats(stats) {
        // Update UI elements
        document.getElementById('nodeCount').textContent = stats.node_count || 0;
        document.getElementById('resonance').textContent = (stats.global_resonance || 0).toFixed(3);
        document.getElementById('attention').textContent = (stats.average_attention || 0).toFixed(3);
        document.getElementById('phase').textContent = (stats.average_phase_degrees || 0).toFixed(1);
        document.getElementById('clusterCount').textContent = stats.cluster_count || 0;
        document.getElementById('fps').textContent = Math.round(1000 / this.pollDelay);
    }

    async sendParameterUpdate(params) {
        try {
            await fetch('/api/parameters', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(params)
            });
        } catch (error) {
            console.error('Error updating parameters:', error);
        }
    }

    async createNodeAtMouse(event) {
        const rect = event.target.getBoundingClientRect();
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const scale = 0.5;
        
        // Convert to world coordinates
        const worldX = (event.clientX - rect.left - centerX) / scale;
        const worldY = (event.clientY - rect.top - centerY) / scale;
        
        try {
            await fetch('/api/nodes', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ x: worldX, y: worldY })
            });
            console.log(`Node created at (${worldX.toFixed(1)}, ${worldY.toFixed(1)})`);
        } catch (error) {
            console.error('Error creating node:', error);
        }
    }

    async triggerQuantumCollapse() {
        try {
            await fetch('/api/collapse', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ x: 0, y: 0 })
            });
            console.log('Quantum collapse triggered');
        } catch (error) {
            console.error('Error triggering collapse:', error);
        }
    }

    async resetSimulation() {
        if (confirm('Reset the entire consciousness lattice?')) {
            try {
                await fetch('/api/reset', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({})
                });
                console.log('Simulation reset');
            } catch (error) {
                console.error('Error resetting simulation:', error);
            }
        }
    }

    setInteractionMode(mode) {
        this.interactionMode = mode;
        if (this.renderer && this.renderer.setInteractionMode) {
            this.renderer.setInteractionMode(mode);
        }
        
        // Update UI
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });
        
        console.log('Interaction mode changed to:', mode);
    }

    setVisualizationMode(mode) {
        this.visualizationMode = mode;
        if (this.renderer && this.renderer.setVisualizationMode) {
            this.renderer.setVisualizationMode(mode);
        }
        
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
                    statusText.textContent = 'Connected (Demo)';
                    break;
                case 'disconnected':
                    statusText.textContent = 'Disconnected';
                    break;
            }
        }
    }

    dispose() {
        this.stopPolling();
        if (this.renderer && this.renderer.dispose) {
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