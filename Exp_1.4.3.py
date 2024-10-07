'''
Date: 06.09.2024
Author: Avinash Singh
Title: Create two functions and compose them to manually perform a square followed by an increment by
stepsize 1.
'''

#%%

# Declaring a function to calculate the square of the number
def square(x):
    return x ** 2

# Declaring a function to increment the value of squared num by 1
def increment(x):
    return x + 1

# Declaring a function to call both the function
def square_and_inc1(val):
    sqVal = square(val)
    incVal = increment(sqVal)
    return incVal
# Calling square_and_inc1 and printing the value
result = square_and_inc1(3)
print(result)
