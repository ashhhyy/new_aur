"""
Mock autonomous logic module for testing on non-Raspberry Pi systems.
Simulates autonomous behavior without requiring hardware.
"""

import time
import logging
import random

logger = logging.getLogger(__name__)

class AutonomousLogic:
    def __init__(self, motor_control, mpu6050, front_sensor, back_sensor, bottom_sensor):
        self.motor_control = motor_control
        self.mpu6050 = mpu6050
        self.front_sensor = front_sensor
        self.back_sensor = back_sensor
        self.bottom_sensor = bottom_sensor
        self.running = False
        logger.info("Mock AutonomousLogic initialized")

    def run(self):
        """Simulate autonomous behavior"""
        try:
            # Get mock sensor data
            orientation = self.mpu6050.get_orientation()
            front_distance = self.front_sensor.get_distance()
            back_distance = self.back_sensor.get_distance()
            bottom_distance = self.bottom_sensor.get_distance()

            logger.info(f"Mock sensors - Orientation: {orientation}, "
                       f"Front: {front_distance:.1f}cm, Back: {back_distance:.1f}cm, "
                       f"Bottom: {bottom_distance:.1f}cm")

            # Simulate simple autonomous behavior
            if front_distance < 30:
                logger.info("Mock: Obstacle detected in front, turning right")
                self.motor_control.turn_right(40)
            elif bottom_distance < 20:
                logger.info("Mock: Too close to bottom, moving up")
                self.motor_control.up(30)
            elif bottom_distance > 150:
                logger.info("Mock: Too far from bottom, moving down")
                self.motor_control.down(30)
            else:
                # Random movement for demonstration
                action = random.choice(['forward', 'turn_left', 'turn_right', 'stop'])
                if action == 'forward':
                    self.motor_control.forward(50)
                elif action == 'turn_left':
                    self.motor_control.turn_left(40)
                elif action == 'turn_right':
                    self.motor_control.turn_right(40)
                else:
                    self.motor_control.stop()
                
                logger.info(f"Mock: Autonomous action - {action}")

        except Exception as e:
            logger.error(f"Mock autonomous logic error: {e}")
            self.motor_control.stop()
