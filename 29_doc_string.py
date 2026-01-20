
  #******* DOC STRING SHOULD BE RIGHT ABOVE FUNCTION BODY OR RIGHT BELOW FUNCTION NAME NOTHING ELSE SHOLD BE IN BETWEEN...********

#a string just above the body of function OR BELOW FUN. NAME AND  stored under     .__d0c__     attribute.

"""def square(n):
    '''takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)"""   #use to document the code

def square(n):
    print(n)   #gives 5
    '''takes in a number n, returns the square of n'''
    print(n**2)     #gives 25
square(5)
print(square.__doc__)     #gives NONE

  #******* DOC STRING SHOULD BE RIGHT ABOVE FUNCTION BODY OR RIGHT BELOW FUNCTION NAME NOTHING ELSE SHOULD BE IN BETWEEN...********