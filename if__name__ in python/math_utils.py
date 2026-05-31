def add(a,b):
    return a + b

def sub(a,b):
    return a - b

print("math_utils.py is being executed!")

if __name__ == "__main__":
    #This block runs only if you run: math_utils.py
    print("Testing math_utils directly...")
    print("3 + 3 =",add(3,3))
    print("7 + 4 =",sub(7,4))
