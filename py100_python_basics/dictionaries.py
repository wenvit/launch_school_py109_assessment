# First Car
# Create a dictionary that contains the following data, 
# and assign it to a variable named car.

# type	color	mileage
# sedan	blue	80000

# first_car = {
#     'type':   'sedan',
#     'color':  'blue',
#     'mileage': 80_000,

# }

# print(first_car)

# - - - - - - - - - - - - - -
# Adding the Year
# Add some code below the following code to define a year 
# key with a value of 2003. Don't update the dictionary 
# literal; instead, add some code after lines 1-5:

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
# }

# car['year'] = 2003

# print(car)

# - - - - - - - - - - - - - -
# Broken Odometer
# Using the following code, delete the 'mileage' key and its associated value from car.

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
#     'year':    2003,
# }

# del car['mileage']
# print(car)

# - - - - - - - - - - - - - -
# What Color?
# Using the following code, select and print the value 'blue' from the car object:

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# print(car['color'])

# - - - - - - - - - - - - - -
# What's My Length?
# Calculate and print the number of key/value pairs in the following dictionary:

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# print(len(car))

# - - - - - - - - - - - - - -
# Checking Key Existence
# Check whether the keys 'name' and 'grade' exist in the following dictionary:

# student = {
#     'id': 123,
#     'grade': 'B',
# }

# print(student.get('name'))
# print(student.get('grade'))

# print('name' in student)
# print('grade' in student)

# - - - - - - - - - - - - - -
# Multiple Cars
# Create a nested dictionary that contains the following data.

# Car
# type	color	year
# sedan	blue	2003

# Truck
# type	color	year
# pickup	red	1998

# vehicles = {
#     'car': {
#         'type':  'sedan', 
#         'color': 'blue',
#         'year':  2003,
#     },

#     'truck': {
#         'type': 'pickup', 
#         'color': 'red',
#         'year': 1998,

#     },
# }

# print(vehicles)
# print(vehicles['car']['type'])
# print(vehicles['truck']['year'])

# - - - - - - - - - - - - - -
# Which Collection?
# Rewrite car as a list of lists in which each nested list 
# contains two elements that represent the corresponding 
# key/value pairs.

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# car_lst = [
#     ['type', 'sedan'],
#     ['color', 'blue'],
#     ['year', 2003],
# ]

# print(car)
# print(car_lst)

# - - - - - - - - - - - - - -
# Divided by Two
# Use a for loop to iterate over the numbers dictionary and 
# return a list containing each number divided by 2 as an integer. 
# The result should be truncated to an integer. Assign the returned 
# list to a variable named half_numbers and print its value using print.

# use //

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }

# half_numbers = []

# for val in numbers.values():
#     half_numbers.append(val // 2)

# print(half_numbers)

# as a list comprehension

# half_numbers = [
#     val // 2
#     for val in numbers.values()
# ]

# print(half_numbers)

# - - - - - - - - - - - - - -
# Labeled Numbers
# Use a for loop to iterate over the numbers dictionary and 
# print each element's key/value pair.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

# Expected output
# A high number is 100.
# A medium number is 50.
# A low number is 10.

for key, val in numbers.items():
    print(f'A {key} number is {val}.')

# - - - - - - - - - - - - - -