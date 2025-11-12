x = int(input("Enter the number: "))
#X is the variable to match

match x:
    case 0:
        print("x is Zero")
    case 2:
        print("x is Two")
    case 4:
        print("x is Four")
    case 7:
        print("x is Seven")
    case 10:
        print("x is Ten")
    case _:
        print(x)