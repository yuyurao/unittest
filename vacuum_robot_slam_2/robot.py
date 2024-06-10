from slam import SLAM
from sensor import Sensor

class VacuumRobot:
    def __init__(self):
        self.slam = SLAM()
        self.sensor = Sensor()
        self.is_running = False
        self.battery_level = 100

    def start(self):
        if self.battery_level > 0:
            self.is_running = True
        else:
            raise ValueError("Cannot start. Battery is depleted.")

    def stop(self):
        self.is_running = False

    def move(self, direction):
        if not self.is_running:
            raise RuntimeError("Cannot move. The robot is not running.")
        x, y = self.slam.get_position()
        if direction == "up":
            new_position = (x, y + 1)
        elif direction == "down":
            new_position = (x, y - 1)
        elif direction == "left":
            new_position = (x - 1, y)
        elif direction == "right":
            new_position = (x + 1, y)
        else:
            raise ValueError("Invalid direction.")

        if not self.sensor.detect_obstacle(new_position):
            self.slam.update_position(new_position)
        else:
            print("Obstacle detected. Cannot move to", new_position)

    def get_map(self):
        return self.slam.get_map()

    def get_position(self):
        return self.slam.get_position()
