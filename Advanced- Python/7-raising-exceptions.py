a = int(input("enter a number:"))
b = int(input("enter second number:"))

if (b==0):
    raise ZeroDivisionError("hey our program is not meant to divide numbers by zero.")
#here we raised a custom error. and our program crashes as we raise an error.
#prints stck trace and terminates.
else:
  print(f"the division of a/b is {a/b} ")