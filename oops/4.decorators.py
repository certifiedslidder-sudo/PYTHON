'''DECORATORS''' # DECORATOR  is a function that takes another function as an argument and returns a new function that modifies the behaviour of the original function. new fx is refered as decorated fx.

'''SYNTAX''' #  @decorator_function
             #  def my_function():
             #pass
'''@decorator_function''' #shorthand for the following code..
"""                 def my_function:
                    pass
                    my_function = decorator_function(my_function)
"""             

def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("thanks for using this function")    
    return mfx    
@greet
def hello():
    print("hello world")
def add(a,b):
    print(a+b)    
     
#greet(hello)()
hello()
greet(add)(1,2)

import logging
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result= func(f"{func.__name__} returned {result}")
        return result
    return decorated
@log_function_call
def my_function(a,b):
    return a+b