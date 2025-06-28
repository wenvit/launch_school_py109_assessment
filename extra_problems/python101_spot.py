######### Type Coercions 

# Which variable is coerced? Is it implicit or explicit coercion?

# x = 3.5 
# y = 5
# z = x + y
# print(z)

# Solution:
# The integer `y` is coerced to a float, specifically from 5 to 5.0
# This is an example of implicit coercion because the program doesn't 
# give explicit instructions to convert the integer to float. 
# Python does the conversion because it numbers of two different 
# types can't be added. 

# - - - - - - - - - - - - - -
# What coercion is happening here? Is it implicit or explicit?

# a = 1
# b = 2
# print(a + b)

# Solution:
# This will print: 3. The mathematical expression `a + b` is evaluated
# to 3 (result of adding integers 1 + 2) before the result is passed
# as an argument to the `print` function. `print` converts its argument
# to strings behind the scenes for display purposes but it's not 
# considered coercion.

# - - - - - - - - - - - - - -
# What coercion is happening here? Is it implicit or explicit?

# month = "December"
# day = int(input("What day is it? "))
# print(f"Today is the {day} of {month}")

# This will print: Today is the 12 of December. The `int`
# function explicitly coerces the string value returned by `input`
# to an integer. As part of the f-string expression, the integer `day`
# is implicitly coerced to a string and embedded with the rest of the 
# string argument passed to the `print` function

########## Numbers and Exception Handling

# What does this return and why? What concept does this cover?

# def convert_to_int(string):
#     try:
#         converted_integer = int(string)
#         return converted_integer
#     except ValueError:
#         return "That string cannot be converted to an integer"

#print(convert_to_int("hello"))
# print(convert_to_int("5"))

# Solution:
# When the string 'hello' is passed to the `convert_to_int`
# function, this prints: That string cannot be converted to an integer.
# This is because in the `try` block, 'hello' is passed as an argument 
# to the `int` function, which returns a ValueError because it's the 
# correct data type but not a value that can be converted to an integer.
# When the ValueError is raised, the `except` block is executed.

# When the string '5' is passed to the function, it prints: 5.
# This is because the `try` block is successfully executed when 
# '5' is passed as an argument to the `int` function. The integer 5
# is returned and passed as an argument to `print`. The `except`
# block is ignored in this case.

# This code illustrates exception handling and type conversion.

# - - - - - - - - - - - - - -
# What does this return and why? What concept does this cover?

# def division(number1, number2):
#     numerator = number1
#     denominator = number2

#     try:
#         result = numerator / denominator
#         return result
#     except ZeroDivisionError:
#         return "The denominator cannot be zero"

# print(division(5, 0))

# Solution:

# This will print: The denominator cannot be zero.
# When the integers `5` and `0` are passed as arguments
# to `division`, these values are assigned to the parameters
# `number1` and `number2`, respectively. The local variables
# `numerator` and `denominator` are then initialized to `number1` 
# and `number2`. In the `try` block, when `numerator` is divided
# by `denominator` which is 0, it raises a `ZeroDivisionError`
# so `result` is not returned. Instead, the `except` block
# is executed which returns the string 'The denominator cannot
# be zero'
# This illustrates the concepts of exception handling, integer division, 
# division by zero

# - - - - - - - - - - - - - 
# What does this print and why, what concept does this demonstrate?

# def addition(number1, number2):
#     number1 += number2

# x = 1
# y = 2

# addition(x, y)
# print(f"x is {x}, y is {y}")

# This will print: x is 1, y is 2.
# `addition` is called passing `x` and `y` as arguments.
# The function is defined with parameters `number1` and 
# `number2`. Because these local variables reference immutable
# integers, when `number1` is reassigned to 3 by adding `number2`
# using augmented assignment, the value referenced by the global
# `x` variable is not affected. An f-string is passed to the `print`
# function where teh values of `x` and `y` are interpolated and
# embedded into the string.
# This illustrates concepts of variable scope and immutability of integers.

# - - - - - - - - - - - - - -

# What does this print and why? What concept does this cover? 
# How would you refactor this to remove the space?

# print(2 + 3 * 4, 4 * (3 + 2))

# Solution:
# This will print: 14 20
# To remove the space:
# print(2 + 3 * 4, 4 * (3 + 2), sep='')

