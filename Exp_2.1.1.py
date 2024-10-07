'''
Date: 06.09.2024
Author: Avinash Singh
Title: Define a simple class named ‘Car’ that has two attributes: ‘make’ and ‘model’. Create instances (objects)
of the ‘Car’ class and display their attributes
'''

#%%

# Creating a class Car
class Car:
    make = 2025 # Initializing attribute make
    model = "Civic" # Initializing attribute model

objects = Car() # Creating object for Class Car

# Displaying the Car's make and model
print("Car's Make: {}, Car's Model: {}.\n".format( objects.make, objects.model))
