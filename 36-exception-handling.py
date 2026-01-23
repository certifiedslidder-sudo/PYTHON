"""a= input("enter the number:")
print(f"multiplication table of {a} is:")
for i in range(1,11):
    print(f"{int(a)}X{i}={int(a)*i}")
    
    
print("some important lines of code")    
print("end of program")








a= input("enter the number:")
print(f"multiplication table of {a} is:")
try:
   for i in range(1,11):
    print(f"{int(a)}X{i}={int(a)*i}")
except:
    print("Invalid input!")
    
print("s ome important lines of code")    
print("end of program")
#JHA ERROR AARA H USSI LINE M ERROR DEGA BAKI KI STATEMENTS JO  SHI H WO AS IT IS EXECUTE KREGI UNLIkE OTHER ERRORS ki pure code ke 4 statement m error ho toh code hi ni chlega...."""

try:
    num= int(input("enter an integer:"))
    a=[6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error!")
     #value error smj ni aya   
