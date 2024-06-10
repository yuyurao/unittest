class VacuumRobot:
    def __init__(self):
        self.wifi_details = {}
        self.auto_empty_enabled = False

    def configure_wifi(self, ssid, password):
        self.wifi_details = {'ssid': ssid, 'password': password}

    def get_wifi_details(self):
        return self.wifi_details

    def auto_empty_dock_auto_empty_control(self, enable):
        self.auto_empty_enabled = enable

    def auto_empty_dock_manual_trigger(self):
        if self.auto_empty_enabled:
            return "Dustbin emptied"
        else:
            return "Auto empty disabled"
