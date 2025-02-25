def sum_num(x):
    return sum(x)
def higher_orderfunction (f,lis):
    var = f(lis)
    return var
result = higher_orderfunction(sum_num,[1,2,3,4,5])
print(result)

def square(x):
    return x**2
def cube(a):
    return a**3
def absolute(b):
    if b >= 0:
        return b
    else:
        return -(b)
    

def hof(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    else:
        return absolute

res=hof('absolute')
print(res(-5))