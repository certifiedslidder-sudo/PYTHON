#tuples are immutable..

countries=("spain", "italy","india","england","germany")
temp = list(countries)
temp.append("russia")        #add item
temp.pop(2)                  #remove item 
temp[2]="finland"            #change item;HERE 2 IS INDEX
countries= tuple(temp)
print(countries)
#therefore we convert tuple to list to manipulate changes in it.

#BUT.......BUT....BUT  WE CAN DIRECTLY CONCATENATE TWO TUPLES WITHOUT CONVERTING THEM TO LIST...

countries=("pakistan","afganistan","bangladesh","srilanka")
countries2=("vietnam","india","china")
southEastAsia= countries + countries2
print(southEastAsia)

         #TUPLE METHODS
         
tuple1 =[0,1,2,3,2,3,1,3,2]         
res = tuple1.count(3)
print('count of 3 in tuple1 is:', res)   #return:3

tuple1 =[0,1,2,2,1,2]         
res = tuple1.count(3)
print('count of 3 in tuple1 is:', res) #return:0 

tuple1 =[0,1,9,6,2,3,3,2]         
res = tuple1.index(3) #return:5
print('first ocurance  of 3 in tuple1 is:', res)         
 
       
tuple1 =[0,1,9,6,2,31,3,2]         
res = tuple1.index(3,3,7) #return:6  (element,start index, end index)
print('first ocurance  of 3 in tuple1 is:', res)    

tuple1 =[0,1,9,6,2,31,3,2]         
res = tuple1.index(322,3,7) #error
print('first ocurance  of 3 in tuple1 is:', res)


tuple1 =[0,1,2,2,1,2]         
res = len(tuple1)   #gives length of tuple
print('length tuple1 is:', res)


#TUPLE WITH ONE ITEM
b=(10,)
print(type(b))
'''while creating a tuple with single element(b),its must to add a comma after 10 other wise b is treated as int type'''