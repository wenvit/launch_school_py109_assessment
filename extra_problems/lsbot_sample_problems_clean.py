# 1.  ​Basic​: What will the following code output? Explain why.

# a = [1, 2, 3]
# b = a 
# b.append(4) 
# print(a) 

# 2. ​Intermediate​: Describe the difference between mutable and 
# immutable objects in Python. Provide examples of each type.


# 3.  ​Basic​: What will be the output of the following code? 
# Explain your reasoning.

# def change_value(val): 
#     val = 5 
   
# num = 10
# change_value(num)
# print(num) 



# - - - - - - - - - - - - - -

# def change_list(lst): 
#     lst = [4, 5, 6]  

# my_list = [1, 2, 3]
# change_list(my_list)
# print(my_list) 

# - - - - - - - - - - - - - -
#4.  ​Intermediate​: Analyze this code and explain what it outputs and why:

# numbers = [1, 2, 3, 4, 5]
# result = 0
   
# for num in numbers:
#     if num % 2 == 0:
#         continue
#     result += num 
       
# print(result)


# - - - - - - - - - - - - - -
# 5. ​Intermediate​: What is the difference between == and is in Python? 
# When would you use each one?

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


# - - - - - - - - - - - - - -
# 8. What will the output of this code be? Explain why.   
# 
# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4:2]) 



# - - - - - - - - - - - - - -
# 9.  Explain what this code is doing and what the final 
# result will be:

# data = {'a': 1, 'b': 2}
# try:
#     print(data['c'])
# except KeyError:
#     print("Key not found")
# finally:
#     print("Done")


# - - - - - - - - - - - - - -
# 10. What will be the output of the following code? Explain why.

# numbers = [1, 2, 3, 4]
# squared = [num ** 2 for num in numbers if num % 2 == 0]
# print(squared)

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
# - - - - - - - - - - - - - -
#1.  ​Basic​: What will the following code output and why?
    
# x = 5
# y = x 
# x += 1 
# print(f"x: {x}, y: {y}") 

# - - - - - - - - - - - - - -
    
#2.  ​Intermediate​: Explain what this code will output and why:
    
#def modify_string(s): # s = 'Hello'
#     s = s + "!" 
#     return s
        
# greeting = "Hello"
# modify_string(greeting)
# print(greeting) 

# - - - - - - - - - - - - - - 
# 3.  ​Basic​: What will be the value of numbers after the following code executes?
    
# numbers = [1, 2, 3, 4, 5]
# numbers[1:3] = [8, 9] # [1, 8, 9, 4, 5]
# print(numbers)

# - - - - - - - - - - - - - 

# 4.  ​Intermediate​: Determine the output of this code:
    
# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
        
# counter = outer()
# print(counter())
# print(counter())

### BEYOND THE SCOPE OF PY109 -- come back to this one

# - - - - - - - - - -

# 5.  ​Basic​: What will the following code output?
    
# values = ['', 0, None, False, [], 'Python', 42] # only truthy values are 'Python' and 42

# for value in values:
#     if value:
#         print(f"{value} is truthy")
#     else:
#         print(f"{repr(value)} is falsy")

#  is falsy
# 0 is falsy
# None is falsy
# False is falsy
# [] is falsy
# Python is truthy
# 42 is truthy

# - - - - - - - - - - - - - - 
# 6.  ​Intermediate​: What will this code output? Explain why.
    
# d1 = {'a': 1, 'b': 2} 
# d2 = d1 
# d3 = dict(d1) 

# d1['c'] = 3 
# print(d1) 
# print(d2) 
# print(d3) 

# - - - - - - - - - - - - - - 
# 7.  ​Advanced​: What's the output of the following code and why?
    
# def strange_math(a, b):
#     if a and b:  
#         return a * b
#     elif a or b: 
#         return a + b
#     else:
#         return 0
            
# print(strange_math(2, 3)) 
# print(strange_math(0, 5)) 
# print(strange_math(4, 0)) 
# print(strange_math(0, 0)) 

# - - - - - - - - - - - - - -
# 8. ​Advanced​: Predict the output:

# def mystery(items): 
#     result = []
#     for i in range(len(items)):
#         if i % 2 == 0:
#             result.append(items[i])
#     return result 
        
# data = "Python"
# print(mystery(data)) 
# print(mystery(mystery(data))) 

# - - - - - - - - - - - - - -
# 9. ​Intermediate​: What will be the output of this code?

# words = ['apple', 'banana', 'cherry']
# capitalized = []

# for word in words:
#     capitalized.append(word.capitalize())  
        
# print(words) 
# print(capitalized) 

# words[0] = 'apricot' 
# print(words) 
# print(capitalized)  

# - - - - - - - - - - - - - - 
# # 10 Advanced

# def process_data(data, filter_func=None): 
#     if filter_func is None:
#         filter_func = lambda x: x
            
#     result = []
#     for item in data:
#         if filter_func(item):
#             result.append(item)
#     return result
        
#numbers = [1, 2, 3, 4, 5, 6]
# evens = process_data(numbers, lambda x: x % 2 == 0)
# odds = process_data(numbers, lambda x: x % 2 != 0)
# all_nums = process_data(numbers)

# print(evens)
# print(odds)
# print(all_nums)

### BEYOND THE SCOPE OF PY109 -- come back to this one
# - - - - - - - - - - - - - -

#1.  ​Basic​: What will the following code output and why?
   
# a = 10
# b = a 
# a += 5 
# print(a, b) 

# - - - - - - - - - - - - - -
# 2.  ​Basic​: Explain the difference between == and is operators 
# in Python. Provide a code example that demonstrates a case 
# where they produce different results.

# - - - - - - - - - - - - - - 

# 3.  ​Intermediate​: What will the following code output and why?
   
# def change_list(lst): # lst = [1, 2, 3]
#     lst.append(4)  
#     lst.append(5) 
        
# my_list = [1, 2, 3]
# change_list(my_list)
# print(my_list) 

# - - - - - - - - - - - - - -
# 4.  ​Intermediate​: Write a function that takes a string 
# and returns a new string with every word capitalized. 
# Words are separated by spaces.

# def capitalize_words(input_string):

#     input_lst = input_string.split()

#     output_string = ''
    
#     for word in input_lst:
#         output_string += word.capitalize() + ' '

#     return output_string

# print(capitalize_words('hello world'))  # 'Hello World'
# print(capitalize_words('python programming is fun'))  # 'Python Programming Is Fun'
# print(capitalize_words('launch school rocks'))  # 'Launch School Rocks'
# print(capitalize_words('a b c'))  # 'A B C'
# print(repr(capitalize_words('')))  # ''

# - - - - - - - - - - - - - -
# 6.  ​Intermediate​: What will the following code output and why?
   
# def outer_function():
#     x = 10
#     def inner_function():
#         print(x)
#     return inner_function
        
# func = outer_function()
# #func()
# - - - - - - - - - - - - - - -
#7.  ​Intermediate​: Write a function that takes a 
# list of integers and returns a new list with only 
# the even numbers. If there are no even numbers, 
# return an empty list.

# def even_list(lst):
# - - - - - - - - - - - - - - -
# 1.  ​Basic​: What will the following code output and why?
    
# x = 10

# def modify_variable():
#     x = 20               
#     print(f"Inside function: {x}") 

# modify_variable()
# print(f"Outside function: {x}") 

# - - - - - - - - - - - - - -
# 3.  ​Intermediate​: What will the following code 
# output and why?
    
# def update_number():
#     global number
#     number = 20
#     print(number) 

# number = 10
# update_number()
# print(number) 

# - - - - - - - - - --  - - -
# 4.  ​Intermediate​: What will the following code output and why? 
# Explain the underlying principle.
    
