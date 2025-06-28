# Question 1.

#print({} and 2 < 3)



# Solution:
# This will print: {}
# The `<` operator has precedence so this expression is evaluated as:
# {} and (2 < 3). The `and` operator short circuits, meaning it stops
# evaluating the expression when it knows with certainty what
# the outcome will be. `and` returns the first falsy value or the 
# last value if all are truthy. In this case, the empty dictionary `{}` is 
# falsy so the expression evaluation short circuits. The last operand 
# evaluated is returned so `{}` is printed. 

 # - - - - - - - - - - - - --

#print(not 'a' or []) 


# Solution:
# This prints: []
# The left subexpression `not 'a'` evaluates falsy because 'a'
# is truthy but is negated by `not`. No short circuiting occurs because
# `or` only short circuits when the left operand is truthy. `or` returns
# the first value that's truthy when evaluating from left to right or 
# the last value if all are falsy. So the last operand evaluated is `[]` 

# - - - - - - - - - - - - - -
#print(0 and 2 > '1' or 'c' > 'a') 




# Solution:

# This will print: True

# The greater than `>` operator takes precedence over `and` and `or`,
# so this expression can be clarified and is equivalent to:
# print(0 and (2 > '1') or ('c' > 'a')) 
# The `and` operator takes precedence over `or`.
# The `and` subexpression short circuits because 0 is falsy, so the 
# expression then simplifies to:
# print(0 or ('c' > 'a'))
# This evaluates to the boolean `True` because with the `or` operator
# only one of the subexpressions needs to be truthy. Short circuiting
# does not occur because the left side of the expression is falsy, and
# `or` will return the first value that's truthy or the last value if all are
# falsy. The right subexpression `'c' > 'a'` is `True` because Python
# compares strings lexicographically and 'c' comes after 'a' in the ASCII
# sequence so is greater than. 
# Note that the `and` subexpression short circuits so `2 > '1'` is never
# evaluated but if it had been evaluated, it would have raised a TypeError
# because an integer can't be compared to a string

# - - - - - - - - - - - - - -
# lst1 = [0, 1, 2, 3] 

# lst2 = lst1.reverse() and lst1.reverse() 

# if lst2:
#     print(lst2)
# else:
#     print(lst1) 


# Solution:

# This will print [3, 2, 1, 0]

# lst1 is initialized to a list object [0, 1, 2, 3]
# On line 55, lst2 is assigned to the value returned by 
# the expression `lst1.reverse() and lst1.reverse()`
# The left subexpression `lst1.reverse()` mutates lst1
# by reversing its elements and also returns the value `None`. 
# Because `None` is falsy, the `and` expression
# short circuits and doesn't evalute the right subexpression. So
# the lst2 variable is assigned to `None`
# In the `if/else` statement, because lst2 is `None` which
# is false, the `if` block doesn't execute. Instead, the 
# `else` block executes, which prints the mutated lst1.

# - - - - - - - - - - - - - -

# numbers = [1, 2, 3, 4] 
# result = numbers.pop() or numbers.pop() 

# print(numbers) 
# print(result)



# Solution:
# This will print: 
# [1, 2, 3]
# 4

# The `numbers` variable is initialized to a list object, `[1, 2, 3, 4]`.
# In the `or` expression, the left subexpression calls the `pop` method on
# `numbers` which mutates the list by removing and returning the last element `4`.
# Because the return value of `4` is truthy, the `or` operator short circuits and
# stops evaluating the expresson. The `result` variable is therefore
# assigned to the integer 4. The first `print` call that passes `numbers` as an
# argument prints the mutated `numbers` list of [1, 2, 3]. The second `print`
# call passes the `result` variable and prints 4.
# This demonstrates concepts of mutable list objects, mutating the caller, truthiness and
# short circuiting. 

# - - - - - - - - - - - - - -
# a = [1, 2, 3]
# b = a
# b = b + [4, 5] 
# print(a) 
# print(b) 



# This will print:
# [1, 2, 3]
# [1, 2, 3, 4, 5]
# The variable `a` is initialized to a list, `[1, 2, 3]` on line 103.
# `b` is assigned to `a` on line 104, so both `b` and `a` are pointing to
# the same list object at this point in the code. On line 105 however, `b` is
# reassigned to a new list resulting from the expression `b + [4, 5]`.
# Because this is a reassignment of `b`, `b` now references the new list and
# `a` remains unchanged. Note that if augmented assignment (`b += [4, 5]`) 
# had been used instead of reassigning `b`, both `b` and `a` would have been
# mutated to the same list object so both print calls would have resulted in
# outputs of [1, 2, 3, 4, 5]`.

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


