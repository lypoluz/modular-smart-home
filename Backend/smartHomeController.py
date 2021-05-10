from abc import ABC, abstractmethod

class Controller(ABC):
    def on_load(self):
        print("meh")
        pass

    def on_unload(self):
        pass

    @abstractmethod
    def get_controller_group(self):
        pass

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, target, data):
        pass

