'''
Date: 06.09.2024
Author: Avinash Singh
Title: Implement a recursive function to calculate the factorial for a given number
'''

#%%

#funtion for calculating the factorial
def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)


# Getting the number from the user and calling the fact function
num = int(input("Enter number to find the factorial: "))
result = fact(num)

# Displaying the number and it's factorial
print("factorial of {} is {}.".format( num, result))