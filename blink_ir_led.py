import os
import time

time_between_press = 0.2

def change_power():
    os.system('irsend SEND_ONCE ~/lgremote2 KEY_POWER')

def change_source(source_value):
    if source_value == 'cable box':
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_MENU')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_OK')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_EXIT')
    elif source_value == 'h.d.m.i. two':
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_MENU')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_OK')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_EXIT')
    elif source_value == 'x. box':
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_MENU')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_DOWN')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_OK')
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 KEY_EXIT')

def change_mute():
    os.system('irsend SEND_ONCE ~/lgremote2 KEY_MUTE')

def change_volume(volume_value, increase_or_decrease_volume):
    if increase_or_decrease_volume == 'higher' or increase_or_decrease_volume == 'increase' or increase_or_decrease_volume == 'raise':
        key = 'KEY_VOLUMEUP'
    elif increase_or_decrease_volume == 'decrease' or increase_or_decrease_volume == 'lower':
        key = 'KEY_VOLUMEDOWN'

    for x in range (0, volume_value):
        time.sleep(time_between_press)
        os.system('irsend SEND_ONCE ~/lgremote2 {}'.format(key))
