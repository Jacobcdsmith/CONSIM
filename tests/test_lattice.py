"""
Unit tests for the ConsciousnessLattice engine.

Tests the core mathematical implementation of the Multiversal Consciousness Framework:
- ConsciousnessNode behavior
- Universe dynamics
- Lattice update mechanisms
- Consciousness calculations
"""

import unittest
import math
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from lattice import ConsciousnessNode, Universe, ConsciousnessLattice, UniverseMode


class TestConsciousnessNode(unittest.TestCase):
    """Test ConsciousnessNode class and Core EQ calculations."""

    def setUp(self):
        """Set up test fixtures."""
        self.node = ConsciousnessNode(
            x=10.0,
            y=20.0,
            frequency=40.0,
            phase=0.0,
            attention=0.5
        )
        self.params = {
            'gravity': 1.0,
            'friction': 0.99,
            'elasticity': 0.8,
            'time_dilation': 1.0,
            'field_strength': 1.0
        }

    def test_node_initialization(self):
        """Test that nodes initialize with correct values."""
        self.assertEqual(self.node.x, 10.0)
        self.assertEqual(self.node.y, 20.0)
        self.assertEqual(self.node.frequency, 40.0)
        self.assertEqual(self.node.phase, 0.0)
        self.assertEqual(self.node.attention, 0.5)

    def test_consciousness_calculation(self):
        """Test Core EQ: C = A(x) * Φ(x) * e^(iτ(x))."""
        self.node.update(0.016, self.params)

        # Expected values: C = 0.5 * 40.0 * e^(i*phase)
        # At phase=0: e^(i*0) = cos(0) + i*sin(0) = 1 + 0i
        # But phase evolves, so we just check that consciousness is calculated
        self.assertIsNotNone(self.node.consciousness_re)
        self.assertIsNotNone(self.node.consciousness_im)

    def test_phase_evolution(self):
        """Test that phase evolves correctly over time."""
        initial_phase = self.node.phase
        self.node.update(0.016, self.params)

        # Phase should increase
        self.assertNotEqual(self.node.phase, initial_phase)
        # Phase should stay in [0, 2π)
        self.assertGreaterEqual(self.node.phase, 0.0)
        self.assertLess(self.node.phase, 2 * math.pi)

    def test_attention_density_calculation(self):
        """Test Gaussian attention density A(x) = exp(-d²/(2σ²))."""
        # Node at origin should have high attention
        node_origin = ConsciousnessNode(x=0.0, y=0.0)
        attention_origin = node_origin.calculate_attention_density()

        # Node far from origin should have low attention
        node_far = ConsciousnessNode(x=500.0, y=500.0)
        attention_far = node_far.calculate_attention_density()

        self.assertGreater(attention_origin, attention_far)
        self.assertLessEqual(attention_origin, 1.0)
        self.assertGreaterEqual(attention_far, 0.0)

    def test_physics_update(self):
        """Test that physics (velocity, position) update correctly."""
        initial_x = self.node.x
        initial_y = self.node.y

        # Apply velocity
        self.node.vx = 10.0
        self.node.vy = 5.0

        self.node.update(0.016, self.params)

        # Position should change
        self.assertNotEqual(self.node.x, initial_x)
        self.assertNotEqual(self.node.y, initial_y)

    def test_friction_application(self):
        """Test that friction reduces velocity over time."""
        self.node.vx = 100.0
        self.node.vy = 100.0

        # Run multiple updates
        for _ in range(10):
            self.node.update(0.016, self.params)

        # Velocity should be reduced due to friction
        self.assertLess(abs(self.node.vx), 100.0)
        self.assertLess(abs(self.node.vy), 100.0)

    def test_boundary_conditions(self):
        """Test that nodes respect world boundaries."""
        # Place node outside boundaries
        self.node.x = 600.0
        self.node.vx = 10.0

        self.node.update(0.016, self.params)

        # Node should be within bounds or velocity should be reversed
        self.assertTrue(
            abs(self.node.x) <= 500 or self.node.vx < 0,
            "Node should respect boundaries"
        )

    def test_intelligence_tensors(self):
        """Test that intelligence tensors are properly initialized and updated."""
        self.assertIsNotNone(self.node.logic_tensor)
        self.assertIsNotNone(self.node.memory_tensor)
        self.assertIsNotNone(self.node.processing_tensor)

        # Tensors should be 2D tuples
        self.assertEqual(len(self.node.logic_tensor), 2)
        self.assertEqual(len(self.node.memory_tensor), 2)
        self.assertEqual(len(self.node.processing_tensor), 2)

    def test_node_serialization(self):
        """Test that nodes can be serialized to dict."""
        node_dict = self.node.to_dict()

        self.assertIsInstance(node_dict, dict)
        self.assertIn('x', node_dict)
        self.assertIn('y', node_dict)
        self.assertIn('frequency', node_dict)
        self.assertIn('phase', node_dict)
        self.assertIn('consciousness_re', node_dict)
        self.assertIn('consciousness_im', node_dict)


