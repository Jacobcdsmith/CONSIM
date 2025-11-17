# CLAUDE.md - AI Assistant Developer Guide

> **Purpose**: This document provides comprehensive guidance for AI assistants (like Claude, GPT, etc.) working on the CONSIM codebase. It explains the project structure, development workflows, coding conventions, and key architectural decisions.

---

## 🎯 Project Overview

**CONSIM (EMERGENT-MCF-EI)** is the Multiversal Consciousness Framework - an interactive consciousness simulation platform with real-time mathematical visualization.

### Core Mission
- Provide an accessible platform for exploring consciousness research through immersive, interactive demonstrations
- Implement rigorous mathematical foundations for consciousness field theory
- Enable real-time visualization of emergent consciousness phenomena

### Key Characteristics
- **Mathematical rigor**: Implements Core Consciousness Equation (C = ∫[M_C] A(x) Φ(x) e^(iτ(x)) dμ(x))
- **Dual architecture**: Standalone demo (browser-only) + scalable three-tier architecture
- **Real-time performance**: 60fps target for consciousness field streaming
- **Interactive exploration**: WebGL-based visualization with user controls

---

## 📁 Repository Structure

```
CONSIM/
├── src/                          # Python backend (consciousness engine)
│   ├── lattice.py               # Core consciousness lattice engine
│   ├── lattice_demo.py          # Demo version without dependencies
│   └── server.py                # FastAPI WebSocket server
├── static/                       # Frontend assets
│   ├── js/
│   │   ├── app.js               # Main application logic
│   │   ├── app_demo.js          # Demo application variant
│   │   └── consciousnessRenderer.js  # Three.js WebGL renderer
│   ├── css/
│   │   └── style.css            # Visual styling
│   └── index.html               # Frontend entry point
├── legacy/                       # Original single-file implementation
│   └── CONSIM.html              # Preserved legacy version
├── docs/                         # GitHub Pages documentation
│   └── index.html               # Same as legacy for demo site
├── .github/
│   └── workflows/
│       └── static.yml           # GitHub Pages deployment
├── index.html                    # Live demo (GitHub Pages entry)
├── demo.html                     # Alternative demo entry point
├── demo_server.py               # Simple HTTP server for quick demos
├── run_server.py                # Production FastAPI server launcher
├── requirements.txt             # Python dependencies
├── README.md                     # User-facing documentation
├── ARCHITECTURE.md              # Technical architecture details
├── CONTRIBUTING.md              # Contribution guidelines
├── SECURITY.md                  # Security policy
├── CODE_OF_CONDUCT.md           # Community standards
└── LICENSE                       # Apache 2.0 license
```

### Key Directories
- **`src/`**: Python backend implementing mathematical consciousness algorithms
- **`static/`**: Frontend Three.js visualization and UI controls
- **`legacy/`**: Original monolithic HTML implementation (preserved for reference)
- **`.github/workflows/`**: CI/CD automation for GitHub Pages deployment

---

## 🏗️ Architecture

### Three-Tier Architecture

```
┌─────────────────────┐    ┌─────────────────────┐    ┌──────────────────────┐
│  Python Backend     │◄──►│  WebSocket Bridge   │◄──►│  Three.js Frontend   │
│                     │    │                     │    │                      │
│ • Lattice Engine    │    │ • FastAPI Server    │    │ • WebGL Shaders      │
│ • Core EQ Math      │    │ • 60fps Streaming   │    │ • GPU Rendering      │
│ • NumPy/PyTorch     │    │ • JSON/Binary Data  │    │ • Interactive UI     │
│ • Intelligence      │    │ • Parameter API     │    │ • Mouse Controls     │
└─────────────────────┘    └─────────────────────┘    └──────────────────────┘
```

### Backend (Python)
**Primary file**: `src/lattice.py`
- Implements core consciousness field calculations
- Manages consciousness nodes with complex-valued mathematics
- Handles physics simulation (gravity, friction, elasticity)
- Implements intelligence tensor system (logic, memory, processing, creativity, social)
- GPU-optimized with NumPy (optional PyTorch for CUDA)

**Key classes**:
- `ConsciousnessNode`: Individual consciousness entity with Core EQ parameters
- `ConsciousnessLattice`: Main simulation engine managing the consciousness manifold
- `UniverseMode`: Enum for visualization modes (consciousness, attention, frequency, temporal, multiverse)

