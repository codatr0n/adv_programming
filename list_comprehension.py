# return a sorted list with numbers first, then letters
my_list = [1, 3, 2, "b", "a", "c"]

from itertools import chain

numbers = sorted([x for x in my_list if type(x) == int])
letters = sorted([x for x in my_list if type(x) == str])

for i in chain(numbers, letters):
    print(i)

