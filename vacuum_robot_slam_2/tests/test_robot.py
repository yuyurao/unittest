import unittest
from robot import VacuumRobot

class TestVacuumRobot(unittest.TestCase):
    def setUp(self):
        self.robot = VacuumRobot()

    def test_start_with_sufficient_battery(self):
        self.robot.start()
        self.assertTrue(self.robot.is_running)

    def test_start_with_depleted_battery(self):
        self.robot.battery_level = 0
        with self.assertRaises(ValueError):
            self.robot.start()

    def test_stop(self):
        self.robot.start()
        self.robot.stop()
        self.assertFalse(self.robot.is_running)

    def test_move_and_update_position(self):
        self.robot.start()
        self.robot.move("up")
        self.assertEqual(self.robot.get_position(), (0, 1))
        self.robot.move("right")
        self.assertEqual(self.robot.get_position(), (1, 1))
        self.robot.move("down")
        self.assertEqual(self.robot.get_position(), (1, 0))
        self.robot.move("left")
        self.assertEqual(self.robot.get_position(), (0, 0))

    def test_obstacle_detection(self):
        self.robot.start()
        self.robot.sensor.add_obstacle((0, 1))
        self.robot.move("up")
        self.assertEqual(self.robot.get_position(), (0, 0))  # Position should not change

    def test_get_map(self):
        self.robot.start()
        self.robot.move("up")
        self.robot.move("right")
        self.robot.move("down")
        expected_map = {(0, 0), (0, 1), (1, 1), (1, 0)}
        self.assertEqual(self.robot.get_map(), expected_map)

if __name__ == '__main__':
    unittest.main()
