MultilineString='''I am in life.
Yes this is life.
Hi how are you'''

# print(MultilineString)

FName="Ashutosh"
LName="Sanghi"
# print(FName + ' ' + LName)
# print(len(FName + ' ' + LName))


str='I am in life.\nYes this is life.\tWe don\'t have saturday off'
# print(str)

pi=22/7
r=4
circle=pi*r**2
# print(circle)

# num = 2
# for i in range(1,11):
#     #  f-string, which allows you to embed expressions inside a string.
#     print(f"{num} * {i} = {num*i}")

#for going from 0 to len
# length=len(str)
# for i in range(0,length):
#     print(str[i],end=" ") #end will not make it into next line

#for going from len to 0
# length=len(str)*-1
# for i in range(-1,length,-1): # the last -1 will decrement 1 instead of incrementing 1 ,
#                                 #now it will decrease from -1 to -length
#     print(str[i],end=" ") #end will not make it into next line

str='I am in life.\nYes this is life.hi\tWe don\'t have saturday off'
FirstThreeChar=str[0:3]  #substring from 0 to 3-1 characters 
# print(FirstThreeChar)

EveryThirdChar=str[::3] #it will print every third character
# print(EveryThirdChar)

ReversedString=str[::-1]  #it will reverse the string
# print(ReversedString)

skipChar=str[3:] #it will skip first three characters
# print(skipChar)

gapinstring=str[0:10:2]  #it will print first 0-9 charcaters with 2-1 gap in between 
# print(gapinstring)

str='I am in life.\nYes this is life.hi \t We don\'t have saturday off'
# print(str.count('life'))  #it will return the number of occurences
# print(str.endswith('off'))  #it will return true or false 
# print(str.endswith(''))

# print(str.find('life')) # returns the position of character from starting
# print(str.rfind('life')) # returns the position of character from right side

# print(str.expandtabs(20)) # it will expand the size of \t 

s="Hello how are you are doing"
# x=s.index('how')
x=s.index('are',11) #it will start from 11 to check but it will count from starting only
# print(x)
s1="hi123"
s2="1242312"
# print(s.isalnum())  #s has space as special character so returns false
# print(s1.isalnum())
# print(s2.isalnum()) #only alphabet or numbers are considered in alnum
# print(s2.isalpha())
# print(s2.isdecimal())  #check for only numbers

s3="\u00b2"
s4="10\u00b2"

# print(s4.isdecimal()) #check for only numbers
# print(s3)
# print(s3.isdigit())
# print(s3.isnumeric())  #check for numbers,roman numbers,arabian numbers,fractions
# print(s4.isdigit())  #check for subscripts,superscripts,numbers etc.
# print(s4.isnumeric())
s4="hiall"
# print(s4.isidentifier())
# print(s4.islower())
s4="     HI ALL        "
# print(s4.isupper())
a=["hi","how","are","youa"]

# print("?".join(a))
# print(s4.strip())  #it will remove leading and trailing whitespaces
s5=(" ".join(a))
print(s5)
# print(s5.strip("ha")) #it will remove leading and trailing ha characters
# print(s5.split(" ")) #it will split the string based on the specified character eg. " "
# print(s5.title()) #capitalize first letter of every word
# print(s5.swapcase())#Convert uppercase characters to lowercase 
                    # and lowercase characters to uppercase.
print(s5.replace("are","cold"))
print(s5.startswith("hi"))

