#!/usr/bin/python3

######################################################
# 🐍 Become a Green Snake with Reporty the Python 😀 #
######################################################

#########################################################################
# Some short, basic and work-in-progress notes just to get you started. #
# This is neither exhaustive, nor systematic guide for Python 3!        #
# Compiled from open online resources and practical experience          #
# by Dimitar D. Mitov - Reporty the Python - ddmitov@gmail.com          #
#########################################################################

# This document is written in Visual Studio Code.
# All examples here require only vanilla Python 3 with core modules.
# Type 'python' or 'python3' in any terminal,
# paste and execute the following code snippets by
# pressing Enter once for single-line statements or
# twice for multi-line statements.

##############################
# Python List Comprehensions #
##############################

animals = ['Grizzly', 'Wolfie', 'Foxie']

# 1. Change all elements to upper case - iteration:
###################################################

uppercase_animals = []

for animal in animals:
    uppercase_animals.append(animal.upper())

print(uppercase_animals)

# Output:
# ['GRIZZLY', 'WOLFIE', 'FOXIE']

# 1. Change all elements to upper case - list comprehension:
############################################################

uppercase_animals = [animal.upper() for animal in animals]

print(uppercase_animals)

# Output:
# ['GRIZZLY', 'WOLFIE', 'FOXIE']

# 2. Change all elements to upper case with a condition - iteration:
####################################################################

conditional_uppercase_animals = []

for animal in animals:
    if 'Wolfie' in animal or 'Foxie' in animal:
        conditional_uppercase_animals.append(animal.upper())

print(conditional_uppercase_animals)

# Output:
# ['WOLFIE', 'FOXIE']

# 2. Change all elements to upper case with a condition - list comprehension:
#############################################################################

conditional_uppercase_animals = [
    animal.upper() for animal in animals
    if 'Wolfie' in animal or 'Foxie' in animal
]

print(conditional_uppercase_animals)

# Output:
# ['WOLFIE', 'FOXIE']

# 3. Find all even numbers using iteration and modulo:
######################################################

# List of numbers from 1 to 10 inclusive:
numbers = list(range(1, 11))

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# Output:
# [2, 4, 6, 8, 10]

# 3. Find all even numbers using
#    list comprehension, lambda function and filter:
####################################################

# List of numbers from 1 to 10 inclusive:
numbers = list(range(1, 11))

# Simpler list comprehension without lambda function and filter:
even_numbers_01 = [number for number in numbers if number % 2 == 0]

print("even_numbers_01:" + str(even_numbers_01))

# Output:
# [2, 4, 6, 8, 10]

# List comprehension with filter and a named function, but no lambda function:
def is_even(x):
    return x % 2 == 0

even_numbers_02 = list(filter(is_even, numbers))

print("even_numbers_02:" + str(even_numbers_02))

# Output:
# [2, 4, 6, 8, 10]

# The full version with list comprehension, lambda function and filter:
even_numbers_03 = list(filter(lambda number: number % 2 == 0, numbers))

print("even_numbers_03:" + str(even_numbers_03))

# Output:
# [2, 4, 6, 8, 10]

# 3. Get all squared numbers using iteration:
#############################################

# List of numbers from 1 to 10 inclusive:
numbers = list(range(1, 11))

squared_numbers = []

for number in numbers:
    squared_numbers.append(number * number)

print(squared_numbers)

# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 3. Get all squared numbers using list comprehension and map:
##############################################################

# List of numbers from 1 to 10 inclusive:
numbers = list(range(1, 11))

squared_numbers = list(map(lambda number: number * number, numbers))

print(squared_numbers)

# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Sources:
# https://indhumathychelliah.com/2020/07/22/list-set-dictionary-comprehensions-in-python/
# https://towardsdatascience.com/my-trick-to-learning-list-comprehensions-in-python-8a54e66d98b
