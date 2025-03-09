class Naga:
    __name = None
    __roll = None
    __branch = None

    def __init__(self,name,roll,branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch
        
    def __displayDetails(self):
        print("Name:", self.__name)
        print("Roll: ",self.__roll)
        print("Branch:",self.__branch)
        
    def accessPrivateFunction(self):
        self.__displayDetails()
        
obj = Naga("naga",220,"EEE")
print(dir(obj))
print(obj._Naga__name)
print(obj._Naga__roll)
print(obj._Naga__branch)
obj._Naga__displayDetails()
obj.accessPrivateFunction()


        