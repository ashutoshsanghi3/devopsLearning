try:
    print(10+50)
    # print(10+'50')
    print(50/0)

except TypeError:
    print("something went wrong")

except ValueError:
    print("something went wrong")

except ZeroDivisionError:
    print("this is zero division error")