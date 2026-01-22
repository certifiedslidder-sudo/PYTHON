dict= {      # onward python 3.7 dict. are now ordered before it was unordered..dictionary are ORDERED collection of data type, stores multiple items in a single variable.
    "harry": "human being",
    "spoon": "object"
}
print(dict["harry"])
print(dict["spoon"])

dict={
    344:"neeraj",
    56:"sneha",
    678:"vaishali",
    567:"vanshika"
}
print(dict[344])
info = {'name':'karan','age':'19','eligible':True}
print(info) #ACCESSING WHOLE DICT.
print(info['name'])   #ACCESING SINGLE ELEMENT OF DICT.
print(info.get('name'))
'''print(info['name2222222'])'''    #will give error
print(info.get('name222222')) #will give none


         #ACCESSING      MULTIPLE      VALUES
info = {'name':'karan','age':'19','eligible':True}
print(info)
print(info.keys())
info = {'name':'karan','age':'19','eligible':True}
print(info)
print(info.values())
#or
for key in info.keys():
    print(info[key])
    
for key in info.keys():
    print(f"the value corresponding to the key {key} is {info[key]}")
print(info.items())  
for key, value in info.items():
    print(f"the value corresponding to the key {key} is {value}")   