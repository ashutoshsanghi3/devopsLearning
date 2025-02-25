s1="devops"
s2="batch"
s3="2"

s=s1+" "+s2+" "+s3
print(s)

print(len(s)) #print length of string
print(s.upper().find("B"))  #convert string to uppercase and find B
print(s[1:]) #remove first letter of string
print(s.split(" ")[0]) #get first word of string
print(s[len(s)-1]) #get last word of string
print(len(s)-1) #get index of last character in string
print(s.index(s[-1])) #s[-1] will give character of last index so 
                        #it will return index of last character in string