from robot import VacuumRobot

def main():
    robot = VacuumRobot()
    robot.start()

    # Simulate some movements
    robot.move("up")
    robot.move("up")
    robot.move("right")
    robot.move("right")
    robot.move("down")
    robot.move("left")

    # Display the map and current position
    print("Current Position:", robot.get_position())
    print("Map:", robot.get_map())

if __name__ == "__main__":
    main()