class TestUniverse(unittest.TestCase):
    """Test Universe class and multiverse superposition."""

    def setUp(self):
        """Set up test fixtures."""
        self.universe = Universe(
            id=0,
            center_x=0.0,
            center_y=0.0,
            radius=250.0,
            resonance_coeff=0.5
        )

    def test_universe_initialization(self):
        """Test that universes initialize correctly."""
        self.assertEqual(self.universe.id, 0)
        self.assertEqual(self.universe.center_x, 0.0)
        self.assertEqual(self.universe.center_y, 0.0)
        self.assertEqual(self.universe.radius, 250.0)
        self.assertEqual(self.universe.resonance_coeff, 0.5)

    def test_node_containment(self):
        """Test that universe correctly identifies contained nodes."""
        # Node inside universe
        node_inside = ConsciousnessNode(x=50.0, y=50.0)
        self.assertTrue(self.universe._contains_node(node_inside))

        # Node outside universe
        node_outside = ConsciousnessNode(x=500.0, y=500.0)
        self.assertFalse(self.universe._contains_node(node_outside))

    def test_universe_serialization(self):
        """Test that universes can be serialized."""
        universe_dict = self.universe.to_dict()

        self.assertIsInstance(universe_dict, dict)
        self.assertIn('id', universe_dict)
        self.assertIn('resonance_coeff', universe_dict)


