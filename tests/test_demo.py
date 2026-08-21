"""
Tests for demo server functionality.

Tests the simplified demo server implementation:
- HTTP request handling
- API endpoints
- Lattice integration
"""

import unittest
import json
import sys
from pathlib import Path
from io import BytesIO

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import demo server components
from demo_server import ConsciousnessHTTPHandler, ConsciousnessLattice


class TestDemoServer(unittest.TestCase):
    """Test demo server functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.lattice = ConsciousnessLattice(grid_size=32)

    def test_lattice_initialization(self):
        """Test that demo lattice initializes correctly."""
        self.assertEqual(len(self.lattice.nodes), 32)
        self.assertEqual(len(self.lattice.universes), 3)
        self.assertIsInstance(self.lattice.lambdas, list)

    def test_lattice_update(self):
        """Test that demo lattice updates without errors."""
        initial_time = self.lattice.time
        stats = self.lattice.update(0.016)

        self.assertGreater(self.lattice.time, initial_time)
        self.assertIsInstance(stats, dict)

    def test_add_node(self):
        """Test adding nodes in demo lattice."""
        initial_count = len(self.lattice.nodes)
        node = self.lattice.add_node(100.0, 200.0)

        self.assertEqual(len(self.lattice.nodes), initial_count + 1)
        self.assertEqual(node.x, 100.0)
        self.assertEqual(node.y, 200.0)

    def test_quantum_collapse(self):
        """Test quantum collapse in demo lattice."""
        node = self.lattice.add_node(0.0, 0.0)
        initial_phase = node.phase

        self.lattice.quantum_collapse(0.0, 0.0)

        # Phase should be affected
        self.assertNotEqual(node.phase, initial_phase)

    def test_state_serialization(self):
        """Test that demo lattice state can be serialized."""
        state = self.lattice.get_state_for_transmission()

        # Should be JSON serializable
        try:
            json_str = json.dumps(state)
            self.assertIsInstance(json_str, str)
        except (TypeError, ValueError) as e:
            self.fail(f"State serialization failed: {e}")


if __name__ == '__main__':
    unittest.main()
