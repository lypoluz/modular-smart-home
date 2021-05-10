import json
import sys

file_location = "config-files/"
file_suffix = ".json"

def load(file_name):
    with open(file_location + file_name + file_suffix, "r") as file:
        data = json.load(file)
    return data

def load_attribute(file_name, attribute):
    return load(file_name)[attribute]


def store(file_name, data):
    with open(file_location + file_name + file_suffix, "w") as file:
        json.dump(data, file, indent=2)

def store_attribute(file_name, attribute, value):
    data = load(file_name)
    data[attribute] = value
    store(file_name, data)



if __name__ == '__main__':
    store(sys.argv[1], sys.argv[2])