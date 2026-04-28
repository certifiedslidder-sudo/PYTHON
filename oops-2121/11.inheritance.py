class Employee:              #base or parent class
    company = "ITC"
    def show(self):
        print(f"the name of the employee is: {self.name} abd his salary is {self.salary}")
  #making multiple class from a class  is error prone as if we are needed to edit it , it may cause some trouble.
  
        
# class Programmer:
#     company="ITC infotech"
#     language="py"
#     def showLanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language.")
        
class Programmer(Employee): #derived class (programmer) or child class from  base class (employee)
    company="infosys"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language.")
                
a=Employee()    #object
b =Programmer()    #another object

print(a.company,b.company)            