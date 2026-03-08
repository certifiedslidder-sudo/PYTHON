"""
Operators in Python can be overloaded using dunder methods.
These methods are called when a given operator is used on the objects.
Operators in Python can be overloaded 
""" 
# __str__()   -->> used to set what gets displayed upon calling str(obj)
#__len__()  --->> used to set what gets displayed upon calling.__len__() or len(obj)
class Number:
    def __init__(self,n):
        self.n= n 
    def __add__(self, num):
        return self.n + num.n
        
n =Number(1)
m = Number(2)
        
print(n+m) #TypeError: unsupported operand type(s) for +: 'Number' and 'Number'

