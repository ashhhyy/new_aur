# Autonomous Underwater Robot - Setup Guide

## Hardware Setup

### 1. Raspberry Pi Setup
1. Connect the components to Raspberry Pi:
   ```
   MPU6050 (I2C):
   - VCC -> 3.3V
   - GND -> GND
   - SCL -> GPIO 3 (SCL)
   - SDA -> GPIO 2 (SDA)

   L298N Motor Drivers:

   L298N #1 (Forward/Backward Motors):
   Motor A (Left):
   - IN1 -> GPIO 17 (Forward)
   - IN2 -> GPIO 18 (Backward)
   - ENA -> GPIO 27 (Speed Control)
   Motor B (Right):
   - IN3 -> GPIO 16 (Forward)
   - IN4 -> GPIO 19 (Backward)
   - ENB -> GPIO 26 (Speed Control)
   - Motor power -> 12V from battery via buck converter

   L298N #2 (Up/Down Motors):
   Motor A (Front):
   - IN1 -> GPIO 22 (Up)
   - IN2 -> GPIO 23 (Down)
   - ENA -> GPIO 24 (Speed Control)
   Motor B (Back):
   - IN3 -> GPIO 12 (Up)
   - IN4 -> GPIO 13 (Down)
   - ENB -> GPIO 6 (Speed Control)
   - Motor power -> 12V from battery via buck converter

   Note: Each L298N motor driver can control two DC motors independently:
   - IN1/IN2 and ENA control Motor A
   - IN3/IN4 and ENB control Motor B
   This setup allows for:
   - Independent left/right motor control for turning
   - Independent front/back vertical motor control for pitch adjustment

   Ultrasonic Sensors:
   Front Sensor:
   - TRIG -> GPIO 5
   - ECHO -> GPIO 25
   - VCC -> 5V
   - GND -> GND

   Back Sensor:
   - TRIG -> GPIO 7
   - ECHO -> GPIO 8
   - VCC -> 5V
   - GND -> GND

   Bottom Sensor:
   - TRIG -> GPIO 20
   - ECHO -> GPIO 21
   - VCC -> 5V
   - GND -> GND
   ```

2. Power Supply:
   - Connect LM2596S buck converter input to 11.1V battery
   - Adjust output to 5V for Raspberry Pi
   - Connect second buck converter for 12V motor power

### 2. ESP32-CAM Setup
1. Connect components:
   ```
   Programming Connection:
   - 5V -> USB-UART 5V
   - GND -> USB-UART GND
   - U0R -> USB-UART TX
   - U0T -> USB-UART RX
   
   SD Card:
   - Insert microSD card (FAT32 formatted)
   ```

2. Camera positioning:
   - Mount camera in waterproof housing
   - Ensure clear view through housing window

## Software Installation

### 1. Raspberry Pi Software
1. Install OS:
   ```bash
   # Download and flash Raspberry Pi OS Lite to SD card
   # Boot Raspberry Pi and perform initial setup
   ```

2. Update system packages:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

3. Enable I2C:
   ```bash
   sudo raspi-config
   # Navigate to Interface Options -> I2C -> Enable
   ```

4. Install repository:
   ```bash
   git clone https://github.com/yourusername/autonomous-underwater-robot.git
   cd autonomous-underwater-robot
   chmod +x setup.sh
   ./setup.sh
   ```

   **Note**: The setup script will automatically:
   - Install Node.js and npm if not present
   - Handle Python package installation with fallback options
   - Configure hardware permissions with error handling

### 2. ESP32-CAM Programming
1. Arduino IDE setup:
   - Install Arduino IDE
   - Add ESP32 board support URL: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   - Install ESP32 board package
   - Select "AI Thinker ESP32-CAM" board

2. Upload code:
   ```
   - Open esp32-cam/esp32_cam_capture.ino
   - Select correct COM port
   - Upload sketch
   ```

### 3. Web Dashboard Setup
1. Install Node.js and npm
2. Setup dashboard:
   ```bash
   cd web-dashboard
   npm install
   npm start
   ```

## Running the System

### On Raspberry Pi (Production)

1. Start Raspberry Pi services:
   ```bash
   cd rpi
   python app.py
   ```

2. Power up ESP32-CAM:
   - It will automatically start capturing images
   - Check SD card for saved images

3. Access web dashboard:
   - Open browser to http://localhost:3000
   - Use dashboard to control robot

