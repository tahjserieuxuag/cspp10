import random
def point_number():
    guess_number = random.randint(1,50)
    return(int(guess_number))
def get_winner(p_move,c_move,guess_number):
    if p_move == guess_number and c_move == guess_number:
        return"tie"
    elif p_move > guess_number and c_move > guess_number:
        return"tie"
    elif p_move == guess_number and c_move > guess_number:
            return"player"
    elif p_move == guess_number and c_move < guess_number:
            return"player"
    elif p_move > guess_number and c_move == guess_number:
            return"computer"
    elif p_move < guess_number and c_move == guess_number:
            return"computer"
    elif p_move < guess_number and c_move < p_move:
            return"player"
    elif c_move < guess_number and c_move > p_move:
            return"computer"
def player_move():
    p_move = int(input("What do you think the nuber is from 1 to 50 ? "))
    return(p_move)
def computer_move():
    c_move = random.randint(1,50)
    return(c_move)
def get_round():
    rounds = int(input("How many rounds would you like to play? "))
    return(rounds + 1)
def score_board(player_wins,com_wins,ties):
     print("__________________________________")
     print("The player's score is {}".format(player_wins))
     print("The computer's score is {}".format(com_wins))
     print("There where {} ties".format(ties))
def play_game():
    guess = point_number()
    Round = get_round()
    pl_move = player_move()
    comp_move = computer_move()
    
    for x in range(1,Round):
        winner = get_winner
        player_wins = 0
        com_wins = 0
        ties = 0
        print("Computer choice {}".format(comp_move))
        print("Player choice {}".format(pl_move))
        print("The number is {}".format(guess))
        if winner == "player":
            print("Player Wins!")
            print("__________________________________")
            player_wins = player_wins + 1
            print(player_wins)
        elif winner == "computer":
            print("Computer Wins!")
            print("__________________________________")
            com_wins = com_wins + 1
            print(com_wins)

        elif winner == "tie":
            print("Tie!")
            print("__________________________________")
            ties = ties + 1
            print(ties)
            
        score_board(player_wins,com_wins,ties)
        if player_wins > com_wins:
            print('Player Wins the Game!')
        elif com_wins > player_wins:
            print('Computer Wins the Game')
        else:
            print('The Game is a Draw')


play_game()
            


