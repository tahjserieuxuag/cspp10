import random





def get_round():
    rounds = int(input("how many rounds would you like to play from 1 to 9: "))
    return (rounds + 1)
def get_p1_move():
    p1_move = input("Would you like to play Rock, Paper or Scissors ")
    if p1_move.lower() == "rock":
        return "Rock"
    elif p1_move.lower() == "paper":
        return "Paper"
    elif p1_move.lower() == "scissors":
        return "Scissors"
def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return "Rock"
    elif comp_move == 2:
        return "Paper"
    elif comp_move == 3:
        return "Scissors"
def get_winner(p1_move,comp_move):
    if p1_move == comp_move:
        return "tie"
    elif p1_move == "Rock" and comp_move == "Paper":
        return "Computer"
    elif p1_move == "Rock" and comp_move == "Scissors":
        return "player"
    elif p1_move == "Paper" and comp_move == "Rock":
        return "computer"
    elif p1_move == "Paper" and comp_move == "Scissors":
        return "computer"
    elif p1_move == "Scissors" and comp_move == "Rock":
        return "computer"
    elif p1_move == "Scissors" and comp_move == "Paper":
        return "player"
def print_score(player_wins,comp_wins,ties):
    print("The player's score is: {}".format(player_wins))
    print("The computer's score is: {}".format(comp_wins))
    print("There are {} tie".format(ties))
def rps():
    player_wins = 0
    comp_wins = 0
    ties = 0
    rounds = get_round()
    for x in range(rounds):
        p1move = get_p1_move()
        compmove = get_comp_move()
        winner = get_winner(p1move,compmove)
        print("Player chose: {}".format(p1move))
        print("Computer chose: {}".format(compmove))
        if winner == "player":
            print("Player Won!")
            player_wins = player_wins + 1
        elif winner == "computer":
            print("Computer Won!")
            comp_wins = comp_wins + 1
        else:
            print("Tie!")
            ties = ties + 1
        print_score(player_wins,comp_wins,ties)

rps()
    