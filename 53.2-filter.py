                  #FILTER
'''
filter function filters a sequence of elements based on a given predicate(a function that returns a boolean value) and returns a nerw sequence containing only the elements that meet the predicate.
SYNTAX: filter(predicate,iterable)
PREDICATE= is a function that returns a boolean value and is applied to each element in the iterable argument. the iterable argument can be a list ,tuple or any iterable object
'''                  
l=[1,2,4,6,4,3]        
def filter_function(a):
    return a>3

newl= list(filter(filter_function,l))
print(newl)

from functools import reduce
def getsum(x,y):
    return x+y
def getprod(x,y):
    return x*y
lst=[1,2,3,4,5]
s=reduce(getsum,lst)
p=reduce(getprod,lst)
print(s)    #output:15
print(p)    #output:120



#USING LAMBDA WITH FILTER()
LST1=[5,10,18,27,25]
f=filter(lambda n:n%5==0,LST1)
print(list(f))      #output:10,15,25