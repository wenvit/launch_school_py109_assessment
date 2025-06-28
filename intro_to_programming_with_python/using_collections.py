# 1. Write Python code to print the seventh number of range(0, 25, 3).

# 0, 3, 6, 9, 12, 15, 18, 21, 24

# # Solution:
# my_range = range(0, 25, 3)

# print(my_range[6])

# - - - - - - - - - - - - - -
# 2. Use slicing to write Python code to print a 6-character 
# substring of 'Launch School' that begins with the first c.

# text = 'Launch School'
# start = text.find('c')
# stop = start + 6

# print(text[start:stop])

# - - - - - - - - - - - - - -
# 3. Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

# Solution:

# orig_tuple = (1, 2, 3, 4, 5)

# tuple_list = list(orig_tuple)  
# tuple_list.reverse()   
# list_extract = tuple_list[1:-1]   
# result = tuple(list_extract)

# print(result)

# Tuples are immutable so this solution relies on using `list` constructor
# to convert to a list. Then the `reverse` method is called on the `list`
# object. `reverse` mutates list in place. This is followed by applying 
# slicing notation to create new list object from the index 1 through -1
# (stop index not inclusive). Final step is to apply `tuple` constructor
# function to convert list to tuple.

# - - - - - - - - - - - - - -
# 4. This is a 3-part question. Consider the following dictionary:

# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet',
# }

# Part 1: Write some code to print Bark by accessing the element 
# associated with the key Dog.
# Part 2: Write some code to print None when you try to print 
# the value associated with the non-existent key, Lizard.
# Part 3: Write some code to print <silence> when you try to 
# print the value associated with the non-existent key, Lizard.

# Solution:

# print(pets['Dog'])
# print(pets.get('Lizard'))
# print(pets.get('Lizard', '<silence>'))

# - - - - - - - - - - - - - -
# 5. Which of the following values can't be used as a key in a 
# dict object, and why?

# 'cat'   
# (3, 1, 4, 1, 5, 9, 2)  
# ['a', 'b']  
# {'a': 1, 'b': 2}  
# range(5)          
# {1, 4, 9, 16, 25} 
# 3                 
# 0.0               
# frozenset({1, 4, 9, 16, 25})  

# Solution:
# ['a', 'b']  
# {'a': 1, 'b': 2}  
# {1, 4, 9, 16, 25} 

# Dictionary keys must be immutable and hashable. A list, dictionary, and set are
# all mutable so cannot be used as dictionary keys. The other objects (string, tuple,
# range, integer, float, frozenset) are all immutable and can be used as dictionary
# keys.

# - - - - - - - - - - - - - -
# 6. What will the following code print?

# print('abc-def'.isalpha())  # False, contains '-'
# print('abc_def'.isalpha())  # False, contains '_'
# print('abc def'.isalpha())  # False, contains ' '
# print('abc def'.isalpha() and 
#       'abc def'.isspace())  # False, first string contains ' ', then short ciruits
# print('abc def'.isalpha() or 
#       'abc def'.isspace())  # False, both False, no short circuiting
# print('abcdef'.isalpha())   # True
# print('31415'.isdigit())    # True
# print('-31415'.isdigit())   # False, contains '-'
# print('31_415'.isdigit())   # False, contains '_'
# print('3.1415'.isdigit())   # False, contains '.'
# print(''.isspace())         # False, empty string

# - - - - - - - - - - - - - -
# 7. Write Python code to replace all the : characters in the string 
# below with +.

# Try this problem using the methods you've learned about in this chapter. 
# Once you have that working, use the Python documentation for 
# the str type to find an alternative solution.

#info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# Solution:
# elements = info.split(':')
# info_mod = '+'.join(elements)
# print(elements)
# print(info_mod)

#print(info.replace(':', '+'))

# - - - - - - - - - - - - - -
# 8. Explain why the code below prints different values on lines 3 and 4.

#text = "It's probably pining for the fjords!"

# print(text[21:35].rfind('f'))    
#print(text.rfind('f', 21, 35))  

# Solution:

# This will print:
# 8
# 29

