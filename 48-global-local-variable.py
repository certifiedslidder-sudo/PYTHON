#variable= name location in memory

#local variable= defined inside function, accessible within that function,created when the function is called and destroyed when the function is returned.....

#global variable= defined outside the function and is accessible from within any function in your code.....
x=4
print(x)



def hello():
    x=5
    y=1
    print(f"the local x is {x}")
    print("hello sneha")
    print(y)   #will print as y is defined inside function and we are printing within that function only...
    
print(f"the global x is {x}")    
hello()  
print(f"the global x is {x}")  
#print(y)  , wont print as its not defined oustide function 
  
  
'''NOW WHAT IF WE WANT TO MODIFY A GLOBAL VARIABLE FROM WITHIN A FUNCTION????/    THIS IS WHERE GLOBAL KEYWORD COMES IN.....'''  
  
    # GLOBAL KEYWORD IS USED TO DECLARE THAT A VARIABLE IS A GLOBAL VARIABLE AND SHOULD BE ACCESSED FROM THE GLOBAL SCOPE. 
  
  
  
x=19     #global variable
def my_function():
    global x  #global keyword tells we want to access global variable x
    x=44      #changes the value of global variable x
    y=5  #local variable
    print(y)
my_function()
print(x)             #will print 44
#print(y)                 
                #will cause an error bcoz y is a           local variable and is not accesssible outside the function...
    