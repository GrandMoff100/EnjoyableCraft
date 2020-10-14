import requests as r
import datetime
import os
import urllib.parse


SERVER_HOST = 'https://eu.mc-api.net/v3'
SERVER_API = 'https://mcapi.xdefcon.com/server'


class Server:
    _status_cache = {}
    _player_cache = {}
    updated_at = None

    def __init__(self, ip, cache_timeout=60):
        self.cache_timeout = cache_timeout
        self.ip = ip
    
    def get(self, attr):
        return self.get_status().get(attr)
    
    @property
    def ping(self):
        return self.get('ping')
    
    @property
    def motd(self):
        try:
            return self.get('motd').get('text')
        except:
            return self.get('motd')

    @property
    def online(self):
        return self.get('serverStatus')

    @property
    def version(self):
        return self.get('version')

    @property
    def icon(self):
        return self.get('icon')

    @property
    def ipv4(self):
        return self.get('serverip')
    
    @property
    def protocol(self):
        return self.get('protocol')
    
    @property
    def players(self):
        return self.get('players')
    
    @property
    def maxplayers(self):
        return self.get('maxplayers')

    def get_status(self):
        now = datetime.datetime.now()
        if self.updated_at is None:
            self._status_cache = self.request_status()
            self.updated_at = now
        if (now - self.updated_at).total_seconds() >= self.cache_timeout:
            self._status_cache = self.request_status()
            self.updated_at = now
        return self._status_cache

    def request_status(self):
        url = os.path.join(SERVER_HOST, 'server', 'ping', self.ip)
        url = os.path.join(SERVER_API, urllib.parse.quote(self.ip), 'full', 'json')
        return r.get(url).json()


