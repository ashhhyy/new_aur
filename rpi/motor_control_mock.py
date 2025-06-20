"""
Mock MotorControl class to bypass GPIO calls for development/testing without hardware.
"""

class MotorControl:
    def __init__(self):
        print("Mock MotorControl initialized - no hardware control")

    def forward(self, speed: int):
        print(f"Mock forward at speed {speed}")

    def backward(self, speed: int):
        print(f"Mock backward at speed {speed}")

    def turn_left(self, speed: int):
        print(f"Mock turn left at speed {speed}")

    def turn_right(self, speed: int):
        print(f"Mock turn right at speed {speed}")

    def up(self, speed: int):
        print(f"Mock up at speed {speed}")

    def down(self, speed: int):
        print(f"Mock down at speed {speed}")

    def pitch_up(self, speed: int):
        print(f"Mock pitch up at speed {speed}")

    def pitch_down(self, speed: int):
        print(f"Mock pitch down at speed {speed}")

    def stop(self):
        print("Mock stop motors")

    def cleanup(self):
        print("Mock cleanup GPIO")
