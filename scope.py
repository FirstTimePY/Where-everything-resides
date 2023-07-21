# scope/variable scope = the region that a var is recognized
#         a var is only available from inside the region it is created
#         a global and locally scoped versions of a var can be created


name = "Joe" # global scope (available inside & outside functions)


# Defining the function "display" which holds a local scope inside
def display():
    name = "Mama"       # local scope (available only inside this function)
    print(name)


# Trying to print the name variable from outside (error):
#print(name)

# Printing the global scope name
print(name)

#Calling the "display" function
display()

