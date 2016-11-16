import random






def get_p1_move():
    p1_move = input("Would you like to play Rock, Paper or Scissors")
    if p1_move == "Rock":
        return "Rock"
    elif p1_move == "Paper":
        return "Paper"
    elif p1_move == "Scissors":
        return "Scissors"
def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return "Rock"
    elif comp_move == 2:
        return "Paper"
    elif comp_move == 3:
        return "Scissors"

print(get_comp_move())
print(get_p1_move())