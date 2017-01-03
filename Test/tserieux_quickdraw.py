import random

def get_player_move():
    bullets = 0
    P_move = input("Will you BLOCK,RELOAD or SHOOT ")
    if p_move.lower() == "block":
        return "block"
    elif p_move.lower() == "shoot":
        return "shoot"
    elif p_move.lower() == "shoot" and bullets == 0:
        return "no bullets"
    elif p_move.lower() == "reload":
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

def quick_draw(comp_move,p_move):
    bullets = 0
    player_health = 3
    computer_health = 3
    while player_health != 0 or computer_health != 0:
        if p_move == "shoot" and comp_move == "reload":
            computer_health = computer_health - 1
            return computer_health
        elif p_move == "shoot" and comp_move == "shoot":
            player_health == player_health - 1 and computer_health == computer_health - 1
            return(player_health,computer_health)
    
        
