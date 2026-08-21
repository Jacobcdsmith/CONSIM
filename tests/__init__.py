"""
CONSIM Testing Framework
========================

Comprehensive testing suite for the Multiversal Consciousness Framework.

Test Structure:
- test_lattice.py: Unit tests for lattice engine components
- test_server.py: Integration tests for FastAPI server
- test_demo.py: Tests for demo server functionality
- test_integration.py: End-to-end integration tests
"""

import sys
from pathlib import Path

# Add src to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))
sys.path.insert(0, str(project_root))
