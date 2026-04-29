class Employee:
    a=1
    @classmethod 
    def show(cls):
        print(f"the class attribute of a is {cls.a}")
        
    @property #makes method behave like a variable hence we can use print(e.name) instead of calling e.name()
    def name(self):   
        return f"{self.fname} {self.lname}"  
    
    @name.setter
    def name (self,value):         
        self.fname = value.split(" ")[0]   # .split (" ") yha space ho wha tod dega aur ek list bana dega.
        self.lname = value.split(" ")[1]
        
e= Employee() #object created
e.a = 45   #creates instance variable a=45, BUT WON'T CHANGE CLASS A
e.name="harry rawat"   #setters runs and sets fname anf lname    
print(e.fname, e.lname)  #property getter runs
e.show()      #prints class attribute