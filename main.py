from flask import Flask, render_template, request, redirect
from mcclient import Server, PlayerClient
from utils import CONFIG, SET_CONFIG, format_statistics, ADD_PLAYER, REMOVE_PLAYER, PLAYERS, Notifier


web_site = Flask(__name__)


server = Server(CONFIG()['IP'])
client = PlayerClient()
event_master = Notifier('logs/admin.log')


@web_site.route('/')
def index():
	return render_template(
        'index.html'
        )

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


@web_site.route('/api/config')
def api_config():
    if request.method == 'GET':
        return CONFIG()
    elif request.method == 'POST':
        try:
            SET_CONFIG(request.headers.get('config_key'), request.headers.get('config_val'))
            return '200 Ok'
        except KeyError as err:
            return str(err)
    else:
        return 'Invalid Request Method'

@web_site.route('/api/players')
def api_players():
    if request.method == 'GET':
        return PLAYERS()
    elif request.method == 'POST':
        ADD_PLAYER(request.headers.get('player'))
    elif request.method == 'DELETE':
        REMOVE_PLAYER(request.headers.get('player'))
    else:
        return 'Invalid Request Method'


@web_site.route('/admin')
def admin():
    return 'Admin page'


if __name__ == '__main__':
    web_site.run(host='0.0.0.0', port=8080)