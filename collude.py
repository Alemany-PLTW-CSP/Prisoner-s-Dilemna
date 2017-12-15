team_name = 'Eric'
strategy_name = 'collude'
stratey_description = 'collude unless betrayed in the last 5 turns'

def move(my_hist, their_hist, my_score, their_score):
    if 'b' in their_hist[-5:]:
        return 'b'
    else:
        return 'c'