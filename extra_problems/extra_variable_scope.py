###### From LSBot on 3/31/2025 ############

# count = 10

# def increment_counter():
#     count = count + 1
#     return count

# print(increment_counter()) 

# Solution:
# This raises an UnboundLocalError. When Python encounters the 
# assignment of `count` variable within the `increment_counter`
# function, it interprets it as a local variable. However, on the 
# right side of the assignment operator `=`, `count` hasn't been
# defined locally. To fix, can either use `global count` which would
# reassign the global variable, or rename to a new local variable such 
# as new_count = count + 1

# - - - - - - - - - - - - - -

# count = 10

# def increment_counter():
#     new_count = count + 1 
#     return new_count

# print(increment_counter()) 
# print(count)  

# - - - - - - - - - - - - - -
# message = "Hello"

# def change_message():
#     global message  
#     message = "Goodbye" 

# change_message()
# print(message) 

# Solution:
# This will print: Goodbye
# When `change_message` is called, the `global message`
# statement tells Python that the global `message` variable
# is used inside the function. So `message = 'Goodbye'`
# reassigns the global `message` variable to 'Goodbye'. This
# is a reassignment because strings are immutable. When `print`
# is called passing `message` as an argument, it prints the 
# reassigned global variable. This is an example of a function 
# with side effects.

# - - - - - - - - - - - - - -
# items = [1, 2, 3]

# def add_item():
#     items.append(4)

# def replace_items():
#     items = [5, 6, 7] 

# add_item()  
# print(items) 
# replace_items() 
# print(items) 


# Solution:

# This will print:
# [1, 2, 3, 4]
# [1, 2, 3, 4]

# The global `items` variable is initialized to a list `[1, 2, 3]`
# When `add_item` is called, the function mutates the global `items`
# object by appending `4`. The `print` function is called with `items`
# as an argument and prints the mutated global object `[1, 2, 3, 4]`.
# `replace_items` is called, which initializes a local `items` variable
# to a list `[5, 6, 7]`. When a variable is initialized within a function,
# it's a local variable, separate from a global variable even though it has
# the same name. This is an example of variable shadowing. So the global
# `items` is not mutated by `replace_items` and the next print call 
# prints `[1, 2, 3, 4]`

# - - - - - - - - - - - - - -
# x = 100

# def outer_function():
#     x = 50 
    
#     def inner_function():
#         x = 25 
#         print("Inner:", x)
    
#     inner_function()
#     print("Outer:", x)

# outer_function()
# print("Global:", x)


# This will print: 

# Inner: 25
# Outer: 50
# Global: 100

# Global `x` is initialized to 100.
# Within `outer_function`, separate `x` variable initialized to 50. 
# This is a separate variable available within `outer_function` shadows
# global `x`. Within `inner_function`, separate `x` variable initialized
# to 25. Again this is a separate variable available within `inner_function`
# that shadows other `x` variables in outer scopes. The `outer_function` is 
# called, which calls `inner_function`, which calls `print('Inner:', x)`. 
# This is the `x` available in `inner_function` which is 25.
#  Then `print('Outer:', x)` is executed. This is `x` available in `outer_function`
# which is 50. Finally, `print('Global;', x)` executes which references global `x`
# which is 100. Illustrates global scope, variable shadowing

# - - - - - - - - - - - - - -
# user_data = {"name": "Alice", "points": 0}

# def update_name():
#     user_data["name"] = "Bob" 

# def reset_user():
#     user_data = {"name": "Guest", "points": 0} 

# update_name()
# print(user_data) 
# reset_user()
# print(user_data) 


# Solution:
# This will print:
# {'name': 'Bob', 'points': 0}
# {'name': 'Bob', 'points': 0}

# Global `user_data` variable is initialized to a dictionary object
# `{"name": "Alice", "points": 0}`.
# `update_name` is called, which mutates the global `user_data` dict 
# object by updating the value associated with the `name` key to 'Bob'.
# The first `print` call passing `user_data` as an argument, prints
# the mutated global `user_data` dict object. The `reset_user` function
# is called, which initializes `user_data` to a dict object. Because
# this variable initialization occurs within the body of a function, 
# Python interprets it as a local variable, separate from the global
# `user_data` variable. This is variable shadowing. The assignment of
# dict object to the local `user_data` variable doesn't mutate the
# global `user_data` variable. So the next `print` call prints the same
# `user_data` object as above. Illustrates variable scope, variable shadowing, 
# function with side effects

# - - - - - - - - - - - - - -
# def modify_list(lst): 

#     lst.append(4)  
#     lst = [10, 20, 30] 
#     lst.append(40) 
#     return lst

# numbers = [1, 2, 3]
# result = modify_list(numbers) 

# print(numbers) 
# print(result) 

