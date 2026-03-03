class Employee:              
    company = "ITC"
    name="sneha"
    def show(self):
        print(f"the name of the employee is: {self.name} and his company is {self.company}")
 
class Coder:
    language="java script"
    def printLanguages(self):
        print(f"out of all the languages {self.language} is your language.") 
        
class Programmer(Employee, Coder):        
    company="infosys"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language.")
                
a=Employee()
b =Programmer()   
b.show()
b.showLanguage()
b.printLanguages()