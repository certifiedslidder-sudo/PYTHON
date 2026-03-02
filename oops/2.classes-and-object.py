#class is a blueprint for creating object.
#An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation.
'''Objects of a given class can invoke the methods available to it without revealing the implementation details to the user. -->> Abstractions & Encapsulation!'''
class Person:
    name="sneha"
    occupation="software developer"
    networth=10  
    def info(self):  
           
        print(f"{self.name} is a {self.occupation}")
'''self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class,simply wo object jiske lie wo method call kia ja rha hai..''' 

a=Person()
b=Person()
c=Person()
a.name= "bhoomika" 
#print(a.name)   
a.occupation="accountant"
#print(a.name,a.occupation)
b.name="nikita"
b.occupation="farmer"
a.info()
b.info()
c.info()