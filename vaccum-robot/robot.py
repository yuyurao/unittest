class VacuumRobot:
    def __init__(self, battery_level=100):
        self.battery_level = battery_level
        self.is_running = False
        self.is_docked = False
        self.position = (0, 0)

    def start(self):
        if self.battery_level > 0:
            self.is_running = True
            self.is_docked = False
        else:
            raise ValueError("Cannot start. Battery is depleted.")

    def stop(self):
        self.is_running = False

    def move(self, direction):
        if not self.is_running:
            raise RuntimeError("Cannot move. The robot is not running.")
        if self.battery_level <= 0:
            raise RuntimeError("Cannot move. Battery is depleted.")
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
        self.battery_level -= 1

    def check_battery(self):
        return self.battery_level

    def dock(self):
        self.is_running = False
        self.is_docked = True
        self.position = (0, 0)
        self.charge(100 - self.battery_level)  # Change here to use the charge method


    def charge(self, amount):
        if amount < 0:
            raise ValueError("Charge amount cannot be negative.")
        self.battery_level = min(100, self.battery_level + amount)
