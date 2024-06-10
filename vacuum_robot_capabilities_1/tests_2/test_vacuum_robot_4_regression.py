import unittest
from robot.vacuum_robot import VacuumRobot

#Regression testing ensures that new code changes do not negatively impact existing functionality.

class TestVacuumRobotRegression(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()
        self.robot.set_fan_speed(3)

    def test_fan_speed(self):
        self.assertEqual(self.robot.fan_speed, 3)
        self.robot.set_fan_speed(5)
        self.assertEqual(self.robot.fan_speed, 5)

if __name__ == '__main__':
    unittest.main()
