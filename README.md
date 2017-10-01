http://www.raspberry-pi-geek.com/Archive/2015/10/Raspberry-Pi-IR-remote
https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-voice-design-best-practices
https://www.hackster.io/austin-stanton/creating-a-raspberry-pi-universal-remote-with-lirc-2fd581

## Arduino
grey -> pin 2
white -> pin 3

## Setup
* ssh into the Raspberry Pi via the following command `ssh pi@192.168.0.15`
* `vncserver`
* Open VNC Viewer
* Head to the where the `vncserver` command sent you
* Download a VNC on Raspberry Pi and Computer. Tuturial [here](https://www.raspberrypi.org/documentation/remote-access/vnc/)
* Other commands can be found [here](https://www.raspberrypi.org/guides/teachers/vnc-classroom-guide.md) to help start on Raspberry Pi
* Once on the Raspberry Pi, cd into the directory of the app and run `sudo python index.py`
* To shutdown the Raspberry, run the following command `sudo shutdown -h now`

## LIRC

Software library for using IR LEDs on Linux machines

## IR LED commands

```
irsend: 00000000000022dd KEY_OK
irsend: 000000000000da25 KEY_EXIT
irsend: 00000000000002fd KEY_UP
irsend: 000000000000827d KEY_DOWN
irsend: 000000000000c03f KEY_VOLUMEDOWN
irsend: 00000000000040bf KEY_VOLUMEUP
irsend: 000000000000d02f KEY_MENU
irsend: 00000000000010ef KEY_POWER
irsend: 000000000000906f KEY_MUTE
``

### How to create a new config file

```
# Stop library
sudo /etc/init.d/lirc stop
# Create new recording in config file ~/lircd.conf
irrecord -d /dev/lirc0 ~/lircd.conf
# Move the created config file to the folder where LIRC looks for the config files
sudo cp lgremote.conf /etc/lirc/lircd.conf
#
sudo cp ~/lircd.conf /etc/lirc/lircd.conf
```
