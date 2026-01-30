'''in python lambda function is a small anonymous function without a name. lambda function can have multiple arguments as shown in below example.
SYNTAX:
       lambda arguments: expression'''


#def double(x):
    #return x*2
def appl(fx, value):
    return 6 + fx(value)

double = lambda x:x*2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3      # we use lambda function if we want to pass function as argument.


print(double(5))
print(cube(5))
print(avg(3,5,43))
print(appl(lambda x: x*x*x,2))