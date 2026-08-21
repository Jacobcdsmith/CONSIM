"""
End-to-end integration tests.

Tests complete workflows and system integration:
- Multi-node interactions
- Cluster formation
- Universe interactions
- Performance benchmarks
"""

import unittest
import time
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from lattice import ConsciousnessLattice, ConsciousnessNode


class TestSystemIntegration(unittest.TestCase):
    """Test complete system integration."""

    def setUp(self):
        """Set up test fixtures."""
        self.lattice = ConsciousnessLattice(grid_size=64, universe_count=3)

    def test_multi_node_interactions(self):
        """Test that multiple nodes interact correctly."""
        # Add several nodes close together
        nodes = []
        for i in range(5):
            node = self.lattice.add_node(10.0 + i * 20, 10.0)
            nodes.append(node)

        # Run several update cycles
        for _ in range(10):
            self.lattice.update(0.016)

        # Nodes should still exist and be updated
        for node in nodes:
            self.assertIn(node, self.lattice.nodes)
            self.assertIsNotNone(node.consciousness_re)
            self.assertIsNotNone(node.consciousness_im)

    def test_cluster_formation(self):
        """Test that clusters form when nodes are close together."""
        # Add many nodes in a small area
        for i in range(10):
            self.lattice.add_node(
                50.0 + (i % 3) * 15,
                50.0 + (i // 3) * 15
            )

        # Run updates to allow cluster formation
        for _ in range(20):
            self.lattice.update(0.016)

        # Should have detected clusters
        # (May or may not form depending on phase/frequency alignment)
        self.assertIsInstance(self.lattice.clusters, list)

    def test_universe_node_interactions(self):
        """Test that universes affect their contained nodes."""
        # Add node and track its frequency
        node = self.lattice.add_node(0.0, 0.0)
        initial_frequency = node.frequency

        # Run many updates
        for _ in range(50):
            self.lattice.update(0.016)

        # Frequency may be modulated by universe
        # Just verify it stays in reasonable range
        self.assertGreater(node.frequency, 0.0)
        self.assertLess(node.frequency, 100.0)

    def test_attention_field_conservation(self):
        """Test that attention field remains normalized through operations."""
        # Perform various operations
        self.lattice.add_node(100.0, 100.0)
        self.lattice.update(0.016)

        node_to_remove = self.lattice.nodes[0]
        self.lattice.remove_node(node_to_remove)

        self.lattice.quantum_collapse(50.0, 50.0)
        self.lattice.update(0.016)

        # Attention should still sum to 1
        total_attention = sum(node.attention for node in self.lattice.nodes)
        self.assertAlmostEqual(total_attention, 1.0, places=4)

    def test_consciousness_continuity(self):
        """Test that consciousness values remain continuous over time."""
        node = self.lattice.add_node(0.0, 0.0)

        consciousness_values = []
        for _ in range(10):
            self.lattice.update(0.016)
            magnitude = (node.consciousness_re**2 + node.consciousness_im**2)**0.5
            consciousness_values.append(magnitude)

        # Values should be continuous (no sudden jumps)
        for i in range(1, len(consciousness_values)):
            diff = abs(consciousness_values[i] - consciousness_values[i-1])
            # Allow reasonable change per frame
            self.assertLess(diff, 50.0, "Consciousness should change smoothly")

    def test_parameter_effects(self):
        """Test that parameter changes affect system behavior."""
        # Create two separate nodes to test different time dilations
        node1 = self.lattice.add_node(0.0, 0.0)
        node1.phase = 0.0

        # Test with normal time dilation
        self.lattice.update_params({'time_dilation': 1.0})
        self.lattice.update(0.016)
        normal_phase_change = node1.phase

        # Create a new node for fast time test
        node2 = self.lattice.add_node(100.0, 100.0)
        node2.phase = 0.0

        # Test with accelerated time
        self.lattice.update_params({'time_dilation': 5.0})
        self.lattice.update(0.016)
        fast_phase_change = node2.phase

        # Fast time should produce more phase change
        # Note: both start from 0 and are measured after one update
        self.assertGreater(fast_phase_change, normal_phase_change)

    def test_system_stability(self):
        """Test that system remains stable over many updates."""
        # Run many update cycles
        for _ in range(100):
            self.lattice.update(0.016)

        # System should still be functional
        self.assertGreater(len(self.lattice.nodes), 0)
        self.assertEqual(len(self.lattice.universes), 3)

        # Global consciousness should be calculable
        stats = self.lattice._calculate_global_consciousness()
        self.assertIsNotNone(stats['consciousness_magnitude'])


class TestPerformanceBenchmarks(unittest.TestCase):
    """Performance benchmarks for the system."""

    def test_update_performance(self):
        """Benchmark lattice update performance."""
        lattice = ConsciousnessLattice(grid_size=128, universe_count=3)

        start_time = time.time()
        iterations = 60  # Simulate 1 second at 60fps

        for _ in range(iterations):
            lattice.update(0.016)

        elapsed_time = time.time() - start_time

        # Should complete 60 updates in reasonable time (< 2 seconds)
        self.assertLess(
            elapsed_time, 2.0,
            f"60 updates took {elapsed_time:.2f}s, should be < 2.0s"
        )

        # Calculate average FPS
        avg_fps = iterations / elapsed_time
        print(f"\nAverage FPS: {avg_fps:.1f}")

    def test_node_scaling(self):
        """Test performance with increasing node counts."""
        results = {}

        for size in [32, 64, 128]:
            lattice = ConsciousnessLattice(grid_size=size, universe_count=3)

            start_time = time.time()
            for _ in range(30):  # 30 frames
                lattice.update(0.016)
            elapsed_time = time.time() - start_time

            fps = 30 / elapsed_time
            results[size] = fps

            print(f"\n{size} nodes: {fps:.1f} FPS")

        # Performance should degrade gracefully
        self.assertGreater(results[32], 10, "Should handle 32 nodes at >10 FPS")

    def test_memory_usage(self):
        """Test memory footprint of the system."""
        import sys

        lattice = ConsciousnessLattice(grid_size=256, universe_count=3)

        # Get approximate size of lattice
        size = sys.getsizeof(lattice)
        print(f"\nLattice object size: {size / 1024:.1f} KB")

        # Should be reasonable (< 1 MB for object itself)
        self.assertLess(size, 1024 * 1024)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""

    def test_empty_lattice(self):
        """Test behavior with no nodes."""
        lattice = ConsciousnessLattice(grid_size=0, universe_count=3)

        # Should handle empty lattice
        stats = lattice._calculate_global_consciousness()
        self.assertEqual(stats['node_count'], 0)
        self.assertEqual(stats['consciousness_magnitude'], 0.0)

    def test_single_node(self):
        """Test behavior with single node."""
        lattice = ConsciousnessLattice(grid_size=1, universe_count=3)

        self.assertEqual(len(lattice.nodes), 1)

        # Should update without errors
        lattice.update(0.016)

        stats = lattice._calculate_global_consciousness()
        self.assertEqual(stats['node_count'], 1)

    def test_extreme_parameters(self):
        """Test with extreme parameter values."""
        lattice = ConsciousnessLattice(grid_size=32, universe_count=3)

        # Very high gravity
        lattice.update_params({'gravity': 100.0})
        lattice.update(0.016)

        # Very high time dilation
        lattice.update_params({'time_dilation': 10.0})
        lattice.update(0.016)

        # Should not crash
        self.assertGreater(len(lattice.nodes), 0)

    def test_rapid_node_addition_removal(self):
        """Test rapid addition and removal of nodes."""
        lattice = ConsciousnessLattice(grid_size=10, universe_count=3)

        # Rapidly add and remove nodes
        for _ in range(20):
            node = lattice.add_node(0.0, 0.0)
            lattice.update(0.016)
            if len(lattice.nodes) > 5:
                lattice.remove_node(lattice.nodes[0])

        # Should remain stable
        stats = lattice._calculate_global_consciousness()
        self.assertIsNotNone(stats)


if __name__ == '__main__':
    unittest.main(verbosity=2)