# Arguments passed to the `print` function are separated by a comma, and
# by default they will be printed out with a space in between. In this case, 
# two separate mathematical expressions are passed to `print`. The first 
# expression `2 + 3 * 4` evaluates to 14 because the `*` operator takes 
# precedence over `+` so python sees this as 3 * 4, which is 12, plus 2. 
# The second expression evaluates to 20 because the subexpression within 
# parentheses is evaluated first `3 + 2`, then multiplied by 4. 
# This demonstrates order of operations, printing multiple arguments,
# the ability to pass evaluate a mathematical expression as an argument 
# to print 

# - - - - - - - - - - - - - -

# What can be used in place of commas to make this more readable?

# print(123112940)

# # Can use underscores:
# print(123_112_940)

# Both versions are integers

######### Strings

# What is the output of this code, and why? What is the concept covered here?

# str1 = "Hello, world!"  
# sub1 = str1[8:12]   # orld
# print(sub1)
# sub2 = str1[::-1]   # !dlrow ,olleH
# print(sub2)
# sub3 = str1[::2]    # Hlo ol!
# print(sub3)

# This will print:
# orld
# !dlrow ,olleH
# Hlo ol!
# `sub1` is initialized to a new string created from slicing `str1``
# starting at index 8 through index 12, not inclusive. No step is 
# specified so by default, every character is selected (step of 1).

# `sub2` is initialized to a new string created from slicing `str1`
# Start and stop indices are not specified, so the slice is made from the
# entirety of the string (start at index 0, stop at end of string). 
# The step is `-1` which means it goes through the string backward
# with a step of 1 starting at the end of the string. In other words,
# this creates a new string in reverse order of the original.

# `sub3` creates a new string from the entirety of the `str1` because
# start and stop indices are not specified (start at index 0, stop at end 
# of string). A step of 2 is specified, which means every other character
# is selected.

# This demonstrates using of slicing notation to create new strings from
# an existing string, index notation

# - - - - - - - - - - - - - -

# What does this print and why? What concept is this?

# print("Hello\nWorld")

# This prints:
# Hello
# World

# The escape character `\n` notation instructs python to interpret the `n`
# as a special newline character instead of as a literal string `'n'`.

# - - - - - - - - - - - - - -

# What does this print and why? What concept is this?

# name = 'Alexander Graham Bell'
# print(name[0])

# This prints: A
# The `name` variable is initialized to a string object. The indexing notation
# is used to access the character at index 0 of the string, which is the 
# first character because indexing starts at 0
# Concepts: text sequences can be indexed

#### f-strings

# What does this print and why, what is the concept?

# name = 'Abraham Lincoln'
# print(f"{name} was a President of the US")

# This will print: Abraham Lincoln was a President of the US
# The `f` notation with quote denotes an f-string. The value referenced
# by the `name` variable enclosed in {} is interpolated and combined with
# the rest of the text string.
# Concepts: f-string interpolation

#### String methods

# What does this print and why?

# mashup = "thIs is How we type careLEssly"
# cleaned = mashup.capitalize()
# print(cleaned)

# This will print: This is how we type carelessly
# The `mashup` variable is initialized to a string with a mix of
# lower & uppercase letters. The `capitalize` method is called on 
# `mashup`, which returns a new string with the first letter 
# capitalized and the remaining lowercase

# - - - - - - - - - - - - - -

# What do these print and why?

# stuff = 'tHIS iS bACKWARDS'
# str1 = stuff.swapcase()
# str2 = stuff.upper()
# str3 = stuff.lower()
# print(stuff)
# print(str1)
# print(str2)
# print(str3)

# This will print: 
# tHIS iS bACKWARDS
# This Is Backwards
# THIS IS BACKWARDS
# this is backwards

# The variable `stuff` is initialized to the string 'tHIS iS bACKWARDS'
# Appllying the `swapcase` method to `stuff` returns a new string with
# all lowercased letters uppercase and vice versa. The `upper` method
# returns a new string with lowercased letters uppercased. The `lower`
# method returns a new string with lowercased letters 

# - - - - - - - - - - - - - -

### 3. What do these print and why?

