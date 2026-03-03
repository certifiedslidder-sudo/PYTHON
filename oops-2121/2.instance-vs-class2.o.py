class Employee:
    language="py"   #this nis a class attribute
    salary=1200000
harry=Employee()
harry.language = "java script" #this is an object/instance attribute
print(harry.language,harry.salary)    #output:java script,1200000
'''Note: Instance attributes, take preference over class attributes during assignment & retrieval.'''

harry=Employee()
#harry.language = "java script"
print(harry.language,harry.salary)    #output:python,1200000