ep1 ={122:45,123:89,567:69}
ep2={222:67,566:90}
#ep1.update(ep2)
print(ep2)
print(ep1)   #ep1 got updated 


ep2.clear()
print(ep2)         #returns:{}

empt={}
print(empt)   #empty dict. created., removes all items from dict.

'''ep1.pop(122)    #removed the key value pair whose key is passed as a parameter.
print(ep1)''' 

'''ep1.popitem()   #will remove the lat key value pair
print(ep1)'''

#del ep1
print(ep1)      #del deletes whole dictionary, if key is not provided

"""del ep1[122]       #here 122 is int
print(ep1)"""   #deleting an  item.

#del ep1["122"]      #WILL GENERATE ERROR AS "122" IS A STRING
print(ep1)    

