# classes, instances, methods
# blueprint / plans
# 
##########################################################################
import random

# dog class
class Dog:
    info = "Man's best friend"

    def __init__(self, name):
        print("I am alive")
        self.lucky_number = random.randint(1,10)
        self.name = name
    
    def bark(self):
        print(f"woof! my name is {self.name} and my number is {self.lucky_number}")


# print(Dog.info)

# dog instance/object
dog1 = Dog("Fido")
dog2 = Dog("Toopka")

# print(dog1.lucky_number, dog1.name) 
# print(dog2.lucky_number, dog2.name)


dog1.bark()
dog2.bark()

# desk class

class Desk:
    '''A furniture item designed to be a physical workspace.'''
    
def __init__(self, leg_count, shelf_count, surface_type, color):
    self.leg_count = leg_count
    self.shelf_count = shelf_count
    self.surface_type = surface_type
    self.color = color


# print(Desk.legs)
# my_desk = Desk(3, 5, "flat", "gray")

    # legs = 3
    # shelves = 5
    # surface = "flat"
    # color = "gray"
