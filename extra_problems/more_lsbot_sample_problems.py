
# 1. Variable Assignment and Scope (Basic)
# Explain what happens in this code and identify 
# the scope of each variable:
# x = 10

# def my_function():
#     global y
#     y = 20 
#     x = 30 
#     print(x) 

# my_function()
# print(x) # 10
# print(y) # 20

# - - - - - - - - - - - - - -
# 2. Truthiness vs Boolean Values (Basic)
# Explain the difference between truthy/falsy values and the 
# boolean values True/False. Give examples of each falsy value in Python.

# 0, 0.0, 0j
# False, None
# [], '', {}
# set(), range(0), frozenset()

# - - - - - - - - - - - - - - 

# my_str = 'something'
# my_lst = ['a', 'b', 'c']


# def my_func(var):
# #    var = var + ' else'
# #    var += ['d']
#     var = var + ['d']
#     return var

# #print(my_func(my_str))
# print(my_func(my_lst)) 
# #print(my_str)
# print(my_lst) 
 # - - - - - - - - - -

# 3. String Methods (Intermediate)
# Write code that demonstrates the difference between strip(), 
# lstrip(), and rstrip() methods using the string "  hello world  ".

# string = "  hello world  "
# print(repr(string.strip()))
# print(repr(string.lstrip()))
# print(repr(string.rstrip()))

# - - - - - - - - - - - - - -

# 4. List Mutability (Intermediate)
# Predict the output and explain what happens with mutability:

# list1 = [1, 2, 3]
# list2 = list1 
# list2.append(4) 
# print(list1)
# print(list2)

# - - - - - - - - - - - - - -
# 6. Dictionary Methods (Basic)
#Write code using a dictionary with at least 3 key-value 
# pairs that demonstrates the use of 
# .keys(), .values(), .items(), and .get() methods.

# pets = {
#     'cat': 'Tiger Lily',
#     'dog1': 'Bailey',
#     'dog2': 'Blue',
# }

# print(pets.keys())
# print(pets.values())
# print(pets.items())
# print(pets.get('fish'))

# - - - - - - - - - - - - - - 
# 7. Slicing (Intermediate)
# Given the string "programming", write expressions to:
# •   Extract the first 4 characters
# •   Extract the last 3 characters
# •   Extract every other character
# •   Reverse the string using slicing

# string = 'programming'
# print(string[:4])
# print(string[-3:])
# print(string[::2])
# print(string[::-1])

# - - - - - - - - - - - - - -
#8. Operator Precedence (Intermediate)
#Evaluate this expression step by step, explaining the order of operations:
#result = 2 + 3 * 4 ** 2 // 3 - 1
# **, * and //, + and -
# 2 + 3 * (4 ** 2) // 3 - 1
# 2 + (3 * 16 // 3) - 1
# 2 + 16 - 1 
# 1
# rint(result)

# - - - - - - - - - - - - - 
# 11. Variable Shadowing (Intermediate)
# Explain what variable shadowing is and predict the output:

# x = 'global'

# def outer():
#     x = 'outer'
    
#     def inner():
#         x = 'inner'
#         print(x) 
    
#     inner()
#     print(x) 

# outer()
# print(x) 

# - - - - - - - - - - - - - -
# 12. Loop Control and Range (Intermediate)
# Write a for loop using range() that prints only 
# the even numbers from 2 to 10, and explain how range() works.

# for num in range(2, 11):
#     if num % 2 == 0:
#         print(num)

# - - - - - - - - - - - - - -
# 13. Exception Handling (Basic)
# Identify what type of exception each of these code snippets would raise and explain when it would occur:
# Snippet A
#int('hello') # ValueError - appropriate type but inappropriate value

# Snippet B
# my_list = [1, 2, 3]
# print(my_list[5]) # IndexError - index out of range

# Snippet C
# my_dict = {'a': 1}
# print(my_dict['b']) # KeyError - key doesn't exist
# - - - - - - - - - - - - - - 

# 1.  ​Basic​: Given the string text = "Launch School", what will text[2:8] 
# return? Explain how Python determines the start and end positions.
# text = "Launch School"
# print(text[2:8]) # unch S

# - - - - - - - - - - - - - -
# 2.  ​Basic​: What's the difference between my_list[1:4] and my_list[1:4:1]? 
# Are they equivalent?

# my_list = [20, 40, 60, 80, 100, 110, 120, 140]

# slice1 = my_list[1:4]
# print(slice1)

# slice2 = my_list[1:4:1]
# print(slice2)

# print(slice1 == slice2)
# print(slice1 is slice2)

# - - - - - - - - - - - - - -
# 3.  ​Intermediate​: Given numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
# explain what each of these slicing operations returns:

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(numbers[::2]) 
# print(numbers[1::2]) 
# print(numbers[::-1]) 

# - - - - - - - - - - - - - -
# 4.  ​Intermediate​: What will happen when you try to slice beyond 
# the bounds of a list? 
# For example, if my_list = [1, 2, 3], 
# what does my_list[1:10] return?

# my_list = [1, 2, 3]
# print(my_list[1:10]) 
# print(my_list[2:4]) 

# - - - - - - -- - - - - - - 
# 5.  ​Advanced​: Given word = "programming", write a slice 
# expression that returns every second character starting 
# from the third character.

# word = "programming"
# print(word[3::2])

# - - - - - - - - - - - - - -

# 6.  ​Advanced​: Explain the difference between negative 
# indexing and negative step values in slicing. 
# Give examples of each.

# word = "programming"
# # print(word[-5:]) # mming
# # print(repr(word[2:5])) # rgo
# # print(repr(word[2:6:-1])) # 
# print(word[:4:-2]) # 

