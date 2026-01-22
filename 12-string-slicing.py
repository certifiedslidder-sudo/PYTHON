name = "sneha"
len1 = len(name)
print("sneha is a ",len1,"letter word.")

fruit = "mango"
mangolen = len(fruit)
print(fruit[0:4])        #here 0 =initial, 4=n therefore print will be (n-1) that is till 3 mang
#include 0 but not 4
print(fruit[1:4])   #include1 but not 4
print(fruit[:5])  #include 0 but not 5  ni smjha
print(fruit[1:])   #include 1 but not 5......and sio non for all...
print(fruit[0:-3])
print(fruit[0:len(fruit)-3])  #len of fruit -3 = 5-3=2 therfore print till 2 that is ma
print(fruit[-1:len(fruit)-3])      #not valid
#4:2 makes no sense
print(fruit[-3:len(fruit)-1]) 
#2:4 therefore from 2 to 3 that is ng
