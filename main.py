import json
import os

def write_superheld_dict(highscore, superheld, players):
    with open('leaderboard.json', 'w') as file:
        highscore[superheld] = players
        json.dump(highscore, file)

def jsonFile(score, naam, superheldenID):
    players = {}
    if os.path.exists('leaderboard.json'):
        with open('leaderboard.json', 'r+') as file:
            if os.stat('leaderboard.json').st_size == 0:
                players[naam] = naam
                write_superheld_dict({}, superheldenID, players)
            else:
                highscores = json.load(file)
                if superheldenID in highscores.keys():
                    players = highscores[superheldenID]
                    if naam in players.keys():
                        if players[naam] > score:
                            print('Try again to improve your Highscore')
                        else:
                            print('New Highscore!')
                            players[naam] = score
                            write_superheld_dict(highscores, superheldenID, players)
                    else:
                        players[naam] = score
                        write_superheld_dict(highscores, superheldenID, players)
                else:
                    players[naam] = score
                    highscores[superheldenID] = players[naam]
                    write_superheld_dict(highscores, superheldenID, players)
jsonFile()