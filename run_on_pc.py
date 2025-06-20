#!/usr/bin/env python3
"""
Startup script to run the autonomous underwater robot web app on PC for development/testing.
This script will start both the Flask backend and provide instructions for the React frontend.
"""

import os
import sys
import subprocess
import threading
import time
import webbrowser
from pathlib import Path

def start_flask_server():
    """Start the Flask backend server"""
    print("Starting Flask backend server...")
    os.chdir(Path(__file__).parent / "rpi")
    
    # Activate virtual environment and start Flask
    if os.name == 'nt':  # Windows
        venv_python = Path("../venv/Scripts/python.exe")
    else:  # Linux/Mac
        venv_python = Path("../venv/bin/python")
    
    if venv_python.exists():
        subprocess.run([str(venv_python), "app.py"])
    else:
        print("Virtual environment not found. Running with system Python...")
        subprocess.run([sys.executable, "app.py"])

def start_react_server():
    """Start the React frontend server"""
    print("Starting React frontend server...")
    os.chdir(Path(__file__).parent / "web-dashboard")
    
    # Try different npm commands for different platforms
    npm_commands = ["npm", "npm.cmd", "npx"]
    
    for npm_cmd in npm_commands:
        try:
            print(f"Trying {npm_cmd}...")
            subprocess.run([npm_cmd, "start"], check=True)
            return
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    
    print("Error: npm not found in system PATH.")
    print("Please install Node.js and npm, or run the React server manually:")
    print("1. Open a new terminal")
    print("2. cd web-dashboard")
    print("3. npm install")
    print("4. npm start")
    input("Press Enter after starting the React server manually...")

def main():
    print("=== Autonomous Underwater Robot - PC Development Mode ===")
    print()
    print("This will start the web application in development mode using mock hardware.")
    print("The app will simulate all hardware components without requiring GPIO access.")
    print()
    
    choice = input("Choose an option:\n1. Start Flask backend only\n2. Start React frontend only\n3. Start both (recommended)\nEnter choice (1-3): ")
    
    if choice == "1":
        start_flask_server()
    elif choice == "2":
        start_react_server()
    elif choice == "3":
        print("\nStarting both servers...")
        print("Flask backend will start first, then React frontend.")
        print("The React server will automatically open your browser.")
        print()
        
        # Start Flask in a separate thread
        flask_thread = threading.Thread(target=start_flask_server, daemon=True)
        flask_thread.start()
        
        # Wait a moment for Flask to start
        time.sleep(3)
        
        # Start React server
        start_react_server()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
