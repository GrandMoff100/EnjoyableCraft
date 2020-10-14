from flask import Flask, render_template, request
from mcclient import Server
from utils import CONFIG, SET_CONFIG, format_statistics


web_site = Flask(__name__)


server = Server(CONFIG()['IP'])


@web_site.route('/')
def index():
	return render_template('index.html', motd=server.motd)

@web_site.route('/players')
def players():
    return render_template('players.html')

@web_site.route('/stats')
def stats():
    info = 'IP: {}\n'.format(CONFIG()['IP'])
    info += '\n'.join(['{}: {}'.format(k, v) for k, v in server.get_status().items()])
    return render_template('stats.html', IP=CONFIG()['IP'], **format_statistics(server.get_status()))

@web_site.route('/github')
def github():
    return 'No Github Repo at this time.'

@web_site.route('/apply')
def apply_redirect():
    return 'Not functional at the moment.\nContact Nate'


if __name__ == '__main__':
    web_site.run(host='0.0.0.0', port=8080)