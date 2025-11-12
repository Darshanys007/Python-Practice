import os
# if(not os.path.exists("Tutorial")):
#     os.mkdir("Tutorial")

for i in range(1,100):
    os.rename(f"Tutorial/PART{i}",f"Tutorial/Class{i}")

# os.mkdir("Tutorial")
# os.rmdir("Tutorial")
# os.makedirs("OS/OS Modules")
# os.removedirs("OS/OS Modules")