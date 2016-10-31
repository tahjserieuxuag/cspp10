endingrange = int(input("enter ending range "))
for x in range(1,endingrange):
    if x%3 == 0 and x%5 == 0:
        fb = x
        fb = "FizzBuzz"
        print(fb)
    elif x % 5 == 0:
        b = x
        b = "Buzz"
        print(b)
    elif x % 3 == 0:
        f  = x
        f = "Fizz"
        print(f)
    else:
        print(x)