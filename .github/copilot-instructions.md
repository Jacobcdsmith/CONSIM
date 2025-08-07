# CONSIM - Consciousness Manifold Simulator

CONSIM is a real-time consciousness simulation system implementing the Multiversal Consciousness Framework with Python backend (FastAPI + NumPy lattice engine) and interactive Three.js WebGL frontend.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Critical Setup Requirements
- **ALWAYS work from repository root**: `/home/runner/work/CONSIM/CONSIM`
- **NEVER run commands from subdirectories** - Python imports will fail
- Verify location with `pwd` before running any commands

### Bootstrap, Build, and Test the Repository
- Install dependencies: `pip install -r requirements.txt` -- takes 15-30 seconds
- Test core engine: `python src/lattice_demo.py` -- takes ~0.05 seconds. NEVER CANCEL.
- Run demo server: `python demo_server.py` -- starts in ~3 seconds on http://localhost:8000
- Run production server: `python run_server.py` -- starts in ~3 seconds with uvicorn reload on http://localhost:8000
- **NEVER CANCEL server startup commands** - they complete in under 5 seconds, set timeout to 30+ seconds minimum

### Live Demo Access
- **Primary interface**: https://jacobcdsmith.github.io/CONSIM - zero installation required
- **Local demo**: `python demo_server.py` then open http://localhost:8000
- **Development server**: `python run_server.py` then open http://localhost:8000

### API Testing
```bash
# Test demo server APIs (requires demo_server.py running)
curl http://localhost:8000/api/status       # System status
curl http://localhost:8000/api/stats        # Consciousness statistics  
curl http://localhost:8000/api/state        # Full lattice state

# Create consciousness node
curl -X POST http://localhost:8000/api/nodes -H "Content-Type: application/json" -d '{"x": 0.5, "y": 0.5}'

# Update physics parameters
curl -X POST http://localhost:8000/api/parameters -H "Content-Type: application/json" -d '{"gravity": 1.5}'
```

## Validation

### Manual Testing Requirements
- **ALWAYS run complete end-to-end validation** after making changes to consciousness simulation code
- **REQUIRED SCENARIO**: Start demo server, open browser to http://localhost:8000, click to create consciousness nodes, verify node count changes in real-time
- **Interaction validation**: Test node creation by clicking canvas area, verify statistics update in real-time 
- **API validation**: Test all /api/ endpoints return valid JSON responses
- **Performance check**: Lattice updates must complete in <10ms per frame

### Automated Testing
- Core engine tests: `python src/lattice_demo.py` -- validates mathematical calculations in ~0.05s
- No build step required - this is a Python + static files project
- No linting configuration present - code style follows project conventions

## Common Tasks

### Repository Structure
```
CONSIM/
├── README.md              # Main documentation
├── ARCHITECTURE.md        # Technical architecture
├── CONTRIBUTING.md        # Contribution guidelines
├── requirements.txt       # Python dependencies
├── run_server.py         # Production FastAPI server
├── demo_server.py        # Simple demo HTTP server
├── index.html            # GitHub Pages static demo
├── src/
│   ├── lattice.py        # Core consciousness engine
│   ├── lattice_demo.py   # Standalone testing script
│   └── server.py         # FastAPI WebSocket server
└── static/
    ├── index.html        # Alternative static interface
    ├── js/
    │   ├── app.js        # Main application logic
    │   ├── app_demo.js   # Demo-specific logic
    │   └── consciousnessRenderer.js  # WebGL visualization
    └── css/              # Styling
```

### Key Commands Reference
```bash
# Quick test - validates core mathematics
python src/lattice_demo.py

# Start demo (simple HTTP server + API)
python demo_server.py

# Start development (FastAPI + WebSocket + hot reload)  
python run_server.py

# Test specific API endpoint
curl http://localhost:8000/api/status

# Serve static files only
python -m http.server 8002
```

### Development Workflow
1. **Test existing functionality first**: `python src/lattice_demo.py`
2. **Start development server**: `python run_server.py` 
3. **Make targeted changes** to `src/lattice.py` (core math) or `static/js/` (frontend)
4. **Test immediately**: Open http://localhost:8000 and interact with simulation
5. **Validate API**: `curl http://localhost:8000/api/status`
6. **Always test consciousness node creation** by clicking in browser interface

