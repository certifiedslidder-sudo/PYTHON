l = ["violet", "bluea", "green", "orange", "grey", "red", "indigo"]
print(l)
l.sort()  #for alpabets it will sort in order of alphabet
print(l)



l = ["violet", "blue", "green", "orange", "grey", "red", "indigo"]
print(l)
l.reverse()
print(l)


l = [11,45,1,2,4,6]
print(l)
l.reverse()
print(l)

l = [11,45,1,2,4,6]
print(l[::-1])   #another way to reverse using slicing


l = [11,45,1,2,4,6]
print(l)
l.append(7)
print(l)

l = [11,45,1,2,4,6]
print(l)
l.sort()
print(l)

l = [11,45,1,2,4,6]
print(l)
l.sort(reverse = True)
print(l)

l = [11,45,1,2,4,6]
print(l)
l.reverse()
print(l)

l = [11,45,1,2,4,6]
print(l.index(1))

l = [11,45,1,2,4,6]
print(l)
print(l.count(1))

l = [11,45,1,2,4,6]
print(l)
m = l  #same list is formed in memory, original list also changes
m[5]= 0
print(l)

l = [11,45,1,2,4,6]
print(l)
m=l.copy()  #new list is formed in memory, original list remains same
m[0]=0
print(l)
print(m)

l = [11,45,1,2,4,6]
print(l)
l.insert(2,100)     #insert 100 at index 2, ,overwrite ya replace nhi krega simple given index m jakr store ho jaega aur toal list ki ek index badh jaegi
print(l)

l = [11,45,1,2,4,6]
print(l)
m=[900,1000,1100]
l.extend(m) #extend l by m
print(l) 

l = [11,45,1,2,4,6]
m=[900,1000,1100]
k = l+m  #new list formed by adding l and m
print(k) 
print(l)
print(m)
           #POP
num=[10,20,30,40,50]
num.pop()  #when no index given,it will automatically remove the last value at the last index ;;;;; LAST IN= FIRST OUT
print(num)    

          #DEL
num=[10,20,30,40,50]
del(num[1:2])    
print(num)      #will delete the numbetr at given index
num=[]          #deletes whole list;;;;;;    DIFFERENT FROM POP

l1=[10,20,30,40,50]
l3=l2=l1
l1=[]
print(l2)
print(l3)  #deleting one wont delete others.

          #UNPACKING A STRING
s='hello'          
l=[*s]
print(l)
            #EMBEDDING
X=[1,6,9,9]
Y=[50,78,90,X,33,56]
print(Y)            
          #NESTED LIST
a=[1,2,3,4] 
b=[5,6,7,8]
c=[a,b]
print(c)
print(c[0][0],c[1][2])  #0th element(index acco.) of 0 list,2nd element of first list       

          