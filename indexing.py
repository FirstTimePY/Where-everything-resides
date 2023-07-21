# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "joe Mama!"


#Checks if the first letter of the name is lowercase and makes it uppercase
#if(name[0].islower()):
#    name = name.capitalize()

#Creating the first name variable and making it uppercase
firstName = name[:3].upper()
#Creating the last name variable and making it lowercase
lastName = name[4:8].lower()
#Creating the variable that stores the last character in our name
lastChar = name[-1]

# Printing (self explanatory)
print(firstName + " " + lastName)
print("Last Character: " + lastChar)













