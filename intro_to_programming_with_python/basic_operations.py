# 1. Concatenate two strings, one with your first name and one with your last, 
# to create a new string with your full name as its value. For example, 
# if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.

# Solution:

#print('Wendy' + ' Vit')

# - - - - - - - - - - - - - -
# 2. This question may be a little challenging if your math skills are rusty. 
# Don't be afraid to take advantage of the hints. Try your best to solve the 
# problem, but don't feel compelled to complete it if you become frustrated.

# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.
# Each digit may require multiple Python statements.

# Solution:

# def floor_div10(num_in):
#     return num_in // 10

# def modulo10(num_in):
#     return num_in % 10

# number1 = 4936
# ones_place = modulo10(number1)

# number2 = floor_div10(number1)   # 493
# tens_place = modulo10(number2)

# number3 = floor_div10(number2)  # 49
# hundreds_place = modulo10(number3)

# thousands_place = floor_div10(number3)

# print(ones_place)
# print(tens_place)
# print(hundreds_place)
# print(thousands_place)

# - - - - - - - - - - - - - -
# 3. What does the following code do? Why?

#print('5' + '10')

# Solution:

# This will print:
# 510

# The quotes around 5 and 10 make these values strings, even though they are 
# digits. With string operands, the `+` operator concatenates strings and 
# returns a new string.

# - - - - - - - - - - - - - -
# 4. Refactor the code from the previous exercise to use coercion 
# to print 15 instead.

# Solution:

# print(int('5') + int('10'))

# - - - - - - - - - - - - - -
# 5. Will an error occur if you try to access a list element with 
# an index greater than or equal to the list's length? For example:

# foo = ['a', 'b', 'c']
# print(foo[3])      # will this result in an error?

# Solution:

# This will result in an IndexError because an index of 3 is beyond
# the range of valid index values for the `foo` list. Valid index
# values for would be 0, 1, 2 for a list of length 3 such as `foo`.

# - - - - - - - - - - - - - -
# 6. To what value does the following expression evaluate?

# print('foo' == 'Foo')
# print('foo' > 'Foo')
# print('foo'.casefold() == 'Foo'.casefold())

# Solution:
# This expression evalues to `False` because for string equality, every
# character from left to right in the string must be equal, including the case
# of the characters. To make this expression evaluate to `True`, you could 
# change `==` to `>` because lowercase 'f' is considered greater than 
# uppercase 'F' and all subsequent characters are the same. Use method
# `casefold` or `lower` to compare strings with all lowercase letters. 

# - - - - - - - - - - - - - -
# 7. What will the following code do? Why?

#int('3.1415')

# Solution
# This will raise a ValueError. This is because the argument '3.1415' 
# is the correct string data type to pass to the `int` function but 
# it's not an appropriate value to coerce to an integer because it 
# contains a decimal point. Can pass the string as argument to `float`
# function first, then pass return float value as argument to `int`, 
# which returns an integer (truncates the decimal portion).

# num_float = float('3.1415')
# print(num_float)
# num_int = int(num_float)
# print(num_int)

# - - - - - - - - - - - - - -
# 8. To what value does the following expression evaluate?

#print('12' < '9')

# Solution:
# This expression evaluates to `True`. The quotes make 12 and 9 strings.
# Python evaluates strings by comparing each character from left to right.
# The first digit '1' is considered less than '9'.