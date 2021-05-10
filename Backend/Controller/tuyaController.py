import time
from tuyapy import TuyaApi
from smartHomeController import Controller
import configLoader

# turn off:
# device.turn_off()

# turn on:
# device.turn_on()

# change_color:
# h, s, v, t = colors.getHsv()
# s = int((s / 255 * 100))
# if s < 60:
#     s = 60
# device.set_color([h, s, 100])


class TuyaController(Controller):

    tuya = None

    def get_controller_group(self):
        return "smart_switches"

    def on_load(self):
        data = configLoader.load("tuya")
        self.tuya = TuyaApi()
        self.__try_connect(data["email"], data["password"], data["country_code"])


    def write_data(self, target, data):
        device = self.__get_device(target)

        if data == "true":
            device.turn_on()
        elif data == "false":
            device.turn_off()

    def read_data(self):
        self.tuya.discover_devices()
        devices = self.tuya.get_all_devices()
        devices_out = list()
        for device in devices:
            if device.dev_type != "switch":
                continue
            devices_out.append({
                "id": device.object_id(),
                "name": device.name(),
                "type": "switch",
                "state": device.data.get("state")
            })
        return devices_out


    def __get_device(self, name_or_id):
        device = self.tuya.get_device_by_id(name_or_id)
        if device:
            return device

        devices = self.tuya.get_all_devices()
        for device in devices:
            if device.name() == name_or_id:
                return device


    def __try_connect(self, email, password, country_code):
        connected = False
        retry_attempts = 0
        while not connected:
            retry_attempts += 1
            try:
                try:
                    self.tuya.init(email, password, country_code, 'tuya')
                    connected = True
                    print("Tuya connection successful")
                except:
                    print(f"Cannot connect to Tuya. --{retry_attempts}\nTrying again in 15 seconds...")
                    time.sleep(15)
            except KeyboardInterrupt:
                print("Keyboard interrupt")
                exit(0)
            if retry_attempts > 5:
                print("You should check the credentials")
