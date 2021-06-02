import json


def CONFIG():
    with open('config.json', 'r') as f:
        return json.load(f)


def SET_CONFIG(key, value):
    config = CONFIG()
    config[key] = value
    with open('config.json', 'w') as f:
        json.dump(config, f)


def CONFIG_VIEW():
    return json.dumps(CONFIG(), indent=4)
