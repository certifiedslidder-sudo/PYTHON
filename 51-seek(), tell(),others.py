# seek(), tell() functions are used to work with the objects and their positions within a file


           #SEEK() FUNCTION
with open('file.txt', 'r') as f:
    print(type(f))
    '''move to the 10th byte in the file.'''
    f.seek(10)
    '''read the next 5 bytes'''#10th se start hoga
    print(f.tell()) 
    data= f.read(5)         
    print(data)
    
    #seek() function allows you to move the current position within a file to a specific point.the position is specified in bytes, and you can move either forward or backward from the current position...
    
    
                #TELL() FUNCTION
"""with open('file.txt', 'r') as f:
    #read the first 10 bytes
    data=f.read(10)
    
    #save the current position.
    current_position = f.tell()
    
    #seek to the saved position.
    f.seek(current_position)  """  
#tell() function returns the current position within the file,in bytes. this can be useful for keeping track of your location within file or for seeking specific position relative to the current position...


          #TRUNCATE() FUNCTION
with open('sample.txt', 'w') as f:
    f.write('hello world!')
    f.truncate(5)          
    
    with open('sample.txt', 'r') as f:
        print(f.read())
   #when we open file in python using open function, you can specify the mode in which you want to open file, if you specify the mode as 'w' , 'a' , the file is opened in write mode and you can write to the file. however, if you want to truncate the file to a specific size, use this function....      