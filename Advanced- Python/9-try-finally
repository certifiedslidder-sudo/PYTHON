      

    # TRY TO UNDERSTAND PROPERLY..........

'''
finally block is commonly used for releasing external resources like file handles, network connections, or database connections, irrespective of whether the use of resource was successful or not.
'''

#MAIN USE = IN FUNCTION 

def main():
    try:
        a = int(input("hey, enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    
    finally:  #it will run even if the function returns.as return means if function retrns then it will exit the function and it will not execute any code after return statement but finally block will execute even if we have return statement in try or except block.
              print("hey i am imnside finally....")
    
    
main()    