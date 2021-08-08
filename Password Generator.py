def fib():

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


num = int(input("enter number here :"))
for i in fib():

    if i > num:
        break

    print(i)
