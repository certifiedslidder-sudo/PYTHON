class Employee:
    a=1
class Programmer(Employee):
    b=2
class Manager(Programmer):
    c=3
    
o=Employee()  
print(o.a)  #prints the attribute a
#print(o.b) AttributeError: 'Employee' object has no attribute 'b'

o=Programmer()
print(o.a)
print(o.b)
#print(o.c)     AttributeError: 'Programmer' object has no attribute 'c

o=Manager()
print(o.a)
print(o.b)
print(o.c) 