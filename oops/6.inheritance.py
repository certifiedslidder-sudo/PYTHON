class Employee:
    def __init__(self, name, id):
        self.name= name
        self.id = id
    def showDetails(self):
        print(f" the name of employee: {self.id} is {self.name}")

class Programmer(Employee):     
    def showLanguage(self):
        print("the default language is python")      
e1 = Employee("neeraj sanwal" , 420)        
e1.showDetails()
e2 = Programmer("neer sanwal" , 400)  
e2.showDetails()      
e2.showLanguage()
#e2.showLanguage()  
# AttributeError: 'Employee' object has no attribute 'showLanguage'
# e2.Programmer("sanwal neeraj" , 440)
# e2.showLanguage()
'''INHERITANCE'''  #when a class derives from another class. the child class will inherit all the public and protected properties and methods from the parent class. it can have its own properties and methods.
"TYPES OF INHERITANCE"    #single inheritance
                          #multiple inheritance     
                          #multilevel inheritance
                          #hierarchical inheritance
                          #hybrid inheritance 
'''SYNTAX'''                          
# class BaseClass:    
#     Body of base class
# class DerivedClass(BaseClass):
#     Body of derived class    