"""
FastAPI Server - WebSocket bridge for real-time consciousness field streaming.

This server wraps the Python lattice engine and provides:
- WebSocket endpoint for real-time 60fps consciousness field streaming 
- REST API for parameter control and system management
- Binary/JSON serialization for efficient data transmission
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from typing import Dict, List, Optional
import asyncio
import json
import time
import logging
from pathlib import Path

from .lattice import ConsciousnessLattice, UniverseMode

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI(
    title="CONSIM Consciousness Lattice Engine",
    description="Real-time consciousness field simulation with WebSocket streaming",
    version="1.0.0"
)

# Global lattice instance
lattice = ConsciousnessLattice(grid_size=128, universe_count=3)

# Connected WebSocket clients
connected_clients: List[WebSocket] = []

# Simulation state
simulation_running = False
target_fps = 60
frame_time = 1.0 / target_fps

class ParameterUpdate(BaseModel):
    """Model for parameter updates."""
    gravity: Optional[float] = None
    friction: Optional[float] = None
    elasticity: Optional[float] = None
    time_dilation: Optional[float] = None
    field_strength: Optional[float] = None

class NodeCreate(BaseModel):
    """Model for creating new nodes."""
    x: float
    y: float

class MouseInfluence(BaseModel):
    """Model for mouse interaction."""
    x: float
    y: float
    mode: str = "push"  # push, pull, vortex, wave, string
    active: bool = False

class QuantumCollapse(BaseModel):
    """Model for quantum collapse events."""
    x: float
    y: float

@app.on_event("startup")
async def startup_event():
    """Initialize the simulation on startup."""
    global simulation_running
    simulation_running = True
    # Start the simulation loop
    asyncio.create_task(simulation_loop())
    logger.info("Consciousness lattice engine started")

@app.on_event("shutdown")
async def shutdown_event():
    """Clean shutdown."""
    global simulation_running
    simulation_running = False
    logger.info("Consciousness lattice engine stopped")

async def simulation_loop():
    """Main simulation loop running at target FPS."""
    global lattice, connected_clients
    
    last_time = time.time()
    
    while simulation_running:
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        
        try:
            # Update lattice
            global_stats = lattice.update(delta_time)
            
            # Get complete state for transmission
            state = lattice.get_state_for_transmission()
            
            # Send to all connected clients
            if connected_clients:
                state_json = json.dumps(state, default=str)
                disconnected_clients = []
                
                for client in connected_clients:
                    try:
                        await client.send_text(state_json)
                    except Exception as e:
                        logger.warning(f"Client disconnected: {e}")
                        disconnected_clients.append(client)
                
                # Remove disconnected clients
                for client in disconnected_clients:
                    connected_clients.remove(client)
            
            # Control frame rate
            elapsed = time.time() - current_time
            sleep_time = max(0, frame_time - elapsed)
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)
                
        except Exception as e:
            logger.error(f"Error in simulation loop: {e}")
            await asyncio.sleep(0.1)  # Prevent tight error loop

@app.websocket("/stream")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time consciousness field streaming."""
    await websocket.accept()
    connected_clients.append(websocket)
    logger.info(f"Client connected. Total clients: {len(connected_clients)}")
    
    try:
        # Send initial state
        initial_state = lattice.get_state_for_transmission()
        await websocket.send_text(json.dumps(initial_state, default=str))
        
        # Listen for client messages (mouse interactions, etc.)
        while True:
            try:
                data = await websocket.receive_text()
                message = json.loads(data)
                
                # Handle different message types
                message_type = message.get('type')
                
                if message_type == 'mouse_influence':
                    # Apply mouse influence to lattice
                    mouse_data = message.get('data', {})
                    # This will be handled in the next update cycle
                    # Store mouse influence for next frame
                    lattice.mouse_influence = mouse_data
                
                elif message_type == 'parameter_update':
                    # Update simulation parameters
                    params = message.get('data', {})
                    lattice.update_params(params)
                    logger.info(f"Parameters updated: {params}")
                
                elif message_type == 'add_node':
                    # Add new consciousness node
                    node_data = message.get('data', {})
                    lattice.add_node(node_data.get('x', 0), node_data.get('y', 0))
                    logger.info(f"Node added at ({node_data.get('x', 0)}, {node_data.get('y', 0)})")
                
                elif message_type == 'quantum_collapse':
                    # Trigger quantum collapse
                    collapse_data = message.get('data', {})
                    lattice.quantum_collapse(collapse_data.get('x', 0), collapse_data.get('y', 0))
                    logger.info(f"Quantum collapse at ({collapse_data.get('x', 0)}, {collapse_data.get('y', 0)})")
                
                elif message_type == 'set_mode':
                    # Change visualization mode
                    mode = message.get('data', {}).get('mode', 'consciousness')
                    lattice.set_mode(UniverseMode(mode))
                    logger.info(f"Mode changed to: {mode}")
                    
            except asyncio.TimeoutError:
                continue
            except json.JSONDecodeError:
                logger.warning("Invalid JSON received from client")
            except Exception as e:
                logger.error(f"Error processing client message: {e}")
                break
    
    except WebSocketDisconnect:
        logger.info("Client disconnected normally")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        if websocket in connected_clients:
            connected_clients.remove(websocket)
        logger.info(f"Client removed. Total clients: {len(connected_clients)}")

# REST API Endpoints for external control

@app.get("/")
async def root():
    """Serve the main application."""
    return FileResponse("static/index.html")

@app.get("/api/status")
async def get_status():
    """Get current simulation status."""
    return {
        "running": simulation_running,
        "connected_clients": len(connected_clients),
        "node_count": len(lattice.nodes),
        "cluster_count": len(lattice.clusters),
        "target_fps": target_fps,
        "time": lattice.time
    }

@app.get("/api/stats")
async def get_stats():
    """Get detailed lattice statistics."""
    return lattice._calculate_global_consciousness()

@app.post("/api/parameters")
async def update_parameters(params: ParameterUpdate):
    """Update simulation parameters."""
    param_dict = params.dict(exclude_unset=True)
    lattice.update_params(param_dict)
    return {"status": "updated", "parameters": param_dict}

@app.get("/api/parameters")
async def get_parameters():
    """Get current simulation parameters."""
    return lattice.params

@app.post("/api/nodes")
async def create_node(node: NodeCreate):
    """Create a new consciousness node."""
    new_node = lattice.add_node(node.x, node.y)
    return {
        "status": "created",
        "node": new_node.to_dict()
    }

@app.post("/api/collapse")
async def trigger_collapse(collapse: QuantumCollapse):
    """Trigger quantum collapse at specified location."""
    lattice.quantum_collapse(collapse.x, collapse.y)
    return {
        "status": "triggered",
        "location": {"x": collapse.x, "y": collapse.y}
    }

@app.post("/api/mode/{mode}")
async def set_mode(mode: str):
    """Set visualization mode."""
    try:
        lattice.set_mode(UniverseMode(mode))
        return {"status": "updated", "mode": mode}
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid mode: {mode}")

@app.post("/api/reset")
async def reset_simulation():
    """Reset the entire simulation."""
    global lattice
    lattice = ConsciousnessLattice(grid_size=128, universe_count=3)
    return {"status": "reset"}

@app.get("/api/export")
async def export_state():
    """Export current lattice state."""
    return lattice.get_state_for_transmission()

# Serve static files (Three.js frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    
    # Run with uvicorn for development
    uvicorn.run(
        "src.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )