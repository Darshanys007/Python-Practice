a = "Darshan!!!!!!!!!!!!!!"
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Darshan","Puneeth"))

b = "Darshan Puneeth Yash"
print(b.split(" "))

c = "introduction to python course, 100 days course"
print(c.capitalize())
count = c.count("course")
print("\"course\" word is comes",count,"times in this line")

print(len(c))
print(c.center(47))

d = "Welcome to DbyD"
print(d.startswith("Welcome"))
print(d.endswith("DbyD"))
print(d.endswith("com",4,10))
print(d.find("to"))
print(d.isalnum())

e = "Welcometopythonworld"
print(e.isalnum())
print(e.isalpha())
print(e.islower())
print(e.isupper())
print(e.isprintable())

f = "   "
print(f.isspace())

g = "Welcome To Python"
print(g.istitle()) #It retuns True, if the First letter of the each word is Capital.
print(g.swapcase()) #Convert each Uppercase char to lowercase and Lowercase char to uppercase   wELCOME tO pYTHON




