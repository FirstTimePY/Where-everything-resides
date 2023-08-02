# Prevents a user from creating an object of that class
# + Compels a user to override abstract methods in a child class

# Abstract class = A class which contains one or more abstract methods.
# Abstract method = A method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")  # This method overrides the abstract 'go' method from the parent class.
                                    # It provides the implementation for the 'go' method in the Car class.

    def stop(self):
        print("This car is stopped")  # This method overrides the abstract 'stop' method from the parent class.
                                      # It provides the implementation for the 'stop' method in the Car class.

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")  # This method overrides the abstract 'go' method from the parent class.
                                           # It provides the implementation for the 'go' method in the Motorcycle class.

    def stop(self):
        print("This motorcycle is stopped")  # This method overrides the abstract 'stop' method from the parent class.
                                             # It provides the implementation for the 'stop' method in the Motorcycle class.

# vehicle = Vehicle()  # You cannot create an instance of an abstract class. It raises an error.

car = Car()  # You can create an instance of the Car class because it is a concrete subclass that implements all the abstract methods.

motorcycle = Motorcycle()  # You can create an instance of the Motorcycle class because it is a concrete subclass that implements all the abstract methods.


# vehicle.go()  # This would raise an error since you cannot call abstract methods on an instance of an abstract class.

car.go()  # This will call the 'go' method of the Car class and print "You drive the car".

motorcycle.go()  # This will call the 'go' method of the Motorcycle class and print "You ride the motorcycle".

car.stop()  # This will call the 'stop' method of the Car class and print "This car is stopped".

motorcycle.stop()  # This will call the 'stop' method of the Motorcycle class and print "This motorcycle is stopped".
