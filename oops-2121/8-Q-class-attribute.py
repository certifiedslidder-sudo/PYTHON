#Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0. Does this change the class attribute?

class Demo:
    a=4
o=Demo()
print(o.a)  #prints class attribute bcoz instance atteribute is not present.
o.a=0   #instance attribute is set now
print(o.a)   #prints instance  attribute becoz  instance atteribute is set.

print(Demo.a)  #prints class attribute 
    
    
    
"""AMNSWER --->>> NOO"""