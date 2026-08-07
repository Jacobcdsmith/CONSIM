#!/usr/bin/env python3
"""
Public hosting script for CONSIM using ngrok.
Exposes the local server to the internet with a public URL.
"""

import sys
import threading
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from pyngrok import ngrok

def start_demo_server():
    """Start the demo server in a thread."""
    import demo_server
    demo_server.start_server(port=8000, host="127.0.0.1")

def main():
    """Start CONSIM with public internet access via ngrok."""
    print("🚀 Starting CONSIM Public Hosting...")
    print("=" * 60)

    # Start the demo server in a background thread
    server_thread = threading.Thread(target=start_demo_server, daemon=True)
    server_thread.start()

    # Wait for server to start
    print("⏳ Starting local server...")
    time.sleep(3)

    # Create ngrok tunnel
    print("🌐 Creating public internet tunnel...")
    try:
        # Open a ngrok tunnel to port 8000
        public_url = ngrok.connect(8000, bind_tls=True)

        print("\n" + "=" * 60)
        print("✅ CONSIM is now LIVE on the internet!")
        print("=" * 60)
        print(f"\n🌍 PUBLIC URL: {public_url}")
        print("\n📱 Share this URL with anyone, anywhere in the world!")
        print("   They can access CONSIM from any device with a browser.")
        print("\n🧠 Features available:")
        print("   • Interactive 3D consciousness field visualization")
        print("   • 64 consciousness nodes in real-time")
        print("   • 3 parallel universe branches")
        print("   • Click to spawn nodes, drag to interact")
        print("   • Multiple visualization modes")
        print("\n⚠️  Note: This tunnel will stay active as long as this")
        print("   script is running. Press Ctrl+C to stop.")
        print("=" * 60)

        # Keep the script running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n🛑 Shutting down public hosting...")
            ngrok.disconnect(public_url)
            print("✅ Tunnel closed. Server stopped.")

    except Exception as e:
        print(f"❌ Error creating tunnel: {e}")
        print("\nTroubleshooting:")
        print("1. Check your internet connection")
        print("2. Ngrok might require authentication")
        print("   Sign up at: https://ngrok.com")
        print("   Get your auth token and run:")
        print("   ngrok config add-authtoken YOUR_TOKEN")
        sys.exit(1)

if __name__ == "__main__":
    main()
