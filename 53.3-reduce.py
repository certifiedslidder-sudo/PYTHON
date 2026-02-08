from functools import reduce
#list of numbers
numbers=[1,2,3,4,5]

#calculate the sum of numbers using the reduce function
sum= reduce(lambda x, y: x+y,numbers)
#print the sum
print(sum)