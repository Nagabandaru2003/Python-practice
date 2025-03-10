# li = [1,2,3,4,5]
# def even(ele):
#     return ele%2 == 0

# nemli = list(filter(even,li))
# print(nemli)
from functools import reduce
li = [1,2,3,4,5,6,7,8,9]
newli = list(filter(lambda num:num%2 == 0,li))
#sum = list(reduce(lambda num:num%2 == 0,li))
def sum(a,b):
    return
print(newli)