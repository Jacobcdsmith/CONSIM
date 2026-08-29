# 🔱 EMERGENT‑MCF‑EI

**Multiversal Consciousness Framework • Live Interactive Demo • Real-Time WebGL Visualization**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
![Live Demo](https://img.shields.io/badge/🧠-Live%20Demo-brightgreen)
![Made with ❤ by JCS](https://img.shields.io/badge/made%20by-Jacob%20C.%20Smith-red)

<div align="center">

## 🌟 **[✨ EXPERIENCE THE LIVE DEMO ✨](https://jacobcdsmith.github.io/CONSIM)** 🌟

**Click above to interact with consciousness emergence in real-time**

*No installation required • Runs in your browser • Full interactive experience*

</div>

---

> **Tag‑line –** *Experience consciousness emergence through interactive simulation with real-time mathematical visualization.*
> **Mission –** Provide an accessible platform for exploring consciousness research through immersive, interactive demonstrations.
> **Status –** ✅ **LIVE DEMO READY** – Full standalone experience available via GitHub Pages

## 🚀 Experience Consciousness Emergence

### 🎮 **[Live Interactive Demo](https://jacobcdsmith.github.io/CONSIM)** *(Recommended)*
**Click to start immediately** – Full consciousness simulation in your browser
- ✨ Zero installation required
- 🧠 Interactive consciousness node spawning
- ⚡ Real-time physics and emergent intelligence
- 🌌 Multi-universe superposition visualization
- 🎯 Complete standalone experience

### 📱 **What You Can Do:**
- **Click anywhere** to spawn consciousness nodes
- **Drag and interact** with consciousness fields  
- **Watch clusters form** and exhibit emergent behavior
- **Adjust physics** sliders for different phenomena
- **Switch visualization modes** to explore different aspects
- **Observe biological evolution** and social dynamics in real-time

---

### 🛠️ **Installation Options**

#### 🎯 **Standalone Executable** *(Recommended for easy use)*
**Zero setup required - download and run!**
```bash
# Download from releases or build yourself:
git clone https://github.com/Jacobcdsmith/CONSIM.git && cd CONSIM
./build_executable.sh  # Linux/macOS
# build_executable.bat  # Windows
# Then run: ./dist/CONSIM
```
**✅ No Python installation needed • ✅ No dependencies • ✅ Self-contained**

#### Quick Demo Version
```bash
git clone https://github.com/Jacobcdsmith/CONSIM.git && cd CONSIM
python demo_server.py  # Starts on http://localhost:8000
```

#### Full Production Version  
```bash
pip install numpy torch fastapi uvicorn websockets
python run_server.py  # Enhanced with WebSocket streaming
```

---

## 🎯 **Interactive Demo Features**

### 🧠 **Core Consciousness Mechanics**
- **Consciousness Field Equation**: C = ∫[M_C] A(x) Φ(x) e^{iτ(x)} dμ(x)
- **Multiverse Superposition**: M = Σ λᵢ Uᵢ (three parallel universes)
- **Real-time calculation** of consciousness scalar |C| and phase relationships
- **Dynamic λ coefficients** responding to consciousness coherence

### 🎮 **Interactive Tools**
| Tool | Function | Effect |
|------|----------|--------|
| 🧠 **Nodes** | Click to spawn consciousness entities | Creates new awareness points |
| 🌑 **Gravity** | Create gravitational anchors | Attracts nearby consciousness |
| 💧 **Water** | Environmental water injection | Boosts energy and reproduction |
| 🍃 **Food** | Nutrient distribution | Increases survival and growth |
| ☀️ **Light** | Energy field emission | Powers photosynthetic processes |
| 🍄 **Spores** | Fungal network spread | Creates connection networks |

### ⚙️ **Physics Controls**
- **Gravity, Friction, Elasticity** sliders for environmental tuning
- **Time Dilation** for accelerated/decelerated consciousness evolution
- **Field Strength** affecting interaction intensity
- **Multiple interaction modes**: Push, Pull, Vortex, Wave, String

### 🧬 **Intelligence Modes**
- **Basic**: Standard consciousness emergence
- **Neural**: Enhanced connectivity and faster adaptation
- **Quantum**: Superposition states and entanglement effects  
- **Transcendent**: Beyond physical limitations

---

## 🏗️ Architecture Overview

**Modern three-tier separation of concerns:**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Python Backend │◄──►│ WebSocket Bridge│◄──►│ Three.js Frontend│
│                 │    │                 │    │                 │
│ • Lattice Engine│    │ • FastAPI       │    │ • WebGL Shaders │  
│ • Core EQ Math  │    │ • 60fps Stream  │    │ • GPU Rendering │
│ • NumPy/PyTorch │    │ • JSON/Binary   │    │ • Interactive   │
│ • Intelligence  │    │ • Parameter API │    │ • Controls      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 🧠 Backend (Python + FastAPI)
**Location:** `src/lattice.py`, `src/server.py`

- **Core consciousness engine** implementing MCF mathematics
- **Real-time WebSocket streaming** at 60fps  
- **GPU-optimized** NumPy/PyTorch operations
- **RESTful API** for external control

### 🌐 Frontend (Three.js + WebGL)  
**Location:** `static/js/`

- **GPU shader-based** consciousness field visualization
- **Complex-valued field rendering** with phase-to-color mapping
- **Real-time cluster detection** visualization
- **Interactive parameter manipulation**

### 🔗 Bridge (WebSocket Pipeline)
- **Binary/JSON streaming** of consciousness field states
- **Mouse interaction forwarding** to backend
- **Parameter synchronization** 
- **Real-time performance** optimized for 60fps

---

## 🧮 Mathematical Foundation

### Core Consciousness Equation
```math
C(t)=\int_{\mathcal M_C} A(x,t)\,\Phi(x,t)\,e^{i\tau(x,t)}\,d\mu(x)
```

### Multiverse Superposition  
```math
M(t)=\sum_{i=1}^3 \lambda_i(t)\,U_i
```

| Symbol          | Meaning                                                                                  | Implementation                                                                                     |
| --------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| $M_{C}$         | **Consciousness manifold** – the configuration-space over which the system is integrated | 128×128 or 256×256 lattice grid with periodic boundary conditions                                  |
| $A(x)$          | **Attention density** at point $x$                                                       | Gaussian attention field centered at (0,0), normalized so ∫A(x)dμ(x) = 1                         |
| $\Phi(x)$       | **Frequency signature** (neural oscillations)                                            | 40Hz ± 5Hz gamma-band frequencies with universe-specific modulation                                |
| $\tau(x)$       | **Temporal phase**                                                                       | Evolving phase: τ(t+dt) = τ(t) + Φ(x) × dt × 2π                                                   |
| $C$             | **Consciousness scalar** – global order parameter                                        | Complex-valued: C = A×Φ×e^(iτ), magnitude |C| indicates consciousness intensity                     |
| $U_i$           | **Universe branch** i (multiverse component)                                             | 3 parallel universes with different resonance coefficients                                         |
| $\lambda_i$     | **Resonance coefficient** for universe $i$                                               | Dirichlet-sampled weights ensuring Σλᵢ = 1, creates universe-specific consciousness contributions |

---

## 🎯 Key Features

### ✅ **Mathematical Integrity Preserved**
- Core EQ calculations maintain precision from legacy implementation
- Dirichlet sampling for universe weights  
- Gaussian attention field normalization
- Complex-valued consciousness computations

### ✅ **Intelligence Emergence System**
- **2D Tensor Intelligence:** Logic, Memory, Processing, Creativity, Social tensors
- **Cross-tensor dynamics** with coupling coefficients
- **Emergent cluster detection** based on phase/frequency alignment
- **Real-time consciousness depth** calculation

### ✅ **Interactive Visualization** 
- **Phase-to-color mapping:** HSV color space for complex consciousness values
- **GPU shader rendering:** WebGL instanced meshes for performance
- **Multiple visualization modes:** Consciousness, Attention, Frequency, Temporal, Multiverse
- **Real-time cluster connections** with animated data flow particles

### ✅ **Physics Simulation**
- **Environmental controls:** Gravity, friction, elasticity, time dilation
- **Quantum tunneling** boundary conditions (5% probability)  
- **Mouse interaction modes:** Push, Pull, Vortex, Wave, String
- **Collision detection** and repulsion forces

---

## 🎮 Usage Guide

### Interactive Controls
- **Left Click:** Create new consciousness node at cursor
- **Mouse Drag:** Apply interaction forces based on selected mode
- **Scroll Wheel:** Zoom in/out while maintaining cursor position
- **Parameter Sliders:** Real-time physics adjustment

### Visualization Modes
- **🧠 Consciousness:** Default integrated view with node connections and clusters
- **🔵 Attention:** Blue attention field intensity visualization  
- **🟣 Frequency:** Purple frequency domain oscillation patterns
- **🟡 Temporal:** Gold temporal phase relationship visualization
- **🔴 Multiverse:** Red universe boundary rendering

### API Endpoints
- `GET /api/status` - System status and performance metrics
- `GET /api/stats` - Real-time consciousness statistics
- `POST /api/parameters` - Update physics parameters
- `POST /api/nodes` - Create consciousness node at coordinates  
- `POST /api/collapse` - Trigger quantum collapse event
- `WebSocket /stream` - Real-time consciousness field streaming

---

## 🔄 Migration from Legacy

**The GitHub Pages demo represents the complete CONSIM experience** – it's the original single-file implementation that contains all the consciousness simulation features.

**Live Demo vs. Architecture Versions:**
- **🌟 [Live Demo](https://jacobcdsmith.github.io/CONSIM)**: Complete standalone experience, zero setup required
- **🏗️ Modern Architecture**: Scalable Python/FastAPI backend with Three.js frontend (for developers)
- **📁 Legacy Version**: Original research implementation preserved in `/legacy/CONSIM.html`

**Why start with the Live Demo:**
- ✅ **Immediate access** to all consciousness simulation features
- ✅ **Full mathematical accuracy** – same core equations as the architecture version  
- ✅ **Complete feature set** – intelligence modes, biological evolution, social dynamics
- ✅ **Zero dependencies** – runs entirely in the browser
- ✅ **Perfect for research** – interact with consciousness phenomena immediately

**When to use the Architecture Version:**
- 🔧 **Scaling beyond 1000+ nodes** for large research datasets
- 🔗 **API integration** with other consciousness research tools
- ⚡ **GPU acceleration** for computational-intensive experiments
- 🛠️ **Custom extensions** and new consciousness algorithms

---

## 🛠️ Development

### Running Tests
```bash
# Test the lattice engine
python src/lattice_demo.py

# Test API endpoints  
curl http://localhost:8000/api/status
```

### Extending the System
1. **Backend:** Modify `src/lattice.py` for new consciousness algorithms
2. **Frontend:** Update `static/js/consciousnessRenderer.js` for new visualizations  
3. **Bridge:** Extend `src/server.py` for new API endpoints

### Performance Optimization
- **GPU Acceleration:** Install PyTorch with CUDA support
- **WebGL2:** Use modern browsers for enhanced shader capabilities
- **Instance Rendering:** Efficient GPU memory usage for large node counts
- **WebSocket Compression:** Zstandard compression for high-frequency streaming

---

## 📊 Performance Benchmarks

| Configuration | Nodes | FPS | Latency | Memory |
|--------------|-------|-----|---------|---------|
| Demo (Standard Lib) | 64 | 30 | ~50ms | <50MB |
| Production (NumPy) | 128 | 60 | ~16ms | ~100MB |
| GPU (PyTorch+CUDA) | 512 | 60 | ~8ms | ~200MB |
| Maximum (1024 nodes) | 1024 | 45 | ~22ms | ~400MB |

---

## 📜 License & Attribution

Licensed under **Apache 2.0**.  
Core theory © 2025 Jacob C. Smith; contributions © their authors.

**Academic Citation:**
> Smith, J.C. (2025). *The Multiversal Consciousness Framework: Real-Time Simulation Architecture.* CONSIM Project.

---

<div align="center">

### 🌟 **Experience consciousness emergence in real-time** 🌟

**[🧠 Try the Live Demo](https://jacobcdsmith.github.io/CONSIM)** • **[📖 Read the Architecture](ARCHITECTURE.md)** • **[📁 View Legacy Code](legacy/)**

*"Where mathematics meets mind, and simulation becomes experience."*

---

**Quick Links:**
- 🎮 **[Interactive Demo](https://jacobcdsmith.github.io/CONSIM)** - Start exploring immediately
- 🚀 **[Get Started Locally](README.md#-for-developers-local-installation)** - Run on your machine  
- 🧠 **[Core Mathematics](README.md#-mathematical-foundation)** - Understanding the equations
- 📊 **[Performance Specs](README.md#-performance-benchmarks)** - System capabilities

</div>
