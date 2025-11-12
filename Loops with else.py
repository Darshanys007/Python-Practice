for i in range(7):
    print(i)
    if i == 4:
        break
else:
    print("Loop finished without a break")

i = 0
while i<7:                                   #The else block will execute only if the loop finish the iterating
    print(i)                                 #without being terminated by a break statement
    i = i + 1
    # if i == 4:
    #     break
else:
    print("Loop finished without a break")




