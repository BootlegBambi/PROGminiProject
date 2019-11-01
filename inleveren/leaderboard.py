import json
import datetime

vandaag = datetime.datetime.today().strftime("%d %b %Y")

with open('leaderboard.json', 'r+') as file:
    topscores = json.load(file)


def write_score(topscores, naam, punten):
    """Write score to file"""
    if naam.strip() == '':
        naam = 'Anonymous'
    else:
        naam = naam.capitalize()

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
    """Return a formatted string of the top 5 players"""
    temp, topscore_text, count = {}, "", 0
    for dict in topscores.keys():
        for item in topscores[dict].keys():
            if item == 'punten':
                temp[dict] = topscores[dict][item]

    for key in sorted(temp, key=temp.get, reverse=True):
        topscore_text += "- {0:<}: {1:>3}\n".format(key, temp[key])
        count += 1
        if count == 5:
            break
    return topscore_text


def lees_dag(topscores):
    """Return a formatted string of the top 5 players of the day"""
    temp, topscore_day_text, count = {}, "", 0
    for item in topscores:
        for dict in topscores[item]:
            if dict == 'datum':
                if topscores[item][dict] == vandaag:
                    temp[item] = topscores[item]['punten']

    for key in sorted(temp, key=temp.get, reverse=True):
        topscore_day_text += "- {0:<}: {1:>3}\n".format(key, temp[key])
        count += 1
        if count == 5:
            break
    return topscore_day_text

