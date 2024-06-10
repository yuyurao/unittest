import unittest
from robot.vacuum_robot import VacuumRobot

#Acceptance testing ensures the system meets business requirements and is ready for deployment.

class TestVacuumRobotAcceptance(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()

    def test_user_acceptance(self):
        self.robot.set_operation_mode("vacuum")
        self.robot.set_speaker_volume(7)
        self.assertEqual(self.robot.operation_mode, "vacuum")
        self.assertEqual(self.robot.speaker_volume, 7)
        self.assertEqual(self.robot.start_cleaning(), "Cleaning started")

if __name__ == '__main__':
    unittest.main()
