import random
Player_mone = 100
#get bet
def get_bet(bank):
    bank = 100
    bet = int(input("How much would you like to bet? "))
    while True:
        if bet > bank:
            bet = int(input("You dont have enough money, bet again "))
        elif bet == 0:
            bet = int(input("You cant bet nothing, bet again "))
        elif bet < 0:
            bet = int(input("you cant bet that, bet again "))
        else:
            return bet
    
    
   

  #get phase 2 roll
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("you rolled {},{} and {} in total".format(dice1,dice2,dice_sum))
    return dice_sum
    
#return "winner" or "loser"
def phase3(point_roll):
    while True:
        roll = roll2dice()
        if roll == point_roll:
            return "win"
        elif roll == 7:
            return "lost"
                    
    
    
    
    
    
 #main game           
def craps():
    bank = 100
    while bank > 0:
        bet = get_bet(bank)
        dice = roll2dice()
        if dice == 2 or dice == 3 or dice == 12:
            print("You Loose")
            bank = bank - bet
        elif dice == 7 or dice == 11:
            print("You Won")
            bank = bank + bet
        else :
            phase = phase3(dice)
            if phase == "win":
                print("You Win")
                bank = bank + bet
            elif phase == "lost":
                print("You Lost")
                bank = bank - bet
        
        print("You have ${} in your bank".format(bank))
           
        
        
        
        

   
craps()
    
    
            

        


    









