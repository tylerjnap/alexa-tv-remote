import os
import time

import json
from pprint import pprint

from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/alexa-tv-remote')

time_between_press = 0.2

@ask.launch
def start_skill():
    welcome_message = 'How should the t.v. update?'
    return question(welcome_message)

@ask.intent('ChangePowerIntent')
def change_power(power_value):
    print power_value

    # Blink LED
    # os.system('irsend SEND_ONCE ~/lgremote2 KEY_POWER')

    text = 'Turning the t.v. {}'.format(power_value)
    return statement(text)

@ask.intent('ChangeSourceIntent')
def change_source(source_value):
    print source_value

    # Blink LED
    # if source_value == 'cable box':
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_MENU)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_OK)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_EXIT)
    # elif source_value == 'h.d.m.i. two':
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_MENU)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_OK)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_EXIT)
    # elif source_value == 'x. box':
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_MENU)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_OK)
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 KEY_EXIT)

    text = 'Changing source to {}'.format(source_value)
    return statement(text)

@ask.intent('MuteIntent')
def change_mute(mute_value):
    print mute_value

    # Blink LED
    # os.system('irsend SEND_ONCE ~/lgremote2 KEY_MUTE)

    text = 'Will {} to t.v.'.format(mute_value)
    return statement(text)

@ask.intent('ChangeVolumeIntent')
def change_volume(volume_value, increase_or_decrease_volume):
    print volume_value
    print increase_or_decrease_volume

    if increase_or_decrease_volume == 'higher' or increase_or_decrease_volume == 'increase' or increase_or_decrease_volume == 'raise':
        key = 'KEY_VOLUMEUP'
    elif increase_or_decrease_volume == 'decrease' or increase_or_decrease_volume == 'lower':
        key = 'KEY_VOLUMEDOWN'

    # Blink LED
    # for x in range (0, volume_value):
    #     time.sleep(time_between_press)
    #     os.system('irsend SEND_ONCE ~/lgremote2 {}'.format(key))

    text = 'Updating the volume by {}'.format(volume_value)
    return statement(text)

if __name__ == '__main__':
    app.run(debug=True)
