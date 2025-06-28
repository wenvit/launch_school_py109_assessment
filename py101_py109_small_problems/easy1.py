# Isn't it Odd?
# Write a function that takes one integer argument and returns True 
# when the number's absolute value is odd, False otherwise.

# def is_odd(num):
#     return abs(num % 2) == 1

# print(is_odd(1))
# print(is_odd(-1))
# print(is_odd(10))
# print(is_odd(0))
# print(is_odd(-2))

# - - - - - - - - - - - - - -
# Odd Numbers
# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# for num in range(1, 100, 2):
#     print(num)

# Further Exploration
# Consider adding a way for the user to specify the starting and ending values 
# of the odd numbers printed.

# def print_odd(start, stop):
#     if start % 2 == 0:
#         start += 1
#     for num in range(start, stop + 1, 2):
#         print(num)

#print_odd(2, 25)
#print_odd(1, 99)
# print_odd(5, 17)

# - - - - - - - - - - - - - -
# Even Numbers
# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

# for num in range(2, 100, 2):
#     print(num)

# - - - - - - - - - - - - - -
# How big is the room?
# Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# length_m = float(input('Please enter room length in meters.  '))
# width_m = float(input('Please enter room width in meters.  '))

# area_m2 = length_m * width_m
# area_ft2 = area_m2 * 10.7639

# print(f"The room's area is {area_m2:,.1f} m2, which is equivalent to\n"
#       f"{area_ft2:,.1f} ft2.")

# - - - - - - - - - - - - - -
# Tip Calculator
# Create a simple tip calculator. The program should prompt for a bill amount 
# and a tip rate. The program must compute the tip, then print both the tip 
# and the total amount of the bill. You can ignore input validation and 
# assume that the user will enter valid numbers.

# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

# bill = float(input('What is the bill? '))
# tip_percentage = int(input('What is the tip percentage? '))

# tip = bill * tip_percentage / 100
# print(f'The tip is ${tip:,.2f}')
# print(f'The total is ${bill + tip:,.2f}')

# - - - - - - - - - - - - - -

# Sum or Product of Consecutive Integers
# Write a program that asks the user to enter an integer 
# greater than 0, then asks whether the user wants to 
# determine the sum or the product of all numbers between 1 
# and the entered integer, inclusive.

# Example 1
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.
# Example 2
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.

# def calculate_sum(target):
#     return sum(range(1, target + 1))

# def calculate_product(target):
#     product = 1

#     for num in range(1, target + 1):
#         product *= num
#     return product

# number = int(input('Please enter an integer > 0. '))

# while number < 0:
#     number = int(input('Try again. The number must be a positive integer. '))

# operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')

# if operation == 's':
#     sum_total = calculate_sum(number)
#     print(f'The sum of integers between 1 and {number} is {sum_total}.')
# elif operation == 'p':
#     product_total = calculate_product(number)
#     print(f'The product of integers between 1 and {number} is {product_total}.')
# else:
#     print('Unknown operation. Only valid entries are "s" and "p".')

# - - - - - - - - - - - - - -
# Short Long Short
# Write a function that takes two strings as arguments, determines the 
# length of the two strings, and then returns the result of concatenating 
# the shorter string, the longer string, and the shorter string once again. 
# You may assume that the strings are of different lengths.

# def short_long_short(string1, string2):
#     if len(string1) > len(string2):
#         return string2 + string1 + string2
#     return string1 + string2 + string1

# # These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

# # - - - - - - - - - - - - - -
# Leap Years (Part 1)
# Write a function that takes any year greater than 0 as input
#  and returns True if the year is a leap year, or False if it is not.

# For simplicity, this exercise assumes that the Gregorian calendar 
# has been in continuous use since the year 1. We'll address that
#  assumption in the next exercise that follows this one.

# To determine whether a given year is a leap year, use the
# rules of the Gregorian calendar:

# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.

# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     else:
#         return year % 4 == 0

# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == False)
# print(is_leap_year(1100) == False)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == False)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# - - - - - - - - - - - - - -
# Leap Years (Part 2)
# In the previous exercise, we assumed that the Gregorian calendar 
# has been in continuous use since the year 1. However, the Gregorian 
# calendar wasn't adopted until much later; prior to that, much of 
# the world used the Julian calendar, which observed leap year 
# every 4 years.

# in 1752, England, Ireland, and the British colonies all 
# switched to the Gregorian calendar. Update the function 
# from the previous exercise so it uses the Julian calendar 
# prior to 1752, and the Gregorian calendar starting in 1752.

# def is_leap_year(year):
#     if year < 1752:
#         return year % 4 == 0
#     elif year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     else:
#         return year % 4 == 0

# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# - - - - - - - - - - - - - -
# Multiples of 3 and 5
# Write a function that computes the sum of all numbers 
# between 1 and some other number, inclusive, that are multiples 
# of 3 or 5. For instance, if the supplied number is 20, the 
# result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

# multiples of 3:  num % 3 == 0
# multiples of 5: num % 5 == 0

# def multisum(target):
#     multiples = []
#     for num in range(1, target + 1):
#         if (num % 3 == 0) or (num % 5 == 0):
#             multiples.append(num)
#     return sum(multiples)

# These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)

# - - - - - - - - - - - - - -
# UTF-16 String Value
# Write a function that determines and returns the UTF-16 
# string value of a string passed in as an argument. The 
# UTF-16 string value is the sum of the UTF-16 values of 
# every character in the string. (You may use ord to 
# determine the UTF-16 value of a character.)

# def utf16_value(text):
#     utf16_sum = 0

#     for char in text:
#         utf16_sum += ord(char)
#     return utf16_sum


# These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)


