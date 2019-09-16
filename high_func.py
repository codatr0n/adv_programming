high_ord_func = lambda x, func: x + func(x)
x = high_ord_func(5, lambda x: x * x) 
print(x)