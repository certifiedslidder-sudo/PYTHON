class Employee:               
    company = "ITC"
    name="sneha"
    def show(self):
        print(f"the name of the employee is: {self.name} and her company is {self.company}")
 
class Coder:
    language="java script"
    def printLanguages(self):
        print(f"out of all the languages {self.language} is my favourite language.") 
        
class Programmer(Employee, Coder):  #MULTIPLE-INHERITANCE      
    company="infosys"
    def showLanguage(self):
        print(f"the name is {self.company} and she is good with {self.language} language.")

class assist(Programmer,Employee,Coder):#MULTI-LEVEL INHERITANCE
    
    
    
#class assist(Employee,Coder,Programmer):  gives MRO AS I GAVE EMPLOYER PRIORITY THAN PROGRAMMER AND I AM CREATING A CONFLICTING INHERITANCE PATH BNY PASSING EMPLOYEE AND CODER BEFORE PROGRAMMER AS CODER IS DERIVERED FROM THOSE TWO  FOLLWED BY ASSIST;;; ASSIST  IS DERIVED FROM PROGRAMMER.    


    company = "git"
    stipned = "12000"
    language = "c++"
    name = "bhoomika"
    def myjob(self):
        print(f" hi i am {self.name} and the company in which i am currently working as an intern is {self.company} and my stipned is {self.stipned} ")
                
                
a=Employee()
b =Programmer()  
c = assist() 
b.show()  
b.showLanguage()
b.printLanguages()
c.myjob()
c.show()
c.showLanguage()
c.printLanguages()