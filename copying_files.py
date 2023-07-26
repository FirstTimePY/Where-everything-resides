# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a dir
# copy2() = copy() + copies metadata (files creation and modification times)

import shutil


shutil.copyfile('C:\\Users\\User\\Desktop\\testfolder\\cool_file.txt', 'C:\\Users\\User\\Desktop\\testfolder\\copied.txt') #source, destination - for copy() and copy2() the args are the same
