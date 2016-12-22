import random
Player_mone = 100

def get_bet():
    bet = int(input("How much would you like to bet? "))
    player_money = 100
    if bet > player_money:
        bet = input("too much ")
    elif bet < 0:
        bet = input("no negative number ")
    elif bet == 0:
        bet = input("zero is not an option ")
    return bet
# get a bet
  
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("you rolled {},{} and {} in total".format(dice1,dice2,dice_sum))
    return dice_sum

def phase3(dice_sum):
    while True:
        pdice1 = random.randint(1,6)
        pdice2 = random.randint(1,6)
        phase_sum = pdice1 + pdice2
        if phase_sum = dice_sum:
        


    










get_bet()
roll2dice()
dice_sum = roll2dice()
