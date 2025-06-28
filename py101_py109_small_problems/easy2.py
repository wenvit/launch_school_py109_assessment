# Welcome Stranger
# Create a function that takes 2 arguments, a list and a dictionary. 
# The list will contain 2 or more elements that, when joined with 
# spaces, will produce a person's name. The dictionary will contain 
# two keys, "title" and "occupation", and the appropriate values. 
# Your function should return a greeting that uses the person's full 
# name, and mentions the person's title.

# def greetings(name_list, title_dict):
#     name = ' '.join(name_list)
#     title = title_dict['title'] + ' ' + title_dict['occupation']
#     return f'Hello, {name}! Nice to have a {title} around.'
    
# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

# - - - - - - - - - - - - - -
# Greeting a user
# Write a program that asks for user's name, then greets the user. 
# If the user appends a ! to their name, the computer will yell 
# the greeting (print it using all uppercase).

# Test cases:

# What is your name? Sue
# Hello Sue.

# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

# def greeting(name):
#     if name.endswith('!'):
#         return f'HELLO {name.upper()} WHY ARE WE YELLING?'
#     return f'Hello {name}.'

# user_name = input('What is your name? ')
# print(greeting(user_name))

# - - - - - - - - - - - - - -
# Multiplying Two Numbers
# Create a function that takes two arguments, multiplies them together, 
# and returns the result.

# def multiply(num1, num2):
#     return num1 * num2

# print(multiply(5, 3) == 15)  # True

# - - - - - - - - - - - - - -

# Squaring an Argument
# Using the multiply function from the "Multiplying Two Numbers" exercise, 
# write a function that computes the square of its argument (the square 
# is the result of multiplying a number by itself).

# def square(num):
#     return multiply(num, num)


# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# - - - - - - - - - - - - - -
# Floating Point Arithmetic
# Write a program that prompts the user for two positive numbers 
# (floating-point), then prints the results of the following 
# operations on those two numbers: addition, subtraction, 
# product, quotient, floor quotient, remainder, and power. 
# Do not worry about validating the input.

# def calculate(flt1, flt2, operator):
#     match operator:
#         case '+':
#             return flt1 + flt2
#         case '-':
#             return flt1 - flt2
#         case '*':
#             return flt1 * flt2
#         case '/':
#             return flt1 / flt2
#         case '//':
#             return flt1 // flt2
#         case '%':
#             return flt1 % flt2
#         case '**':
#             return flt1**flt2

# prompt = '==>'

# flt1 = float(input(f'{prompt} Enter the first number:\n'))
# flt2 = float(input(f'{prompt} Enter the second number:\n'))

# print(f'{prompt} {flt1} + {flt2} = {calculate(flt1, flt2, '+')}')
# print(f'{prompt} {flt1} - {flt2} = {calculate(flt1, flt2, '-')}')
# print(f'{prompt} {flt1} * {flt2} = {calculate(flt1, flt2, '*')}')
# print(f'{prompt} {flt1} / {flt2} = {calculate(flt1, flt2, '/')}')
# print(f'{prompt} {flt1} // {flt2} = {calculate(flt1, flt2, '//')}')
# print(f'{prompt} {flt1} % {flt2} = {calculate(flt1, flt2, '%')}')
# print(f'{prompt} {flt1} ** {flt2} = {calculate(flt1, flt2, '**')}')

# - - - - - - - - - - - - - -
# The End Is Near But Not Here
# Write a function that returns the next to last word in the string 
# argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at 
# least two words.

# def penultimate(text):
#     words = text.split()
#     return words[-2]

# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# - - - - - - - - - - - - - -
# Exclusive Or
# The or operator returns a truthy value if either or both 
# of its operands are truthy, a falsy value if both operands 
# are falsy. The and operator returns a truthy value if both 
# of its operands are truthy, and a falsy value if either
# operand is falsy. This works great until you need only 
# one of two conditions to be truthy, the so-called exclusive 
# or, also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function that 
# takes two arguments, and returns True if exactly one 
# of its arguments is truthy, False otherwise.

# and --> truthy if both truthy, falsy otherwise
# or --> truthy if one or both truthy, falsy otherwise
# xor --> truthy if only one truthy

# def xor(arg1, arg2):
#     list_of_bools = [bool(arg1), bool(arg2)]
#     return list_of_bools.count(True) == 1

# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# - - - - - - - - - - - - - -
# Odd Lists
# Write a function that returns a list that contains every other 
# element of a list that is passed in as an argument. The values 
# in the returned list should be those values that are in the 1st, 
# 3rd, 5th, and so on elements of the argument list.

# input list
# return list consisting of every other element starting with first
# element at index 0 and then even numbered indices thereafter

# first way

# def oddities(input_lst):
#     idx = 0
#     output_lst = []
#     while idx <= len(input_lst) - 1:
#         if idx % 2 == 0:
#             output_lst.append(input_lst[idx])
#         idx += 1
#     return output_lst

# second way
# def oddities(input_lst):
#     output_lst = []

#     for idx in range(len(input_lst)):
#         if idx % 2 == 0:
#             output_lst.append(input_lst[idx])
#     return output_lst

# third way

# def oddities(input_lst):
#     return input_lst[::2]


# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True


# - - - - - - - - - - - - - -
# How Old is Teddy?

#Build a program that randomly generates and prints Teddy's age. 
# To get the age, you should generate a random number between 20 
# and 100, inclusive.

# import random

# age = random.randint(20, 100)

# print(f'Teddy is {age} years old!')

# Teddy is 69 years old!

# - - - - - - - - - - - - - -
# When Will I Retire?
# Build a program that displays when the user will retire 
# and how many years she has to work till retirement.

# Example output

# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

# from datetime import datetime

# age = int(input('What is your age? '))
# retirement_age = int(input('At what age would you like to retire? '))

# year = datetime.now().year
# work_years_remaining = retirement_age - age
# retirement_year = year + work_years_remaining

# print(f"It's {year}. You will retire in {retirement_year}.")
# print(f'You only have {work_years_remaining} years of work to go!')

# - - - - - - - - - - - - - -
# Get Middle Character
# Write a function that takes a non-empty string argument 
# and returns the middle character(s) of the string. If 
# the string has an odd length, you should return exactly one character. 
# If the string has an even length, you should return exactly two characters.

# def center_of(text):
#     idx = len(text) // 2

#     if len(text) % 2 == 0:
#         return text[idx-1:idx+1]
#     return text[idx]

# another way

# def center_of(text):
#     idx = len(text) // 2

#     return text[idx-1:idx+1] if len(text) % 2 == 0 else text[idx]


# ExampleS
# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True


# - - - - - - - - - - - - - -
# Always Return Negative
# Write a function that takes a number as an argument. If the argument 
# is a positive number, return the negative of that number. 
# If the argument is a negative number, return it as-is.

# def negative(num):
#     return num if num < 0 else (-num)

# print(negative(5) == -5)      # True
# print(negative(-3) == -3)     # True
# print(negative(0) == 0)       # True
# - - - - - - - - - - - - - -