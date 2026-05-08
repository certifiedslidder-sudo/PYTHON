#store the multiplication tables generated in problem 3 in a file named tables.txt

n = int(input("enter a number:"))

table = [n*i for i in range(1,11)]
with open("myfile2.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)}  \n")
    
