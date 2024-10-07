'''
Date: 06.09.2024
Author: Avinash Singh
Title: Access dictionary values using keys and iterate through the 
dictionary to print all key-value pairs.
'''

#%%

# creating a dictionay

Fruits = {'Apple': 21, 'Mango': 44, 'Banana': 24}

#Accessing values using keys
seaVal = input("Enter the Fruit to know the quantity available: ")
print("The quantity of {} is {}.".format( seaVal, Fruits[seaVal]))

#iterate and print all key and value pairs.
for i in Fruits:
    print("{}: {}".format(i, Fruits[i]))

