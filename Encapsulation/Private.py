class Private:
    def __init__(self):
        self.__salary = 50000
    
    def salary(self):
        return self.__salary

obj = Private()
print(obj.salary())