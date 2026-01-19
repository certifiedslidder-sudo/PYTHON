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

txt = "for only {}"