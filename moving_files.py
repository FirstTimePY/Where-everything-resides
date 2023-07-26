import os

#Same can be done for folders
source = "C:\\Users\\User\\Desktop\\testfolder\\cooler_file.txt"
destination = "C:\\Users\\User\\Desktop\\cooler_file.txt"

#Self explanatory if you looked at the code of my other files
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source + " was not found")