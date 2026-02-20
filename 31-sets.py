
       #SETS DO NOT CONTAIN DUPLICATE ENTRIES LIKE LIST.
a=set()   #empty set
b={20}     # set with one item
c={'sanjay', 35, 446.899}     # set with multiple item
d={100,100,100,100}         #only one 100 gets stored.

s = {2,6,8,2,3}    #sets are unordered collection of data type..    
print(s)           #sets are immutable..
info = {"carter", 19,False, 5.808,87}
print(info)             #no gurantee of order
  # therforre cannot be accessed using index numbers.
  
  
s1={'morning' , 'evening'}  #works
s2={(12,13),(45,68)}        #works
'''s3={[34,67],[77,34]}'''       #will give error
  #it is not possible to create a set of lists, we can create a set of strings and tuples as these are immutable and has a hash value that remains same all the time.
  

  #QUICK QUIZ = TRY TO CREATE AN EMPTY SET. CHECK USING THE TYPE() FUNCTION WHETHER THE TYPE OF YOUR VARIABLE IS A SET..
sneha = set()
print(type(sneha))

#ACCESSING SET ITEMS:
for value in info:
    print(value)
    
    
    
    