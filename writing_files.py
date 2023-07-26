# kinda similar to reading files

#The text to write in the new file we create
text = "whats up\n\ni still like turtles"
text2 = "\n\nthis text is appended"

# Same as with reading files, the default after the path is "r" for read, but because we want to write we put in "w"
with open("C:\\Users\\User\\Desktop\\testfolder\\testfile2.txt",'w') as file:
    #We write in the new file what is written in the text string
    file.write(text)

# We want to append so we put in "a"
with open("C:\\Users\\User\\Desktop\\testfolder\\testfile2.txt",'a') as file:
    #We write in the new file what is written in the text string
    file.write(text2)