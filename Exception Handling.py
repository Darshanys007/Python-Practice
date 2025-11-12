a = input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} * {i} = {int(a)*i}")
except:
    print("Inavid literal")
    
print("some lines of code")
print("End of program")


try:
    x = 10/0
except ZeroDivisionError:
    print("Zero division error")

