"""f= open('myfile.txt','r')  #2 arguments:  (name of file,mode)
    #r mode is default,this mode opens the file for reading only and gives an error if the file does not exist.this is the default mode if no mode is passed as parameter.
f= open('myfile2.txt','w')
    #w mode opens the file for writing only and creates a new file if the file does not exist.
    
    #a mode opens the file for appending only and creates a new file if it does not exist. 

    #t mode used to handle text file.
'''there is no difference in between r and rt or w and wt since text mode is default.
b(binary): used to handle binary files(image,pdf etc.)'''
#print(f)
text=f.read()
print(text)
f.close()"""

"""        #writing a file
f= open('myfile.txt','a')  
f.write('hello,guyzzz!!!!')
f.close()
"""

    #______WITH STATEMENT_______
with open('myfile.txt', 'a') as f:
    f.write("hey i am inside with ")
   #you can use the with statement to automatically close the file after you are done with it..

'''keep in mind that writing to a file will overwrite its contents. if you want to append to a file instead of overwriting it, you can open it in append mode'''