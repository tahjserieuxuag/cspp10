from random import (random, randint)

def roll():
    return randint( 1, 6 ), randint( 1, 6 )




def main():
    print("Craps simulation") 
    while True:
        response = input("Enter an integer value > 0 ")
        if response == "": 
          print("Thank you for your business!")
          break

        try:
          num_trials = int(response)
          if num_trials < 1: 
              raise ValueError("Input must be >= 1 ")

          roundsPlayed = 0
          wins = 0
          while roundsPlayed < num_trials:
              roundsPlayed += 1
              if playRound(): 
                  wins += 1

            print( "Probability of winning is {0:>0.2%}".format( wins/num_trials  ) )

        except ValueError as err:
          print( err )
        except TypeError as err:
          print( err )

main()