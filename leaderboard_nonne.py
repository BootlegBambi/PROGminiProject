import json
import os

def write_superheld_dict(highscore, superheld, players):
    with open('leaderboard.json', 'w') as file:
        highscore[superheld] = players
        json.dump(highscore, file)

def jsonFile(score, naam, naam1):
    players = {}
    if os.path.exists('leaderboard.json'):
        with open('leaderboard.json', 'r+') as file:
            if os.stat('leaderboard.json').st_size == 0:
                players[naam] = naam
                write_superheld_dict({}, naam1, players)
            else:
                highscores = json.load(file)
                if naam1 in highscores.keys():
                    players = highscores[naam1]
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


jsonFile(25,'Youri','Youri')