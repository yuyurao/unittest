import unittest
from robot.vacuum_robot import VacuumRobot

#Usability testing evaluates how user-friendly the software is, focusing on the user interface and user experience.

class TestVacuumRobotUsability(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()

    def test_usability(self):
        self.robot.change_voice_pack("friendly_voice")
        self.assertEqual(self.robot.voice_pack, "friendly_voice")
        self.robot.set_speaker_volume(5)
        self.assertEqual(self.robot.speaker_volume, 5)

if __name__ == '__main__':
    unittest.main()
