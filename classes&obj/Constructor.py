# new method 

class ClassName:
    def __new__(cls, parameter):
        instance = super(ClassName,cls).__new__(cls)
        return instance
    

# __init__ method

class ClassName:
    def __init__(self, parameters):
        self.attribute = value
        
        
        
        
        
# defult Constructor 

class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2000

car = Car()
print(car.make)
print(car.model)
print(car.year)

# parameterized Constructor

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

car = Car("Honda","Civic", 2025)
print(car.make,car.model,car.year)