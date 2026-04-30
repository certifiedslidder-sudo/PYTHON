#override the __len__() method on vector of file no.23....  to display the dimesions of the vector


class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        result =  vector(self.x + other.x , self.y+ other.y, self.z+other.z)    
        return result
    def __mul__(self,other):
        result = self.x*other.x + self.y*other.y + self.z *other.z
        return result
            
    def __str__(self):
        return f"vector({self.x}, {self.y}, {self.z})" 
    
    
    def __len__(self):
        return 3
    
    
V1= vector(1,2,4)    
print(len(V1))  #3