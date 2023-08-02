# Map Function in Python

# The map() function applies a specified function to each item in an iterable (e.g., list, tuple) and returns an iterator.

# Syntax: map(function, iterable)

# In this example, we have a list of tuples called 'store'.
store = [("shirt", 20.0),
         ("pants", 25.0),
         ("jacket", 35.0),
         ("socks", 5.0)]

# Define a lambda function 'to_euros' that takes a tuple 'data' and returns a new tuple.
# The new tuple contains the same item as the original tuple but with the price converted to euros (at the time of writing 1 USD = 0.92 Euro).
to_euros = lambda data: (data[0], data[1] * 0.92)

# Define a lambda function 'to_dollars' that takes a tuple 'data' and returns a new tuple.
# The new tuple contains the same item as the original tuple but with the price converted to dollars (at the time of writing 1 USD = 0.92 Euro).
to_dollars = lambda data: (data[0], data[1] / 0.92)

# Use the map() function to apply the 'to_euros' function to each tuple in the 'store' list.
# The result is an iterator, so we convert it to a list called 'store_euros'.
store_euros = list(map(to_euros, store))

# Use the map() function to apply the 'to_dollars' function to each tuple in the 'store' list.
# The result is an iterator, so we convert it to a list called 'store_dollars'.
store_dollars = list(map(to_dollars, store))

# Print the items in 'store_euros' and 'store_dollars' lists.

# Print the items in 'store_euros'.
for i in store_euros:
    print(i)

# Print a separator line for clarity.
print("-----------------------")

# Print the items in 'store_dollars'.
for i in store_dollars:
    print(i)
