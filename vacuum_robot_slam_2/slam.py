class SLAM:
    def __init__(self):
        self.position = (0, 0)
        self.map = set()
        self.map.add(self.position)

    def update_position(self, new_position):
        self.position = new_position
        self.map.add(new_position)

    def get_position(self):
        return self.position

    def get_map(self):
        return self.map
