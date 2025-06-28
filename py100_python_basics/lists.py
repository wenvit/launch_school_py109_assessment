# First Element
# Write a function that returns the first element 
# of a list provided as an argument. For example:

# def first(lst):
#     if not lst:
#         return 'Must provide non-empty list'
#     return lst[0]

# print(first(['Earth', 'Moon', 'Mars']))  # Earth
# print(first([]))

# - - - - - - - - - - - - - -
# Last Element
# Write a function that returns the last element 
# of a list provided as an argument. For example:

# def last(lst):
#     return lst[-1]

# def last(lst):
#     if not lst:
#         return 'Must provide non-empty list'
#     return lst[len(lst) - 1]

# print(last(['Earth', 'Moon', 'Mars']))  # Mars
# print(last([]))

# - - - - - - - - - - - - - -
# Add + Delete
# We are given the following list of energy sources.

# Write some code to remove 'fossil' from the list, 
# then add 'geothermal' to the end of the list.

# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
# energy.remove('fossil')
# energy.append('geothermal')
# print(energy)

# - - - - - - - - - - - - - -
# Alphabet
# Split the string alphabet into a list of characters.

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_lst = list(alphabet)
# print(alphabet_lst)

# - - - - - - - - - - - - - -
# Filter
# Count the number of elements in scores that are 100 or above.

# scores = [96, 47, 113, 89, 100, 102]

# scores_above_100 = [
#     score 
#     for score in scores
#     if score >= 100
# ]

# print(len(scores_above_100))

# - - - - - - - - - - - - - -
# Vocabulary
# You've been given a list of vocabulary words grouped into sub-lists, 
# by meaning. This is a two-dimensional list or a nested list. 
# Write some code that iterates through and prints all the words, 
# one per line.

# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# for inner_lst in vocabulary:
#     for word in inner_lst:
#         print(word)

# - - - - - - - - - - - - - -
# Equality
# Predict the output of the code shown below. When you run the code, 
# do you see what you expected? Why or why not?

# list1 = [2, 6, 4]
# list2 = [2, 6, 4]

# print(list1 == list2)

# This will print `True`. `==` checks for value equality, meaning
# objects with the same value, meaning same data type, same length, 
# and elements in the same order. The lists do not have to be 
# the same objects in memory. To check for object equality, use `is`
# operator. In this case, `list1 is list2` would return `False`
# because these are two different objects.

# - - - - - - - - - - - - - -

# Type
# How can you check if a variable holds a value that is a list? 
# Given two variables, verify whether the values they hold are lists.

# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'

# print(0 in some_value1)
# print(100 in some_value1)
# print('k' in some_value2)
# print('z' in some_value2)

# print(isinstance(some_value1, list))
# print(isinstance(some_value1, int))
# print(isinstance(some_value2, list))
# print(isinstance(some_value2, str))

# - - - - - - - - - - - - - -
# Travel
# The destinations list contains a list of travel destinations.

# Write a function that, without using the built-in in operator, 
# checks whether a specific destination is included within 
# destinations. For example: When checking whether 'Barcelona' 
# is contained in destinations, the expected output is True,
# whereas the expected output for 'Nashville' is False.

# def is_destination(destination, lst):
#     for city in lst:
#         if city == destination:
#             return True
#     return False

# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']

# print(is_destination('Barcelona', destinations))
# print(is_destination('Nashville', destinations))
# print(is_destination('', destinations))

# - - - - - - - - - - - - - -
# Passcode
# We generated parts of a passcode and now want to combine 
# them into a string. Write some code that creates and 
# prints a string that contains each portion of the 
# passcode separated by hyphens (-).

# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# passcode_combined = '-'.join(passcode)
# print(passcode_combined)
# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

# - - - - - - - - - - - - - -
# Checking items off the grocery list
# We have a grocery list. As we check off items on that list, 
# from the top of the list to the bottom, we want to remove 
# them from the list.

# Write code that removes the items from grocery_list, 
# one by one, until it is empty. If you print the elements you 
# remove, the expected behavior would look as follows.

# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']

# for idx in range(len(grocery_list)):
#     print(grocery_list.pop(0))
# print(grocery_list)

# A better solution from Launch School:

while grocery_list:
    item = grocery_list.pop(0)
    print(item)
print(grocery_list)

# Expected output
# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []