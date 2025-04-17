# What's My Value (Part 1)

# What will the following code do and why? 
# Don't run it until you have tried to answer.

# if True:
#     my_value = 20

# print(my_value)

# This will print: 20
# The variable `my_value` is initialized to the integer `20`
# within the `if` block. Variables initialized within `if` block
# are accessible outside the code block (global scope in this case). 
# `print` call has access to global variable `my_value`

# if False:
#     my_new_value = 42

# print(my_new_value)

# This raises a `NameError` because the `if` block is never executed
# because the condition is `False` so `my_new_value` is never 
# initialized

# - - - - - - - - - - - - - -
# What's My Value (Part 2)

# What will the following code do and why? Don't run it until 
# you have tried to answer.

# x = 10

# def my_function():
#     x = x + 5
#     print(x)

# my_function()

# This will raise an `UnboundLocalErro` because within the function body,
# python sees the assignment statement `x = x + 5` and interprets
# `x` as a local variable. On the right side of the assignment operator
# `=`, when it encounters the `x` it raises the error because it hasn't
# been initialized. This error could be resolved with the statement 
# `global x` above `x = x + 5`, which would print 15

# - - - - - - - - - - - - - -
# What's My Value (Part 3)

# What will the following code do and why? Don't run it until 
# you have tried to answer.

# def my_function():
#     a = 1

#     if True:
#         print(a)

# my_function()

# This will print: 1.
# Within the body of `my_function`, the local variable `a`
# is initialized to the integer `1`. The variable `a` can 
# be accessed within the `if` block, so passing `a` as an 
# argument to `print` outputs `1`

# - - - - - - - - - - - - - -
# What's My Value (Part 4)

# What will the following code do and why? Don't run it until 
# you have tried to answer.

# a = 1

# def my_function():
#     print(a)

# my_function()

# This will print: 1.
# A global variable `a` is initialized to the integer `1`. This
# global variable is accessible within the body of `my_function`
# so when `a` is passed as an argument to `print`, it prints `1`

# - - - - - - - - - - - - - -
# What's My Value (Part 5)

# What will the following code do and why? Don't run it until 
# you have tried to answer.

# a = 1

# def my_function():
#     print(a)
#     a = 2

# my_function()

# This raises an error.
# Within the body of `my_function`, when Python encounters an 
# assignment `a = 2`, it interprets `a` as a local variable. 
# However, the local variable `a` isn't initialized before passing
# it as an argument to `print`. If the statement `global a` is 
# inserted prior to the `print` call, it would print `1`, which
# is the value of the global variable `a`.

# - - - - - - - - - - - - - -
# What's My Value (Part 6)

# What will the following code do and why? Don't run it until 
# you have tried to answer.

# a = 1

# def my_function():
#     a = 2

# my_function()
# print(a)

# This will print: 1.
# A global variable `a` is initialized to the integer `1`.
# Within the body of `my_function`, a local variable `a` is 
# initialized to the integer `2`. The local `a` is a separate
# variable from the global `a`, an example of variable shadowing.
# Calling `my_function` has no affect on the global variable `a`.


# - - - - - - - - - - - - - -
# What's My Value (Part 7)

# What will the following code do and why? Don't run it until 
# you have tried to answer.

# a = 1

# def my_function():
#     global a
#     a = 2

# my_function()
# print(a)

# This prints: 2
# Within the body of `my_function`, the `global a` statement
# tells Python that the variable `a` is the global `a`. 
# The global variable `a` is initialized to the integer `1`.
# When `my_function` is called, the global `a` is reassigned to
# the integer `2`, which is passed as an argument to the `print` 
# function

# - - - - - - - - - - - - - -
# What's My Value (Part 8)

# What will the following code do and why? Don't run it until 
# you have tried to answer.

# print(greeting)

# greeting = 'Hello world!'

# this will raise a `NameError` because when `print` is called passing
# the the global variable `greeting` as an argument, `greeting` has not
# yet been initialized

# - - - - - - - - - - - - - -
# What's My Value (Part 9)

# a = 7

# def my_function(b):
#     b += 10

# my_function(a)
# print(a)

# This will print: 7
# The global variable `a` is initialized to the integer `7`.
# `my_function` is called passing the reference to the global `a`
# object. Within `my_function`, the local variable `b` points to 
# the same object refernced by the global `a`. Within the function, 
# `b` is reassigned to `17` using augmented assignment. Because
# integers are immutable, the reassignment of `b` does not impact
# the object referenced by the global variable `a`

# - - - - - - - - - - - - - -
# What's My Value (Part 10)

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# This will print: [10, 2, 3]
# The global variable `b` is initialized to the list object
# `[1, 2, 3]`. Within `my_function`, the list object referenced
# by `b` is mutated by reassigning the first list element 
# (referenced by index 0) to the integer `10`. When `my_function`
# is called, the list object referenced by `b` is mutated, then
# the mutated `b` is printed.