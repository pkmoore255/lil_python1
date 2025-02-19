# functions, parameters, input
# reference, with examples
# 
##########################################################################

# define function
def bark():
    print("woof woof")

# for i in range(10):
#     bark()

# parameters
def hello(name):
    print(f"Hello {name}!")

# hello("Jay")

def add_numbers(num1,num2):
    print(num1 + num2)

# add_numbers(4,8)

def dog_info(age,name):
    print(f"Your dog, {name}, is {age} years old.")

# dog_info(7,"Zoey")

def double(number):
    return number * 2

new_number = double(5)
# print(new_number)


def make_caps(string):
    cap_string = string.upper()
    return cap_string

names = ['g', 'i', 'joe']

# for name in names:
#     print(name.upper())

# print(make_caps("hey there"))


# input

# user_text = input('Please enter your name: ')
# print(f"Hey there {user_text}")

# user_number = input("What do you want to double?")
# print(int(user_number)*2)

# def change_text_case()

user_text = input("Enter some text: ")
upper_or_lower = input("Enter 1 for uppercase and 2 for lowercase: ")

if upper_or_lower == "1":
    print(user_text.upper())
if upper_or_lower == "2":
    print(user_text.lower())
else:
    print("Please try again.")