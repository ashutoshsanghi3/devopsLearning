def hello_world():
    print("Hello World")

# hello_world()

def hello_world(message):
    print(message)

# hello_world("This is hello")

def hello_world(nums):
    sum=0
    for i in nums:
        sum+=i 
    print(sum)

# hello_world([1,2,3,4,5])

def check_prime(num):
    for i in range(2,num//2):
        if num%i==0:
            print("not prime")
            return
    print("prime")

# check_prime(17)

def first_repeating_number(nums):
    store=set()
    for i in nums:
        if(i in store):
            return i
        store.add(i)
    return -1

# print(first_repeating_number([2,4,5,3,2,3]))

def f(fname,lname):
    return fname+" "+lname


def sum_of_two_numbers(a,b):
    return a+b


person = {
    "fname":"Ashutosh",
    "lname":"Sanghi",
    "uid":291197,
    "years":[2024,2025],
    "skills":{
        "backend_tech":["nodejs","expressjs"],
        "databases":["mysql","postgress","h2"]
    }}

