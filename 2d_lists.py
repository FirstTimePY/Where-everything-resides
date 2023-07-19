# 2D Lists = a list of lists

#making the lists
drinks = ["water", "coffee", "soda", "tea"]
food = ["pizza", "burger", "ice cubes"]
dessert = ["dog", "cake"]

#combining the lists into 1/making the 2D list
everything = [drinks, food, dessert]

# Prints the item "0" in the list "2" <--> list 2 refers to "dessert" and item 0 refers to "dog" inside "dessert"
print(everything[2][0])
