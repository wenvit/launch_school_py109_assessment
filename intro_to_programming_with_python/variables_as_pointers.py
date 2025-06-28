# In your own words, explain the difference 
# between these two expressions.

# my_object1 == my_object2
# my_object1 is my_object2

# Solution:

# my_object1 == my_object2 is evaluating the value equality of 
# my_object1 and my_object2. This will return True if the two 
# variables have the same value. If the variables are collections, they 
# must be the same data type and same elements.

# my_object1 is my_object2 is evaluating the object equality
# of the two variables. This expression will return True if the 
# two variables are pointing to the same object in memory.

# - - - - - - - - - - - - - -
# 2. Without running this code, what will it print? Why?

# set1 = {42, 'Monty Python', ('a', 'b', 'c')}
# set2 = set1
# set1.add(range(5, 10))
# print(set2)

# # Solution:

# # This will print: 
# {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)} # not necessarily in this order

# This is because on line 21, `set2` is assigned to `set1` meaning both 
# `set2` and `set1` variables point to the same object in memory. When `set1` is
# mutated on line 22 by invoking the `add` method with the argument 
# `range(5, 10)`, the change can be seen in `set2` because they point 
# to the same object. The elements in `set1` and `set2` will not
# necessarily print out in the same order because sets are unordered 
# collections.

# - - - - - - - - - - - - - -
# 3. Without running this code, what will it print? Why?

# dict1 = {
#     "Hitchhiker's Guide to the Galaxy": 42,
#     'Monty Python': 'The Life of Brian',
#     'Airplane!': "Don't call me Shirley!",
# }

# dict2 = dict(dict1)
# dict2['Monty Python'] = 'Holy Grail'
# print(dict1['Monty Python'])

# Solution:

# This code will print: The Life of Brian
# This is because the `dict` constructor function creates
# a copy of the `dict` object and assigns it to `dict2` (line 47).
# When the value associated with the `Monty Python` key in the 
# `dict2` copy is reassigned on line 48, the change isn't seen in the
# original `dict1` object because `dict2` is a copy. Note that `dict2` is
# a shallow copy, which means if a mutable object had been updated in `dict2`
# instead of a string, the changes would be seen in both `dict1` and `dict2` 

# dict1 = {
#     "Hitchhiker's Guide to the Galaxy": 42,
#     'Monty Python': ['The Life of Brian'],
#     'Airplane!': "Don't call me Shirley!",
# }

# dict2 = dict(dict1)
# dict2['Monty Python'][0] = 'Holy Grail'
# print(dict1['Monty Python'])  # ['Holy Grail']

# - - - - - - - - - - - - - -
# 4. Without running this code, what will it print? Why?

# dict1 = {
#     'a': [1, 2, 3],
#     'b': (4, 5, 6),
# }

# dict2 = dict(dict1)
# dict1['a'][1] = 42 
# print(dict2['a']) 

# Solution:

# This will print:
# [1, 42, 3]
# On line 80, the `dict` constructor function creates a shallow copy of
# `dict1` and assigns it to `dict2`. The `dict2` shallow copy is a duplicate
# of the top-level structure of `dict1` with the same keys but the values 
# are not duplicates, they are references to the same objects in the original. 
# On line 81, the list object associated with the `dict1` key 'a' is mutated
# by updating the value at index 1 to 42. Because this mutates the same list 
# object as the object referenced by key 'a' in `dict2`, the change can 
# immediately be seen when printing `dict2['a']`. If this behavior is not 
# intended, a deep copy of the dictionary can be created using copy.deepcopy() 
# from the copy module.

# - - - - - - - - - - - - - -
# 5. Write some code to create a deep copy of the dict1 object and assign 
# it to dict2. You should only modify the code where indicated.

# import copy

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = copy.deepcopy(dict1) # You may modify the `???` part
#             # of this line

# # All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])

# # All of these should print True

# print(dict1['a'][0][0] is dict2['a'][0][0])
# print(dict1['a'][0][1] is dict2['a'][0][1])
# print(dict1['a'][1][0] is dict2['a'][1][0])
# print(dict1['a'][1][1] is dict2['a'][1][1])
# print(dict1['b'][0][0] is dict2['b'][0][0])
# print(dict1['b'][0][1] is dict2['b'][0][1])
# print(dict1['b'][1][0] is dict2['b'][1][0])
# print(dict1['b'][1][1] is dict2['b'][1][1])

# - - - - - - - - - - - - - -
# 6. The following program is nearly identical to that of the previous 
# exercise. However, this time, it should create a shallow copy of dict1. 
# Be careful: you're not allowed to use the copy module in this exercise.`

# In addition, before you run this code, can you predict the output values?

# dict1 = {
#     'a': [{7, 1}, ['aa', 'aaa']],
#     'b': ({3, 2}, ['bb', 'bbb']),
# }

# dict2 = dict(dict1) # You may modify the `???` part
            # of this line

# print(dict1         is dict2)          # False
# print(dict1['a']    is dict2['a'])     # True
# print(dict1['a'][0] is dict2['a'][0])  # True
# print(dict1['a'][1] is dict2['a'][1])  # True
# print(dict1['b']    is dict2['b'])     # True
# print(dict1['b'][0] is dict2['b'][0])  # True
# print(dict1['b'][1] is dict2['b'][1])  # True
