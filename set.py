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

###############
# Python Sets #
###############

# 1. Definition: #
##################

# Sets are used to store multiple items in a single variable.
# A set is a collection which is:

# 1. unordered,
# 2. unchangeable and
# 3. does not allow duplicates.

# Sets are written with curly brackets.

animals_set = {
    'Grizzly',
    'Wolfie',
    'Foxie',
    'Mickie Mouse',
    'Minie Mouse',
    'Stuart Little'
}

# 2. Get the number of elements in a set: #
###########################################

print(len(animals_set))
# 6

# 3. Check if an element is in a set: #
#######################################

print('Grizzly' in animals_set)
# True

print('Tiger' in animals_set)
# False

# 4. Add an element to a set: #
###############################

animals_set.add('Tiger')

print(animals_set)

# {
#     'Grizzly',
#     'Wolfie',
#     'Foxie',
#     'Mickie Mouse',
#     'Minie Mouse',
#     'Stuart Little',
#     'Tiger'
# }

# 5. Add multiple elements to a set: #
######################################

animals_set.update({
    'Lion',
    'Elephant',
    'Giraffe'
})

print(animals_set)

# {
#     'Grizzly',
#     'Wolfie',
#     'Foxie',
#     'Mickie Mouse',
#     'Minie Mouse',
#     'Stuart Little',
#     'Tiger',
#     'Lion',
#     'Elephant',
#     'Giraffe'
# }

# 6. Remove an element from a set: #
####################################

animals_set.remove('Foxie')

print(animals_set)

# {
#     'Grizzly',
#     'Wolfie',
#     'Mickie Mouse',
#     'Minie Mouse',
#     'Stuart Little',
#     'Tiger',
#     'Lion',
#     'Elephant',
#     'Giraffe'
# }

# 7. Remove an element from a set without raising an error: #
#############################################################

animals_set.discard('Tiger')

print(animals_set)

# {
#     'Grizzly',
#     'Wolfie',
#     'Mickie Mouse',
#     'Minie Mouse',
#     'Stuart Little',
#     'Lion',
#     'Elephant',
#     'Giraffe'
# }

# 8. Clear a set: #
###################

animals_set.clear()

print(animals_set)
# set()

# 9. Union of two sets: #
#########################

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
# {1, 2, 3, 4, 5}

# 10. Intersection of two sets: #
#################################

print(set1.intersection(set2))
# {3}

# 11. Difference of two sets: #
###############################

print(set1.difference(set2))
# {1, 2}

# 12. Symmetric difference of two sets: #
#########################################

print(set1.symmetric_difference(set2))
# {1, 2, 4, 5}

# 13. Profiling set operations for speed comparison: #
######################################################

# In the following case,
# checking if an element is in a set is faster
# than checking if an element is in a list.

import cProfile

test_set = set(range(0, 1000000))
test_list = list(range(0, 1000000))

cProfile.run(
'''
1000000 in test_set
'''
)

# 2 function calls in 0.000 seconds

cProfile.run(
'''
1000000 in test_list
'''
)

# 2 function calls in 0.013 seconds

# 14. Set comprehension: #
##########################

# Create a list of numbers:
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Use set comprehension to create a set of squares of even numbers:
even_squares = {num ** 2 for num in numbers if num % 2 == 0}

print(even_squares)
# {4, 16, 36}

############
# Sources: #
############

# https://www.w3schools.com/python/python_sets.asp
# https://www.w3schools.com/python/python_ref_set.asp
# https://stackoverflow.com/questions/582336/how-do-i-profile-a-python-script
# https://cloud.sambanova.ai/
