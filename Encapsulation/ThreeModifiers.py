class Super:
    var1 = None
    _var2 = None
    __var3 = None  # Corrected from __var2

    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    def displayPublicMember(self):
        print("Public Data Member:", self.var1)

    def _displayProtectedMember(self):
        print("Protected Data member: ", self._var2)

    def __displayPrivateMember(self):
        print("Private Data Member: ", self.__var3)

    def accessProtectedMember(self):
        self._displayProtectedMember()
        
    def accessPrivateMember(self):
        self.__displayPrivateMember()

class Sub(Super):  # Corrected from super
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    def accessProtectedMember(self):
        self._displayProtectedMember() # Corrected typo and call

obj = Sub("naga", 20, 'bandaru')
obj.displayPublicMember()
obj.accessProtectedMember()
obj.accessPrivateMember()
print()

obj._displayProtectedMember() # Corrected typo
obj._Super__displayPrivateMember() # Corrected typo and call
print()

print("obj is accessing protected member:", obj._var2)
print("obj is accessing private member:", obj._Super__var3)