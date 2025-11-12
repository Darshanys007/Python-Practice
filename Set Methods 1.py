s1 = {2,3,4,5}
s2 = {5,6,7,8}
print(s1,s2)
s1.update(s2)
print(s1,s2)
print(s1.union(s2))

cities1 = {"Davanagere","Chitradurga","Shivamogga"}
cities2 = {"Bidar","Hospet","Raychuru","Davanagere"}
cities3 = cities1.intersection(cities2)
print(cities3) #print the values which common is both(cities1 and cities2)
cities1.intersection_update(cities2)
print(cities1) #cities1 will be update, which is common in both(cities1 and cities2)


cities4 = {"Davanagere","Chitradurga","Shivamogga"}
cities5 = {"Bidar","Hospet","Raychuru","Davanagere"}
cities6 = cities4.symmetric_difference(cities5)
print(cities6) #Remove which common in both, and print the rest of the values


cities7 = {"Davanagere","Chitradurga","Shivamogga"}
cities8 = {"Bidar","Hospet","Raychuru","Davanagere"}
cities9 = cities7.difference(cities8)
print(cities9)
