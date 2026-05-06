#namespace = dictionary of identifiers...
#identifier inside func. = local variable
#identifiers outside func. = global variable

'''if a local and global variable has same name;
       local overshadows global'''
#global keyword changes the variable outside of the function(local variable )
 
a= 89

def fun():
    global a
    a = 3
    print(a)
    
fun()
print(a)     