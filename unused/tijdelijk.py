import json
import datetime

def Highscores_Opslaan(puntenaantal,speler):
    vandaag = datetime.datetime.today()
    datum = vandaag.strftime("%d %b %Y")

    with open('leaderboard.json','r') as json_file:
        data = json.load(json_file)

    data['All_Time_Highscores'].append([(str(puntenaantal)),speler,datum])
    data['Dag_Highscores'].append([(str(puntenaantal)), speler, datum])

    for scores in data['Dag_Highscores']:
        if scores[2] != datum:
            data['Dag_Highscores'].remove(scores)

    with open('leaderboard.json','w') as json_file:
        json.dump(data,json_file,indent=4)

def All_Time_Highscores_afspelen():
    with open('leaderboard.json','r') as json_file:
        data = json.load(json_file)
        alle_highscores=data['All_Time_Highscores']
        print('Speler : Score')

        alle_highscores.sort()
        alle_highscores.reverse()
        for persoon in alle_highscores:
            print(persoon[1]+' : '+str(persoon[0]))

def Dag_Highscores_afspelen():
    with open('leaderboard.json','r') as json_file:
        data = json.load(json_file)
        alle_highscores=data['Dag_Highscores']
        print('Speler : Score')

        alle_highscores.sort()
        alle_highscores.reverse()
        for persoon in alle_highscores:
            print(persoon[1]+' : '+str(persoon[0]))


Highscores_Opslaan('16','hoi')
All_Time_Highscores_afspelen()
Dag_Highscores_afspelen()
