# 1.  ​Basic​: What will the following code output? Explain why.

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# This will print:  [1, 2, 3, 4]
# `a` is initialized to list `[1, 2, 3]`. `b` is assigned
# to `a`, which means both `b` and `a` point to the same list
# object in memory. The `append` method is applied to `b` which
# mutates `b` by adding the integer `4` to the list. Because `a` and `b`
# reference the same object, the changes to `b` are seen when 
# `a` is printed.
# This demonstrates concepts of mutability of lists and variables as
# pointers.

# 2. ​Intermediate​: Describe the difference between mutable and 
# immutable objects in Python. Provide examples of each type.

# Mutable objects can be modified, meaning an object in 
# memory can be mutated while the object's identity (its memory address) 
# remains the same. Examples of mutable objects: lists, 
# dictionaries, sets.
# Immutable objects cannot be mutated/modified. To change the value 
# of an immutable object, it must be reassigned to a different object 
# in memory. The original object remains unchanged in memory. 
# Examples of immutable objects:  strings, integers, floats, 
# tuples, ranges, and frozensets. 

# 3.  ​Basic​: What will be the output of the following code? 
# Explain your reasoning.

# def change_value(val):
#     val = 5
   
# num = 10
# change_value(num)
# print(num)

# This will print: 10
# The global variable `num` is initialized to the integer 10.
# `change_value` is called passing `num` as an argument, which
# passes a reference to the global `num` object. `change_value`
# is defined with the parameter `val`. Within the body of the 
# function, the local variable `val` is reassigned to the integer 5.
# Since `val` is a local variable separate from any global variables,
# the global `num` is unchanged. When `print` is called, it prints
# the global `num`.
# This demonstrates concepts of variable scope 

# - - - - - - - - - - - - - -

# def change_list(lst):
#     lst = [4, 5, 6]  

# my_list = [1, 2, 3]
# change_list(my_list)
# print(my_list)


# This will print: 
# Inside function: [4, 5, 6]
# Outside function: [1, 2, 3]
# `change_list` function is defined with parameter `lst`. When `change_list`
# is called passing a reference to `my_list` object, the local variable
# `lst` points to same object as `my_list`. Within the function, local
# `lst` reassigned to object `[4, 5, 6]`. This reassignment doesn't 
# affect global object because global variables cannot be reassigned within 
# function.

# <<<<< run this solution through lsbot sometime >>>>>>

# - - - - - - - - - - - - - -
#4.  ​Intermediate​: Analyze this code and explain what it outputs and why:

# numbers = [1, 2, 3, 4, 5]
# result = 0
   
# for num in numbers:
#     if num % 2 == 0:
#         continue
#     result += num 
       
# print(result)

# This prints: 9 
# This code snippet calculates the sum of all of the odd integers
# in the `numbers` list. The `for` loop iterates over each `num` 
# integer within the `numbers` list. The `if` statement has a 
# conditional expression `num % 2 == 0` which returns `True`
# when `num` divided by `2` has a remainder of `0`.
# If the conditional expression is `True`, the `continue` keyword 
# jumps to the next iteration of the `for` loop. Otherwise, `result`
# is reassigned with the augmented assignment operator `+=`. 

# - - - - - - - - - - - - - -
# 5. ​Intermediate​: What is the difference between == and is in Python? 
# When would you use each one?

# The equality operator `==` evaluates value equality. It returns
# `True` when two objects have the same value. The `is` operator 
# evaluates object equality. For value equality, objects must be the
# same data type and have same elements. `is` will return `True` when an object
# has the same identity as another object (i.e., they are the same
# objects in memory). 
# A typical use case for `==` is in `if` statement to execute a block
# of code if two objects are equal in value.
# A use case for `is` is to check if two different variables 
# have the same object identity, i.e., reference the same 
# object in memory.

# - - - - - - - - - - - - - -
# 6. skip ==> *args & **kwargs not necessary for Py109

# - - - - - - - - - - - - - -
# 7. What will the following code output? Explain your answer.


# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#     inner()
#     return x

# print(outer())

# This will print: nonlocal
# Within the `outer` function, the variable `x` is initialized
# to the string 'local'. Within the nested function `inner`,
# the `nonlocal x` statement tells Python that the `x` within 
# the body of `inner` is in the nonlocal scope (outside the scope 
# of `inner`). The statement `x = 'nonlocal'` reassigns the nonlocal
#  `x` variable to 'nonlocal'. 


# - - - - - - - - - - - - - -
# 8. What will the output of this code be? Explain why.   
# 
# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4:2])

