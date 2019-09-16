"""
    Filter, Map, Reduce exercises

    filter() takes a function and list as arguments
    - filter returns a list of filtered items based on the lambda function
        ex:
        filter(lambda function, list)

    map() takes a function and list as arguments
    - map returns a list of modified items based on the lambda function
        ex:
        map(lambda function, list)

    reduce() takes a function and list as arguments
    - reduce performs a repetitive operation over all the elements in the list
    - reduce needs to be imported from functools
        ex: 
        reduce(lambda function, list)
"""

from functools import reduce

# defining our list
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
print('orginal list: ', li)

# filter example - find all the odd numbers inlist
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print('filtered list - odd numbers: ', final_list) 

# map example - double all numbers
final_list = list(filter(lambda x: (x*2), li))
print('mapped list - doubled numbers: ', final_list)

# reduce example - sum all numbers
result = reduce((lambda x, y: x + y), li)
print('reduced list - sum of all: ', result)
