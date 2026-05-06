def myFunc():
    print("hello world")
    
myFunc()
print(__name__)  #will print __main__ if this file is run directly, otherwise it will print the name of the module if imported


if __name__ == "__main__":
    print("we are directly running this code.")
    myFunc()
print(__name__)    
    
   