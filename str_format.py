# str.format() aka string format = optional method that gives users more control when displaying output


animal = "cow"
item = "moon"
#animalk = "cow"
#itemk = "moon"


#print("The "+animal+" jumped over the "+item)

#An elegant way to write the above code:

print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item)) #positional argument
print("The {animalk} jumped over the {itemk}".format(animalk="cow",itemk="moon")) #keyword argument


#Another elegant way to write it:

txt = "The {} jumped over the {}"
print(txt.format(animal,item))





#Elegant name printing

name = "Joe"

#Adds 10 spaces of padding
print("Hello my name is {:10} Nice to meet you".format(name))
#Left align based on the padding inputted
print("Hello my name is {:>10} Nice to meet you".format(name))
#Right align based on the padding inputted
print("Hello my name is {:<10} Nice to meet you".format(name))
#Center align based on the padding inputted
print("Hello my name is {:^10} Nice to meet you".format(name))





# Number formatting


num = 3.14159
num2 = 1000
num3 = 69
anum = 3491823

# Print only the first 2 numbers after "." in the number PI
print("The number PI is {:.2f}".format(num))
# Turns 1000 to 1,000
print("The number is {:,}".format(num2))
# Turning num3 to binary
print("The number is {:b}".format(num3))
# Turning num2 to octo
print("The number is {:o}".format(num2))
# Turning anum to HEX
print("The number is {:X}".format(anum))
# Turning anum to scientific notation
print("The number is {:E}".format(anum))

