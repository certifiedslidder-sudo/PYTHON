#CREATE A PY. PROG. CAPABLE OF GREETING YOU WITH GOOD MORNING, GOOD AFTERNOON AND GOOD EVENING. YOUR PROGRAM  SHOULD USE TIME MODULE TO GET THE CURRENT HOUR. 

#sample program:

"""import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')   
print(timestamp) 
    
#https://docs.python.org/3/library/time.html#time.strftime"""


             #P R O G R A M
"""            
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')   
print(timestamp)"""  

import time 
t = time.strftime('%H:%M:%S')  #h will run till 12
hour = int(time.strftime('%H'))
hour = int(input("enter hours:"))
print(hour)
if(hour>0 and hour<12):
    print("Good Morning Sir!")    
elif(hour>12 and hour<17):
    print("Good Afternoon Sir!")   
elif(hour>17 and hour<=23):   #nott 0 logic glt baithega
    print("Good Evening Sir!")   