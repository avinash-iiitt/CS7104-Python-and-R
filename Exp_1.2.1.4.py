# Date: 30.08.2024
# Author: Avinash Singh
# Title: To Perform Logical Operations

#%%
a=10
b=20
c=2
print("\na=10\nb=20\nc=2\n")
expression=(a>b) and (b>c)
print("(a>b) and (b>c) is ",expression)
expression=(a>b) or (b>c)
print("(a>b) or (b>c) is ",expression)
expression=not ((a>b) or (b>c))
print("not ((a>b) or (b>c)) is ",expression)