import random






def get_p1_move():
    p1_move = input("Would you like to play Rock, Paper or Scissors ")
    if p1_move == "Rock":
        return "Rock"
    elif p1_move == "Paper":
        return "Paper"
    elif p1_move == "Scissors":
        return "Scissors"
def get_comp_move():
    comp_move.lower = random.randint(1,3)
    if comp_move.lower == 1:
        return "Rock"
    elif comp_move.lower == 2:
        return "Paper"
    elif comp_move.lower == 3:
        return "Scissors"
def get_round():
    rounds = int(input("how many rounds would you like to play from 1 to 9 "))
    return rounds
print(get_comp_move())
print(get_p1_move())
print(get_round())