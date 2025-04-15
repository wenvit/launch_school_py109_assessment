# 1. What does the following function do? 
# Be sure to identify the output value.

# def do_something(dictionary):
#     return sorted(dictionary.keys())[1].upper()

# my_dict = {
#     'Karl':     108,
#     'Clare':    175,
#     'Karis':    140,
#     'Trevor':   180,
#     'Antonina': 132,
#     'Chris':    101,
# }

# print(do_something(my_dict))

# This will print: CHRIS
# Within the function, several functions and methods are chained.
# First, the `keys` method is called on the local `dictionary`
# variable, which returns a dictionary view object of the keys.
# Then the `sorted` function passes the keys as an argument, which
# returns a new list of the dictionary keys sorted in alphabetical
# order. The element within the list at index 1 is accessed, and 
# the `upper` method is applied to it, which returns a new string
# with all cased letters uppercased. 

# - - - - - - - - - - - - - -
# 2. Use the sqrt function from the math library to write some 
# code that outputs the square root of 37. Try to write the 
# code in three different ways.

# Solution

# import math

# print(math.sqrt(37))

# from math import sqrt

# print(sqrt(37))

# import math as m

# print(m.sqrt(37))

# - - - - - - - - - - - - - -
# 3. Consider the following code:

# def sum_of_squares(num1, num2):
#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

# Write a nested function in sum_of_squares that will 
# make this code work as shown.

# Solution:
# def sum_of_squares(num1, num2):

#     def square(num):
#         return num**2

#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

# - - - - - - - - - - - - - -
# 4. Write a function called increment_counter that 
# increments a counter variable every time it is called.
# You can test your code with the following:

# counter = 0

# def increment_counter():
#     global counter
#     counter += 1

# print(counter)                # 0

# increment_counter()
# print(counter)                # 1

# increment_counter()
# print(counter)                # 2

# counter = 100
# increment_counter()
# print(counter)                # 101

# - - - - - - - - - - - - - -
# 5. On reflection, we've decided that we don't 
# want to rely on using a global variable in the 
# code we wrote in the previous example. To fix 
# this, we're going to nest the code from the 
# previous example into an outer function:

# There's a bug in this code. Identify the bug, and fix it.

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()