import json
import datetime

def Highscores_Opslaan(puntenaantal,speler):
    vandaag = datetime.datetime.today()
    datum = vandaag.strftime("%d %b %Y")

    with open('leaderboard.json','r') as json_file:
        data = json.load(json_file)

    for dicts in data:
        if len(data[dicts]) == 0:
            data[dicts].append([puntenaantal, speler, datum])
        else:
            for x in range(0, len(data[dicts])):
                if data[dicts][x][1] == speler:
                    if data[dicts][x][0] < puntenaantal:
                        data[dicts].remove(data[dicts][x])
                        data[dicts].append([puntenaantal, speler, datum])
                        data[dicts].sort(key=lambda x: x[0])
                        data[dicts].reverse()
                    else:
                        pass
                else:
                    data[dicts].append([puntenaantal, speler, datum])
                    data[dicts].sort(key=lambda x: x[0])
                    data[dicts].reverse()

    remove_list = []
    for x in range(0, len(data['Dag_Highscores'])):
        if data['Dag_Highscores'][x][2] != datum:
            remove_list.append(data['Dag_Highscores'][x])
    if remove_list:
        for value in remove_list:
            data['Dag_Highscores'].remove(value)


    with open('leaderboard.json','w') as json_file:
        json.dump(data,json_file,indent=4)

def All_Time_Highscores_afspelen():
    with open('leaderboard.json', 'r') as json_file:
        data = json.load(json_file)
        all_scores = data['All_Time_Highscores']
    print('Speler : Score')
    for persoon in all_scores:
        print(persoon[1] + ' : ' + str(persoon[0]))

def Dag_Highscores_afspelen():
    with open('leaderboard.json', 'r') as json_file:
        data = json.load(json_file)
        all_scores = data['Dag_Highscores']
    print('Speler : Score')
    for persoon in all_scores:
        print(persoon[1] + ' : ' + str(persoon[0]))


Highscores_Opslaan(4,'jee')
All_Time_Highscores_afspelen()
Dag_Highscores_afspelen()
