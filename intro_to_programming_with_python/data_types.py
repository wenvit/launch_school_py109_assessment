### EXERCISES FROM DATA TYPES CHAPTER

# 1. Identify the data type or class for each of the following values:

# Note: data type is more general terminology, while class is specifically
# defined as a class in Python

# Solution:

# def what_class(obj):
#     return type(obj).__name__

# print(what_class('True'))         # str 
# print(what_class(False))          # bool 
# print(what_class((1, 2, 3)))      # tuple
# print(what_class(1.5))            # float
# print(what_class([1, 2, 3]))      # list
# print(what_class(2))              # int
# print(what_class(range(5)))       # range
# print(what_class({1, 2, 3}))      # set
# print(what_class(None))           # NoneType
# print(what_class({'foo': 'bar'})) # dict

# - - - - - - - - - - - - - 

# 2. Create a tuple called names that contains several pet names. 
# For instance:

# Name
# Asta
# Butterscotch
# Pudding
# Neptune
# Darwin

# Solution:

# pet_names = (
#     'Asta', 
#     'Butterscotch', 
#     'Pudding', 
#     'Neptune', 
#     'Darwin',
# )

# print(pet_names)
# print(type(pet_names).__name__)

# - - - - - - - - - - - - - 

# 3. Create a dictionary named pets that contains a 
#    list of pet names and the type of animal. 

# For instance:

# Name	Animal
# Asta	dog
# Butterscotch	cat
# Pudding	cat
# Neptune	fish
# Darwin	lizard

# Solution:

# pets = {
#     'Asta':         'dog',
#     'Butterscotch': 'cat', 
#     'Pudding':      'cat',
#     'Neptune':      'fish',
#     'Darwin':       'lizard',
# }

# print(pets)
# print(type(pets).__name__)