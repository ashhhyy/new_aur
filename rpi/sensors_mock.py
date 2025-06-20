"""
Mock sensors module for testing on non-Raspberry Pi systems.
Simulates MPU6050 and ultrasonic sensors without requiring hardware.
"""

import time
import random
import logging
from typing import Tuple

logger = logging.getLogger(__name__)

class MPU6050:
    def __init__(self):
        logger.info("Mock MPU6050 initialized")
        self.simulated_orientation = {'x': 0.0, 'y': 0.0, 'z': 0.0}

    def get_orientation(self) -> dict:
        """Simulate orientation data with small random variations"""
        self.simulated_orientation = {
            'x': self.simulated_orientation['x'] + random.uniform(-0.1, 0.1),
            'y': self.simulated_orientation['y'] + random.uniform(-0.1, 0.1),
            'z': self.simulated_orientation['z'] + random.uniform(-0.1, 0.1)
        }
        return self.simulated_orientation

class UltrasonicSensor:
    def __init__(self, trigger_pin: int, echo_pin: int):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.simulated_distance = 100.0  # Start at 100cm
        logger.info(f"Mock Ultrasonic Sensor initialized (TRIG: {trigger_pin}, ECHO: {echo_pin})")

    def get_distance(self) -> float:
        """Simulate distance measurement with small random variations"""
        # Add some noise to the simulated distance
        self.simulated_distance += random.uniform(-5, 5)
        # Keep the distance within realistic bounds (5cm to 200cm)
        self.simulated_distance = max(5, min(200, self.simulated_distance))
        return self.simulated_distance
