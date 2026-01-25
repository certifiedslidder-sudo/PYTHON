marks=[12,56,32,98,12,45,1,4]
index=0
for mark in marks:
    print(mark)   #har mark k sath uska index de dega
    if(index==3):
        print("harry , awesome")
    index +=1 
    
#index=0
for index, mark in enumerate(mark):
    print(mark)   #har mark k sath uska index de dega
    if(index==3):
        print("harry , awesome")
    #index +=1     
      
      
      
#loop over a list and print the index and value of each element.       
fruits = ['apple', 'banana', 'cherry', 'date']
for index, fruit in enumerate(fruits):
    print(index, fruit)
    
  #loop over a list and print the index and value of each element, starting the index from 1 instead of 0.
fruits = ['apple', 'banana', 'cherry', 'date']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
        
fruits = ['apple', 'banana', 'cherry', 'date']
for index, fruit in enumerate(fruits):
    print(f"{index+1}:{fruit}")       