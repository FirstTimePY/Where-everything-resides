# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

# it doesnt have to be **kwargs it can be anything, for example **hello or **joe
def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello There", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")


#This should make sense if you know basic python and have been following all my code
hello(title="Mr.",first="Joe",middle="Jeff",last="Mama")








