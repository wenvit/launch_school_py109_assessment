# 1. To what values do the following expressions evaluate?

# `and` short circuits when left operand is falsy
# `or` short circuits when left operand is truthy

False or (True and False)   # False
True or (1 + 2)             # True
(1 + 2) or True             # 3
True and (1 + 2)            # 3
False and (1 + 2)           # False
(1 + 2) and True            # True
(32 * 4) >= 129             # False
False != (not True)         # False
True == 4                   # False
False == (847 == '847')     # True

# - - - - - - - - - - - - - -
# 2. Write a function, even_or_odd, that determines 
# whether its argument is an even or odd number. 
# If it's even, the function should print 'even'; 
# otherwise, it should print 'odd'. Assume the 
# argument is always an integer.

# Solution:

# def even_or_odd(number):
#     print('even' if number % 2 == 0 else 'odd')

# even_or_odd(10)
# even_or_odd(-10)
# even_or_odd(3)
# even_or_odd(0)

# - - - - - - - - - - - - - -
# 3. Without running the following code, what does it print? Why?

# def bar_code_scanner(serial):
#     match serial:
#         case '123':
#             print('Product1')
#         case '113':
#             print('Product2')
#         case '142':
#             print('Product3')
#         case _:
#             print('Product not found!')

# bar_code_scanner('113')
# bar_code_scanner(142)

# Solution:
# This code will print:
# Product2
# Product not found!

# When `bar_code_scanner` is called passing the string '113' 
# as an argument, Python searches for a value equivalent to '113'
# in the `match/case` statement. The `case 113:` block executes 
# printing Product2. In the next `bar_code_scanner` call, the 
# integer 142 is passed as an argument. Python doesn't find an equivalent
# value in the `match/case` statement. The string '142' is not equivalent
# to the integer 142 because they are different data types. The 
# default `case _:` block is executed.

# - - - - - - - - - - - - - -
# 4. Refactor this statement to use a regular if statement instead.

# return ('bar' if foo() else qux())

# # Solution:
# if foo():
#     return 'bar'
# else:
#     return qux()

# - - - - - - - - - - - - - -
# 5. What does this code output, and why?

# def is_list_empty(my_list):
#     if my_list:
#         print('Not Empty')
#     else:
#         print('Empty')

# is_list_empty([])

# This will print: Empty
# `is_list_empty` is called on line 85 passing an empty list `[]`
# as an argument. An empty list is falsy, so the `else` block within
# the function executes. The `if` block would execute if `my_list`
# were truthy (contains at least one element).

# - - - - - - - - - - - - - -
# 6. Write a function that takes a string as an argument and returns 
# an all-caps version of the string when the string is longer than 
# 10 characters. Otherwise, it should return the original string. 

# Example: change 'hello world' to 'HELLO WORLD', but don't change 
# 'goodbye'.

# Solution:

# def long_string_caps(text):
#     if len(text) > 10:
#         return text.upper()
#     return text

# print(long_string_caps('hello world'))
# print(long_string_caps('goodbye'))
# print(long_string_caps('check12345'))
# print(long_string_caps('check123456'))
# print(repr(long_string_caps('')))

# - - - - - - - - - - - - - -
# 7. Write a function that takes a single integer 
# argument and prints a message that describes whether:

# the value is greater than 100
# the value is between 51 and 100 (inclusive)
# the value is between 0 and 50 (inclusive)
# the value is less than 0

# Solution:

def number_range(number):
    if number > 100:
        print(f'{number} is greater than 100')
    elif number >= 51:
        print(f'{number} is between 51 and 100')
    elif number >= 0:
        print(f'{number} is between 0 and 50')
    else:
        print(f'{number} is less than 0')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0