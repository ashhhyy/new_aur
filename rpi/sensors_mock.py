"""
Mock sensors module to bypass smbus and GPIO for development/testing without hardware.
"""

import time

class MPU6050:
    def __init__(self, bus=1, address=0x68):
        print("Mock MPU6050 initialized")

    def get_orientation(self):
        # Return dummy orientation data
        return {'pitch': 0.0, 'roll': 0.0, 'yaw': 0.0}

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        print(f"Mock UltrasonicSensor initialized on pins {trigger_pin}, {echo_pin}")

    def get_distance(self):
        # Return dummy distance
        return 100.0
