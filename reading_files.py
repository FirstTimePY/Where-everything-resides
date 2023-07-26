#Lets read the contents of our test txt file!

try:
#With the listed test file below, we open it and read its contents and print them
    with open("C:\\Users\\User\\Desktop\\testfolder\\testfile.txt") as file:
        print(file.read())
#Exception, if the file is not found, print the following
except FileNotFoundError:
    print("file not found")

# This checks if the file closes after its done being read, if so it will print "True" if not it will print "False"
#print(file.closed)
