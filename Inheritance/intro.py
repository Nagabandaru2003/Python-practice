class Animal:
    def __init__(self,name):
        self.name = name
    def Speak(self):
        pass
class Dog(Animal):
    def Speak(self):
        return f"{self.name} barks!"
    
dog = Dog("Ryme")
print(dog.Speak())
 