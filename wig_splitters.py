import json, keyboard
from flask import Flask, request


round_hs = 0 #stores round_hs
app = Flask(__name__)

name_file = open("name.txt")
player_name = name_file.readline()
name_file.close()


@app.route("/", methods=['POST'])
def listen():
    global player_name
    json_data = json.loads(request.data)
    if json_data.get('player').get('activity') != 'playing' and json_data.get('player').get('activity') != 'textinput':
        return "not in game"
    if json_data.get('player').get('name') != player_name:
        return "not a wigsplitter"
    else:
        print(json_data)
        main(json_data)
    return "playing"

def wig_split():
    keyboard.press_and_release('p')

def main(json_game_data):
    global round_hs
    json_player = json_game_data.get('player')

    if json_player.get('state').get('round_killhs') > 0:
        if json_player.get('state').get('round_killhs') > round_hs:
            print (round_hs)
            print (json_player.get('state').get('round_killhs'))
            wig_split()
            round_hs = json_player.get('state').get('round_killhs')
    else:
        round_hs = 0

app.run(host='127.0.0.1', port=5000)

