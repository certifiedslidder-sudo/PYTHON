# errors that occurs during execution(RUNTIME) : EXCEPTIONS.
# ex
# memory related - stack, heap overflow , exceeding bounds.
#arithmetic related - division by zero,overflow.
#others - attempt to use an unassigend refrence, file not found, network related errors.





try: #contains statement that i suspect  wrong.
   a = int(input("enter a number:"))
   print(a)
except ValueError as v:   
    print("hey")
    print(v)
except Exception as e:   
    print(e)
    
    
print("LAST BUT NOT THE LEAST , I WOULD LIKE TO THANK MYSELF!!!")    
   
   
   
   
"""
       In Python, stack traces are displayed when an unhandled exception is raised, helping developers debug by tracing back to the root cause. For example, if a function calls another function that raises an error, the stack trace shows the full path of calls.

"""
   