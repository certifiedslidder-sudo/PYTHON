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
