import os

folders = os.listdir("data")
print(os.getcwd())  #returns a string representing current working directory..
os.chdir("/Users")
print(os.getcwd())
#print(folders)


for folder in folders:
    print(folder)     #AB YE ERROR DEGA KYUKI HUMNE DIRECTORY CHANGE KR DI H , DIRECTORY CHANGE KRNE SE PHELE AGR HUM RUN KRTE TO CORRECTLY EXECUTE HO JATA...........
    print(os.listdir(f"data/{folder}"))
    
    
    #EXPLORE MORE ON OS MODULES....