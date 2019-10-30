import json
import os
import functies

superheld ={}
players = {}
superheldenID = 'appel'

naam = input('Vul je naam in: ')

if os.path.exists('leaderboard.json'):
    with open('leaderboard.json', 'r+') as file:
        if os.stat('leaderboard.json').st_size == 0:
            players[naam] = functies.speel_het_spel(superheldenID)
            functies.write_superheld_dict({}, superheldenID, players)
        else:
            highscores = json.load(file)
            if superheldenID in highscores.keys():
                players = highscores[superheldenID]
                score = functies.speel_het_spel(superheldenID)
                if naam in players.keys():
                    if players[naam] > score:
                        print('Je hebt je high score niet verbeterd')
                    else:
                        print('Je hebt een nieuwe high score!')
                        players[naam] = score
                        functies.write_superheld_dict(highscores, superheldenID, players)
                else:
                    players[naam] = score
                    functies.write_superheld_dict(highscores, superheldenID, players)
            else:
                score = functies.speel_het_spel(superheldenID)
                players[naam] = score
                highscores[superheldenID] = players[naam]
                functies.write_superheld_dict(highscores, superheldenID, players)
