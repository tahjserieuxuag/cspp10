word = input("Enter a noun ")
number = int(input("Enter a numberber "))

if word[-2:] == "fe" and (number > 1 or number == 0) :
    print("{} {}".format(number,word[:-2]+"ves"))
elif word[-2:] == "fe" and (number == 1):
    print("{} {}".format(number,word))
elif word[-2:] == "ay" or word[-2:] == "ey" or word[-2:] == "oy" or word[-2:] == "uy" and (number > 1 or number == 0):#more specific equation before the generic one
    print("{} {}".format(number,word+"s"))
elif word[-1:] == "y" and (number > 1 or number == 0 ):
    print("{} {}".format(number,word[:-1]+"ies"))
elif word[-1:] == "y" and (number == 1):
    print("{} {}".format(number,word))
elif word[-2:] == "sh" or word[-2:] == "ch" and (number > 1 or number == 0) :
    print("{} {}".format(number,word+"es"))
elif word[-2:] == "us" and (number > 1 or number == 0) :
    print("{} {}".format(number,word[:-2]+"i"))
else :
     print("{} {}".format(number,word + "s"))