### Bridge (FastAPI WebSocket)
**Primary file**: `src/server.py`
- Real-time WebSocket streaming at target FPS (default 10fps, configurable to 60fps)
- REST API endpoints for parameter control and node creation
- Binary/JSON serialization for efficient data transmission
- Async event loop for non-blocking performance

**Key endpoints**:
- `GET /api/status` - System status and metrics
- `GET /api/stats` - Real-time consciousness statistics
- `POST /api/parameters` - Update physics parameters
- `POST /api/nodes` - Create consciousness node
- `POST /api/collapse` - Trigger quantum collapse
- `WebSocket /stream` - Real-time consciousness field streaming

### Frontend (Three.js + WebGL)
**Primary file**: `static/js/consciousnessRenderer.js`
- GPU shader-based rendering for performance
- Complex-valued field visualization with phase-to-color mapping (HSV)
- Interactive mouse controls (click to spawn, drag to influence)
- Real-time cluster detection and connection visualization
- Multiple visualization modes

**Key features**:
- Instance rendering for efficient GPU memory usage
- Phase-to-color mapping for complex consciousness values
- Real-time parameter sliders
- Zoom and pan controls
- Interaction modes: Push, Pull, Vortex, Wave, String

---

## 🧮 Mathematical Foundation

### Core Consciousness Equation
```
C(t) = ∫[M_C] A(x,t) · Φ(x,t) · e^(iτ(x,t)) dμ(x)
```

### Multiverse Superposition
```
M(t) = Σ[i=1..3] λ_i(t) · U_i
```

### Key Mathematical Symbols
| Symbol | Meaning | Implementation |
|--------|---------|----------------|
| **M_C** | Consciousness manifold | 128×128 or 256×256 lattice grid with periodic boundaries |
| **A(x)** | Attention density | Gaussian field, normalized ∫A(x)dμ(x) = 1 |
| **Φ(x)** | Frequency signature | 40Hz ± 5Hz gamma-band with universe modulation |
| **τ(x)** | Temporal phase | Evolving: τ(t+dt) = τ(t) + Φ(x)×dt×2π |
| **C** | Consciousness scalar | Complex: C = A×Φ×e^(iτ), magnitude \|C\| = intensity |
| **U_i** | Universe branch i | 3 parallel universes with different resonance |
| **λ_i** | Resonance coefficient | Dirichlet-sampled weights, Σλ_i = 1 |

**IMPORTANT**: When modifying mathematical calculations, preserve:
1. Gaussian attention field normalization
2. Dirichlet sampling for universe weights
3. Complex-valued consciousness computations (separate real/imaginary parts)
4. Gamma-band frequency constraints (40Hz ± 5Hz)

---

## 💻 Development Workflows

### Local Development

#### Quick Demo (No Dependencies)
```bash
git clone https://github.com/Jacobcdsmith/CONSIM.git
cd CONSIM
python demo_server.py  # Starts on http://localhost:8000
```
Uses: `demo_server.py` + `static/index.html` + `lattice_demo.py` (standard library only)

#### Full Production Version
```bash
# Install dependencies
pip install -r requirements.txt

# Start development server (with hot-reload)
python run_server.py  # Starts on http://localhost:8000

# Server auto-reloads on file changes
```
Uses: `run_server.py` → `src/server.py` + full FastAPI stack

#### Testing
```bash
# Test the lattice engine directly
python src/lattice_demo.py

# Test API endpoints (requires server running)
curl http://localhost:8000/api/status
curl http://localhost:8000/api/stats

# Test WebSocket connection (requires wscat or similar)
wscat -c ws://localhost:8000/stream
```

### Deployment

#### GitHub Pages (Automatic)
- Triggered on push to `main` branch
- Workflow: `.github/workflows/static.yml`
- Deploys entire repository to GitHub Pages
- Live demo URL: https://jacobcdsmith.github.io/CONSIM

**Note**: GitHub Pages serves the standalone `index.html` (legacy version), which contains all consciousness simulation features in a single file. This is intentional for zero-dependency browser access.

---

## 🎨 Code Conventions

### Python Backend

