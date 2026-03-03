#Add a static method in problem 2, to greet the user with hello.
  
#problem2=Write a class “Calculator” capable of finding square, cube and square root of a number.  

class Calculator:
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f"the square of {self.n} is {self.n*self.n}") 
          
    def cube(self):
        print(f"the cube of {self.n} is {self.n*self.n*self.n}")     
         
    def squareroot(self):
        print(f"the squareroot of {self.n} is {self.n**1/2}")    
        
    @staticmethod                #modified line
    def hello():
        print("hello world!!")    
        
a= Calculator(5) 
a.hello()                             #modified line
a.square()
a.cube()
a.squareroot()

b= Calculator(1)  
b.hello()                            #modified line
b.square()
b.cube()
b.squareroot()

c= Calculator(50000)  
c.hello()                            #modified line
c.square()
c.cube()
c.squareroot()
