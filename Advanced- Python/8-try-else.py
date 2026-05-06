#try box successfully run ho without exceptions,    tbhi wo else ke andar jata hai ....
#else block must occur after all the except blocks.

try:
    lst = [10,20,abc,40,50]
    for num in lst:
        i= int(num)
        j = i*i
        print(i,j)
except NameError:
    print(NameError.args) 
else:
    print("total number processed", len(lst))         
    del(lst)  
        