# s1 = "Hello"
# print(s1.isalpha())   # True, all alpha characters
# s2 = "Hello World"
# print(s2.isalpha())   # False, contains a space
# s3 = "Hello!"
# print(s3.isalpha())   # False, contains !
# s4 = "Hello123"
# print(s4.isalpha())   # False, contains digits
# s5 = ""
# print(s5.isalpha())   # False, empty string
# s6 = "こんにちは"
# print(s6.isalpha())   # True, all unicode alpha characters
# s7 = "HelloWorld"
# print(s7.isalpha())   # True, all alpha characters
# words = ["apple", "banana", "cherry"]
# print(all(word.isalpha() for word in words))   
# True, each word in words list contains all alpha characters
#    if all returns True if all True

### 4. What does this print and why?

# string1 = "HelloWorld"
# string2 = "12345"
# string3 = "Hello World"

# result1 = string1.isalpha()  # True
# result2 = string2.isalpha()  # False
# result3 = string3.isalpha()  # False

# print("Is '{}' alphabetic?".format(string1), result1)
# print("Is '{}' alphabetic?".format(string2), result2)
# print("Is '{}' alphabetic?".format(string3), result3)

# This will print:
# Is 'HelloWorld' alphabetic? True
# Is '12345' alphabetic? False
# Is 'Hello World' alphabetic? False

# These print calls use the older string interpolation syntax.
# The `print` function is called with two arguments.
# The first argument is an expression that invokes the format method on a string
#    object passing string1, string2, string3
#    as arguments which are interpolated in the {}. result1, result2, result3
#    are also passed as arguments to print which prints 

### 5. What do these print and why?

# s1 = "123abc"
# print(s1.isdigit())  # False, contains alpha characters
# s2 = "123$%^"
# print(s2.isdigit())  # False, contains non-digit characters
# s3 = ""
# print(s3.isdigit())  # False, empty string
# s4 = "12345"
# print(s4.isdigit())  # True, contains digits only

### 6. What do these print and why?

# print("Hello World".isalnum())  # False, contains space
# print("Hello@World".isalnum())  # False, contains @
# print("".isalnum())             # False, empty string
# print("Hello123".isalnum())     # True, only alpha and digits

### 7. What do these print and why?


# name = 'HELLO'

# if name.isupper():
#     print("WORLD")
# else:
#     print("world")

# This prints: WORLD
# calling `isupper` method on string 'HELLO' returns True
#    because all characters are upper case
# `if` block executes because expression evaluates as truthy

###  8. What do these print and why?

# def punctuation_type(str):
#     if str == str.upper():
#         print('This is all caps')
#     elif str == str.lower():
#         print('This is all lowercase')
#     else:
#         print('Neither')

# str1 = 'HELLO'
# str2 = 'yolo'
# str3 = 'My Name Is: '

# punctuation_type(str1)  # This is all caps
# punctuation_type(str2)  # This is all lowercase
# punctuation_type(str3)  # Neither

# Function `punctuation_type` defined with parameter `str`
# `if` str equals str with upper method called on it, print 
#      This is all caps
# `elif` str equals str with lower method called on it, print
#      This is all lowercase
# `else` print Neither


# ### 9. What do these print and why?

# str1 = "    "
# str2 = "  Hello   "
# str3 = "Hello World"

# print(str1.isspace())  # True, contains only spaces
# print(str2.isspace())  # False, contains alpha characters
# print(str3.isspace())  # False, contains alpha characters

# sentence = "Hello     World!   How are you?   "
# word_count = sum(1 for word in sentence.split() if not word.isspace())

# print("Number of words in the sentence:", word_count)

# This will print:  Number of words in the sentence: 5

# ### 10. What do these print and why?

# s = "   Hello, World!   "
# print(s.strip())   # Hello, World!
# print(s.strip(" !")) # Hello, World

# ### 11. What do these print and why?

# s = "www.example.com"
# print(s.lstrip('wcmo.'))  # example.com

# ### 12. What do these print and why?

# s = 'impatient'
# print(s.rstrip('tp'))  # impatien
# print(s.rstrip('p'))   # impatient

# ### 13. What do these print and why?

# s = "Hello, World!"
# print(s.replace("Hello", "Hi")) # Hi, World!
# print(s.replace("o", "0"))      # Hell0, W0rld!

# ### 14. What do these print and why?

# sentence = "This is a sample sentence."
# words = sentence.split()
# print(words) # ['This', 'is', 'a', 'sample', 'sentence.']

# csv_data = "John,Doe,30,New York"
# fields = csv_data.split(",")
# print(fields) # ['John', 'Doe', '30', 'New York']

