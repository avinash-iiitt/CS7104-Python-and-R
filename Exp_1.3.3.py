'''
Date: 06.09.2024
Author: Avinash Singh
Title: Create a dictionary and store information about a person (name, age, 
and city). Add a key-value pair to the existing dictionary and delete the same.
'''

#%%

# creating a dictionay

person = {}

numPer = int(input("Enter the number of people you want to add to the dictionary: "))

for i in range(numPer):
    pName = input("Enter person name: ")
    pAge = int(input("Enter person age: "))
    pCity = input("Enter person city: ")
    person[pName] = [pAge, pCity]
    
print(person)

ck = input("Do you want to delete a record(y/n): ")


if( ck == 'y' or ck == 'Y'):
    delval = input("Enter the person Name to delete: ")
    person.pop(delval)
    

print(person)