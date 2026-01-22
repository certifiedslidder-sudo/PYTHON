  #iterating over a string
name = 'sneha'
for i in name:
    print(i)
    if(i == "e"):
        print("this is something fab")
        
        #iterating over a list
colors = ["red", "green","blue","yellow"]
for colors in colors: 
    print(colors)     #this prints the elements of a list
    for i in colors:
      print(i)  #this will print word wise the whole list
    
        #range()
for k in range(5):
    print(k+1)
        
for k in range(1,9):
    print(k+1)
    
for k in range(1,11,3):  #start,stop,step...here 3 is step therefore range jumps 3 steps sarting from 1 to 11
    print(k)