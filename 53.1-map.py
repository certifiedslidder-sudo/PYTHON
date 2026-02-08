'''
MAP,REDUCE,FILTER ARE BUILT IN FUNCTION IN PYTHON THAT ALLOWS YOU TO APPLY A FUNCTION TO A SEQUENCE OF ELEMENTS AND RETURN A NEW SEQUENCE...
THESE FUNCTIONS ARE KNOWN AS        higher order functions,as they take other functions as argument..

'''
'''
if we use these functions than we dont need a for loop or if statement to control the flow while iterating over elements of sequence like string,list,tuple.
'''
                  #MAP
                  
#syntax: (function,iterable). the function argument is a function that is applied to each element in the iterable argument. the iterable argument can be a kist, tuple or any other iterable object.     
                 
#def cube(x):
#    return x*x*x

#print(cube(2))
l=[1,3,2,4,6,7]
'''newl=[]
for item in l:
    newl.append(cube(item))'''
    
newl=list(map(lambda x:x*x*x, l))     
#(function ka naam,wo list jiske har element pr app ye function apply krna chahte ho )    
print(newl)
    
import math
def fun(n):
    return n*n
lst=[5,10,15,20,25]
m1=map(math.radians,lst)
m2=map(math.factorial,lst)
m3=map(fun,lst)
print(list(m1))
print(list(m2))
print(list(m3))



     #USING LAMBDA WITH MAP()
LST1=[5,10,15,20,25]
m=map(lambda n:n*n, LST1)   
print(list(m))     #output:25,100,225,400,625