### On PC (Development/Testing)

The project includes mock modules that simulate hardware components, allowing you to test and develop the web interface on a PC without requiring actual hardware.

#### Prerequisites
1. Python 3.7 or higher
2. Node.js and npm (download from https://nodejs.org/)
3. Git (for cloning the repository)

#### Option 1: Using run_on_pc.py (Cross-platform)
```bash
# Activate virtual environment first (if using one)
python run_on_pc.py
```
This script will:
1. Detect your operating system
2. Start the Flask backend with mock hardware
3. Try multiple methods to start the React frontend
4. Provide manual instructions if automatic startup fails

#### Option 2: Using run_on_pc_improved.bat (Windows)
```bash
# Simply double-click run_on_pc_improved.bat
# Or run from command prompt:
run_on_pc_improved.bat
```
The batch file will:
1. Check for Node.js and npm installation
2. Display Node.js and npm versions
3. Activate virtual environment if available
4. Start Flask backend in a new window
5. Install React dependencies if needed
6. Start React frontend in a new window

#### Manual Start
1. Start Flask backend with mock modules:
   ```bash
   cd rpi
   python app.py
   ```
   The app will automatically detect it's running on a PC and use mock hardware modules.

2. Start React frontend:
   ```bash
   cd web-dashboard
   npm start
   ```

3. Access the web interface:
   - Backend API: http://localhost:5000
   - Frontend Dashboard: http://localhost:3000

Note: When running on PC, all hardware functions (motors, sensors) are simulated. This is useful for:
- Developing and testing the web interface
- Testing autonomous logic algorithms
- Debugging without requiring physical hardware

## Testing

1. Test motor control:
   ```bash
   # In Python shell
   from motor_control import MotorControl
   mc = MotorControl()
   
   # Test basic movement
   mc.forward(50)     # Move forward at 50% speed
   mc.backward(30)    # Move backward at 30% speed
   mc.turn_left(40)   # Turn left at 40% speed
   mc.turn_right(40)  # Turn right at 40% speed
   
   # Test vertical movement
   mc.up(60)          # Move up at 60% speed
   mc.down(60)        # Move down at 60% speed
   mc.pitch_up(30)    # Pitch nose up at 30% speed
   mc.pitch_down(30)  # Pitch nose down at 30% speed
   
   mc.stop()          # Stop all motors
   mc.cleanup()       # Clean up GPIO when done
   ```

2. Test sensors:
   ```bash
   # In Python shell
   from sensors import MPU6050, UltrasonicSensor
   mpu = MPU6050()
   print(mpu.get_orientation())
   ```

3. Test ESP32-CAM:
   - Check SD card for new images
   - Verify timestamps in filenames

## Troubleshooting

### 1. Setup Issues

**Flask Installation Hash Mismatch:**
```bash
# If you see hash mismatch errors, the updated requirements.txt should fix this
# If issues persist, try:
pip install --no-deps Flask==2.3.3
```

**Node.js/npm Not Found:**
```bash
# The setup script now installs Node.js automatically
# If manual installation is needed:
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**SPI Module Not Found:**
```bash
# This warning is normal if SPI devices aren't used
# To check available modules:
lsmod | grep spi
```

### 2. Hardware Issues

**Motor Issues:**
- Check voltage at motor terminals (should be ~12V)
- Verify GPIO connections match the pin assignments
- Test L298N driver LEDs (should light up when active)
- Ensure buck converter output is stable

**Sensor Issues:**
- Run i2cdetect to check MPU6050: `sudo i2cdetect -y 1`
- Check ultrasonic sensor wiring and power (5V required)
- Verify power supply voltages with multimeter

### 3. Software Issues

**Communication Issues:**
- Check network connectivity: `ping localhost`
- Verify Flask server is running: `ps aux | grep python`
- Check web dashboard console for errors (F12 in browser)
- Ensure ports 5000 (Flask) and 3000 (React) are available

**Permission Issues:**
```bash
# Add user to required groups:
sudo usermod -a -G gpio,i2c,spi $USER
# Then logout and login again
```

## Safety Checks

1. Before submerging:
   - Verify all seals
   - Check buoyancy
   - Test emergency stop

2. During operation:
   - Monitor battery voltage
   - Watch for unusual behavior
   - Keep safety float ready

3. After use:
   - Dry all components
   - Check for water ingress
   - Recharge battery
