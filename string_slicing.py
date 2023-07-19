# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]


#Full Name of the user:
name = "Joe Mama"

#Slicing the full name into the first and last name
first_name = name[0:3]
last_name = name[4:8]
#Another way to do it:
# first_name = name[:3]
# last_name = name[4:]

#Reversing the name
reversed_name = name[::-1]

#Normal Full Name using step
normal_name = name[0:8:1]

#Rather *Odd* full name with only every 2 characters being returned
odd_name = name[0:8:2]

#Rather *Very Odd* full name with only every 3 characters being returned
very_odd_name = name[0:8:3]



#Printing everything:

print("-----------------------------------------------------")
print("Combined Full Name: "+first_name + " " + last_name)
print("-----------------------------------------------------")
print("Normal Name: " + normal_name) 
print("-----------------------------------------------------")
print("Odd Name: " + odd_name) 
print("-----------------------------------------------------")
print("Very Odd Name: " + very_odd_name)
print("-----------------------------------------------------")
print("Reversed Full Name: " + reversed_name)
print("-----------------------------------------------------")




### more string slicing



# Removing and creating a substring based on the website URL
website1 = "https://google.com"
website2 = "https://x.com"

slice = slice(8,-4)

print("Website 1 name: " + website1[slice])
print("-----------------------------------------------------")
print("Website 2 name: " + website2[slice])
print("-----------------------------------------------------")