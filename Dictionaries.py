dic = {
    7: "Darshan",
    18: "Karthik",
    17: "Mani"
}
print(dic[7])

info = {'name':'Darshan','age':17,'eligible':True}
print(info)
print(info['name']) #It throws error if key doesn't exist
print(info.get('name1')) #It not throws the error if key doesn't exist

print(info.keys()) #Print the keys
print(info.values()) #Print the values

for key in info.keys():
    print(f"The {key} is {info[key]}")

print(info.items()) #Print Key:value pair

for key,value in info.items():
    print(f"The {key} is {value}")
