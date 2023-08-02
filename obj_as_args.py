# Define a class Car
class Car:
    color = None  # Class-level attribute 'color' is initialized to None

# Define a class Motorcycle
class Motorcycle:
    color = None  # Class-level attribute 'color' is initialized to None

# Define a function change_color that takes a 'car' object and a 'color' as arguments
def change_color(car, color):
    car.color = color  # Update the 'color' attribute of the 'car' object with the provided 'color'

# Create three instances of the Car class: car_1, car_2, and car_3
car_1 = Car()
car_2 = Car()
car_3 = Car()

# Create an instance of the Motorcycle class: bike_1
bike_1 = Motorcycle()

# Call the change_color function for each car instance, updating their colors
change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "lime")

# Call the change_color function for the bike_1 instance, updating its color
change_color(bike_1, "white")

# Print the color attribute of each car instance
print(car_1.color)  # Should print "red" as we set it using the change_color function
print(car_2.color)  # Should print "blue" as we set it using the change_color function
print(car_3.color)  # Should print "lime" as we set it using the change_color function

# Print the color attribute of the bike_1 instance
print(bike_1.color)  # Should print "white" as we set it using the change_color function
