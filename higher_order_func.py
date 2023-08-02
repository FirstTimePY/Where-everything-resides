# Higher Order Function

# Higher Order Function is a function that either:
# 1. Accepts a function as an argument (callback function)
# or
# 2. Returns a function

# In Python, functions are also treated as objects, so we can pass them as arguments or return them from functions.

# Example 1:
# Define two functions: loud and quiet
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# Define a higher order function called hello that takes another function as an argument
def hello(func):
    # Call the function passed as an argument with the text "Hello" and store the result in 'text'
    text = func("Hello")
    # Print the modified 'text'
    print(text)

# Call the hello function and pass the 'loud' function as an argument
# The hello function will call the 'loud' function with the text "Hello" and print the result in uppercase
hello(loud)

# Call the hello function and pass the 'quiet' function as an argument
# The hello function will call the 'quiet' function with the text "Hello" and print the result in lowercase
hello(quiet)


# Example 2:
# Define a higher order function called divisor that takes a number 'x' as an argument
def divisor(x):
    # Define a nested function called dividend that takes another number 'y' as an argument
    def dividend(y):
        # Return the result of 'y' divided by 'x'
        return y / x
    # Return the 'dividend' function itself (without calling it)
    return dividend

# Call the divisor function with the argument '2', which returns the 'dividend' function with 'x' set to 2
# Store the 'dividend' function in the variable 'divide'
divide = divisor(2)

# Call the 'divide' function with the argument '8'
# This will execute the 'dividend' function, which divides 8 by 2 and returns 4
print(divide(8))
