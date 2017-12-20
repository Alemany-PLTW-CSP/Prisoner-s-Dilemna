
team_name = 'anthony'
strategy_name = 'betryal'
strategy_description = 'if they have a betryal in the last five move I betray, if there is no betryal i have a one in ten chance of betrying if i dont betray i check to see who score is high if there score is higher than I betray or else i Collode '
    import random
def move(my_history, their_history, my_score, their_score):
   
     if 'b' in their_history[-5:]:
        return 'b'       
    else:
        if random.random()< 0.001
        return 'b'
        else:
            if their_score > my_score
            return 'b'
            else:
                return 'c'