#!/usr/bin/python

import os
import urllib

# Stop screen session with mavproxy
print "Stopping mavproxy"
os.system("sudo screen -X -S mavproxy quit")

# Download most recent firmware
print "Downloading latest ArduSub firmware..."
firmwarefile = urllib.URLopener()
firmwarefile.retrieve("http://firmware.ardusub.com/Sub/latest/PX4-vectored/ArduSub-v2.px4", "/tmp/ArduSub-v2.px4")

# Download flashing script
print "Downloading px4 flashing tool..."
firmwarefile = urllib.URLopener()
firmwarefile.retrieve("https://raw.githubusercontent.com/PX4/Firmware/master/Tools/px_uploader.py", "/tmp/px_uploader.py")

# Flash Pixhawk
print "Flashing Pixhawk..."
os.system("python /tmp/px_uploader.py --port /dev/ttyACM0 /tmp/ArduSub-v2.px4")

# Wait a few seconds
time.sleep(5)

# Start screen session with mavproxy
print "Restarting mavproxy"
os.system("sudo screen -dm -S mavproxy /home/pi/companion/RPI2/Raspbian/start_mavproxy_telem_splitter.sh")