# Solution:
# This will print:
# [1, 2, 3, 4]
# [10, 20, 30, 40]
# Global `numbers` variable is initialized to a list object `[1, 2, 3]`.
# `modify_list` function is called passing `numbers` object by reference.
# `modify_list` function is defined with a parameter `lst`. Global `numbers`
# and local `lst` variables point to the same object when the function is called.
# `lst.append(4)` mutates the global list object by appending `4`. `numbers` points 
# to the mutated list. On the next line in the function body, the local variable 
# `lst` is reassigned to a new list object `[10, 20, 30]`. This reassignment of the 
# local variable doesn't impact the global `numbers` object. Then the local `lst`
# is mutated by appending `40`. The mutated local `lst` return value is
# `[10, 20, 30, 40]` which is assigned to the `result` variable.
# `print(numbers)` outputs `[1, 2, 3, 4]`, and `print(result)` outputs
# `[10, 20, 30, 40]`
# This demonstrates variable scope, mutability of lists, passing by object reference,
# and function side effects (mutating global object from within function)

################
# What does the following code do and why? 

# total = 10

# def update_total():
#     total = total + 5 
#     return total

# print(update_total())

# Solution: 
# This will raise an UnboundLocalError on line 186 because when Python
# encounters a variable assignment within the body of a function, it assumes
# it's assignment of a local variable. The expression `total + 5` on the right
# side of the assignment statement raises the error because `total` hasn't 
# been assigned locally yet.

# - - - - - - - - - - - - - -

# total = 10

# def update_total(value):  
#     value = value + 5  
#     return value

# result = update_total(total) 

# print(total)  
# print(result)  

# Solution:
# This will print:
# 10
# 15
# This is because `update_total` is called passing the global variable
# `total` as an argument. Within `update_total`, the local variable (parameter)
# `value` is reassigned by adding 5, which gets returned to `result`. So printing
# `result` outputs `15`. The global variable `total` remains `10` because integers 
# are immutable.
# This demonstrates variable scope

# - - - - - - - - - - - - - -

# What is the output of this code?

# lst1 = [0, 1, 2, 3] 
# lst2 = lst1.pop(0) and lst1.pop() 

# if lst2:
#     print(2, lst2)
# else:
#     print(1, lst1) 


# Solution


# This will print:
# 1 [1, 2, 3]

# In the assignment of lst2 , the expression lst1.pop(0) and lst1.pop() 
# returns 0. This is because applying the pop method with the argument 0 
# to lst1 returns the integer 0 which is the element at the index 0 of lst1 (first element).  
# This is a mutating operation on lst1. 
# Because 0 is falsy, the and expression 
# short circuits, returns the first falsy value of 0, and the right subexpression 
# never executes. The value of lst1 after the mutation is [1, 2, 3]. 
# pop method returns None, so lst2 is assigned to NoneIn the 
# if/else statement, the if block doesn’t execute because lst2 is 0 which is 
# falsy. The else block executes which prints 1 [1, 2, 3]
# Concepts of truthy/falsy, short circuiting, mutable lists, methods that mutate
# objects in place return None

# - - - - - - - - - - - - - -
# What does the following code do?

# greeting = ["Hello"]

# def greet(greeting): 
#     greeting += ["world"]  
#     print(greeting) 

# greet(greeting)
# print(greeting) 

# This will print:
# ['Hello', 'world']
# ['Hello', 'world']

# The global variable `greeting` is assigned to the list object ['Hello'].
# The `greet` function is called passing the `greeting` object by reference
# to the parameter `greeting`, which means the local
# variable `greeting` points to same list object as global `greeting`. 
# Within the `greet` function, `greeting` is mutated by the augmented assignment
# operator `+=`. The result is that the list object referenced by both the local `greeting`
# and global `greeting` variables are mutated to ['Hello', 'world'].
# When `greet` is called, the `print` call within the function prints `greeting` 
# which references `['Hello', 'world']`. Then `print` is called passing global
# `greeting` which prints the same list object `['Hello', 'world']`. 
# This demonstrates variable scope, mutability of lists.

# - - - - - - - - - - - - - -

# Changing augmented assignment to assignment

# greeting = ["Hello"]

# def greet(greeting): 
#     greeting = greeting + ["world"] 
#     print(greeting) 

# greet(greeting)
# print(greeting) 

#- - - - - - - - - - - - - - - - 
# greeting = ["Hello"]

# def greet():
#     greeting += ["world"] 
#     print(greeting)

# greet()
# print(greeting)


# This one is also an unboundlocal error. Without passing 
# a reference to the global object to the function, the function
# greet is reassigning the global variable greeting, which isn't allowed
#


# - - - - - - - - - - - - - -
# greeting = "Hello"

# def greet(greeting):
#     greeting += " world" 
#     print(greeting) 

# greet(greeting)
# print(greeting) 


# This print:
# Hello world
# Hello

