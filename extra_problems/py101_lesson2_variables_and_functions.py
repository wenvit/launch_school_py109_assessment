# Example 1

# my_var = 1

# def my_func():
#     print(my_var) 

# my_func()

# Solution:
# This will print: 1. The global `my_var` is initialized to the 
# integer 1 on line 3.  `my_var` is not initialized within `my_func`
# so python searches for the nearest definition in the outer scopes.
# The value referenced by the global `my_var` is passed to the 
# `print` function within `my_func`

# - - - - - - - - - - - 
# Example 2

# my_var = 1

# def my_func():
#     my_var = 2

# my_func()
# print(my_var) 


# Solution:
# This will print: 1. 
# A global variable `my_var` is initialized to the integer 1. 
# Within `my_func`, a variable `my_var` is initialized to the integer 2.
# A variable initialized inside a function is a local variable. This is 
# a separate variable from the global `my_var` even though it has the same
# name, which demonstrates variable shadowing. When `print` is invoked
# with `my_var` as an argument, it accesses the global `my_var` because 
# the local `my_var` is not available outside the function.
# This demonstrates the concepts of variable scope and variable shadowing.

# - - - - - - - - - - - - - -
#  Example 3

# my_var = [1]

# def my_func():
#     my_var[0] = 2

# my_func()
# print(my_var) 


# Solution:
# This will print: [2]
# The global variable my_var is initialized to a list object [1] on line 44. 
# The expression within my_func doesn’t initialize my_var (i.e., it doesn't
# create a local `my_var`), it reassigns the element at index 0 to the 
# integer 2, which is a mutating operation. Python performs this mutation 
# on the global my_var list. Calling my_func mutates the my_var list to [2], 
# and the global my_var is passed to print as an argument. 
# Mutating a global variable from within a function is an example of a function side effect.
# This demonstrates concepts of variable scope, lists as mutable objects, 
# and function side effects. 

# - - - - - - - - - - - - - -
# Example 4

# def my_func():
#     my_var = 1

# my_func()
# print(my_var)  

# Solution:
# This will raise a NameError stating that `my_var` hasn't been defined.
# Within `my_func`, a variable `my_var` is initialized to the integer 1, 
# which creates a local variable that's only accessible within the function.
# `my_func` is called but it only creates the local variable, so 
# when `print` is invoked on the next line passing `my_var` as an argument, 
# it raises the error
# This demonstrates concept of variable scope

# - - - - - - - - - - - - - -
# Example 5

# my_var = [1]

# def my_func(my_var):
#     my_var.append(2)

# my_func(my_var)  # [1, 2]
# print(my_var) 


# Solution:
# This will print: [1, 2]
# The global variable `my_var` is initialized on line 83 to a list object, [1].
# `my_func` is called with `my_var` as an argument. This passes the object 
# `my_var` by reference to to the function, meaning a reference to the global `my_var` object
# is passed. Within the function, the `append` method is applied to `my_var`
# which mutates the list by appending the integer 2. Because `my_var` is a reference
# to the global `my_var`, this mutation is done on the global my_var object. 
# When `print` is called with `my_var` as an argument, the global `my_var` which 
# has been mutated is printed. This is an example of a function side effect because the 
# function mutates a global variable.
# This demonstrates concepts of variable scope, pass by object reference, mutable variables, 
# and function side effects.

# - - - - - - - - - - - - - -
# Example 6

# my_var = [1]

# def my_func(my_var): 
#     my_var = [2] 

# my_func(my_var)
# print(my_var)  


# Solution:
# This will print: [1]
# The global `my_var` variable is initialized to a list object, `[1]`.
# When `my_func` is called on line 110, it passes the global object `my_var` by 
# reference to the function. The function is defined with a parameter `my_var`,
# which is a local variable separate from the global `my_var`, even though they have the 
# same name (example of variable shadowing). Within the function, the local `my_var`
# is reassigned to a new list object, `[2]`. This doesn't affect the global `my_var`.
# When `print` is called, it prints the global `my_var`
# This demonstrates concepts of variable scope, pass by object reference, variable shadowing

# - - - - - - - - - - - - - -
# Example 7

# my_var = "Hello"

# def my_func():
#     print(my_var + " world")  

# my_func()

# Solution:
# This will print: Hello world
# The global variable `my_var` is initialized to the string 'Hello'. A global variable is
# accessible everywhere within the program, including within functions.
# When `my_func` is called within the body of the function, the `print` function
# accesses the global variable `my_var` and concatenates the string ' world'

# - - - - - - - - - - - - - -
# Example 8

# my_var = "Hello"

# def my_func():
#     return my_var + " world"

# my_func()
# print(my_var)


# Solution:
# This will print: Hello.
# Global variable `my_var` is initialized to the string 'Hello' on line 147. When `my_func`
# is called on line 152, it returns the concatenation of global `my_var` and ' world'.
# However, the return value isn't captured in a variable, and `my_var` is not modified because
# strings are immutable. `print` accesses the global `my_var` which is unchanged by 
# the call to `my_func`

# - - - - - - - - - - - - - -
# Example 9

# my_var = "Hello"

# def my_func():
#     my_var = my_var + " world"
#     return my_var

# my_func()
# print(my_var)

# Solution:
# This will raise an UnboundLocalError because Python sees the assignment
# of `my_var` within body of function and interprets it as a local variable.
# The expression on the right side of the `=` raises error because `my_var`
# hasn't been initialized locally yet. 


