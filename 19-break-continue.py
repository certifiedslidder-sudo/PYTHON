for i in range(12):
     if(i ==10):
        break        #break ka mtlb loop ko chod kar nikl jao
     print("5X", i+1,"=",5*(i+1))
print("exit the loop")

for i in range(17):
     if(i ==10):
      print("skip the iteration")
      continue     #10 wala itteration chor dia aur uske agge wala continue rkha;itterstion skipped not the whole loop.
     print("5X", i,"=",5*i)
     
i=0 
while True:
    print(i)
    i+=1
    if(i%100 ==0):
        break
    
    