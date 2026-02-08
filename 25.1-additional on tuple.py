"""c='sanjay',25,34579.678
print(type(c))   #returns: <class 'tuple'
#while initializing a tuple we can drop().



#TUPLES CAN BE REPEATED.BUT UNLIKE LIST TUPLES CANNOT NE REPEATED USING A*
tpl1=(10,)*5
tpl2=(10)*5
print(tpl1)   #returns: (10,10,10,10,10)
print(tpl2)   #returns:50


#USING BUILT IN FUNCTIONS ON TUPLES"""
"""
t=(12,15,13,23,22,16,17)
len(t)  
print(len(t))
max(t) 
print(max(t))
min(t)
print(min(t))
sum(t)
print(sum(t))
any(t)
print(any(t))
all(t)
print(all(t))
sorted(t)
print(sorted(t))
reversed(t)
print(reversed(t))"""



records=(
    ('sneha',24,45.45),('aarav',34,234.30),
    ('srey',34,33.34),('pre',34,4.90)
)
print(records[0][0],records[0][1],records[0][2])
print(records[1][0],records[1][1],records[1][2])
for n,a,s in records:
    print(n,a,s)
'''output= sneha 24 45.45
aarav 34 234.3
sneha 24 45.45
aarav 34 234.3
srey 34 33.34
pre 34 4.9'''

records=(
    ('sneha',24,45.45),('aarav',34,234.30),
    ('srey',34,33.34),('pre',34,4.90)
)
for n,a,s in records:
    print(n,a,s)
'''output:sneha 24 45.45
aarav 34 234.3
srey 34 33.34
pre 34 4.9'''

#TUPLE UNPACKING USING *OPERATOR
X=(1,2,4,2)
Y=(23,56,*X,30,33)     
print(Y)     #outout:(23, 56, 1, 2, 4, 2, 30, 33)

#TUPLE EMBEDDING
X=(1,2,4,2)
Y=(23,56,X,30,33)     
print(Y)      #outout:(23, 56, (1, 2, 4, 2), 30, 33)


