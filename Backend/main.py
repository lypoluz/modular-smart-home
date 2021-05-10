from commandListener import CommandListener
from importlib import import_module
from smartHomeController import Controller
import configLoader


class Application:
    _controller = dict()

    def __init__(self):
        plugins = configLoader.load("initial-plugins")
        for plugin in plugins:
            self.__load_plugin(plugin)

    def handle_command(self, cmd):
        group, target, data = cmd["group"], cmd["target"], cmd["data"]
        if group == "application":
            self.__application_command_handler(target, data)
        elif group in self._controller:
            for controller in self._controller[group].values():
                controller.write_data(target, data)
        else:
            print(f'There is no group "{group}"')

    def read_data(self, cmd):
        group = cmd["group"]
        out = dict()
        if group == "all":
            for g in self._controller.keys():
                data = self.__get_data_from_group(g)
                if data:
                    out[g] = data
        elif group in self._controller:
            data = self.__get_data_from_group(group)
            if data:
                out[group] = data
        else:
            print(f'There is no group "{group}"')
        return out

    def __get_data_from_group(self, group):
        out = list()
        if group in self._controller:
            for controller in self._controller[group].values():
                data = controller.read_data()
                if data:
                    out += data
            return out

    def __application_command_handler(self, target, data):
        if target == "load_plugin":
            self.__load_plugin(data)
        elif target == "unload_plugin":
            self.__unload_plugin(data)

    def __load_plugin(self, plugin_name):
        for group in self._controller.keys():
            if plugin_name in self._controller[group].keys():
                return

        module = import_module("." + plugin_name, "Controller")
        attrs = dir(module)
        plugin = None
        for sattr in attrs:
            attr = getattr(module, sattr)
            if issubclass(attr, Controller) and attr is not Controller:
                plugin = attr()
                break
        plugin.on_load()
        plugin_group = plugin.get_controller_group()
        if not (plugin_group in self._controller):
            self._controller[plugin_group] = dict()
        self._controller[plugin_group][plugin_name] = plugin
        print("loaded plugin: " + plugin_name)

    def __unload_plugin(self, plugin_name):
        for group in self._controller.keys():
            if plugin_name in self._controller[group].keys():
                self._controller[group].pop(plugin_name).on_unload()
                print("unloaded plugin: " + plugin_name)
                break


if __name__ == "__main__" and True:
    print("")
    print("")

    application = Application()

    server = configLoader.load("this-server")
    command_listener = CommandListener(server["address"], server["port"], application.handle_command,
                                       application.read_data)
    command_listener.start_listening()
