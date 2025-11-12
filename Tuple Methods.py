tup = (2,4,6,7,9)
temp = list(tup)   #Convert tuple into list, because tuples are immutable

temp.append(10)
temp.pop()   #Remove the last item
temp.pop(1)  #Remove the 1st index
# print(temp)

tup = tuple(temp)   #Convert list into tuple again, after alter the list(tup1)
print(tup)


tup1 = ("Davanagere","Chitradurga","Shivamogga","Davanagere","Bangalore")
tup2 = ("Japan","America","Rausia")
res = tup1 + tup2
print(res)

res1 = tup1.count("Davanagere")
print("Count of Darshan in tup1 is",res1)