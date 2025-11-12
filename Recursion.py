'''
factorial(5) = 5*4*3*2*1
factorial(4) = 4*3*2*1
factorial(3) = 3*2*1
factorial(2) = 2*1
factorial(1) = 1
factorial(0) = 1
'''
# factorial(n) = n * factorial(n - 1)

def factorial(n):
    if(n == 0) or (n == 1):
        return 1
    else:
        return n * factorial(n - 1)
    
# n = int(input("Enter a number to find factorial:"))
# print(factorial(n))

'''
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1
'''


# fibonacci sequence
'''
f(0) = 0
f(1) = 1
f(2) = f(1) + f(0)
f(n) = f(n - 1) + f(n - 2)
'''

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(7))
# 0 1 2 3 4 5 6 7.....
# 0 1 1 2 3 5 8 13....