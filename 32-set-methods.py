s1= {1,2,5,6} 
s2={3,6,7}
print(s1.union(s2))   #merges both sets completely
print(s1,s2)
s1.update(s2)   
print(s1,s2)    #here s1 now becomes 1,2,3,5,6,7

cities = {"tokyo","madrid","berlin","delhi"}
cities2= {"tokyo","madrid","seoul","kabul"}
cities3= cities.union(cities2)
print(cities3)

cities = {"tokyo","madrid","berlin","delhi"}
cities2= {"tokyo","madrid","seoul","kabul"}
cities3= cities.intersection(cities2)  #will print only the common elements from both the sets.
print(cities3)
cities.intersection_update(cities2)
print(cities)

cities = {"tokyo","madrid","berlin","delhi"}
cities2= {"tokyo","madrid","seoul","kabul"}
cities3= cities.symmetric_difference(cities2) #uncommon
print(cities3)


cities = {"tokyo","madrid","berlin","delhi"}
cities2= {"seoul","kabul","delhi"}
cities3= cities.difference(cities2)   #a-b; a ka wo element jo b mai na ho..
print(cities3)

     #INBUILT SET METHODS FOR MANIPULATION OF SETS.
cities = {"tokyo2","madrid2","berlin","delhi"}
cities2= {"tokyo","madrid","seoul","kabul"}
print(cities.isdisjoint(cities2)) #when intersection is zero
#will print true if there are no common element and will print false if there are any common element.
cities = {"tokyo2","madrid","berlin","delhi"}
cities2= {"tokyo","madrid","seoul","kabul"}
print(cities.isdisjoint(cities2))

cities = {"tokyo","madrid","berlin","delhi","seoul","kabul"}
cities2= {"tokyo","madrid","seoul","kabul"}
print(cities.issuperset(cities2)) #if all elements of b are in a 
#cities 2 ke agr sare elements are cities mai ho to true return hoga; superset hai..... are cities2 yha cities ka subset hai
cities = {"tokyo","madrid","berlin","delhi"}
cities2= {"tokyo","madrid","seoul","kabul"}
print(cities.issuperset(cities2))

cities = {"tokyo","madrid","berlin","delhi"}
cities2={"seol","kabul"}
print(cities.issuperset(cities2)) #false
cities3= {"tokyo","madrid","delhi"}
print(cities.issuperset(cities3))     #true

cities = {"tokyo","madrid","berlin","delhi"}
cities2={"seol","kabul"}
print(cities2.issubset(cities)) #false
cities3= {"tokyo","madrid","delhi"}
print(cities3.issuperset(cities))   #true

cities={"tokyo","madrid","berlin","delhi"}
cities.add("helsinki")
print(cities)

cities={"tokyo","madrid","berlin","delhi"}
cities2={"helsinki","seoul","kabul"}
cities.update(cities2)
print(cities)

cities={"tokyo","madrid","berlin","delhi"}
cities.remove("berlin")
print(cities)

#THE DIFFERENCE BTW REMOVE() AND DISCARD() IS, THAT IF  WE TRY TO REMOVE() AN ITEM WHICH IS NOT PRESENT IN THE SET,  IT RAISES  AN ERROR WHEREAS DISCARD() DOES NOT.

cities={"tokyo","madrid","berlin","delhi"}
cities.remove("noida")
print(cities)

cities={"tokyo","madrid","berlin","delhi"}
cities.discard("noida")
print(cities)

cities={"tokyo","madrid","berlin","delhi"}
item= cities.pop()
print(cities) #cant predict bcoz unordered set
print(item)   #cant predict
 
cities={"tokyo","madrid","berlin","delhi"}
del cities    #deletes an entire set;throws error
print(cities)


   #WHAT IF WE DONT WANT TO DELETE THE ENTIRE SET, WE JUST WANT TO DELETE ALL ITEMS WITHIN THE SET
cities={"tokyo","madrid","berlin","delhi"}
cities.clear()    #deletes all items within set
print(cities)    #returns: set()

info = { "carla", 19,False,5.9}
if "carla" in info:
    print("carla is present.")
else:
    print("carla is absent.")    



           #NO EMBEDDING
           #NO UNPACKING