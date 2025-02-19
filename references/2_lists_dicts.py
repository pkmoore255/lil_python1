# lists, for loops, dictionaries
# reference, with examples
# 
##########################################################################

# lists
ingredients_list = ["milk", "eggs", "sugar", "cocoa powder"]
numbers = [4, 7, 28]
# print(numbers[0])

ingredients_list.append("vanilla extract")
ingredients_list.insert(3, "flour")
del(ingredients_list[4])

# print(ingredients_list)


# for loops
# for item in ingredients_list:
#     ingredients_list.pop()
#     print(ingredients_list)

# for number in range(40):
#     print(number*2)


# dictionaries
# cat name:age
cats = {"Phoebe":12, "Oliver":10, "Snowball":3}

cats["Wilson"] = 1
del(cats["Oliver"])

# print(cats["Phoebe"]) # lookup name (key), print age (value)

is_odd_dict = {0:False, 1:True, 2:False, 3:True, 4:False, 5:True, 6:False, 7:True}

print(is_odd_dict[5])
