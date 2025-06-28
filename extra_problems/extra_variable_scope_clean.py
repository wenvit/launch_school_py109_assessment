###### From LSBot on 3/31/2025 ############

# count = 10

# def increment_counter():
#     count = count + 1
#     return count

# print(increment_counter()) 

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

# - - - - - - - - - - - - - -
# x = 100 

# def outer_function():
#     x = 50 # separate variable from global x; variable shadowing
    
#     def inner_function():
#         x = 25 # variable shadowing
#         print("Inner:", x) 
    
#     inner_function()
#     print("Outer:", x) 

# outer_function()
# print("Global:", x) 

# Inner: 25
# Outer: 50
# Global: 100


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


################
# What does the following code do and why? 

# total = 10

# def update_total():
#     total = total + 5 
#     return total

# print(update_total())


# - - - - - - - - - - - - - -

# total = 10

# def update_total(value):  
#     value = value + 5  
#     return value 

# result = update_total(total) 

# print(total)  
# print(result)  


# - - - - - - - - - - - - - -

# What is the output of this code?

# lst1 = [0, 1, 2, 3] 
# lst2 = lst1.pop(0) and lst1.pop() 

# if lst2:
#     print(2, lst2)
# else:
#     print(1, lst1) 

# - - - - - - - - - - - - - -
# What does the following code do?

# greeting = ["Hello"] 

# def greet(greeting):
#     greeting += ["world"]  
#     print(greeting) 

# greet(greeting)
# print(greeting) 

# - - - - - - - - - - - - - -

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

# - - - - - - - - - - - - - -
# greeting = "Hello"

# def greet(greeting): 
#     greeting += " world" 
#     print(greeting) 

# greet(greeting)
# print(greeting) 
# - - - - - - - - - - - - - - 
# greeting = "Hello"

# def greet():
#     greeting = greeting + " world" 
#     print(greeting) 

# greet()
# print(greeting) 

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
#             greeting = 'Hi'
#         print(greeting) 

#     rich_greet()
#     print(greeting) 

# greet(greeting) 
# print(greeting) 

# - - - - - - - - - - - - 

# greeting = "Hello"

# def greet(greeting):  

#     def rich_greet(greeting): 
#         if greeting:
#             greeting = "Hi" 
#         print(greeting) 

#     rich_greet(greeting)
#     print(greeting) 

# greet(greeting) 
# print(greeting) 

# - - - - - - - - - - - - - -
# greeting = "Hello"

# def greet(greeting):  # greet parameter = Hello

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