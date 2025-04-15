# 1. What happens when you run the following program?
#    Why do we get that result?

# def set_foo():
#     foo = 'bar'

# set_foo()
# print(foo)

# Solution:

# This code will raise a `NameError` when `print` is invoked on line 8 
# with `foo` as an argument. This is because the variable `foo`
# is not accessible in the global scope outside the `set_foo` function.
# Because `foo` is initialized within the `set_foo` function, 
# it's a local variable that's only available within the scope 
# of the function. Modifying the code by adding the line `global foo` 
# within the body of `set_foo` would allow `foo` to be accessed 
# outside of the scope of the function.

# - - - - - - - - - - - - - -
# 2. Take a look at this code snippet. What does this program print? Why?

# foo = 'bar'

# def set_foo():
#     foo = 'qux'

# set_foo()
# print(foo)

# Solution:

# This will print: bar. This is because the global variable `foo` is accessed
# when `foo` is passed as an argument to `print` on line 30.
#  `foo` is initialized to 'bar' in the global scope on line 24. 
# Within the `set_foo` function, a variable `foo` is assigned to `qux`. This is 
# initialization of a separate, local variable `foo` because 
# because global variables cannot be reassigned within a function without
# the `global` keyword. The local variable `foo` shadows (supersedes)
# the global `foo` within the body of the function, but isn't available 
# outside the function where print is called. If the intent of the code is to
# print qux, this could be accomplished by inserting `global foo` in the 
# above the initialization of `foo` within the function.

# - - - - - - - - - - - - - -
# 3. Write a program that uses a multiply function to multiply two 
# numbers and returns the result. Ask the user to enter the two numbers, 
# then output the numbers and result as a simple equation.

# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

# Solution:

# def multiply(left, right):
#     return left * right

# number1 = float(input('Enter the first number: '))
# number2 = float(input('Enter the second number: '))

# product = multiply(number1, number2)

# print(f'{number1} * {number2} = {number1 * number2}')
# print(number1)
# print(left)

# To describe what's happening here: when function `multiply` is 
# called, global variables `number1` and `number2` are passed as arguments
# to the `multiply` function. The multiply function is defined with two 
# parameters `left` and `right`, which are local variables. The arguments
# are passed by object reference to the function, meaning the local 
# variables `left` and `right` point to the same objects referenced by
# `number1` and `number2` when the function is called.

# - - - - - - - - - - - - - -
# 4. Consider this code:

# def multiply_numbers(num1, num2, num3):
#     result = num1 * num2 * num3
#     return result

# product = multiply_numbers(2, 3, 4)

# Identify the following items in that code:
# function name                  multiply_numbers
# function arguments             2, 3, 4
# function definition            lines 79-81 (from def to return)
# function body                  lines 80-81
# function parameters            num1, num2, num3
# function invocation            multiply_numbers() on line 83
# function return value          variable `result` which is 24 in this example
# all identifiers                multiply_numbers, num1, num2, num3, result, product

# - - - - - - - - - - - - - -
# 5. What does the following code print?

# def scream(words):
#     return words + '!!!!'

# scream('Yipeee')

# Solution:

# This code doesn't print anything. The function `scream` is defined
# with parameter `words` and returns concatenation of `words` and '!!!!'
# The function `scream` is invoked on line 102 with the argument 'Yipeee'.
# The return value from the function is not captured in a variable and is
# not passed to the `print` function

# - - - - - - - - - - - - - -
# 6. What does the following code print?

# def scream(words):
#     words = words + '!!!!'
#     return
#     print(words)

# scream('Yipeee')

# Solution:

# This will print nothing. The function `scream` is defined with a parameter
# words. Within the function on line 115, `words` is reassigned to the 
# concatenation of words and '!!!!'. The `return` keyword on line 116, 
# terminates the function and returns execution of the program to the 
# point where the function is called, line `119`. The `print` call on 
# line 117 is never executed.

# - - - - - - - - - - - - - -
 # 7. Without running the following code, what do you think it will do?

# def foo(bar, qux):
#     print(bar)
#     print(qux)

# foo('Hello')

# Solution:

# This code will raise a TypeError that `foo` function expects 2 arguments
# but only one given. `foo` is defined on lines 114-116 with 
# 2 parameters `bar` and `qux`. `foo` is invoked on line 118 with only 
# a single argument (the string 'Hello'). Unless default parameters are
# specified, a function must be invoked with the same number of arguments as
# the number of parameters in the function definition.

# - - - - - - - - - - - - - -
# 8. Without running the following code, what do you think it will do?

# def foo(bar, qux):
#     print(bar)
#     print(qux)

# foo(42, 3.141592, 2.718)

# Solution:

# This code will raise a TypeError because the function is defined
# with two parameters on line 150, but the function is invoked
# with three arguments on line 154. Unless default parameters are
# specified, a function must be invoked with the same number of arguments as
# the number of parameters in the function definition.

# - - - - - - - - - - - - - -
# 9. Without running the following code, what do you think it will do?

# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42, 3.141592, 2.718)

# Solution:

# This code will print: 
# 42
# 3.141592
# 2.718
# The function `foo` is defined with 3 parameters on line 167,
# and the function is invoked with 3 arguments on line 172.
# Although the function is defined with default values for the 
# 2nd and 3rd parameters, the defaults are ignored because the
# 2nd and 3rd arguments in the function call supersede the defaults.
# The arguments are assigned to the positional parameters in 
# the order they are listed when the function is invoked, with the
# first parameter assigned to the first argument, second parameter
# assigned to the second argument, and third parameter to third 
# argument. 

