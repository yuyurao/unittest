import unittest
import time
from robot.vacuum_robot import VacuumRobot

#Performance testing assesses the speed, responsiveness, and stability of the system under a workload.

class TestVacuumRobotPerformance(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()

    def test_performance(self):
        start_time = time.time()
        self.robot.start_cleaning()
        time.sleep(1)  # Simulate cleaning time
        self.robot.stop_cleaning()
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 2)  # Ensure the operation completes within 2 seconds

if __name__ == '__main__':
    unittest.main()
