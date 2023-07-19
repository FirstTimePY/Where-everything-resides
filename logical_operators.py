# logical operators (and,or,not) = used to check if two or more conditional statements are true

temp = int(input("What is the temp outside? (in celcius): "))

if temp >=0 and temp <=30:
    print("The weather is nice today")
    print("Go outside for once now")
elif temp < 0 or temp >30: 
    print("The temp is not so good today")
    print("Stay inside and play minecraft")

#Reversing everything by using the "NOT" operator
# if not(temp >=0 and temp <=30):
#     print("The weather is nice today")
#     print("Go outside for once now")
# elif not(temp < 0 or temp >30): 
#     print("The temp is not so good today")
#     print("Stay inside and play minecraft")
