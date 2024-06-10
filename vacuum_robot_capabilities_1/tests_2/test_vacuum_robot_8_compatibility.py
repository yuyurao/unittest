import unittest
from robot.vacuum_robot import VacuumRobot

#Compatibility testing ensures the software works across different environments.

class TestVacuumRobotCompatibility(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()

    def test_wifi_configuration(self):
        self.robot.configure_wifi("HomeNetwork", "password123")
        wifi_details = self.robot.get_wifi_details()
        self.assertEqual(wifi_details['ssid'], "HomeNetwork")
        self.assertEqual(wifi_details['password'], "password123")

if __name__ == '__main__':
    unittest.main()
