class Employee:
    language="py"   
    salary=1200000
    
    def __init__(self,name,salary,language): #dunder method:automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating an object")
    
    def getnInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
    @staticmethod      #decorator
    def greet():   #GREET KO PASS KR DIA BINA OBJ DIE.
        print("good morning cuties")
        
harry=Employee("harry", 1300000,"javascript")
# harry.greet()
# harry.name="harry"
print(harry.name,harry.salary,harry.language)
harry.getnInfo()