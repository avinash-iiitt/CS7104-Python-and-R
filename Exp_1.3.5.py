'''
Date: 06.09.2024
Author: Avinash Singh
Title: Create a user-defined function experiment 3 with input arguments as name, age and city, return the
value as “stored successfully” if the statements executes successfully. Create any one local and global
parameter out of this function
'''

#%%

# creating a user-defined function exp3

fee = 1000

def exp3():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    fee = 100
    print("Your tution fee is {} and your exam fee is {}".format(globals()['fee'], fee)) #local and global variable
    return name,age,city

name,age,city = exp3() #calling the function
print("Name: {}, Age: {}, City: {}".format( name, age, city))

