#Create a class “Programmer” for storing information of few programmers working at Microsoft.


class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name= name
        self.salary=salary
        self.pin=pin
        
h=Programmer("harry",12000,609)        
print(h.name, h.salary, h.pin, h.company)

s=Programmer("sneha",140000,356)        
print(s.name, s.salary, s.pin, s.company)

n=Programmer("neearj",145000,5798)        
print(n.name, n.salary, n.pin, n.company)

a=Programmer("aarav",14500,3296)        
print(a.name, a.salary, a.pin, a.company)

p=Programmer("priya",145000,3567)        
print(p.name, p.salary, p.pin, p.company)

i=Programmer("ira",149000,30234)        
print(i.name, i.salary, i.pin, i.company)