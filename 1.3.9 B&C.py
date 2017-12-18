####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'B&C'
strategy_name = 'Collude 10 rounds unless betrayed. Betray 11th round forward.'
strategy_description = '''Betray if ever betrayed. If I haven't been betrayed yet, I'll betray starting with the 10th round.'''

import random
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.'''
    # If the other player has betrayed,
    if 'b' in their_history or len(their_history)>10: 
        return 'b'               # Betray.
    else:
        return 'c'