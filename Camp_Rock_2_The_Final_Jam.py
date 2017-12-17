team_name = 'Bonus Jonas'
strategy_name = 'Camp Rock 2: The Final Jam'
strategy_description = '''Junie Cortez's warty fingers'''

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    prior_round = their_history[-1]
    if prior_round == 'c':
        return 'c'
    else:
        return 'b'