#!/usr/bin/python3

#############################################################################
# 🐍 Non-primitive Inbuilt Python Data Structures with Reporty the Python 😀 #
#############################################################################

##################################################################
# Some short and basic notes just to get you started.            #
# This is neither exhaustive, nor systematic guide for Python 3! #
# Compiled from open resources and practical experience          #
# by Dimitar D. Mitov - Reporty the Python - ddmitov@gmail.com   #
##################################################################

# This document is written in Visual Studio Code.
# All examples here require only vanilla Python 3.

# Type 'python' or 'python3' in any terminal,
# paste and execute the following code snippets by
# pressing Enter once for single-line statements or
# twice for multi-line statements.

#################
# Python Tuples #
#################

# 1. Definition: #
##################

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is:

# 1. ordered,
# 2. unchangeable and
# 3. allows duplicates.

# Tuples are written with round brackets.

animals_tuple = (
    'Grizzly',
    'Wolfie',
    'Foxie',
    'Mickie Mouse',
    'Minie Mouse',
    'Stuart Little'
)

# 2. Get the number of elements in a tuple: #
#############################################

print(len(animals_tuple))
# 6

# 3. Check if an element is in a tuple: #
#########################################

print('Grizzly' in animals_tuple)
# True

print('Tiger' in animals_tuple)
# False

# 4. Access an element in a tuple: #
####################################

print(animals_tuple[0])
# Grizzly

# 5. Access a range of elements in a tuple: #
#############################################

print(animals_tuple[1:3])
# ('Wolfie', 'Foxie')

# 6. Unpack a tuple: #
######################

name1, name2, name3, name4, name5, name6 = animals_tuple

print(name1)
# Grizzly

print(name2)
# Wolfie

# 7. Join two tuples: #
#######################

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple1 + tuple2)
# (1, 2, 3, 4, 5, 6)

# 8. Multiply a tuple: #
########################

print(tuple1 * 2)
# (1, 2, 3, 1, 2, 3)

# 9. Convert a tuple to a list: #
#################################

print(list(animals_tuple))
# ['Grizzly', 'Wolfie', 'Foxie', 'Mickie Mouse', 'Minie Mouse', 'Stuart Little']

# 10. Convert a list to a tuple: #
##################################

print(tuple(['Grizzly', 'Wolfie', 'Foxie']))
# ('Grizzly', 'Wolfie', 'Foxie')

# 11. Tuple comprehension: #
############################

# Python does not directly support tuple comprehension like it does for lists.
# However, you can use the tuple() function in combination with
# a generator expression to achieve similar results.

# Define the input range:
numbers = range(1, 6)

# Use tuple comprehension (via generator expression):
squared_numbers = tuple(x**2 for x in numbers)

print(squared_numbers)
# (1, 4, 9, 16, 25)

############
# Sources: #
############

# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_ref_tuple.asp
# https://stackoverflow.com/questions/582336/how-do-i-profile-a-python-script
# https://cloud.sambanova.ai/
