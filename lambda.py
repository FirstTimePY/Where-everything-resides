# Lambda Function

# A lambda function is a function defined in a single line using the 'lambda' keyword.
# It can accept any number of arguments, but it can only have one expression.
# Lambda functions are often used as shortcuts or for simple, throw-away operations.

# Syntax: lambda parameters: expression

# Define a lambda function called 'double' that takes 'x' as an argument and returns 'x * 2'
double = lambda x: x * 2

# Define a lambda function called 'multiply' that takes 'x' and 'y' as arguments and returns 'x * y'
multiply = lambda x, y: x * y

# Define a lambda function called 'add' that takes 'x', 'y', and 'z' as arguments and returns 'x + y + z'
add = lambda x, y, z: x + y + z

# Define a lambda function called 'full_name' that takes 'first_name' and 'last_name' as arguments
# and returns their concatenation with a space in between
full_name = lambda first_name, last_name: first_name + " " + last_name

# Define a lambda function called 'age_check' that takes 'age' as an argument
# and returns True if 'age' is greater than or equal to 18, otherwise returns False
age_check = lambda age: True if age >= 18 else False

# Call the lambda functions and print the results

print(double(5))  # Should print 10 (5 * 2)

print(multiply(5, 6))  # Should print 30 (5 * 6)

print(add(5, 6, 7))  # Should print 18 (5 + 6 + 7)

print(full_name("Joe", "Mama"))  # Should print "Joe Mama"

print(age_check(19))  # Should print True, as 19 is greater than or equal to 18
