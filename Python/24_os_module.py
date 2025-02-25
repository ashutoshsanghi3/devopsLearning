import os
print("Current Working Directory: ",os.getcwd())
try:
    f=open("file1.txt")
    # print(f.read())
    # print(type(f.readline()))
    # print(f.readlines())
    # print(type(f.readlines()))
    os.remove("file2.txt")
finally:
    f.close()
