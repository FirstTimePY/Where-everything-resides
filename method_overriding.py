# Method Overriding in Python

# In object-oriented programming (OOP), method overriding occurs when a subclass provides a specific implementation for a method
# that is already defined in its superclass. The subclass overrides the behavior of the method inherited from the superclass.

# First, we define a base class named 'Animal'.
class Animal:
    def eat(self):
        # Method representing the generic eating action of an animal.
        print("This animal eats")

# Next, we define a subclass named 'Rabbit', which inherits from the 'Animal' class.

class Rabbit(Animal):
    # Since the 'Rabbit' class has no method definitions here, it implicitly inherits the 'eat' method from the 'Animal' class.
    # However, the 'eat' method can be overridden in the 'Rabbit' class to provide a specialized implementation for rabbits.

    def eat(self):
        # This is the overridden 'eat' method for rabbits, which provides a specific implementation for their eating behavior.
        print("This rabbit is eating a carrot")

# Create an instance of the 'Rabbit' class.
rabbit = Rabbit()

# Now, let's demonstrate method overriding:

# Output: "This rabbit is eating a carrot"
# When we call 'rabbit.eat()', the overridden 'eat' method in the 'Rabbit' class is invoked,
# and the specific implementation for rabbits (eating a carrot) is executed.
rabbit.eat()
