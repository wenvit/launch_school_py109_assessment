# Repeat Yourself
# Write a function that takes two arguments, a string and a positive 
# integer, then prints the string as many times as the integer indicates.

# def repeat(text, multiplier):
#     for _ in range(multiplier):
#         print(text)

# repeat('Hello', 3)
# repeat("something else", 10)

# example output
# Hello
# Hello
# Hello

# - - - - - - - - - - - - - -

# ddaaiillyy ddoouubbllee
# Write a function that takes a string argument and returns 
# a new string that contains the value of the original string 
# with all consecutive duplicate characters collapsed into 
# a single character.

# def crunch(text):

#     if text:
#         crunched = text[0]
#         idx = 1
#         while idx <= len(text) - 1:
#             if text[idx] != text[idx-1]:
#                 crunched += text[idx]
#             idx += 1
#         return crunched
#     return text

# def crunch(text):

#     if text: 
#         crunched = text[0]
#         for char in text:
#             if crunched.endswith(char):
#                 continue
#             crunched += char
#         return crunched
#     return text



# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# - - - - - - - - - - - - - -

# Bannerizer
# Write a function that takes a short line of text and prints it within a box.

# def print_in_box(message):
#     top_bottom = '+' + ('-' * (len(message) + 2)) + '+'
#     spaces = ' ' * (len(message) + 4)
#     padding = '|' + ' ' * (len(message) + 2) + '|'
#     banner = '|' + ' ' + message + ' ' + '|'

#     print(top_bottom)
#     print(spaces)
#     print(padding)
#     print(spaces)
#     print(banner)
#     print(spaces)
#     print(padding)
#     print(spaces)
#     print(top_bottom)

# print_in_box('To boldly go where no one has gone before.')
# print_in_box('')

# - - - - - - - - - - - - - -

# Stringy Strings
# Write a function that takes one argument, a positive integer, 
# and returns a string of alternating '1's and '0's, always starting with a '1'. 
# The length of the string should match the given integer.

# def stringy(num):

#     stringy_string = '1'
#     for _ in range(num - 1):
#         if stringy_string.endswith('1'):
#             stringy_string += '0'
#         else:
#             stringy_string += '1'
#     return stringy_string

# another way

# def stringy(num):

#     stringy_string = ''
#     for idx in range(num):
#         digit = '1' if idx % 2 == 0 else '0'
#         stringy_string += digit
#     return stringy_string

# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

# - - - - - - - - - - - - - -
# Right Triangles
# Write a function that takes a positive integer, n, 
# as an argument and prints a right triangle whose sides 
# each have n stars. The hypotenuse of the triangle (the diagonal
#  side in the images below) should have one end at the lower-left 
# of the triangle, and the other end at the upper-right.

# def triangle(num):
#     for multiplier in range(1, num + 1):
#         print(' ' * (num - multiplier) + ('*' * multiplier))

# triangle(5)
# triangle(9)

# - - - - - - - - - - - - - -

# Madlibs
# Madlibs is a simple game where you create a story template with
#  "blanks" for words. You, or another player, then construct a 
# list of words and place them into the story, creating an often 
# silly or funny story as a result.

# Create a simple madlib program that prompts for a noun, a verb,
#  an adverb, and an adjective, and injects them into a story that you create.

# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly

# Do you walk your blue dog quickly? That's hilarious!
# The blue dog walks quickly over the lazy dog.
# The dog quickly walks up to Joe's blue turtle.

# madlib = {}

# madlib['noun'] = input('Enter a noun: ')
# madlib['verb'] = input('Enter a verb: ')
# madlib['adjective'] = input('Enter an adjective: ')
# madlib['adverb'] = input('Enter an adverb: ')

# print(f"Do you walk your {madlib['adjective']} {madlib['noun']} {madlib['adverb']}? That's hilarious!")
# print(f'The {madlib['adjective']} {madlib['noun']} {madlib['verb']} {madlib['adverb']} over the lazy dog.')
# print(f"The {madlib['noun']} {madlib['adverb']} walks up to Joe's {madlib['adjective']} turtle. ")

# - - - - - - - - - - - - - -

# Double Doubles
# A double number is an even-length number whose left-side digits are 
# exactly the same as its right-side digits. For example, 44, 3333, 
# 103103, and 7676 are all double numbers, 
# whereas 444, 334433, and 107 are not.

# Write a function that returns the number provided as an 
# argument multiplied by two, unless the argument is a double number. 
#  If the argument is a double number, return the double number as-is.

# def twice(num):
#     num_str = str(num)
#     split_idx = len(num_str) // 2

#     if num_str[:split_idx] == num_str[split_idx:]:
#         return num
#     else:
#         return num * 2

# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True

# - - - - - - - - - - - - - -

# Grade Book
# Write a function that determines the mean (average) of 
# the three scores passed to it, and returns the letter 
# associated with that grade.

# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

# from statistics import mean

# def get_grade(score1, score2, score3):
#     avg_score = mean([score1, score2, score3])

#     if avg_score >= 90:
#         return 'A'
#     elif avg_score >= 80:
#         return 'B'
#     elif avg_score >= 70:
#         return 'C'
#     elif avg_score >= 60:
#         return 'D'
#     else:
#         return 'F'

# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True

# - - - - - - - - - - - - - -
# Clean up the words
# Given a string that consists of some words and an assortment 
# of non-alphabetic characters, write a function that returns 
# that string with all of the non-alphabetic characters replaced 
# by spaces. If one or more non-alphabetic characters occur in a 
# row, you should only have one space in the result (i.e., the 
# result string should never have consecutive spaces).

# def clean_up(text):
#     text_clean = ''
#     for char in text:
#         if char.isalpha():
#             text_clean += char
#         elif text_clean.endswith(' '):
#             text_clean += ''
#         else:
#             text_clean += ' '
#     return text_clean


# print(clean_up("---what's my +*& line?") == " what s my line ")
# # True

# - - - - - - - - - - - - - -
# What Century is That?
# Write a function that takes a year as input and returns the century. 
# The return value should be a string that begins with the century number, 
# and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000 
# comprise the 20th century.

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True