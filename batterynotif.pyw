##########################
# batterynotif v1.0      
# Author: Diby M. (github.com/d1by)
# Date: April 24 2023
##########################
##########################
# Edit these fields:
# (refer to README file)

percent_goal = 80 # battery percentage at which notification will be sent

##########################

import os, time
import psutil
from plyer import notification

notify = True
while(True):
    battery = psutil.sensors_battery()

    if(battery == None):
        notification.notify(
            title = "error",
            message = "no battery found",
            app_icon = f"{os.path.realpath(os.path.dirname(__file__))}/icons/battery_icon_warn.ico",
            timeout = 10
        )

    else:
        if(battery.power_plugged):
            if(battery.percent >= percent_goal and notify):
                notification.notify(
                    title = "battery fully charged" if battery.percent == 100 else f"battery goal reached",
                    message = f"{battery.percent}% remaining.",
                    app_icon = f"{os.path.realpath(os.path.dirname(__file__))}/icons/battery_icon_white.ico",
                    timeout = 10
                )

                #prevents multiple notifications
                notify = False

            time.sleep(60)

        else:
            notify = True
            time.sleep(60)
