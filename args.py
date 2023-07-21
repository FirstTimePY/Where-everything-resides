# *args = parameter that will pack all arguments into a tuple. useful so that a function can accept a varying amount of arguments

# it doesnt have to be *args it can be anything, for example *hello or *joe
def add(*args):
    #The sum variable
    sum = 0

    #args now list omag
    args = list(args)

    #Changing the value at index 0 to 100
    args[0] = 100

    # basic py for loop
    for i in args:
        sum += i
    #after the loop is escaped:
    return sum

#printing
print(add(1,1,1))
