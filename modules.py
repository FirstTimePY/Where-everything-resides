# module = a file containing py code. May contain funcs, classes, etc.
# used with modular programming, which is seperate a program into parts





#How msgs.py looks like:
# def hello():
#     print("Hello, have a nice day!")

# def bye():
#     print("Cya later")





#Importing everything from msgs.py
# import msgs as m

#Calling functions imported from msgs.py
# m.hello()
# m.bye()


#Another way to do the above code:
from msgs import hello,bye #(change it from "hello,bye" to "*" to import everything)

hello()
bye()


#List all modules available in python
help("modules")