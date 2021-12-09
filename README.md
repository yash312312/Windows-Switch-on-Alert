<h1> Windows login Alert on Mobile Phone</h1>
A simple python program to send push notifications to your phone as soon as Windows is booted up

### Requirements
* Create an account on <a href="https://www.pushbullet.com/">PushBullet.com</a>.
* Install <a href="https://play.google.com/store/apps/details?id=com.pushbullet.android">PushBullet app</a> on your 
mobile phone and login using same id.

### Process
* Generate access token from <a href="https://www.pushbullet.com/">PushBullet</a> website by navigating to **Settings>
Access Tokens>Request Access Token**.
* Store the access token in a variable **access_token** in the *.env* file.
    - access_token=XXXXXXXX<br>
    .<br>
    ├── .env<br>
    └── main.py
* Install packages mentioned in requirements.txt if required.
* Open Run command window by pressing **Windows logo key + R** and type **shell:startup** and press **Enter**.
* Now copy **run.bat** from the directory and **Paste Shortcut** in the startup folder **(do not paste the copied file)**.
* Further, you can hide the black command prompt window on startup by right clicking on the shortcut then **Properties>Shortcut>
Run>Minimized**. 
