"""
Simplified Lattice Engine - Demo version using only Python standard library.

This demonstrates the mathematical foundation without external dependencies.
For the full GPU-accelerated version, install: pip install numpy torch fastapi uvicorn
"""

import math
import random
import time
import json
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum

class UniverseMode(Enum):
    CONSCIOUSNESS = "consciousness"
    ATTENTION = "attention" 
    FREQUENCY = "frequency"
    TEMPORAL = "temporal"
    MULTIVERSE = "multiverse"

@dataclass
class ConsciousnessNode:
    """
    Individual consciousness node implementing the Core EQ calculations.
    
    Simplified version using Python standard library instead of NumPy.
    """
    x: float = 0.0
    y: float = 0.0
    vx: float = 0.0
    vy: float = 0.0
    radius: float = 3.0
    base_radius: float = 3.0
    
    # Core EQ Parameters
    frequency: float = 40.0  # Φ(x): 40Hz gamma ± 5Hz noise
    base_frequency: float = 40.0
    phase: float = 0.0  # τ(x): random in [0, 2π)
    attention: float = 0.0  # A(x): Gaussian attention density
    
    # Complex consciousness value C = A*Φ*e^(iτ)
    consciousness_re: float = 0.0  # Real part
    consciousness_im: float = 0.0  # Imaginary part
    
    universe_id: int = 0
    resonance_coeff: float = 1.0  # λ_i
    
    mass: float = 1.0
    
    # Intelligence tensor system (2D tensors)
    logic_tensor: Tuple[float, float] = field(default_factory=lambda: (0.5, 0.5))
    memory_tensor: Tuple[float, float] = field(default_factory=lambda: (0.5, 0.5))
    processing_tensor: Tuple[float, float] = field(default_factory=lambda: (0.5, 0.5))
    creativity_tensor: Tuple[float, float] = field(default_factory=lambda: (0.5, 0.5))
    social_tensor: Tuple[float, float] = field(default_factory=lambda: (0.5, 0.5))
    
    # Emergent properties
    consciousness_depth: float = 0.0
    self_awareness: float = 0.0
    adaptive_capacity: float = 0.0
    collective_intelligence: float = 0.0
    
    cluster_id: int = -1
    thought_intensity: float = 0.0
    recursion_level: int = 0

    def update(self, delta_time: float, params: Dict[str, float], mouse_influence: Optional[Dict] = None):
        """Update consciousness node using Core EQ calculations."""
        
        # Apply time dilation
        delta_time *= params.get('time_dilation', 1.0)
        
        # Calculate consciousness value: C = A(x) * Φ(x) * e^(iτ(x))
        # e^(iτ) = cos(τ) + i*sin(τ)
        cos_tau = math.cos(self.phase)
        sin_tau = math.sin(self.phase)
        
        # C is complex: C = A(x) * Φ(x) * (cos(τ) + i*sin(τ))
        self.consciousness_re = self.attention * self.frequency * cos_tau
        self.consciousness_im = self.attention * self.frequency * sin_tau
        
        # Evolve phase based on frequency (simple evolution)
        self.phase += self.frequency * delta_time * 2 * math.pi / 1000
        self.phase = self.phase % (2 * math.pi)  # Keep in [0, 2π)
        
        # Apply mouse interaction if provided
        if mouse_influence:
            self._apply_mouse_interaction(mouse_influence, delta_time, params)
        
        # Apply gravity and physics
        self._apply_physics(delta_time, params)
        
        # Update tensor system
        self._update_intelligence_tensors(delta_time, params)
        
        # Update radius based on consciousness magnitude |C|
        consciousness_magnitude = math.sqrt(self.consciousness_re**2 + self.consciousness_im**2)
        self.radius = self.base_radius + consciousness_magnitude * 0.1

    def _apply_mouse_interaction(self, mouse_influence: Dict, delta_time: float, params: Dict[str, float]):
        """Apply mouse interaction forces based on mode."""
        mouse_x = mouse_influence.get('x', 0)
        mouse_y = mouse_influence.get('y', 0)
        interaction_mode = mouse_influence.get('mode', 'push')
        is_active = mouse_influence.get('active', False)
        
        if not is_active:
            return
            
        dx_mouse = mouse_x - self.x
        dy_mouse = mouse_y - self.y
        distance_mouse = math.sqrt(dx_mouse**2 + dy_mouse**2)
        max_distance = 200 * params.get('field_strength', 1.0)
        
        if distance_mouse < max_distance:
            angle = math.atan2(dy_mouse, dx_mouse)
            force = (max_distance - distance_mouse) / max_distance
            force *= params.get('field_strength', 1.0)
            
            if interaction_mode == 'push':
                # Repel from mouse
                self.vx -= math.cos(angle) * force * 0.4 * delta_time * 60
                self.vy -= math.sin(angle) * force * 0.4 * delta_time * 60
            elif interaction_mode == 'pull':
                # Attract to mouse
                self.vx += math.cos(angle) * force * 0.4 * delta_time * 60
                self.vy += math.sin(angle) * force * 0.4 * delta_time * 60
            elif interaction_mode == 'vortex':
                # Create vortex effect
                tangential_angle = angle + math.pi/2
                self.vx += math.cos(tangential_angle) * force * 0.5 * delta_time * 60
                self.vy += math.sin(tangential_angle) * force * 0.5 * delta_time * 60
            elif interaction_mode == 'wave':
                # Wave-like movement
                time_factor = time.time() * 10
                wave_force = math.sin(distance_mouse * 0.05 - time_factor) * force
                self.vx += math.cos(angle) * wave_force * 0.5 * delta_time * 60
                self.vy += math.sin(angle) * wave_force * 0.5 * delta_time * 60

    def _apply_physics(self, delta_time: float, params: Dict[str, float]):
        """Apply gravity, friction, and boundary conditions."""
        
        # Apply gravity (center attraction)
        if params.get('gravity', 0) > 0:
            dx = 0 - self.x
            dy = 0 - self.y
            dist_center = math.sqrt(dx**2 + dy**2)
            if dist_center > 10:
                gravity_force = params['gravity'] * 0.001 * delta_time * 60
                self.vx += (dx / dist_center) * gravity_force
                self.vy += (dy / dist_center) * gravity_force
        
        # Update position
        self.x += self.vx * delta_time * 60
        self.y += self.vy * delta_time * 60
        
        # Apply friction
        friction = params.get('friction', 0.99) ** (delta_time * 60)
        self.vx *= friction
        self.vy *= friction
        
        # Boundary conditions with quantum tunneling
        world_bounds_x = 1000  # Large world bounds
        world_bounds_y = 1000
        
        if self.x < -world_bounds_x/2 or self.x > world_bounds_x/2:
            if random.random() < 0.05:  # 5% quantum tunneling
                self.x = world_bounds_x/2 if self.x < -world_bounds_x/2 else -world_bounds_x/2
            else:
                self.vx *= -0.8 * params.get('elasticity', 0.8)
                self.x = max(-world_bounds_x/2, min(world_bounds_x/2, self.x))
                
        if self.y < -world_bounds_y/2 or self.y > world_bounds_y/2:
            if random.random() < 0.05:
                self.y = world_bounds_y/2 if self.y < -world_bounds_y/2 else -world_bounds_y/2
            else:
                self.vy *= -0.8 * params.get('elasticity', 0.8)
                self.y = max(-world_bounds_y/2, min(world_bounds_y/2, self.y))

    def _update_intelligence_tensors(self, delta_time: float, params: Dict[str, float]):
        """Update 2D intelligence tensor system."""
        evolution_rate = 0.02 * params.get('time_dilation', 1.0)
        
        # Simple tensor evolution with coupling
        # Logic influences Memory
        self.memory_tensor = (
            self.memory_tensor[0] + self.logic_tensor[0] * evolution_rate * 0.1,
            self.memory_tensor[1] + self.logic_tensor[1] * evolution_rate * 0.1
        )
        
        # Memory influences Processing
        self.processing_tensor = (
            self.processing_tensor[0] + self.memory_tensor[0] * evolution_rate * 0.15,
            self.processing_tensor[1] + self.memory_tensor[1] * evolution_rate * 0.15
        )
        
        # Calculate emergent properties
        logic_magnitude = math.sqrt(self.logic_tensor[0]**2 + self.logic_tensor[1]**2)
        memory_magnitude = math.sqrt(self.memory_tensor[0]**2 + self.memory_tensor[1]**2)
        processing_magnitude = math.sqrt(self.processing_tensor[0]**2 + self.processing_tensor[1]**2)
        
        self.consciousness_depth = min(1.0, (logic_magnitude + memory_magnitude + processing_magnitude) / 3)
        self.self_awareness = min(1.0, logic_magnitude * 0.8 + self.thought_intensity * 0.2)
        
        # Decay thought intensity
        self.thought_intensity = max(0, self.thought_intensity - delta_time * 0.5)

    def calculate_attention_density(self) -> float:
        """Calculate A(x) based on Gaussian distribution centered at (0,0)."""
        sigma = 200.0  # Standard deviation for attention field
        d_sq = self.x**2 + self.y**2
        return math.exp(-d_sq / (2 * sigma**2))

    def to_dict(self) -> Dict:
        """Serialize node state for WebSocket transmission."""
        return {
            'x': self.x,
            'y': self.y,
            'radius': self.radius,
            'frequency': self.frequency,
            'phase': self.phase,
            'attention': self.attention,
            'consciousness_re': self.consciousness_re,
            'consciousness_im': self.consciousness_im,
            'universe_id': self.universe_id,
            'cluster_id': self.cluster_id,
            'consciousness_depth': self.consciousness_depth,
            'self_awareness': self.self_awareness,
            'thought_intensity': self.thought_intensity,
            'recursion_level': self.recursion_level
        }

