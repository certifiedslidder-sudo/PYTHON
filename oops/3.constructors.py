'''CONSTRUCTOR'''   #special method in a class used to create and intitialize an onbject of a class.It is invoked automatically when an object of class is crerated.
'''PURPOSE'''      #initialize or assign values to the data members of the class. it cannot return any value other than NONE..

'''SYNTAX'''       #   def__init__(self):      initialization
'''TYPES'''  
'''    parameterized= accepts arguments along with self
       default = when const. dont accept any value from the obj and only accepts one argument : self
              '''  
class Person:
    def __init__(self,name,o):
        print("hey i am a person")
        self.name=name
        self.occupation= o
    def info(self):
         print(f"{self.name} is a {self.occupation}")
         
a= Person("sneha","developer")        #person=class
b= Person("shreya","hr")
a.info()        
b.info()
#c=Person() ---->>>> TypeError: Person.__init__() missing 2 required positional arguments: 'n' and 'o'


#c=Person(1,2,3) '''TypeError: Person.__init__() takes 3 positional arguments but 4 were given'''
'''self ke jagah pr c automatically pass ho rha hai.'''

# print(a.name)
# a.name="divya"
# a.occupation="hr"