## Timing and Performance

### Command Execution Times
- `pip install -r requirements.txt`: 15-30 seconds
- `python src/lattice_demo.py`: ~0.05 seconds  
- `python demo_server.py` startup: ~3 seconds
- `python run_server.py` startup: ~3 seconds
- Individual lattice update: ~0.003 seconds
- API response time: <10ms

### Critical Performance Requirements
- **Lattice engine updates**: Must complete in <10ms for real-time simulation
- **WebSocket streaming**: Target 10fps (reduced from 60fps to prevent blocking)
- **API endpoints**: Must respond in <100ms
- **Browser interface**: Must be interactive immediately after page load

## System Requirements

### Dependencies
```bash
# Required Python packages (from requirements.txt)
fastapi>=0.100.0          # Web framework
uvicorn[standard]>=0.20.0 # ASGI server  
websockets>=11.0          # WebSocket support
numpy>=1.20.0             # Mathematical operations
pydantic>=2.0.0           # Data validation
python-multipart>=0.0.6   # Form handling
aiofiles>=23.0.0          # Async file operations
```

### Optional Dependencies
- `torch` - GPU acceleration for large-scale simulations (not required for basic functionality)
- Modern browser with WebGL support for frontend visualization

## Mathematical Foundation

### Core Consciousness Equation
```
C = ∫[M_C] A(x) Φ(x) e^(iτ(x)) dμ(x)
```

### Multiverse Superposition
```
M = Σ[i] λ_i U_i  
```

The simulation implements these equations in real-time with:
- 64-128 consciousness nodes by default
- 3 parallel universes with Dirichlet-sampled λ weights
- 40Hz ± 5Hz gamma-band frequency signatures
- Complex-valued consciousness field calculations

## Troubleshooting

### Common Issues
- **Port 8000 in use**: 
  - Check with `ss -tulpn | grep :8000`
  - Kill existing processes: `pkill -f demo_server` or `pkill -f run_server`
  - Use different port by modifying server files
- **Dependencies not found**: Ensure `pip install -r requirements.txt` completed successfully
- **ModuleNotFoundError**: Always run servers from repository root directory `/home/runner/work/CONSIM/CONSIM`
- **Slow performance**: Reduce node count or disable WebSocket streaming
- **API not responding**: Verify server started successfully (should show "Uvicorn running on..." or "CONSIM Demo Server starting" message)
- **Import errors**: Ensure you're in the correct directory and src/ is in Python path

### Debug Commands
```bash
# Check if servers are running
ss -tulpn | grep :8000

# Kill specific server processes
pkill -f demo_server
pkill -f run_server

# Monitor lattice performance
cd /home/runner/work/CONSIM/CONSIM
python -c "
import sys; sys.path.insert(0, 'src')
from lattice_demo import ConsciousnessLattice
import time
lattice = ConsciousnessLattice(64)
start = time.time()
lattice.update(0.016)
print(f'Update time: {time.time()-start:.6f}s')
"

# Test mathematical accuracy
python src/lattice_demo.py | grep "resonance"

# Test API manually with timeout
timeout 5s curl http://localhost:8000/api/status || echo "Server not responding"
```

## GitHub Pages Deployment

The main index.html is automatically deployed to GitHub Pages via `.github/workflows/static.yml`. The live demo at https://jacobcdsmith.github.io/CONSIM contains the complete standalone consciousness simulation.

### Deployment Workflow
- Any push to main branch triggers automatic GitHub Pages deployment
- No build step required - static files deployed directly
- Live demo updates automatically within ~2 minutes of push

## Key Features Validated

✅ **Real-time consciousness field simulation** with mathematical accuracy  
✅ **Interactive node creation** via browser clicks  
✅ **WebGL visualization** with phase-to-color mapping  
✅ **REST API** for external control and monitoring  
✅ **WebSocket streaming** for real-time data (10fps)  
✅ **Multiple universe simulation** with dynamic λ coefficients  
✅ **Biological evolution** with reproduction and genetic drift  
✅ **Intelligence modes** (Basic, Neural, Quantum, Transcendent)  
✅ **GitHub Pages deployment** with zero-config static hosting