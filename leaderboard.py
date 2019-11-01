import json
import datetime

vandaag = datetime.datetime.today().strftime("%d %b %Y")

with open('leaderboard.json', 'r+') as file:
    topscores = json.load(file)

def write_score(topscores, naam, punten):
    if naam in topscores.keys():
        speler = topscores[naam]
        if punten > speler['punten']:
            speler['punten'] = punten
            speler['datum'] = str(datetime.datetime.today().strftime("%d %b %Y"))
            topscores[naam] = speler
    else:
        speler = {}
        speler['punten'] = punten
        speler['datum'] = str(datetime.datetime.today().strftime("%d %b %Y"))
        topscores[naam] = speler

    with open('leaderboard.json', 'w') as file:
        json.dump(topscores, file, indent=4)


def lees_score(topscores):
    temp = {}
    for dict in topscores.keys():
        for item in topscores[dict].keys():
            if item == 'punten':
                temp[dict] = topscores[dict][item]
            if len(temp) == 5:
                break
        if len(temp) == 5:
            break

    topscore_text = ""
    for name, score in sorted(temp.items(), reverse=True):
        topscore_text += " - {0:10} : {1:2}\n".format(name, score)
    return topscore_text


def lees_dag(topscores):
    temp = {}
    for item in topscores:
        for dict in topscores[item]:
            if dict == 'datum':
                if topscores[item][dict] == vandaag:
                    temp[item] = topscores[item]
            if len(temp) == 5:
                break

    topscore_day_text = ""
    for row in sorted(temp.items(), reverse=True):
        topscore_day_text += " - {0:10} : {1:2}\n".format(row[0], row[1]['punten'])
    return topscore_day_text
