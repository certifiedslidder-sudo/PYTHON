"""marks =[3,5,6, "sneha", True ]  #list is to store multiple data under a single name
print(type(marks))        #lists are mutable
print(marks)           #enclosed in[], elements seprated by','
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

lst1= [1,2,3,4,5,6]
lst2=["red","blue","pink"]
print(lst1)
print(lst2)

details=["sneha",18,"aTYbbmU",9.8]
print(details)

color=["red", "blue","pink","grey"]
#index  [0]      [1]      [2]    [3]
print(color[0])
print(color[1])
print(color[2])
print(color[3])


color=["red", "blue","pink","grey"]
#index  [-4]   [-3]   [-2]    [-1]
print(color[-1])       #length of marks -1;(4-1)=element at 3rd index
print(color[-2])       #length of marks -2;(4-2)=2mnd index
print(color[-3])       #length of marks -3;(4-3)=1st index
print(color[-4])       #length of marks -4;(4-4)=0th index


#CHECK WHETHER AN ITEM IS PRESENT IN THE LIST
marks=[3,5,6,"sneha",True]
if 6 in marks:
    print("yes")
else:
    print("no")    
    
marks=[3,5,6,"sneha",True]
if "6" in marks:  #in list 6 is given as int not as string so output is no
    print("yes")
else:
    print("no")
if "neh" in "sneha":
    print("yes") 
else:
    print("no")  
    
marks=[3,5,6,"sneha",True]
if "sneha" in marks:
    print("yes")
else:
    print("no")"""    

marks=[3,5,6,"sneha",True]
print(marks)
print(marks[:])   #full list
print(marks[1:])  #full list
print(marks[1:4])  #one less than 4
print(marks[1:-1])  #from one to (5-1)=4 : 1 to 3

"""         #CONCEPT OF JUMP INDEX
marks=[3,5,6,"sneha",True, 6,7,2,32,345,23]
print(marks[1:9])
print(marks[1:9:2]) #first one to four slicing, then jump by 2"""

animals = ["cat", "dog", "bat","mouse","pig","horse","donkey","goat", "cow"]
print(animals[4:])
print(animals[-4:])
print(animals[:6])
print(animals[:-3])
print(animals[1:8:3])