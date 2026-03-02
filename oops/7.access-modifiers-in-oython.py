'''ACCESS SPECIFIERS/MODIFIERS'''
#used to limit the access of class variables and class methods outside of class whilw learning the concepts of inheritance...
'''TYPES'''      #public access modifiers
                 #private access modifiers
                 #protected access modifiers
# class Employee:
#     pass
 
# a= Employee() 
# a.emp1 = 5

'''PUBLE ACCESS MODIFIER'''
#all the variables and methods(member functions)in python are by default public.any instant variable in the class followed by the self keyword i.e, self.var_name are public accessed.
class Employee:
    def __init__(self):
        self.name = "sneha"
a=Employee()
print(a.name)      
    
'''IN PYTHON THERE IS NO CONCEPT OF PRIVATE ACCESS MODIFIERS....IN SOME OTHER LANGUAGE WE CAN USE __NAME  .this is known as WEAK INTERNAL USE INDICATOR'''    

class Employee:
    def __init__(self):
        self.__name = "sneha21"
a=Employee()
#print(a.__name)           cannot be accessed directly...
print(a._Employee__name)   #can be accessed indirectly
print(a.__dir__())

'''PROTECTED ACCESS MODIFIERS'''