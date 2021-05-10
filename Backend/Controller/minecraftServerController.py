import os
import subprocess

from smartHomeController import Controller
import configLoader



class MinecraftController(Controller):

    location = None
    server_name = None
    screen_name = None
    jar_file = None
    Xms = None
    Xmx = None

    def get_controller_group(self):
        return "minecraft_server"

    def on_load(self):
        data = configLoader.load("minecraft")
        self.location = data["location"]
        self.jar_file = data["jar_file"]
        self.server_name = data["server_name"]
        self.screen_name = data["screen_name"]
        self.Xms = data["Xms"]
        self.Xmx = data["Xmx"]

    def read_data(self):
        return [{
            "id": self.get_id(),
            "name": self.server_name,
            "type": "switch",
            "state": str(self.get_state())
        }]


    def write_data(self, target, data: str):
        if target == self.get_id():
            if data.lower() == "true":
                subprocess.run(f"screen -dmS {self.screen_name} java -Xms{self.Xms} -Xmx{self.Xmx} -jar {self.location}{self.jar_file} --nogui", shell=True)
            elif data.lower() == "false":
                subprocess.run(f'screen -S {self.screen_name} -X stuff "stop\015"', shell=True)
        return

    def get_id(self):
        return f"|{self.location}|-|{self.server_name}|-|{self.screen_name}|"

    def get_state(self):
        output = subprocess.run('screen -ls', shell=True, capture_output=True, text=True).stdout
        print(f"{output}")
        print(f"{self.screen_name}")
        return ('.'+self.screen_name) in output



