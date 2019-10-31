import json

def write_superheld_dict(highscore, superheld, players):
    with open('leaderboard.json', 'w') as file:
        highscore[superheld] = players
        json.dump(highscore, file)


