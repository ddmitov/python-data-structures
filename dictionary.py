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

#######################
# Python Dictionaries #
#######################

# 1. Definition:
################

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is:

# 1. ordered,
# 2. changeable and
# 3. does not allow duplicates.

# As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are written with curly brackets, and have keys and values.

animals_dictionary = {
    'Grizzly': 'bear',
    'Wolfie': 'wolf',
    'Foxie': 'fox',
    'Mickie Mouse': 'mouse',
    'Minie Mouse': 'mouse',
    'Stuart Little': 'mouse'
}

# 2. Get the value of a key:
############################

print(animals_dictionary.get('Grizzly'))
# bear

print(animals_dictionary['Grizzly'])
# bear

# 3. Get all keys as a list:
############################

print(list(animals_dictionary.keys()))

# [
#     'Grizzly',
#     'Wolfie',
#     'Foxie',
#     'Mickie Mouse',
#     'Minie Mouse',
#     'Stuart Little'
# ]

# 4. Get all values as a list:
##############################

print(list(animals_dictionary.values()))

# [
#     'bear',
#     'wolf',
#     'fox',
#     'mouse',
#     'mouse',
#     'mouse'
# ]

# 5. Get the number of elements in a dictionary:
################################################

print(len(animals_dictionary))
# 6

# 6. Filter dictionary on key using iteration:
##############################################

filtered_dictionary = {}

for key in animals_dictionary.keys():
    if 'Mouse' in key:
        filtered_dictionary[key] = animals_dictionary[key]

print(filtered_dictionary)

# {
#     'Mickie Mouse': 'mouse',
#     'Minie Mouse': 'mouse'
# }

# 7. Filter dictionary on value using iteration:
################################################

filtered_dictionary = {}

for key, value in animals_dictionary.items():
    if 'mouse' in value:
        filtered_dictionary[key] = value

print(filtered_dictionary)

# {
#     'Mickie Mouse': 'mouse',
#     'Minie Mouse': 'mouse'
# }

# 8. Refernce to and copy of a dictionary, update an element in a dictionary:
#############################################################################

animals_dictionary_reference = animals_dictionary

print(animals_dictionary)

# {
#     'Grizzly': 'bear',
#     'Wolfie': 'wolf',
#     'Foxie': 'fox',
#     'Mickie Mouse': 'mouse',
#     'Minie Mouse': 'mouse',
#     'Stuart Little': 'mouse'
# }

print(animals_dictionary_reference)

# {
#     'Grizzly': 'bear',
#     'Wolfie': 'wolf',
#     'Foxie': 'fox',
#     'Mickie Mouse': 'mouse',
#     'Minie Mouse': 'mouse',
#     'Stuart Little': 'mouse'
# }

animals_dictionary_copy = animals_dictionary.copy()

# Two equivalent expressions to update an element in a dictionary:
animals_dictionary_copy['Wolfie'] = 'big bad wolf'
animals_dictionary_copy.update({'Wolfie': 'big bad wolf'})

print(animals_dictionary)

# {
#     'Grizzly': 'bear',
#     'Wolfie': 'wolf',
#     'Foxie': 'fox',
#     'Mickie Mouse': 'mouse',
#     'Minie Mouse': 'mouse',
#     'Stuart Little': 'mouse'
# }

print(animals_dictionary_reference)

# {
#     'Grizzly': 'bear',
#     'Wolfie': 'wolf',
#     'Foxie': 'fox',
#     'Mickie Mouse': 'mouse',
#     'Minie Mouse': 'mouse',
#     'Stuart Little': 'mouse'
# }

print(animals_dictionary_copy)

# {
#     'Grizzly': 'bear',
#     'Wolfie': 'big bad wolf',
#     'Foxie': 'fox',
#     'Mickie Mouse': 'mouse',
#     'Minie Mouse': 'mouse',
#     'Stuart Little': 'mouse'
# }

# Changes in the dictionary are instantly visible in the dictionary reference!
# The copied dictionary is not changed when the original dictionary is changed.

# 9. Remove an element from a dictionary:
#########################################

animals_dictionary.pop('Foxie')

print(animals_dictionary)

# {
#     'Grizzly': 'bear',
#     'Wolfie': 'wolf',
#     'Mickie Mouse': 'mouse',
#     'Minie Mouse': 'mouse',
#     'Stuart Little': 'mouse'
# }

# 10. Clear a dictionary:
#########################

animals_dictionary.clear()

print(animals_dictionary)
# {}

# 11. Profiling dictionary operations for speed comparison:
###########################################################

# In the following case,
# filtering a dictionary on key using dictionary comprehension is faster
# than filtering the same dictionary using iteration.

import cProfile

test_dictionary = {index: 0 for index in range(0, 1000000)}

filtered_dictionary = {}

cProfile.run(
'''
for key in test_dictionary.keys():
    if key == 100000:
        filtered_dictionary[key] = test_dictionary[key]
'''
)

# 4 function calls in 0.049 seconds

cProfile.run(
'''
filtered_dictionary = {
    key: test_dictionary[key] for key in test_dictionary.keys()
    if key == 100000
}
'''
)

# 5 function calls in 0.029 seconds

# Sources:
# https://www.w3schools.com/python/python_dictionaries.asp
# https://www.w3schools.com/python/python_ref_dictionary.asp
# https://stackoverflow.com/questions/582336/how-do-i-profile-a-python-script
