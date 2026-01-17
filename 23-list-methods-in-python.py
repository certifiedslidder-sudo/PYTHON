l = ["violet", "blue", "green", "orange", "grey", "red", "indigo"]
print(l)
l.sort()
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
l.insert(2,100)     #insert 100 at index 2
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