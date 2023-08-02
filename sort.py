# Sorting in Python

# sort() method: Used with lists, it sorts the elements of the list in place.

# sorted() function: Used with iterables, it returns a new sorted list from the items in the iterable.

# Example 1:
# Uncomment the code below to sort the list 'students' in reverse order and print the sorted list.

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
# students.sort(reverse=True)
# for i in students:
#     print(i)

# This will print the list in reverse alphabetical order:
# Squidward
# Spongebob
# Sandy
# Patrick
# Mr. Krabs

# Uncomment the code below to use the sorted() function to create a new sorted list called 'sorted_students'.

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
# sorted_students = sorted(students, reverse=True)
# for i in sorted_students:
#     print(i)

# The output will be the same as the previous example.

# Example 2:
# In this example, we have a list of tuples 'students', where each tuple contains a name, a grade, and an age.

students = [("Squidward", "A", 31),
            ("Sandy", "B", 25),
            ("Patrick", "F", 26),
            ("Spongebob", "C", 29),
            ("Mr. Krabs", "D", 41)]

# We define a lambda function called 'grade' that takes a tuple 'grades' and returns the element at index 1 (the grade).
# This will be used as the key for sorting the list of tuples.
grade = lambda grades: grades[1]

# We use the sort() method on the 'students' list, specifying the 'key' parameter as our 'grade' lambda function.
# This sorts the list of tuples based on the grade, in ascending order (from A to F).
students.sort(key=grade)

# We then loop through the sorted list and print each tuple.
for i in students:
    print(i)

# The output will be the list sorted based on the grades:
# ('Squidward', 'A', 31)
# ('Sandy', 'B', 25)
# ('Spongebob', 'C', 29)
# ('Patrick', 'F', 26)
# ('Mr. Krabs', 'D', 41)
