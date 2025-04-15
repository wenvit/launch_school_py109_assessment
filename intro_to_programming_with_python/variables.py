# 1. Classify the following potential non-constant variable 
# names as idiomatic, non-idiomatic, or illegal. For the 
# non-idiomatic and illegal names, explain your choice.

# Solution:
# Idiomatic non-constant variable names use snake_case with all lowercase
# letters (a-z) and words separated by '_'. Can use digits (0-9). 
# Illegal to start with digit or be a reserved keyword (e.g., return, def, pass)

# index         idiomatic
# CatName       non-idiomatic - contains uppercase chars and doesn't separate words with '_'
# lazy_dog      idiomatic
# quick_Fox     non-idiomatic - contains uppercase character
# 1stCharacter  illegal - starts with digit
# operand2      idiomatic
# BIG_NUMBER    non-idiomatic - contains uppercase characters
# π             non-idiomatic - not ASCII character

# - - - - - - - - - - - - - -
# 2. Classify the following potential function names as 
# idiomatic, non-idiomatic, or illegal. For the non-idiomatic 
# and illegal names, explain your choice.

# Solution
# Idiomatic function names use snake_case with all lowercase
# letters (a-z) and words separated by '_'. Can use digits (0-9). 
# Illegal to start with digit or be a reserved keyword (e.g., return, def, pass)

# index         idiomatic
# CatName       non-idiomatic - contains uppercase chars & doesn't separate words with '_'
# lazy_dog      idiomatic
# quick_Fox     non-idiomatic - contains uppercase char
# 1stCharacter  illegal - starts with digit
# operand2      idiomatic
# BIG_NUMBER    non-idiomatic - contains uppercase characters
# π             non-idiomatic - not ASCII character

# - - - - - - - - - - - - - -
# 3. Classify the following potential constant names as idiomatic, 
# non-idiomatic, or illegal. For the non-idiomatic and illegal names, 
# explain your choice.

# Solution:
# Idiomatic constant variable names use SCREAMING_SNAKE_CASE with all 
# uppercase letters (A-Z) and words separated by '_'. Can use digits (0-9). 
# Illegal to start with digit or be a reserved keyword (e.g., return, def, pass)

# index       non-idiomatic - contains lowercase letters
# CatName     non-idiomatic - contains lowercase letters & words not separated by '_'
# snake_case  non-idiomatic - contains lowercase letters
# LAZY_DOG3   idiomatic
# 1ST         illegal - starts with digit
# operand2    non-idiomatic - contains lowercase letters
# BIG_NUMBER  idiomatic
# Π           non-idiomatic - not an ASCII char

# - - - - - - - - - - - - - -
# 4. Classify the following potential class names as idiomatic, non-idiomatic, 
# or illegal. For the non-idiomatic and illegal names, explain your choice.

# Solution:
# Idiomatic class names use PascalCase with words starting with uppercase
# character and remainder lowercase. Multiple words separated by uppercase letter.
# Can use digits (0-9). Illegal to start with digit or be a reserved keyword 
# (e.g., return, def, pass)

# index      non-idiomatic - starts with lowercase char
# CatName    idiomatic
# Lazy_Dog   non-idiomatic - '_' between words
# 1ST        illegal - starts with digit
# operand2   non-idiomatic - starts with lowercase letter
# BigNumber3 idiomatic
# Πi         non-idiomatic - contains non-ASCII char
#
# - - - - - - - - - - - - - -
# 5. Write a program named greeter.py that greets 'Victor' three times. 
# Your program should use a variable and not hard code the string value 
# 'Victor' in each greeting. Here's an example run of the program:

# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.

# Solution:

# name = 'Victor'

# def greeting(time_of_day):
#     print(f'Good {time_of_day}, {name}.')

# greeting('Morning')
# greeting('Afternoon')
# greeting('Evening')

# - - - - - - - - - - - - - -
# 6. Write a program named age.py that includes someone's age 
# and then calculates and reports the future age 10, 20, 30, 
# and 40 years from now. Here's the output for someone who is 
# 22 years old.

# You are 22 years old.
# In 10 years, you will be 32 years old.
# In 20 years, you will be 42 years old.
# In 30 years, you will be 52 years old.
# In 40 years, you will be 62 years old.

# years = [10, 20, 30, 40]

# current_age = int(input('How old are you? '))

# print(f'You are {current_age} years old.')

# for year in years:
#     print(f'In {year} years, you will be {current_age + year} years old.')

# - - - - - - - - - - - - - -
# 7. What happens when you run the following code? Why?

# NAME = 'Victor'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# NAME = 'Nina'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# Solution:
# this will print
# Good Morning, Victor 
# Good Afternoon, Victor
# Good Evening, Victor
# Good Morning, Nina
# Good Afternoon, Nina
# Good Evening, Nina

# The print calls concatenate the greeting strings with
# the values referenced by NAME. Although NAME doesn't
# follow idiomatic rules for non-constant variable names,
# the program will run without an error.

# - - - - - - - - - - - - - -
# 8. Challenge: This program uses a bit of math. Don't let that scare you 
# away -- try it anyway.

# Assume you have $1,000.00 in the bank, and you've somehow managed 
# to find a bank that pays you 5% (this is a wish-fulfillment fantasy) 
# compounded interest every year. After one year, you will have 
# $1,050 ($1,000 times 1.05). After two years, you will have $1,050 
# times 1.05, or $1102.50. Create a variable named balance that 
# contains the amount of money you will have after 5 years, then 
# print the result. Use a single expression if you can to set 
# balance to the correct value.

# Solution:
# balance = 1000
# balance = balance * (1.05 ** 5)

# print(f'${balance:,.2f}')

# - - - - - - - - - - - - - -
# 9. Repeat the previous question but, this time, use augmented 
# assignment to compute the final result, one year at a time.

# Solution:

# balance = 1000

# balance *= 1.05 # yr 1
# balance *= 1.05 # yr 2
# balance *= 1.05 # yr 3
# balance *= 1.05 # yr 4
# balance *= 1.05 # yr 5

# print(f'${balance:,.2f}')
# - - - - - - - - - - - - - -
# 10. Assume that obj already has a value of 42 when the 
# code below starts running. Which of the subsequent statements 
# reassign the variable? Which statements mutate the value of 
# the object that obj references? Which statements do neither? 
# If necessary, you can read the documentation.

obj = 42          # initialization to int 42

# Solution:

obj = 'ABcd'      # reassignment to str 'ABcd'
obj.upper()       # neither
obj = obj.lower() # reassignment to str 'abcd'
print(len(obj))   # neither
obj = list(obj)   # reassignment to list ['a', 'b', 'c', 'd']
obj.pop()         # mutation of list ['a', 'b', 'c']
obj[2] = 'X'      # mutation of list ['a', 'b', 'X']
obj.sort()        # mutation of list ['X', 'a', 'b'] 
set(obj)          # neither
obj = tuple(obj)  # reassignment to tuple ('X', 'a', 'b')

print(obj)        # ('X', 'a', 'b')