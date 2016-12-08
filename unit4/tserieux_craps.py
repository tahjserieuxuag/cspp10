import random
Player_mone = 100

def get_bet():
    bet = int(input("How much would you like to bet "))
    return bet
    
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("you rolled {},{} and {} in total".format(dice1,dice2,dice_sum))
    return dice_sum
get_bet()
roll2dice()