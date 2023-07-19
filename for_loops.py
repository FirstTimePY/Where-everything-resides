# for loop = a statement that will execute its block of code a limited amount of times


# while loops = unlimited times
# for loops = limited times


import time

# Counts from 10 down to 1
# for i in range(10):
#     print(i+1)

#Counts from 50 all the way to 100
# for i in range(50,100+1):
#     print(i)

#Counts from 50 all the way to 100 but it goes like 50, 52, 54 all the way to 100
# for i in range(50,100+1,2):
#     print(i)

#Prints every letter in the name
# for i in "Joe Mama":
#     print(i)

#New year count down
for secs in range(10,0,-1):
    print(secs)
    #Makes the counter sleep for 1 second before continuing each number
    time.sleep(1)
# Prints "Happy New Year! 🎉" after the count down is over
print("Happy New Year! 🎉")
# Pause terminal for 5 seconds after "Happy New Year! 🎉"
time.sleep(5)