"""
Simple HTTP Server for CONSIM Demo
Serves the Three.js frontend and provides basic API endpoints.
"""

import http.server
import socketserver
import json
import urllib.parse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from lattice_demo import ConsciousnessLattice

class ConsciousnessHTTPHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler with API support for consciousness lattice."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)
        
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

# Global lattice instance
lattice = ConsciousnessLattice(grid_size=64)

def start_server(port=8000):
    """Start the consciousness simulation server."""
    with socketserver.TCPServer(("", port), ConsciousnessHTTPHandler) as httpd:
        print(f"🧠 CONSIM Demo Server starting on http://localhost:{port}")
        print(f"✨ Consciousness lattice with {len(lattice.nodes)} nodes initialized")
        print(f"🌌 {len(lattice.universes)} universes with λ weights: {[f'{l:.3f}' for l in lattice.lambdas]}")
        print(f"🔗 API endpoints: /api/status, /api/stats, /api/state")
        print("💡 Open http://localhost:8000 in your browser")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    start_server()