tup = (1,3,5)           #tuple
print(type(tup),tup)

tup = (5)               #int
print(type(tup),tup)


tup = ("sn")            #string
print(type(tup),tup)


tup = (5,"sn")           #tuple
print(type(tup),tup)
 
tup=[1,8,99,57]          #list
print(type(tup),tup)

tup=[1,8,99,57]     
tup[3] = 7         #value of list can be changed
print(type(tup),tup)

tup=(1,8,99,57)   
#tup[3] = 7         #value of tuple can't  be changed;error
print(type(tup),tup) 

tup=(3,7,98,"sneha",True)
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
if 98 in tup:
    print("yes 98 is in this tuple")
    
if 9 in tup:
    print("yes 98 is in this tuple")    
else:
    print("9 is not in this  tuple")    
    
tup2= tup[1:4]     #after slicing a new tuple is formed.
print(tup)
print(tup2)