# def modify_list(lst): # lst = [1, 2, 3]
#     lst.append(4) # lst = [1, 2, 3, 4]; also mutates my_list
#     print(f"Inside function: {lst}")

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(f"Outside function: {my_list}")

# Inside function: [1, 2, 3, 4]
# Outside function: [1, 2, 3, 4]

# - - - - - - - - - - - -- - -
#6.  ​Intermediate​: What will the following code output and why?
    
# def change_string(s): # s = 'Hello'
#     s = s + " World" # 'Hello World'
#     print(f"Inside function: {s}") # Inside function: Hello World

# greeting = "Hello"
# change_string(greeting)
# print(f"Outside function: {greeting}") # Outside function: Hello

# - - - - - - - - - - - - - - 
# 7.  ​Advanced​: Explain the output of this code and the 
# underlying principle it demonstrates:
    
# def outer():
#     x = "outer variable"
        
#     def inner():
#         print(x) 
        
#     inner()

# outer()

# - - - - - - - - - - - - - -
# 
#8.  ​Intermediate​: What will this nested function code output and why?
    
# def outer():
#     x = "outer variable"
        
#     def inner():
#         x = "inner variable" # local variable separate from x in nonlocal scope, shadows x in nonlocal scope
#         print(f"Inner function: {x}") # Inner function: inner variable
        
#     inner()
#     print(f"Outer function: {x}") # Outer function: outer variable

# outer()
 # - - - - - - - - - - - - - -

# 9.  ​Advanced​: What will the following code output and why?
    
# a = [1, 2, 3]
# b = a 
# a.append(4) 
# print(b)
 # - - - - - - - - - - - - - 

# 10. ​Intermediate​: What will the following code output and why?
    
# def modify_dict(d): 
#     d["key"] = "new value" 

# my_dict = {"key": "original value"}
# modify_dict(my_dict)
# print(my_dict) 

# - - - - - - - - - - - - - -

# 11. ​Advanced​: Explain the difference in output between these two code examples:

    
# Example 1
# a = 5
# b = a 
# a = 10 
# print(b) 

# Example 2
# a = [1, 2, 3]
# b = a 
# a = [4, 5, 6] 
# print(b) 

# - - - - - - - - - - - - - -
# 12. ​Intermediate​: What will the following code output and why?
    
# def process(items): 
#     items = items + [4, 5] 
#     return items

# numbers = [1, 2, 3]
# result = process(numbers) 
# print(numbers) 
# print(result) 

# - - - - - - - - - - - - - - -

# Advanced​: What will the following code output and why?
   
# def strange_function():
#     x = 10
#     def inner_function():
#         nonlocal x
#         x = 20
#         print(f"Inner x: {x}") 
#     inner_function()
#     print(f"Outer x: {x}") 

# strange_function()
 # - - - - - - - - - - - - - -

 # 15. ​Intermediate​: What will the following code output and why?
   
# x = [1, 2, 3]
# y = x.copy() 
# x.append(4) 
# print(y) 
 # - - - - - - - - - - - - - -
 # ​Advanced​: Explain what happens in each line of this code:
   
# def outer():
#     count = 0
        
#     def inner():
#         nonlocal count
#         count += 1
#         return count
        
#     return inner

# counter = outer()
# print(counter())
# print(counter())

 # - - - - - - - - - - - - - 
# 17. ​Intermediate​: What will the following code output and why?
   
# a = 5
# b = 5
# print(a is b)

# c = 500
# d = 500
# print(c is d)

# - - - - - - - - - - - - - -

# 19. ​Advanced​: What will the following code output and why?
   
# def modify(a, b): 
#     a += 10 
#     b += [4] 

# num = 5
# lst = [1, 2, 3]
# modify(num, lst)
# print(num, lst) 
 # - - - - - - - - - - - - - 
# 20. ​Intermediate​: Explain what happens in this code in terms of variable 
# references:
   