# seq = 'abcdefghi'
# print(seq[3:7])    # defg
# print(seq[-6:-2])  # defg
# print(seq[2:8])  # cdefgh 
# print(seq[7:3:-2]) # efgh --> hf
# print(repr(seq[3:3])) # ''
# print(seq[:])  # abcdefghi        
# print(seq[::-1])  # ihgfedcba
# print(seq[:len(seq)]) # abcdefghi

# seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(seq[3:7])       # [4, 5, 6, 7]
# print(seq[-6:-2])     # [5, 6, 7, 8]
# print(seq[2:8:2])     #  [3, 5, 7]
# print(seq[3:3])       #  []
# print(seq[:])         #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(seq[::-1])     # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(seq[0:len(seq): -1])

# seq = [[1, 2], [3, 4]]
# seq_dup = seq[:] # creates a copy; shallow copy
# print(seq[0] is seq_dup[0])  # True



# - - - - - - - - - - - -
# 7.  ​Basic​: What will 3 + 4 * 2 evaluate to? Explain the order of operations.
# print(3 + 4 * 2) # `*` is evaluated before `+`; 3 + 8 = 11

# - - - - - - - - - - - - - - - -
# 8.  ​Basic​: Compare the results of 10 - 3 - 2 versus 10 - (3 - 2). Explain why they're different.

# print(10 - 3 - 2) # 5
# print(10 - (3 - 2)) # 9

# - - - - - - - - - - - - - -
# 5 + 3 * 2 > 10 and 4 < 6 or False
# ((5 + (3 * 2)) > 10) and (4 < 6) or False
# 11 > 10 and (4 < 6) or False
# True and True or False
# True or False --> True

# print(5 + 3 * 2 > 10 and 4 < 6 or False)

# - - - - - - - - - - - - - - 
# print(not 5 > 3 and 2 + 3 == 5 or 1)
# False and 5 == 5 or 1
# False or 1 ==> 1

# - - - - - - - - - - - - - -
# 12. ​Advanced​: Explain why parentheses are important in this expression:
   
# result1 = 10 + 5 * 2 / 5   # 10 + (5 * 2 / 5) ==> 10 + 2 = 12
# result2 = (10 + 5) * 2 / 5 # 15 * 2 / 5 ==> 6

# print(result1)
# print(result2)

# - - - - - - - - - - - - - -

# 13. ​Intermediate​: Given text = "Python Programming", 
# what will text[2 + 1:len(text) - 3] return? 
# Explain the order of operations.

# text = "Python Programming"
# print(text[2 + 1:len(text) - 3])

# text[3:15] ==> hon Programm

# - - - - - - - - - - - - - - - 

#14. ​Advanced​: What will this code output and why?
   
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = my_list[1 + 1:2 * 3:2 - 1]
# print(result)

# result = my_list[2:6:1] ==> [3, 4, 5, 6]
# - - - - - - - - - - - - - -
# data = "abcdefghijklmnop" 
# cdefghijklmnop
# cfilo --> olifc
# print(data[14:1:-3])

# - - - - - - - - - - - - - - 

# text = "Python Programming"
# result = text[::2][::-1][1::2]
# print(result)

# Pto rgamn
# nmagr otP
# mg t

# - - - - - - - - - - - - - -
# 3.  ​Advanced​: Given matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
# explain what matrix[1:][0][::2] returns and 
# trace through each step of the slicing operation.

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = matrix[1:][0][::2] 
# print(result)

# [[4, 5, 6], [7, 8, 9]]
# [4, 5, 6]
# [4, 6]

# - - - - - - - - - - - - - -

# 4.  ​Advanced​: Compare and contrast the behavior of these three expressions:
   
# my_string = "Launch School"
# expr1 = my_string[100:] 
# expr2 = my_string[:100] 
# expr3 = my_string[100:200] 

# print(repr(expr1))
# #print(expr2)
# print(repr(expr3))

# - - - - - - - - - - - - - -
# 5.  ​Advanced​: Given nested = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 
# write a single expression using slicing that produces [2, 4, 7, 9].

#nested = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# expected output [2, 4, 7, 9]
# result = nested[0][1:4:2] + nested[1][1:4:2]
# print(result)

# - - - - - - - - - - - - - -
#  ​Advanced​: Determine the result and explain the order of operations:
   
# result = 2 + 3 * 4 ** 2 % 5 - 1
# print(result)
# order of operations: 
# **
# *, %
# +, -
# 2 + (3 * (4**2) % 5) - 1
# 2 + (3 * 16 % 5) -1
# 2 + 3 - 1
# 4
# - - - - - - - - - - - - - -
#print(True or False and not True or False and True)
# True or False and False or False and True
# True or (False and False) or (False and True)
# True or False or False
# True

# - - - - - - - - - - - - - -

# result1 = 5 > 3 > 1 
# result2 = (5 > 3) > 1 

# print(result1)
# print(result2)

# - - - - - - - - - - - - - -

# 9.  ​Advanced​: What will this code output and in what order are the operations performed?
   
# x = 10
# y = 5
# result = x > y and x - y > 0 or x // y == 2 and not x % y
# print(result)

# 10 > 5 and 10 - 5 > 0 or 10 // 5 == 2 and not 10 % 5
# (10 > 5) and (10 - 5 > 0) or (10 // 5 == 2) and (not (10 % 5))
# True and True or True and True
# (True or True) ==> True

# - - - - -- - - - - - - - - -

# 10. ​Advanced​: Trace through the evaluation of this complex expression step by step:
   
# print(not 0 and 3 + 2 * 4 > 10 or 5 ** 2 // 4 == 6 and False)
# not 0 and (3 + 2 * 4 > 10) or (5 ** 2 // 4 == 6 ) and False
# True and (11 > 10) or ( 6 == 6) and False
# True and True or True and False
# True or False
# True