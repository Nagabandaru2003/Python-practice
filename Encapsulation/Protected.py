class Protected:
    def __init__(self):
        self._age = 30

class Subclass(Protected):
    def display_age(self):
        print(self._age)
obj = Subclass().display_age()
