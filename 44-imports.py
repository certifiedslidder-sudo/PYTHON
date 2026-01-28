"""import math
result = math.sqrt(9)
print(result)     #output:3.0

"if i want to import only one function"""

"""from math import sqrt, pi,floor
result= sqrt(9)
res=sqrt(9)*pi
ans=floor(4.2343)
print(result) #output:3.0
print(pi)     #output:3.141592653589793
print(ans)    #output:4
print(res)    #output:9.42477796076938

from math import *  #this imports everthing, not recomended as it leads to confusion
 
import math as m
result= m.sqrt(9)*m.pi
print(result)"""

"""import math
print(dir(math))   #you can see everthing that imports in math
print(math.nan)
print(math.nan, type(math.nan)) """     #class float


from sneha import welcome,sneha     # 0R     from sneha import *
import math

print(dir(math))
print(math.nan, type(math.nan))
welcome()
print(sneha)

import sneha as hr
import math

print(dir(math))
print(math.nan, type(math.nan))
hr.welcome()
print(hr.sneha)