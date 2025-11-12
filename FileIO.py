#READING A FILE
# f = open('myfile.txt','r')
# # print(f)
# text = f.read()
# print(text)

# f = open('photo.jpg','rb')
# print(f)
# text = f.read()
# print(text)

# WRITING A FILE
# f = open('myfile2.txt','w')
# f.write("Hello world!")
# f.close()

f = open('myfile2.txt','a')
f.write("Hello world!")
f.close()

# f = open('myfile3.txt','w')
# f.write("Hello world!")
# f.close()

# with open('myfile','r') as f:
#     text = f.read()
#     print(text)

with open('file4.txt','r') as f:
    print(type(f))
    f.seek(10) #Move to the 10th byte in the file

    print(f.tell()) #Returns the current position within the file, in bytes  #10
    data = f.read(5) #Read the next 5 bytes  #Eleven Tweleve Thirteen Fourteen Fifteen
    print(data)