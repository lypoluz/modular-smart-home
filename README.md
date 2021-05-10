# modular-smart-home

This is a modular smart-home solution.


## Features
* control different _things_ through a web interface
* different _things_ are being loaded in dynamically
* Add your own python modules to add functionality
* Includes example modules
  - 'tuyaController' controls tuya-switches
  - 'minecraftServerController' starts and stops a MinecraftServer

## Future features:
* smart-home-solution
  * modular system for custom html designs
  * html buttons
  * time dependent actions
* example modules
  * boot / shutdown control of Windows / Linux machines
  * more functionalities to control a minecraft server

---

## How to use it
This solution is designed to run on two machines (web server and backend server) but it can also run on just one
machine.

#### _Backend_-setup  
The contents of _Backend_ are supposed to be on the backend server. This can be anywhere in the file system.

###### Requirements
* system
  * python 3.9.4 (could work with earlier versions too)
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
_Frontend/**this-server.json**_
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
_BackEnd-_.

## How it works
soon TM

---

## **CAUTION!**
**In case your website is public, everyone could access it thus your devices and control them.
You might want to do something against that.**


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

####### Config
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