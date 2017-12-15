team_name = 'Peteman' # Only 10 chars displayed.
strategy_name = 'Cheesy Torto :)'
strategy_description = 'Artificial Intelligence'
    
def move(my_history, their_history, my_score, their_score):
    agent1 = test_score(my_score, their_score)
    agent2 = test_history(my_history, their_history)
    if agent1 and agent2:
        return 'c'    
    else:
        return 'b'  
          
def test_score(my, op):
    if my >= (op + 250):
        return True
    elif my < op:
        return False
    elif my == op == 0:
        return True
    else:
        return
        
def test_history(my, op):
    length = len(op)
    if length >= 2 and op[-1] == 'c' and op[-2] == 'c':
        return True
    elif my[-1] == 'c' and op[-1] == 'c':
        return True
    elif my[-1] == 'c' and op[-1] == 'b':
        return False
    elif my[-1] == 'b' and op[-1] == 'c':
        return True
    elif my[-1] == 'b' and op[-1] == 'b':
        return False
    else:
        return
        
def test_move(my_history, their_history, my_score, their_score, result):
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False
                