class Father():
    def show(self):
        print("In Father")

class Mother():
    def display(self):
        print("In Mother")


class Child(Father,Mother):
    def show(self):
        print("In Child")

obj = Child()
obj.show()
obj.display()
    
    
    