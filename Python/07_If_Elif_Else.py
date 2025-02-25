num=int(input("please enter a number: "))
# if num>10:
#     print(f"{num} is greater than 10")
# elif num<10:
#     print(f"{num} is less than 10")
# else:
#     print(f"{num} is equal to 10")

i=1
while i<=10:
    if i==5:
        i+=1
        continue
    print(num*i)
    i+=1
else:
    print("table printing done")

