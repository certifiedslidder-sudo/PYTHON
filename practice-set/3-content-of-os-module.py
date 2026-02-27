"""write a python program to print the contents of a directory using the os module. search online for the function which does that """

import os

#specify the directory you want to list
directory_path = "C:\\Users\\asus\\OneDrive\\Desktop\\PYTHON"

#list all files and directories in the specified path
contents= os.listdir("C:\\Users\\asus\\OneDrive\\Desktop\\PYTHON")
for item in contents:
    print(item)