# Duck typing = Concept where the class of an object is less important than the methods/attributes it possesses.
#               Class type is not checked if the minimum methods/attributes are present.
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck."

# Define a Duck class with 'walk' and 'talk' methods
class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

# Define a Chicken class with only the 'talk' method
class Chicken:
    def talk(self):
        print("This chicken is clucking")

# Define a Person class
class Person():
    # Define a method 'catch' that takes a 'duck' object as an argument
    def catch(self, duck):
        duck.walk()   # Call the 'walk' method of the 'duck' object
        duck.talk()   # Call the 'talk' method of the 'duck' object
        print("You caught the critter!")

# Create an instance of the Duck class
duck = Duck()

# Create an instance of the Chicken class
chicken = Chicken()

# Create an instance of the Person class
person = Person()

# Uncommenting the line below would raise an error since the Chicken class does not have a 'walk' method.
# person.catch(chicken)

# Call the 'catch' method of the 'person' object, passing the 'duck' object as an argument
# Since the 'duck' object has both 'walk' and 'talk' methods, it can be caught by the 'person' object.
person.catch(duck)
