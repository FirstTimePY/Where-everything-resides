# loop control statements = chagne a loops extension from its normal sequence

# (b)reak = used to terminate the loop
# (c)ontinue = skips to the next iteration of the loop
# (p)ass = does nothing, acts as a placeholder



# example of when a break would be useful:

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break



#############################################################

#use of the continue statement
# phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")



#############################################################

# using the pass statement:

for i in range(1,21+1):

    #this will skip the number "20" because we put a "pass" statement for it
    if i == 20:
        pass
    else:
        print(i)