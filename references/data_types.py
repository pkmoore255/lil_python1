# data types
# numbers, strings, etc.
# reference, with examples

##########################################################################

# int
day = 21
temp = -15

# float
weight = 110.10

# print(temp * 100)

bars = 4 # number of chocolate bars
sugar = 24.5 # grams of sugar in each bar

# strings
shirt = "blue"
cafe = "My Boba Cafe"
store = "Nick's Surf Shop, the \"best\" there is"

# print(shirt, sugar)

##########################################################################

day = 21
day_name = 'Tuesday'
month = 'October'
temp = 55

# print(f"Today is {day_name} {month} {day} and it's {temp} degrees outside.")



##########################################################################

# boolean
light_is_on = False

# if light_is_on:
#     print("The light is on")

# baby_is_asleep = True

# if baby_is_asleep:
#    print("Time to wake up.")
# else:
#     print("Go to sleep.")


age = 25

if age >= 18:
    print("Adult.")
else:
    print("Child.")



##########################################################################
import random


# print(random.randint(1,10)) # inclusive
# print(random.random())

# version 1
answer_list = ['yes', 'no', 'maybe']

print(random.choice(answer_list))


# version 2
answer = random.randint(1,3)

if answer == 1:
    print('yes')
if answer == 2:
    print('no')
if answer == 3:
    print('maybe')
