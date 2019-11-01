import json
import datetime

vandaag = datetime.datetime.today().strftime("%d %b %Y")

with open('leader.json', 'r+') as file:
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

    with open('leader.json', 'w') as file:
        json.dump(topscores, file, indent=4)




write_score(topscores=topscores, punten=500, naam='nonne')

def lees_score(topscores):
    temp = {}
    for dict in topscores.keys():
        for item in topscores[dict].keys():
            if item == 'punten':
                temp[topscores[dict][item]] = dict
    print(temp)


def lees_dag(topscores):
    dict_vandaag = {}
    for item in topscores:
        for dict in topscores[item]:
            if dict == 'datum':
                if topscores[item][dict] == vandaag:
                    dict_vandaag[item] = topscores[item]
    print(dict_vandaag)

with open('leader.json', 'r+') as file:
    topscores = json.load(file)

lees_dag(topscores)

