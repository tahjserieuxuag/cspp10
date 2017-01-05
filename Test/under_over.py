import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    # generate a random number from 1 to 6
    dice_1 =random.randint(1,6)
    # generate another random number from 1 to 6
    dice_2 = random.randint(1,2)
    # get the sum of the two rolls
    dice_sum = dice_1 +dice_2
   
    # print the sum
    print("You rolled a {}".format(dice_sum))
   
    # return the sum
    return dice_sum

# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet():
    ask_bet = int(input("how much would you like to bet? "))
    bank = 100
    while True:
        if ask_bet > bank:
            print("your bet is too high")
            ask_bet = ask_bet = int(input("how much would you like to bet? "))
        elif ask_bet < 0:
            print("no negative numbers")
            ask_bet = int(input("how much would you like to bet? "))
        elif ask_bet == 0:
            print("you cant bet nothing")
            ask_bet = int(input("how much would you like to bet? "))
            
    # ask the player how much they want to bet
   
    # if player's bet is more than they have
    #   available in bank, then get new bet
   
    # if player's bet is valid, then return
    #   the bet
 
# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    if dice_sum == 7:
        return "7"
    elif dice_sum < 7:
        return "under 7"
    elif dice_sum > 7:
        return "over 7"
        
    # if the sum is over 7, return "over7"
   
    # if the sum is under 7, return "under7"
   
    # if the sum is 7, return "equal7"
 
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    select_range = input("Do you think it is over 7, under 7, or equals 7")
    if select_range == "equals 7":
        return "equals 7"
    elif select_range == "over 7":
        return "over seven"
    elif select_range == "under seven":
        return "under seven"
    # present user with choices "over7", "under7",
    #   or "equal7"
   
    # return their choice

def main_game():
    
    
 
# function for the main game
roll2dice()
get_bet()