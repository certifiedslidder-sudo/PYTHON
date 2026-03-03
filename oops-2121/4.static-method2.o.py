class Employee:
    language="py"   
    salary=1200000
    
    def getnInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
    @staticmethod      #decorator
    def greet():   #GREET KO PASS KR DIA BINA OBJ DIE.
        print("good morning cuties")
        
harry=Employee()
#harry.language = "java script"
harry.greet()
harry.getnInfo()