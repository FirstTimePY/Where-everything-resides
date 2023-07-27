
#REQUIED FILE: car.py
#CONTENTS OF car.py:

# class Car:

#     wheels = 4 #class variable
    
#     def __init__(self, make, model, year, color):
#         self.make = make #instance variable
#         self.model = model #instance variable
#         self.year = year #instance variable
#         self.color = color #instance variable




#Very self explanatory
from car import Car

car_1 = Car("Bentley","Mulliner",2021,"black")
car_2 = Car("Rolls Royce","Ghost",2022,"blue")

#Change the wheels from 4 to 3
car_1.wheels = 3

print(car_1.wheels)
print(car_2.wheels)

# print(Car.wheels)