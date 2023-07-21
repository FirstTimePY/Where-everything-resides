# Nested Function Calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function

#Code normally:
# num = input("Enter a whole positive num: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

#Using nested function calls: (you will probably never see 4 god damn nested functions in real code)
print(round(abs(float(input("Enter a whole positive num: ")))))