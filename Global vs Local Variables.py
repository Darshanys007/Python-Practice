# def my_function():
#     x = 5 #local variable
#     print(f"Inside function:{x}")
# my_function()
# print(x) #Error x is not defined


# x = 10 #global variable
# def my_function1():
#     print(f"Inside function:{x}")
# my_function1()
# print(f"Outside function {x}")


x = 3
def change():
    global x
    x = 6 #Modifies the global variable
    print(f"Inside function:{x}")
change()
print(f"Outside function {x}")


