#Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f"the square of {self.n} is {self.n*self.n}") 
          
    def cube(self):
        print(f"the cube of {self.n} is {self.n*self.n*self.n}")     
         
    def squareroot(self):
        print(f"the squareroot of {self.n} is {self.n**1/2}")     
        
a= Calculator(5)  
a.square()
a.cube()
a.squareroot()

b= Calculator(1)  
b.square()
b.cube()
b.squareroot()
c= Calculator(50000)  
c.square()
c.cube()
c.squareroot()

c= Calculator(0)  
c.square()
c.cube()
c.squareroot()