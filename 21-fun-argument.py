"""       #REQUIRED ARGUMENTS
def average(a,b):
    print("the average is" , (a+b)/2)
average(4,6)
 
      #DEFAULT ARGUMENTS
def average(a=9, b=1):
     print("the average  is" , (a+b)/2)               #will print average of 1,5
average(1,5)

def average(a=9, b=1):
     print("the average  is" , (a+b)/2)               #will print average of 9,1
average()


def average(a=9, b=1):
     print("the average  is" , (a+b)/2)              
     print("the average  is" , (a+b)/2)               #will take value of b as default 1
average(5)



def average(a=9, b=1):
     print("the average  is" , (a+b)/2)              
     print("the average  is" , (a+b)/2)           
     print("the average  is" , (a+b)/2)               #will take value of a as default 9
average(b=6)"""

"""def name(fname,nname="singh",lname="rawat"):
    print("hello,",fname,nname,lname)
name("aarav")                        #will print hello, aarav singh rawat
name("chicko")                        #will print hello, aarav chicko rawat
name("aarav" ,"chicko","cutie")      #will print hello,aarav chicko cutie
name("aaru","apple","pie")           #will print hello, aaru apple pie """

#WE CAN ALSO CHANGE THE ORDER OF ARGUMENT
"""def average(a=4,b=6):
    print("the average is" , (a+b)/2)
average(b=4,a=6)"""

#VARIABLE LENGHT ARGUMENT
"""def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is:", sum/len(numbers))    
average(5,6)  """      

"""def name(**name):
    print(type(name))
    print("hello,",name["fname"],name["mname"],name["lname"])
name(fname="aarav",mname="singh",lname="rawat")"""

def average(*numbers):
    #print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    #print("average is:", sum/len(numbers))  
    return sum/len(numbers)  
#average(5,6)
#return sum/len(numbers)
c =average(5,6,9,8)
print(c)