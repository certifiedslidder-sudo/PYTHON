#THE STATEMENT IN ELSE BOX WILL BE EXECUTED AFTER ALL THE ITERATION ARE COMPLETED. same for while loop too.

for i in range(5):
    print(i)
else:
    print("sorry no i") 
    
for i in []:
    print(i)
else:
    print("sorry no i")    
    
for i in range(7):
    print(i) 
    if i==4:
        break  #break ka mtlb lopp toot gya h 
else:          #else tb hi  execute hota hai jb loop complete hota h 
    print("sorry no i ")             #else print ni hoga
    
i = 0
while i<7:
    print(i)
    i+=1
    if i==4:
        break
else:
    print("sorry no i")        
    
for x in range(5):
    print("iteration no {} in for loop".format(x+1))    
else:
    print("else block in loop")  
print("out of loop")      