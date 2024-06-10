import unittest
from robot.vacuum_robot import VacuumRobot

#Security testing identifies vulnerabilities in the system to ensure data protection and prevent unauthorized access.

class TestVacuumRobotSecurity(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()

    def test_lock_keys(self):
        self.robot.lock_keys(True)
        self.assertTrue(self.robot.key_locked)
        self.robot.lock_keys(False)
        self.assertFalse(self.robot.key_locked)

if __name__ == '__main__':
    unittest.main()
