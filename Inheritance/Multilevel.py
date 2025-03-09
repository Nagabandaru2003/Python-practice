class Parent():
    def display(self):
        print("Parent Class")
    def mom(self):
        print('MOM & Dad is a Weavers')
        
class Child(Parent):
    def show(self):
        print('child class')

class GrandChild(Child):
    def show(self):
        print('Grandchild class')
        
g = GrandChild()
g.show()
g.display()
g.mom()