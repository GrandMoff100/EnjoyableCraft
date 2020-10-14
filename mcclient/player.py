import requests as r
import urllib.parse
import os

MOJANG_HOST = 'https://api.mojang.com'


FACE_AVATAR_URL = 'https://cravatar.eu/helmavatar/{}/{}.png'
CUBE_AVATAR_URL = 'https://cravatar.eu/helmhead/{}/{}.png'

BUST_AVATAR_URL = 'https://minotar.net/armor/bust/{}/{}.png'

class PlayerClient:
    player_cache = {}

    def get_player(self, user):
        user = user.lower()
        if user not in self.player_cache:
            user, uuid = self.request_player(user)
            self.player_cache[user] = uuid
            player = Player(user, uuid)
        else:
            player = Player(user, self.player_cache[user])
        
        return player
    
    def request_player(self, user):
        user = user.lower()
        user = urllib.parse.quote(user)
        url = os.path.join(MOJANG_HOST, 'users', 'profiles', 'minecraft', user)
        response = r.get(url)
        if response.content == b'':
            return None, None
        else:
            return tuple(response.json().values())
        


class Player:
    def __init__(self, user, uuid, avatar_res=190):
        self.name = user
        self.uuid = uuid

        self.bust_url = BUST_AVATAR_URL.format(user, avatar_res)
        self.face_url = FACE_AVATAR_URL.format(user, avatar_res) 
        self.cube_url = CUBE_AVATAR_URL.format(user, avatar_res)
    
    def __repr__(self):
        return f'<Player \'{self.name}\', \"{self.uuid}\">'
    
    def __str__(self):
        return self.name



playerclient = PlayerClient()

print(playerclient.get_player('Redstone_genius_'))

print(playerclient.player_cache)

print(playerclient.get_player('Redstone_Genius_'))