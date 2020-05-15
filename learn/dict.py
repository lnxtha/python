numbers = {'one': 1, 'two': 2, 'three': 3}

# These return dict object that is iterables and can be converted to list by type casting them as list
print(number.keys())

print(number.values())

print(number.items()) 


# Ordered Dictionaries

# Later version of python 3.7 onwards, values saved in dictionaries also save order


# To print keys as a list

print(list(numbers))

# To check if a key exists in a dictionary.

'five' in numbers
# Prints ---> False

# Get Method in dictionary (Similar to NVL in PL Sql)

 picnicItems = {'apples': 5, 'cups': 2} 
 
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.') 
# Prints ---> 'I am bringing 2 cups.' 

print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.' )
# Prints ---> 'I am bringing 0 eggs.'


# setDefault()

numbers.setdefault('six',6) 


# This check if keys named six exists in dictionary. If not inserts six, else returns value of key = six.
