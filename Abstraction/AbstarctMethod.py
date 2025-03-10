from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        
    @abstractmethod
    def printDetails(self):
        pass
    def accelerate(self):
        print('Speed up....')
    def breack_applied(self):
        print('car stopped..')
    
class Hatchback(Car):
    def printDetails(self):
        print('Brand:',self.brand)
        print('Model:',self.model)
        print('year:',self.year)
    def sunroof(self):
        print('noot having this feature')

class Suv(Car):
    def printDetails(self):
        print('Brand:',self.brand)
        print('Model:',self.model)
        print('year:',self.year)
    def sunroof(self):
        print('Avail...')
        
car1 = Hatchback('maruthi','alto',2022)

car1.printDetails()
car1.accelerate()
car1.sunroof()

             
       