import os
import time

time_between_press_initial = 1.5
time_between_press_source = 0.1
time_between_press_before_exit = 0.5

time_between_press_volume = 0.2

# LIRC conf file when finding out blink values for IR LED
lirc_file_conf = '~/lgremote2'

def change_power():
    os.system('irsend SEND_ONCE {} KEY_POWER'.format(lirc_file_conf))

def change_source(source_value):
    if source_value == 'cable box':
        os.system('irsend SEND_ONCE {} KEY_MENU'.format(lirc_file_conf))
        time.sleep(time_between_press_initial)
        os.system('irsend SEND_ONCE {} KEY_DOWN'.format(lirc_file_conf))
        time.sleep(time_between_press_source)
        os.system('irsend SEND_ONCE {} KEY_DOWN'.format(lirc_file_conf))
        time.sleep(time_between_press_source)
        os.system('irsend SEND_ONCE {} KEY_OK'.format(lirc_file_conf))
        time.sleep(time_between_press_before_exit)
        os.system('irsend SEND_ONCE {} KEY_EXIT'.format(lirc_file_conf))
    elif source_value == 'HDMI2':
        os.system('irsend SEND_ONCE {} KEY_MENU'.format(lirc_file_conf))
        time.sleep(time_between_press_initial)
        os.system('irsend SEND_ONCE {} KEY_DOWN'.format(lirc_file_conf))
        time.sleep(time_between_press_source)
        os.system('irsend SEND_ONCE {} KEY_DOWN'.format(lirc_file_conf))
        time.sleep(time_between_press_source)
        os.system('irsend SEND_ONCE {} KEY_DOWN'.format(lirc_file_conf))
        time.sleep(time_between_press_source)
        os.system('irsend SEND_ONCE {} KEY_OK'.format(lirc_file_conf))
        time.sleep(time_between_press_before_exit)
        os.system('irsend SEND_ONCE {} KEY_EXIT'.format(lirc_file_conf))
    elif source_value == 'Xbox':
        os.system('irsend SEND_ONCE {} KEY_MENU'.format(lirc_file_conf))
        time.sleep(time_between_press_initial)
        os.system('irsend SEND_ONCE {} KEY_DOWN'.format(lirc_file_conf))
        time.sleep(time_between_press_source)
        os.system('irsend SEND_ONCE {} KEY_DOWN'.format(lirc_file_conf))
        time.sleep(time_between_press_source)
        os.system('irsend SEND_ONCE {} KEY_DOWN'.format(lirc_file_conf))
        time.sleep(time_between_press_source)
        os.system('irsend SEND_ONCE {} KEY_DOWN'.format(lirc_file_conf))
        time.sleep(time_between_press_source)
        os.system('irsend SEND_ONCE {} KEY_OK'.format(lirc_file_conf))
        time.sleep(time_between_press_before_exit)
        os.system('irsend SEND_ONCE {} KEY_EXIT'.format(lirc_file_conf))

def change_mute():
    os.system('irsend SEND_ONCE {} KEY_MUTE'.format(lirc_file_conf))

def change_volume(volume_value, increase_or_decrease_volume):
    key = ''
    if increase_or_decrease_volume == 'higher' or increase_or_decrease_volume == 'increase' or increase_or_decrease_volume == 'raise':
        key = 'KEY_VOLUMEUP'
    elif increase_or_decrease_volume == 'decrease' or increase_or_decrease_volume == 'lower':
        key = 'KEY_VOLUMEDOWN'

    for x in range (0, int(volume_value)):
        time.sleep(time_between_press_volume)
        os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, key))
