# modular-smart-home

This is a modular smart-home solution.


## Features
* control different _things_ through a web interface
* different _things_ are being loaded in dynamically
* Add your own python modules to add functionality
* Includes example modules
  - 'tuyaController' Controls tuya-switches
  - 'minecraftServerController' Starts and stops a Minecraft server
* Add html designs in javascript to complement your own modules
* Includes html modules
  - 'createSwitch' A checkbox with some css and a header

## Future features:
* smart-home-solution
  * auto page update
  * time dependent actions
* example modules
  * boot/shutdown control of Windows/Linux machines
  * more functionalities to control a minecraft server
  * RGB light controller

---

## How to use it
This solution is designed to run on two machines (web server and backend server) but it can also run on just one
machine.

#### _Backend_-setup  
The contents of _Backend_ are supposed to be on the backend server. This can be anywhere in the file system.  
First set up a virtual environment in you _"Backend"_ directory and load it:  
```python -m venv ./venv```  
```source ./venv/bin/activate```

To start the backend listener run:  
```python main.py```

I would recommend starting it in a _screen_ session though. Run:  
```screen -S msh_App python main.py```  

###### Requirements
* system
  * python 3.9.4 (could work with earlier versions too)
  * (Some example modules have additional requirements)
  * (Tested on Debian 4.19)  

