# OOP = Object Oriented Programming



#NEEDED FILE: car.py
#Contents of car.py:

# class Car:
    
#     def __init__(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color

#     def drive(self):
#         print("\nThis " + self.make + " is driving")

#     def stop(self):
#         print("\nThis " + self.make + " is stopped")


#Imports
import time
from car import Car

#Easy to understand
car_1 = Car("Bentley","Mulliner",2021,"black")
car_2 = Car("Rolls Royce","Ghost",2022,"blue")

#Self explanatory
print("----------------------------")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print("----------------------------")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

#Self explanatory
car_1.drive()
time.sleep(3)
car_2.stop()





