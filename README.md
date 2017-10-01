http://www.raspberry-pi-geek.com/Archive/2015/10/Raspberry-Pi-IR-remote
https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-voice-design-best-practices
https://www.hackster.io/austin-stanton/creating-a-raspberry-pi-universal-remote-with-lirc-2fd581

## Setup
* ssh into the Raspberry Pi via the following command `ssh pi@192.168.0.16`
* `vncserver`
* Open VNC Viewer
* Head to the where the `vncserver` command sent you
* Download a VNC on Raspberry Pi and Computer. Tuturial [here](https://www.raspberrypi.org/documentation/remote-access/vnc/)
* Other commands can be found [here](https://www.raspberrypi.org/guides/teachers/vnc-classroom-guide.md) to help start on Raspberry Pi
* Once on the Raspberry Pi, cd into the directory of the app and run `sudo python index.py`
* To shutdown the Raspberry, run the following command `sudo shutdown -h now`

## Start ngrok
```
ngrok http 5000
```

## LIRC

[Link](http://lirc.sourceforge.net/)

Software library for using IR LEDs on Linux machines.

### Installation and Setup

Run from command line.

```
sudo apt-get install lirc
```

Add to your /etc/modules file by entering the command below

```
sudo /etc/modules
```

and add these to that file:

```
lirc_dev
lirc_rpi gpio_in_pin=23 gpio_out_pin=22
```

Change your /etc/lirc/hardware.conf file by entering the command below

```
sudo nano /etc/lirc/hardware.conf
```

```
# /etc/lirc/hardware.conf
#
# Arguments which will be used when launching lircd
LIRCD_ARGS="--uinput"
# Don't start lircmd even if there seems to be a good config file
# START_LIRCMD=false
# Don't start irexec, even if a good config file seems to exist.
# START_IREXEC=false
# Try to load appropriate kernel modules
LOAD_MODULES=true
# Run "lircd --driver=help" for a list of supported drivers.
DRIVER="default"
# usually /dev/lirc0 is the correct setting for systems using udev
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
# Default configuration files for your hardware if any
LIRCD_CONF=""
LIRCMD_CONF=""
```

Edit your /boot/config.txt by entering the command below

```
sudo nano /boot/config.txt
```

```
dtoverlay=lirc-rpi,gpio_in_pin=23,gpio_out_pin=22
```

Now restart lircd so it picks up these changes:

```
sudo /etc/init.d/lirc stop
sudo /etc/init.d/lirc start
```

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

## Programmed LIRC commands

```
KEY_OK
KEY_EXIT
KEY_UP
KEY_DOWN
KEY_VOLUMEDOWN
KEY_VOLUMEUP
KEY_MENU
KEY_POWER
KEY_MUTE
```
