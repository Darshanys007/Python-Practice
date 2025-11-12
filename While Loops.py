# i = 0
# while(i<20000):
#     print(i)
#     i += 1   #i = i + 1
# print("Done with the loop")

# i = 0
# while(i<50):
#     i = int(input("Enter the number: "))
#     print(i)
# print("Number Doesn't exist")

count = 5
while(count>0):
    print(count)
    count = count - 1  # count -= 1

# while True:
#     print("Hello world")  #If the conditional never become false, the loops runs forever...

i = 5
while(i<5):
    print(i)
    i += 1  
else:
    print("Loop finished without break")


# Emulating Do While in Python
while True:
    number = int(input("Enter a number greater than 10: "))
    if number > 10:
        break
print("Yes! You are right",number,"is greater than 10")