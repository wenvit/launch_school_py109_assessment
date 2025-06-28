 # 12. 2.  ​Intermediate​: Create a function that takes 
# a list of integers and returns a new list containing 
# only the prime numbers from the original list.

# return True if prime --> not divisible by any other number except 1 & itself

# def is_prime(input):
#     # creates list of factors for composite numbers
#     # if input is prime number, list is empty (falsy)
#     # if input is prime number, return not [] ==> True
 
#     check = [
#         num for
#         num in range(2, input)
#         if input % num == 0
#     ]

#     return not bool(check)

# def prime_list(orig_list):

#     new_list = []

#     for num in orig_list:
#         if is_prime(num) and num != 1:
#             new_list.append(num)
#     return new_list

# print(prime_list([5, 4, 3, 2, 1]))
# print(prime_list([23, 50, 60, 37, 1]))

# another example
# prime100 = []

# for num in range(2, 101):
#     if is_prime(num):
#         prime100.append(num)

# print(prime100)





# - - - - - - - - - - - - - -

#11. Basic: Write a function that accepts a string and 
# returns a boolean indicating whether the string is a 
# palindrome (reads the same forward and backward, ignoring
# # spaces, punctuation, and case).

# def is_palindrome(input_string):
#     clean_string = ''

#     if input_string:

#         for char in input_string:
#             if char.isalnum():
#                 clean_string += char.lower()
#         return clean_string == clean_string[::-1]
#     else:
#         return 'Must provide a valid string.'



# print(is_palindrome('!!!saiPpuak&&&ivikaupp  iAs **'))
# print(is_palindrome('mad     am'))
# print(is_palindrome('what is palindrome'))
# print(is_palindrome(''))
# - - - - - - - - - - - - - - - - - -
# def clean_up(text):
#     clean_text = ''

#     for char in text:
#         if char.isalpha():
#             clean_text += char
#         elif clean_text.endswith(' '):
#             clean_text += ''
#         else:
#             clean_text += ' '
#     return clean_text

# print(clean_up("---what's my +*& line?"))
# print(clean_up("a---what's my +*& line?"))
# print(clean_up(" ---what's my +*& line?"))




#print(clean_up("---what's my +*& line?") == " what s my line ")
# True




# - - - - - - - - - - - - - -
# def crunch(input_string):

#     crunched_string = ''

#     for char in input_string:
#         if not crunched_string.endswith(char):
#             crunched_string += char
#     return crunched_string
    

# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# - - - - - - - - - - - - - - 

# def center_of(text):
#     mid_idx = len(text) // 2

#     if len(text) % 2 == 1:
#         return text[mid_idx]
#     else:
#         return text[mid_idx - 1: mid_idx + 1]

# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True

# - - - - - - - - - - - - - -
# def oddities(input_list):
#     new_list = []
#     for idx in range(len(input_list)):
#         if idx % 2 == 0:
#             new_list.append(input_list[idx])
#     return new_list

# def oddities(input_list):
#     new_list = [
#         input_list[idx]
#         for idx in range(len(input_list))
#         if idx % 2 == 0
#     ]
#     return new_list

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# - - - - - - - - - - - - 
# def xor(param1, param2):
    
#     return bool(param1) != bool(param2) 


# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# - - - - - - - - - - - - - - 
# def penultimate(text):
#     text_list = text.split()
#     return text_list[-2]

# # These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# - - - - - - - - - - - - - -
# num1 = float(input('==> Enter the first number: '))
# num2 = float(input('==> Enter the second number: '))

# def computations(num1, num2, operator):
#     match operator:
#         case '+':
#             return num1 + num2
#         case '-':
#             return num1 - num2
#         case '*':
#             return num1 * num2
#         case '/':
#             return num1 / num2

# print(f'==> {num1} + {num2} = {computations(num1, num2, '+')}')
# print(f'==> {num1} - {num2} = {computations(num1, num2, '-')}')
# print(f'==> {num1} * {num2} = {computations(num1, num2, '*')}')
# print(f'==> {num1} / {num2} = {computations(num1, num2, '/')}')

# - - - - - - - - - - - - - -
# user_name = input('What is your name?')

# if user_name.endswith('!'):
#     print(f'HELLO {user_name.upper()} WHY ARE WE YELLING?')
# else:
#     print(f'Hello {user_name}.')

# - - - - - - - - - - - - - -
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



# - - - - - - - - - - - - - - 
# Write a function that computes the sum of all numbers between 1 and some other number, 
# inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, 
# the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# def multisum(target):

#     sum_of_ints = 0

#     for num in range(1, target + 1):
#         if (num % 3 == 0) or (num % 5 == 0):
#             sum_of_ints += num

#     return sum_of_ints
        


# These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)



# - - - - - - - - - - - - -
# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False

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



# - - - - - - - - - - - -
# def short_long_short(string1, string2):
#     if len(string1) < len(string2):
#         new_string = string1 + string2 + string1
#     else:
#         new_string = string2 + string1 + string2

#     return new_string


# These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")


# - - - - - - - - - - - - - - 
# def compute_sum(user_num):
#     sum_of_int = 0

#     for num in range(1, (user_num + 1)):
#         sum_of_int += num
#     return sum_of_int

# def compute_product(user_num):
#     prod_of_int = 1

#     for num in range(1, (user_num + 1)):
#         prod_of_int *= num
#     return prod_of_int

# user_num = int(input('Enter an integer greater than 0: '))
# operation = input('Enter "s" to compute the sum, or "p" to compute the product: ')

# if operation == 's':
#     print(f'The sum of the integers between 1 and {user_num}'
#           f' is {compute_sum(user_num)}.')
# else:
#     print(f'The product of the integers between 1 and {user_num}'
#           f' is {compute_product(user_num)}.')




# - - - - - - - - - - - - - - -
# for even_num in range(2, 100, 2):
#     print(even_num)

# - - - - - - - - - - - - - - -
# for odd_num in range(1, 100, 2):
#     print(odd_num)

# - - - - - - - - - - - - - - 
# def is_odd(num):

#     return abs(num) % 2 == 1

# print(is_odd(0))

# - - - - - - - - - - - - - -
# student = {
#     'id': 123,
#     'grade': 'B',
# }

# print('name' in student)
# print('grade' in student)
# - - - - - - - - - - - - - - -

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }

# half_numbers = []

# for score in numbers.values():
#     half_numbers.append(score // 2)
# print(half_numbers)

# 
#[50, 25, 12]
# - - - - - - - - - - - - - - -

# scores = [96, 47, 113, 89, 100, 102]

# one way
# high_scores = [1 for score in scores if score >= 100]
# print(high_scores)
# print(sum(high_scores))

# another way

# count = 0

# for score in scores:
#     if score >=100:
#         count += 1
# print(count)
# - - - - - - - - - - - - - - -
# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
# energy.remove('fossil')
# print(energy)
# - - - - - - - - - - - - - - -
# def first(my_list):
#     if my_list:
#         return my_list[0]
#     return 'list is empty'

# print(first(['Earth', 'Moon', 'Mars']))  # Earth
# print(first([]))

# - - - - - - - - - - - - - - 
# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']

# while grocery_list:
#     print(grocery_list.pop(0))

# print(grocery_list)

# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []