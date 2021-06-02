import requests as r
from .config import CONFIG


def format_statistics(info):
    info['status_color'] = 'green' if info['serverStatus'] == 'online' else 'red'
    info['serverStatus'] = 'Online' if info['serverStatus'] == 'online' else 'Offline'
    try:
        info['motd'] = info['motd']['text']
    except KeyError:
        pass

    return info


def get_form_json():
    ID = CONFIG()['RESPONSES_ID']
    sheet_name = CONFIG()['RESPONSES_NAME']
    CSV_URL = f"https://docs.google.com/spreadsheets/d/{ID}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    response = r.get(CSV_URL)

    lines = response.content.decode('UTF-8').replace('","', '|').splitlines()
    lines = [line[:-2][1:].split('|') for line in lines]
    print(*lines, sep='\n')
    questions, *answers = lines

    return questions, answers
