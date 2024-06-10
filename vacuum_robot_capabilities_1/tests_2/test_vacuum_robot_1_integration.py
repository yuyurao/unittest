import unittest
from robot.vacuum_robot import VacuumRobot

#Integration testing involves verifying that different modules or services work together as expected.

class TestVacuumRobotIntegration(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()
        self.robot.auto_empty_dock_auto_empty_control(True)
        self.robot.set_fan_speed(3)

    def test_integration_auto_empty_and_fan_speed(self):
        self.assertTrue(self.robot.auto_empty_enabled)
        self.assertEqual(self.robot.fan_speed, 3)

    def test_integration_location_and_snapshot(self):
        self.robot.go_to_location(5, 10)
        self.assertEqual(self.robot.current_location, (5, 10))

        snapshot = self.robot.take_map_snapshot()
        self.assertIn(snapshot, self.robot.list_map_snapshots())

if __name__ == '__main__':
    unittest.main()
