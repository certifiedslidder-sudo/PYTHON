#write a program ro open three files myfile.txt , myfile1.txt , myfile2.txt and if any of these filea are not present , a message without exiting must be printed promoting the same.


try:
 with open("myfile.txt","r") as f:
    print(f.read())
except Exception as e:
    print(e)    
try:
 with open("myfile1.txt","r") as f:
    print(f.read())
except Exception as e:
    print(e)    
try:
 with open("myfile2.txt","r") as f:
    print(f.read())
except Exception as e:
    print(e)    
print("thamks ")    