# The first code snippet applies the `rfind` method to the slice
# of `text` starting at index 21 and stopping at index 35 (not inclusive).
#  `text[21:35]` returns a new string `'for the fjords'`.
# The index of the first 'f' from the right of the new string is `8``.
# In the second snippet, start and stop indexes are passed as 
# arguments to `rfind`. The start and stop indexes are in reference
# to the entire string `text`. In this case, the same instance of 'f' 
# is identified, but the index is 29 because it's in reference to
# the entire `text` string object. 

# - - - - - - - - - - - -- - 
# 9. Write some code to replace the value 6 in the following nested list with 606:

# stuff = [
#     ['hello', 'world'],
#     ['example', 'mem', None, 6, 88],
#     [4, 8, 12],
# ]

# Solution:

# Because lists are mutable, reassigning the list element at index 3
# within the nested list at index 1 mutates the list.

# stuff[1][3] = 606
# print(stuff)

# - - - - - - - - - - - - - -
# 10. Consider the following nested collection:

# cats = {
#     'Pete': {
#         'Cheddar': {
#             'color': 'orange',
#             'enjoys': {
#                 'sleeping',
#                 'snuggling',
#                 'meowing',
#                 'eating',
#                 'birdwatching',
#             },
#         },
#         'Cocoa': {
#             'color': 'black',
#             'enjoys': {
#                 'eating',
#                 'sleeping',
#                 'playing',
#                 'chewing',
#             },
#         },
#     },
# }

# Write one line of code to print the activities that Cocoa enjoys.
#print(cats['Pete']['Cocoa']['enjoys'])

# - - - - - - - - - - - - - -
# 11. Without running the following code, determine what each line 
# should print.

# print('johnson' in 'Joe Johnson')  # False
# print('sen' not in 'Joe Johnson')  # True
# print('Joe J' in 'Joe Johnson')    # True
# print(5 in range(5))               # False
# print(5 in range(6))               # True
# print(5 not in range(5, 10))       # False
# print(0 in range(10, 0, -1))       # False
# print(4 in {6, 5, 4, 3, 2, 1})     # True
# print({1, 2, 3} in {1, 2, 3})      # False
# print({3, 2} in {1, frozenset({2, 3})}) # True

# - - - - - - - - - - - - - -
# 12. Write some code that determines and prints whether the 
# number 3 appears inside each of these lists.
# You should print True or False depending on each result.

# numbers1 = [1, 3, 5, 7, 9, 11]  # True
# numbers2 = []                   # False
# numbers3 = [2, 4, 6, 8]         # False
# numbers4 = ['1', '3', '5']      # False
# numbers5 = ['1', 3.0, '5']      # True

# print(3 in numbers1)
# print(3 in numbers2)
# print(3 in numbers3)
# print(3 in numbers4)
# print(3 in numbers5)

# - - - - - - - - - - - - - -
# 13. Without running the following code, determine what each 
# print statement should print.

# cats = ('Cocoa', 'Cheddar',
#         'Pudding', 'Butterscotch')

# print('Butterscotch' in cats)  # True
# print('Butter' in cats)        # False
# print('Butter' in cats[3])     # True
# print('cheddar' in cats)       # False

# - - - - - - - - - - - - - -
# 14. Assume you have the following sequences:

# my_str = 'abc'
# my_list = ['Alpha', 'Bravo', 'Charlie']
# my_tuple = (None, True, False)
# my_range = range(10, 60, 10)

# Write some code that combines the sequences into a 
# list of tuples. Each tuple should contain one member 
# of each sequence. Print the final result so you can 
# see all the values, which should look like this:

# [('a', 'Alpha', None, 10),
#  ('b', 'Bravo', True, 20),
#  ('c', 'Charlie', False, 30)]

# print(list(zip(my_str, my_list, my_tuple, my_range)))

# - - - - - - - - - - - - - -
# 15. Without running the following code, what values will 
# be printed by line 10?

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
values = pets.values()
print(keys) 
del pets['Dog'] 
pets['Snake'] = 'Sssss' 
print(keys) 
print(values)






# Solution: 
# This will print ['Cat', 'Bird', 'Snake'] wrapped as a 
# dict view. The dict view object immediately updates as
# changes are made