# This prints:
# False
# [1, 2, 3]

# `numbers` global variable is initialized to list [0, 1, 2, 3] on line 126.
# On line 133, the first call to `modify_list` on the left side of the `and` expression
# passes `numbers` as argument to `modify_list`. `modify_list` function parameter 
# `lst` is a local variable which points to the same `numbers` list object because `numbers`
# is passed by object reference to the function. The `if` expression within 
# the function evaluates the expression `lst and lst[0] == 0`. 
# An `and` expression will return the first falsy value or the last value 
# if all are truthy. In this case, because the left operand `lst` contains elements 
# and is truthy, expression doesn't short circuit and returns `0`, 
# which is the value resolved by the right subexpression `lst[0]`
# because the element at index 0 of lst is 0. This simplifies to `0 == 0` which is `True`
# so the code in the `if` block executes. The `pop` method with 0 as an argument
# mutates local `lst` by removing the element at index 0. This also mutates global
# `numbers` list because `lst` references the same object. The list object referenced by
# both global `numbers` and local `lst` variables is `[1, 2, 3]` at this point.
# The function returns `True` to the left operand on line 133. 
# Because the left subexpression is truthy on line 133, the right subexpression executes, 
# which again calls `modify_list` passing the mutated `numbers` list as an argument. 
# This time, the expression in the `if` statement evaluates to `False`. This is because
# `lst and lst[0]` returns a value of 1. The left operand `lst` is still truthy because it
# contains elements but the right operand `lst[0]` returns 1 since the element at index 0 is now 1.
# The expression simplifies to `1 == 0` with returns `False` so the `if` block doesn't
# execute. The function returns `False` to the right side of the `and` expression on line 133
# so `result` is assigned to `False` because `True and False` is `False`
# This demonstrates concepts of variable scope, mutability of lists, passing by object reference,
# truthiness and short circuiting.

# - - - - - - - - - - - - - -

# original = ["a", "b", "c"]
# modified = original.copy() 

# modified.append("d") if len(original) > 2 else original.clear() 

# print(original) 
# print(modified) 


# This will print:
# ['a', 'b', 'c']
# ['a', 'b', 'c', 'd']

# `original` is assigned to list object ['a', 'b', 'c']
# `modified` is assigned to a copy of `original`, not same object as `original`. 
# Ternary expression mutates `modified` by applying `append` method passing `d` as argument
# if len(original) > 2 else `original` list is emptied by applying `clear` method. 
# Because the length of original` is 3, `modified` is mutated by appending 'd'. 
# `modified` is a separate object from `original`, so `original `is not mutated.

# - - - - - - - - - - - - - -
# text = 'Hello! I am Eloise.'

# def swap(s):
#     for char in s:
#         s.replace(char, char.upper())
#     return s

# print(swap(text)) 
# print(text)

# This will print:
# Hello! I am Eloise.
# Hello! I am Eloise.

# # The global `text` variable is initialized to the string 'Hello! I am Eloise.' 
# The function `swap` is called passing the global `text` variable as an argument. 
# The `swap` function has a parameter `s` which points to the string object referenced by 
# `text` when the function is called. Within the function, a `for` statement is used to loop
# over each character in `s`, and the `replace` method is called on each character
# replacing it with an uppercase letter returned from the `upper` method. 
# `replace` creates a new string but the new uppercased string isn't captured by a variable
# in this function. The original string referenced by the local variable `s` isn't mutated
# because strings are immutable. The function returns `s` which is unchanged from the 
# original string object. 
# This demonstrates concepts of immutability of strings and variable scope.

# - - - - - - - - - - - - - -

# exclamation_marks = '!!!'

# def shout(text):
#     return text.upper() + exclamation_marks

# print(shout('hello') + exclamation_marks)

# This prints:
# HELLO!!!!!!

# The global variable `exclamation_mark` is initialized to the string `'!!!'`.
# The `shout` function is defined with the parameter `text`.
#  When `shout` is called passing `'hello'` as an argument, 
# `text` is assigned to the string `'hello'`. The function returns `text.upper()` which
# creates a new string with all characters in `text` uppercased concatenated with 
# the string referenced by the global `exclamation_marks` variable. The global variable
# can be accessed from within the function body. The value returned by calling 
# `shout` is then concatenated with the global `exclamation_marks` value again. 

