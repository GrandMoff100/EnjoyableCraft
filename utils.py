import json


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