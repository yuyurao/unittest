from robot import VacuumRobot

def main():
    robot = VacuumRobot()
    robot.start()

    # Add some obstacles
    robot.sensor.add_obstacle((1, 1))
    robot.sensor.add_obstacle((2, 2))

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
