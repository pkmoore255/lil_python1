# classes, instances, methods, inheritance
# blueprint / plans
# 
##########################################################################
import random

class Animal:
    info = "a living organism that feeds on organic matter"

    def __init__(self, name):
        print("an animal is created")
        self.name = name

# dog class
class Dog(Animal):
    info = "Man's best friend"

    def __init__(self, name):
        # super().__init__(name)    points to / runs parent class first
        print("a dog is created")
        self.lucky_number = random.randint(1,10)
        self.name = name
        self.fur = ""
    
    def bark(self):
        print(f"woof! my name is {self.name} and my number is {self.lucky_number}")



class Bulldog(Dog):

    def __init__(self, name):
        super().__init__(name)
        print("A bulldog is created")


# print(Dog.info)

# dog instance/object
dog1 = Bulldog("Fido")


# dog2 = Dog("Toopka")

# print(dog1.lucky_number, dog1.name) 
# print(dog2.lucky_number, dog2.name)
print(dog1.info)

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
