# CONSIM - Consciousness Manifold Simulator

**Always follow these instructions first and only search for additional context if the information here is incomplete or found to be in error.**

CONSIM is a Python-based consciousness simulation framework that implements the Multiversal Consciousness Framework through real-time mathematical visualization. It provides both a standalone demo version and a production FastAPI server with WebSocket streaming.

## Bootstrap and Setup Commands

### Install Dependencies
```bash
pip install -r requirements.txt
```
**Timing**: 15 seconds. Installs fastapi, uvicorn, websockets, numpy, pydantic, python-multipart, aiofiles.

### Validate Installation
```bash
python src/lattice_demo.py
```
**Timing**: <50ms. **NEVER CANCEL** - this validation always completes quickly.
Expected output: "🎉 All tests passed! The consciousness lattice engine is working."

## Running the Application

### Demo Version (Zero Dependencies)
```bash
python demo_server.py
```
**Timing**: Starts in 2-3 seconds. **NEVER CANCEL** - startup is fast.
- Uses Python standard library only
- Serves on http://localhost:8000
- API endpoints: `/api/status`, `/api/stats`, `/api/state`, `/api/nodes`, `/api/parameters`

### Production Version (FastAPI + WebSocket)
```bash
python run_server.py
```
**Timing**: Starts in 2-3 seconds. **NEVER CANCEL** - startup is fast.
- Requires dependencies from requirements.txt
- Serves on http://localhost:8000
- WebSocket streaming: `ws://localhost:8000/stream`
- Enhanced with GPU acceleration when numpy/torch available

## Testing and Validation

### API Testing
Test the consciousness simulation API endpoints:
```bash
# Check server status
curl -s http://localhost:8000/api/status

# Get consciousness statistics  
curl -s http://localhost:8000/api/stats

# Add consciousness node
curl -s -X POST -H "Content-Type: application/json" -d '{"x": 10, "y": 10}' http://localhost:8000/api/nodes

# Update physics parameters
curl -s -X POST -H "Content-Type: application/json" -d '{"gravity": 1.5, "friction": 0.95}' http://localhost:8000/api/parameters
```

### WebSocket Testing
Test real-time consciousness field streaming:
```bash
# Create test client
cat > /tmp/test_websocket.py << 'EOF'
import asyncio, websockets, json
async def test():
    async with websockets.connect("ws://localhost:8000/stream") as ws:
        for i in range(3):
            data = json.loads(await ws.recv())
            print(f"Frame {i+1}: {len(data.get('nodes', []))} nodes")
asyncio.run(test())
EOF

timeout 5 python /tmp/test_websocket.py
```

### Manual UI Testing
1. Open http://localhost:8000 in browser
2. **Expected behavior**: UI loads with consciousness lattice interface, physics controls, and mathematical equations
3. **Click anywhere in black visualization area** to spawn consciousness nodes
4. **Adjust sliders** (Gravity, Friction, Time Dilation, Field Strength) to see real-time effects
5. **Test interaction modes**: Push, Pull, Vortex, Wave buttons change mouse behavior
6. **Test visualization modes**: Switch between Consciousness, Attention, Frequency, Temporal, Multiverse views

**Known issue**: Three.js may fail to load from CDN due to network restrictions. App falls back to 2D canvas renderer automatically.

## Code Structure and Development

### Key Files
- **`src/lattice.py`**: Core consciousness engine with NumPy/PyTorch GPU acceleration
- **`src/lattice_demo.py`**: Standard library demo version (zero dependencies)
- **`src/server.py`**: FastAPI WebSocket server
- **`run_server.py`**: Production server entry point
- **`demo_server.py`**: Demo server entry point
- **`static/js/app.js`**: Frontend application logic
- **`static/js/app_demo.js`**: Demo frontend logic
- **`static/js/consciousnessRenderer.js`**: WebGL/Three.js visualization
- **`static/index.html`**: Web interface for backend servers
- **`index.html`**: GitHub Pages standalone version (full consciousness simulation)
- **`docs/index.html`**: Additional documentation interface
- **`legacy/CONSIM.html`**: Original single-file implementation (preserved for reference)

### Mathematical Foundation
The system implements two core equations:
- **Core EQ**: `C = ∫[M_C] A(x) Φ(x) e^(iτ(x)) dμ(x)` - consciousness scalar calculation
- **Multiverse**: `M = Σ[i] λ_i U_i` - three-universe superposition

### Development Workflow
1. **Test changes**: Always run `python src/lattice_demo.py` first (takes <50ms)
2. **Backend changes**: Modify `src/lattice.py` for new consciousness algorithms
3. **Frontend changes**: Update `static/js/consciousnessRenderer.js` for new visualizations  
4. **API changes**: Extend `src/server.py` for new endpoints
5. **Restart server**: Changes require server restart (FastAPI reload enabled in dev mode)

## Validation Scenarios

### Complete End-to-End Test
Always perform this full validation after making changes:

1. **Start server**: `python run_server.py` (wait 3 seconds)
2. **Validate API**: `curl -s http://localhost:8000/api/status` should return JSON with "running": true
3. **Test WebSocket**: Use websocket test script - should receive streaming data
4. **Test UI**: Open browser, spawn nodes by clicking, verify real-time updates
5. **Test physics**: Adjust gravity slider, verify consciousness nodes react
6. **Test modes**: Switch visualization modes, verify display changes

### Performance Expectations
- **Server startup**: 2-3 seconds for both demo and production versions
- **API response time**: <100ms for all endpoints
- **WebSocket frame rate**: ~10fps (configurable in server.py)
- **Frontend render rate**: 30-60fps depending on browser and node count
- **Memory usage**: <100MB for standard operation, ~200MB with GPU acceleration

## Common Issues and Troubleshooting

### Three.js CDN Blocked
**Symptom**: "Three.js failed to load" in browser console
**Solution**: This is expected in restricted networks. App automatically falls back to 2D canvas renderer.

### API 404 Errors in Frontend
**Symptom**: Frontend shows "Error updating lattice: Update failed"
**Solution**: Frontend expects different API endpoints. Use manual API testing instead. This is a known routing issue.

### Port Already in Use
**Symptom**: "Address already in use" error
**Solution**: Kill existing server: `pkill -f python` then restart

### WebSocket Connection Failed
**Symptom**: WebSocket test hangs or fails
**Solution**: Ensure production server is running (`python run_server.py`), not demo server

## Build and Deploy

**No build process required** - this is pure Python and JavaScript with no compilation step.

### GitHub Pages Deployment
The standalone version deploys automatically via `.github/workflows/static.yml` when pushing to main branch.

### Local Development
```bash
# Quick development cycle
python src/lattice_demo.py           # Validate core engine (<50ms)
python run_server.py                 # Start development server (3 seconds)
# Make changes to src/ or static/
# Restart server to see changes
```

## Architecture Notes

- **Backend**: Python FastAPI with async WebSocket streaming
- **Frontend**: Vanilla JavaScript with Three.js/WebGL (fallback to 2D canvas)
- **Data flow**: Backend streams consciousness field states via WebSocket at 10fps
- **Rendering**: GPU-accelerated when possible, CPU fallback always available
- **Mathematics**: Core consciousness equations implemented in both NumPy (production) and standard library (demo)

## No Formal Testing Infrastructure
This project does not use pytest, jest, or similar test frameworks. Validation relies on:
1. The `lattice_demo.py` script for core engine testing
2. Manual API testing with curl commands  
3. Manual UI testing in browser
4. WebSocket streaming verification

Always use the validation procedures above rather than looking for test commands that don't exist.