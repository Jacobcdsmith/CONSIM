#!/usr/bin/env python3
"""
CONSIM Test Runner
==================

Comprehensive test suite runner for the Multiversal Consciousness Framework.

Usage:
    python run_tests.py              # Run all tests
    python run_tests.py unit         # Run only unit tests
    python run_tests.py integration  # Run only integration tests
    python run_tests.py performance  # Run only performance tests
    python run_tests.py fast         # Run quick tests only (skip slow tests)
"""

import unittest
import sys
import time
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))
sys.path.insert(0, str(project_root))


def run_all_tests(verbosity=2):
    """Run all tests."""
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    return result.wasSuccessful()


def run_unit_tests(verbosity=2):
    """Run only unit tests."""
    from tests.test_lattice import (
        TestConsciousnessNode,
        TestUniverse,
        TestConsciousnessLattice,
        TestUniverseMode
    )

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestConsciousnessNode))
    suite.addTests(loader.loadTestsFromTestCase(TestUniverse))
    suite.addTests(loader.loadTestsFromTestCase(TestConsciousnessLattice))
    suite.addTests(loader.loadTestsFromTestCase(TestUniverseMode))

    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    return result.wasSuccessful()


def run_integration_tests(verbosity=2):
    """Run only integration tests."""
    from tests.test_integration import (
        TestSystemIntegration,
        TestEdgeCases
    )

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestSystemIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))

    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    return result.wasSuccessful()


def run_performance_tests(verbosity=2):
    """Run only performance tests."""
    from tests.test_integration import TestPerformanceBenchmarks

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPerformanceBenchmarks)

    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    return result.wasSuccessful()


def run_server_tests(verbosity=2):
    """Run only server tests."""
    from tests.test_server import (
        TestServerAPI,
        TestServerWebSocket,
        TestServerModels
    )
    from tests.test_demo import TestDemoServer

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestServerAPI))
    suite.addTests(loader.loadTestsFromTestCase(TestServerWebSocket))
    suite.addTests(loader.loadTestsFromTestCase(TestServerModels))
    suite.addTests(loader.loadTestsFromTestCase(TestDemoServer))

    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    return result.wasSuccessful()


def run_fast_tests(verbosity=2):
    """Run fast tests only (skip performance benchmarks)."""
    from tests.test_lattice import (
        TestConsciousnessNode,
        TestUniverse,
        TestConsciousnessLattice,
        TestUniverseMode
    )
    from tests.test_integration import TestSystemIntegration, TestEdgeCases

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestConsciousnessNode))
    suite.addTests(loader.loadTestsFromTestCase(TestUniverse))
    suite.addTests(loader.loadTestsFromTestCase(TestConsciousnessLattice))
    suite.addTests(loader.loadTestsFromTestCase(TestUniverseMode))
    suite.addTests(loader.loadTestsFromTestCase(TestSystemIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))

    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    return result.wasSuccessful()


def print_banner(text):
    """Print a formatted banner."""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def main():
    """Main test runner."""
    args = sys.argv[1:]

    # Determine which tests to run
    test_type = args[0] if args else 'all'

    print_banner("🧠 CONSIM Test Suite")

    start_time = time.time()

    # Run appropriate tests
    if test_type == 'unit':
        print_banner("Running Unit Tests")
        success = run_unit_tests()
    elif test_type == 'integration':
        print_banner("Running Integration Tests")
        success = run_integration_tests()
    elif test_type == 'performance':
        print_banner("Running Performance Tests")
        success = run_performance_tests()
    elif test_type == 'server':
        print_banner("Running Server Tests")
        success = run_server_tests()
    elif test_type == 'fast':
        print_banner("Running Fast Tests")
        success = run_fast_tests()
    elif test_type == 'all':
        print_banner("Running All Tests")
        success = run_all_tests()
    else:
        print(f"Unknown test type: {test_type}")
        print("\nAvailable options:")
        print("  all         - Run all tests (default)")
        print("  unit        - Run unit tests only")
        print("  integration - Run integration tests only")
        print("  performance - Run performance benchmarks")
        print("  server      - Run server tests only")
        print("  fast        - Run fast tests (skip performance)")
        return 1

    elapsed_time = time.time() - start_time

    # Print summary
    print("\n" + "=" * 70)
    if success:
        print(f"  ✅ All tests passed in {elapsed_time:.2f}s")
    else:
        print(f"  ❌ Some tests failed in {elapsed_time:.2f}s")
    print("=" * 70 + "\n")

    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
