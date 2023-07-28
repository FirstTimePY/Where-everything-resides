#multi-level inheritance = when a derived (child) class inherits another derived (child) class



# Base class 'Organism' with an attribute 'alive' set to True.
class Organism:
    alive = True

# Derived class 'Animal' inheriting from 'Organism'.
class Animal(Organism):
    def eat(self):
        # Method representing the action of an animal eating.
        print("This animal is eating")

# Derived class 'Dog' inheriting from 'Animal'.
class Dog(Animal):
    def bark(self):
        # Method representing the action of a dog barking.
        print("This dog is barking")



    #Optional code i made on my own :)
    # def status(self):
    #     if self.alive:
    #         print(f"This {type(self).__name__} is alive")
#dog.status()



# Create an instance of the 'Dog' class.
dog = Dog()

# Demonstrate usage of inherited attributes and methods:

# Output: True
print(dog.alive)
# When accessing 'dog.alive', it inherits the 'alive' attribute from 'Organism',
# indicating that the dog is alive.

# Output: "This animal is eating"
dog.eat()
# The 'eat' method is inherited from the 'Animal' class.
# Calling 'dog.eat()' prints a message indicating that the dog is eating.

# Output: "This dog is barking"
dog.bark()
# The 'bark' method is defined in the 'Dog' class itself.
# Calling 'dog.bark()' prints a message indicating that the dog is barking.
