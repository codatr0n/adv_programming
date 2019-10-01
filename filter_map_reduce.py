"""
    Filter, Map, Reduce exercises

    filter() takes a function and list as arguments
    - filter returns a list of filtered items based on the lambda function
    - wrap the filter object in a list function
        ex:
        list(filter(lambda function, list))

    map() takes a function and list as arguments
    - map returns a list of modified items based on the lambda function
    - wrap the map object in a list function
        ex:
        list(map(lambda function, list))

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

print('')

# more lambda examples

# list of dictionaries with programming languages and frameworks
# framework is empty for language main name
programming_lanuages = [
    {'language': 'python', 'framework': 'flask'}, 
    {'language': 'python', 'framework': 'django'}, 
    {'language': 'python', 'framework': ''}, 
    {'language': 'php', 'framework': 'laravel'},
    {'language': 'php', 'framework': 'symfony'},
    {'language': 'php', 'framework': ''},
    {'language': 'php', 'framework': 'codeigniter'},
    {'language': 'javascript', 'framework': 'react'},
    {'language': 'javascript', 'framework': 'angular'},
    {'language': 'javascript', 'framework': ''},
    {'language': 'javascript', 'framework': 'vue'},
    {'language': 'javascript', 'framework': 'nodejs'},
    {'language': 'java', 'framework': 'blade'},
    {'language': 'java', 'framework': ''},
    {'language': 'java', 'framework': 'spark'},
    {'language': 'java', 'framework': 'spring'},
    {'language': 'ruby', 'framework': 'rails'},
    {'language': 'swift', 'framework': ''},
    {'language': 'go', 'framework': ''},
    {'language': 'c#', 'framework': ''},
    {'language': 'c#', 'framework': 'asp.net'},
]

##############################################################################
# FIND ALL LANGUAGE NAMES AND PRINT THEM
##############################################################################
# first operation returns a filtered list of entries where framework is empty
languages = list(filter(lambda x: x['framework'] =='', programming_lanuages))
# output: [{'language': 'python', 'framework': ''}, {'language': 'php', 'framework': ''}, {'language': 'javascript', 'framework': ''}, {'language': 'java', 'framework': ''}, {'language': 'swift', 'framework': ''}, {'language': 'go', 'framework': ''}, {'language': 'c#', 'framework': ''}]
# second operations returns a list with the language name extraxted from
# the dictionary and joins the list to a comma separeted string
print('List of all programming languages:')
print(', '.join(list(map(lambda x: x['language'], languages)))) 
# output: python, php, javascript, java, swift, go, c#

##############################################################################
# FIND ALL FRAMEWORK NAMES AND PRINT THEM IN UPPER CASE
##############################################################################
# first operation returns a list of frameworks in uppercase
frameworks_upper = list(map(lambda x : x['framework'].upper(),  programming_lanuages))
# output: ['FLASK', 'DJANGO', '', 'LARAVEL', 'SYMFONY', '', 'CODEIGNITER', 'REACT', 'ANGULAR', '', 'VUE', 'NODEJS', 'BLADE', '', 'SPARK', 'SPRING', 'RAILS', '', '', '', 'ASP.NET']
# second operation returns a filtered list with empty entries omitted
# and prints it as a joined comma separated string
print('\nList of all frameworks in UPPER CASE:')
print(', '.join(list(filter(lambda x: x != '', frameworks_upper)))) 
# Output: FLASK, DJANGO, LARAVEL, SYMFONY, CODEIGNITER, REACT, ANGULAR, VUE, NODEJS, BLADE, SPARK, SPRING, RAILS, ASP.NET

##############################################################################
# FIND ALL FRAMEWORKS RELATED TO JAVASCRIPT
##############################################################################
# first operation returns a list of entries where language is javascript
# and framework is not empty
js_frameworks = list(filter(lambda x: x['language'] == 'javascript' and x['framework'] != '', programming_lanuages))
# output: [{'language': 'javascript', 'framework': 'react'}, {'language': 'javascript', 'framework': 'angular'}, {'language': 'javascript', 'framework': 'vue'}, {'language': 'javascript', 'framework': 'nodejs'}]
# second operation extracts the framework names in a list and joins it to
# a comma separated string
print('\nList of Javascript related frameworks:')
print(', '.join(list(map(lambda x: x['framework'], js_frameworks))))
# output: react, angular, vue, nodejs


##############################################################################
# WORKING WITH LISTS OF DICTIONARIES - MAPPING AND FILTERING
##############################################################################

solutions = [{'algo': 'dfs', 'route': [], 'steps': [], 'time': 2.22},
             {'algo': 'dfs', 'route': [], 'steps': [], 'time': 1.32},
             {'algo': 'dfs', 'route': [], 'steps': [], 'time': 1.62},
             {'algo': 'dfs', 'route': [], 'steps': [], 'time': 0.72},
             {'algo': 'dfs', 'route': [], 'steps': [], 'time': 1.72},
             {'algo': 'a*', 'route': [], 'steps': [], 'time': 1.85},
             {'algo': 'a*', 'route': [], 'steps': [], 'time': 1.12},
             {'algo': 'a*', 'route': [], 'steps': [], 'time': 1.34},
             {'algo': 'a*', 'route': [], 'steps': [], 'time': 0.62},
             {'algo': 'a*', 'route': [], 'steps': [], 'time': 0.95}]

# lambda function filters the list based on the algo input
# algo = 'dfs' will return all solutions for DFS solver
algo = 'dfs'
result = list(filter(lambda x: algo in x['algo'], solutions))

# second lambda function filters the list of dicts based on algo input
# filtered list is passed to the first map lambda function
# which returns all the values of the time key
algo = 'a*'
result = list(map(lambda x: x['time'], filter(lambda x: algo in x['algo'], solutions)))
