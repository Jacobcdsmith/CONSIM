#!/usr/bin/env python3
"""
Quick demo script showing how to interact with CONSIM executable via API
This demonstrates how easy it is to interact with the consciousness simulation
"""

import requests
import time
import json
import random

def test_consim_api(base_url="http://localhost:8000"):
    """Test the CONSIM API endpoints"""
    
    print("🧠 CONSIM API Demo")
    print("=" * 50)
    
    try:
        # Test status endpoint
        print("1. Checking server status...")
        response = requests.get(f"{base_url}/api/status")
        status = response.json()
        print(f"   ✅ Server running: {status['node_count']} nodes, {status['cluster_count']} clusters")
        
        # Test stats endpoint
        print("\n2. Getting consciousness statistics...")
        response = requests.get(f"{base_url}/api/stats")
        stats = response.json()
        print(f"   🧮 Consciousness magnitude: {stats['consciousness_magnitude']:.3f}")
        print(f"   🌊 Global resonance: {stats['global_resonance']:.3f}")
        print(f"   👁️  Average attention: {stats['average_attention']:.3f}")
        
        # Add some nodes
        print("\n3. Adding consciousness nodes...")
        for i in range(5):
            x = random.uniform(-50, 50)
            y = random.uniform(-50, 50)
            response = requests.post(f"{base_url}/api/nodes", 
                                   json={"x": x, "y": y})
            result = response.json()
            print(f"   ➕ Added node at ({x:.1f}, {y:.1f})")
            time.sleep(0.2)
        
        # Update physics parameters
        print("\n4. Adjusting physics parameters...")
        new_params = {
            "gravity": 1.5,
            "friction": 0.95,
            "time_dilation": 1.2
        }
        response = requests.post(f"{base_url}/api/parameters", json=new_params)
        print(f"   ⚙️  Updated physics: {new_params}")
        
        # Trigger updates and watch evolution
        print("\n5. Running simulation updates...")
        for i in range(10):
            requests.post(f"{base_url}/api/update")
            response = requests.get(f"{base_url}/api/stats")
            stats = response.json()
            print(f"   Frame {i+1}: nodes={stats['node_count']}, "
                  f"clusters={stats['cluster_count']}, "
                  f"resonance={stats['global_resonance']:.3f}")
            time.sleep(0.1)
        
        print("\n✅ Demo completed successfully!")
        print(f"🌐 Open {base_url} in your browser to see the visual simulation")
        
    except requests.exceptions.ConnectionError:
        print(f"❌ Could not connect to CONSIM server at {base_url}")
        print("   Make sure the CONSIM executable is running first:")
        print("   ./dist/CONSIM --no-browser")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_consim_api()