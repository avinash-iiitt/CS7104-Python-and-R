'''
Date: 06.09.2024
Author: Avinash Singh
Title: Create a lambda function to map the square of each number in a list, further, apply a filter using lambda
function to get even numbers. Lastly, calculate the product of all numbers from the obtained list of even
numbers.
'''

#%%
from functools import reduce

# creating a lambda function to map square of each number from 1 to 5
sqlist = list(map( lambda x: x**2, range(1,6,1)))
print(sqlist)

# Filtering the list to get the even numbers
even_num = list(filter(lambda x: x % 2 == 0, sqlist))
print(even_num)

# reducing the list and applying the multiplication on each even num
prod_even = reduce(lambda x, y: x * y, even_num)
print(prod_even)
