class Employee:
    language="py"   
    salary=1200000
    
    def getnInfo(self):   #self is imp...
        print(f"the language is {self.language}. the salary is {self.salary}")
        
    def greet(self):
        print("good morning cuties")
        
harry=Employee()
#harry.language = "java script"
#harr=Employee()
#harr.language = "java"
#harr.getnInfo()
harry.greet()
harry.getnInfo()

#Employee.getnInfo(harry)
#Employee.getnInfo()