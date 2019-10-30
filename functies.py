import json

def speel_het_spel(superheldenID):
    score = 25
    while True:
        antwoord = input('Answer: ')
        if antwoord == superheldenID:
            print('Correct answer!')
            print('your score is {}'.format(score))
            return score
        else:
            print('wrong answer, try again')
            score -= 1

def write_superheld_dict(highscore, superheld, players):
    with open('leaderboard.json', 'w') as file:
        highscore[superheld] = players
        json.dump(highscore, file)


