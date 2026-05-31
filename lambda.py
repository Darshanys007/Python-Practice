# def double(x):
#     return x*2
# print(double(5))

def apply(fx, value):
    return 6 + fx(value)

double = lambda x: x*2
square = lambda x: x*x  #x**2
cube = lambda x: x*x*x  #x**3
avg = lambda x,y,z: (x+y+z)/3
print(double(5))
print(square(5))
print(cube(5))
print(avg(23,43,55))
print(apply(lambda x: x*x, 2))