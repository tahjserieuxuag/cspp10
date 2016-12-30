import random
Player_mone = 100

def get_bet():
    bet = int(input("How much would you like to bet? "))
    player_money = 100
    while bet>player_money or bet < 0 or bet == 0:
        if bet > player_money:
            bet = input("too much bet again ")
        elif bet < 0:
            bet = input("no negative number ")
        elif bet == 0:
            bet = input("zero is not an option, bet again ")
        return bet
# get a bet
  
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("you rolled {},{} and {} in total".format(dice1,dice2,dice_sum))
    if dice_sum == 7 or dice_sum == 1:
        return "Winner"
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return "Loose"
    return dice_sum
    

def phase3(dice_sum):
    while True:
        pdice1 = random.randint(1,6)
        pdice2 = random.randint(1,6)
        phase_sum = pdice1 + pdice2
        if phase_sum == dice_sum:
            print("player wins")
            return "win"
        elif phase_sum == 7:
            print("you lose")
            return "lose"
def craps():
    
            

        


    










get_bet()
