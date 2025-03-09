class Naga:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def diaplayAge(self):
        print("Age:",self.age)
        
obj = Naga("naga",21)
obj.diaplayAge()
print("List of Fields and methods inside onj:",dir(obj))
print("Name:",obj.name)
obj.diaplayAge()