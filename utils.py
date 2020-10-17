import json
import os


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

        info['serverStatus'] = 'Online' if info['serverStatus'] == 'online' else 'Offline'
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


class Notifier:
    def __init__(self, file):
        self.directory, self.name = os.path.split(file)

        self.log = open(self.file, 'a+')
        
    @property
    def file(self):
        return os.path.join(self.directory, self.name)
    
    def notify(self, message, method='local'):
        if method == 'local':
            print(message)
        elif method == 'discord':
            self.discord_notify(message)
        elif method == 'admin':
            pass

    
    def discord_notify(message):
        pass
    
    def admin_notify(message):
        pass
    
    def recent_admin_events(self):
        return self.log.read()