# This will print: [2, 4]
# The slicing notation creates a new list object starting with index 1 and
# stopping with index 4 (not inclusive), with a step of 2 (include every other
# element). 

# - - - - - - - - - - - - - -
# 9.  Explain what this code is doing and what the final 
# result will be:

data = {'a': 1, 'b': 2}
try:
    print(data['c'])
except KeyError:
    print("Key not found")
finally:
    print("Done")

# This will print:
# Key not found
# Done
# The `try` block includes code that Python monitors for exceptions. In
# this case, attempting to access the key `c` within the dictionary `data`
# raises a `KeyError` because the `data` dictionary doesn't contain the key 
# `c`. So the `except KeyError` block executes, printing Key not found.
# The `finally` block in Python always executes regardless of whether an 
# exception is raised so 'Done' is printed.

# - - - - - - - - - - - - - -
# 10. What will be the output of the following code? Explain why.

# numbers = [1, 2, 3, 4]
# squared = [num ** 2 for num in numbers if num % 2 == 0]
# print(squared)

# This will print:
# [4, 16]

# - - - - - - - - - - - - - -
# 11. Basic: Write a function that accepts a string and 
# returns a boolean indicating whether the string is a 
# palindrome (reads the same forward and backward, ignoring
# spaces, punctuation, and case).

# def is_palindrome(text):
    
#     if not text:
#         return False
    
#     text_lst = [ 
#         char.lower()
#         for char in text
#         if char.isalpha()
#     ]

#     if not text_lst:
#         return False

#     text_clean = ''.join(text_lst)
#     text_clean_reverse = text_clean[::-1]

#     return text_clean == text_clean_reverse

# print(is_palindrome('red Rum, Sir, is murder'))
# print(is_palindrome('TACO cat'))
# print(is_palindrome('no lemon, no melon'))
# print(is_palindrome('Eva, can I see bees in a cave?'))
# print(is_palindrome('Was   it a CAT I saw?'))
# print(is_palindrome('12345'))
# print(is_palindrome('        '))
# print(is_palindrome(''))

# - - - - - - - - - - - - - -
# 12. 2.  ​Intermediate​: Create a function that takes 
# a list of integers and returns a new list containing 
# only the prime numbers from the original list.

# Prime numbers are positive integers >= 2 divisible only 
# by 1 and itsel. So check to see if number is divisible 
# by any of range of numbers between 2 and one less than number 
# create list of True or False if number 

# def is_prime(num):

#     div_check = [
#         num % n == 0
#         for n in range(2, num)
#     ]
#     return not any(div_check)

# def list_of_primes(lst):

#     primes = [
#         num 
#         for num in lst
#         if is_prime(num)
#     ]
#     return primes

# print(list_of_primes([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(list_of_primes([10, 100, 1001, 10003]))

# - - - - - - - - - - - - - -
# Basic: Write a function named filter_by_value 
# that takes a dictionary and a value as arguments. 
# The function should return a new dictionary that 
# only contains the key-value pairs where the value 
# is equal to the given value.

# def filter_by_value(dict_param, val_param):

#     new_dict = {}
#     for key, val in dict_param.items():
#         if val == val_param:
#             new_dict[key] = val
#     return new_dict

# Another way using dict comprehension

# def filter_by_value(dict_param, val_param):
    
#     new_dict = {
#         key: val
#         for key, val in dict_param.items()
#         if val == val_param

#     }

#     return new_dict

# test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}

# print(filter_by_value(test_dict, 1))
# print(filter_by_value(test_dict, 4))
# print(filter_by_value(test_dict, 5))
# print(filter_by_value(test_dict, 3))
# print(filter_by_value(test_dict, 1) == {'a': 1, 'c': 1})
# print(filter_by_value(test_dict, 4) == {})
# print(filter_by_value({}, 5) == {})

# - - - - - - - - - - -
# def modify_dict(d):
#     d['c'] = 3
#     print(id(d))
#     d = {'x': 10, 'y': 20}
#     print(id(d))
#     return d
   
# my_dict = {'a': 1, 'b': 2}
# result = modify_dict(my_dict)
# print(my_dict)
# print(id(my_dict))
# print(result)
# print(id(result))

# # - - - - - - - - - - - -
# def modify_nested(data):
#     data[1][0] = 'changed'
#     return data
   
# original = [1, ['a', 'b'], 3]
# modified = modify_nested(original)
# print(original)
# print(id(original))
# print(id(modified))