import random 

num = random.randint(1,100)

guess = int(input("What do you think the number is "))
attempts = 0
while guess != num:
    if num > guess:
        attempts = attempts + 1
        guess = (int(input("too low try again ")))
    elif num < guess:
        attempts = attempts +1
        guess =(int(input("to high try again ")))
    else:
        break
print("you did it the number is {} it took you {} attempts".format(num,attempts))
            
