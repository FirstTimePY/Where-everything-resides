# woohoo this seems fun!
# basics of file detection

#importing the OS library
import os

#Setting our file or folder path
path = "C:\\Users\\User\\Desktop\\testfolder\\"

#If our path is real and exists then it will print "That path exists!"
if os.path.exists(path):
    print("That path exists!")
    #Check if the path leads to a file and print something if so
    if os.path.isfile(path):
        print("That is a file!")
    #Check if the path leads to a folder/directory and print something if so
    elif os.path.isdir(path):
        print("That is a directory or folder")
#If our path is NOT real and does NOT exists then it will print "That path does not exist!"
else:
    print("That path does not exist!")