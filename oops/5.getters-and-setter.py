'''GETTERS''' #methods used to access the values of an objects properties,are typically designed using the @property decorator.
class MyClass:                      #MyClass=class
    def __init__(self, value):       # single property=value; initialized in the init method.
        self._value = value  #value method is getter that uses @property decorator;; returns value of the _value property.
    def show(self):
        print(f" Value is {self._value}")    
    @property #@ laga kr property ban jata h method..
    def ten_value(self):      #property=ten_value
        return 10* self._value  
    
    @ten_value.setter  #property_name.setter se value set kr sakte hai
    def ten_value(self,new_value):   #-value ko set kroge na ki ten_value ki;;;;; jisse ten_value ki value derive ho rhi hai wo set kroge.
        self._value=new_value/10
        return 10* self._value    
    
obj = MyClass(10)
obj.ten_value = 67    #we cant set like this...
print(obj.ten_value)
obj.show()    
'''SETTERS'''  #getters dont take any parameters and we cannot set the value through getter method.therefore setters can be added by decorating method with @property_name.setter        

""" 
getters are a convenient way to access the value of an objects properties, while keeping the internal representation of the property hidden. this can be useful for ENCAPSULATING  and data validation."""