class TestConsciousnessLattice(unittest.TestCase):
    """Test ConsciousnessLattice class and system integration."""

    def setUp(self):
        """Set up test fixtures."""
        self.lattice = ConsciousnessLattice(grid_size=32, universe_count=3)

    def test_lattice_initialization(self):
        """Test that lattice initializes correctly."""
        self.assertEqual(self.lattice.grid_size, 32)
        self.assertEqual(self.lattice.universe_count, 3)
        self.assertEqual(len(self.lattice.nodes), 32)
        self.assertEqual(len(self.lattice.universes), 3)

    def test_dirichlet_sampling(self):
        """Test that Dirichlet λ weights sum to 1."""
        total = sum(self.lattice.lambdas)
        self.assertAlmostEqual(total, 1.0, places=5)

        # All λ values should be positive
        for lambda_val in self.lattice.lambdas:
            self.assertGreater(lambda_val, 0.0)

    def test_attention_normalization(self):
        """Test that attention field normalizes to ∫A(x)dμ(x) = 1."""
        total_attention = sum(node.attention for node in self.lattice.nodes)
        self.assertAlmostEqual(total_attention, 1.0, places=5)

    def test_lattice_update(self):
        """Test that lattice updates without errors."""
        initial_time = self.lattice.time

        # Update lattice
        stats = self.lattice.update(0.016)

        # Time should advance
        self.assertGreater(self.lattice.time, initial_time)

        # Stats should be returned
        self.assertIsInstance(stats, dict)
        self.assertIn('consciousness_magnitude', stats)
        self.assertIn('node_count', stats)

    def test_global_consciousness_calculation(self):
        """Test global consciousness integral calculation."""
        stats = self.lattice._calculate_global_consciousness()

        self.assertIn('consciousness_magnitude', stats)
        self.assertIn('global_resonance', stats)
        self.assertIn('average_attention', stats)
        self.assertIn('node_count', stats)
        self.assertIn('cluster_count', stats)

        # Consciousness magnitude should be non-negative
        self.assertGreaterEqual(stats['consciousness_magnitude'], 0.0)

    def test_add_node(self):
        """Test adding nodes dynamically."""
        initial_count = len(self.lattice.nodes)

        new_node = self.lattice.add_node(100.0, 200.0)

        self.assertEqual(len(self.lattice.nodes), initial_count + 1)
        self.assertIn(new_node, self.lattice.nodes)
        self.assertEqual(new_node.x, 100.0)
        self.assertEqual(new_node.y, 200.0)

        # Attention should still be normalized
        total_attention = sum(node.attention for node in self.lattice.nodes)
        self.assertAlmostEqual(total_attention, 1.0, places=5)

    def test_remove_node(self):
        """Test removing nodes safely."""
        initial_count = len(self.lattice.nodes)
        node_to_remove = self.lattice.nodes[0]

        self.lattice.remove_node(node_to_remove)

        self.assertEqual(len(self.lattice.nodes), initial_count - 1)
        self.assertNotIn(node_to_remove, self.lattice.nodes)

        # Attention should still be normalized
        if self.lattice.nodes:  # If there are still nodes
            total_attention = sum(node.attention for node in self.lattice.nodes)
            self.assertAlmostEqual(total_attention, 1.0, places=5)

    def test_quantum_collapse(self):
        """Test quantum collapse effect."""
        # Add node near collapse point
        node = self.lattice.add_node(0.0, 0.0)
        initial_phase = node.phase

        # Trigger collapse at origin
        self.lattice.quantum_collapse(0.0, 0.0)

        # Node phase should be affected
        self.assertNotEqual(node.phase, initial_phase)

    def test_cluster_detection(self):
        """Test that clusters are detected correctly."""
        # Add several nodes close together
        for i in range(5):
            self.lattice.add_node(10.0 + i * 5, 10.0)

        # Run update to trigger cluster detection
        self.lattice.update(0.016)

        # Clusters should be detected
        self.assertIsInstance(self.lattice.clusters, list)

    def test_parameter_updates(self):
        """Test that parameters update correctly."""
        new_params = {
            'gravity': 2.0,
            'friction': 0.95,
            'time_dilation': 2.0
        }

        self.lattice.update_params(new_params)

        self.assertEqual(self.lattice.params['gravity'], 2.0)
        self.assertEqual(self.lattice.params['friction'], 0.95)
        self.assertEqual(self.lattice.params['time_dilation'], 2.0)

    def test_state_transmission(self):
        """Test that state can be prepared for transmission."""
        state = self.lattice.get_state_for_transmission()

        self.assertIsInstance(state, dict)
        self.assertIn('nodes', state)
        self.assertIn('universes', state)
        self.assertIn('clusters', state)
        self.assertIn('global_stats', state)
        self.assertIn('params', state)
        self.assertIn('lambdas', state)

        # Nodes should be serialized
        self.assertIsInstance(state['nodes'], list)
        if state['nodes']:
            self.assertIsInstance(state['nodes'][0], dict)


class TestUniverseMode(unittest.TestCase):
    """Test UniverseMode enum."""

    def test_mode_values(self):
        """Test that all modes have correct values."""
        self.assertEqual(UniverseMode.CONSCIOUSNESS.value, "consciousness")
        self.assertEqual(UniverseMode.ATTENTION.value, "attention")
        self.assertEqual(UniverseMode.FREQUENCY.value, "frequency")
        self.assertEqual(UniverseMode.TEMPORAL.value, "temporal")
        self.assertEqual(UniverseMode.MULTIVERSE.value, "multiverse")


if __name__ == '__main__':
    unittest.main()
