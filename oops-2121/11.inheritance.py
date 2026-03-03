class Employee:              #base or parent class
    company = "ITC"
    def show(self):
        print(f"the name of the employee is: {self.name} abd his salary is {self.salary}")
        
# class Programmer:
#     company="ITC infotech"
#     language="py"
#     def showLanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language.")
        
class Programmer(Employee):          #derived or child class
    company="infosys"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language.")
                
a=Employee()
b =Programmer()   

print(a.company,b.company)            