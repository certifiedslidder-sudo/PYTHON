letter= "hey my name is {} and i am from {}"
country= "india"
name="sneha"
print(letter.format(name,country))
print(letter.format(country,name))

letter= "hey my name is {1} and i am from {0}"
country= "india"
name="sneha"
print(letter.format(country, name))
print(f"hey my name is {name} and i am from {country}")

txt = "for only {price:.2f} dollars!"
print(txt.format(price = 49.09999))

price = 49.09999
txt = f"for only {price:.2f} dollars!"
print(txt)
#print(txt.format(price = 49.09999))

print(f"{2 * 30}")   #we can use it in single statement as well..

print(type(f"{2 * 30}") )  # printing data type

print(f" we use f strings like this : hey my name is {{name}} and i am from {{country}}")
#  {{}} does literal printing as it is ; it retains f string as a f string.