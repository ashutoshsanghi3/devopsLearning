import re
string = "Good morning all,Kerala is good and the trivandrum is good and the UST is also good"
match = re.search("Morning",string,re.I) #re.I is for case insensitive
# match = re.match("Morning",string,re.I)
# match = re.findall("Morning",string,re.I)
# print(match)
# if match:
#     print("Matching",match.group(0))

match1 =re.findall("(?i)Morning",string)
# print(match1)
# match2=re.findall("good.morning",string,re.I | re.DOTALL)
# print(match2)
match2=re.findall("good",string,re.I | re.DOTALL)
# print(match2)
match3=re.search("good.morning",string,re.I | re.DOTALL)
# print(match3)
# myspan=match3.span()
# print(myspan)
l=[]
for i in re.finditer(re.escape("good"),string,re.I):
    l.append(i.span())
    # print(i)
# print(l)

match4=re.sub("(?i)good","Awesome",string)
# print(match4)

string1='''Hi
Hello
Welcome'''
match5=re.split("\n",string1)
# print(match5)

pattern='[K].*'  #starts from K and every character after that
pattern1='[t].*[g]'
match6=re.findall(pattern,string)
match6_1=re.findall(pattern1,string)
print(match6)
print(match6_1)