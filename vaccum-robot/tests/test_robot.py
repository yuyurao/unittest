import unittest
from unittest.mock import patch
from robot import VacuumRobot

class TestVacuumRobot(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()

    def test_start_with_sufficient_battery(self):
        self.robot.start()
        self.assertTrue(self.robot.is_running)
        self.assertFalse(self.robot.is_docked)

    def test_start_with_depleted_battery(self):
        self.robot.battery_level = 0
        with self.assertRaises(ValueError):
            self.robot.start()

    def test_stop(self):
        self.robot.start()
        self.robot.stop()
        self.assertFalse(self.robot.is_running)

    def test_move_when_running(self):
        self.robot.start()
        self.robot.move("up")
        self.assertEqual(self.robot.position, (0, 1))
        self.robot.move("right")
        self.assertEqual(self.robot.position, (1, 1))
        self.robot.move("down")
        self.assertEqual(self.robot.position, (1, 0))
        self.robot.move("left")
        self.assertEqual(self.robot.position, (0, 0))

    def test_move_when_not_running(self):
        with self.assertRaises(RuntimeError):
            self.robot.move("up")

    def test_move_with_depleted_battery(self):
        self.robot.start()
        self.robot.battery_level = 0
        with self.assertRaises(RuntimeError):
            self.robot.move("up")

    def test_invalid_direction(self):
        self.robot.start()
        with self.assertRaises(ValueError):
            self.robot.move("diagonal")

    def test_battery_consumption(self):
        initial_battery = self.robot.check_battery()
        self.robot.start()
        self.robot.move("up")
        self.assertEqual(self.robot.check_battery(), initial_battery - 1)

    def test_dock(self):
        self.robot.start()
        self.robot.move("up")
        self.robot.dock()
        self.assertFalse(self.robot.is_running)
        self.assertTrue(self.robot.is_docked)
        self.assertEqual(self.robot.position, (0, 0))
        self.assertEqual(self.robot.check_battery(), 100)

    def test_charge_battery(self):
        self.robot.battery_level = 50
        self.robot.charge(30)
        self.assertEqual(self.robot.check_battery(), 80)

    def test_overcharge_battery(self):
        self.robot.battery_level = 90
        self.robot.charge(20)
        self.assertEqual(self.robot.check_battery(), 100)

    def test_charge_with_negative_amount(self):
        with self.assertRaises(ValueError):
            self.robot.charge(-10)

    @patch.object(VacuumRobot, 'charge')
    def test_dock_and_charge(self, mock_charge):
        self.robot.start()
        self.robot.move("up")
        current_battery_level = self.robot.check_battery()
        self.robot.dock()
        expected_charge_amount = 100 - current_battery_level
        mock_charge.assert_called_with(expected_charge_amount)  # Mock the charge method to verify it was called

if __name__ == '__main__':
    unittest.main()
