l1=[]
l2=[123,"python",3.5]
l3=["c","java,python"]
print(l1)
print(l2)
print(l3)

mylist=["banana","apple","mango", "tomato","berry"]
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[1:3])
print(mylist[-1])
print(mylist[-4:2])


num=[1,2,3,4,5]
lang=["python","c","java","php"]
print(num+lang)
print(num*2)
print(lang[2])
print(lang[1:4])
print('cpp' in lang)
print(6 not in num)


num=[1,2,3,4,5]
print(num)
num[2]=56
print(num)
num[1:3]=[23,45]
print(num)
num[4]="python"
print(num)

num=[1,2,3,4,5]
del num[1]
print(num)
del num[1:3]
print(num)

lang=["python", "c","java", "php"]
print("the list items are \n")
for i in lang:
    print(i)

num1=[1,2,3,4,5,6]
num2=['java','c','pyhton','cpp']
print("length of list",len(num1)) 
print("max of num1", max(num1))
print("max of num1", max(num2))
print("min of num1", max(num1))
print("min of num2", max(num2))
print("sum of items",sum(num1))
#print("sum of items",sum(num2))           will give error

str="python"
list1=list(str)
print(list1)
num=[1,3,2,4,6,5]
lang=['java','c','python','cpp']
print(sorted(num))
print(sorted(lang))
num.append(6)
print(num)
lang.append("cpp")
print(lang)
l1=[1,2,]

   




"""l1=[2,4,6,9,3,6,]
name=["sneha", "suhana", "aarav","vaishali" ,"vanshika"]
l1.sort()
print(l1)
name.sort()
print(name)
l3=["Shashank", "Ram","mohan","Manoj","ram"]      #sorted with the help of ascii values of uppercase+lowercase
l3.sort()
print(l3)"""