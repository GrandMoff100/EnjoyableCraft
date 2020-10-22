from flask import Flask, render_template, request, redirect, jsonify
from mcclient import Server, PlayerClient
from utils import CONFIG, SET_CONFIG, format_statistics, ADD_PLAYER, REMOVE_PLAYER, PLAYERS, get_form_json, CONFIG_VIEW
import requests as r
import json


web_site = Flask(__name__)


server = Server(CONFIG()['IP'])
client = PlayerClient()


@web_site.route('/')
def index():
    return render_template('index.html')

@web_site.route('/players')
def players():
    players = PLAYERS()
    objs = [[client.get_player(player), permissions] for player, permissions in players.items()]
    return render_template('players.html', objs=objs)

@web_site.route('/stats')
def stats():
    return render_template('stats.html', IP=CONFIG()['IP'], **format_statistics(server.get_status()))

@web_site.route('/github')
def github():
    return redirect(CONFIG()['GITHUB'])

@web_site.route('/apply')
def apply_redirect():
    return redirect(CONFIG()['APPLY_FORM'])

@web_site.route('/highlights')
def highlights():
    return 'No highlights yet, sorry :('


@web_site.route('/api/config', methods=['GET'])
def api_config():
    return CONFIG()

@web_site.route('/api/config/<key>', methods=['POST'])
def api_set_config(key):
    try:
        SET_CONFIG(request.headers.get('config_key'), request.headers.get('config_val'))
        return '200 Ok'
    except KeyError as err:
        return str(err)
    

@web_site.route('/api/players', methods=['GET'])
def api_players():
    return PLAYERS()

@web_site.route('/api/players/<player>', methods=['POST', 'DELETE'])
def api_players_player(player):
    if request.method == 'POST':
        ADD_PLAYER(player)
    elif request.method == 'DELETE':
        REMOVE_PLAYER(player)
    else:
        return 'Invalid Request Method'


@web_site.route('/api/applications')
def applications():
    questions, answers = get_form_json()
    return {
        'questions': questions,
        'answers': answers
    }


@web_site.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        url = 'https://' + request.host + '/api/applications'
        csv = r.get(url).json()
        return render_template('admin.html', config=CONFIG(), players=PLAYERS(), csv=json.dumps(csv, indent=4), config_file_view=CONFIG_VIEW())
    else:
        return 'Invalid Method'
        

@web_site.route('/heroku')
def heroku():
    return redirect(CONFIG()['HEROKU'])


if __name__ == '__main__':
    web_site.run(host='0.0.0.0', port=8080)
    