#!/usr/bin/python3

#####################################################
# 🐍 Become a Green Snake with Reporty the Python 😀 #
#####################################################

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

################
# Python Lists #
################

# 1. Definition:
################
# The list is a data structure in Python
# containing a sequence of elements which are:

# 1. changeable and
# 2. ordered.

# Any Python list may have elements with different types:
############################################################

heterogenous_list = [1, 2, 3, 'one', 'two', 'three']

for element in heterogenous_list:
    print(element)

# 1
# 2
# 3
# one
# two
# three

animals = ['Grizzly', 'Wolfie', 'Foxie']

# 3. Iteration:
###############
# The indentation is important!
# No need to declare the 'animal' variable before this line.

for animal in animals:
    print(animal)

# Grizzly
# Wolfie
# Foxie

# 4. Acess a list element by its index:
#######################################
print(animals[0])

# Grizzly

# 5. Acess a list elements using a negative index:
##################################################
print(animals[-1])

# Foxie

print(animals[-2])

# Output
# Wolfie

# 6. Append an item to a list:
##############################
print("animals object id before append(): " + str(id(animals)))

animals.append('Rabbit')

print("animals object id after append(): " + str(id(animals)))

for animal in animals:
    print(animal)

# Grizzly
# Wolfie
# Foxie
# Rabbit

# 7. Join two lists:
####################
disney_animals = ['Mickey Mouse', 'Minie Mouse']

combined_animals = animals + disney_animals

print("animals object id after append(): " + str(id(animals)))

for animal in combined_animals:
    print(animal)

# Grizzly
# Wolfie
# Foxie
# Rabbit
# Mickey Mouse
# Minie Mouse

# 8. Make a new alphabetically sorted list from an existing list:
#################################################################

sorted_animals = sorted(combined_animals)

for animal in sorted_animals:
    print(animal)

# Grizzly
# Foxie
# Wolfie
# Mickey Mouse
# Minie Mouse
# Rabbit

# 9. Sort alphabetically a list in-place:
#########################################

combined_animals.sort()

for animal in combined_animals:
    print(animal)

# Grizzly
# Foxie
# Wolfie
# Mickey Mouse
# Minie Mouse
# Rabbit

# 10. Check if an item exists in a list:
########################################

if 'Grizzly' in combined_animals:
    print('Grizzly is in the list')

if 'Reporty the Python' not in combined_animals:
    print('Reporty the Python is not in the list.')

# 11. Remove an element from a list:
####################################

combined_animals.remove('Foxie')

print("combined_animals after remove: " + str(combined_animals))
print("combined_animals object id after remove: " + str(id(combined_animals)))

for animal in combined_animals:
    print(animal)

# Grizzly
# Wolfie
# Mickey Mouse
# Minie Mouse
# Rabbit

# 12. Update a list element by index:
#####################################

combined_animals[0] = 'Reporty the Python'

for animal in combined_animals:
    print(animal)

# Reporty the Python
# Wolfie
# Mickey Mouse
# Minie Mouse
# Rabbit

# Source:
# https://indhumathychelliah.com/2020/06/12/an-introduction-to-python-list/
