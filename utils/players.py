import json
import os
import requests as r
from .config import CONFIG, SET_CONFIG


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