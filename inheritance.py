#Inheritance

#Creating the Animal class (Parent)
class Animal:
    
    #Animal here will be alive
    alive = True

    #Defining eat
    def eat(self):
        print("This animal is eating")
    #Defining sleep
    def sleep(self):
        print("This animal is sleeping")

#Creating the Rabbit class (Child, because it contains the parent class "Animal" in its parenthesis)
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

#Creating the Fish class (Child, because it contains the parent class "Animal" in its parenthesis)
class Fish(Animal):
    #pass
    #Children copy all the variables inside their parent but they can also have their own stuff
    def swim(self):
        print("This fish is swimming")

#Creating the Hawk class (Child, because it contains the parent class "Animal" in its parenthesis)
class Hawk(Animal):
    #pass
    #Children copy all the variables inside their parent but they can also have their own stuff
    def fly(self):
        print("This hawk is flying")

#yes
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

#Calling their functions
rabbit.run()
fish.swim()
hawk.fly()



















