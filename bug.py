def my_function(x):
    if x == 0:
        return 0
    else:
        return my_function(x - 1) + x

print(my_function(5)) #This will work correctly
print(my_function(1000)) #This will cause a RecursionError