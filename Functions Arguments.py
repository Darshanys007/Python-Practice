def default_args(message="Hello",name="Darshan"):
    print(message,name)

default_args("hello","yash") 


def keyword_args(message="Hello",name="Darshan"):
    print(message,name)

keyword_args(name="Darshan",message="Hello") 


def add(*numbers): #Variable-length Arguments
    print(type(numbers)) #collects Arguments as a tuple
    # print(sum(numbers))
    return sum(numbers)

sum1 = add(1,2,3,4,5,6,7,8,9)
print(sum1)

def name(**name):
    print(type(name)) #collects Arguments as a dictionary
    print("hello",name["fname"],name["mname"],name["lname"])

name(fname="Darshan",mname="Yash",lname="king")