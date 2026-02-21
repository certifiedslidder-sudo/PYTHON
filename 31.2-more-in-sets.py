#iterated over using a for loop, but cannot use while loop as cannot be  accessed using index numbers as they are unordered collection of data type.

'''s=frozenset({'gate','fate','late'})   #for immutable set,use frozenset
s.add('rate')'''  #error


s={12,24,36,48,60}
"""t={24,48,12,36,60}
u={60,12,48,24,36}
print(s)       #will print {48, 36, 24, 12, 60}     
print(t)       #will print {48, 36, 24, 12, 60}
print(u)       #will print {48, 36, 24, 12, 60}


st=[10,20,49,20,20,78,10]
s=set(st)    #repetitions will be eliminated
print(s)

s={12,15,13,23,22,16,17}
t={'a','b','c'}
u=set()
s.add('hello')
print(s)
s.update(t)
print(s)
u=s.copy()
print(u)
s.remove(15)
print(s)"""
s.remove(789)       #error
print(s)
s.discard(789)      #no differnce
print(s)
"""s.discard(789)
print(s)
s.clear
print(s)"""