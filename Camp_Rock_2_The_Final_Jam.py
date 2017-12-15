team_name = 'Bonus Jonas'
strategy_name = 'Camp Rock 2: The Final Jam'
strategy_description = '''Junie Cortez's warty fingers'''

def move(my_history, their_history, my_score, their_score):
    if 'c' in their_history[-1]:
        return 'c'
    else:
        return 'b'