@dataclass
class Universe:
    """Universe class implementing multiverse superposition M = Σ λ_i U_i."""
    
    id: int
    center_x: float = 0.0
    center_y: float = 0.0
    radius: float = 250.0
    resonance_coeff: float = 1.0  # λ_i
    nodes: List[ConsciousnessNode] = field(default_factory=list)

    def update(self, time_factor: float):
        """Update universe-specific effects on contained nodes."""
        for node in self.nodes:
            if self._contains_node(node):
                # Apply universe-specific frequency modulation
                node.frequency = node.base_frequency * (1 + self.resonance_coeff * 0.2 * math.sin(time_factor * 0.05))

    def _contains_node(self, node: ConsciousnessNode) -> bool:
        """Check if node is within this universe's boundary."""
        dist = math.sqrt((node.x - self.center_x)**2 + (node.y - self.center_y)**2)
        return dist < self.radius

    def to_dict(self) -> Dict:
        """Serialize universe state."""
        return {
            'id': self.id,
            'center_x': self.center_x,
            'center_y': self.center_y,
            'radius': self.radius,
            'resonance_coeff': self.resonance_coeff,
            'node_count': len(self.nodes)
        }

class ConsciousnessLattice:
    """
    Main lattice engine implementing the Multiversal Consciousness Framework.
    
    Simplified version using standard library for demonstration.
    """
    
    def __init__(self, grid_size: int = 128, universe_count: int = 3):
        self.grid_size = grid_size
        self.universe_count = universe_count
        self.time = 0.0
        
        # Initialize nodes and universes
        self.nodes: List[ConsciousnessNode] = []
        self.universes: List[Universe] = []
        self.clusters: List[Dict] = []
        
        # Dirichlet-sampled λ weights for universes
        self.lambdas = self._sample_dirichlet([1.0] * universe_count)
        
        # Physics parameters
        self.params = {
            'gravity': 1.0,
            'friction': 0.99,
            'elasticity': 0.8,
            'time_dilation': 1.0,
            'field_strength': 1.0
        }
        
        # Initialize system
        self._initialize_universes()
        self._initialize_nodes()
        self._normalize_attention_field()
        
        # Performance tracking
        self.last_update_time = time.time()
        
    def _sample_dirichlet(self, alpha: List[float]) -> List[float]:
        """Simplified Dirichlet sampling using gamma distribution approximation."""
        # Simple approximation: sample gamma and normalize
        samples = []
        for a in alpha:
            # Approximate gamma sampling
            samples.append(random.random() ** (1.0 / a))
        
        total = sum(samples)
        return [s / total for s in samples]
    
    def _initialize_universes(self):
        """Create universes with sampled λ coefficients."""
        self.universes = []
        for i in range(self.universe_count):
            universe = Universe(
                id=i,
                center_x=random.uniform(-400, 400),
                center_y=random.uniform(-400, 400),
                radius=random.uniform(150, 250),
                resonance_coeff=self.lambdas[i]
            )
            self.universes.append(universe)
    
    def _initialize_nodes(self):
        """Initialize consciousness nodes on the manifold."""
        self.nodes = []
        
        for i in range(self.grid_size):
            # Random placement within visible world
            x = random.uniform(-500, 500)
            y = random.uniform(-500, 500)
            
            # Assign to random universe
            universe_id = random.randint(0, self.universe_count - 1)
            
            # Create node with Core EQ parameters
            node = ConsciousnessNode(
                x=x, y=y,
                frequency=40.0 + random.uniform(-5, 5),  # 40Hz ± 5Hz
                phase=random.uniform(0, 2*math.pi),  # Random phase
                universe_id=universe_id,
                resonance_coeff=self.lambdas[universe_id]
            )
            
            # Initialize intelligence tensors
            node.logic_tensor = (random.random(), random.random())
            node.memory_tensor = (random.random(), random.random())
            node.processing_tensor = (random.random(), random.random())
            node.creativity_tensor = (random.random(), random.random())
            node.social_tensor = (random.random(), random.random())
            
            self.nodes.append(node)
            self.universes[universe_id].nodes.append(node)
    
    def _normalize_attention_field(self):
        """Normalize attention field A(x) so ∫A(x)dμ(x) = 1."""
        total_attention = 0.0
        
        # Calculate attention for each node
        for node in self.nodes:
            node.attention = node.calculate_attention_density()
            total_attention += node.attention
        
        # Normalize
        if total_attention > 0:
            for node in self.nodes:
                node.attention /= total_attention
    
    def update(self, delta_time: float, mouse_influence: Optional[Dict] = None):
        """Update the entire consciousness lattice."""
        current_time = time.time()
        actual_delta_time = min(0.05, current_time - self.last_update_time)
        self.last_update_time = current_time
        
        self.time += actual_delta_time * self.params['time_dilation']
        
        # Update universes
        for universe in self.universes:
            universe.update(self.time)
        
        # Update nodes with node-to-node interactions
        self._update_nodes_with_interactions(actual_delta_time, mouse_influence)
        
        # Update clusters and intelligence
        self._update_clusters()
        
        # Calculate global consciousness value
        return self._calculate_global_consciousness()
    
    def _update_nodes_with_interactions(self, delta_time: float, mouse_influence: Optional[Dict] = None):
        """Update all nodes including mutual interactions."""
        
        # Calculate repulsion forces between nodes
        for i, node in enumerate(self.nodes):
            # Reset forces
            repulsion_x = 0.0
            repulsion_y = 0.0
            
            # Calculate repulsion from other nodes
            for j, other_node in enumerate(self.nodes):
                if i == j:
                    continue
                    
                dx = other_node.x - node.x
                dy = other_node.y - node.y
                distance = math.sqrt(dx**2 + dy**2)
                min_distance = node.radius + other_node.radius + 10
                
                if distance < min_distance and distance > 0:
                    force = (min_distance - distance) / min_distance
                    angle = math.atan2(dy, dx)
                    repulsion_strength = 0.5 * delta_time * 60 * self.params['elasticity']
                    repulsion_x -= math.cos(angle) * force * repulsion_strength
                    repulsion_y -= math.sin(angle) * force * repulsion_strength
            
            # Apply repulsion
            node.vx += repulsion_x
            node.vy += repulsion_y
            
            # Update node
            node.update(delta_time, self.params, mouse_influence)
    
    def _update_clusters(self):
        """Detect and update consciousness clusters."""
        # Reset cluster assignments
        for node in self.nodes:
            node.cluster_id = -1
        
        self.clusters = []
        processed = set()
        
        # Build clusters based on proximity and phase/frequency alignment
        for i, node in enumerate(self.nodes):
            if i in processed:
                continue
                
            cluster_nodes = [node]
            processed.add(i)
            queue = [i]
            
            while queue:
                current_idx = queue.pop(0)
                current_node = self.nodes[current_idx]
                
                for j, candidate in enumerate(self.nodes):
                    if j in processed:
                        continue
                        
                    dx = candidate.x - current_node.x
                    dy = candidate.y - current_node.y
                    distance = math.sqrt(dx**2 + dy**2)
                    
                    if distance < 80:  # Cluster proximity threshold
                        # Check phase compatibility
                        phase_diff = abs(math.sin(current_node.phase - candidate.phase))
                        phase_compatible = phase_diff < 0.5
                        
                        # Check frequency compatibility
                        freq_ratio = min(current_node.frequency, candidate.frequency) / max(current_node.frequency, candidate.frequency)
                        freq_compatible = freq_ratio > 0.7
                        
                        if phase_compatible and freq_compatible:
                            cluster_nodes.append(candidate)
                            queue.append(j)
                            processed.add(j)
            
            # Create cluster if significant
            if len(cluster_nodes) >= 3:
                cluster_id = len(self.clusters)
                cluster = {
                    'id': cluster_id,
                    'nodes': cluster_nodes,
                    'center_x': sum(n.x for n in cluster_nodes) / len(cluster_nodes),
                    'center_y': sum(n.y for n in cluster_nodes) / len(cluster_nodes),
                    'recursion_depth': 0,
                    'complexity_score': 0
                }
                
                # Assign cluster ID to nodes
                for node in cluster_nodes:
                    node.cluster_id = cluster_id
                
                self.clusters.append(cluster)
    
    def _calculate_global_consciousness(self) -> Dict[str, float]:
        """Calculate global consciousness integral C = ∫A(x)Φ(x)e^(iτ(x))dμ(x)."""
        total_consciousness_re = 0.0
        total_consciousness_im = 0.0
        total_attention = 0.0
        total_phase = 0.0
        
        for node in self.nodes:
            # Weight by universe λ coefficient
            lambda_weight = self.lambdas[node.universe_id]
            total_consciousness_re += node.consciousness_re * lambda_weight
            total_consciousness_im += node.consciousness_im * lambda_weight
            total_attention += node.attention
            total_phase += node.phase
        
        # Calculate magnitude |C|
        consciousness_magnitude = math.sqrt(total_consciousness_re**2 + total_consciousness_im**2)
        
        return {
            'consciousness_magnitude': consciousness_magnitude,
            'global_resonance': consciousness_magnitude / len(self.nodes) if self.nodes else 0,
            'average_attention': total_attention / len(self.nodes) if self.nodes else 0,
            'average_phase_degrees': (total_phase / len(self.nodes) * 180 / math.pi) % 360 if self.nodes else 0,
            'node_count': len(self.nodes),
            'cluster_count': len(self.clusters),
            'time': self.time
        }
    
    def add_node(self, x: float, y: float) -> ConsciousnessNode:
        """Add a new consciousness node at specified coordinates."""
        universe_id = random.randint(0, self.universe_count - 1)
        
        node = ConsciousnessNode(
            x=x, y=y,
            frequency=40.0 + random.uniform(-5, 5),
            phase=random.uniform(0, 2*math.pi),
            universe_id=universe_id,
            resonance_coeff=self.lambdas[universe_id]
        )
        
        # Calculate attention based on Gaussian model
        node.attention = node.calculate_attention_density()
        
        self.nodes.append(node)
        self.universes[universe_id].nodes.append(node)
        
        return node
    
    def quantum_collapse(self, x: float, y: float):
        """Trigger quantum collapse effect at specified location."""
        for node in self.nodes:
            dx = node.x - x
            dy = node.y - y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance < 200:  # Collapse radius
                # Reset consciousness and add random phase shift
                node.consciousness_re = 0
                node.consciousness_im = 0
                node.phase += math.pi
                node.phase = node.phase % (2 * math.pi)
                
                # Add outward force
                if distance > 0:
                    angle = math.atan2(dy, dx)
                    push_force = (200 - distance) / 200 * 5
                    node.vx += math.cos(angle) * push_force
                    node.vy += math.sin(angle) * push_force
    
    def set_mode(self, mode: UniverseMode):
        """Set visualization mode (affects frontend rendering)."""
        # This will be used by the frontend to determine rendering style
        self.current_mode = mode
    
    def get_state_for_transmission(self) -> Dict:
        """Get complete lattice state for WebSocket transmission."""
        return {
            'nodes': [node.to_dict() for node in self.nodes],
            'universes': [universe.to_dict() for universe in self.universes],
            'clusters': self.clusters,
            'global_stats': self._calculate_global_consciousness(),
            'mode': getattr(self, 'current_mode', UniverseMode.CONSCIOUSNESS).value,
            'params': self.params,
            'lambdas': self.lambdas,
            'time': self.time
        }
    
    def update_params(self, new_params: Dict[str, float]):
        """Update physics parameters."""
        self.params.update(new_params)