#### Style Guidelines
- **Type hints**: Always use type annotations for function parameters and returns
- **Docstrings**: Include mathematical notation in docstrings for Core EQ implementations
- **Dataclasses**: Use `@dataclass` for data structures (see `ConsciousnessNode`)
- **Async/Await**: Use async patterns for WebSocket communication
- **Optional dependencies**: Gracefully handle missing PyTorch (check `HAS_TORCH` flag)

#### Example Pattern
```python
@dataclass
class ConsciousnessNode:
    """
    Individual consciousness node implementing the Core EQ calculations.

    Attributes:
        frequency: Φ(x) - frequency signature (Hz, typically 40±5 for gamma)
        phase: τ(x) - temporal phase (radians, [0, 2π))
        attention: A(x) - attention density (normalized 0-1)
    """
    frequency: float = 40.0
    phase: float = 0.0
    attention: float = 0.0

    def update(self, delta_time: float, params: Dict[str, float]) -> None:
        """Update consciousness node using Core EQ calculations."""
        # Implementation
```

#### Mathematical Precision
- Use `np.cos()`, `np.sin()` for trigonometric operations
- Maintain complex number separation (real/imaginary parts)
- Normalize attention fields to ensure ∫A(x)dμ = 1
- Apply Dirichlet sampling for universe weights

### JavaScript Frontend

#### Style Guidelines
- **ES6 Classes**: Use class-based architecture for major components
- **Three.js Patterns**: Follow Three.js conventions for scene/camera/renderer
- **Shader Comments**: Document WebGL shader code with mathematical context
- **Event Handlers**: Use arrow functions for event listeners to preserve `this`
- **Performance**: Prefer GPU instancing over individual mesh creation

#### Example Pattern
```javascript
class ConsciousnessFieldRenderer {
    constructor(options = {}) {
        this.options = {
            latticeSize: options.latticeSize || 128,
            complexField: options.complexField !== false,
            ...options
        };
        this.init();
    }

    init() {
        this.setupScene();
        this.setupCamera();
        this.setupRenderer();
        this.animate();
    }

    animate = () => {
        requestAnimationFrame(this.animate);
        this.render();
    }
}
```

#### Three.js Specific
- **Scene background**: `0x0a0a1a` (dark blue, consistent with consciousness theme)
- **Fog**: Subtle fog for depth (`THREE.Fog(0x0a0a1a, 1000, 3000)`)
- **Camera**: PerspectiveCamera with 60° FOV
- **Materials**: Use shader materials for complex visualizations

### File Naming
- Python: `snake_case.py`
- JavaScript: `camelCase.js`
- CSS: `kebab-case.css`
- Documentation: `UPPERCASE.md` for top-level, `Title Case.md` for subdirectories

### Commit Messages
Follow the project's "Commit Spellcraft" guidelines:
- Present tense: "Fix event loop glitch" (not "Fixed")
- Minify fluff, maximize signal
- Reference issues when relevant: "Fix #123: Resolve WebSocket timeout"
- Keep first line under 72 characters

---

## 🔧 Common Development Tasks

### Adding a New Consciousness Algorithm

1. **Backend** (`src/lattice.py`):
```python
def calculate_new_phenomenon(self, node: ConsciousnessNode) -> float:
    """
    Calculate new consciousness phenomenon.

    Mathematical basis: [Explain equation here]
    """
    # Implement Core EQ variant
    return result
```

2. **Frontend** (`static/js/consciousnessRenderer.js`):
```javascript
updateVisualization(data) {
    // Add new visualization mode
    if (this.currentMode === 'new_mode') {
        // Render new phenomenon
    }
}
```

3. **Bridge** (`src/server.py`):
```python
# Add API endpoint if needed
@app.post("/api/new_phenomenon")
async def trigger_phenomenon(params: PhenomenonParams):
    lattice.calculate_new_phenomenon(params)
    return {"status": "success"}
```

### Adding a New Visualization Mode

1. Add enum value in `src/lattice.py`:
```python
class UniverseMode(Enum):
    NEW_MODE = "new_mode"
```

2. Implement shader in `static/js/consciousnessRenderer.js`:
```javascript
setupMaterials() {
    this.newModeMaterial = new THREE.ShaderMaterial({
        vertexShader: /* GLSL */`...`,
        fragmentShader: /* GLSL */`...`,
        uniforms: { /* ... */ }
    });
}
```

3. Update mode switcher in UI

### Adding Physics Parameters

