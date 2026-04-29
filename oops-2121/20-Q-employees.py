#3. Create a class ‘Employee’ and add salary and increment properties to it.

class employee:
    def __init__(self,salary,increment):
        self.salary = salary
        self.increment = increment
        
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,increment):
        self.increment = increment
e = employee(50000, 5000) 
print(e.salary)   
print(e.salaryAfterIncrement)