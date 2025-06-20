"""
Mock motor control module for testing on non-Raspberry Pi systems.
Simulates motor control without requiring GPIO hardware.
"""

import time
import logging

logger = logging.getLogger(__name__)

class MotorControl:
    def __init__(self):
        logger.info("Mock MotorControl initialized (no GPIO required)")
        self.current_state = {
            'left_motor': {'direction': 'stop', 'speed': 0},
            'right_motor': {'direction': 'stop', 'speed': 0},
            'front_motor': {'direction': 'stop', 'speed': 0},
            'back_motor': {'direction': 'stop', 'speed': 0}
        }

    def forward(self, speed: int):
        """Mock forward movement"""
        logger.info(f"Mock: Moving forward at speed {speed}")
        self.current_state['left_motor'] = {'direction': 'forward', 'speed': speed}
        self.current_state['right_motor'] = {'direction': 'forward', 'speed': speed}

    def backward(self, speed: int):
        """Mock backward movement"""
        logger.info(f"Mock: Moving backward at speed {speed}")
        self.current_state['left_motor'] = {'direction': 'backward', 'speed': speed}
        self.current_state['right_motor'] = {'direction': 'backward', 'speed': speed}

    def turn_left(self, speed: int):
        """Mock left turn"""
        logger.info(f"Mock: Turning left at speed {speed}")
        self.current_state['left_motor'] = {'direction': 'backward', 'speed': speed}
        self.current_state['right_motor'] = {'direction': 'forward', 'speed': speed}

    def turn_right(self, speed: int):
        """Mock right turn"""
        logger.info(f"Mock: Turning right at speed {speed}")
        self.current_state['left_motor'] = {'direction': 'forward', 'speed': speed}
        self.current_state['right_motor'] = {'direction': 'backward', 'speed': speed}

    def up(self, speed: int):
        """Mock upward movement"""
        logger.info(f"Mock: Moving up at speed {speed}")
        self.current_state['front_motor'] = {'direction': 'up', 'speed': speed}
        self.current_state['back_motor'] = {'direction': 'up', 'speed': speed}

    def down(self, speed: int):
        """Mock downward movement"""
        logger.info(f"Mock: Moving down at speed {speed}")
        self.current_state['front_motor'] = {'direction': 'down', 'speed': speed}
        self.current_state['back_motor'] = {'direction': 'down', 'speed': speed}

    def pitch_up(self, speed: int):
        """Mock pitch up"""
        logger.info(f"Mock: Pitching up at speed {speed}")
        self.current_state['front_motor'] = {'direction': 'down', 'speed': speed}
        self.current_state['back_motor'] = {'direction': 'up', 'speed': speed}

    def pitch_down(self, speed: int):
        """Mock pitch down"""
        logger.info(f"Mock: Pitching down at speed {speed}")
        self.current_state['front_motor'] = {'direction': 'up', 'speed': speed}
        self.current_state['back_motor'] = {'direction': 'down', 'speed': speed}

    def stop(self):
        """Mock stop all motors"""
        logger.info("Mock: Stopping all motors")
        for motor in self.current_state:
            self.current_state[motor] = {'direction': 'stop', 'speed': 0}

    def cleanup(self):
        """Mock cleanup"""
        logger.info("Mock: Cleaning up motor control")
        self.stop()

    def get_status(self):
        """Get current motor status for debugging"""
        return self.current_state
