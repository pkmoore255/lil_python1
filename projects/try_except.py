# 
# this creates a random fortune 
# 
##########################################################################


print("before")

try:
    # 4 / 0
    # print(name)
    print(age)
except NameError as e:               # e is error variable, print relevant info
    print("This was a name issue")
    print(e)
except ZeroDivisionError:
    print("Can't divide by 0")
except:
    print("Something went wrong.")


class CheeseError(Exception):
    pass


def upper_fun(word):
    if len(word) <= 0:
        raise CheeseError("The word needs at least one character")
    if word.isalpha() == False:
        raise Exception("Please only use letters, no special characters")
    return word.upper()

print(upper_fun("909"))

print("after")
