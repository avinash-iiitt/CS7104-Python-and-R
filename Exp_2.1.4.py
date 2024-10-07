'''
Date: 06.09.2024
Author: Avinash Singh
Title: Modify the ‘Car’ class to include a ‘year’ attribute. Use the ‘__init__’ method to initialize all attributes
when an object is created. Further, add a ‘__str__’ method to the ‘Car’ class to return a string representation
of the object. Lastly, add a class method named ‘total_cars’ to track the number of ‘Car’ objects created.
'''
#%%

# Creating a class Car
class Car:
    make = 2025 # Initializing attribute make
    model = "Civic" # Initializing attribute model
    engine_state = True # Setting value for engine_state
    year = 2025
    tot_cars = 0
    
    # Creating init dender function
    def __init__(self, make, model, engine_state, year):
        self.make = make
        self.model = model
        self.engine_state = engine_state
        self.year = year
        Car.tot_cars += 1
    # Creating the str dender function
    def __str__(self):
        return "[ Make: {}, Model: {}, Engine_State: {}, Year: {}]".format( self.make, self.model, self.engine_state, self.year)
    
    # Creating a method start engine
    def start_engine():
        if (Car.engine_state):
            print("The Car's Engine Has Started !")
        else:
            print("The Car's Engine Is Idle !")
    
    # Creating a method total cars that tracks the total no. of objects created
    def total_cars():
        print("Total Number of Cars are {}.".format(Car.tot_cars))
  

# Calling the init dunder function
obj1 = Car(2025, "Civic", True, 2025) # Creating object for Class Car
obj2 = Car(2024, "Sedan", False, 2024) # Creating object for Class Car

# Calling the str dunder function
print( Car.__str__(obj1))
print( Car.__str__(obj2))

# Calling total_cars function
Car.total_cars()