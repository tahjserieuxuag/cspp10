import random 

num = random.randint(1,100)
guess = int(input("What do you think the number is "))
while guess != num:
    if num > guess:
        attempts = guess + 1
        print (int(input(("To low try again "))))
        
    elif num < guess:
        attempts = guess +1
        print (int(input(("to high try again "))))
    else :
        break
print("you did it the number is {} it took you {} attempts".format(num,attempts))
            
