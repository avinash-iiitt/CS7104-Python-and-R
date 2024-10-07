# Date: 30.08.2024
# Author: Avinash Singh
# Title: To perform Arithematic Operations

#%%
a=5
b=10
c=2
result=(a+b)
print("Addition of ",a, "and ",b, "is ",result)
result=(b-a)
print("Subtraction of ",b, "and ",a, "is ",result)
result=(a*b)
print("Multiplication of ",a, "and ",b, "is ",result)
result=(b/c)
print("Division of ",b, "by ",c, "is ",result)
result=(b%c)
print("Remainder of ",b, "by ",c, "is ",result)
result=(a**b)
print(a, "raised to the power ",b, "is ",result)
expression=((a+b)*(a-b))/((a%c)+(a**c))
print("result of expression - ((a+b)*(a-b))/((a%c)+(a**c)) is",expression)

