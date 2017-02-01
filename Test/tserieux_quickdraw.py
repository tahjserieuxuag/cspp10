import random

def get_player_move():
    bullets = 0
    P_move = input("will you block,reload or shoot ")
    if p_move == "block":
        return "block"
    elif p_move == "shoot":
        return "shoot"
    elif p_move == "shoot" and bullets == 0:
        return "no bullets"
    elif p_move == "reload":
        return "reload"
    else:
        p_move = input("That is not a move, input again")

def get_comp_move():
    cbullet = 0
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return "shoot"
    elif comp_move == 1 and cbullet == 0:
        return "no bullets"
    elif comp_move == 2:
        return "block"
    elif comp_move == 3:
        return "reload"

def game():
    player_health = 3
    com_health = 3
    com_move = get
 
    
    
    
        
