   # USE    OF    FINALLY???????????////
def func1():
 try:
     l=[1,5,6,7]
     i= int(input("enter the index:"))
     print(l[i])
     return 1
 except:
     print("some error occured")
     return 0
 finally:  
     print(" I  am always executed.")      #always executed either if we go inside try or inside  except, even if function returns inside try , it will execute.....    
             
x = func1()
print(x)  







def func1():
 try:
     l=[1,5,6,7]
     i= int(input("enter the index:"))
     print(l[i])
     return 1
 except:
     print("some error occured")
     return 0
 #finally:   #always executed either if we go inside try or inside  except, even if function returns inside try , it will execute.....
     
     
       # print(" I  am always executed.")     
print(" I  am always executed.")  #wont execute if function returns inside try; check by entering 0     
       
x = func1()
print(x)    