# The global `greeting` variable is initialized to a string 'Hello'.
# `greet` function is called passing `greeting` object by reference to
# the parameter `greeting`. Within the function, `greeting` is 
# reassigned with the augmented assignment operator `+=` to `Hello world`. 
# This reassignment creates a new string and doesn't impact the global 
# `greeting` object because can't reassign global variable from within
# a function without global keyword. The `print` call from
# within the function prints the local `greeting` which is 'Hello world'
# `print` call outside function prints unchanged global `greeting` variable 
# which is `Hello`


#################
# def replace(string, value):  
#     while True: 
#         break

#     string = value 

# greet = 'Hey!'
# replace(greet, 'Hello')
# print(greet) 

#################
# greeting = 'Hello'

# def greet():
#     greeting = 'Hi' 

# greet()
# print(greeting) 


################
# what is printed and why

# def modify_list(lst): 
#     lst.append(4) 
#     lst = [1, 2, 3] 
#     return lst

# numbers = [5, 6, 7]
# result = modify_list(numbers)
# print(numbers) 
# print(result) 



#################
# numbers = [1, 2, 3]
# def modify_list():
#     numbers.append(4) 
#     print(numbers) 

# modify_list()
# print(numbers) 


##################
# x = 10
# def outer():
#     x = 20
#     def inner():
#         global x
#         x = 30
#         print(x)  
#     inner()
#     print(x) 

# outer()
# print(x) 



############
# fruits = {'apple': 1, 'banana': 2, 'cherry': 3}

# def update_fruits():
#     fruits['apple'] = 5  
#     fruits.update({'date': 4}) 
#     print(fruits) 

# update_fruits()
# print(fruits) 



###############
# numbers = [1, 2, 3]
# def modify_list():
#     numbers = [4, 5, 6] 
#     numbers.extend([7, 8]) 
#     print(numbers) 
# modify_list()
# print(numbers) 

#############
# Example use case for short-circuiting
# Check to ensure name is not None before
# calling `isupper` method
# # 
# name = 'WENDY'

# if name != None and name.isupper(): 
#     print(f"Hi, {name}.")
# else:
#     print("Hello, whoever you are.")

############
# name = get_name_from_user()
# if name:
#     print(f"Hi {name}")
# else:
#     print("you must enter your name!")

###########
# data = []  

# def add_item(item):
#     global data  
#     data.append(item)  

# add_item("hello")
# print(data) 

###########

# data = []

# def replace_data():
#     data = ["replaced"] 

# def replace_data_correctly():
#     global data
#     data = ["replaced"]  

# def modify_data():
#     data.append("modified") 

# replace_data() 
# replace_data_correctly() 
# modify_data() 
# print(data)    


##############
# data = []  

# def add_item_without_global(item): 
#     data.append(item) 

# def add_item_with_global(item): 
#     data.append(item)  

# add_item_with_global('XYZ') 
# add_item_without_global('ABC') 
# print(data) 







###############
# data = []


# def reassign_without_global():
#     data = ["new data"]  
    
# def reassign_with_global():
#     global data
#     data = ["new data"] 

# reassign_without_global()
# print(data) 

# reassign_with_global()
# print(data) 

##############


# def add_element(my_list):
#     my_list.append([4]) 

# my_list = [1, 2, 3]

# add_element(my_list)
# print(my_list) 

############

# def add_element(my_list):
#     my_list = my_list + [4] 
#     print(my_list) 


# my_list = [1, 2, 3]

# add_element(my_list)
# print(my_list) 

# - - - - - - - - - - - - -

# def add_element():
#     my_list = [4] 
#     print(my_list) 


# my_list = [1, 2, 3]

# add_element()
# print(my_list) 

# - - - - - - - - - - - - -
# def add_element(my_list):
#     my_list += [4] 
#     print(my_list) 


# my_list = [1, 2, 3]

# add_element(my_list)
# print(my_list) 


# - - - - - - - - - - - - -


# total = 10

# def update_total(value):  
#     value = value + 5    
#     return value 

# result = update_total(total) 
# print(total)   
# print(result) 


# - - - - - - - - - - - - - -
# greeting = "Hello"

# def greet(greeting):  
#     def rich_greet():
#         if greeting:
#             greeting = "Hi"
#         print(greeting) 

#     rich_greet()
#     print(greeting) 

# greet(greeting) 
# print(greeting) 

# - - - - - - - - - - - - 

# greeting = "Hello"

# def greet(greeting):  
#     def rich_greet():
#         global greeting
#         if greeting:
#             greeting = "Hi"
#         print(greeting) 

#     rich_greet()
#     print(greeting) 

# greet(greeting) 
# print(greeting) 

# - - - - - - - - - - - - - -
# a = [1, 2, 3]

# def my_function(a):
#     a = [1]
#     print(a)

# my_function(a)
# print(a) 

# - - - - - - - - - - - - - - -
# hello = "Hello, world!"

# def my_func():
#     print(hello)

# print(my_func())