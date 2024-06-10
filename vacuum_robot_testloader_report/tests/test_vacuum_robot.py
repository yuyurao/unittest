import unittest
from robot.vacuum_robot import VacuumRobot

class TestVacuumRobot(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()

    def test_auto_empty_dock_auto_empty_control(self):
        self.robot.auto_empty_dock_auto_empty_control(True)
        self.assertTrue(self.robot.auto_empty_enabled)

    def test_auto_empty_dock_manual_trigger(self):
        self.robot.auto_empty_dock_auto_empty_control(True)
        result = self.robot.auto_empty_dock_manual_trigger()
        self.assertEqual(result, "Dustbin emptied")

if __name__ == '__main__':
    unittest.main()
