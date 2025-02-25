import re
file=input("Enter file path: ")
f=open(file)
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
pattern="[\\w._]+@[\\w*]*+.[\\w]*"
l=[]
for i in f.readlines():
    match=re.findall(pattern,i)
    if match:
        l.append(match)
        print(match)
    
print(l)