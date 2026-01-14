       #REQUIRED ARGUMENTS
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
average(b=6)

        