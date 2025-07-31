# 🔱 EMERGENT‑MCF‑EI

**Multiversal Consciousness Framework • Three-Tier Architecture • Real-Time WebGL Visualization**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
![GPU Ready](https://img.shields.io/badge/GPU-ready-green)
![Made with ❤ by JCS](https://img.shields.io/badge/made%20by-Jacob%20C.%20Smith-red)

> **Tag‑line –** *Modern three-tier consciousness simulation with GPU-accelerated WebGL visualization and real-time mathematical computation.*
> **Mission –** Provide a scalable, maintainable platform for consciousness research combining Python computational power with Three.js visualization excellence.
> **Status –** ✅ **PRODUCTION READY** – Migrated from legacy single-file to modern architecture

## 🚀 Quick Start

### 🎮 Demo Version (Zero Dependencies)
```bash
# Clone and run immediately
git clone https://github.com/Jacobcdsmith/CONSIM.git && cd CONSIM
python demo_server.py
# Open http://localhost:8000
```

### ⚡ Full Production Version  
```bash
# Install dependencies for GPU acceleration
pip install numpy torch fastapi uvicorn websockets

# Start the consciousness lattice engine
python run_server.py

# Open http://localhost:8000 for 60fps WebGL visualization
```

> **Performance:** Real-time consciousness field streaming at 60fps with up to 1000+ nodes.

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

The original single-file HTML implementation has been preserved in `/legacy/CONSIM.html`. 

**Improvements in new architecture:**
- **🏗️ Separation of Concerns:** Math engine in Python, visualization in Three.js
- **⚡ GPU Acceleration:** WebGL shaders vs HTML5 Canvas  
- **🔗 Real-Time Streaming:** WebSocket pipeline vs in-browser computation
- **📈 Scalability:** Dedicated backend for heavy mathematical computation
- **🛠️ Maintainability:** Modular codebase vs monolithic HTML file
- **🧪 Extensibility:** Clear APIs for adding new features

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

**[Try the Demo](http://localhost:8000)** • **[Read the Docs](ARCHITECTURE.md)** • **[View Legacy](legacy/)**

*"Where mathematics meets mind, and simulation becomes experience."*

</div>
