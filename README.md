# Amazon Alexa TV Remote

Actions are initiated through voice commands through Amazon Alexa Skill, which then gets relayed to the internet connected Raspberry Pi, which then sends the correct signal through the IR LED to the TV to turn it on, increase the volume, etc.

Basically, it makes your TV voice controlled through Alexa.

## How to use
Initiate skill
```
"Alexa, ask the TV to update."
or
"Alexa, tell the TV to update."
```
Turn TV on/off
```
"Turn the TV on."
```
Change source (cable box, Xbox, HDMI2)
```
"Change the source to the cable box."
```
Increase/decrease volume
```
"Increase the volume by five."
```
Mute/unmute the TV
```
"Mute the TV."
```

## Quick start for hardware
* ssh into the Raspberry Pi via the following command `ssh pi@192.168.0.16`
* `tmux` then `cd alexa-tv-remote` then `python index.py`; `CTRL+b then d` to exit tmux session
* `tmux` then `cd alexa-tv-remote` then `./ngrok http 5000` (take this URL and add to Amazon Alexa Skill dashboard); `CTRL+b then d` to exit tmux session
* To shutdown the Raspberry Pi, if need be, run the following command `sudo shutdown -h now`

## TMUX Overview
Allows you to SSH into a Raspberry Pi, create terminal sessions, initiate processes, and exit without terminating them.

Create new session
```
tmux
```

Detach from session
```
CTRL+b then d
```

List sessions
```
tmux ls
```

Attach to specific session
```
tmux attach -t <SESSION_NUMBER>
```

## LIRC Overview

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

### Programmed LIRC commands

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

## Important links
- [Blog turning RPi into remote](http://www.raspberry-pi-geek.com/Archive/2015/10/Raspberry-Pi-IR-remote)
- [Another blog turning RPi into remote](https://www.hackster.io/austin-stanton/creating-a-raspberry-pi-universal-remote-with-lirc-2fd581)
