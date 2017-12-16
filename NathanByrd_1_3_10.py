team_name = 'Nate and Bella'
strategy_name = 'beat Peteman'
strategy_description = 'Return as collude if both statements return as false, otherwise return betrayel'
    
def move(my_history, their_history, my_score, their_score):
    history = h(my_history, their_history)
    score = s(my_score, their_score)
    if history and score == True:
        return 'c'
    else:
        return 'b'
        
def h(mine, opponent):
    if opponent[-1] == 'c':
        return True
    elif mine[-1] == 'c' and opponent[-1] == 'c':
        return True
    elif mine[-1] == 'c' and opponent[-1] == 'b':
        return False
    elif mine[-1] == 'b' and opponent[-1] == 'c':
        return True
    elif mine[-1] == 'b' and opponent[-1] == 'b':
        return False
    else:
        return
        
def s(mine, opponent):
    if mine >= opponent:
        return True
    elif mine < opponent:
        return False 
    else:
        return
        
