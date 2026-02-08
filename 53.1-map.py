def cube(x):
    return x*x*x

print(cube(2))
l=[1,3,2,4,6,7]
'''newl=[]
for item in l:
    newl.append(cube(item))'''
    
newl=list(map(cube, l))      
#(function ka naam,wo list jiske har element pr app ye function apply krna chahte ho )    
print(newl)
    
    