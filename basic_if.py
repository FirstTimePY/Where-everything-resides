# if statement = a block of code that will execute if its conditiion is true
# i already know how all this works but im just doing it for the fun of it

age = int(input("How old are you?: "))

if age >= 100:
    print("Shouldn't you be dead?")
elif age >=45:
    print("You're really old!")
elif age >= 18:
    print("You're an adult!")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You are a child!")
