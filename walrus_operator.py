# Walrus operator :=

# The walrus operator, new to Python 3.8, is an assignment expression that allows you to assign values to variables
# as part of a larger expression.

# Example 1:
# Normally, we would do the following to assign a value to a variable and then print it:
# happy = True
# print(happy)

# With the walrus operator, we can combine these two operations in one line:
# print(happy := True)

# Example 2:
# Here's a practical example of why the walrus operator is useful:


# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

#Now lets write the above program but using the walrus operator:


# Create an empty list called 'foods'
foods = list()

# Run a loop until the user enters "quit" as the input
# Inside the loop, ask the user for their favorite food, and append it to the 'foods' list
# The loop breaks when the user enters "quit"
# Without the walrus operator, we would have to use an extra line to assign the input value to the 'food' variable.
# With the walrus operator, we can do it in a single line, making the code more concise.
while food := input("What food do you like?: ") != "quit":
    foods.append(food)