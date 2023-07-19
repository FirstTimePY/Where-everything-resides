# nested loops = the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"
# doesnt matter if its a while or for loop

# simple inputs:
rows = int(input("How many rows do you want?: "))
colums = int(input("How many colums do you want?: "))
symbol = input("Enter a symbol to use for this test: ")

#creating the outer loop:
for i in range(rows):
    #creating the inner loop:
    for j in range(colums):
#printing:
        print(symbol, end="")
    print()
