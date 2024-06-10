import unittest
from robot.vacuum_robot import VacuumRobot

#System testing involves testing the complete system to ensure it meets the specified requirements.

class TestVacuumRobotSystem(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()

    def test_system_behavior(self):
        self.robot.set_dnd("22:00", "07:00")
        self.robot.set_fan_speed(4)
        self.robot.start_cleaning()
        self.assertEqual(self.robot.dnd_timespan, ("22:00", "07:00"))
        self.assertEqual(self.robot.fan_speed, 4)
        self.assertEqual(self.robot.start_cleaning(), "Cleaning started")

if __name__ == '__main__':
    unittest.main()
