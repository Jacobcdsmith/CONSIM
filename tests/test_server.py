"""
Integration tests for the FastAPI server.

Tests the WebSocket bridge and REST API endpoints:
- WebSocket streaming
- API endpoints
- Parameter updates
- Node creation
- Quantum collapse events
"""

import unittest
import asyncio
import json
import sys
from pathlib import Path
from unittest.mock import Mock, patch, AsyncMock

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi.testclient import TestClient

# Import server module properly
import src.server as server
app = server.app
lattice = server.lattice


class TestServerAPI(unittest.TestCase):
    """Test REST API endpoints."""

    @classmethod
    def setUpClass(cls):
        """Set up test client."""
        cls.client = TestClient(app)

    def test_status_endpoint(self):
        """Test GET /api/status."""
        response = self.client.get("/api/status")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn('node_count', data)
        self.assertIn('cluster_count', data)
        self.assertIn('target_fps', data)
        self.assertIn('time', data)

    def test_stats_endpoint(self):
        """Test GET /api/stats."""
        response = self.client.get("/api/stats")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn('consciousness_magnitude', data)
        self.assertIn('global_resonance', data)
        self.assertIn('node_count', data)

    def test_get_parameters(self):
        """Test GET /api/parameters."""
        response = self.client.get("/api/parameters")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn('gravity', data)
        self.assertIn('friction', data)
        self.assertIn('elasticity', data)
        self.assertIn('time_dilation', data)

    def test_update_parameters(self):
        """Test POST /api/parameters."""
        new_params = {
            'gravity': 2.0,
            'friction': 0.95
        }

        response = self.client.post("/api/parameters", json=new_params)

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(data['status'], 'updated')
        self.assertIn('parameters', data)

    def test_create_node(self):
        """Test POST /api/nodes."""
        node_data = {
            'x': 100.0,
            'y': 200.0
        }

        initial_count = len(lattice.nodes)
        response = self.client.post("/api/nodes", json=node_data)

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(data['status'], 'created')
        self.assertIn('node', data)
        self.assertEqual(len(lattice.nodes), initial_count + 1)

    def test_trigger_collapse(self):
        """Test POST /api/collapse."""
        collapse_data = {
            'x': 50.0,
            'y': 50.0
        }

        response = self.client.post("/api/collapse", json=collapse_data)

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(data['status'], 'triggered')
        self.assertIn('location', data)

    def test_set_mode(self):
        """Test POST /api/mode/{mode}."""
        response = self.client.post("/api/mode/consciousness")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(data['status'], 'updated')
        self.assertEqual(data['mode'], 'consciousness')

    def test_set_invalid_mode(self):
        """Test POST /api/mode/{mode} with invalid mode."""
        response = self.client.post("/api/mode/invalid_mode")

        self.assertEqual(response.status_code, 400)

    def test_reset_simulation(self):
        """Test POST /api/reset."""
        response = self.client.post("/api/reset")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(data['status'], 'reset')

    def test_export_state(self):
        """Test GET /api/export."""
        response = self.client.get("/api/export")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn('nodes', data)
        self.assertIn('universes', data)
        self.assertIn('clusters', data)
        self.assertIn('global_stats', data)


class TestServerWebSocket(unittest.TestCase):
    """Test WebSocket functionality."""

    @classmethod
    def setUpClass(cls):
        """Set up test client."""
        cls.client = TestClient(app)

    def test_websocket_connection(self):
        """Test WebSocket connection and initial state."""
        with self.client.websocket_connect("/stream") as websocket:
            # Should receive initial state
            data = websocket.receive_text()
            state = json.loads(data)

            self.assertIn('nodes', state)
            self.assertIn('universes', state)
            self.assertIn('global_stats', state)

    def test_websocket_add_node(self):
        """Test adding node via WebSocket."""
        with self.client.websocket_connect("/stream") as websocket:
            # Receive initial state
            websocket.receive_text()

            # Send add node message
            message = {
                'type': 'add_node',
                'data': {'x': 150.0, 'y': 250.0}
            }
            websocket.send_json(message)

            # Give time for processing
            import time
            time.sleep(0.1)

            # Check that node was added
            # (In real scenario, would receive updated state)

    def test_websocket_parameter_update(self):
        """Test updating parameters via WebSocket."""
        with self.client.websocket_connect("/stream") as websocket:
            # Receive initial state
            websocket.receive_text()

            # Send parameter update
            message = {
                'type': 'parameter_update',
                'data': {'gravity': 3.0}
            }
            websocket.send_json(message)

            # Give time for processing
            import time
            time.sleep(0.1)

    def test_websocket_mouse_influence(self):
        """Test mouse influence via WebSocket."""
        with self.client.websocket_connect("/stream") as websocket:
            # Receive initial state
            websocket.receive_text()

            # Send mouse influence
            message = {
                'type': 'mouse_influence',
                'data': {
                    'x': 100.0,
                    'y': 100.0,
                    'mode': 'push',
                    'active': True
                }
            }
            websocket.send_json(message)

            # Give time for processing
            import time
            time.sleep(0.1)

    def test_websocket_quantum_collapse(self):
        """Test quantum collapse via WebSocket."""
        with self.client.websocket_connect("/stream") as websocket:
            # Receive initial state
            websocket.receive_text()

            # Send quantum collapse
            message = {
                'type': 'quantum_collapse',
                'data': {'x': 0.0, 'y': 0.0}
            }
            websocket.send_json(message)

            # Give time for processing
            import time
            time.sleep(0.1)

    def test_websocket_set_mode(self):
        """Test setting mode via WebSocket."""
        with self.client.websocket_connect("/stream") as websocket:
            # Receive initial state
            websocket.receive_text()

            # Send mode change
            message = {
                'type': 'set_mode',
                'data': {'mode': 'attention'}
            }
            websocket.send_json(message)

            # Give time for processing
            import time
            time.sleep(0.1)


class TestServerModels(unittest.TestCase):
    """Test Pydantic models."""

    def test_parameter_update_model(self):
        """Test ParameterUpdate model validation."""
        ParameterUpdate = server.ParameterUpdate

        # Valid data
        params = ParameterUpdate(gravity=2.0, friction=0.95)
        self.assertEqual(params.gravity, 2.0)
        self.assertEqual(params.friction, 0.95)

        # Partial data (optional fields)
        params_partial = ParameterUpdate(gravity=1.5)
        self.assertEqual(params_partial.gravity, 1.5)
        self.assertIsNone(params_partial.friction)

    def test_node_create_model(self):
        """Test NodeCreate model validation."""
        NodeCreate = server.NodeCreate

        node = NodeCreate(x=100.0, y=200.0)
        self.assertEqual(node.x, 100.0)
        self.assertEqual(node.y, 200.0)

    def test_mouse_influence_model(self):
        """Test MouseInfluence model validation."""
        MouseInfluence = server.MouseInfluence

        mouse = MouseInfluence(x=50.0, y=75.0, mode='push', active=True)
        self.assertEqual(mouse.x, 50.0)
        self.assertEqual(mouse.y, 75.0)
        self.assertEqual(mouse.mode, 'push')
        self.assertTrue(mouse.active)

    def test_quantum_collapse_model(self):
        """Test QuantumCollapse model validation."""
        QuantumCollapse = server.QuantumCollapse

        collapse = QuantumCollapse(x=10.0, y=20.0)
        self.assertEqual(collapse.x, 10.0)
        self.assertEqual(collapse.y, 20.0)


if __name__ == '__main__':
    unittest.main()
