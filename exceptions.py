#exception = events detected during execution that interrupt the flow of a program

#This will try the following code
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

#If one of the numbers to be divided is a zero, then it will display the following print msg
except ZeroDivisionError:
    print("nuh uh you cannot do that blud (stop diving by zero)")
#If theres a value error/the user inputs anything BUT a number it will display the following print msg
except ValueError:
    ("blud i said no (numbers only)")
#For any other exceptions just print "Something went wrong"
except Exception:
    print("Something went wrong")
#If there are no exceptions, just print the result
else:
    print(result)
#Adding "finally:" beacuse its cool
finally:
    print(f"\n\nHello! This will always execute no matter what")
