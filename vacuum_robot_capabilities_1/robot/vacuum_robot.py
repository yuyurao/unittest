class VacuumRobot:
    def __init__(self):
        self.auto_empty_enabled = False
        self.carpet_mode_enabled = False
        self.carpet_sensor_mode = "ignore"
        self.dnd_timespan = None
        self.fan_speed = 1
        self.water_usage = 1
        self.current_location = (0, 0)
        self.map_snapshots = []
        self.virtual_restrictions = []
        self.consumables = {"filter": 100, "brush": 100}
        self.current_statistics = {"area": 0, "runtime": 0}
        self.total_statistics = {"area": 0, "runtime": 0, "cleanup_count": 0}
        self.speaker_volume = 5
        self.voice_pack = "default"
        self.operation_mode = "vacuum"
        self.key_locked = False
        self.located = False
        self.wifi_details = {}

    def auto_empty_dock_auto_empty_control(self, enable: bool):
        self.auto_empty_enabled = enable

    def auto_empty_dock_manual_trigger(self):
        if self.auto_empty_enabled:
            return "Dustbin emptied"
        return "Auto-empty disabled"

    def set_carpet_mode(self, enable: bool):
        self.carpet_mode_enabled = enable

    def set_carpet_sensor_mode(self, mode: str):
        if mode in ["ignore", "avoid", "lift"]:
            self.carpet_sensor_mode = mode
        else:
            raise ValueError("Invalid carpet sensor mode")

    def set_dnd(self, start_time: str, end_time: str):
        self.dnd_timespan = (start_time, end_time)

    def set_fan_speed(self, speed: int):
        if 1 <= speed <= 5:
            self.fan_speed = speed
        else:
            raise ValueError("Invalid fan speed")

    def set_water_usage(self, usage: int):
        if 1 <= usage <= 5:
            self.water_usage = usage
        else:
            raise ValueError("Invalid water usage")

    def go_to_location(self, x: int, y: int):
        self.current_location = (x, y)

    def take_map_snapshot(self):
        snapshot = f"Snapshot-{len(self.map_snapshots) + 1}"
        self.map_snapshots.append(snapshot)
        return snapshot

    def list_map_snapshots(self):
        return self.map_snapshots

    def reset_map(self):
        self.map_snapshots = []

    def configure_virtual_restrictions(self, restrictions):
        self.virtual_restrictions = restrictions

    def reset_consumable(self, consumable):
        if consumable in self.consumables:
            self.consumables[consumable] = 100

    def get_current_statistics(self):
        return self.current_statistics

    def get_total_statistics(self):
        return self.total_statistics

    def set_speaker_volume(self, volume: int):
        if 0 <= volume <= 10:
            self.speaker_volume = volume
        else:
            raise ValueError("Invalid volume level")

    def change_voice_pack(self, voice_pack: str):
        self.voice_pack = voice_pack

    def set_operation_mode(self, mode: str):
        if mode in ["vacuum", "mop", "both"]:
            self.operation_mode = mode
        else:
            raise ValueError("Invalid operation mode")

    def lock_keys(self, lock: bool):
        self.key_locked = lock

    def locate(self):
        self.located = True
        return "Robot is here!"

    def start_cleaning(self):
        return "Cleaning started"

    def pause_cleaning(self):
        return "Cleaning paused"

    def stop_cleaning(self):
        return "Cleaning stopped"

    def return_to_home(self):
        return "Returning to home"

    def manual_control(self, direction: str):
        return f"Moving {direction}"

    def configure_wifi(self, ssid, password):
        self.wifi_details = {'ssid': ssid, 'password': password}

    def get_wifi_details(self):
        return self.wifi_details