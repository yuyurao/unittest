from slam import SLAM

class VacuumRobot:
    def __init__(self):
        self.slam = SLAM()
        self.is_running = False
        self.position = (0, 0)
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
        x, y = self.position
        if direction == "up":
            self.position = (x, y + 1)
        elif direction == "down":
            self.position = (x, y - 1)
        elif direction == "left":
            self.position = (x - 1, y)
        elif direction == "right":
            self.position = (x + 1, y)
        else:
            raise ValueError("Invalid direction.")
        self.slam.update_position(self.position)

    def get_map(self):
        return self.slam.get_map()

    def get_position(self):
        return self.slam.get_position()
