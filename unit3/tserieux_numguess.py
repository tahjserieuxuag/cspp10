import random 

num = random.randint(1,100)
print (num)
guess = int(input("What do you think the number is "))
attempts = 0
while guess != num:
   if guess >= num :
        attempts = guess +1
        print (int(input(("to high try again "))))
   elif guess <= num:
        attempts = guess + 1
        print (int(input(("To low try again "))))
   else:
        break
print("you did it the number is {} it took you {} attempts".format(num,attempts))
            
