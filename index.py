import json
from pprint import pprint

from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/alexa_remote_control')

@ask.launch
def start_skill():
    welcome_message = 'Which channel do you want me to put on?'
    return question(welcome_message)

@ask.intent('ChangeChannelIntent')
def change_channel(channel_name):

    #Look up code for changing channel
    ##
    print channel_name
    # with open('channel_list.json') as data_file:
    #     channel_list = json.load(data_file)
    # channel_number = channel_list[channel_name]
    # print channel_number
    # Run function for changing channel on Pi
    ##
    # Tell user that Alexa is changing the channel
    text = 'Changing the channel to {}'.format(channel_name)
    return statement(text)

if __name__ == '__main__':
    app.run(debug=True)
