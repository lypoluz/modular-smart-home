import json
from socket import socket, AF_INET, SOCK_STREAM
import sys
import configLoader


def establish_socket():
    data = configLoader.load("this-server")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((data["address"], data["port"]))
    return sock


def load_plugin(plugin_name):
    sock = establish_socket()
    sock.send(
        json.dumps({"mode": "write", "group": "application", "target": "load_plugin", "data": plugin_name}).encode())
    sock.close()


def unload_plugin(plugin_name):
    sock = establish_socket()
    sock.send(
        json.dumps({"mode": "write", "group": "application", "target": "unload_plugin", "data": plugin_name}).encode())
    sock.close()


def print_error_message(msg=""):
    print("Your input could not be processed. " + msg)
    print("Please use the following pattern:")
    print("python pluginManager.py [load|unload] [plugin_name]...")
    exit(0)


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) < 2:
        print_error_message("Too few arguments")

    mode = args[0]
    plugins = args[1:]

    if mode == "load":
        for plugin in plugins:
            load_plugin(plugin)
    elif mode == "unload":
        for plugin in plugins:
            unload_plugin(plugin)
    else:
        print_error_message("unknown mode")
