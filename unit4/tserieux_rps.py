import random





player_wins = 0
comp_wins = 0
ties = 0
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
def get_round():
    rounds = int(input("how many rounds would you like to play from 1 to 9 "))
    return rounds
def get_winner(p1_move,comp_move):
    if p1_move == comp_move:
        ties = ties +1
        return "tie"
    elif p1_move == "rock" and comp_move == "paper":
        player_wins == player_wins +1
        return "player"
    elif p1_move == "rock" and comp_move == "scissors":
        player_wins == player_wins + 1
        return "player"
    elif p1_move == "paper" and comp_move == "rock":
        comp_wins == comp_wins + 1
        return "computer"
    elif p1_move == "paper" and comp_move == "scissors":
        comp_wins == comp_wins +1
        return "computer"
    elif p1_move == "scissors" and comp_move == "rock":
        comp_wins == comp_wins + 1
        return "computer"
    elif p1_move == "scissors" and comp_move == "paper":
        player_wins == player_wins + 1
        return "player"
def print_score(player_wins,comp_wins,ties):
    print("The player's score is {}".format(player_wins))
    print("The computer's score is {}".format(comp_wins))
    print("There were {} ties".format(ties))

    
print(get_round())    
print(get_comp_move())
print(get_p1_move())
print(print_score(player_wins,comp_wins,ties))

