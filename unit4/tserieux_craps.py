import random
Player_mone = 100

def get_bet():
    bet = int(input("How much would you like to bet? "))
    return bet
    
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("you rolled {},{} and {} in total".format(dice1,dice2,dice_sum))
    return dice_sum

def phase3 (dice_sum):
    phase3_dice = 0
    dice_sum = phase3_dice
    phase_dice = random.randint(1,6)
    phase_dice1 = random.randint(1,6)
    phase_sum = phase_dice + phase_dice1
    print("you rolled {},{} and {} in total".format(phase_dice,phase_dice1,phase_sum))
    
def bet_verificatoin(bet):
    player_money = 100
    if bet > player_money:
        bet = input("too much ")

    










get_bet()
roll2dice()
phase3(dice_sum)