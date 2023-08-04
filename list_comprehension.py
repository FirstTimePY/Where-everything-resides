# list comprehension = a way o create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression (if/else) for item in iterable if condiional]




# squares = []                # create an empty list
# for i in range(1,11):       #create a for loop
#     squares.append(i * i)   #define wha each loop iteration should do
# print(squares)              #print

# #Making the exact same thing but using a list comprehension:A
# squares = [i*i for i in range(1,11)]
# print(squares)


#students = [100,90,80,70,60,50,40,30,0]

#passed_students = list(filter(lambda x: x >= 60, students))

#passed_students = [i for i in students if  i >= 60]

#passed_students = [i if  i >= 60 else "FAILED" for i in students]

#print(passed_students)




# A better version:


# A list of student scores (out of 100)
student_scores = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# A dictionary mapping student names to their respective scores
student_grades = {
    "Alice": 100,
    "Bob": 90,
    "Charlie": 80,
    "David": 70,
    "Eve": 60,
    "Frank": 50,
    "Grace": 40,
    "Hannah": 30,
    "Isaac": 0
}

# A list comprehension to determine if each student passed or failed based on the score (>= 60)
# If the score is greater than or equal to 60, use the score itself, otherwise, set the value to "FAILED"
passed_students = [f"{name} - {score}" if score >= 60 else f"{name} - FAILED" for name, score in student_grades.items()]

# Print the results in a neat and readable format
print("=== Student Grades ===")
for student_info in passed_students:
    
    print(student_info)
