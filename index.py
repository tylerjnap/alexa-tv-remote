import blink_ir_led

import json
from pprint import pprint

from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_skill():
    welcome_message = 'How should the t.v. update?'
    return question(welcome_message)

@ask.intent('ChangePowerIntent')
def change_power(power_value):
    print power_value

    blink_ir_led.change_power()

    text = 'Turning the t.v. {}'.format(power_value)
    return statement(text)

@ask.intent('ChangeSourceIntent')
def change_source(source_value):
    print source_value

    blink_ir_led.change_source(source_value)

    text = 'Changing source to {}'.format(source_value)
    return statement(text)

@ask.intent('MuteIntent')
def change_mute(mute_value):
    print mute_value

    blink_ir_led.change_mute()

    text = 'Will {} to t.v.'.format(mute_value)
    return statement(text)

@ask.intent('ChangeVolumeIntent')
def change_volume(volume_value, increase_or_decrease_volume):
    print volume_value
    print increase_or_decrease_volume

    blink_ir_led.change_volume(volume_value, increase_or_decrease_volume)

    text = 'Updating the volume by {}'.format(volume_value)
    return statement(text)

if __name__ == '__main__':
    app.run(debug=True)
