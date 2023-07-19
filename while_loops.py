# while loop = a statement that will execute its block of code as long as its condition remains true

#Self explanatory code, run it yourself if you don't understand
# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hey there " + name)


# Another way to do it:
name = None

while not name:
    name = input("Enter your name: ")

print("Hey there " + name)