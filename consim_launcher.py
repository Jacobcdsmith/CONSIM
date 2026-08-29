#!/usr/bin/env python3
"""
CONSIM Launcher - Standalone Executable Version
Launches the consciousness simulation with embedded web server.

This script is designed to be packaged with PyInstaller for distribution.
"""

import os
import sys
import webbrowser
import time
import threading
from pathlib import Path

# Add src to path for imports
script_dir = Path(__file__).parent
if hasattr(sys, '_MEIPASS'):
    # Running from PyInstaller bundle
    base_dir = Path(sys._MEIPASS)
else:
    # Running from source
    base_dir = script_dir

sys.path.insert(0, str(base_dir / "src"))

# Import the demo server components
import http.server
import socketserver
import json
import urllib.parse

from lattice_demo import ConsciousnessLattice

class ConsciousnessHTTPHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler with API support for consciousness lattice."""
    
    def __init__(self, *args, **kwargs):
        # Set the directory to serve files from
        if hasattr(sys, '_MEIPASS'):
            # Running from PyInstaller bundle
            serve_directory = sys._MEIPASS
        else:
            # Running from source
            serve_directory = str(Path(__file__).parent)
        
        super().__init__(*args, directory=serve_directory, **kwargs)
        
    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/':
            self.path = '/static/index.html'
        elif self.path.startswith('/api/'):
            self.handle_api_get()
            return
        
        super().do_GET()
    
    def do_POST(self):
        """Handle POST requests."""
        if self.path.startswith('/api/'):
            self.handle_api_post()
        else:
            self.send_error(404)
    
    def handle_api_get(self):
        """Handle API GET requests."""
        global lattice
        
        if self.path == '/api/status':
            status = {
                'running': True,
                'node_count': len(lattice.nodes),
                'cluster_count': len(lattice.clusters),
                'time': lattice.time
            }
            self.send_json_response(status)
        
        elif self.path == '/api/stats':
            stats = lattice._calculate_global_consciousness()
            self.send_json_response(stats)
        
        elif self.path == '/api/state':
            # Get current lattice state
            state = lattice.get_state_for_transmission()
            # Serialize nodes properly
            serialized_state = {
                'nodes': [node.to_dict() for node in lattice.nodes],
                'universes': [universe.to_dict() for universe in lattice.universes],
                'clusters': lattice.clusters,
                'global_stats': lattice._calculate_global_consciousness(),
                'params': lattice.params,
                'lambdas': lattice.lambdas,
                'time': lattice.time
            }
            self.send_json_response(serialized_state)
        
        else:
            self.send_error(404)
    
    def handle_api_post(self):
        """Handle API POST requests."""
        global lattice
        
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return
        
        if self.path == '/api/update':
            # Update lattice
            lattice.update(0.016)  # ~60fps
            self.send_json_response({'status': 'updated'})
        
        elif self.path == '/api/parameters':
            # Update parameters
            lattice.update_params(data)
            self.send_json_response({'status': 'updated', 'parameters': data})
        
        elif self.path == '/api/nodes':
            # Add new node
            node = lattice.add_node(data.get('x', 0), data.get('y', 0))
            self.send_json_response({'status': 'created', 'node': node.to_dict()})
        
        elif self.path == '/api/collapse':
            # Trigger quantum collapse
            lattice.quantum_collapse(data.get('x', 0), data.get('y', 0))
            self.send_json_response({'status': 'triggered'})
        
        elif self.path == '/api/reset':
            # Reset simulation
            lattice = ConsciousnessLattice(grid_size=64)
            self.send_json_response({'status': 'reset'})
        
        else:
            self.send_error(404)
    
    def send_json_response(self, data):
        """Send JSON response."""
        json_data = json.dumps(data).encode('utf-8')
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(json_data)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        self.wfile.write(json_data)

def open_browser_delayed(url, delay=2):
    """Open browser after a short delay to ensure server is ready."""
    time.sleep(delay)
    try:
        webbrowser.open(url)
        print(f"🌐 Browser opened: {url}")
    except Exception as e:
        print(f"⚠️  Could not open browser automatically: {e}")
        print(f"💡 Please manually open: {url}")

def start_server(port=8000, auto_open=True):
    """Start the consciousness simulation server."""
    global lattice
    
    # Initialize the consciousness lattice
    lattice = ConsciousnessLattice(grid_size=64)
    
    # Start server
    with socketserver.TCPServer(("", port), ConsciousnessHTTPHandler) as httpd:
        url = f"http://localhost:{port}"
        
        print("="*60)
        print("🧠 CONSIM - Consciousness Lattice Simulation")
        print("="*60)
        print(f"✨ Server starting on {url}")
        print(f"🌌 Consciousness lattice with {len(lattice.nodes)} nodes initialized")
        print(f"🔀 {len(lattice.universes)} universes with λ weights: {[f'{l:.3f}' for l in lattice.lambdas]}")
        print(f"🔗 API endpoints available at {url}/api/")
        print("="*60)
        print("💡 INSTRUCTIONS:")
        print("   • Click anywhere to spawn consciousness nodes")
        print("   • Drag to interact with consciousness fields")
        print("   • Use sliders to adjust physics parameters")
        print("   • Watch clusters form and evolve in real-time")
        print("="*60)
        print("⏹️  Press Ctrl+C to stop the server")
        print("="*60)
        
        # Open browser automatically if requested
        if auto_open:
            browser_thread = threading.Thread(target=open_browser_delayed, args=(url,))
            browser_thread.daemon = True
            browser_thread.start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")
            print("👋 Thank you for exploring consciousness with CONSIM!")

if __name__ == "__main__":
    # Parse command line arguments
    auto_open = True
    port = 8000
    
    if len(sys.argv) > 1:
        if "--no-browser" in sys.argv:
            auto_open = False
        
        # Look for port argument
        for arg in sys.argv[1:]:
            if arg.startswith("--port="):
                try:
                    port = int(arg.split("=")[1])
                except ValueError:
                    print("⚠️  Invalid port number, using default 8000")
    
    start_server(port=port, auto_open=auto_open)