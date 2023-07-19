# tuple(s) = collection which is ordered and unchangeable
#        used to group together related data


# creating a collection of student records and using tuples to help us do that
student = ("Joe",16,"male")

#Print how many times "Joe" appears
#print(student.count("Joe"))
#Print the index of "male" in student
#print(student.index("male"))

#Display the contents of a tuple using a "for" loop
for a in student:
    print(a)

#Checks if "Joe" is present in "student" then prints "Joe is here"
if "Joe" in student:
    print("Joe is here")
else:
    #If "Joe" is NOT present in "student" then it prints the following:
    print("Joe isn't here :(")