# Test the lattice engine
if __name__ == "__main__":
    print("Testing CONSIM Lattice Engine (Standard Library Version)")
    
    # Create lattice
    lattice = ConsciousnessLattice(grid_size=32)  # Smaller for demo
    
    print(f"✅ Lattice created with {len(lattice.nodes)} nodes")
    print(f"✅ {len(lattice.universes)} universes with λ weights: {[f'{l:.3f}' for l in lattice.lambdas]}")
    
    # Run a few updates
    for i in range(5):
        stats = lattice.update(0.016)  # ~60fps
        print(f"Frame {i+1}: {stats['node_count']} nodes, {stats['cluster_count']} clusters, resonance: {stats['global_resonance']:.3f}")
    
    # Test adding a node
    new_node = lattice.add_node(0, 0)
    print(f"✅ Added node at (0,0), attention: {new_node.attention:.4f}")
    
    # Test quantum collapse
    lattice.quantum_collapse(0, 0)
    print("✅ Triggered quantum collapse at (0,0)")
    
    # Test serialization
    state = lattice.get_state_for_transmission()
    # Custom JSON serialization for complex objects
    def serialize_for_json(obj):
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        elif isinstance(obj, (list, tuple)):
            return [serialize_for_json(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: serialize_for_json(value) for key, value in obj.items()}
        else:
            return obj
    
    serializable_state = serialize_for_json(state)
    print(f"✅ State serialized: {len(json.dumps(serializable_state))} characters")
    
    print("\n🎉 All tests passed! The consciousness lattice engine is working.")
    print("\nFor the full GPU-accelerated version with FastAPI and Three.js:")
    print("1. Install dependencies: pip install numpy torch fastapi uvicorn")
    print("2. Run: python run_server.py")
    print("3. Open: http://localhost:8000")