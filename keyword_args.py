# keyword arguments = arguments preceded by an identifier when we pass them to a function 
#                     The order of arguments doesnt matter, unlike positional arguements 
#                     Python knows the names of the arguments that our function receives


#Self explanatory function:
def hello(first,middle,last):
    print("Hello " + first+" " + middle +" "+ last)


# As demonstrated here, the order doesnt matter since the arguments preceded by an identifier.
hello(last="Mama",middle="Jeff",first="Joe")