# Filter Function in Python

# The filter() function creates a collection of elements from an iterable (e.g., list, tuple) for which a function returns true.

# Syntax: filter(function, iterable)

friends = [("Rachel", 18),
           ("Joe", 21),
           ("Ross", 20),
           ("Timothy", 16),
           ("Jim", 19),
           ("Destiny", 17)]

# Define a lambda function 'age' that takes a tuple 'data' and returns True if the age is greater than or equal to 18.
age = lambda data: data[1] >= 18

# Use the filter() function to create a new list called 'drinking_buddies' that contains the friends for whom 'age' function returns True.
drinking_buddies = list(filter(age, friends))

# Print the items in 'drinking_buddies' without parentheses using string formatting.

# Print the header.
print("The following people are safe to go drinking:")

# Loop through the 'drinking_buddies' list and print each item without parentheses.
# We use string formatting to display the name and age without parentheses.
for name, age in drinking_buddies:
    print(f"{name}, {age}")
