# This code demonstrates multiple inheritance in Python. Multiple inheritance occurs when a child class is derived from more than one parent class.

# First, we define a class named 'Prey' representing animals that can flee.
class Prey:
    def flee(self):
        # Method representing the action of an animal fleeing.
        print("This animal flees")

# Next, we define a class named 'Predator' representing animals that can hunt.
class Predator:
    def hunt(self):
        # Method representing the action of an animal hunting.
        print("This animal is hunting")

# Now, we define three different classes, 'Rabbit', 'Hawk', and 'Fish', which are child classes inheriting from 'Prey' and/or 'Predator'.

# Class 'Rabbit' inherits from 'Prey' only.
class Rabbit(Prey):
    pass

# Class 'Hawk' inherits from 'Predator' only.
class Hawk(Predator):
    pass

# Class 'Fish' inherits from both 'Prey' and 'Predator', demonstrating multiple inheritance.
class Fish(Prey, Predator):
    pass

# Create instances of the classes.

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# Now, let's demonstrate how inherited methods work for each instance:

# Output: "This animal flees"
# Since 'Rabbit' inherits the 'flee' method from the 'Prey' class, calling 'rabbit.flee()' triggers the fleeing action.
#rabbit.flee()

# Output: "This animal is hunting"
# Since 'Hawk' inherits the 'hunt' method from the 'Predator' class, calling 'hawk.hunt()' triggers the hunting action.
#hawk.hunt()

# Output: "This animal flees" and "This animal is hunting"
# Since 'Fish' inherits both 'flee' and 'hunt' methods from both 'Prey' and 'Predator' classes,
# calling 'fish.flee()' triggers the fleeing action, and calling 'fish.hunt()' triggers the hunting action.
fish.flee()
fish.hunt()