# - - - - - - - - - - - - - -
# 10. Without running the following code, what do you think it will do?
# 
# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42, 3.141592)

# Solution:

# This will print:
# 42
# 3.141592
# 2
# The function `foo` is defined with 3 parameters, and the `second` and `third` 
# parameters have default values. When the function is invoked on line 197, the 
# arguments 42 and 3.141592 are passed positionally to the `first` and `second` 
# parameters (`first` assigned to 42 and `second` assigned to 3.141592). The 
# default value for the `second` parameter is ignored because it's superseded 
# by the argument 3.141592. Because no argument is passed to the `third` 
# parameter, it is assigned to the default value of 2.

# - - - - - - - - - - - - - -
# 11. Without running the following code, what do you think it will do?

# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42)

# This will priint:
# 42
# 3
# 2

# Solution:

# The function `foo` is defined on line 214 with three parameters `first`,
# `second`, `third`. The `second` and `third` parameters have default values.
# When `foo` is called on line 219, a single argument of 42 is passed positionally
# to the `first` parameter. The `second` and `third`
# parameters are assigned their default values.

# - - - - - - - - - - - - - -
# 12. Without running the following code, what do you think it will do?

# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo()

# Solution:

# This will raise a TypeError. The function `foo` definition includes
# three parameters, with the `second` and `third` parameters having default
# values. The `first` parameter doesn't have a default, so the function
# expects a minimum of a single argument. `foo` is called on line 240 without
# any arguments, so it raises the error

# - - - - - - - - - - - - - -
# 13. Without running the following code, what do you think it will do?

# def foo(first, second=3, third):
#     print(first)
#     print(second)
#     print(third)

# foo(42)

# Solution:

# This will raise a SyntaxError. With positional parameters in a function definition,
# a parameter can't have a default value followed by parameters without default values. 
# Parameters with default values should always be at the end of a list of positional
# parameters.

# - - - - - - - - - - - - - -
# 14. Identify all of the identifiers on each line of the following code.

# def multiply(left, right):   
#     return left * right      

# def get_num(prompt):         
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')

# Solution:

# 266: multiply (function name), left & right (parameter names)
# 267: left & right (parameters)
# 269: get_num (function name), prompt (parameter)
# 270: float & input (built in function names), prompt (argument)
# 272: first_number (variable), get_num (function name)
# 273: second_number (variable), get_num (function name)
# 274: product (variable), multiply (function name),
#      first_number & second_number (arguments)
# 275: print (built in function), first_number, second_number, product (variables)

# - - - - - - - - - - - - - -
# 15. Using the code below, classify the identifiers as global, local, or built-in.

# def multiply(left, right):
#     return left * right

# def get_num(prompt):
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')

# Solution:

# global: 
# multiply, get_num - function names
# first_number, second_number, product - variable names
# 
# local: 
# left, right, prompt - parameter names
# 
# built in: 
# float, input, print - function names
# 
#  - - - - - - - - - - - - - 
# 16. In the code shown below, identify all of the function names 
# and parameters present in the code. Include the line numbers 
# for each item identified.

# def multiply(left, right):
#     return left * right

# def get_num(prompt):
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')

# Solution:

# function names: 
# multiply, lines 316 (definition) also 324 (call)
# get_num, line 319 (definition) also 322 & 323 (call)
# float & input, line 320
# print, line 325

# parameter names:
# left & right, line 316 (definition) & 317
# prompt, lines 319 (definition) & 320 (argument)
# - - - - - - - - - - - - - -

# 17. Which of the identifiers in the following program 
# are function names? Which are method names? Which are 
# built-in functions?

# def say(message):
#     print(f'==> {message}')

# string1 = input()
# string2 = input()

# say(max(string1.upper(), string2.lower()))

# Solution:

# function names: say

# method names: upper, lower

# built-in functions: input, print, max

# - - - - - - - - - - - - - -
# 18. The following function returns a list of the remainders of dividing
# the numbers in numbers by 3:

# def remainders_3(numbers):
#     return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains 
# at least one number that is not evenly divisible by 3 (that is, the 
# remainder is not 0):

# numbers_1 = [0, 1, 2, 3, 4, 5, 6]
# numbers_2 = [1, 2, 4, 5]
# numbers_3 = [0, 3, 6]
# numbers_4 = []

# Solution:

# A number is divisible by 3 if number % 3 == 0, which is falsy
# A number is not divisible by 3 if number % 3 > 0, which is truthy
# So can use `any` to determine if aat least one number is not 
# divisible by 3. `any` will return True if at least one element is
# truthy

# print(any(remainders_3(numbers_1)))
# print(any(remainders_3(numbers_2)))
# print(any(remainders_3(numbers_3)))
# print(any(remainders_3(numbers_4)))

# - - - - - - - - - - - - - -
# 19. The following function returns a list of the remainders 
# of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following 
# lists do not contain any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # False
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]            # True
numbers_3 = [0, 5, 10]                          # False
numbers_4 = []                                  # True

# Solution:

# True ==> does not contain number divisible by 5 (number % 5 == 0)
# A number is not divisible by 5 if number % 5 > 0
# Using `all` function will return True if all elements are truthy
# None of the elements are 0 

print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))