class Employee:
    language="py"    
    salary=1200000
    greeting="have a nice day"
    day="sunday"
    
    def getInfo(self):   #self is imp...
        print(f"the language is {self.language}. the salary is {self.salary}")
        
    def greet(self):
        print("good morning guyz") 
        print(f"the greeting of the day is {self.greeting} and today is {self.day}")   
       
harry = Employee()
harry.language = "javascript" 
harry.greeting= "good evening"
harry.day="saturday"
harry.getInfo()
harry.greet()    
Employee.getInfo(harry)       