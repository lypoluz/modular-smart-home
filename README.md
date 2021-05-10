# modular-smart-home

This is a modular smart-home solution


## Features
* Add your own python modules to add functionality
* Includes example modules
  - 'tuyaController' controls tuya-switches
  - 'minecraftServerController' starts and stops a MinecraftServer

## Future features:
* modular system for custom html designs

## How to use it


## **CAUTION!**
In case your website is public, everyone could access your website thus your devices and control them.
You might want to do something against that.  


## Custom modules
### Example modules
___
#### tuyaController
The tuyaController module connects to your tuya account to control your devices. Currently, there is only support
for switches and not for RGB lamps etc.

Use the config file to load the credentials of you account:  
_Backend/config-files/tuya.json_
```JSON
{
  "email": "your.email@address.com",
  "password": "a_strong_password",
  "country_code": 49
}
```
_"email"_  
This is your email.  
Somehow this does not work your tuya account is connected to a Google account etc.

_"password"_  
The password to your account. Keep it strong!

_"country_code"_
the country code of the country your tuya account is registered in.  
e.g.: Germany: 49

___
#### minecraftServerController
The minecraftServerController module controls a Minecraft server via _screen_. Currently you can only turn it on or off.
It is planed to add backup functionality.

Use the config file to set some server settings:  
_Backend/config-files/minecraft.json_
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
Minimal RAM usage of your Minecraft server.

_"Xmx"_  
Maximal RAM usage of your Minecraft server.

---
### Add your own modules