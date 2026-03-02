'''
•Noun → Class → Employee
•Adjective → Attributes → name, age, salary
•Verbs → Methods → getSalary(), increment()
'''
'''CLASS'''


#Objects of a given class can invoke the methods available to it without revealing the implementation details to the user. -->> Abstractions & Encapsulation!
class Employee:
    language="py"     #this is a class atribute.
    salary=1200000
    
harry=Employee()
harry.name="harry"    #this is an object attribute
print(harry.language,harry.name, harry.salary)

rohan=Employee()
rohan.name="rohan cariappa"
print(rohan.salary, rohan.name,rohan.language)    
#HERE NAME IS OBJECT/INSTANCE ATTRIBUTE(particular person) AND LANGUAGE AND SALARY ARE CLASS ATTRIBUTES(belong to class(all employee not only rohan.)) 
# AS THEY DIRECTLY BELONG TO CLASS AND CAN BE ACCESSED BY ALL THE OBJECTS OF THE CLASS.
