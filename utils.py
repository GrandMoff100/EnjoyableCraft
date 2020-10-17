import json
from mcclient import PlayerClient


def CONFIG():
    with open('config.json', 'r') as f:
        return json.load(f)


def SET_CONFIG(key, value):
    config = CONFIG()
    config[key] = value
    with open('config.json', 'w') as f:
        json.dump(config, f)


def format_statistics(info):
    try:
        info['motd'] = str(repr(info['motd']['text']))
        print(info['serverStatus'])
        info['status_color'] = 'green' if info['serverStatus'] == 'online' else 'red'
        info['serverStatus'] = 'True' if info['serverStatus'] == 'online' else 'False'
    except Exception:
        pass
    return info

def PLAYERS():
    with open('players.json', 'r') as f:
        return json.load(f)

def WRITE_PLAYERS(players):
    with open('players.json', 'w') as f:
        json.dump(players, indent=4)
    

def ADD_PLAYER(playername, permissions='Member'):
    players = PLAYERS()
    if playername not in players:
        players[playername] = permissions
    WRITE_PLAYERS(players)
    

def REMOVE_PLAYER(playername):
    players = PLAYERS()
    if playername in players:
        del playername
    WRITE_PLAYERS(players)
