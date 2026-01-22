          #STRINGS  ARE  IMMUTABLE
a = "!!!harry !!!!!!!! harry"
print(len(a))
print(a)

print(a.upper())                    #convert to uppercase

print(a.lower())                    #convert to lowercase

print(a.rstrip("$"))                #remove receeding  tailing characters  not the initial onrs

print(a.replace("harry","john"))    #replaces

print(a.split(" "))
9666666
blogHeading  = "introduction to js"
print(blogHeading.capitalize())
blogHeading  = "introduction tO jS"
print(blogHeading.capitalize())
#converts 1st character to upper case but all others to lower case

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))

print(a.count("harry"))

str1 = "Welcome to the Console!!!"
print(str1. endswith("!!!"))

str1 = "welcome to the console!!!"
print(str1.endswith("to",4,10))

str1 = "he's name is dan. he is an honest man."
print(str1.find("is"))   #will detect the first occurance of is .

#str1 = "he's name is dan. he is an honest man."
#print(str1.find("you"))
#if the string is not found the compiler will return -1

#str1 = "he's name is dan. he is an honest man."
#print(str1.index("hello"))  #will return error

str1 = "Welcometotheconsole"
print(str1.isalnum())

str1 = "welcome"
print(str1.isalpha())

str1 = "welcome000"
print(str1.isalpha())

str1 = "welcome"
print(str1.islower())

str1 = "welCome"
print(str1.islower())

str1 = "WELCOME HOME"
print(str1.isupper())

str1 = "welcome to my house buddy"
print(str1.isprintable())

str1 = "welcome to my house buddy\n"  #\n is not a printable character
print(str1.isprintable())

str2 = "         "   #white space using space bar
print(str2.isspace())
str2 = "        "  #white space using tab
print(str2.isspace())

str3= "World Health Organisation"
str4 = "the World is HEAling"
print(str3.istitle())
print(str4.istitle())

str1 = "Python is a Interpreter Language"
print(str1.startswith("Python"))
str1 = "Python is a Interpreter Language"
print(str1.startswith("is"))
str1 = "Python is a Interpreter Language"
print(str1.startswith("sneha"))

str4 = "the World is HEAling"
print(str4.swapcase())