###### Config
This is the configuration for the created server socket:  
_Backend/config-files/**this-server.json**_
```JSON
{
"address": "127.0.0.1",
"port": 12345
}
```
_"address"_  
If _Backend_ and _Frontend_ are on the same machine _127.0.0.1_ should be fine. Ideally this is the local ip address,
e.g.: _192.168.178.123_. Just make sure it is the same as in the config file of _Frontend_.

_"port"_  
_12345_ should be fine, you can change it though. Just make sure it is the same as in the config file of
_Frontend_.

#### _Frontend_-setup  
The contents of _Frontend_ are supposed to be on the frontend server. This needs to be in within your web server path.

###### Requirements
* system
  * web server setup
  * php
  * local file read access
  * (Tested on Raspbian 4.19)

###### Config
This is the configuration for the created server socket:
_Frontend/**Controller-Server.json**_
```JSON
{
"address": "127.0.0.1",
"port": 12345
}
```
_"address"_  
If _Backend_ and _Frontend_ are on the same machine _127.0.0.1_ should be fine. Else it needs to be the local address of
your backend server.

_"port"_  
_12345_ should be fine, you can change it though. Just make sure it is the same as in the config file of
_BackEnd_.

## How it works
soon TM

---

## **CAUTION!**
**In case your website is public, everyone could access it thus your devices and control them.
You might want to do something against that.** At this moment it is not planed to integrate something to address this
issue. 


## Custom modules
### Example modules
___
#### tuyaController
The tuyaController module connects to your tuya account to control your devices. Currently, there is only support
for switches and not for RGB lamps etc.

###### Requirements
* system
  * Internet connection
* python modules
  * tuyapy
  * requests

###### Config
Use the config file to load the credentials of you account:  
_Backend/config-files/**tuya.json**_
```JSON
{
  "email": "your.email@address.com",
  "password": "a_strong_password",
  "country_code": 49
}
```
_"email"_  
This is your email.  
Somehow this does not work if your tuya account is connected to a Google account etc.

_"password"_  
The password to your account. Keep it strong!

_"country_code"_  
the country code of the country your tuya account is registered in.  
e.g.: Germany: 49

___
#### minecraftServerController
The minecraftServerController module controls a Minecraft server via _screen_. Currently, you can only turn it on or off.
It is planed to add backup functionality, and the ability to control _Minecraft-Overviewer_.

###### Requirements
* linux packages
  * screen
  * Minecraft server setup

###### Config
Use the config file to set some server settings:  
_Backend/config-files/**minecraft.json**_
```JSON
{
  "location": "/path/to/my/server/",
  "jar_file": "server.jar",
  "server_name": "My Minecraft Server",
  "screen_name": "mc_server",
  "Xms": "1G",
  "Xmx": "4G"
}
```
_"location"_  
Absolute path to the directory the server is installed in.

_"jar_file"_  
Name of the jar file. _server.jar_ is the default vanilla server file name. This may change for bucket or spigot etc.
servers.

_"server_name"_  
Displayed name on your control website.

_"screen_name"_  
Session name for _screen_.

_"Xms"_  
Minimal RAM allocation of your Minecraft server.

_"Xmx"_  
Maximal RAM allocation of your Minecraft server.

---
### Add your own modules

###### Creating a module
Create a new .py file inside _Backend/Controller/_.  
Your Controller needs to inherit from the 'Controller' class
You can use this file template:
```PYTHON
from smartHomeController import Controller

class MyController(Controller):

    def on_load(self):
        pass

    def on_unload(self):
        pass

    def get_controller_group(self):
        pass

    def read_data(self):
        pass

    def write_data(self, target, data):
        pass
```

_"on_load()"_ [Optional]  
Gets called when your module gets loaded.

_"on_unload()"_  [Optional]  
Gets called when your module gets unloaded.

_"get_controller_group()"_ : str  
You are required to return a string with the group your controller belongs to.

_"read_data()"_ : list  
Here you return a list with all the things you are controlling. The items in the list should be dicts representing the
data of your controllables. Each controllable is required to have the following keys: "id", "type", "name", "state". 
Within "state" you have the data to represent everything that can change in the controllable.

_"write_data(target, data)"_  
:_"target"_ is the "id" of a controllable.  
:_"data"_ is e.g. a boolean if type is a switch, it is type dependent. You decide what to do with it!

###### Loading/Unloading a module
To load/unload your module run  
```python pluginManager.py [load|unload] [plugin_name]...```  
in the _"Backend"_ directory.
 
If you want your module to get loaded when you start main.py, you need to add the file of your module (without ".py")
into _config-files/**initial-plugins.json**_.
```JSON
[
  "tuyaController",
  "minecraftServerController",
  "yourModule_fileName"
]
```

###### ConfigLoader
In case you want to load and store config files in your modules you can use the included ConfigLoader module. See this
example:
```PYTHON
import configLoader

# load all the data
my_stored_data = configLoader.load("myConfigFile")

# load one attribute  
my_stored_attribute = configLoader.load_attribute("myConfigFile", "myStoredAttribute") # if the stored data is a dict
my_stored_list_item4 = configLoader.load_attribute("myConfigFile", 4) # if the stored data is a list

# store/overwrite all the data
configLoader.store("myConfigFile", my_stored_data)

# store/overwrite one attribute  
configLoader.store_attribute("myConfigFile", "myStoredAttribute", my_stored_attribute) # if the stored data is a dict
configLoader.store_attribute("myConfigFile", 4, my_stored_list_item4) # if the stored data is a list
```

---
### Add your own types (HTML designs)

###### Existing types
_Switch_  
Switch something on or off.

###### Creating a type
Sadly this process is quite unintuitive and done in javascript...  

Add the file inside _Frontend/controllableCreators/**createMyType.json**_
Here is a _switch_ example, which is the same as the provided switch:
```JAVASCRIPT
function createMyType(name, state, group, target) {
    // create a container to hold the all the other elements
    let switchContainer = document.createElement("div");  
    switchContainer.classList.add("mySwitchContainer");
    switchContainer.id = target;

    let nameElement = document.createElement("h3"); 
    nameElement.innerText = name;

    let labelElement = document.createElement("label");
    labelElement.classList.add("toggle");

    let inputElement = document.createElement("input");
    inputElement.classList.add("checkbox");
    inputElement.name = "checkbox";
    inputElement.type = "checkbox";
    // "writeTargetData" is super important, this sends data to the backend. It takes 3 parameters:
    // "group" (the group it belongs to), "target" (target controllable), "data" (Here just whether it is checked) 
    inputElement.setAttribute("onchange", "writeTargetData(\""+ group + "\", \"" + target + "\", this.checked)");
    // in case of type === "switch", state is just a bool
    inputElement.checked = state; 

    let sliderElement = document.createElement("span");
    sliderElement.classList.add("slider");
    sliderElement.classList.add("round");

    switchContainer.append(nameElement);
    labelElement.append(inputElement);
    labelElement.append(sliderElement);
    switchContainer.append(labelElement);
    // return the created container. Don't worry about appending it to the rest of the document.
    return switchContainer; 
}
```
The name of the function is actually important!  
It needs to start with "create", and the next letter needs to be capitalized. Everything after "create" is the name of
your type. It is mandatory that this is the same as the "type" attribute in your python module.

###### Register your type
Add a _script_ tag in index.html within _head_. You can also add a _link_ to the stylesheet there.
```HTML
<!-- Custom types -->
<script defer src="controllableCreators/createSwitch.js"></script>
<link rel="stylesheet" href="controllableCreators/createSwitch.css">

<script defer src="controllableCreators/createMyType.js"></script>
<link rel="stylesheet" href="controllableCreators/createMyType.css">
```

---
### Contact me for support
dominik.potulski@gmail.com