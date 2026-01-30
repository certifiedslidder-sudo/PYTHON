f= open('myfile3.txt','r')
i=0
while True:
    i=i+1
    line= f.readline()
    if not line:
        break 
    m1= line.split(",")[0]
    m2= line.split(",")[1]
    m3= line.split(",")[2]
    print(f"marks of student {i} in maths is: {m1}")
    print(f"marks of student {i} in english is: {m2}")
    print(f"marks of student {i} in sst is: {m3}")
 
    print(line)
#rREADLINES() METHOD: READS ALL THE LINES OF THE FILE LINE BY LINE  AND RETURNS THEM AS A LIST OF STRINGS....



          # WRITELINES() METHOD
#writeline() method in python writes a sequence of strings to a file.the sequence can be any iterable object,such as list or tuple.          
f= open('myfile4.txt','w')
lines= ['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()   
'''
keep in mind that this method do not add newline characters between the strings in the sequence.if you want to add newlines between the strings,you can use a loop to write each string seprately...

'''

f= open('myfile5.txt','w')
lines= ['line1', 'line2', 'line3']
for line in lines:
    f.write(line + '\n')
f.close()    

    