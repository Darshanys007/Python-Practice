#MAP()
#Applies a function to each item in an iterable (like a list)
numbers = [1,2,3,4,5]
square = list(map(lambda x: x**2, numbers))
print(square)


#FILTER()
#Filter elements of an iterable based on a condition (function that return true/false)
numbers = [1,2,3,4,3,6,7,9,8]
evenl = list(filter(lambda x: x % 2 == 0, numbers))
print(evenl)


#REDUCE()
#Applies a function to elements of an iterable cumulatively, reducing it to a single value
from functools import reduce
numbers = [1,2,3,4,5]
#sum of all numbers
#Use only x(the accumulator) and y(the current item)
total = reduce(lambda x,y: x + y, numbers)
print(total)