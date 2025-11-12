cities1 = {"Davanagere","Chitradurga","Shivamogga"}
cities2 = {"Bidar","Hospet","Raychuru","Davanagere"}
cities3 = cities1.isdisjoint(cities2)
print(cities3)

cities1 = {"Davanagere","Chitradurga","Shivamogga"}
cities2 = {"Bidar","Hospet","Raychuru","Davanagere"}
print(cities1.issuperset(cities2))

cities1 = {"Davanagere","Chitradurga","Shivamogga"}
cities2 = {"Bidar","Hospet","Raychuru","Davanagere"}
print(cities2.issubset(cities1))

students = {"Darshan","Puneeth","Yash"}
students.add("Leo")
print(students)

students = {"Darshan","Puneeth","Yash"}
students2 = {"Leo","Deva","Vikram"}
students.update(students2)
print(students)

students = {"Darshan","Puneeth","Yash"}
students.remove("Puneeth")
# students.remove("Puneeth") #It throws the error and not go to next line
print(students)

students = {"Darshan","Puneeth","Yash"}
students.discard("Puneeth")
students.discard("Puneeth1") #It not throws the error, Sometimes errors are important
print(students)

students = {"Darshan","Puneeth","Yash"}
item = students.pop()
print(students)
print(item)