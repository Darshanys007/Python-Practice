a = int(input("Enter your age: "))
b = input("You are Physically Disabled (yes or no): ")

if (a >= 18):
    if(b == "no" or b == "No" or b == "NO" or b == "nO"):
        print("You are eligible to apply for DL")
    else:
        print("You are not eligible apply for DL")
else:
    print("You are not adult")