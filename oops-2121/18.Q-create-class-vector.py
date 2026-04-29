"""1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
6. Write __str__() method to print the vector as follows: 7i + 8j +10k
Assume vector of dimension 3 for this problem.
7. Override the __len__() method on vector of problem 5 to display the dimension of the vector."""


class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j ")    
       
class ThreeDvector(TwoDvector):
    def __init__ (self,i,j,k):
        super().__init__ (i,j) 
        self.k = k    
        
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j +{self.k}k")      
        
a= TwoDvector(1,2)
b = ThreeDvector(1,2,3) 
a.show()
b.show() 
         