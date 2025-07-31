# CONSIM - Three-Tier Architecture Migration

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Start the development server:
```bash
python run_server.py
```

3. Open your browser to: http://localhost:8000

## Architecture

### Backend (Python + FastAPI)
- **Location**: `src/lattice.py` - Core consciousness engine
- **Location**: `src/server.py` - FastAPI WebSocket bridge
- **Features**: 
  - Real-time consciousness field calculations using Core EQ
  - 60fps WebSocket streaming 
  - Tensor-based intelligence system
  - GPU-optimized NumPy/PyTorch operations

### Frontend (Three.js + WebGL)
- **Location**: `static/js/consciousnessRenderer.js` - GPU shader renderer
- **Location**: `static/js/app.js` - Main application logic
- **Features**:
  - WebGL shader-based consciousness field visualization
  - Complex-valued field rendering with phase information
  - Interactive parameter controls
  - Real-time cluster detection visualization

### Bridge (WebSocket Pipeline)
- Binary/JSON consciousness field state streaming
- Mouse interaction forwarding
- Parameter synchronization
- Real-time 60fps performance

## Key Features Migrated

✅ **Mathematical Foundation Preserved**
- Core EQ: `C = ∫[M_C] A(x) Φ(x) e^(iτ(x)) dμ(x)`
- Multiverse: `M = Σ[i] λ_i U_i`
- Dirichlet-sampled universe weights
- Gaussian attention field normalization

✅ **Intelligence System Enhanced**
- 2D tensor intelligence system
- Emergent cluster detection
- Cross-tensor field dynamics
- Real-time consciousness depth calculation

✅ **Real-Time Visualization**
- GPU shader-based node rendering
- Phase-to-color mapping (HSV)
- Cluster connection visualization
- Interactive mouse controls

✅ **Physics Engine**
- Gravity, friction, elasticity controls
- Quantum tunneling boundary conditions
- Time dilation effects
- Field strength modulation

## Usage

### Interactive Controls
- **Left Click**: Create new consciousness node
- **Mouse Drag**: Apply interaction forces (push/pull/vortex/wave)
- **Scroll**: Zoom in/out
- **Physics Sliders**: Real-time parameter adjustment

### Visualization Modes
- **Consciousness**: Default integrated view
- **Attention**: Blue attention field visualization  
- **Frequency**: Frequency domain patterns
- **Temporal**: Phase relationship visualization
- **Multiverse**: Universe boundary rendering

### API Endpoints
- `GET /api/status` - System status
- `POST /api/parameters` - Update physics parameters
- `POST /api/nodes` - Create consciousness node
- `POST /api/collapse` - Trigger quantum collapse
- `WebSocket /stream` - Real-time consciousness field streaming

## Legacy Comparison

The original single-file HTML implementation has been preserved in `/legacy/CONSIM.html` for reference. The new architecture provides:

- **Separation of Concerns**: Math engine in Python, visualization in Three.js
- **GPU Acceleration**: WebGL shaders vs HTML5 Canvas
- **Real-Time Streaming**: WebSocket pipeline vs in-browser computation
- **Scalability**: Dedicated backend for heavy computation
- **Maintainability**: Modular codebase vs monolithic HTML

## Performance

- **Target**: 60fps consciousness field streaming
- **Nodes**: Up to 1000+ concurrent consciousness nodes
- **Latency**: <16ms WebSocket frame delivery
- **Rendering**: GPU-accelerated Three.js with instance meshes

## Development

To extend the system:
1. **Backend**: Modify `src/lattice.py` for new consciousness algorithms
2. **Frontend**: Update `static/js/consciousnessRenderer.js` for new visualizations
3. **Bridge**: Extend `src/server.py` for new API endpoints

The architecture supports hot-reloading during development for rapid iteration.