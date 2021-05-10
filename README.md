# modular-smart-home

This is a modular smart-home solution


## Features
* Add your own python modules to add functionality
* Includes example modules
  - 'tuyaController' controls tuya-switches
  - 'minecraftServerController' starts and stops a MinecraftServer

## Future features:
* modular system for custom html designs


## **CAUTION!**
In case your website is public, everyone could access your website thus your devices and control them.
You might want to do something against that.  


***
# Custom modules
***
## Example modules
### tuyaController
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
_**"email"**_  
This is your email.  
Somehow this does not work your tuya account is connected to a Google account etc.

_**"password"**_  


#### minecraftServerController


### Add your own modules