class Employee:
    def __init__(self):
        print("constructor of Employee")
    a=1
class Programmer(Employee):
    def __init__(self):
        print("constructor of Programmer")
    b=2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("constructor of Manager")
    c=3
    
# o=Employee()  
# print(o.a)  
#print(o.b) AttributeError: 'Employee' object has no attribute 'b'

# o=Programmer()
# print(o.a)
# print(o.b)
#print(o.c)     AttributeError: 'Programmer' object has no attribute 'c

o=Manager()
print(o.a)
print(o.b)
print(o.c) 