'''
name-->> class-->> employee
adjective-->> attributes-->> name,age,salary
verbs-->> methods-->> getsalary(),increment()'''


class Employee:
    language="py"   #this is a class attribute
    salary=1200000
harry=Employee()
harry.name="harry"  #this is an object/instance attribute
print(harry.name,harry.language,harry.salary)
harr=Employee()
harr.name="harr"
print(harr.name,harr.language,harr.salary)
arry=Employee()
arry.name="arry"
print(arry.name,arry.language,arry.salary)
rry=Employee()
rry.name="rry"
print(rry.name,rry.language,rry.salary)
     
    #name= object attribute
    #lang,salary=class attribute