1. Update `ParameterUpdate` model in `src/server.py`:
```python
class ParameterUpdate(BaseModel):
    new_param: Optional[float] = None
```

2. Apply in lattice engine (`src/lattice.py`):
```python
def update(self, delta_time: float):
    new_param = self.params.get('new_param', default_value)
    # Apply to consciousness calculations
```

3. Add UI control in `static/index.html`:
```html
<input type="range" id="new-param" min="0" max="1" step="0.01" value="0.5">
```

---

## 🚨 Critical Points for AI Assistants

### ✅ DO

1. **Preserve mathematical integrity**: Core EQ calculations must remain accurate
2. **Use existing patterns**: Follow established code structure (dataclasses, async/await, Three.js classes)
3. **Test mathematical changes**: Run `python src/lattice_demo.py` after modifying Core EQ
4. **Check both server modes**: Ensure changes work with both `demo_server.py` and `run_server.py`
5. **Document equations**: Include mathematical notation in docstrings
6. **Handle optional dependencies**: Check `HAS_TORCH` before using PyTorch
7. **Maintain performance**: Target 60fps for WebSocket streaming
8. **Use type hints**: All Python functions should have type annotations
9. **Respect separation of concerns**: Backend = math, Frontend = visualization, Bridge = communication

### ❌ DON'T

1. **Break the Core EQ**: Never modify consciousness calculations without understanding mathematical basis
2. **Remove legacy support**: Keep `demo_server.py` and `lattice_demo.py` working without heavy dependencies
3. **Break GitHub Pages**: Don't modify `index.html` in ways that break standalone browser demo
4. **Ignore performance**: Consciousness simulation requires real-time performance
5. **Mix concerns**: Don't put visualization logic in backend or math logic in frontend
6. **Hard-code values**: Use parameters and configuration for tunable values
7. **Skip documentation**: Mathematical code requires detailed comments
8. **Assume dependencies**: Not all users have PyTorch/GPU; provide NumPy fallbacks

### 🔍 Before Making Changes

1. **Read relevant documentation**:
   - `README.md` - User-facing features
   - `ARCHITECTURE.md` - Technical architecture
   - `CONTRIBUTING.md` - Development process

2. **Understand the mathematical context**:
   - What consciousness equation is being implemented?
   - How does it relate to the Core EQ?
   - What are the valid parameter ranges?

3. **Check dependencies**:
   - Does this require new Python packages? Update `requirements.txt`
   - Does this require new JavaScript libraries? Document in code comments
   - Will this work without GPU/PyTorch?

4. **Test locally**:
   - Run `python demo_server.py` and verify demo works
   - Run `python run_server.py` and verify production mode works
   - Test in browser at http://localhost:8000

---

## 📊 Performance Targets

| Configuration | Nodes | FPS | Latency | Memory |
|--------------|-------|-----|---------|---------|
| Demo (stdlib only) | 64 | 30 | ~50ms | <50MB |
| Production (NumPy) | 128 | 60 | ~16ms | ~100MB |
| GPU (PyTorch+CUDA) | 512 | 60 | ~8ms | ~200MB |
| Maximum (1024 nodes) | 1024 | 45 | ~22ms | ~400MB |

**When optimizing**:
- Profile with Python's `cProfile` or `line_profiler`
- Use NumPy vectorized operations instead of loops
- Leverage GPU with PyTorch when available
- Use WebGL instancing for large node counts
- Minimize WebSocket payload size (consider binary encoding)

---

## 🔐 Security Considerations

Per `SECURITY.md`:
- Only versions 5.1.x and 4.0.x receive security updates
- Report vulnerabilities to JACOBCSMITHD@GMAIL.COM
- Maintain responsible testing guidelines (no production impact)
- Follow coordinated disclosure (90 days or until patch)

**When adding features**:
- Validate all API inputs (use Pydantic models)
- Sanitize user-provided parameters before mathematical calculations
- Prevent infinite loops in consciousness algorithms
- Limit WebSocket message sizes
- Rate-limit API endpoints if exposing to public internet

---

## 🌐 External Resources

- **Live Demo**: https://jacobcdsmith.github.io/CONSIM
- **Repository**: https://github.com/Jacobcdsmith/CONSIM
- **License**: Apache 2.0 (see LICENSE file)
- **Author**: Jacob C. Smith
- **Academic Citation**:
  > Smith, J.C. (2025). *The Multiversal Consciousness Framework: Real-Time Simulation Architecture.* CONSIM Project.

