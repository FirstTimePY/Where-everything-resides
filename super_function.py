# super() = Function used to give access to the methods of a parent class. Returns a temporary object of a parent class when used

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)  # Call the parent class's __init__ method to initialize length and width
                                        # using the 'super()' function, which returns a temporary object of the parent class.
        
    def area(self):
        return self.length * self.width   # Calculate and return the area of the square

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)   # Call the parent class's __init__ method to initialize length and width
        self.height = height              # using 'super()' and set the height attribute for the cube.

    def volume(self):
        return self.length * self.width * self.height  # Calculate and return the volume of the cube

# Create instances of Square and Cube classes
square = Square(3, 3)
cube = Cube(3, 3, 3)

# Print the area of the square and the volume of the cube
print(square.area())
print(cube.volume())



