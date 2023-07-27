#Importing the OS library and shutil so we can remove the file
import os
import shutil

#Creating the path variable and the file it leads to
#path = "epic.txt"
path = "empty" #empty = folder

#Self explanatory
try:
    #Removing the file provided in the path
    #os.remove(path)

    #Removing the dir provided in the path
    os.rmdir(path)

    #Delete a directory containing files
    #shutil.rmtree(path)


#If the file provided in the path is not found then print the following
except FileNotFoundError:
    print("File was not found")
#If you do not have perimssion to delete the dir or file provided in the path the following print message with show up
except PermissionError:
    print("You dont got no perms to delete that blud")
#Example: if you use "os.rmdir" to delete a dir thats NOT empty, the following will output:
except OSError:
    print("You cant delete that using that function")
#If there are no exceptions, the following will print as a success message
else:
    print(path+" was deleted")