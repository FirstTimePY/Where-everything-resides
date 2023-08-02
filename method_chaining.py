# method chaining = calling multiple methods sequentially - each call performs an action on the same object and returns self


class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

#Normally we would call 2 functions like this:
#car.turn_on()
#car.drive()

#But with method chaining we can do it with 1 line
#car.turn_on().drive()

#Another Example:
#car.brake().turn_off()

#Lets call all 4 functions at once:

car.turn_on().drive().brake().turn_off()

#After a while the above code can become a bit hard to read, so we can "format" it:

# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()

