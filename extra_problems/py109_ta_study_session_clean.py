# Question 1.

#print({} and 2 < 3)

 # - - - - - - - - - - - - --

# print(not 'a' or []) 


# - - - - - - - - - - - - - -
# print(0 and 2 > '1' or 'c' > 'a') 

# - - - - - - - - - - - - - -
# lst1 = [0, 1, 2, 3] 

# lst2 = lst1.reverse() and lst1.reverse() 

# if lst2:
#     print(lst2)
# else:
#     print(lst1) 


# - - - - - - - - - - - - - -

# numbers = [1, 2, 3, 4] 
# result = numbers.pop() or numbers.pop() 

# print(numbers) 
# print(result) 

# - - - - - - - - - - - - - -
# a = [1, 2, 3]
# b = a 
# b = b + [4, 5] 
# print(a) 
# print(b) 

# - - - - - - - - - - - - - -

# def modify_list(lst): 

#     if lst and lst[0] == 0:  
#         lst.pop(0)  
#         return True 
#     return False 

# numbers = [0, 1, 2, 3] 
# result = modify_list(numbers) and modify_list(numbers) 

# print(result)
# print(numbers)  

# - - - - - - - - - - - - - -

# original = ["a", "b", "c"]
# modified = original.copy() 

# modified.append("d") if len(original) > 2 else original.clear() 

# print(original) 
# print(modified) 


# - - - - - - - - - - - - - -
# text = 'Hello! I am Eloise.'

# def swap(s):
#     for char in s:
#         s.replace(char, char.upper())
#     return s

# print(swap(text)) 
# print(text)


# - - - - - - - - - - - - - -

# exclamation_marks = '!!!'

# def shout(text):
#     return text.upper() + exclamation_marks

# print(shout('hello') + exclamation_marks)


# - - - - - - - - - - - - - -
# exclamation_marks = '!!!'

# def shout(text, exclamation_marks):
#     exclamation_marks += '¡¡¡'  
#     return text.upper() + exclamation_marks

# print(shout('hello', exclamation_marks) + exclamation_marks)


# - - - - - - - - - - - - - -
# exclamation_marks = '!!!'

# def shout(text):
#     global exclamation_marks
#     exclamation_marks = '¡¡¡'
#     return text.upper() + exclamation_marks

# - - - - - - - - - - - - - -

# exclamation_marks = '!!!'

# def shout(text):
#     exclamation_marks = '¡¡¡' + exclamation_marks 
#     return text.upper() + exclamation_marks

# print(shout('hello') + exclamation_marks)


# - - - - - - - - - - - - - -

#print({} and 2 > '1' or 'c' > 'a')

# - - - - - - - - - - - - - -
# Describe the two functions in terms of:
# 1. compare return values
# 2. side effects
# 3. overall function behavior, arguments, parameters etc.

# letters = ['a', 'b', 'c']

# def add_el1(lst, el): 
#     return lst + [el] 

# def add_el2(lst, el): 
#     return lst.append(el) 


# print(add_el1(letters, 'd'))
# print(add_el2(letters, 'd')) 
# print(letters) 


# - - - - - - - - - - - - - -
# text = 'Hello! I am Eloise.'

# def swap(s):

#     for char in s:

#     s.replace(char, char.upper())

# return s

# print(swap(text))

# print(text)

# - - - - - - - - - - - - - -
# text = 'Hello! I am Eloise'

# def swap(s):

#     for char in s:

#         text = s.replace(char, char.upper())

#     return text

# print(swap(text)) 

# print(text) 

# - - - - - - - - - - - - - -
#  Write function to increment every age by 1

# players = [
# {'name': "Joe", 'age': 25},
# {'name': "Andy", 'age': 31},
# {'name': "Ralph", 'age': 18},
# {'name': "Mark", 'age': 28},
# ]

# def plus_one(input_list):
#     for player in input_list:
#         player['age'] += 1

# plus_one(players)
# print(players)









# - - - - - - - - - - - - - -
#Here’s a version of function. Will it work correctly, why or why not

# players = [

# {'name': "Joe", 'age': 25},
# {'name': "Andy", 'age': 31},
# {'name': "Ralph", 'age': 18},
# {'name': "Mark", 'age': 28},

# ]

# def age_players(players):

#     for player in players:

#         for key, value in player.items():

#             if key == 'age':

#                 value += 1

# age_players(players)

# print(players)

