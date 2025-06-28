# 1. The following code causes an infinite loop (a loop that never 
# stops iterating). Why?

# counter = 0

# while counter < 5:
#     print(counter)

# Solution:
# A `while` loop will iterate as long as the expression is truthy. 
# In this case, the `while` loop iterates as long as `counter` 
# is less than 5. Because there is no expression within the 
# `while` block that increments `counter`, it remains `0` which 
# is always less than 5, in other words always falsy. A line of code after the call to `print`
# incrementing the `counter` variable would eventually make the
# condition truthy 

# - - - - - - - - - - - - - -
# 2. ---skip---

# - - - - - - - - - - - - - -
# 3. Use a while loop to print the numbers in my_list, one number 
# per line. Then, do the same with a for loop.

#my_list = [6, 3, 0, 11, 20, 4, 17]

# # Solution: 

# idx = 0

# while idx < len(my_list):
#     print(my_list[idx])
#     idx += 1

# for num in my_list:
#     print(num)

# - - - - - - - - - - - - - -
# 4. Use a while loop to print all numbers in my_list 
# with even values, one number per line. Then, print
#  the odd numbers using a ' for' loop.

#my_list = [6, 3, 0, 11, 20, 4, 17]

# idx = 0

# # even numbers

# while idx < len(my_list):
#     if my_list[idx] % 2 == 0:
#         print(my_list[idx])
#     idx += 1
# # odd numbers

# for num in my_list:
#     if num % 2 != 0:
#         print(num)

# - - - - - - - - - - - - - -
# 5. Print all of the even numbers in the following list 
# of nested lists. Don't use any while loops.

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for obj in my_list:
#     for num in obj:
#         if num % 2 == 0:
#             print(num)

# - - - - - - - - - - - - - -
# 6. Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. 
# In this problem, you should write code that creates a new 
# list with one element for each number in my_list. If the 
# original number is an even, then the corresponding element 
# in the new list should contain the string 'even'; otherwise, 
# the element should contain 'odd'.

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# def even_odd(num):
#     return 'even' if num % 2 == 0 else 'odd'

# new_list = [ even_odd(num) for num in my_list ]
# print(new_list)



# Expected output
# pretty-printed for clarity
# [
#     'odd', 'odd', 'even', 'odd',
#     'even', 'even', 'even', 'odd',
#     'odd', 'even', 'even'
# ]

# def odd_or_even(num_check):
#     return ('even' if num_check % 2 == 0 else 'odd')

# result = [ odd_or_even(num) 
#           for num 
#           in my_list ]

# print(result)

# - - - - - - - - - - - - - -
# 7. Write a find_integers function that returns a list 
# of all the integers from my_tuple:

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)


# def find_integers(input):

#     list_of_int = [
#         item
#         for item in input
#         if type(item) is int
#     ]

#     return list_of_int

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)
# integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]

# - - - - - - - - - - - - - -
# 8. Write a comprehension that creates a dict object 
# whose keys are strings and whose values are the length 
# of the corresponding key. Only keys with odd lengths 
# should be in the dict. Use the set given by my_set 
# as the source of strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_set_dict = {
    cat: len(cat)
    for cat in my_set

}

print(my_set_dict)












# result = {
#     element: len(element)
#     for element in my_set
#     if len(element) % 2 != 0
# }

# print(result)











# - - - - - - - - - - - - - -
# 9. Write a function that computes and returns the factorial 
# of a number by using a for or while loop. The factorial of a 
# positive integer n, signified by n!, is defined as the product 
# of all integers between 1 and n, inclusive:

# using `for` loop
# def factorial(n):
#     product = 1

#     for factor in range(1, n + 1):
#         product *= factor
    
#     return product

# Also in descending order
# def factorial(n):
#     product = 1

#     for factor in range(n, 0, -1):
#         product *= factor
#     return product


# using `while` loop

# def factorial(n):

#     factor = 1
#     product = 1

#     while factor <= n:
#         product *= factor
#         factor += 1
    
#     return product

# descending order
# def factorial(n):

#     product = 1

#     while n > 0:
#         product *= n
#         n -= 1
    
#     return product


# num = int(input("Please enter an integer and I'll calculate the factorial: "))

# result = factorial(num)
# print(result)

# - - - - - - - - - - - - - -

# The following code uses the randrange function from Python's random library
#  to obtain and print a random integer within a given range. Using a while 
# loop, it keeps running until it finds a random number that matches the last 
# number in the range. Refactor the code so it doesn't require two different 
# invocations of randrange.

# import random

# highest = 10
# number = random.randrange(highest + 1)
# print(number)

# while number != highest:
#     number = random.randrange(highest + 1)
#     print(number)

# highest = 10

# while True:
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break

# - - - - - - - - - - - - - -

# 11. Print all of the even numbers in the following 
# list of nested lists. This time, don't use any for loops.

# my_list = [
#   [1, 3, 6, 11],
#   [4, 2, 4],
#   [9, 17, 16, 0],
# ]

# idx_outer = 0

# while idx_outer < len(my_list):
#     idx_inner = 0

#     while idx_inner < len(my_list[idx_outer]):
#         inner_list = my_list[idx_outer]
#         if inner_list[idx_inner] % 2 == 0:
#             print(inner_list[idx_inner])
#         idx_inner += 1
    
#     idx_outer += 1