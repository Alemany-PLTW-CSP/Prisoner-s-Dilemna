team_name = 'Brendon'
strategy_name = 'Betray until colluded'
strategy_description = '''\
Betray first round. Betray, unless colluded; then always collude.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if 'c' in their_history:
        return 'c'
    else:
        return 'b'