#!/bin/bash

echo "Setting up Autonomous Underwater Robot..."

# Check if running on Raspberry Pi
if ! grep -q "Raspberry Pi" /proc/cpuinfo; then
    echo "Warning: This script is designed for Raspberry Pi. Some features may not work on other systems."
fi

# Install Node.js and npm if not present
echo "Checking Node.js and npm installation..."
if ! command -v node &> /dev/null; then
    echo "Installing Node.js and npm..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
    echo "Node.js version: $(node --version)"
    echo "npm version: $(npm --version)"
else
    echo "Node.js already installed: $(node --version)"
    echo "npm already installed: $(npm --version)"
fi

# Create virtual environment and install Python dependencies
echo "Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# Install Python packages with better error handling
echo "Installing Python packages..."
if ! pip install -r requirements.txt; then
    echo "Warning: Some Python packages failed to install. Trying alternative installation..."
    # Try installing packages individually to identify problematic ones
    pip install Flask Flask-CORS
    pip install RPi.GPIO || echo "Warning: RPi.GPIO installation failed (normal on non-Pi systems)"
    pip install adafruit-circuitpython-mpu6050 adafruit-blinka || echo "Warning: Adafruit libraries installation failed"
    pip install Pillow numpy
fi

# Setup web dashboard
echo "Setting up web dashboard..."
cd web-dashboard
if ! npm install; then
    echo "Error: npm install failed. Please check your Node.js installation."
    exit 1
fi
cd ..

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p images
mkdir -p logs

# Configure permissions for hardware access
echo "Configuring hardware permissions..."
if grep -q "Raspberry Pi" /proc/cpuinfo; then
    # Enable I2C if not already enabled
    if ! grep -q "^i2c-dev" /etc/modules; then
        echo "i2c-dev" | sudo tee -a /etc/modules
    fi
    
    # Enable SPI if not already enabled (optional for this project)
    if ! grep -q "^spi-dev" /etc/modules; then
        echo "spi-dev" | sudo tee -a /etc/modules
    fi
    
    # Add user to required groups
    sudo usermod -a -G gpio,i2c,spi $USER
    
    # Reload modules with error handling
    echo "Loading I2C module..."
    sudo modprobe i2c-dev || echo "Warning: i2c-dev module load failed"
    
    echo "Loading SPI module..."
    sudo modprobe spi-dev || echo "Warning: spi-dev module load failed (this may be normal)"
fi

# Create systemd service for auto-start (only on Raspberry Pi)
if grep -q "Raspberry Pi" /proc/cpuinfo; then
    echo "Creating systemd service..."
    sudo tee /etc/systemd/system/underwater-robot.service > /dev/null << EOL
[Unit]
Description=Autonomous Underwater Robot Service
After=network.target

[Service]
ExecStart=$(pwd)/venv/bin/python $(pwd)/rpi/app.py
WorkingDirectory=$(pwd)
User=$USER
Environment=PYTHONPATH=$(pwd)
Restart=always

[Install]
WantedBy=multi-user.target
EOL

    # Enable and start service
    sudo systemctl enable underwater-robot
    sudo systemctl start underwater-robot
fi

echo "Setup complete!"
echo "To start the application:"
echo "1. Flask API: source venv/bin/activate && python rpi/app.py"
echo "2. Web Dashboard: cd web-dashboard && npm start"
