# Reduce Function in Python

# The reduce() function is used to apply a specified function to an iterable and reduce it to a single cumulative value.
# It performs the function on the first two elements, then takes the result and the next element, and repeats the process until only one value remains.

# Syntax: reduce(function, iterable)

import functools

# Example 1:
# Uncomment the code below to find the word formed by concatenating the letters in the 'letters' list using the reduce() function.
# The lambda function takes two letters 'x' and 'y', and concatenates them using '+'. The result is printed as 'word'.

# letters = ["H", "E", "L", "L", "O"]
# word = functools.reduce(lambda x, y: x + y, letters)
# print(word)

# The output will be the word "HELLO".

# Example 2:
# In this example, we want to find the factorial of 5 using the reduce() function.

# Define a list 'factorial' containing the numbers from 5 to 1 in descending order.
factorial = [5, 4, 3, 2, 1]

# Use the reduce() function to find the factorial of 5.
# The lambda function takes two numbers 'x' and 'y', and multiplies them using '*'.
# The reduce() function will apply this lambda function cumulatively to the numbers in the 'factorial' list.
# The result will be stored in the variable 'result'.
result = functools.reduce(lambda x, y: x * y, factorial)

# Print the result, which is the factorial of 5.
print(result)

# The output will be 120, which is the factorial of 5 (5 * 4 * 3 * 2 * 1).