---

## 🤝 Contributing Workflow (for AI Assistants)

When implementing changes:

1. **Understand the request**: Clarify requirements with the user
2. **Plan the implementation**: Break down into backend/frontend/bridge components
3. **Check existing code**: Look for similar patterns to follow
4. **Implement incrementally**: Make small, testable changes
5. **Test thoroughly**: Verify both demo and production modes
6. **Document changes**: Update docstrings and inline comments
7. **Commit with clear messages**: Follow "Commit Spellcraft" guidelines
8. **Suggest tests**: Recommend how user can verify the changes

### Example Implementation Flow

```
User Request: "Add a new 'quantum entanglement' visualization mode"

Step 1: Plan
- Backend: Add quantum_entanglement calculation in lattice.py
- Frontend: Create shader for entanglement visualization
- Bridge: Add mode to UniverseMode enum

Step 2: Backend (src/lattice.py)
- Add UniverseMode.QUANTUM_ENTANGLEMENT
- Implement calculate_entanglement() method
- Update node update logic to track entanglement pairs

Step 3: Frontend (static/js/consciousnessRenderer.js)
- Create entanglementMaterial with custom shader
- Add entanglement connection rendering
- Update mode switcher

Step 4: Test
- Run demo_server.py, verify mode appears
- Run run_server.py, verify WebSocket streams entanglement data
- Check browser console for errors

Step 5: Document
- Add docstring with mathematical basis
- Update CLAUDE.md with new mode (if significant)
- Suggest user test: "Click mode selector, choose 'Quantum Entanglement', spawn nodes"
```

---

## 📚 Quick Reference

### Python Dependencies
```
fastapi>=0.100.0
uvicorn[standard]>=0.20.0
websockets>=11.0
numpy>=1.20.0
pydantic>=2.0.0
python-multipart>=0.0.6
aiofiles>=23.0.0
```

### JavaScript Dependencies
- Three.js (included via CDN in HTML)
- No build process required (vanilla JS)

### Server Startup Commands
```bash
# Demo mode (no dependencies)
python demo_server.py

# Production mode (requires requirements.txt)
python run_server.py

# With specific host/port
python run_server.py --host 0.0.0.0 --port 8080
```

### Key Files Checklist
When making changes, consider impact on:
- [ ] `src/lattice.py` - Core consciousness engine
- [ ] `src/server.py` - FastAPI server
- [ ] `static/js/consciousnessRenderer.js` - Three.js renderer
- [ ] `static/js/app.js` - Application logic
- [ ] `static/index.html` - UI controls
- [ ] `requirements.txt` - Python dependencies
- [ ] `README.md` - User documentation
- [ ] `CLAUDE.md` - This file (if architectural changes)

---

## 🎓 Learning Path for New AI Assistants

If you're new to this codebase, study in this order:

1. **README.md** - Understand user perspective and features
2. **ARCHITECTURE.md** - Grasp three-tier architecture
3. **src/lattice.py** (first 100 lines) - Learn Core EQ implementation
4. **static/js/consciousnessRenderer.js** (first 100 lines) - Understand visualization
5. **src/server.py** - See how WebSocket bridge works
6. **CONTRIBUTING.md** - Learn development culture and workflow
7. **This file (CLAUDE.md)** - Deep dive into patterns and conventions

**Time estimate**: ~30 minutes to reach productive contribution level

---

## 📞 Getting Help

As an AI assistant, if you encounter:

- **Unclear mathematical notation**: Ask user to clarify the consciousness equation context
- **Ambiguous requirements**: Request specific examples or use cases
- **Architecture questions**: Refer back to ARCHITECTURE.md or this file
- **Build/dependency issues**: Check Python version (3.8+), installed packages
- **Performance problems**: Profile before optimizing, check FPS targets above

**Remember**: The project maintainer (Jacob C. Smith) values "deliberate clarity" and "sharp messages" (per CONTRIBUTING.md). Be precise and technically accurate in communications.

---

**Last Updated**: 2025-01-17
**Codebase Version**: 1.0.0
**Target AI Assistant**: Claude Code, GPT-4, Copilot, or similar code-aware AI

---

*"Build bravely. Ship weird. See you in the diffs."* - CONTRIBUTING.md
