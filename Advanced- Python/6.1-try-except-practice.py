try:
    a = int(input("enter a number:"))
    b = int(input("enter a number:"))
    c = a/b
    print('c=',c)
except ZeroDivisionError as zde:
    print('denominator is zero') 
    print(zde.args)
except ValueError:
    print("unable to convert string to int")
except:
    print("some other unknown error occurred")           