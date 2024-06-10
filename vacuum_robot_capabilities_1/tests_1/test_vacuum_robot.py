import unittest
from robot.vacuum_robot import VacuumRobot

class TestVacuumRobotCapabilities(unittest.TestCase):

    def setUp(self):
        self.robot = VacuumRobot()

    def test_auto_empty_dock_auto_empty_control(self):
        self.robot.auto_empty_dock_auto_empty_control(True)
        self.assertTrue(self.robot.auto_empty_enabled)

        self.robot.auto_empty_dock_auto_empty_control(False)
        self.assertFalse(self.robot.auto_empty_enabled)

    def test_auto_empty_dock_manual_trigger(self):
        self.robot.auto_empty_dock_auto_empty_control(True)
        self.assertEqual(self.robot.auto_empty_dock_manual_trigger(), "Dustbin emptied")

        self.robot.auto_empty_dock_auto_empty_control(False)
        self.assertEqual(self.robot.auto_empty_dock_manual_trigger(), "Auto-empty disabled")

    def test_set_carpet_mode(self):
        self.robot.set_carpet_mode(True)
        self.assertTrue(self.robot.carpet_mode_enabled)

        self.robot.set_carpet_mode(False)
        self.assertFalse(self.robot.carpet_mode_enabled)

    def test_set_carpet_sensor_mode(self):
        self.robot.set_carpet_sensor_mode("avoid")
        self.assertEqual(self.robot.carpet_sensor_mode, "avoid")

        with self.assertRaises(ValueError):
            self.robot.set_carpet_sensor_mode("invalid_mode")

    def test_set_dnd(self):
        self.robot.set_dnd("22:00", "07:00")
        self.assertEqual(self.robot.dnd_timespan, ("22:00", "07:00"))

    def test_set_fan_speed(self):
        self.robot.set_fan_speed(3)
        self.assertEqual(self.robot.fan_speed, 3)

        with self.assertRaises(ValueError):
            self.robot.set_fan_speed(6)

    def test_set_water_usage(self):
        self.robot.set_water_usage(3)
        self.assertEqual(self.robot.water_usage, 3)

        with self.assertRaises(ValueError):
            self.robot.set_water_usage(6)

    def test_go_to_location(self):
        self.robot.go_to_location(5, 10)
        self.assertEqual(self.robot.current_location, (5, 10))

    def test_take_map_snapshot(self):
        snapshot = self.robot.take_map_snapshot()
        self.assertIn(snapshot, self.robot.list_map_snapshots())

    def test_reset_map(self):
        self.robot.take_map_snapshot()
        self.robot.reset_map()
        self.assertEqual(self.robot.list_map_snapshots(), [])

    def test_configure_virtual_restrictions(self):
        restrictions = [{"type": "wall", "coordinates": [(0, 0), (1, 1)]}]
        self.robot.configure_virtual_restrictions(restrictions)
        self.assertEqual(self.robot.virtual_restrictions, restrictions)

    def test_reset_consumable(self):
        self.robot.reset_consumable("filter")
        self.assertEqual(self.robot.consumables["filter"], 100)

    def test_get_current_statistics(self):
        stats = self.robot.get_current_statistics()
        self.assertEqual(stats, {"area": 0, "runtime": 0})

    def test_get_total_statistics(self):
        stats = self.robot.get_total_statistics()
        self.assertEqual(stats, {"area": 0, "runtime": 0, "cleanup_count": 0})

    def test_set_speaker_volume(self):
        self.robot.set_speaker_volume(7)
        self.assertEqual(self.robot.speaker_volume, 7)

        with self.assertRaises(ValueError):
            self.robot.set_speaker_volume(11)

    def test_change_voice_pack(self):
        self.robot.change_voice_pack("new_pack")
        self.assertEqual(self.robot.voice_pack, "new_pack")

    def test_set_operation_mode(self):
        self.robot.set_operation_mode("mop")
        self.assertEqual(self.robot.operation_mode, "mop")

        with self.assertRaises(ValueError):
            self.robot.set_operation_mode("invalid_mode")

    def test_lock_keys(self):
        self.robot.lock_keys(True)
        self.assertTrue(self.robot.key_locked)

    def test_locate(self):
        self.assertEqual(self.robot.locate(), "Robot is here!")
        self.assertTrue(self.robot.located)

    def test_start_cleaning(self):
        self.assertEqual(self.robot.start_cleaning(), "Cleaning started")

    def test_pause_cleaning(self):
        self.assertEqual(self.robot.pause_cleaning(), "Cleaning paused")

    def test_stop_cleaning(self):
        self.assertEqual(self.robot.stop_cleaning(), "Cleaning stopped")

    def test_return_to_home(self):
        self.assertEqual(self.robot.return_to_home(), "Returning to home")

    def test_manual_control(self):
        self.assertEqual(self.robot.manual_control("forward"), "Moving forward")

if __name__ == '__main__':
    unittest.main()
