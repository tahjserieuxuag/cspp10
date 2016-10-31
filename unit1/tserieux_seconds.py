time = int(input("enter a time in seconds "))
# hours = minutes/60
# minutes = hours/ 60
# seconds = minutes % 60
seconds = int(time%60)
minutes = int(time/60)
hours = int(minutes/60)
minutes = minutes%60 #the minutes are equal to the left over minutes that did  not fit in an hour


print("{} seconds {} hours, {} minutes, and {} seconds".format(time,hours,minutes,seconds))

