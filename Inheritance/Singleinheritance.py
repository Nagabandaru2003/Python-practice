class Person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber

class Employee(Person):
    def __init__(self, name, idnumber,salary):
        super().__init__(name, idnumber)
        self.salary = salary

emp = Employee('naga',220,400000)
print(emp.name,emp.idnumber,emp.salary)