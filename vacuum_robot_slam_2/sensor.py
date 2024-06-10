class Sensor:
    def __init__(self):
        self.obstacles = set()

    def add_obstacle(self, position):
        self.obstacles.add(position)

    def detect_obstacle(self, position):
        return position in self.obstacles