# sentence = "This is a sample sentence."
# words = sentence.split(maxsplit=2)
# print(words)  # ['This', 'is' 'a sample sentence.']

# ### 15. What does this print and why?

# str1 = "hello world"
# str2 = str1.capitalize()
# print("Original string:", str1)  # Original string: hello world
# print("Capitalized string:", str2) # Capitalized string: Hello world

#### Truthy & Falsy

### 1. What do these print and why?

# truthy_values = [
#     1, 
#     2, 
#     3, 
#     "hello", 
#     [1, 2, 3], 
#     {"a": 1}, 
#     True, 
#     0, 
#     "", 
#     [],
#     {},
#     None, 
#     False,
# ]

# print("Values:")
# for value in truthy_values:
#     if value:
#         print(f"{value} is truthy")
#     else:
#         print(f"{value} is falsy")

# This prints:
# Values:
# 1 is truthy
# 2 is truthy
# 3 is truthy 
# hello is truthy
# [1, 2, 3] is truthy
# {"a": 1} is truthy
# True is truthy
# 0 is falsy 
#  is falsy
# [] is falsy
# {} is falsy
# None is falsy
# False is falsy

# ### 2. What do these print and why?

# x = 5
# y = 10
# z = 15

# print(x > 0 and y < 20) # True
# print(not x == y)       # True
# print(x < y and y < z)  # True
# print(x > y or y > z)   # False
# print(not (x > y))      # True


# ### 3. What do these print and why?

# a = 10
# b = 20

# print(a < b < 30)   # True
# print(a > b or b == 20) # True

# ### 4. What do these print and why?

# my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)  # True


# ### 5. What do these print and why?

# temperature = 25
# time_of_day = "morning"

# if temperature < 30 and (time_of_day == "morning" or time_of_day == "afternoon"):
#     print("It's a pleasant day!")
# else:
#     print("It's either too hot or not the right time of day.")

# This will print: It's a pleasant day!


# ### 6. What does this print and why?

# num = 12

# if num / 3 < 3 and num > 10:
#     print("Hello")
# elif num >= 8 and num < 6 or num > 4 and num < 16:
#     print("Hello 2")
# elif num % 4 == 0 or num < 7 and num < 10:
#     print("Hello 3")
# else:
#     print("Buy")

# This will print: Buy


# - - - - - - - - - - - - - -
# What happens when you run this code? What changes would you
# make to this code?

# lst = [1, 2, 3]

# def empty_list(lst):
#     for idx in range(len(lst)):  # 0, 1, 2
#         lst.pop(idx)             
#     return lst

# print(empty_list(lst))
# print(lst)

# Within `empty_list`, the `for` loop iterates over a range of integers
# from 0 to the length of `lst` (3):  0, 1, 2.
# Each iteration of the loop, the `pop` method is applied to `lst` and
# mutates `lst` by removing the element at index `idx`. First iteration,
# element at index 0, then element at index 1, then element at index 2. 
# However, at this point, there is no element at index 2, so the list 
# is not completely emptied. Here's the sequence:
# [1, 2, 3]  original `lst`
# [2, 3]     first iteration - remove index 0
# [2]        second iteratin - remove index 1
# IndexError        third iteration - error because there is no index 2

# When `empty_lst` is called, a reference to the global list object `lst`
# is passed. Within the function, the local variable `lst` points to the 
# same object as global `lst` variable. As the function mutates local `lst`
# by applying the `pop` method each iteration of the loop, the same object
# referenced by teh global variable `lst` is mutated. So the print call,
# prints out the mutated list

# How to fix:

# lst = [1, 2, 3]

# def empty_list(lst):
#     while lst:
#         lst.pop(0)

#     return lst

# print(empty_list(lst))
# print(lst)

# - - - - - - - - - - - - - - 

# print(1 or 2 and 3) #
# print(0 or 2 and 3) #
# print(1 or 0 and 3) # 
# print(1 or 2 and 0) # 
# print(0 or 0 and 3) # 
# print(0 or 2 and 0) # 
# print(1 or 0 and 0) # 
# print(0 or 0 and 0) #  

# print(1 and 2 or 3) # 
# print(0 and 2 or 3) # 
# print(1 and 0 or 3) # 
# print(1 and 2 or 0) # 
# print(0 and 0 or 3) # 
# print(0 and 2 or 0) # 
# print(1 and 0 or 0) # 
# print(0 and 0 or 0) #  