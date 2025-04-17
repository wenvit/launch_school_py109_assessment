# Loop and Print
# Add some code inside the following for loop to print 
# the current value of num on each iteration. Before 
# you execute the code: What sequence of numbers 
# do you expect to be printed?

# for num in range(0, 11, 2):
#     print(num)

# Expected output:
# 0
# 2
# 4
# 6
# 8
# 10

# - - - - - - - - - - - - - -
# Looping over List Elements
# Using the code below as a starting point, write a while loop 
# that prints the elements of lst at each index and terminates 
# after printing the last element of the list.

# lst = [1, 3, 7, 15]
# index = 0

# while index < len(lst):
#     print(lst[index])
#     index += 1

# - - - - - - - - - - - - - -
# Continue

# Write a for loop that iterates over the elements of the list 
# cities and prints the length of each string. If the element 
# is None, use the continue statement to skip forward to the
#  next iteration without printing anything.

# cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
#           'Vienna', None, 'London', 'Beijing', None]

# for city in cities:
#     if city is None:
#         continue
#     print(city)

# - - - - - - - - - - - - - -
# And on and on and on
# The following code keeps looping forever. (You can hit Ctrl-C to 
# stop it.) Why does the loop keep running? Modify it so that it 
# stops after the first iteration.

# while True:
#     print("and on")
#     break

# A `while` block will iterate as long as the condition is truthy. 
# In this case, `True` is truthy and nothing in the `while` block
# makes it falsy, so it iterates forever. A `break` statement will
# break out of nearet enclosing loop.

# - - - - - - - - - - - - - -
# Finding Nemo
# Loop over the elements of the fish_list list below, logging 
# each one. Terminate the loop immediately after printing the 
# string 'Nemo'.

# fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

# for fish in fish_list:
#     print(fish)
#     if fish == 'Nemo':
#         break

# - - - - - - - - - - - - - -
# Loop on Command
# Modify the following code so the loop continues iterating 
# until the user inputs 'yes'.

# while True:
#     print('Should I stop looping?')
#     answer = input()

#     if answer in ['y', 'yes', 'Yes']:
#         break

# - - - - - - - - - - - - - -

