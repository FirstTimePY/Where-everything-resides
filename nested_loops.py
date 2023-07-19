# nested loops = the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"
# doesnt matter if its a while or for loop

rows = int(input("How many rows do you want?: "))
colums = int(input("How many colums do you want?: "))
symbol = input("Enter a symbol to use for this test: ")

for i in range(rows):
    for j in range(colums):
        print(symbol, end="")
    print()
