'''
Date: 06.09.2024
Author: Avinash Singh
Title: Add a method ‘start engine’ to the ‘Car’ class that prints a message indicating that the car’s engine has
started.
'''
#%%

# Creating a class Car
class Car:
    make = 2025 # Initializing attribute make
    model = "Civic" # Initializing attribute model
    engine_state = True # Setting value for engine_state
    
    # Creating a method start engine
    def start_engine():
        if (Car.engine_state):
            print("The Car's Engine Has Started !")
        else:
            print("The Car's Engine Is Idle !")
        

objects = Car() # Creating object for Class Car

# Calling the start engine function
Car.start_engine()