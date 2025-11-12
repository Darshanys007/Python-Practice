#Finally
# def fun1():
#     try:
#         return "Returning from try"
#     finally:
#         print("Finally blocks run always")

# print(fun1())

try:
    file = open("file.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file, if error is occured")


# Raise
a = int(input("Enter any value between 5 to 10: "))
if(a<5 or a>10):
    raise ValueError("Value should be 5 to 10")


try:
    boy = input("Who do you want to marry:")
    if boy.lower() != "darshan":
        raise Exception("You can only marry Darshan, select him!")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Yes! Darshan is SMART!!")
finally:
    print("Love from D-Matromany...")