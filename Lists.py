l = [1,2,3,"Darshan",True]
print(l)

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

print(l[-4]) #length of list(5) - index[4] = 1
print(l[1:-1]) #1 to 3  #print(l[1:4])

if 3 in l:
    print("Yes")
else:
    print("No")

if "Darshan" in l:
    print("Yes")
else:
    print("No")


l1 = [1,2,3,4,5,6,7]
print(l1)
print(l1[1:6:2]) #Jump Index


l2 = [i*i for i in range(1,11)]
print(l2)
l2 = [i for i in range(1,11)]
print(l2)
l2 = [i for i in range(1,11) if i % 2 == 0]
print(l2)