# - - - - - - - - - - - - - -
# exclamation_marks = '!!!'

# def shout(text, exclamation_marks):
#     exclamation_marks += '¡¡¡'  
#     return text.upper() + exclamation_marks

# print(shout('hello', exclamation_marks) + exclamation_marks)

# Solution:

# This will print: HELLO!!!¡¡¡!!!

# A global variable `exclamation_marks` is initialized to the string `'!!!'`.
# The `shout` function is called passing the string `'hello'` and the value
# referenced by the global variable `exclamation_marks` as arguments to the
# `text` and `exclamation_marks` parameters, respectively.
# The `exclamation_marks` parameter is a local variable within the `shout`
# function that's a separate variable from the global `exclamation_marks`
# variable even though it has the same name. This is an example of 
# variable shadowing. Within the function, the augmented assignment operator `+=`
# is used to reassign the local `exclamation_marks` to `'!!!¡¡¡'`. 
# This reassignment of the local variable doesn't change the value of the 
# global `exclamation_marks` because strings are immutable.
#  The function returns the concatenation of `text` uppercased 
# (by applying `upper` method to 'hello') and the
# value of the local `exclamation_marks`. The `print` function then concatenates
# the value returned by `shout` with the global value of `exclamation_marks` which
# remains `'!!!'`
# This demonstrates concepts of variable scope, immutability of strings, 
# variable shadowing.

# - - - - - - - - - - - - - -
# exclamation_marks = '!!!'

# def shout(text):
#     global exclamation_marks
#     exclamation_marks = '¡¡¡'
#     return text.upper() + exclamation_marks

# print(shout('hello') + exclamation_marks)

# This will print: HELLO¡¡¡¡¡¡
# The `shout` function is called passing 'hello' as an argument,
# and the return value is `text` uppercased (by applying `upper` to
# the string 'hello') concatenated with the value referenced by
# the global variable `exclamation_marks`, which is '¡¡¡'. This is 
# a global variable because the `global` keyword is used with 
# `exclamation_marks` within the function. The `print` call then
# concatenates the return value from the `shout` function call with 
# the global `exclamation_marks` value. Note that if the `global`
# keyword hadn't been used within the function, the `print` call would
# raise a `NameError` saying `exclamation_marks` is not defined because
# it's not defined outside the function.
# This demonstrates concepts of variable scope, use of global keyword.

# - - - - - - - - - - - - - -

# exclamation_marks = '!!!'

# def shout(text):
#     exclamation_marks = '¡¡¡' + exclamation_marks 
#     return text.upper() + exclamation_marks

# print(shout('hello') + exclamation_marks)


# Solution:
# This will raise an UnboundLocalError because Python sees the assignment
# `exclamation_marks = '¡¡¡' + exclamation_marks`, and interprets 
# `exclamation_marks` as a local variable, however in the expression 
# on the right side of the assignment operator, `exclamation_marks` hasn't
# been defined locally yet. Use of `global` keyword is one way around this, and
# would result in reassigning the global `exclamation_marks`

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

# solution:
# This will print:
# ['a', 'b', 'c', 'd']
# None
# ['a', 'b', 'c', 'd']

# The global letters variable is initialized to a list object, ['a', 'b', 'c']

# The function add_el1 is defined with two parameters: lst and el. It returns 
# a new list created by concatenating lst with [el]. add_el1 has no side effects 
# because it creates a new list object.

# The function add_el2 is defined with two parameters: lst and el. It mutates 
# lst by calling the append method on lst with el passed as an argument. 
# This mutates the global letters object because the local variable
# lst references the same object as letters which is a mutable list. 
# It returns None because the append method mutates the object it is called on 
# and has a return value of None. add_el2 has a side effect of
# mutating a global object.

# add_el1 is called, passing letters and 'd' as arguments. A new list 
# object of ['a', 'b', 'c', 'd'] is returned and printed when passed to the 
# print function.

# add_el2 is called, passing letters and 'd' as arguments. letters is 
# mutated by appending 'd' and None is returned and printed when passed to the 
# print function.

# Finally, letters is passed to printw. The object referenced by letters 
# has been mutated by add_el2 so ['a', 'b', 'c', 'd'] is output.
# This problem illustrates concepts of function side effect of 
# mutating global object, passing by object reference, and shows an 
# example of a method that mutates the object it’s called on and 
# returns a value of None







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

# def age_plus_one(input_dict):
#     for person in input_dict:
#         person['age'] += 1

# age_plus_one(players)
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

